from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes

BOT_TOKEN = "PASTE_YOUR_BOT_TOKEN_HERE"

users = {}

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user = update.effective_user

    if user.id not in users:
        users[user.id] = {
            "name": user.first_name,
            "balance": 0,
            "referrals": 0
        }

    text = f"""
👋 Welcome {user.first_name}

Welcome to Machine Affiliate Bot

Commands:
/account - My Account
/referral - My Referral Link
/support - Support
"""

    await update.message.reply_text(text)

async def account(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user = users.get(update.effective_user.id)

    if not user:
        await update.message.reply_text("Please use /start first.")
        return

    await update.message.reply_text(
        f"""👤 My Account

Name: {user['name']}
Balance: ₦{user['balance']}
Referrals: {user['referrals']}
"""
    )

async def referral(update: Update, context: ContextTypes.DEFAULT_TYPE):
    bot_username = "MachineAffiliateBot"
    user_id = update.effective_user.id

    await update.message.reply_text(
        f"Your referral link:\nhttps://t.me/{bot_username}?start={user_id}"
    )

async def support(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "Contact Admin: @YourTelegramUser
   "Contact Admin: @YourTelegramUser")     
        
   app = ApplicationBuilder().token(BOT_TOKEN).build()

app.add_handler(CommandHandler("start", start))
app.add_handler(CommandHandler("account", account))
app.add_handler(CommandHandler("referral", referral))
app.add_handler(CommandHandler("support", support))

print("Bot Started...")
app.run_polling()
