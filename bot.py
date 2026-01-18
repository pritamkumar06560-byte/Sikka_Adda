from telegram.ext import Updater, CommandHandler
import time

TOKEN = "8030650064:AAFQbsp1DqvS98e4ptstNdItB3dYyo7IPFE"
ADMIN_ID = 7801717222  # apna telegram numeric id

START_TIME = 1768754187
DAYS_LIMIT = 10

def expired():
    return time.time() > START_TIME + (DAYS_LIMIT * 86400)

def start(update, context):
    if expired():
        update.message.reply_text("⛔ Bot campaign end ho chuka hai.")
        return
    update.message.reply_text(
        "Welcome 👋\n"
        "10 din ka Refer & Earn Bot\n\n"
        "/balance – Balance dekho"
    )

def balance(update, context):
    if expired():
        update.message.reply_text("⛔ Campaign over.")
        return
    update.message.reply_text("Your balance: 0 coins")

def main():
    updater = Updater(TOKEN, use_context=True)
    dp = updater.dispatcher

    dp.add_handler(CommandHandler("start", start))
    dp.add_handler(CommandHandler("balance", balance))

    updater.start_polling()
    updater.idle()

main()
