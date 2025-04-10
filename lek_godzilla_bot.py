from telegram import Update, Bot
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters, CallbackContext
import logging
import random

# === CONFIG ===
TOKEN = "8064847863:AAG3ruw0U3jV0FruQCrtWuN32y340zkuNYU"
lek_god_respostas = [
    "Fala tu, chefia 😈 Aqui é o LEK GODZILLA na escuta... o que tu quer dominar hoje?",
    "Tu mandou isso aí, mas já pensou em como transformar isso em dinheiro hoje? 💸",
    "Rapaz... tu tá cutucando o monstro certo. Manda a visão completa. 👊",
    "Se for pra ganhar grana com isso, eu tô dentro. Desenvolve aí. 😎",
    "Lek GODZILLA ativado, parceiro. Tô pronto pra devorar a internet contigo. 🌐🔥"
]

# === LOG ===
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO)

# === HANDLERS ===
def start(update: Update, context: CallbackContext) -> None:
    update.message.reply_text("👑 Salve! Tu ativou o LEK GODZILLA. Me manda tua dúvida ou missão digital e vamo começar a quebrar tudo!")

def reply(update: Update, context: CallbackContext) -> None:
    msg = update.message.text
    resposta = random.choice(lek_god_respostas)
    update.message.reply_text(resposta)

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
