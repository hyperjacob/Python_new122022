from telegram import Update
from telegram.ext import Updater, CommandHandler, CallbackContext import datetime from spy import *
def hi_command(update: Update, context: CallbackContext):
log(update, context)
update.message.reply_text(f'Hi {update.effective_user.first_name}!")
def help_command(update: Update, context: CallbackContext):
log(update, context)
update.message.reply_text(f'/hiln/time\n/help')
def time_command(update: Update, context: CallbackContext):
log(update, context)
update.message.reply_text(f'{datetime.datetime.now.time01)
def sum_command(update: Update, context: CallbackContext):
log(update, context)
msg = update.message.text
print(msg)
items = msg.split # / sum 123 534543
× = int(items[1])
y = int(items[21)
update.message.reply_text(f'{x} + {y] = {x+y!')
