import telebot

token = '962893501:AAEAx6OxcXatlI_MX-fvfjrORxyApbyK9R8'
bot = telebot.TeleBot(token)
status_message = 'Узнать статус заказа'
review_message = 'Оставить отзыв'
order_number_message = 'Введите номер заказа'
phone_number_message = 'Введите номер телефона, с которого был сделан заказ'
cancel_message = 'Отменить заказ'
alter_delivery_conditions_message = 'Изменить условия доставки'
alter_delivery_time_message = 'Изменить время доставки'
alter_delivery_place_message = 'Изменить место доставки'


@bot.message_handler(commands=['start', 'help'])
def reply_welcome(message, first_time=True):
    markup = telebot.types.ReplyKeyboardMarkup()
    markup.row(status_message, review_message)
    bot.send_message(message.chat.id, "Добрый день!")
    bot.send_message(message.chat.id, "Чем могу Вам помочь? Выберите один из вариантов в выпадающем меню ниже",
                     reply_markup=markup)


@bot.message_handler(func=lambda m: True if m.text == review_message else False)
def reply_status(message):
    bot.send_message(message.chat.id, "Пожалуйста, оставьте свой отзыв о товаре :")
    # todo - process review massage


@bot.message_handler(func=lambda m: True if m.text == status_message else False)
def reply_status(message):
    markup = telebot.types.ReplyKeyboardMarkup()
    markup.row(order_number_message,
               phone_number_message)
    bot.send_message(message.chat.id, "Выберите один из вариантов, по которому мы сможем найти Ваш заказ:",
                     reply_markup=markup)


@bot.message_handler(func=lambda m: True if m.text == order_number_message
                            or m.text == phone_number_message else False)
def reply_order_phone(message):
    # todo - парсинг номера телефона или номера заказа, проверка в базе

    markup = telebot.types.ReplyKeyboardMarkup()
    markup.row(cancel_message,
               alter_delivery_conditions_message)
    bot.send_message(message.chat.id, "Что Вы хотите сделать с Вашим заказом ?", reply_markup=markup)


@bot.message_handler(func=lambda m: True if m.text == cancel_message else False)
def reply_cancel(message):
    bot.send_message(message.chat.id, "Заказ успешно отменен.")
    reply_welcome(message, first_time=False)

@bot.message_handler(func=lambda m: True if m.text == alter_delivery_conditions_message else False)
def reply_alter_delivery(message):
    markup = telebot.types.ReplyKeyboardMarkup()
    markup.row(alter_delivery_time_message,
               alter_delivery_place_message)
    bot.send_message(message.chat.id, "Что именно Вы хотите изменить? Выберите один из вариантов", reply_markup=markup)

@bot.message_handler(func=lambda m: True if m.text == alter_delivery_time_message else False)
def reply_alter_delivery_time(message):
    # todo - сделать изменение
    bot.send_message(message.chat.id, "Данные успешно изменены")
    reply_welcome(message, first_time=False)


@bot.message_handler(commands=[alter_delivery_place_message])
def reply_alter_delivery_place(message):
    # todo - сделать изменение
    bot.send_message(message.chat.id, "Данные успешно изменены")
    reply_welcome(message, first_time=False)

@bot.message_handler(func=lambda message: True)
def reply_default_all(message):
    bot.reply_to(message, "Не угадал с сообщением. Попробуй еще раз")

bot.polling()
