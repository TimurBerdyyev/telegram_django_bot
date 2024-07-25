import os
from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import Updater, CommandHandler, CallbackQueryHandler, CallbackContext
from dotenv import load_dotenv
from .token import BOT_TOKEN


def start(update: Update, context: CallbackContext):
    keyboard = [
        [InlineKeyboardButton('рпоцедуры', callback_data='процедуры')],
        [InlineKeyboardButton('салоны', callback_data='салон')],
        [InlineKeyboardButton('мастера', callback_data='мастер')],
        [InlineKeyboardButton('о нас', callback_data='хотите узнать о нас '),
         InlineKeyboardButton('связь с менеджером', callback_data='контакты менеджера')]
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)
    update.message.reply_text('Выберите опцию:', 
                              reply_markup=reply_markup)
    

def button(update: Update, context: CallbackContext):
    query = update.callback_query
    query.answer()
    query.edit_message_text(text=f'вы выбоали :{query.data}')


def main():
    updater = Updater(BOT_TOKEN, use_context=True)
    updater.dispatcher.add_handler(CommandHandler('start', start))
    updater.dispatcher.add_handler(CallbackQueryHandler(button))
    updater.start_polling()
    updater.idle()


if __name__ == '__main__':
    load_dotenv()
    main()