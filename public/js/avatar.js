// public/js/avatar.js

(() => {
  const ENDPOINTS = {
    token: '/api/streaming/token',
    session: '/api/streaming/session',
    start: '/api/streaming/start',
    stop: '/api/streaming/stop'
  };

  const refs = {
    video: document.getElementById('avatar-video'),
    toggle: document.getElementById('avatar-toggle')
  };

  // Общий объект для доступа из chat.js
  window.avatarStream = {
    enabled: false,
    token: null,
    sessionId: null,
    room: null,
    mediaStream: null
  };

  function updateToggleColour() {
    refs.toggle.classList.toggle('on', window.avatarStream.enabled);
    refs.toggle.classList.toggle('off', !window.avatarStream.enabled);
  }

  function showSpinner(mode) {
    const txt = mode === 'connect'
      ? refs.toggle.dataset.connect
      : refs.toggle.dataset.disconnect;
    refs.toggle.dataset.prev = refs.toggle.textContent;
    refs.toggle.innerHTML = `<span class="spinner"></span>${txt}`;
    refs.toggle.disabled = true;
    refs.toggle.classList.remove('on', 'off');
  }

  function hideSpinner() {
    refs.toggle.textContent = refs.toggle.dataset.prev || 'АВАТАР';
    refs.toggle.disabled = false;
    updateToggleColour();
  }

  function bindLiveKit(room) {
    const mediaStream = new MediaStream();
    window.avatarStream.mediaStream = mediaStream;
    refs.video.srcObject = mediaStream;

    room.on(LivekitClient.RoomEvent.TrackSubscribed, track => {
      if (track.mediaStreamTrack.kind === 'video' || track.mediaStreamTrack.kind === 'audio') {
        mediaStream.addTrack(track.mediaStreamTrack);
      }
    });

    room.on(LivekitClient.RoomEvent.TrackUnsubscribed, track => {
      mediaStream.getTracks()
        .filter(t => t === track.mediaStreamTrack)
        .forEach(t => mediaStream.removeTrack(t));
    });
  }

  async function startAvatar() {
    showSpinner('connect');
    try {
      // Получаем токен и сохраняем его
      const { token } = await fetch(ENDPOINTS.token, { method: 'POST' }).then(r => r.json());
      window.avatarStream.token = token;

      // Создаём новую сессию
      const sess = await fetch(
        `${ENDPOINTS.session}?token=${encodeURIComponent(token)}`,
        {
          method: 'POST',
          headers: { 'Content-Type': 'application/json' },
          body: JSON.stringify({})
        }
      ).then(r => r.json());
      window.avatarStream.sessionId = sess.session_id;

      // Запускаем аватара на сервере
      await fetch(
        `${ENDPOINTS.start}?token=${encodeURIComponent(token)}`,
        {
          method: 'POST',
          headers: { 'Content-Type': 'application/json' },
          body: JSON.stringify({ session_id: sess.session_id })
        }
      );

      // Флаг 'готовности' ставим сразу после старта сессии нужна для чата
      window.avatarStream.enabled = true;

      // Настраиваем и коннектимся к LiveKit
      window.avatarStream.room = new LivekitClient.Room({ adaptiveStream: true, dynacast: true });
      bindLiveKit(window.avatarStream.room);
      await window.avatarStream.room.connect(sess.url, sess.access_token);

      // Разблокируем автоплей аудио при первой подписке
      window.avatarStream.room.once(LivekitClient.RoomEvent.TrackSubscribed, track => {
        if (track.mediaStreamTrack.kind === 'audio') {
          refs.video.muted = false;
          refs.video.play().catch(() => {});
        }
      });
    } catch (e) {
      console.error('Avatar start error:', e);
      alert('Не удалось запустить аватара.');
      // откатим флаг в случае ошибки
      window.avatarStream.enabled = false;
    } finally {
      hideSpinner();
    }
  }

  async function stopAvatar() {
    showSpinner('disconnect');
    try {
      window.avatarStream.room?.disconnect();
      await fetch(
        `${ENDPOINTS.stop}?token=${encodeURIComponent(window.avatarStream.token)}`,
        {
          method: 'POST',
          headers: { 'Content-Type': 'application/json' },
          body: JSON.stringify({ session_id: window.avatarStream.sessionId })
        }
      );
    } catch (e) {
      console.warn('Avatar stop error:', e);
    } finally {
      // Сброс всех данных
      refs.video.srcObject = null;
      refs.video.load();
      window.avatarStream = { enabled: false, token: null, sessionId: null, room: null, mediaStream: null };
      hideSpinner();
    }
  }

  // отвечает за включение и выключение аватара
  refs.toggle.addEventListener('click', () => {
    if (window.avatarStream.enabled) {
      stopAvatar();
    } else {
      startAvatar();
    }
  });

  // меняем цвет кнопки при включении-выключении аватара
  updateToggleColour();
})();
