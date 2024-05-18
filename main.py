from email import message
from multiprocessing.reduction import send_handle
import webbrowser
import telebot
from telebot import *
from data_base.tables import reg_id, reg_name, reg_sname, reg_phone, table_users, profile, up, correct
import time
import asyncio
from config import TOKEN



bot=telebot.TeleBot(TOKEN)


@bot.message_handler(commands=["start"])
def start(message):
    reg_id(message.from_user.id)
    murkup=types.InlineKeyboardMarkup()
    murkup.add(types.InlineKeyboardButton("Меню", callback_data="menu"))
    bot.send_message(message.chat.id, f"Здравствуй, {message.from_user.first_name} тебя приветсвует помощник Успокойся!", reply_markup=murkup)
    




@bot.callback_query_handler(func=lambda call: True)
def menu(call):
    if call.data == "menu":
        murkup=types.InlineKeyboardMarkup()
        up(call.message.chat.id, call.message.chat.username)
        murkup.add(types.InlineKeyboardButton("Наш сайт", url="https://успокойся.рус"))
        murkup.add(types.InlineKeyboardButton("Играть", callback_data="play"))
        murkup.add(types.InlineKeyboardButton("Группа телеграмм", url="https://t.me/KeepCalmAndHappy"))
        murkup.add(types.InlineKeyboardButton("Задать вопрос создателю", callback_data="qvestion"))
        murkup.add(types.InlineKeyboardButton("Правила игры", callback_data="roole"))
        murkup.add(types.InlineKeyboardButton("Профиль", callback_data="profile"))
        bot.send_message(call.message.chat.id, "🗒Меню:", reply_markup=murkup)
        
        
    if call.data == "roole":
        markup=types.InlineKeyboardMarkup()
        markup.add(types.InlineKeyboardButton("Меню", callback_data="menu"))
        bot.send_message(call.message.chat.id, """🎲 Успокойся! - новая психо-мотивационная игра, созданная специально для тех, кто стремится к лучшей версии себя, хочет освоить позитивное мышление и увеличить уровень счастья в своей жизни. С этой игрой все изменится к лучшему.🚀

Игра Успокойся! предлагает уникальные мотивационные техники, которые основаны на внутреннем желании, ведь лучшая мотивация идет именно от нашей собственной внутренней силы. Игроки заключают дружеские пари 🤑на выполнение задач в течение 30 дней под присмотром психотренера. Основные задания включают в себя физические упражнения, правильное питание, медитации и психологические тренировки, каждое из которых приносит определенное количество баллов активности.⚡️
У каждого задания свое количество баллов: например за утреннюю зарадку, игрок получает 5 баллов. за чистку зубов - 1 балл, а за выполнение круга жизни - 10 баллов. Баллы начисляются только при наличии отчета о выполнении. Каждое задание отмечается повышением (либо понижением)  психорейтинга.🎯

Через чат в телеграмме, участники получают возможность выполнять задания вместе, обмениваться отчетами о проделанной работе и получать рекомендации психотренера. Это обеспечивает поддержку и помощь в трудные моменты, позволяя достигать большего с легкостью.💪

Психорейтинг, измеряемый авторской системой, помогает бороться с негативными мыслями, дает силы на самосовершенствование, а разработанная система психологических тренировок обеспечивает легкий путь к лучшей версии себя.🦸🏻‍♂️

Наши психотренеры разрабатывают распорядок дня, в котором указано время выполнения задач, цена в баллах активности и ожидаемое повышение психорейтинга. Эта игра не требует значительных усилий , а благодаря умелому управлению, игроки обретают больше свободного времени для себя и для любимых занятий.⏰

Игрок, набравший наибольшее количество баллов активности и увеличивший средний психорейтинг, становится победителем и забирает призовой фонд. 💰Это не просто игра – это возможность узнать свои границы и обрести счастье.🥰

Успокойся! помогает формировать новые нейронные связи, стимулирует выработку дофамина, окситоцина, серотонина и эндорфина. Путем достижения целей, упражнений и поддержания правильного питания и медитации, уровень счастья поднимается на новый уровень.😎

Это не требует выполнения сложных заданий или принуждения. Проработка проблем позволяет не только почувствовать вкус счастья, но и закрепить его. Успокойся! – это возможность стать лучшей версией себя и обрести счастье в виде мотивации и поддержки.🤩""", reply_markup=markup)
     
     
    
        
        
    if call.data == "qvestion":
        markup=types.InlineKeyboardMarkup()
        btn2=(types.InlineKeyboardButton("Что такое психорейтинг?", callback_data="psix"))
        btn3=(types.InlineKeyboardButton("У меня нету времени на тренинг", callback_data="no_time"))
        btn4=(types.InlineKeyboardButton("Я боюсь откраыватся", callback_data="fear"))
        btn5=(types.InlineKeyboardButton("Я не верю в этот подход", callback_data="lai"))
        btn6=(types.InlineKeyboardButton("Я сам справлюсь", callback_data="I_sam"))
        btn7=(types.InlineKeyboardButton("Это слишком дорого", callback_data="many"))
        btn8=(types.InlineKeyboardButton("Хочу индивидуальные занятия с психологом", url="https://успокойся.рус/psycologists.html"))
        markup.add(btn2,btn3,btn4,btn5,btn6,btn7,btn8, row_width=1)
        markup.add(types.InlineKeyboardButton("Остались вопросы?", url="https://t.me/KeepCalmAndHappy"))
        markup.add(types.InlineKeyboardButton("Меню", callback_data="menu"))
        bot.send_message(call.message.chat.id, "🤔Популярные вопросы пользователей:", reply_markup=markup)
    
    

    if call.data == "psix":
        markup=types.InlineKeyboardMarkup()
        markup.add(types.InlineKeyboardButton("Назад к вопросам ->", callback_data="qvestion"))
        markup.add(types.InlineKeyboardButton("Меню", callback_data="menu"))
        bot.send_message(call.message.chat.id, """Психорейтинг - это цифровое значение отображающее психологическое состояние игрока по шкале от 0 до 5. Где 0 абсолютно несчастен полная депрессия либо глубокий невроз и 5 абсолютное счастье эйфория
Показания психорейтинга проходят следующим образом: 
Записывается шот на 1 минуту, где игрок указывает на свои мысли которые управляют его разумом 
называет о чем думал с последнего замера психорейтинга 
Важно делиться не только хорошим но и переживаниями""", reply_markup=markup)
        
        
    if call.data == "no_time":
        markup=types.InlineKeyboardMarkup()
        markup.add(types.InlineKeyboardButton("Назад к вопросам ->", callback_data="qvestion"))
        markup.add(types.InlineKeyboardButton("🗒Меню", callback_data="menu"))
        bot.send_message(call.message.chat.id, "Полностью понимаю, что у вас много дел, но наш тренинг предоставляет уникальную возможность для эффективного управления временем. Мы специально разработали этот тренинг так, чтобы он был гибким и доступным для занятых людей. Наши участники часто отмечают, что благодаря нашему тренингу они научились эффективно распределять свое время, что привело к повышенной продуктивности во всех аспектах их жизни. Мы также предлагаем поддержку в разработке персонального расписания для тренинга, чтобы убедиться, что он идеально впишется в вашу занятую жизнь. Не хотите ли вы выделить небольшое время, чтобы узнать больше о том, как этот тренинг может помочь вам стать более продуктивным и управлять временем с легкостью?", reply_markup=markup)
        
        
    if call.data == "fear":
        markup=types.InlineKeyboardMarkup()
        markup.add(types.InlineKeyboardButton("Назад к вопросам ->", callback_data="qvestion"))
        markup.add(types.InlineKeyboardButton("🗒Меню", callback_data="menu"))
        bot.send_message(call.message.chat.id, "Я понимаю, что вопрос открытости может вызывать сильные чувства неуверенности и дискомфорта. Однако, важно помнить, что наша работа - это создание безопасного пространства, где вы можете почувствовать себя комфортно и защищено. Мы уделяем особое внимание вашим потребностям и готовы настроить процесс так, чтобы он был оптимально комфортен и безопасен для вас. Мы также строго соблюдаем принципы конфиденциальности, что означает, что ваша чувствительная информация будет находиться под надежной защитой. Вам не нужно беспокоиться о том, что ваша уязвимость будет оставаться незащищенной. Наша цель - создать теплую и поддерживающую среду, где вы можете чувствовать себя комфортно, открываться и расти. Все упражнения построены так, чтобы дать вам возможность открываться постепенно, в вашем собственном темпе, и мои коллеги и я будем под рукой, чтобы обеспечить вас поддержкой и пониманием на протяжении всего процесса. Наши предыдущие сезоны подтверждают, что участники ощущают глубокую радость и освобождение, когда они преодолевают свои страхи и делятся своими переживаниями. Что если вы предоставите себе возможность познакомиться с этим окружением, чтобы увидеть, как оно может изменить вашу жизнь?", reply_markup=markup)
    
    if call.data == "I_sam":
        markup=types.InlineKeyboardMarkup()
        markup.add(types.InlineKeyboardButton("Назад к вопросам ->", callback_data="qvestion"))
        markup.add(types.InlineKeyboardButton("🗒Меню", callback_data="menu"))
        bot.send_message(call.message.chat.id, """Мы уважаем вашу независимость. Однако, наш тренинг не только предоставляет знания и навыки, но и создает уникальное сообщество, где люди делятся опытом, поддерживают друг друга и вдохновляют на рост. Участники наших тренингов часто отмечают, что самость самостоятельно - это важно, но иметь поддержку и мудрость коллектива - это то, что помогает им преодолеть трудности и добиться настоящего личностного и профессионального роста. Мы также предлагаем индивидуальные консультации и поддержку вне тренингов, чтобы убедиться, что вы получаете максимальную пользу от нашего опыта. Рассмотрите возможность присоединиться к нашей уникальной общине, где ваш рост и успех станут приоритетом. """, reply_markup=markup)
    
    
    if call.data == "lai":
        markup=types.InlineKeyboardMarkup()
        markup.add(types.InlineKeyboardButton("Назад к вопросам ->", callback_data="qvestion"))
        markup.add(types.InlineKeyboardButton("🗒Меню", callback_data="menu"))
        bot.send_message(call.message.chat.id, """
            Понимаю ваше сомнение. Каждый из нас имеет свое видение и опыт, когда дело касается методов саморазвития. Однако, позвольте мне пояснить, что наш подход основан на знаниях и опыте, которые помогли многим людям достичь своих целей и улучшить качество своей жизни. Мы предоставляем индивидуальные методики, разработанные с учетом уникальности каждого клиента. Мы также готовы адаптировать наши подходы и техники под ваши уникальные потребности и запросы. Могу ли я предложить вам более подробное описание наших методик и практик, чтобы помочь вам лучше понять, как этот подход может быть применим и полезен в вашем случае?""", reply_markup=markup)
    
    
    if call.data == "many":
        markup=types.InlineKeyboardMarkup()
        markup.add(types.InlineKeyboardButton("Назад к вопросам ->", callback_data="qvestion"))
        markup.add(types.InlineKeyboardButton("🗒Меню", callback_data="menu"))
        bot.send_message(call.message.chat.id, """Мы понимаем вашу озабоченность, в наше вермя очень важно знать за что ты платишь и выбирать самые выгодные условия! Цена игры включает в себя не только 30 дневное сопровождение психолога, но и инвестицию в ваше личностное развитие. Представьте это не как расход, а как инвестицию в себя. После окончания игры вы получите навыки, которые помогут вам в карьере, личной жизни и достижении ваших целей. Это вложение в ваше будущее и достижение успеха, которое окупится многократно. Давайте посмотрим на это не как расход, а как инвестицию в свое собственное счастье и успех. Тем более стоимость участия может позволить себе даже студент! """, reply_markup=markup)
    
        
        
    if call.data == "play":
        bot.register_next_step_handler(bot.send_message(call.message.chat.id, """Введите ваше имя 
Если хотите оставить поле пустым введите: - """), name)
    
    
    if call.data == "profile":
        pr=profile(call.message.chat.id)
        markup=types.InlineKeyboardMarkup()
        markup.add(types.InlineKeyboardButton("Изменить", callback_data="play"),types.InlineKeyboardButton("Меню", callback_data="menu"))
        bot.send_message(call.message.chat.id, f"""🎫Ваш профиль: 
Имя: {pr[0][2]}
Фамилия: {pr[0][3]}
Номер телефона: {pr[0][5]}""",reply_markup=markup)
        
        
        
