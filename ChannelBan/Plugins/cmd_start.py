from pyrogram import Client, filters
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton, CallbackQuery

@Client.on_message(filters.command(["start", "start@ChannelBanRobot"]))
async def start(_, message: Message):
    await message.reply_text(
        f"""<b>Hi {message.from_user.first_name} 😉️!</b>
 `Heya I'm A Anti Channel Tegram bot to delete and ban message sent by channel`""",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "Support", url="https://t.me/danger_bots"
                    ),
                    InlineKeyboardButton(
                        "Dev", url="https://t.me/danger_of_telegram"
                    )
                ],
                [
                    InlineKeyboardButton(
                        "Owner✨️", url="https://t.me/Qalbeyy"
                    )
                ]
            ]
        )
    )
