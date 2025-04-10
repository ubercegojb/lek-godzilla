# LEK GODZILLA - Bot Telegram com IA Open-Source Integrada (via LM Studio)
# -----------------------------------------------
# Requisitos: python-telegram-bot, requests
# Subir em: Render.com, Replit.com ou local
# A IA deve estar rodando localmente via LM Studio (porta 1234, ou edita abaixo)

from telegram import Update
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters, CallbackContext
import logging
import requests

# === CONFIG ===
TOKEN = "8064847863:AAG3ruw0U3jV0FruQCrtWuN32y340zkuNYU"
LOCAL_AI_ENDPOINT = "http://localhost:1234/v1/completions"  # URL da IA local (LM Studio)
HEADERS = {"Content-Type": "application/json"}

# === LOG ===
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO)

# === FUNÇÃO: Conecta com a IA local ===
def perguntar_ai(prompt):
    payload = {
        "prompt": prompt,
        "max_tokens": 200,
        "temperature": 0.8,
        "stop": ["\n"],
    }
    try:
        response = requests.post(LOCAL_AI_ENDPOINT, json=payload, headers=HEADERS)
        if response.status_code == 200:
            result = response.json()
            return result.get("choices", [{}])[0].get("text", "Sem resposta da IA.")
        else:
            return f"Erro na IA (status {response.status_code})"
    except Exception as e:
        return f"Erro na conexão com a IA: {e}"

# === HANDLERS ===
def start(update: Update, context: CallbackContext) -> None:
    update.message.reply_text("👑 Salve! Tu ativou o LEK GODZILLA. Me manda tua dúvida ou missão digital e vamo começar a quebrar tudo!")

def reply(update: Update, context: CallbackContext) -> None:
    user_msg = update.message.text
    resposta_lek = perguntar_ai(user_msg)
    update.message.reply_text(resposta_lek)

# === MAIN ===
def main():
    updater = Updater(TOKEN)
    dispatcher = updater.dispatcher
    dispatcher.add_handler(CommandHandler("start", start))
    dispatcher.add_handler(MessageHandler(Filters.text & ~Filters.command, reply))
    updater.start_polling()
    updater.idle()

if __name__ == '__main__':
    main()