def phone(message):
    if correct(message.text)==True:
        reg_phone(message.text, message.from_user.id)
        murkup=types.InlineKeyboardMarkup()
        up(message.from_user.id,message.from_user.username)
        murkup.add(types.InlineKeyboardButton("Наш сайт", url="https://успокойся.рус"))
        murkup.add(types.InlineKeyboardButton("Играть", callback_data="play"))
        murkup.add(types.InlineKeyboardButton("Группа телеграмм", url="https://t.me/KeepCalmAndHappy"))
        murkup.add(types.InlineKeyboardButton("Задать вопрос создателю", callback_data="qvestion"))
        murkup.add(types.InlineKeyboardButton("Правила игры", callback_data="roole"))
        murkup.add(types.InlineKeyboardButton("Профиль", callback_data="profile"))
        bot.send_message(message.chat.id, "🗒Меню:", reply_markup=murkup)
    else:
        not_valid_phone(message.from_user.id)
 


def smane(message):
    reg_sname(message.text, message.from_user.id)
    bot.register_next_step_handler(bot.send_message(message.chat.id, """Введите ваш номер телефона начиная с +7 
Если хотите оставить поле пустым введите: - """), phone )
        
  
        
def name(message):
    reg_name(message.text, message.from_user.id, message.from_user.username)
    bot.register_next_step_handler(bot.send_message(message.chat.id, """Введите фамилию 
Если хотите оставить поле пустым введите: - """), smane)
    


