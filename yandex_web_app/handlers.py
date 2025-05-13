import asyncio
from aiogram import Router
from keyboards import keyboard
from aiogram import types
from aiogram.filters import Command
from web_app_handler import WebAppDataFilter
from config import CRYPTO_API
from aiocryptopay import AioCryptoPay, Networks


router = Router()

crypto_pay = AioCryptoPay(token=CRYPTO_API, network=Networks.MAIN_NET)


@router.message(Command('start'))
async def start(message: types.Message):
    await message.answer('<b><i>Добро пожаловать в магазин</i></b>', reply_markup=keyboard, parse_mode='html')


PRICE = {
    '1': 8,
    '2': 5,
    '3': 4,
    '4': 0.03,
    '5': 1,
    '6': 1
}


@router.message(WebAppDataFilter())
async def handle_web_app_data(message: types.Message, web_app_data: types.WebAppData):
    if web_app_data.data == '1':
        await message.answer('''<i><b>ВЫ НАЖАЛИ НА ПЕРВЫЙ ТОВАР</b></i>''', parse_mode='html')
    if web_app_data.data == '2':
        await message.answer('''<b><i>ВЫ НАЖАЛИ НА ВТОРОЙ ТОВАР</i></b>''', parse_mode='html')
    if web_app_data.data == '3':
        await message.answer('''<b><i>ВЫ НАЖАЛИ НА ТРЕТИЙ ТОВАР</i></b>''', parse_mode='html')
    if web_app_data.data == '4':
        await message.answer('''<b><i>ВЫ НАЖАЛИ НА ЧЕТВЕРТЫЙ ТОВАР</i></b>''', parse_mode='html')
    if web_app_data.data == '5':
        await message.answer('''<b><i>ВЫ НАЖАЛИ НА ПЯТЫЙ ТОВАР</i></b>''', parse_mode='html')
    if web_app_data.data == '6':
        await message.answer('''<b><i>ВЫ НАЖАЛИ НА ШЕСТОЙ ТОВАР</i></b>''', parse_mode='html')
    summa = PRICE[web_app_data.data]
    invoice = await crypto_pay.create_invoice(amount=summa, asset="USDT")
    url = invoice.bot_invoice_url
    await message.answer(f'<b><i>Cчёт для покупки ⬇</i></b>\n\n{url}', parse_mode='html')
    await asyncio.sleep(5)
    invoice = await crypto_pay.get_invoices(invoice_ids=invoice.invoice_id)
    data_invoice = f"{invoice}".split()
    print(data_invoice)
    if data_invoice[1] == "status='paid'":
        await message.answer('''<b><i>СПАСИБО ЗА ПОКУПКУ!</i></b>''', parse_mode="html")
    await crypto_pay.close()