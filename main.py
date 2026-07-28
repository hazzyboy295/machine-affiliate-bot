from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes
import os

# 1. BOT TOKEN - Replace with your token
BOT_TOKEN = "PASTE_YOUR_BOT_TOKEN_HERE"

# 2. Fake user data for now. Replace this with your database later
user = {'name': 'User', 'balance': 0, 'referrals': 0}

# 3. /start and /account command
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        f"👤 My Account\n"
        f"Name: {user['name']}\n"
        f"Balance: ₦{user['balance']}\n"
        f"Referrals: {user['referrals']}"
    )

async def account(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        f"👤 My Account\n\n"
        f"Name: {user['name']}\n"
        f"Balance: ₦{user['balance']}\n"
        f"Referrals: {user['referrals']}"
    )

# 4. /referral command
async def referral(update: Update, context: ContextTypes.DEFAULT_TYPE):
    bot_username = "MachineAffiliateBot"  # <-- change to your bot username
    user_id = update.effective_user.id
    
    await update.message.reply_text(
        f"Your referral link:\nhttps://t.me/{bot_username}?start={user_id}"
    )

# 5. /support command - THIS WAS THE ERROR LINE
async def support(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "Contact Admin: @YourTelegramUser"  # <-- change to your username
    )

# 6. RUN THE BOT
def main():
    app = ApplicationBuilder().token(BOT_TOKEN).build()

    app.add_handler(CommandHandler("start", start))
    app.add_handler(CommandHandler("account", account))
    app.add_handler(CommandHandler("referral", referral))
    app.add_handler(CommandHandler("support", support))

    print("Bot Started...")
    app.run_polling()

if __name__ == "__main__":
    main()
"Contact Admin: @YourTelegramUser"
