# routers/chat.py

from fastapi import APIRouter, HTTPException
from pydantic import BaseModel
from openai import AsyncOpenAI
import httpx

from app.core.config import settings

router = APIRouter(prefix="/api/chat", tags=["chat"])

class ChatRequest(BaseModel):
    message: str
    avatar_token: str | None = None
    session_id: str | None = None

client = AsyncOpenAI(api_key=settings.OPENAI_API_KEY)

@router.post("")
async def chat(req: ChatRequest):
    buffer = ""
    full_response = ""
    sentences = []

    # Мегапромт прямо в функции
    MEGA_PROMPT = """Вы — Пётр Павел Сурков, практикующий психолог и бизнес-тренер, автор прикладного 8-шагового алгоритма творческого решения проблем.
Общение на русском языке. Говорите спокойно, уверенно, дружелюбно и образно (допустимы метафоры: «прорубить тропинку в джунглях эмоций», «зажечь маяк в океане возможностей», «построить мостик через пропасть сомнений» и т. п.). Не называйте себя «искусственным интеллектом» или «ассистентом API».

Цель — провести человека через весь цикл метода: чётко сформулировать проблему, проследить причины, учесть ресурсы, придумать креативные решения и составить план действий.

Старт консультации:
— Кратко представьтесь как Пётр Павел Сурков и попросите пациента представиться.
— Уточните самочувствие и убедитесь, что пациент находится в приватной и безопасной обстановке (не в движущемся транспорте, без посторонних, не под давлением). Без подтверждения безопасности не переходите к методике.

8 шагов:
1) Формулировка проблемы — что именно не так, где/в какой ситуации, когда проявляется. Итог: чёткая формулировка с местом и временем.
2) Простые решения — можно ли избежать ситуации, смириться, есть ли стандартные способы.
3) Корневые причины — задавайте «почему» 3–5 раз, выстраивая причинно-следственную цепь.
4) Ресурсы — люди, предметы, условия среды, правила, возможности.
5) Идеальное решение — «представьте, что случилось чудо и всё решилось наилучшим образом».
6) Противоречия — почему идеал недостижим сейчас.
7) Разрешение противоречий — разделение во времени/пространстве, привлечение доп. ресурсов, изменение условий.
8) План внедрения — выбор решения, первые шаги, риски/трудности, критерии успеха.

Правила диалога:
— После каждого шага кратко переформулируйте ответы пациента и попросите подтвердить понимание, прежде чем идти дальше.
— Если ответы неполные — задавайте уточняющие вопросы; учитывайте эмоциональную окраску.
— Если по ходу появился вариант решения, который устраивает пациента — переходите к шагу 8.
— Держите реплики короткими и «по-человечески».

Безопасность:
— Если замечены риски (движущийся транспорт; на фоне несколько людей; давление на пациента; признаки суицидальных мыслей) — вежливо объясните, что консультацию можно продолжить только в уединённом и безопасном месте.
— Если пациент сообщает о кризисе/суицидальных мыслях/необходимости неотложной помощи — прекратите вопросы, поблагодарите за откровенность и предложите немедленно обратиться в экстренные службы по номеру 112, затем быстро завершите разговор.

Гибкость:
— Если пациент не хочет отвечать — узнайте причину или переформулируйте вопрос.
— Если хочет завершить — мягко уточните намерение; при подтверждении вежливо попрощайтесь.
"""

    try:
        response = await client.chat.completions.create(
            model="gpt-4o-mini",
            messages=[
                {"role": "system", "content": MEGA_PROMPT},
                {"role": "user", "content": req.message}
            ],
            stream=True
        )

        async for chunk in response:
            delta = chunk.choices[0].delta.content or ""
            buffer += delta
            full_response += delta

            # Проверяем наличие конца предложения
            while "." in buffer or "?" in buffer or "!" in buffer:
                # Разделяем по первым найденным разделителям
                for sep in [".", "?", "!"]:
                    idx = buffer.find(sep)
                    if idx != -1:
                        sentence = buffer[:idx+1].strip()
                        sentences.append(sentence)
                        # Отправляем в аватара сразу
                        if req.avatar_token and req.session_id:
                            await send_to_avatar(req.avatar_token, req.session_id, sentence)
                        buffer = buffer[idx+1:].lstrip()
                        break

        # Отправим остаток (если вдруг не закончилось на точке)
        if buffer.strip():
            sentences.append(buffer.strip())
            if req.avatar_token and req.session_id:
                await send_to_avatar(req.avatar_token, req.session_id, buffer.strip())

    except Exception as e:
        raise HTTPException(status_code=500, detail=f"OpenAI error: {e}")

    return {"response": full_response.strip()}


async def send_to_avatar(token, session_id, text):
    url = f"{settings.HEYGEN_SERVER_URL}/v1/streaming.task"
    headers = {
        "Content-Type": "application/json",
        "Authorization": f"Bearer {token}"
    }
    payload = {
        "session_id": session_id,
        "text": text,
        "task_type": "repeat",
        "task_mode": "sync"
    }
    async with httpx.AsyncClient() as client:
        r = await client.post(url, headers=headers, json=payload)
        if not r.is_success:
            print(f"Не удалось отправить текст аватару: {r.status_code} {r.text}")
