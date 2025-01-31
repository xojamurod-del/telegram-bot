import wikipediaapi
from telegram import Update
from telegram.ext import Application, CommandHandler, MessageHandler, filters, CallbackContext

# API Token
TELEGRAM_API_TOKEN = "5877849504:AAGWxOWyBAtJzbewgdKN8wgqfMMcwNd4TSg"  # O'z tokeningizni qo'ying

# Wikipedia API obyektini yaratish
def create_wiki(lang='uz'):
    """Wikipedia obyektini yaratish"""
    user_agent = "WikipediaBot/1.0 (https://yourbotwebsite.com; your_email@example.com)"  # O'zingizga mos qilib o'zgartiring
    return wikipediaapi.Wikipedia(user_agent=user_agent, language=lang)

async def start(update: Update, context: CallbackContext):
    """ /start buyrug'iga javob """
    await update.message.reply_text("Assalomu alaykum! Men Wikipedia botiman. Menga mavzu yuboring.")

async def handle_message(update: Update, context: CallbackContext):
    """ Foydalanuvchi xabariga javob """
    text = update.message.text
    wiki_wiki = create_wiki('uz')  # O'zbekcha Wikipedia
    page = wiki_wiki.page(text)
    
    if page.exists():
        await update.message.reply_text(page.summary[:4000])  # Telegram cheklovidan oshmaslik uchun
    else:
        await update.message.reply_text(f"'{text}' mavzusi topilmadi.")

def main():
    """ Botni ishga tushirish """
    app = Application.builder().token(TELEGRAM_API_TOKEN).build()

    # Buyruqlar va xabarlar uchun handler qo'shish
    app.add_handler(CommandHandler("start", start))
    app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, handle_message))

    # Botni ishga tushirish
    print("Bot ishga tushdi...")
    app.run_polling()

if __name__ == "__main__":
    main()
