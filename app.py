from flask import Flask, request
from telegram import Update
from telegram.ext import Application, CommandHandler
import config

# Flask app for webhook
app = Flask(__name__)

# Initialize Telegram bot
application = Application.builder().token(config.BOT_TOKEN).build()

# --- Command Handlers ---
async def start(update: Update, context):
    await update.message.reply_text(
        "Welcome to SolInvestAI Bot 🚀\n\n"
        "Here’s what I can do:\n"
        "🔹 /autoinvest – Buy crypto automatically\n"
        "🔹 /p2p – Peer-to-peer transactions\n"
        "🔹 /trade – Manage trades\n"
        "🔹 /automation – Set up recurring tasks"
    )

async def autoinvest(update: Update, context):
    await update.message.reply_text("Auto Invest 💹\nEnter the amount & frequency you’d like to invest.")

async def p2p(update: Update, context):
    await update.message.reply_text("P2P 🤝\nProvide details of what you want to buy/sell.")

async def trade(update: Update, context):
    await update.message.reply_text("Trade 📊\nPlease enter your trade details.")

async def automation(update: Update, context):
    await update.message.reply_text(
        "Automation ⚙️\nOptions:\n"
        "1️⃣ Schedule recurring investments\n"
        "2️⃣ Set price alerts\n"
        "3️⃣ Enable wallet balance alerts"
    )

# Add handlers
application.add_handler(CommandHandler("start", start))
application.add_handler(CommandHandler("autoinvest", autoinvest))
application.add_handler(CommandHandler("p2p", p2p))
application.add_handler(CommandHandler("trade", trade))
application.add_handler(CommandHandler("automation", automation))

# --- Flask route for Telegram Webhook ---
@app.route("/", methods=["POST"])
def webhook():
    update = Update.de_json(request.get_json(force=True), application.bot)
    application.update_queue.put_nowait(update)
    return "ok", 200

# --- Flask test route ---
@app.route("/")
def home():
    return "SolInvestAI Bot is running!", 200

# Run locally (Render will use gunicorn)
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
