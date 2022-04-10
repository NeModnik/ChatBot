

import time
import vk_api
from vk_api.keyboard import VkKeyboardColor, VkKeyboard
from vk_api.longpoll import VkLongPoll, VkEventType


def keyboard_hello():
    global keyboard
    keyboard = vk_api.keyboard.VkKeyboard(one_time=False, inline=True)
    keyboard.add_button('Привет', color=VkKeyboardColor.POSITIVE)
    keyboard.add_button('Статистика', color=VkKeyboardColor.SECONDARY)
    keyboard.add_line()
    keyboard.add_button('Мемы', color=VkKeyboardColor.SECONDARY)
    keyboard.add_button('Опрос', color=VkKeyboardColor.PRIMARY)

    #return keyboard_hello()


def send_photo(user_id, url):
    vk.method('messages.send', {'user_id': user_id, 'attachment': url, 'random_id': 0})


'''def create_keyboard():
    keyboard = vk_api.keyboard.VkKeyboard(one_time=False)
    keyboard.add_button("Закрыть", color=vk_api.keyboard.VkKeyboardColor.DEFAULT)
    keyboard.add_button("Кнопка", color=vk_api.keyboard.VkKeyboardColor.POSITIVE)
    return keyboard.get_keyboard()'''


def write(user_id, message):
    vk.method('messages.send', {'user_id': user_id, 'message': message, 'random_id': 0})
    #keyboard_hello()


def sender(user_id, text):
    vk.method('messages.send',
              {'user_id': user_id, 'message': text, 'random_id': 0, 'keyboard': keyboard.get_keyboard()})




token = "df8a6f35ad2057d0ae84534d1a6ae9a135cd8a12ecc9155b6f5410734d7471d5b35d878695465c88206af"
vk = vk_api.VkApi(token=token)
longpoll = VkLongPoll(vk)

for event in longpoll.listen():
    if event.type == vk_api.longpoll.VkEventType.MESSAGE_NEW:
        if event.to_me:
            request = event.text
            if request == "Меню":
                keyboard_hello()
                sender(event.user_id, 'Ваше меню')
            if request == "Привет":
                keyboard_hello()
                sender(event.user_id, 'Меню')
                write(event.user_id, "Привет,вездекодерам!")

            if request =="Опрос":
                n=0
                questions = ['ВОВ закончилась в 1945г?',
                             'Равносторонний треугольник - треугольник у которого все углы равны?', 'Ты вездекодер?',
                             'Какого цвета растения?', 'В чем дело?', 'В чем сила?',
                             'Есть ли в Египте пирамиды Хеопса?', 'Есть ли цензура в России']
                write(event.user_id, questions[n])
                keyboard = VkKeyboard(one_time=True, inline=False)
                keyboard.add_button('Да', VkKeyboardColor.POSITIVE)
                keyboard.add_button('Нет', VkKeyboardColor.NEGATIVE)
                sender(event.user_id, 'Выберите варианты ответа')
                if request=="Да" or request=="Нет":
                    n+=1
                    write(event.user_id, questions[n])
            if request == "Мемы":
                k = 457260347
                like = 0
                dislike = 0
                for i in range(5):
                    name = ('photo174318716_' + str(k))
                    send_photo(event.user_id, name)
                    keyboard = VkKeyboard(one_time=True)
                    keyboard.add_button('Лайк', VkKeyboardColor.POSITIVE)
                    keyboard.add_button('Дизлайк', VkKeyboardColor.NEGATIVE)
                    keyboard.add_button('Подожди', VkKeyboardColor.NEGATIVE)
                    keyboard.add_button('Продолжить', VkKeyboardColor.POSITIVE)
                    sender(event.user_id, 'Лайк/дизлайк')
                    time.sleep(5)
            if request == "Лайк" or request == "лайк":
                like += 1
                k = k + 1
            if request == "Дизлайк" or request == "диз":
                dislike = dislike + 1
                k = k + 1
            if request=="Подожди":
                break
            if request=="Продолжить":
                continue

                    # print(k)
            if request == "Cтатистика":
                write(event.user_id, ('Вы поставили ' + str(like) + ' лайков'))
                write(event.user_id, ('Вы поставили ' + str(dislike) + ' дизлайков'))
