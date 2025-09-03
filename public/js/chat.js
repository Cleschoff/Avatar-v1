// public/js/chat.js

(() => {
  const ENDPOINTS = {
    chat: '/api/chat',
    streamTask: '/api/streaming/task'
  };

  const refs = {
    input: document.getElementById('message-input'),
    send: document.getElementById('send-button'),
    chat: document.getElementById('chat-container')
  };

  /**
   * Добавляет сообщение в окно чата
   * @param {string} text — текст сообщения
   * @param {'user'|'bot'} cls — CSS-класс для стиля сообщения
   */
  function addMessage(text, cls) {
    const msgEl = document.createElement('div');
    msgEl.className = `message ${cls}`;
    msgEl.textContent = text;
    refs.chat.appendChild(msgEl);
    refs.chat.scrollTop = refs.chat.scrollHeight;
  }

  /**
   * Отправка сообщения на сервер и озвучка аватаром (если включён)
   * @param {string} [forcedText] — текст для отправки вместо input
   */
  async function sendMessage(forcedText) {
    const raw = forcedText ?? refs.input.value;
    const msg = raw.trim();
    if (!msg) return;

    // 1) Отображаем своё сообщение
    console.debug('[Chat] User message:', msg);
    addMessage(msg, 'user');
    if (!forcedText) refs.input.value = '';

    refs.send.disabled = true;

    try {
      // 2) Запрос к чат-API
      console.debug('[Chat] Sending to /api/chat:', msg);
      const res = await fetch(ENDPOINTS.chat, {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({ message: msg })
      });
      if (!res.ok) throw new Error(`HTTP ${res.status}`);
      const { response } = await res.json();

      const botText = response || '(нет ответа)';
      console.debug('[Chat] Bot response:', botText);
      addMessage(botText, 'bot');

      // 3) Логируем состояние avatarStream перед попыткой отправки таска
      console.debug('[Avatar] State before task:', {
        enabled: window.avatarStream?.enabled,
        sessionId: window.avatarStream?.sessionId,
        token: window.avatarStream?.token
      });

      // 4) Если аватар запущен — шлём задачу на озвучку
      if (window.avatarStream?.enabled && window.avatarStream.sessionId) {
        console.debug('[Avatar] Sending task to /api/streaming/task');
        try {
          const taskRes = await fetch(
            `${ENDPOINTS.streamTask}?token=${encodeURIComponent(window.avatarStream.token)}`,
            {
              method: 'POST',
              headers: { 'Content-Type': 'application/json' },
              body: JSON.stringify({
                session_id: window.avatarStream.sessionId,
                text: botText,
                task_type: 'repeat',
                task_mode: 'sync'
              })
            }
          );
          console.debug('[Avatar] Task response status:', taskRes.status);
          if (!taskRes.ok) {
            const errText = await taskRes.text();
            console.error('[Avatar] Task error body:', errText);
          }
        } catch (err) {
          console.error('[Avatar] Fetch task error:', err);
        }
      } else {
        console.warn('[Avatar] Skip task: avatarStream not ready');
      }

    } catch (err) {
      console.error('[Chat] Ошибка соединения или обработки:', err);
      addMessage('Ошибка соединения', 'bot');
    } finally {
      refs.send.disabled = false;
    }
  }

  // Доступно для transcribe.js автосендера (присваивается глобальному объекту window)
  window.sendMessage = sendMessage;

  // Обработчики UI
  refs.send.addEventListener('click', () => sendMessage());
  refs.input.addEventListener('keypress', e => {if (e.key === 'Enter') sendMessage();
  });
})();
