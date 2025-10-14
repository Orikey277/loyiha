from aiogram import Bot, Dispatcher, types, F
import asyncio
from aiogram.filters import Command
from aiogram.types import KeyboardButton, ReplyKeyboardMarkup

# ------------------- MENYULAR -------------------

def menu_uz():
    button = KeyboardButton(text="🏢Kompaniya Haqida")
    button2 = KeyboardButton(text="📍Filiallar")
    button3 = KeyboardButton(text="Bosh Ish O'rinlari")
    button5 = KeyboardButton(text="Menyu")
    button6 = KeyboardButton(text="Yangiliklar")
    button4 = KeyboardButton(text="📍Kantakt/Manzilimiz")
    button7 = KeyboardButton(text="🇺🇸/🇺🇿 Til")

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


def about_menu_uz():
    button = KeyboardButton(text="Lavash")
    button2 = KeyboardButton(text="Mini hot-dog")
    button3 = KeyboardButton(text="Shaurma")
    button4 = KeyboardButton(text="Loonger")
    button5 = KeyboardButton(text="🔙 Orqaga")
    rkm = ReplyKeyboardMarkup(
        keyboard=[
            [button, button2],
            [button3, button4],
            [button5]
        ],
        resize_keyboard=True
    )
    return rkm


def menu_en():
    button = KeyboardButton(text="🏢About the company")
    button2 = KeyboardButton(text="📍Branches")
    button3 = KeyboardButton(text="Job vacancies")
    button5 = KeyboardButton(text="Menu")
    button6 = KeyboardButton(text="News")
    button4 = KeyboardButton(text="📍Contact/Address")
    button7 = KeyboardButton(text="🇺🇸/🇺🇿 Language")

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


def about_menu_en():
    button = KeyboardButton(text="Lavash")
    button2 = KeyboardButton(text="Mini hot-dog")
    button3 = KeyboardButton(text="Shaurma")
    button4 = KeyboardButton(text="Loonger")
    button5 = KeyboardButton(text="🔙 Back")
    rkm = ReplyKeyboardMarkup(
        keyboard=[
            [button, button2],
            [button3, button4],
            [button5]
        ],
        resize_keyboard=True
    )
    return rkm


def language_menu():
    btn1 = KeyboardButton(text="🇺🇸 English")
    btn2 = KeyboardButton(text="🇺🇿 O‘zbekcha")
    btn_back = KeyboardButton(text="🔙 Back")
    rkm = ReplyKeyboardMarkup(
        keyboard=[[btn1, btn2],
                  [btn_back]],
        resize_keyboard=True
    )
    return rkm


# ------------------- ASOSIY SOZLAMALAR -------------------

API_TOKEN = "8144083932:AAGEi3qw7dqW04FVAvSilBEVkSGUxcNv02E"
bot = Bot(token=API_TOKEN)
dp = Dispatcher()

image = "https://imageproxy.wolt.com/assets/680227bab89d06ee6f4fd65a"
pdp = "https://www.spot.uz/media/img/2023/12/TNWEkA17027458253420_l.jpg"
s = "https://www.spot.uz/media/img/2023/12/TNWEkA17027458253420_l.jpg"
i = "https://yukber.uz/image/cache/catalog/Shaurma-700x700.jpg"
v = "https://lefood.menu/wp-content/uploads/w_images/2023/07/recept-76707-1240x827.jpg"
q = "https://cdn.кухня.рф/recipe/27a53a0a-0c3d-4bc1-9023-e2b058fff43a.webp"
r = "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcSuz81rKYGM9ErG6GtHaz5zzp9E4Eii6cpTjg&s"

# Har bir foydalanuvchining tili
user_lang = {}


# ------------------- HANDLERLAR -------------------

@dp.message(Command('start'))
async def send_start(message: types.Message):
    user_lang[message.from_user.id] = 'uz'
    await message.answer_photo(
        photo=image,
        caption="Oqtepa Lavash botiga hush kelibsiz!",
        reply_markup=menu_uz()
    )


# 🇺🇸/🇺🇿 TIL TANLASH BO'LIMI
@dp.message(F.text.in_({"🇺🇸/🇺🇿 Til", "🇺🇸/🇺🇿 Language"}))
async def choose_language(message: types.Message):
    await message.answer("Tilni tanlang / Choose language:", reply_markup=language_menu())


@dp.message(F.text == "🇺🇸 English")
async def set_english(message: types.Message):
    user_lang[message.from_user.id] = 'en'
    await message.answer("Language changed to English 🇺🇸", reply_markup=menu_en())


@dp.message(F.text == "🇺🇿 O‘zbekcha")
async def set_uzbek(message: types.Message):
    user_lang[message.from_user.id] = 'uz'
    await message.answer("Til o‘zbekchaga o‘zgartirildi 🇺🇿", reply_markup=menu_uz())


