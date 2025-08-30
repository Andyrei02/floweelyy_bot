from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton


main_menu_kb = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text="Despre noi", callback_data="about_us")]
])

# about_kb = InlineKeyboardMarkup(inline_keyboard=[
#     [
#         InlineKeyboardButton(text="Instagram", url="https://www.instagram.com/floweelyy"),
#         InlineKeyboardButton(text="📍 Locatie", url="https://maps.app.goo.gl/mmAZ2gvBEdGsFWk18")
#     ]
# ])