def password(message):
    if message.text == "qicSivpOOYZ_0MA2tumeCGbyEcLtCj":
        bot.send_message(message.chat.id, f"все пользователи:{table_users()}")
        



@bot.message_handler(commands=["menu"])
def menu1(message):
    murkup=types.InlineKeyboardMarkup()
    up(message.from_user.id,message.from_user.username)
    murkup.add(types.InlineKeyboardButton("Наш сайт", url="https://успокойся.рус"))
    murkup.add(types.InlineKeyboardButton("Играть", callback_data="play"))
    murkup.add(types.InlineKeyboardButton("Группа телеграмм", url="https://t.me/KeepCalmAndHappy"))
    murkup.add(types.InlineKeyboardButton("Задать вопрос создателю", callback_data="qvestion"))
    murkup.add(types.InlineKeyboardButton("Правила игры", callback_data="roole"))
    murkup.add(types.InlineKeyboardButton("Профиль", callback_data="profile"))
    bot.send_message(message.chat.id, "🗒Меню:", reply_markup=murkup)
    
    
@bot.message_handler(commands=["users"])
def user_table(message):
    bot.register_next_step_handler(bot.send_message(message.chat.id, "Введите пароль"), password)
    
    
def not_valid_phone(id):
    bot.register_next_step_handler(bot.send_message(id,"""Невернно введен номер телефона!
Введите ваш номер телефона начиная с +7 
Если хотите оставить поле пустым введите: - """), phone)
    
    
    
    
    
while True:
    try:
        asyncio.run(bot.polling(non_stop=True, interval=1, timeout=0))
    except:
        time.sleep(2)



