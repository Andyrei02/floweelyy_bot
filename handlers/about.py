from aiogram import F, Router, types


router = Router()

@router.callback_query(F.data == "about_us")
async def cmd_info(callback_query: types.CallbackQuery):
    await callback_query.message.answer(
"\n\
<b>🚚 Livrare</b> \n\
Livrare rapidă în Glodeni și zonele învecinate. \n\n\
<b>Urmăriți-ne</b> \n\
Instagram: <a href='https://www.instagram.com/floweelyy'>floweelyy</a> \n\n\
<b>📞 Contactați-ne</b> \n\
+37360239628 / +37360239628 \n\n\
<b>📍 Locație</b> \n\
<a href='https://maps.app.goo.gl/mmAZ2gvBEdGsFWk18'>Vasile Zgârcea 9, Glodeni</a> \n\n\
"
    )
