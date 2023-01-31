from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes, CallbackQueryHandler
from bot_command import hi_command, time_command, help_command, sum_command, set_timer, unset, msg, xo, button


app = ApplicationBuilder().token("TOKEN").build()

app.add_handler(CommandHandler('hi', hi_command))
app.add_handler(CommandHandler('start', hi_command))
app.add_handler(CommandHandler('time', time_command))
app.add_handler(CommandHandler('help', help_command))
app.add_handler(CommandHandler('sum', sum_command))
app.add_handler(CommandHandler("set", set_timer))
app.add_handler(CommandHandler("unset", unset))
app.add_handler(CommandHandler("msg", msg))
app.add_handler(CommandHandler("xo", xo))
app.add_handler(CallbackQueryHandler(button))
app.run_polling()


