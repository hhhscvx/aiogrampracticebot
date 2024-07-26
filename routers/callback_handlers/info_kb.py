from aiogram.types import (InlineKeyboardButton,
                           InlineKeyboardMarkup)


class ProxyCountries:
    BELGIUM = 'Belgium 🇧🇪'
    CZECHIA = 'Czechia 🇨🇿'
    GERMANY = 'Germany 🇩🇪'
    ITALY = 'Italy 🇮🇹'

class ProxyPayment:
    payment_callback = "payment"
    main_menu_callback = "main_menu"
    pay_text = "💳 Pay now"
    back_to_main_menu_text = "⬅️ Main menu"


def proxy_keyboard_markup() -> InlineKeyboardMarkup:
    btn1 = InlineKeyboardButton(text=ProxyCountries.BELGIUM,
                                callback_data=ProxyCountries.BELGIUM)
    btn2 = InlineKeyboardButton(text=ProxyCountries.CZECHIA,
                                callback_data=ProxyCountries.CZECHIA)
    btn3 = InlineKeyboardButton(text=ProxyCountries.GERMANY,
                                callback_data=ProxyCountries.GERMANY)
    btn4 = InlineKeyboardButton(text=ProxyCountries.ITALY,
                                callback_data=ProxyCountries.ITALY)

    keyboard = [[btn1], [btn2], [btn3], [btn4]]
    markup = InlineKeyboardMarkup(inline_keyboard=keyboard)

    return markup

def payment_markup() -> InlineKeyboardMarkup:
    btn1 = InlineKeyboardButton(text=ProxyPayment.pay_text,
                                callback_data=ProxyPayment.payment_callback)
    btn2 = InlineKeyboardButton(text=ProxyPayment.back_to_main_menu_text,
                                callback_data=ProxyPayment.main_menu_callback)

    keyboard = [[btn1, btn2]]
    markup = InlineKeyboardMarkup(inline_keyboard=keyboard)

    return markup
