from flask import Flask
from telegram.ext import Application, CommandHandler
import config

app = Flask(__name__)

# Telegram bot setup
application = Application.builder().token(config.BOT_TOKEN).build()

# Command handler
async def start(update, context):
    await update.message.reply_text("Hello 👋! Bot is running successfully.")

application.add_handler(CommandHandler("start", start))

# Flask route
@app.route("/")
def home():
    return "Bot is alive!", 200

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