@dp.message(F.text.in_({"🔙 Orqaga", "🔙 Back"}))
async def go_back(message: types.Message):
    lang = user_lang.get(message.from_user.id, 'uz')
    if lang == 'uz':
        await message.answer("Asosiy menyu", reply_markup=menu_uz())
    else:
        await message.answer("Main menu", reply_markup=menu_en())


# ------------------- O‘ZBEKCHA FUNKSIYALAR -------------------

@dp.message(F.text == '🏢Kompaniya Haqida')
async def kompaniya_haqida(message: types.Message):
    await message.answer_photo(
        photo=pdp,
        caption="Biz — Oqtepa Lavash, 2010-yilda Chilonzorda kichik kafeda tashkil topgan restoranlar tarmog‘imiz.",
        reply_markup=menu_uz()
    )

@dp.message(F.text == '📍Filiallar')
async def filiallar(message: types.Message):
    await message.answer_photo(photo=s, caption="Filiallarimiz: Oxunboboyev, Nukus2 va boshqalar.", reply_markup=menu_uz())

@dp.message(F.text == 'Menyu')
async def menyu(message: types.Message):
    await message.answer("Menyuda fast food mahsulotlari mavjud:", reply_markup=about_menu_uz())

@dp.message(F.text == 'Yangiliklar')
async def yangiliklar(message: types.Message):
    await message.answer("Tez orada yangi yangiliklar chiqadi!", reply_markup=menu_uz())

@dp.message(F.text == "Bosh Ish O'rinlari")
async def ish_orinlari(message: types.Message):
    await message.answer("Hozircha bo‘sh ish o‘rinlari mavjud emas.", reply_markup=menu_uz())

@dp.message(F.text == '📍Kantakt/Manzilimiz')
async def contact(message: types.Message):
    await message.answer("☎️ Telefon raqam: (78)-150-00-30", reply_markup=menu_uz())


# ------------------- INGLIZCHA FUNKSIYALAR -------------------

@dp.message(F.text == '🏢About the company')
async def about_company(message: types.Message):
    await message.answer_photo(
        photo=pdp,
        caption="We are Oqtepa Lavash — founded in 2010 in Chilonzor. Now we have 96 branches in 11 cities of Uzbekistan.",
        reply_markup=menu_en()
    )

@dp.message(F.text == '📍Branches')
async def branches(message: types.Message):
    await message.answer_photo(photo=s, caption="Our branches: Oxunboboyev, Nukus2 and many more.", reply_markup=menu_en())

@dp.message(F.text == 'Menu')
async def menu_section(message: types.Message):
    await message.answer("We have a variety of delicious fast foods:", reply_markup=about_menu_en())

@dp.message(F.text == 'News')
async def news(message: types.Message):
    await message.answer("Stay tuned for Oqtepa Lavash news!", reply_markup=menu_en())

@dp.message(F.text == 'Job vacancies')
async def jobs(message: types.Message):
    await message.answer("Currently, there are no open positions.", reply_markup=menu_en())

@dp.message(F.text == '📍Contact/Address')
async def contact_en(message: types.Message):
    await message.answer("☎️ Phone: (78)-150-00-30", reply_markup=menu_en())


# ------------------- YON TAOMLAR -------------------

@dp.message(F.text.in_({'Lavash', 'Mini hot-dog', 'Shaurma', 'Loonger'}))
async def meals(message: types.Message):
    lang = user_lang.get(message.from_user.id, 'uz')
    if lang == 'uz':
        if message.text == 'Lavash':
            await message.answer_photo(photo=v, caption="Pishloqli katta lavash narxi - 55.000", reply_markup=about_menu_uz())
        elif message.text == 'Mini hot-dog':
            await message.answer_photo(photo=q, caption="Mini hot-dog narxi - 17.000", reply_markup=about_menu_uz())
        elif message.text == 'Shaurma':
            await message.answer_photo(photo=i, caption="Shaurma narxi - 31.000", reply_markup=about_menu_uz())
        elif message.text == 'Loonger':
            await message.answer_photo(photo=r, caption="Loonger narxi - 35.000", reply_markup=about_menu_uz())
    else:
        if message.text == 'Lavash':
            await message.answer_photo(photo=v, caption="Cheese Lavash price - 55,000", reply_markup=about_menu_en())
        elif message.text == 'Mini hot-dog':
            await message.answer_photo(photo=q, caption="Mini hot-dog price - 17,000", reply_markup=about_menu_en())
        elif message.text == 'Shaurma':
            await message.answer_photo(photo=i, caption="Shaurma price - 31,000", reply_markup=about_menu_en())
        elif message.text == 'Loonger':
            await message.answer_photo(photo=r, caption="Loonger price - 35,000", reply_markup=about_menu_en())


# ------------------- MAIN -------------------

async def main():
    print("Bot ishga tushdi...")
    await dp.start_polling(bot)


if __name__ == '__main__':
    asyncio.run(main())
