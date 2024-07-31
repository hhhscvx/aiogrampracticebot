from aiogram.types import ReplyKeyboardMarkup, KeyboardButton


class CryptoSphere:
    retro = "Retro hunting"
    nft = "NFT Degen"
    both = "Both"
    SPHERES = [retro, nft, both]


def choose_sphere_keyboard() -> ReplyKeyboardMarkup:
    btn1 = KeyboardButton(text=CryptoSphere.retro)
    btn2 = KeyboardButton(text=CryptoSphere.nft)
    btn3 = KeyboardButton(text=CryptoSphere.both)

    keyboard = [[btn1, btn2, btn3]]
    markup = ReplyKeyboardMarkup(keyboard=keyboard,
                                 resize_keyboard=True)

    return markup
