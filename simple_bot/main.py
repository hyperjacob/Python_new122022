from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes
from bot_command import hi_command, time_command, help_command, sum_command


app = ApplicationBuilder().token("5839277268:AAFucI-ikmjHeVVmOd2C5oXSA1PYRk5tuYk").build()

app.add_handler(CommandHandler('hi', hi_command))
app.add_handler(CommandHandler('time', time_command))
app.add_handler(CommandHandler('help', help_command))
app.add_handler(CommandHandler('sum', sum_command))
app.run_polling()