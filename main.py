from string import capwords

from aiogram import Bot, Dispatcher, types, F
import asyncio
from aiogram.filters import Command
from aiogram.types import KeyboardButton, ReplyKeyboardMarkup


def menu():
    button = KeyboardButton(text="🏢Kompaniya Haqida")
    button2 = KeyboardButton(text="📍Filiallar")
    button3 = KeyboardButton(text="Bosh Ish O'rinlari")
    button5 = KeyboardButton(text="Menyu")
    button6 = KeyboardButton(text="Yangiliklar")
    button4 = KeyboardButton(text="📍Kantakt/Manzilimiz")
    button7 = KeyboardButton(text="USA/UZB Til")

    rkm = ReplyKeyboardMarkup(
        keyboard=[
            [button, button2],
            [button3],
            [button5, button6],
            [button4, button7]
        ],
        resize_keyboard=True
    )
    return rkm

def about_menu():
    button = KeyboardButton(text="Lavash")
    button2 = KeyboardButton(text="Mini hot-dog")
    button3 = KeyboardButton(text="Shaurma")
    button4 = KeyboardButton(text="Loonger")
    button5 = KeyboardButton(text="back")
    rkm = ReplyKeyboardMarkup(
        keyboard=[
            [button, button2],
            [button3, button4],
            [button5]
        ],
        resize_keyboard=True
    )
    return rkm

API_TOKEN = "8144083932:AAGEi3qw7dqW04FVAvSilBEVkSGUxcNv02E"
bot = Bot(token=API_TOKEN)
dp = Dispatcher()
image = "https://imageproxy.wolt.com/assets/680227bab89d06ee6f4fd65a"
pdp = "https://www.spot.uz/media/img/2023/12/TNWEkA17027458253420_l.jpg"
# m = "https://optim.tildacdn.one/tild3936-6131-4466-b266-313935643031/-/resize/460x/-/format/webp/224.png.webp"
# e = "https://optim.tildacdn.one/tild3866-6666-4463-b264-623834373665/-/resize/440x/-/format/webp/Frame_1000003424.png.webp"
# n = "https://optim.tildacdn.one/tild6537-6630-4332-b434-633063373836/-/resize/440x/-/format/webp/Frame_1350380468.png.webp"
# t = "https://optim.tildacdn.one/tild3162-3461-4639-b265-346665613839/-/resize/440x/-/format/webp/123333333.png.webp"
# mentor = [m, e, n, t]
# a = "https://storage.googleapis.com/star-lab/blog/OGs/python.png"
# b = "https://blog.geekster.in/wp-content/uploads/2023/05/Frontend-vs-Backend-Languages.webp"
# q = "https://images.twinkl.co.uk/tw1n/image/private/t_630/u/ux/02wchouritvxqgixxoeagap-2.fit-scale.size-760x427.v1569482197_ver_1.jpg"
# s = "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcS-qyyqPN_5Z-EM_fhMLtiM2lDmgfjyZ6YoEw&s"
# r = "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcQJPUPtK30F-coSkTGVGVKsNhMn36zWqVm_4FavYIAioJ1J2txIuCckiywhtjccR0VxRcg&usqp=CAU"
s = "https://www.spot.uz/media/img/2023/12/TNWEkA17027458253420_l.jpg"
i = "https://yukber.uz/image/cache/catalog/Shaurma-700x700.jpg"
v = "https://lefood.menu/wp-content/uploads/w_images/2023/07/recept-76707-1240x827.jpg"
q = "https://cdn.кухня.рф/recipe/27a53a0a-0c3d-4bc1-9023-e2b058fff43a.webp"
r = "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcSuz81rKYGM9ErG6GtHaz5zzp9E4Eii6cpTjg&s"

@dp.message(Command('start'))
async def send_start(message: types.Message):
    await message.answer_photo(
        photo=image,
        caption="Oqtepa Lavash botiga hush kelibsiz!",
        reply_markup=menu()
    )

@dp.message(F.text == '🏢Kompaniya Haqida')
async def send_start(message: types.Message):
    await message.answer_photo(
        photo=pdp,
        caption="Biz — Oqtepa Lavash, 2010-yilda Chilonzorda kichik bir kafeda “o‘zimizniki”lar uchun lavashlar tayyorlay boshlagan ikki aka-uka, Behzod va Farhod G‘ulomovlar tomonidan tashkil etilgan restoranlar tarmog‘imiz. Ammo “o‘zimiznikilar” uchun deb boshlangan bu tashabbus birgina tumanning chegarasidan ancha uzoqqa chiqib ketdi: bugungi kunda bizning O‘zbekistonning 11 ta shaharda 96 ta filialimiz bor va biz hali ham soddalik, sifat va mehmonlarga yaqinroq bo'lishga ishonamiz.",
        reply_markup=menu()
    )

@dp.message(F.text == '📍Filiallar')
async def send_start(message: types.Message):
    await message.answer_photo(photo=s, caption="Filiallarimiz juda ham kop masalan: Oxunboboyev,   Nukus2 va boshqa juda ham kop filiallar mavjud", reply_markup=menu())

@dp.message(F.text == 'Menyu')
async def send_start(message: types.Message):
    await message.answer("Menyuda koplab Oqtepa Lavashning fast foodlari mavjud", reply_markup=about_menu())

@dp.message(F.text == 'Yangiliklar')
async def send_start(message: types.Message):
    await message.answer("Tez orada Oqtepa lavashdan yangiliklar kuting", reply_markup=menu())

@dp.message(F.text == "Bosh Ish O'rinlari")
async def send_start(message: types.Message):
    await message.answer("Hozircha bosh ish o'rinlari mavjud emas!", reply_markup=menu())

@dp.message(F.text == 'Shaurma')
async def send_start(message: types.Message):
    await message.answer_photo(
        photo=i,
    caption="Shaurma narxi - 31.000",
        reply_markup=about_menu()
    )

@dp.message(F.text == 'Lavash')
async def send_start(message: types.Message):
    await message.answer_photo(
        photo=v,
      caption="Pishloqli katta lavash narxi - 55.000",
        reply_markup=about_menu()
    )

@dp.message(F.text == 'Mini hot-dog')
async def send_start(message: types.Message):
    await message.answer_photo(
        photo=q,
        caption="Mini hot-dog narxi - 17.000",
        reply_markup=about_menu()
    )

@dp.message(F.text == 'Loonger')
async def send_start(message: types.Message):
    await message.answer_photo(photo=r,
        caption="Loonger narxi - 35.000",
        reply_markup=about_menu()
    )

@dp.message(F.text == 'back')
async def menu_handler(message: types.Message):
    await message.answer("Orqaga", reply_markup=menu())

@dp.message(F.text == '📍Kantakt/Manzilimiz')
async def send_start(message: types.Message):
    await message.answer(
"☎️ Telefon raqamlar (78)-150-00-30",
        reply_markup=menu()
    )


async def main():
    await dp.start_polling(bot)


if __name__ == '__main__':
    asyncio.run(main())