from aiogram import Router, types
from aiogram.filters import Command

from utils.users import save_user
from keyboards import main_menu


router = Router()
text = f"\
Bun venit la 🌸 <b>Floweelyy!</b> 🌸 \n\
Creăm buchete cu dragoste și grijă - doar pentru tine. \n\
Permite-ne să te ajutăm să găsești buchetul perfect pentru orice moment 💐\
"

@router.message(Command("start"))
async def cmd_start(message: types.Message):
    await save_user(message.from_user)
    await message.answer_photo(
        photo="https://instagram.fkiv9-1.fna.fbcdn.net/v/t51.2885-19/447756338_825854359024203_3334144817659439619_n.jpg?efg=eyJ2ZW5jb2RlX3RhZyI6InByb2ZpbGVfcGljLmRqYW5nby40ODYuYzIifQ&_nc_ht=instagram.fkiv9-1.fna.fbcdn.net&_nc_cat=103&_nc_oc=Q6cZ2QFK3wqsLVBwKbfTM0aZwKGk177ent7ZT2_DAZPNMmEDFFArw0M3PTtWc9QV6mDrrB4&_nc_ohc=XAHO67yGdqAQ7kNvwHErm0h&_nc_gid=lH1Mm6RnBcX5FBiFY7XBVQ&edm=APoiHPcBAAAA&ccb=7-5&oh=00_AfVr3Crbjp8plUKdJd3mvPxHxbiyl757QIXRVqT4hX3Y8A&oe=68B28955&_nc_sid=22de04",
        caption=f"<b>Salut {message.from_user.first_name}</b>\n {text}",
        reply_markup=main_menu.main_menu_kb
    )
