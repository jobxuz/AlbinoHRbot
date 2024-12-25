# import logging
# from loader import db
# from aiogram import Dispatcher

# #from data.config import ADMINS
# #from handlers.users.admin import ADMINS
# ADMINS = db.select_all_admin_ids()


# async def on_startup_notify(dp: Dispatcher):
#     for admin in ADMINS:
#         try:
#             await dp.bot.send_message(admin, "Bot ishga tushdi")

#         except Exception as err:
#             logging.exception(err)
