import telebot
from telebot.types import InlineKeyboardMarkup, InlineKeyboardButton

# التوكن حقك
TOKEN = "8425515227:AAH5czokZjO6m_Bon3Jat07OTn90kbRF-D4"
bot = telebot.TeleBot(TOKEN)

# رسالة الترحيب
welcome_text = """
✨ أهلاً وسهلاً بك في بوت *Luxury HD خلفيات* ✨

🔹 اختر القسم اللي يعجبك من القائمة تحت 👇
"""

# القائمة الرئيسية
def main_menu():
    markup = InlineKeyboardMarkup(row_width=2)

    markup.add(
        InlineKeyboardButton("👦 بروفايلات أولاد", url="https://t.me/LuxuryHD_Backgrounds/198"),
        InlineKeyboardButton("👧 بروفايلات بنات", callback_data="girls"),
    )

    markup.add(
        InlineKeyboardButton("⚽ مشاهير كرة القدم", callback_data="football"),
        InlineKeyboardButton("👕 تيشيرتات كرة/سلة", url="https://t.me/LuxuryHD_Backgrounds/313"),
    )

    markup.add(
        InlineKeyboardButton("🎤 مشاهير هيب هوب ومطربين", callback_data="hiphop"),
        InlineKeyboardButton("🇮🇶 شخصيات سياسية", callback_data="politics"),
    )

    markup.add(
        InlineKeyboardButton("👻 شبح جمالي", url="https://t.me/LuxuryHD_Backgrounds/12"),
        InlineKeyboardButton("💀 فن الجمجمة", url="https://t.me/LuxuryHD_Backgrounds/52"),
    )

    markup.add(
        InlineKeyboardButton("🕌 خلفيات إسلامية", url="https://t.me/LuxuryHD_Backgrounds/511"),
    )

    markup.add(
        InlineKeyboardButton("🌅 مناظر طبيعية", callback_data="nature"),
        InlineKeyboardButton("🌹 خلفيات ورد", url="https://t.me/LuxuryHD_Backgrounds/675"),
    )

    markup.add(
        InlineKeyboardButton("🎌 خلفيات إنمي", url="https://t.me/LuxuryHD_Backgrounds/647"),
        InlineKeyboardButton("🐭 خلفيات كرتونية", callback_data="cartoon"),
    )

    return markup


# قائمة بنات
def girls_menu():
    markup = InlineKeyboardMarkup(row_width=1)
    markup.add(
        InlineKeyboardButton("👧 بروفايلات بنات (جزء 1)", url="https://t.me/LuxuryHD_Backgrounds/163"),
        InlineKeyboardButton("👧 بروفايلات بنات (جزء 2)", url="https://t.me/LuxuryHD_Backgrounds/458"),
        InlineKeyboardButton("⬅️ رجوع", callback_data="main")
    )
    return markup

# كرة القدم
def football_menu():
    markup = InlineKeyboardMarkup(row_width=2)
    markup.add(
        InlineKeyboardButton("⚽ كريستيانو رونالدو", url="https://t.me/LuxuryHD_Backgrounds/261"),
        InlineKeyboardButton("⚽ ميسي", url="https://t.me/LuxuryHD_Backgrounds/422"),
        InlineKeyboardButton("⬅️ رجوع", callback_data="main")
    )
    return markup

# الهيب هوب
def hiphop_menu():
    markup = InlineKeyboardMarkup(row_width=2)
    markup.add(
        InlineKeyboardButton("🎤 توباك / 2pac", url="https://t.me/LuxuryHD_Backgrounds/52"),
        InlineKeyboardButton("🎤 روس / Russ", url="https://t.me/LuxuryHD_Backgrounds/619"),
        InlineKeyboardButton("⬅️ رجوع", callback_data="main")
    )
    return markup

# السياسة
def politics_menu():
    markup = InlineKeyboardMarkup(row_width=1)
    markup.add(
        InlineKeyboardButton("🇮🇶 صدام حسين", url="https://t.me/LuxuryHD_Backgrounds/52"),
        InlineKeyboardButton("⬅️ رجوع", callback_data="main")
    )
    return markup

# مناظر طبيعية
def nature_menu():
    markup = InlineKeyboardMarkup(row_width=1)
    markup.add(
        InlineKeyboardButton("🌅 مناظر طبيعية", url="https://t.me/LuxuryHD_Backgrounds/543"),
        InlineKeyboardButton("🎨 خلفيات طبيعية رسم", url="https://t.me/LuxuryHD_Backgrounds/385"),
        InlineKeyboardButton("⬅️ رجوع", callback_data="main")
    )
    return markup

# كرتون
def cartoon_menu():
    markup = InlineKeyboardMarkup(row_width=1)
    markup.add(
        InlineKeyboardButton("🐭 توم وجيري", url="https://t.me/LuxuryHD_Backgrounds/600"),
        InlineKeyboardButton("⬅️ رجوع", callback_data="main")
    )
    return markup


# أوامر
@bot.message_handler(commands=['start'])
def send_welcome(message):
    bot.send_message(message.chat.id, welcome_text, parse_mode="Markdown", reply_markup=main_menu())


# التحكم في الأزرار
@bot.callback_query_handler(func=lambda call: True)
def callback_query(call):
    if call.data == "main":
        bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.id,
                              text=welcome_text, parse_mode="Markdown", reply_markup=main_menu())
    elif call.data == "girls":
        bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.id,
                              text="اختر قسم 👧:", reply_markup=girls_menu())
    elif call.data == "football":
        bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.id,
                              text="⚽ اختر لاعب:", reply_markup=football_menu())
    elif call.data == "hiphop":
        bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.id,
                              text="🎤 اختر مغني:", reply_markup=hiphop_menu())
    elif call.data == "politics":
        bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.id,
                              text="🇮🇶 اختر شخصية:", reply_markup=politics_menu())
    elif call.data == "nature":
        bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.id,
                              text="🌅 اختر نوع الخلفيات:", reply_markup=nature_menu())
    elif call.data == "cartoon":
        bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.id,
                              text="🐭 اختر كرتون:", reply_markup=cartoon_menu())


print("🤖 البوت شغال...")
bot.polling()
