from telegram import Update
from telegram.ext import ApplicationBuilder, ContextTypes, CommandHandler
import time
import os
TOKEN = os.getenv('BOT_TOKEN')


# start command
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await context.bot.send_message(chat_id=update.effective_chat.id, text="Hi there! I'm Guptchar Gupta 🕵️📡\n/help to get help")

# help command
async def help(update: Update,context: ContextTypes.DEFAULT_TYPE):
    await context.bot.send_message(chat_id=update.effective_chat.id, text="Commands:\n/start: to start the bot\n/help: to get help\n/scan: to initiate a scan instance")

# scan command
async def scan(update: Update,context: ContextTypes.DEFAULT_TYPE):    # initiate scan
    await context.bot.send_message(chat_id=update.effective_chat.id, text="Scan initiated 🔍")
    await context.bot.send_message(chat_id=update.effective_chat.id, text="Wait 5 seconds please......")
    time.sleep(5.0)
    await context.bot.send_photo(chat_id=update.effective_chat.id, photo='./processing/image.png')
    with open("./processing/data.txt", 'r') as file:
        lines = file.readlines()
        angle = lines[0].strip()  # first line of data.txt
        distance = str(int(lines[1].strip()) - 25)  # second line of data.txt - 25
        data_string = f"angle = {angle}, distance = {distance}"
    await context.bot.send_message(chat_id=update.effective_chat.id, text=data_string)




if __name__ == '__main__':
    app = ApplicationBuilder().token(TOKEN).build()
    
    start_handler = CommandHandler('start', start)
    help_handler = CommandHandler('help', help)
    scan_handler = CommandHandler('scan', scan)

    app.add_handlers([start_handler, help_handler, scan_handler])

    app.run_polling()

