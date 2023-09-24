define gg = Character('[playerName]', color="#42AAFF")
define yarik = Character('Ярослав', color="#6600ff")
define workerAndry = Character('Сотрудник Андрей', color="#C6C3B5")
define workers = Character('Сотрудники', color="#9c8786")
define alenaBeforeNamingHerself = Character('Девушка', color="#e1ff00")
define alena = Character('Алёна', color="#e1ff00")
define aleksei = Character('Алексей', color="#d18d4d")
define waiter = Character('Официант', color="#56c4ae")
define nikitaBeforeNamingHimself = Character('???', color="#f12b10")
define nikita = Character('Никита', color="#f12b10")


transform toLeft:
    xalign 0.2
    yalign 0.5

transform toCenter:
    xalign 0.5
    yalign 0.5

transform toRight:
    xalign 0.8
    yalign 0.5

transform toLeftYarik:
    xalign 0.2
    yalign 0.635
    xzoom 0.9 yzoom 0.9

transform toCenterYarik:
    xalign 0.5
    yalign 0.635
    xzoom 0.9 yzoom 0.9

transform toRightYarik:
    xalign 0.8
    yalign 0.635
    xzoom 0.9 yzoom 0.9

transform toLeftGG:
    xalign 0.2
    yalign 2.0

transform toCenterGG:
    xalign 0.5
    yalign 2.0

transform toRightGG:
    xalign 0.8
    yalign 2.0

transform toLeftShlepa:
    xalign 0.3
    yalign 0.9
    xzoom 0.6 yzoom 0.6

transform toCenterShlepa:
    xalign 0.5
    yalign 0.9
    xzoom 0.6 yzoom 0.6

transform toRightShlepa:
    xalign 0.7
    yalign 0.9
    xzoom 0.6 yzoom 0.6

transform toGGShlepa:
    xalign 0.3
    yalign 0.87
    xzoom 0.6
    yzoom 0.6


transform вСпальнеМеждуШкафомИКроватью:
    xalign 0.75
    yalign 0.5

label start:

    play music "audio/фоновая музыка.mp3" fadein 4.0 fadeout 4.0 loop volume 0.2

    scene фон дом_гг спальня

    $ badEnding = 0
    $ neutralEnding = 0
    $ goodEnding = 0

    $ goodShlepaRelationship = 0
    $ neutralShlepaRelationship = 0
    $ badShlepaRelationship = 0

    $ goodCoworkersRelationship = 0
    $ neutralCoworkersRelationship = 0
    $ badCoworkersRelationship = 0

    $ goodAlenaRelationship = 0
    $ neutralAlenaRelationship = 0
    $ badAlenaRelationship = 0

    "Каждый день нашего разработчика компьютерных игр ничем не отличался от остальных, но было кое-что особенное
в его жизни..."

    $ playerName = renpy.input("Выберите имя для главного героя:")
    $ playerName = playerName.strip()
    if playerName == "":
        $ playerName = "Михаил"


    show гг with dissolve:
        вСпальнеМеждуШкафомИКроватью
        xzoom 0.9 yzoom 0.9

    gg "Какое же хорошее утро, что может пойти не так в этот чудесный день?"

    gg "Так не хочется выходить из дома..."

    scene фон дом_гг спальня
    with fade

    show гг:
        вСпальнеМеждуШкафомИКроватью
        xzoom 0.9 yzoom 0.9
        parallel:
            linear 2.0 toCenterGG
        parallel:
            linear 2.0 xzoom 1 yzoom 1

    gg "Хмммм, а где Шлепун???"

    gg "Ах, да, точно, я же оставил его у своего друга, вчера явно был тяжёлый рабочий день."

    scene фон дом_гг спальня
    with fade

    show гг:
        toCenterGG

    menu:
        "Я скучаю по Шлепуну":
            gg "Всего один день без Шлепуна, а я уже скучаю по нему."

            $ goodEnding += 1
            $ goodShlepaRelationship += 1

        "Мне так хорошо без Шлепуна":
            gg "Всего один день без Шлепуна, но мне стало легче, хоть отдохнул от него."

            $ badEnding += 1
            $ badShlepaRelationship += 1

    scene фон дом_гг спальня
    with fade

    show гг:
        toCenterGG
        xzoom 1 yzoom 1
        parallel:
            linear 2.0 вСпальнеМеждуШкафомИКроватью
        parallel:
            linear 2.0 xzoom 0.9 yzoom 0.9

    gg "Ладно, пора собираться на работу."
    
    menu:
        "Попрощаться со Шлепуном":
            gg "Шлепун, иди прощаться!"

            pause 1

            gg "Ах, да, я забыл..."

            $ goodEnding += 1
            $ goodShlepaRelationship += 1

        "Выйти из квартиры":
            gg "Хорошо, что Шлепун меня не провожает, так даже лучше."

            $ badEnding += 1
            $ badShlepaRelationship += 1

    jump street_chatWithYarik
    
label street_chatWithYarik:
    scene фон улица_день
    with fade
    
    show гг with dissolve:
        toLeftGG

    gg "Кто это мне написал?"

    show телефон гг входящее_сообщение_ярика:
        toRight
        xzoom 0.5 yzoom 0.5

    yarik "{b}(сообщение){/b} Привет, со Шлепуном всё хорошо, я его приведу вечером, как и договаривались."


    menu:
        yarik "{b}(сообщение){/b} Привет, со Шлепуном всё хорошо, я его приведу вечером, как и договаривались."

        "Я хочу побыстрее увидеть Шлепуна":
            hide телефон гг входящее_сообщение_ярика

            show телефон гг сообщение_ярик_хорошее:
                toRight
                xzoom 0.5 yzoom 0.5

            gg "{b}(сообщение){/b} Конечно, я уже соскучился по нему!"

            $ goodEnding += 1
            $ goodShlepaRelationship += 1

        "Я хочу ещё отдохнуть от Шлепуна":
            hide телефон гг входящее_сообщение_ярика

            show телефон гг сообщение_ярик_плохая1:
                toRight
                xzoom 0.5 yzoom 0.5

            gg "{b}(сообщение){/b} А можешь ещё побыть с ним, хочу отдохнуть."

            hide телефон гг сообщение_ярик_плохая1

            show телефон гг сообщение_ярик_плохая2:
                toRight
                xzoom 0.5 yzoom 0.5

            yarik "{b}(сообщение){/b} Прости, но я не смогу, нужно провести время с женой."

            hide телефон гг сообщение_ярик_плохая2

            show телефон гг сообщение_ярик_плохая3:
                toRight
                xzoom 0.5 yzoom 0.5

            gg "{b}(сообщение){/b} Ладно, тогда приходи с Шлепуном."

            $ badEnding += 1
            $ badShlepaRelationship += 1

    jump street_dogEscapedAlena

label street_dogEscapedAlena:

    scene фон улица_день
    with fade

    show гг with dissolve:
        toLeftGG

    show алена без_собаки with dissolve:
        toRightGG

    alenaBeforeNamingHerself "БУСИНКА, БУСИНКА, СТОЙ, ВЕРНИСЬ!"

    $ helpedAlena = False;
    default helpedAlena = False

    menu:
        alenaBeforeNamingHerself "БУСИНКА, БУСИНКА, СТОЙ, ВЕРНИСЬ!"

        "Помочь девушке, поймать собачку и вернуть ей":

            $ helpedAlena = True

            $ goodEnding += 1
            $ goodAlenaRelationship += 1

            jump street_weHelpedAlenaAndReturnedTheDog

        "Пройти мимо":

            $ helpedAlena = False

            $ badEnding += 1
            $ badAlenaRelationship += 1

            jump street_weDidntHelpAlena

label street_weHelpedAlenaAndReturnedTheDog:
    scene фон улица_день

    show гг:
        toLeftGG

    show алена с_собакой:
        toRightGG

    gg "Держите вашего друга, больше не теряйте!"

    alenaBeforeNamingHerself "Господи, спасибо вам большое! Не знаю что бы я делала без вас!" 

    gg "Да не за что, удачи вам!"

    alenaBeforeNamingHerself "А как вас хоть зовут, может мне вас как-нибудь отблагодарить?"

    gg "Я [playerName]."

    alenaBeforeNamingHerself "Приятно познакомиться, [playerName], а меня зовут Алёна!"

    gg "Очень приятно, Алёна! Надеюсь мы как-нибудь ещё увидимся."

    alena "Я тоже! Всего вам хорошего и ещё раз спасибо!!!"
    
    gg "И вам всего хорошего!"

    jump street_afterWeHelpedOrNotAlena


label street_weDidntHelpAlena:

    scene фон улица_день

    show гг:
        toLeftGG

    show алена без_собаки:
        toRightGG

    gg "Я спешу на работу."

    alenaBeforeNamingHerself "Ну что же вы! Мне нужна помощь!"

    jump street_afterWeHelpedOrNotAlena

label street_afterWeHelpedOrNotAlena:

    scene фон улица_день

    show гг:
        toLeftGG

        parallel:
            linear 10.0 xalign 1.0
        parallel:
            linear 0.5 yalign 1.9
            linear 0.5 yalign 2.0
            repeat 16

    pause 10

    jump office_entry

label office_entry:

    scene фон офис общий
    with fade

    show гг:
        toLeftGG

    show сотрудник андрей:
        xalign 0.8 
        yalign 1.0
    
    workerAndry "Здравствуйте, [playerName], у нас тут случилась небольшая неприятность."

    menu:
        workerAndry "Здравствуйте, [playerName], у нас тут случилась небольшая неприятность."

        "Ответить с пониманием":
            gg 'Так, Андрей, я просил обращаться на "ты". Рассказывай, что случилось?'

            workerAndry "Алексей, который отвечал за создание движений персонажа, уехал по неизвестным причинам, а ещё он не отвечает на наши звонки."

            gg "Хорошо, ничего страшного, я пока займусь его задачами, а до него я обязательного дозвонюсь."

            workerAndry "Я понял Вас, больше вопросов нет, пойду работать."

            gg "Тогда у меня есть один вопрос."

            workerAndry "Какой?"

            gg 'Я же просил не обращаться на "Вы".'

            workerAndry "Извиняюсь, больше такого не повторится."

            gg "Ха-ха, всё хорошо, до встречи."

            workerAndry "Пока."

            $ goodEnding += 1
            $ goodCoworkersRelationship += 1
            $ answerToAdnry = 0
        
        "Ответить с гневом":
            gg "Что на этот раз?!"

            workerAndry "Алексей, который отвечал за создание движений персонажа, уехал по неизвестным причинам, а ещё он не отвечает на наши звонки."

            gg "Да что это за безответственность! Я во что бы то ни стало дозвонюсь до него!"

            gg "Передай Николаю, чтобы он сделал задачи за Алексея."

            workerAndry "Конечно, [playerName], я ему передам."

            gg "Так-то лучше. Есть ещё какие-то вопросы или проблемы?"
            
            workerAndry "Нет."

            gg "Тогда свободен."

            workerAndry "До свидания."

            $ badEnding += 1
            $ badCoworkersRelationship += 1
            $ answerToAdnry = 1

    jump office_ggCabinetAfterWeCameToWorkAfterWeHelpedOrNotAlena

screen wipeTheDust:
    vbox xalign 0.9 yalign 0.68:
        imagebutton auto "фотка_шлепуна_пыль %s.png" action [Return(1)]

label office_ggCabinetAfterWeCameToWorkAfterWeHelpedOrNotAlena:

    scene фон офис кабинет_гг_с_пылью_серая_заливка
    with fade

    show гг без_ног:
        toLeftGG
        xalign 0.0

    $ clearPhoto = False
    default clearPhoto = False

    menu:
        "Убрать пыль с рамки с фотографией Шлепуна":

            call screen wipeTheDust

            # if _return == 1:
            #     window hide 
            #     show шлепун довольный:
            #         toLeftShlepa
            #         yalign 0.6

            # pause 1


            scene фон офис кабинет_гг_серая_заливка

            show гг без_ног:
                toLeftGG
                xalign 0.0
            
            $ clearPhoto = True
            $ goodEnding += 1
            $ goodShlepaRelationship += 1
        "Не трогать фотографию":

            $ clearPhoto = False
            $ neutralEnding += 1
            $ neutralShlepaRelationship += 1

    pause 2

    image first_image = "анимация с кодом/0.gif"
    image code_interactive1:
        "анимация с кодом/0.gif"
        0.3
        "анимация с кодом/1.gif"
        0.3
        "анимация с кодом/2.gif"
        0.3
        "анимация с кодом/3.gif"
        0.3
        "анимация с кодом/4.gif"
        0.3
        "анимация с кодом/5.gif"
        0.3
        "анимация с кодом/6.gif"
        0.3
        "анимация с кодом/7.gif"
        0.3
        "анимация с кодом/8.gif"
        0.3
        "анимация с кодом/9.gif"
        0.3
    
    image code_interactive2:
        "анимация с кодом/10.gif"
        0.3
        "анимация с кодом/11.gif"
        0.3
        "анимация с кодом/12.gif"
        0.3
        "анимация с кодом/13.gif"
        0.3
        "анимация с кодом/14.gif"
        0.3
        "анимация с кодом/15.gif"
        0.3
        "анимация с кодом/16.gif"
        0.3
        "анимация с кодом/17.gif"
        0.3
        "анимация с кодом/18.gif"
        0.3
        "анимация с кодом/19.gif"
        0.3
        "анимация с кодом/20.gif"
        0.3

    image code_interactive3:
        "анимация с кодом/21.gif"
        0.3
        "анимация с кодом/21.gif"
        0.3
        "анимация с кодом/22.gif"
        0.3
        "анимация с кодом/23.gif"
        0.3
        "анимация с кодом/24.gif"
        0.3
        "анимация с кодом/25.gif"
        0.3
        "анимация с кодом/26.gif"
        0.3
        "анимация с кодом/27.gif"
        0.3
        "анимация с кодом/28.gif"
        0.3
        "анимация с кодом/29.gif"
        0.3
        "анимация с кодом/30.gif"
        0.3

    if (clearPhoto):
        scene фон офис кабинет_гг_серая_заливка
    else:
        scene фон офис кабинет_гг_с_пылью_серая_заливка

    show гг без_ног:
        toLeftGG
        xalign 0.0

    show first_image:
        xalign 0.4
        yalign 0.14
        xzoom 1.3
        yzoom 1.2

    gg "Что же, приступим к программировнанию."

    $ code_input1 = renpy.input("Напишите {color=#e5ff00}layer.bindPopup(){/color}", exclude=None)
    $ code_input1 = code_input1.strip()

    while (code_input1 != "layer.bindPopup()"):
        pause 1
        gg "Я ошибся, ничего страшного, напишу заново."
        $ code_input1 = renpy.input("Напишите {color=#e5ff00}layer.bindPopup(){/color}", exclude=None)
        $ code_input1 = code_input1.strip()

    pause 1

    show code_interactive1:
        xalign 0.4
        yalign 0.14
        xzoom 1.3
        yzoom 1.2
        
    pause 3

    #gg "Ха, помню похожую задачку на юлёрне, когда еще учился в УРФУ, были времена.... Спасибо Юрий Юлернович!!!"
    $ code_input2 = renpy.input("Напишите {color=#e5ff00}$('select').change(function() {{} );{/color}", exclude=None)
    $ code_input2 = code_input2.strip()

    while (code_input2 != "$('select').change(function() {} );"):
        pause 1
        gg "Я ошибся, ничего страшного, напишу заново."
        $ code_input2 = renpy.input("Напишите {color=#e5ff00}$('select').change(function() {{} );{/color}", exclude=None)
        $ code_input2 = code_input2.strip()

    pause 1

    show code_interactive2:
        xalign 0.4
        yalign 0.14
        xzoom 1.3
        yzoom 1.2
        
    pause 3

    #TODO
    #gg "Спасибо Вам большое, Юрий Юлёрнович!"
    $ code_input3 = renpy.input("Напишите {color=#e5ff00}for (var i = 0; i < response.length; i++){/color}", exclude=None)
    $ code_input3 = code_input3.strip()

    while (code_input3 != "for (var i = 0; i < response.length; i++)"):
        pause 1
        gg "Я ошибся, ничего страшного, напишу заново."
        $ code_input3 = renpy.input("Напишите {color=#e5ff00}for (var i = 0; i < response.length; i++){/color}", exclude=None)
        $ code_input3 = code_input3.strip()

    pause 1

    show code_interactive3:
        xalign 0.4
        yalign 0.14
        xzoom 1.3
        yzoom 1.2
        
    pause 1

    gg "Ха, помню похожую задачку на юлёрне, когда еще учился в УРФУ, были времена.... Спасибо Юрий Юлернович!!!"

    scene чёрный_фон
    with fade

    "(спустя 3 часа работы)"
    
    if (clearPhoto):
        scene фон офис кабинет_гг_серая_заливка
    else:
        scene фон офис кабинет_гг_с_пылью_серая_заливка

    show гг без_ног:
        toLeftGG
        xalign 0.0

    gg "Точно, нужно позвонить Алексею и спросить, где он."

    play sound "audio/исходящий звонок телефона.mp3" fadein 0.5

    pause 5

    stop sound

    show телефон гг разговор_с_алексеем:
        toRight
        xzoom 0.4 yzoom 0.4

    menu:
        "Построить вежливый и понимающий разговор":
            gg "{b}(звонок){/b} Привет, у тебя что-то случилось? Просто не вижу тебя в офисе."

            aleksei "{b}(звонок){/b} Привет, нет, просто мне нужно срочно было по делам вернуться в родной город. Прости что не предупредил, приеду через 2 дня."

            gg "{b}(звонок){/b} Хорошо, я все понимаю, но только не затягивай. "

            gg "{b}(звонок){/b} Знай – с большой силой приходит большая ответственность, не забывай девиз нашей компании."

            aleksei "{b}(звонок){/b} Конечно не забуду, скоро вернусь!"

            $ goodEnding += 1
            $ goodCoworkersRelationship += 1

        "Построить суровый и бесчувственный разговор":
            gg "{b}(звонок){/b} Здравствуй, Алексей. Скажи-ка мне, почему тебя сегодня нет на работе?"

            aleksei "{b}(звонок){/b} Здравствуйте, у меня произошли непредвиденные обстоятельства в жизни, не смог сообщить, извините."

            gg "{b}(звонок){/b} Тогда будь готов к непредвиденным последствиям."

            aleksei "{b}(звонок){/b} Что Вы имеете в виду?"

            gg "{b}(звонок){/b} Ты оштрафован, всю информацию смотри в своём email'е."

            aleksei "{b}(звонок){/b} Обещаю, такого больше не повторится."

            gg "{b}(звонок){/b} Хочу в это верить."

            gg "{b}(звонок){/b} Я думаю, ты забыл наш девиз — c большой силой приходит большая ответственность."

            aleksei "{b}(звонок){/b} Что же Вы, конечно нет."

            gg "{b}(звонок){/b} Смотри у меня."

            gg "{b}(звонок){/b} Даю тебе 2 дня, чтобы ты появился на работе. До встречи!"

            aleksei "{b}(звонок){/b} Я вас понял. До свидания!"

            $ badEnding += 1
            $ badCoworkersRelationship += 1

    hide телефон гг разговор_с_алексеем

    gg "Наш девиз..."

    gg "Дядя Борис, это всё благодаря ему, ещё в детстве он постоянно мне твердил эту поговорку, спасибо тебе!"

    scene чёрный_фон
    with fade

    if (answerToAdnry == 0):
        "Всё остальное время [playerName] продолжал решать задачи Алексея до самого вечера."
    else:
        "Всё остальное время [playerName] решал поставленные перед собой задачи."

    if (clearPhoto):
        scene фон офис кабинет_гг_серая_заливка with fade
    else:
        scene фон офис кабинет_гг_с_пылью_серая_заливка with fade

    show гг без_ног:
        toLeftGG
        xalign 0.0

    play sound "audio/входящий звонок телефона.mp3" fadein 0.5

    pause 5

    stop sound

    show телефон гг разговор_с_яриком:
        toRight
        xzoom 0.4 yzoom 0.4


    yarik "{b}(звонок){/b} Привет, я заеду к тебе домой через час, буду со Шлепуном, всё в силе?"

    gg "{b}(звонок){/b} Да, я тоже скоро приду."

    menu:
        gg "{b}(звонок){/b} Да, я тоже скоро приду."

        "Поскорей бы увидеться со Шлепуном":
            gg '{b}(звонок){/b} Уже скучаю по своему пельмешку...'

            yarik "{b}(звонок){/b} Ха-ха, хорошо, я позвоню."

            $ goodEnding += 1
            $ goodShlepaRelationship += 1

        "Ещё бы отдохноть от Шлепуна":
            gg "{b}(звонок){/b} Опять возиться с ним...."

            yarik "{b}(звонок){/b} Я позвоню."

            $ badEnding += 1
            $ badShlepaRelationship += 1
    
    gg "{b}(звонок){/b} Буду ждать звонок."

    hide телефон гг разговор_с_яриком
    jump cafe_afterYarikCalledUsAndWeConfirmedMeeting

label cafe_afterYarikCalledUsAndWeConfirmedMeeting:

    scene фон улица_вечер
    with fade

    show гг:
        toLeftGG
        parallel:
            linear 8.0  xalign 0.95

        parallel:
            linear 0.3 yalign 1.9
            linear 0.3 yalign 2.0
            repeat 26

    pause 8

    scene фон кафе_вечер
    show гг:
        toLeftGG
        parallel:
            linear 8.0  xalign 0.95

        parallel:
            linear 0.3 yalign 1.9
            linear 0.3 yalign 2.0
            repeat 13

    gg "Хм, как вкусно пахнет рядом с этим кафе! Я обязательно как-нибудь зайду."

    jump home_hall_WhenYarikReturnsOurCat

label home_hall_WhenYarikReturnsOurCat:

    scene фон дом прихожая_закрытая_дверь_вечер
    with fade

    show гг:
        toLeftGG

    play sound "audio/входящий звонок телефона.mp3" fadein 0.5

    pause 5

    stop sound

    show телефон гг разговор_с_яриком:
        toRight
        xzoom 0.4 yzoom 0.4

    yarik "{b}(звонок){/b} Я подъезжаю."

    gg "{b}(звонок){/b} Отлично, иду открывать."
    

    hide телефон гг разговор_с_яриком

    show гг:
        toLeftGG


    scene фон дом прихожая_закрытая_дверь_вечер
    with fade

    show гг:
        toLeftGG

    pause 1.0

    show ярик без_ног:
        toRightYarik

    show шлепун обычный:
        toRightShlepa

        parallel:
            linear 1.0  xalign 0.3

        parallel:
            linear 0.3 yalign 0.9
            linear 0.3 yalign 0.87
            repeat 2


    pause 2

    menu:
        "Обрадоваться возвращению Шлепуна":
            gg "Мой дружок, я очень по тебе соскучился!"

            hide шлепун обычный
            show шлепун довольный:
                toGGShlepa

            play sound "audio/мурчание.mp3" fadein 0.5 volume 0.4 fadeout 0.5

            pause 3

            stop sound fadeout 1.0

            $ goodEnding += 1
            $ goodShlepaRelationship += 1
        
        "Наругать Шлепуна за грязные лапы":
            gg "Шлепун, куда ты бежишь, сначала нужно лапы помыть. Щас мне опять придётся пол затирать."

            $ badEnding += 1
            $ badShlepaRelationship += 1

    gg "Ярик, проходи, чай попьём."

    jump home_kitchen_afterYarikReturnedShlepun

label home_kitchen_afterYarikReturnedShlepun:
    
    #TODO
    scene фон дом прихожая_закрытая_дверь_вечер
    with fade

    show ярик без_ног:
        toRightYarik

    show гг:
        toLeftGG

    show шлепун обычный:
        toGGShlepa

    yarik "Твой Шлепун такой неугомонный, скакал по всем комнатам. Он очень активный."

    gg "Дааа, приходится с ним справляться."

    yarik "Кстати, помнишь то кафе рядом с твоей работой?"

    gg "Да, проходил сегодня мимо."

    yarik "Дак вот, когда я гулял со Шлепуном, он положил глаз на это заведение, видимо там так аппетитно готовили пельмени, что ему очень понравилось. Его буквально тянуло туда."

    menu:
        yarik "Дак вот, когда я гулял со Шлепуном, он положил глаз на это заведение, видимо там так аппетитно готовили пельмени, что ему очень понравилось. Его буквально тянуло туда."

        "Я хочу пойти туда со Шлепуном":
            gg "Тогда мы завтра с ним обязательно зайдем туда. Согласен, Шлепун?"

            hide шлепун обычный
            show шлепун довольный:
                toGGShlepa

            play sound "audio/мурчание.mp3" fadein 0.5 volume 0.4 fadeout 0.5

            pause 3

            stop sound fadeout 1.0

            yarik "Отличная идея!"

            $ goodEnding += 1
            $ goodShlepaRelationship += 1
        "Я хочу туда сходить один":
            gg "Если честно, то у меня нет желания туда идти со Шлепуном, я бы лучше сходил один."

            yarik "Ну он же хочет там покушать."

            gg "Я понимаю, но я не хочу идти с ним."

            $ badEnding += 1
            $ badShlepaRelationship += 1

    hide шлепун довольный
    show шлепун обычный:
        toGGShlepa

    yarik "А как вообще у тебя с работой?"

    menu:
        yarik "А как вообще у тебя с работой?"

        "Лучшая работа и лучшие работники.":
            gg "Все нормально, работники как всегда радают!"

            gg "Сам знаешь, одну фичу добавишь, плюс два бага, как обычно."

            gg "Сейчас работаем над игрой, в основе которой лежит путешествие в чёрную дыру, такого в мире игр я ещё не видел."

            gg "Спасибо моей професси за возможность реализовывать свои мечты!"

            yarik "Успехов тебе, я знаю, что ты со всем справишься!"

            $ goodEnding += 1
            $ goodCoworkersRelationship += 1

        "Лучшая работа и огорчающие работники.":
            gg "Да как обычно, один куда то уехал, другие не справляются с работой. Как я устал от этого..."

            yarik "А ты не думал, что, может, ты с ними слишком строг?"

            gg "Ты правда так думаешь?"

            yarik "Ну, если честно, то да."

            menu:
                yarik "Ну, если честно, то да."

                "Ты прав":
                    gg "Наверное, ты прав... Я попробую пересмотреть своё отношение к ним."

                    $ goodEnding += 1
                    $ goodCoworkersRelationship += 1
                
                "Ты не прав":
                    gg "Я так не считаю. Начальник должен быть требовательным."

                    yarik "Ну, смотри сам."
                    
                    $ badEnding += 1
                    $ badCoworkersRelationship += 1

            $ badEnding += 1
            $ badCoworkersRelationship += 1

    scene чёрный_фон
    with fade

    "(спустя час тёплых разговоров)"

    scene фон дом прихожая_закрытая_дверь_вечер
    with fade


    show ярик без_ног:
        toRightYarik

    show гг:
        toLeftGG

    show шлепун обычный:
        toGGShlepa
    yarik "Ладно, пойду-ка я, жена ждёт."

    gg "Ну, жена это святое, спасибо за то, что посидел со Шлепуном, мы благодарны тебе. Да, Шлепун?"

    hide шлепун обычный
    show шлепун довольный:
        toGGShlepa

    play sound "audio/мурчание.mp3" fadein 0.5 volume 0.4 fadeout 0.5

    pause 3

    stop sound fadeout 1.0

    hide шлепун довольный
    show шлепун обычный:
        toGGShlepa

    yarik "До встречи."

    jump home_bedroom_afterYarikReturnedShlepaAndLeft

label home_bedroom_afterYarikReturnedShlepaAndLeft:

    scene фон дом_гг спальня_вечер_выключенный_свет
    with fade

    show гг:
        вСпальнеМеждуШкафомИКроватью

    show шлепун обычный:
        toLeftShlepa
        yalign 0.6

    menu:
        "Поиграть со Шлепуном":
            gg "Шлепун, давай ко мне, сейчас мы с тобой поиграем!"

            show шлепун обычный:
                toLeftShlepa
                yalign 0.6
                parallel:
                    linear 1.0  xalign 0.75

                parallel:
                    linear 0.2 yalign 0.9
                    linear 0.2 yalign 0.87
                    repeat 2

            pause 2

            scene чёрный_фон
            with fade

            "(спустя час игр со Шлепуном)"

            $ goodEnding += 1
            $ goodShlepaRelationship += 1

        "Не играть со Шлепуном":
            $ badEnding += 1
            $ badShlepaRelationship += 1


    jump home_bedroom_eveningBeforeShlepaLeft

screen shlepa123:
    vbox xalign 0.3 yalign 0.6:
        imagebutton auto "шлепун обычный %s.png" action [SetVariable("flag", True), Return(1)]

label home_bedroom_eveningBeforeShlepaLeft:

    scene фон дом_гг спальня_вечер_выключенный_свет
    with fade

    show гг:
        toCenterGG

    show шлепун обычный:
        toLeftShlepa
        yalign 0.6

    gg "Пора бы уже ложиться нам спать. Пойду открою окно, а то жарко сегодня."

    scene фон дом_гг спальня_вечер_выключенный_свет_открытое_окно
    with fade

    show гг:
        toCenterGG

    show шлепун обычный:
        toLeftShlepa
        yalign 0.6

    gg "Отлично, теперь хоть я не замучаюсь от жары."

    jump home_bedroom_nightWhenShlepaLeft

label home_bedroom_nightWhenShlepaLeft:

    scene фон дом_гг спальня_вечер_выключенный_свет_открытое_окно
    with fade

    show гг:
        toCenterGG

    show шлепун обычный:
        toLeftShlepa
        yalign 0.6

    gg "Пойду-ка я спать."

    $ flag = False
    default flag = False 

    menu:
        gg "Пойду-ка я спать."

        "Погладить Шлепуна": 

            call screen shlepa123
            hide шлепун обычный

            if _return == 1:
                window hide 
                show шлепун довольный:
                    toLeftShlepa
                    yalign 0.6

                play sound "audio/мурчание.mp3" fadein 0.5 volume 0.4 fadeout 0.5

                pause 3

                stop sound fadeout 1.0

            pause 1

            $ goodEnding += 1
            $ goodShlepaRelationship += 1

        "Не гладить Шлепуна":
            $ badEnding += 1
            $ badShlepaRelationship += 1



    hide гг
    
    hide шлепун обычный

    scene чёрный_фон
    with fade

    pause 4

    jump home_bedroom_ggDreamWhenShlepaLeft

label home_bedroom_ggDreamWhenShlepaLeft:
    
    scene фон кафе_вечер
    with fade

    show шлепун обычный:
        xalign 1.3
        yalign 0.8
        xzoom 0.6 yzoom 0.6
        parallel:
            linear 3.6 xalign -0.3
        parallel:
            linear 0.2 yalign 0.82
            linear 0.2 yalign 0.8
            repeat 9

    pause 3.6

label home_bedroom_ggAfterDreamWhenShlepaLeft:

    scene фон дом_гг спальня_вечер_выключенный_свет_открытое_окно
    with fade

    show гг испуг:
        toCenterGG

    gg "Господи, мне такой кошмар приснился."

    hide гг испуг
    show гг испуг_с_руками:
        toCenterGG

    gg "Стоп, а где Шлепун?"

    hide гг испуг_с_руками
    show гг испуг:
        toCenterGG
        parallel:
            linear 2.0 xalign 0.75
        parallel:
            linear 0.2 yalign 1.9
            linear 0.2 yalign 2.0
            repeat 5
    
    gg "Шлепун, кс-кс-кс-кс."

    hide гг испуг
    show гг испуг:
        toRightGG
        xalign 0.75

        parallel:
            linear 2.0 toLeftGG
        parallel:
            linear 0.2 yalign 1.9
            linear 0.2 yalign 2.0
            repeat 5

    gg "Только не это..."

    hide гг испуг
    show гг испуг:
        toLeftGG

        parallel:
            linear 2.0 toCenterGG
        parallel:
            linear 0.2 yalign 1.9
            linear 0.2 yalign 2.0
            repeat 5


    gg "Что делать???"

    pause 2

    gg "Окно... Срочно на улицу!"


label street_NightWhenShlepaLeft:

    scene фон кафе_вечер
    with fade

    show гг испуг:
        toRightGG
        xalign 1.3

        parallel:
            linear 7.0 xalign 0.05
        parallel:
            linear 0.3 yalign 1.9
            linear 0.3 yalign 2.0
            repeat 11
    
    pause 7

    gg "И тут его нет..."

    if (goodShlepaRelationship >= badShlepaRelationship):

        gg "Господи, где Шлепун, я так его люблю, я не знаю как мне теперь жить."

    else:

        gg "Как бы я не относился к Шлепуну, нужно его срочно найти."

    scene фон улица_вечер
    with fade

    show гг испуг:
        toRightGG

        parallel:
            linear 7.0 xalign 0.05
        parallel:
            linear 0.3 yalign 1.9
            linear 0.3 yalign 2.0
            repeat 11
    
    pause 7

    gg "И тут его нет. Где же он?"

    hide гг испуг
    show гг испуг:
        toLeftGG
        xalign 0.05
        

        parallel:
            linear 2.0 toCenterGG
        parallel:
            linear 0.3 yalign 1.9
            linear 0.3 yalign 2.0
            repeat 3
    
    pause 2


    scene фон улица_вечер
    with fade

    #TODO
    image rainGif:
        "rain/0.gif"
        0.05
        "rain/1.gif"
        0.05
        "rain/2.gif"
        0.05
        "rain/3.gif"
        0.05
        "rain/4.gif"
        0.05
        "rain/5.gif"
        0.05
        "rain/6.gif"
        0.05
        "rain/7.gif"
        0.05
        repeat

    show rainGif:
        yzoom 2.0
        xzoom 2.0

    show гг испуг:
        toCenterGG

    stop music fadeout 4.0

    play music "audio/дождь грусть.mp3" fadein 0.5 volume 0.05 fadeout 0.5

    pause 1

    gg "Мне срочно нужно спрятаться от дождя!"

    hide гг испуг
    show гг испуг:
        toCenterGG
        parallel:
            linear 2.0 xalign 0.05
        parallel:
            linear 0.3 yalign 1.9
            linear 0.3 yalign 2.0
            repeat 3
    
    pause 3

    gg "Я не знаю, где искать Шлепуна..."

    if (goodShlepaRelationship >= badShlepaRelationship):
        gg "Я не смогу без него, но я его все равно его найду!"

        gg "Я не представляю своей жизни без него. Шлепун, пожалуйста, вернись!"

    else:
        gg "Я найду Шлепуна любой ценой, ведь мы в ответе за тех, кого приручили."

    gg "..."

    window hide
    pause 2

    gg "Очень сложно сделать что-то сейчас, во время такого ливня."

    gg "Надо возвращаться домой."


    scene фон улица_вечер

    show rainGif:
        yzoom 2.0
        xzoom 2.0

    show гг испуг:
        toLeftGG
        xalign 0.05

        parallel:
            linear 10.0 xalign 1.0
        parallel:
            linear 0.3 yalign 1.9
            linear 0.3 yalign 2.0
            repeat 16

    pause 10

    scene фон кафе_вечер

    show rainGif:
        yzoom 2.0
        xzoom 2.0
    
    show гг испуг:
        xalign 0.0
        yalign 2.0

        parallel:
            linear 10.0 xalign 1.0
        parallel:
            linear 0.3 yalign 1.9
            linear 0.3 yalign 2.0
            repeat 16

    pause 10

    scene фон дом_гг спальня_вечер_выключенный_свет_открытое_окно
    with fade

    show гг испуг with dissolve:
        toCenterGG

    gg "Шлепун..."

    stop music fadeout 2.0

    play music "audio/фоновая музыка.mp3" fadein 4.0 fadeout 4.0 loop volume 0.2

    jump morning_home_AfterShlepaLeft

label morning_home_AfterShlepaLeft:
    
    scene чёрный_фон with fade

    pause 2

    scene фон дом_гг спальня_открытое_окно with fade

    show гг with dissolve:
        toCenterGG

    "Утро после бессоной ночи."

    play sound "audio/исходящий звонок телефона.mp3" fadein 0.5

    pause 5

    stop sound

    show телефон гг разговор_с_яриком:
        toRight
        xzoom 0.4 yzoom 0.4

    gg "{b}(звонок){/b} У меня есть разговор, давай встретимся в том кафе, о котором ты рассказывал мне вчера."

    yarik "{b}(звонок){/b} Без проблем, если что-то случилось, я помогу, а пока не переживай, я слышу по голосу, что что-то не так."

    gg "{b}(звонок){/b} Спасибо за поддержку. Во сколько тебе удобно?"

    yarik "{b}(звонок){/b} Давай встретимся после работы, ты во сколько закончишь?"

    gg "{b}(звонок){/b} В 17:00."

    yarik "{b}(звонок){/b} Тогда договорились, только не волнуйся."

    gg "{b}(звонок){/b} Спасибо тебе большое, мне сейчас как никогда нужна поддержка."

    jump morning_street_AfterShlepaLeft
    
label morning_street_AfterShlepaLeft:
    
    scene фон кафе_день
    with fade

    stop music fadeout 4.0

    play music "audio/грустная песня.mp3" fadein 0.5 fadeout 0.5

    show гг:
        toRightGG
        xalign 1.3

        parallel:
            linear 8.0 xalign 0.05
        parallel:
            linear 0.3 yalign 1.9
            linear 0.3 yalign 2.0
            repeat 13
    
    pause 8

    scene фон улица_день
    with fade

    show гг:
        toRightGG
        xalign 1.3

        parallel:
            linear 8.0 toLeftGG
        parallel:
            linear 0.3 yalign 1.9
            linear 0.3 yalign 2.0
            repeat 13
    
    pause 8

    stop music fadeout 2.0

    play music "audio/фоновая музыка.mp3" fadein 4.0 fadeout 4.0 loop volume 0.2
 
    jump day_job_afterShlepaLeft

label day_job_afterShlepaLeft:

    scene фон офис общий
    with fade

    show гг:
        toLeftGG

    gg "Мне надо собраться перед предстоящим совещанием."

    scene фон офис общий
    with fade

    show гг:
        toLeftGG

    image worker1 = "сотрудник андрей.png"
    image worker2 = "сотрудник андрей.png"
    image worker3 = "сотрудник андрей.png"

    show worker1:
        xalign 0.8
        yalign 1.1
    show worker2:
        xalign 0.9
        yalign 1.15
    show worker3:
        xalign 1.0
        yalign 1.05

    gg "И так, коллеги, сегодня, как и планировалось, у нас проходит совещание. Жду ваши идеи по поводу сюжета нашей игры."

    workers "Наша задача – исследовать один из самых загадочных объектов вселенной! Наверняка там есть жизнь!"

    workers "Возможно мы подтвердим теорию о мультивселенной..."

    gg "Даа, дааа, отличная идея... Напишите мне это всё на почту, я обязательно посмотрю."

    if (goodCoworkersRelationship >= badCoworkersRelationship):
        
        workers "У вас что-то случилось?"

        gg "Нет, просто устал."
    
    gg "Есть ещё какие-то идеи?"

    workers "Пока что мы работаем над управлением корабля, на котором будет совершаться путешествие в чёрную дыру."

    workers "Это пространство оказалось слишком неизведанным, но мы стараемся сделать что-то новое, чего еще не было в игровой индустрии."

    $ replyOnCoworkersIdeas = 0
    menu:
        workers "Это пространство оказалось слишком неизведанным, но мы стараемся сделать что-то новое, чего еще не было в игровой индустрии."

        "Ваши идеи действительно многообещающие":

            gg "Вы действительно придумали что-то, что никогда не встречалось в мире компьютерных игр, молодцы!"

            gg "Видно, что вы не забываете девиз нашей компании – c большой силой приходит большая ответственность!"

            $ replyOnCoworkersIdeas = 1
            $ goodCoworkersRelationship += 1
            $ goodEnding += 1
 
        "Ваши идеи банальны и скучны":

            gg "Вы знаете, можно было придумать что-то поинтереснее. В игру с такой задумкой никому не будет интересно играть."

            gg "Видно, что вы забываете девиз нашей компании – c большой силой приходит большая ответственность!"

            $ replyOnCoworkersIdeas = 0
            $ badCoworkersRelationship += 1
            $ badEnding += 1

    gg "Впрочем, всё равно отправьте мне ваши идеи на почту. Я сейчас не в состоянии их анализировать."

    workers "У Вас точно всё в порядке?"

    menu:
        workers "У Вас точно всё в порядке?"

        "От меня сбежал Шлепун":

            gg "Ладно... В общем, вы все прекрасно знаете моего любимчика, Шлепуна, сегодня ночью он сбежал..."

            gg "Я не знаю что делать..."

            workers "Почему вы сразу нам не сказали?"

            workers "Мы обязательно вам поможем! Вы уже распространили объявления или куда-то обращались?"

            gg "Еще нёт, я был в полной расстерянности."

            workers "Тогда мы займемся распечаткой его фотографий и их расклейкой!"

            gg "Спасибо вам большое, не знаю, чтобы я без вас делал!"

            if (replyOnCoworkersIdeas == 1):
                gg "А на счёт ваших идей, не забудьте мне их скинуть на почту, они все очень хороши."

                gg "Когда всё решится со Шлепуном, мы обязательно вернёмся к этому вопросу."

                workers "Хорошо, только не переживайте, он не мог вас оставить без ведомой на то причины."

            else:
                workers "Только не переживайте, он не мог вас оставить без ведомой на то причины."

            gg "Я тоже так считаю. Спасибо всем, собрание окончено, можем расходиться."

            $ goodCoworkersRelationship += 1
            $ goodEnding += 1

        "[[Умолчать]":

            gg "Даже если у меня что-то случилось, то я не хочу вам об этом рассказывать, это вовсе не обязательно знать."

            workers "Мы просто хотели как лучше."

            gg "Считаю, что собрание пора заканчивать, всем спасибо."

            workers "Как скажите, босс."

            gg "{b}(в мыслях){/b} Займусь пока что распечаткой фотографий Шлепуна для расклейки."

            $ badCoworkersRelationship += 1
            $ badEnding += 1

    jump day_job_afterShlepaLeft_afterCoworkersMeeting

label day_job_afterShlepaLeft_afterCoworkersMeeting:
    
    if (clearPhoto):
        scene фон офис кабинет_гг_серая_заливка with fade
    else:
        scene фон офис кабинет_гг_с_пылью_серая_заливка with fade

    show гг испуг_с_руками:
        toLeftGG
        xalign 0.0
        yalign 3.0

    "Наш [playerName] никогда не чувствовал себя хуже, чем сейчас."


    if (clearPhoto):
        scene фон офис кабинет_гг_серая_заливка with fade
    else:
        scene фон офис кабинет_гг_с_пылью_серая_заливка with fade

    show гг без_ног:
        toLeftGG
        xalign 0.0

    gg "Надо заняться своими задачами."

    image first_image1 = "анимация с кодом/0.gif"
    image code_interactive21:
        "анимация с кодом/0.gif"
        0.1
        "анимация с кодом/1.gif"
        0.1
        "анимация с кодом/2.gif"
        0.1
        "анимация с кодом/3.gif"
        0.1
        "анимация с кодом/4.gif"
        0.1
        "анимация с кодом/5.gif"
        0.1
        "анимация с кодом/6.gif"
        0.1
        "анимация с кодом/7.gif"
        0.1
        "анимация с кодом/8.gif"
        0.1
        "анимация с кодом/9.gif"
        0.1
        "анимация с кодом/10.gif"
        0.1
        "анимация с кодом/11.gif"
        0.1
        "анимация с кодом/12.gif"
        0.1
        "анимация с кодом/13.gif"
        0.1
        "анимация с кодом/14.gif"
        0.1
        "анимация с кодом/15.gif"
        0.1
        "анимация с кодом/16.gif"
        0.1
        "анимация с кодом/17.gif"
        0.1
        "анимация с кодом/18.gif"
        0.1
        "анимация с кодом/19.gif"
        0.1
        "анимация с кодом/20.gif"
        0.1
        "анимация с кодом/21.gif"
        0.1
        "анимация с кодом/21.gif"
        0.1
        "анимация с кодом/22.gif"
        0.1
        "анимация с кодом/23.gif"
        0.1
        "анимация с кодом/24.gif"
        0.1
        "анимация с кодом/25.gif"
        0.1
        "анимация с кодом/26.gif"
        0.1
        "анимация с кодом/27.gif"
        0.1
        "анимация с кодом/28.gif"
        0.1
        "анимация с кодом/29.gif"
        0.1
        "анимация с кодом/30.gif"
        0.1
    image code_interactive22:
        "ошибка в коде/1.gif"
        0.1
        "ошибка в коде/1.gif"
        0.1
        "ошибка в коде/2.gif"
        0.1
        "ошибка в коде/3.gif"
        0.1
        "ошибка в коде/4.gif"
        0.1
        "ошибка в коде/5.gif"
        0.1
        "ошибка в коде/6.gif"
        0.1
        "ошибка в коде/7.gif"
        0.1
        "ошибка в коде/8.gif"
        0.1
        "ошибка в коде/9.gif"
        0.1
        "ошибка в коде/10.gif"
        0.1
        "ошибка в коде/11.gif"
        0.1
        "ошибка в коде/12.gif"
        0.1
        "ошибка в коде/13.gif"
        0.1
        "ошибка в коде/14.gif"
        0.1
        "ошибка в коде/15.gif"
        0.1
        "ошибка в коде/16.gif"
        0.1
        "ошибка в коде/17.gif"
        0.1
        "ошибка в коде/18.gif"
        0.1
        "ошибка в коде/19.gif"
        0.1
        "ошибка в коде/20.gif"
        0.1
        "ошибка в коде/21.gif"
        0.1
        "ошибка в коде/22.gif"
        0.1
        "ошибка в коде/23.gif"
        0.1
        "ошибка в коде/24.gif"
        0.1
        "ошибка в коде/25.gif"
        0.1
        "ошибка в коде/26.gif"
        0.1
        "ошибка в коде/27.gif"
        0.1
        "ошибка в коде/28.gif"
        0.1
        "ошибка в коде/29.gif"
        0.1
        "ошибка в коде/30.gif"
        0.1
        "ошибка в коде/31.gif"
        0.1
        "ошибка в коде/32.gif"
        0.1
        "ошибка в коде/33.gif"
        0.1
        "ошибка в коде/34.gif"
        0.1
        "ошибка в коде/35.gif"
        0.1
        "ошибка в коде/36.gif"
        0.1
        "ошибка в коде/37.gif"
        0.1
        "ошибка в коде/38.gif"
        0.1
        "ошибка в коде/39.gif"
        0.1
        "ошибка в коде/40.gif"
        0.1
        "ошибка в коде/41.gif"
        0.1
        "ошибка в коде/42.gif"
        0.1
        "ошибка в коде/43.gif"
        0.1
        "ошибка в коде/44.gif"
        0.1
        "ошибка в коде/45.gif"
        0.1
        "ошибка в коде/46.gif"
        0.1

    show first_image1:
        xalign 0.4
        yalign 0.14
        xzoom 1.3
        yzoom 1.2


    gg "Как я сделаю свои задачи в таком состоянии..."

    $ code_input21 = renpy.input("Напишите {color=#e5ff00}ضافةلكلمةمعرفكلمةلموضعالسابق{/color}", exclude=None)

    pause 1

    gg "Я не понимаю..."

    $ code_input21 = renpy.input("Напишите {color=#e5ff00}ضافةلكلمةمعرفكلمةلموضعالسابق{/color}", exclude=None)

    pause 1

    gg "Что делать..."

    pause 1

    show code_interactive21:
        xalign 0.4
        yalign 0.14
        xzoom 1.3
        yzoom 1.2

    pause 3.2

    show code_interactive22:
        xalign 0.368
        yalign 0.1
        xzoom 1.923
        yzoom 1.303
    
    pause 4.8

    gg "Я не могу погрузиться в работу, всё валится из рук из-за случившегося..."

    hide гг

    if (clearPhoto):
        scene фон офис кабинет_гг_серая_заливка with fade
    else:
        scene фон офис кабинет_гг_с_пылью_серая_заливка with fade

    show гг без_ног:
        toLeftGG

    play sound "audio/исходящий звонок телефона.mp3" fadein 0.5

    pause 5

    stop sound

    show телефон гг разговор_с_яриком with dissolve:
        toRight 
        xzoom 0.4 yzoom 0.4

    pause 1

    gg "{b}(звонок){/b} Алё. Всё в силе?"

    yarik "{b}(звонок){/b} Да, конечно. Что у тебя с голосом? Я переживаю!"

    gg "{b}(звонок){/b} Расскажу всё при встрече."

    yarik "{b}(звонок){/b} Ты меня пугаешь... Уже выезжаю."

    gg "{b}(звонок){/b} Хорошо, я тоже уже выхожу, до встречи."

    yarik "{b}(звонок){/b} До встречи."

    stop music fadeout 4.0

    play music "audio/грустная песня.mp3" fadein 0.5 fadeout 0.5

    jump scene30

label scene30:

    scene фон улица_день
    with fade

    show гг:
        xalign 0.05
        yalign 2.0
        parallel:
            linear 5 xalign 0.4
        parallel:
            linear 0.3 yalign 1.9
            linear 0.3 yalign 2.0
            repeat 8
        
    pause 5

    "Шлепун..."

    stop music fadeout 4.0

    play music "audio/музыка воспоминаний.mp3" fadein 3.0 volume 0.3 loop

    scene белый_фон 
    with dissolve

    show гг with dissolve:
        toLeftGG

    show шлепун обычный with dissolve:
        toRightShlepa
        yalign 0.85

    gg "Шлепун, любимый, беги ко мне!"

    hide шлепун обычный
    show шлепун обычный:
        toRightShlepa
        yalign 0.85
        parallel:
            linear 1.0 toGGShlepa yalign 0.87
        parallel:
            linear 0.2 yalign 0.85
            linear 0.2 yalign 0.87
            repeat 2
    
    pause 1

    gg "Умничка, пельмешек мой!"

    window hide

    hide шлепун обычный
    show шлепун довольный:
        toGGShlepa yalign 0.87

    pause 1.5

    scene белый_фон 
    with dissolve

    show гг with dissolve:
        toLeftGG

    show шлепун обычный with dissolve:
        toGGShlepa
        yalign 0.85

    gg "Шлепун, давай наперегонки побегаем до конца улицы."

    gg "На счёт три."

    gg "Раз..."

    gg "Два..."

    gg "Три!"

    window hide

    hide гг
    show гг:
        toLeftGG
        parallel:
            linear 3.0 xalign 0.95
        parallel:
            linear 0.3 yalign 1.9
            linear 0.3 yalign 2.0
            repeat 5

    hide шлепун обычный
    show шлепун обычный:
        toGGShlepa
        yalign 0.85
        parallel:
            linear 1.6 xalign 1.05 yalign 0.87
        parallel:
            linear 0.2 yalign 0.85
            linear 0.2 yalign 0.87
            repeat 3

    pause 3

    gg "Ух, Шлепун, за тобой не угнаться."

    gg "Молодчина, пельмешек мой!"

    window hide

    hide шлепун обычный
    show шлепун довольный:
        xalign 1.05 yalign 0.87
        xzoom 0.6 yzoom 0.6

    pause 1.5

    stop music fadeout 2.0

    play music "audio/грустная песня.mp3" fadein 0.5 fadeout 0.5

    scene фон улица_день
    with fade

    show гг:
        toCenterGG
        xalign 0.4 yalign 2.0

    if (goodShlepaRelationship >= badShlepaRelationship):
        gg "Я обязан найти Шлепуна!"

    else:
        gg "Конечно, я не очень хорошо относился к Шлепуну, но я обязан найти его!"

    gg "«Мы в ответе за тех кого приручили»"

    gg "Шлепун..."

    hide гг
    show гг:
        toCenterGG
        xalign 0.4 yalign 2.0
        parallel:
            linear 6 xalign 0.95
        parallel:
            linear 0.3 yalign 1.9
            linear 0.3 yalign 2.0
            repeat 10
        
    pause 6

    stop music fadeout 4.0

    play music "audio/фоновая музыка.mp3" fadein 4.0 fadeout 4.0 loop volume 0.2

    jump scene31

label scene31:

    if (goodCoworkersRelationship >= badCoworkersRelationship):

        scene фон кафе_день_с_листовками
        with fade

        show гг:
            toLeftGG
            xalign 0.05
            parallel:
                linear 3 xalign 0.25
            parallel:
                linear 0.3 yalign 1.9
                linear 0.3 yalign 2.0
                repeat 5

        show worker1:
            xalign 0.5
            yalign 1.1
        show worker2:
            xalign 0.6
            yalign 1.15
        show worker3:
            xalign 0.7
            yalign 1.05
        
        pause 3

        gg "Даже не знаю, как я могу вас отблагадорить, вы не представляете, как много для меня это значит."

        workers "Нам только в радость помогать Вам, Вы очень хороший начальник, мы просто относимся к Вам так же, как и Вы к нам."

        gg "Мне очень приятно, но мне пора идти на встречу."

        workers "Пока!"

        gg "Пока."

    else:

        scene фон кафе_день
        with fade

        show гг:
            toLeftGG
            xalign 0.05
            parallel:
                linear 6.5 xalign 0.8
            parallel:
                linear 0.3 yalign 1.9
                linear 0.3 yalign 2.0
                repeat 10
        
        pause 6

        gg "Пожалуй, размещу фотографию здесь."

        pause 1

        scene фон кафе_день_с_листовками

        show гг:
            xalign 0.8 yalign 2.0

        pause 0.5

        gg "Надеюсь, это поможет."

    jump scene33

#scene32 is empty

label scene33:

    scene фон кафе_внутри
    with fade

    show гг with dissolve:
        toLeftGG
        xalign 0.35

    gg "Время 16:50, Ярика еще нету, пока присяду за какой-нибудь столик."

    gg "Какой аппетитный аромат пельменей, нужно заказать что-нибудь."

    show официант:
        toRight
        yalign 1.0
        xalign 0.7

    waiter "Вы готовы сделать заказ?"

    gg "Да, принесите, пожалуйста, ваши фирменные пельмени, на всё кафе стоит такой чудесный аромат, аж слюнки текут."

    workers "С удовольствием!"

    window hide
    hide официант

    pause 1

    show ярик with dissolve:
        toRightGG
        xalign 0.02

    gg "Ярик, привет."

    yarik "Привет, я очень переживал, давай, рассказывай быстрее, что случилось."

    gg "Даже не знаю с чего начать. Если кратко – Шлепун пропал."

    gg "Когда я проснулся, окно было открыто, а его не было, я не могу даже описать свои эмоции."

    gg "Сегодня мне нужно все обдумать."

    yarik "Шлепун... Ещё вчера он был с нами, куда он мог деться?"

    gg "Я тоже не понимаю!"

    yarik "Так, для начала нужно всё продумать и понять, почему он ушел."

    yarik "Даже не сомневайся, мы его найдем, Шлепун очень любит тебя и не мог уйти без весомой причины, я уверен!"

    menu:
        yarik "Даже не сомневайся, мы его найдем, Шлепун очень любит тебя и не мог уйти без весомой причины, я уверен!"

        "Я тоже люблю Шлепуна":

            gg "Я тоже его люблю, надеюсь он скоро найдется..."

            $ goodShlepaRelationship += 1
            $ goodEnding += 1

        "Он не мог далеко убежать":

            gg "Да вернется он, далеко не мог убежать."

            $ badShlepaRelationship +=1
            $ badEnding += 1 
    
    show алена без_собаки:
        toRightGG
        xalign 1.3
        parallel:
            linear 3.0 xalign 0.6
        parallel:
            linear 0.3 yalign 2.0
            linear 0.3 yalign 1.9
            repeat 5

    show пельмени:
        toRightGG
        xalign 1.2
        xzoom 0.1
        yzoom 0.1
        parallel:
            linear 3.0 xalign 0.55
        parallel:
            linear 0.3 yalign 0.4
            linear 0.3 yalign 0.405
            repeat 5
    
    pause 3


    if (helpedAlena):

        alena "Здравствуйте, вот ваш заказ... [playerName]? Это вы? Какая неожиданная встреча."

        hide пельмени
        show пельмени:
            xalign 0.2
            yalign 0.72
            xzoom 0.1
            yzoom 0.1

        gg "Алёна! Здравствуйте, знакомьтесь, это мой друг Ярослав."

        yarik "Да, здравствуйте, очень приятно."

        alena "[playerName], у вас что-то случилось? А то вы выглядите не очень?"

        gg "Если честно, то мой питомец пропал."

        alena "Ужас какой, прям как моя собачка, если бы не вы..."

        alena "Спасибо вам за тот случай, не знаю как я жила бы без своей любимки. Я могу вам чем-то помочь?"
        
        gg "Пока я даже не знаю, только если поможете в его поисках." 
        
        alena "С радостью, зовите когда я понадоблюсь, вот вам мой номер."

        gg "Спасибо вам... Может, присядете?"

        alena "Ну только если на несколько минут."


    else:

        alenaBeforeNamingHerself "Здравствуйте, вот ваш заказ... Молодой человек, мы с вами не встречались?"

        hide пельмени
        show пельмени:
            xalign 0.2
            yalign 0.72
            xzoom 0.1
            yzoom 0.1

        gg "Хм..."

        gg "Да, встречались. У вас убежала собака, а я проходил мимо."

        alenaBeforeNamingHerself "А, вспомнила, вы не помогли мне, моя собачка чуть не убежала, но я ее поймала."

        gg "Предлагаю начать наше знакомоство сначала. Простите меня за тот случай, не знаю, что на меня нашло."

        alenaBeforeNamingHerself "Хорошо, наверное вы просто куда-то спешили, опустим эту ситуации. Вы плохо выглядите, у вас что-то случилось?"

        gg "Ещё раз извините, может, присядите?"

        alenaBeforeNamingHerself "Ну только если на несколько минут."

        gg "Как вас зовут?"

        alenaBeforeNamingHerself "Я Алёна, а вы?"
        
        gg "Меня зовут [playerName]."

    alena "Кстати, представляете, сегодня ночью кто то стащил наши фирменные пельмешки с холодильника!"

    alena "Никаких следов и отпечатков не оставили, как будто работали в перчатках, надеюсь, что это больше не повториться."        

    gg "Дааа, «хорошая» ночка сегодня выдалась..."

    yarik "Странно, что у меня ничего не произошло! Хотя нет, произошло, с женой поругался."

    gg "Ну вот, у всех что-то случилось сегодня ночью."

    yarik "Так, мы собрались тут, чтобы помочь, расскажи, что ты сейчас собираешься делать?"

    gg "Сегодня я всё ещё раз обдумаю, составлю примерную карту, куда он мог пойти, и завтра решим, где искать."

    yarik "Хорошо."

    alena "Отличная идея, но для начала съешьте все таки наши фирменные пельмени, а то они стоят и стоят"

    gg "Ах, да, совсем забыл, сейчас отведаю!"

    alena "Простите, мне правда пора уже идти работать, а то и так из-за пельменей ещё влетит..."
    
    alena "В общем, приятно было познакомиться, звоните, если что, ещё раз, не расстраивайтесь, всё наладится."

    gg "Мне тоже было очень приятно познакомиться, до встречи, постараюсь не грустить."

    alena "Да, согласен с Алёной, мне тоже уже пора, с женой еще мириться нужно. Ты знаешь, я всегда на связи и, если что, буду рядом, звони, до встречи!"

    gg "Всем пока, сейчас доем, кстати, очень вкусные пельмешки и тоже пойду домой."


    scene фон кафе_день_с_листовками
    with fade
    
    play sound "audio/грустная песня.mp3" fadein 0.5 fadeout 0.5 volume 0.2

    show гг:
        toCenterGG
        parallel:
            linear 4.0 xalign 1.0
        parallel:
            linear 0.3 yalign 1.9
            linear 0.3 yalign 2.0
            repeat 3

    pause 3

    gg "Я найду Шлепуна в любом случае."

    stop sound

    jump scene34

label scene34:

    scene фон дом прихожая_закрытая_дверь_вечер
    with fade

    show гг:
        toLeftGG

    gg "После разговора с ребятами легче не стало..."

    gg "Эх, помню, как я грустил из-за расставания с девушкой во времена учебы в УрФУ."

    gg "Тогда я занимался разработкой игры, визуальной новеллы, про свою бывшую девушку."

    gg "Помню, как она стала популярной и девушка захотела вернуться ко мне, только уже не по любви, а потому что я стал широко известным."

    gg "Стоп. Стоп. Стоп. Вернулась... Разработчик игр... Точно!!!"

    gg "Я буду писать игру про своего Шлепуна, нужно сделать это как можно быстрее, я должен осветить это на весь мир, чтобы точно найти Шлепуна."

    gg "Решено. Сколько раз меня еще выручит моя профессия?!"

    gg "Пойду в ванну и спать, нужно хорошенько выспаться, чтобы точно сделать игру лучшей из лучших!!!"

    gg "Всё, нельзя медлить, допиваю чай и в кровать, как говориться – утро вечера мудренее!"

    scene фон дом_гг спальня_вечер_выключенный_свет with fade

    show гг:
        toCenterGG

    gg "Так, всё, пора ложиться."

    scene чёрный_фон with fade

    pause 3

    scene белый_фон with dissolve

    show шлепун обычный with fade:
        toCenter

    pause 2

    hide шлепун обычный
    show шлепун довольный:
        toCenter
        
    pause 1

    scene фон дом_гг спальня with fade

    show гг:
        toCenterGG 

    gg "Шлепун..."

    jump scene35

label scene35:

    if (clearPhoto):
        scene фон офис кабинет_гг_серая_заливка with fade
    else:
        scene фон офис кабинет_гг_с_пылью_серая_заливка with fade

    show гг без_ног:
        toLeftGG

    show телефон гг разговор_с_яриком_и_аленой:
        toRight
        xzoom 0.4 yzoom 0.4

    play sound "audio/исходящий звонок телефона.mp3" fadein 0.5

    pause 5

    stop sound

    gg "{b}(звонок){/b} В общем, я знаю, что делать, Алёна, предлагаю тебе поискать Шлепуна там, где мы с тобой встретились первый раз."

    gg "{b}(звонок){/b} Я буду разрабатывать про него игру, чтобы как можно больше людей узнали о моём питомце, так намного быстрее получится найти Шлепуна, как вам идея?"

    yarik "{b}(звонок){/b} [playerName], ты гений!"

    $ alenaAgreedToHelp = False
    default alenaAgreedToHelp = False

    if (goodAlenaRelationship >= badAlenaRelationship):

        alena "{b}(звонок){/b} Да, согласна с Яриком, буду стараться найти Шлепуна вместе с Бусинкой!"

        gg "{b}(звонок){/b} Спасибо вам большое! А я пойду работать над игрой"

        gg "{b}(звонок){/b} Ах да, Ярик, а ты постарайся поискать Шлепуна там, где вы гуляли, может он где-то там..."

        gg "{b}(звонок){/b} Я тоже буду стараться искать его в перерывах между разработкой игры."

        yarik "{b}(звонок){/b} Без проблем, [playerName]."

        gg "{b}(звонок){/b} Отлично! Тогда всем до встречи."

        alena "{b}(звонок){/b} До встречи."

        yarik "{b}(звонок){/b} До встречи."

        $ alenaAgreedToHelp = True
    
    else:

        alena "{b}(звонок){/b} Прости, [playerName], но я не смогу помочь."

        gg "{b}(звонок){/b} Ладно, прости за беспокойство. Буду работать над игрой."

        gg "{b}(звонок){/b} Ах, да, Ярик, а ты постарайся поискать Шлепуна там, где вы гуляли, может он где-то там..."

        gg "{b}(звонок){/b} Я тоже буду стараться искать его в перерывах между разработкой игры."

        yarik "{b}(звонок){/b} Я помогу найти Шлепуна!"

        gg "{b}(звонок){/b} Отлично! Тогда всем до встречи."

        yarik "{b}(звонок){/b} До встречи."

        $ alenaAgreedToHelp = False

    jump scene36

label scene36:

    scene фон офис общий with fade

    show гг:
        toLeftGG

    gg "Объявляю срочное собрание!"

    image worker1 = "сотрудник андрей.png"
    image worker2 = "сотрудник андрей.png"
    image worker3 = "сотрудник андрей.png"

    show worker1:
        xalign 0.8
        yalign 1.1
    show worker2:
        xalign 0.9
        yalign 1.15
    show worker3:
        xalign 1.0
        yalign 1.05

    gg "Надеюсь, все пришли. Значит так, после последнего собрания я понял, что ваши идеи на вес золота, поэтому разработку игры про путешествие в чёрную дыру я доверяю полностью вам."

    gg "Это окончательное решение, вы справитесь без меня, главное помните – с большой силой приходит большая ответственность."

    workers "Это большая честь для нас! А как там Шлепун, он нашёлся? Чем будете заниматься Вы?"

    gg "У меня есть грандиозный план, скоро узнаете, я уверен, что он найдется, собрание окончено, спасибо всем, за работу!"

    hide worker1
    hide worker2
    hide worker3

    gg "Что же, начало разработки игры положено. Буду трудиться и день и ночь."

    jump scene37

screen downloadRenpy:
    vbox xalign 0.407 yalign 0.35:
        imagebutton auto "download RenPy %s.png" action [SetVariable("flag1", True), Return(1)]

screen buildGame:
    vbox xalign 0.565 yalign 0.44:
        imagebutton auto "build game %s.png" action [SetVariable("flag2", True), Return(1)]

label scene37:

    stop music fadeout 4.0

    play sound "audio/интенсивная музыка.mp3" fadein 4.0 fadeout 2.0 loop volume 0.1

    $ flag1 = False
    default flag1 = False 

    $ flag2 = False
    default flag2 = False 

    if (clearPhoto):
        scene фон офис кабинет_гг_белая_заливка with fade
    else:
        scene фон офис кабинет_гг_с_пылью_белая_заливка with fade

    show гг без_ног:
        toLeftGG
        xalign 0.0

    show ренпай оф_сайт:
        xzoom 0.5
        yzoom 0.5
        xalign 0.4
        yalign 0.14

    pause 1

    "Скачайте движок для создания игры."

    call screen downloadRenpy

    # if _return == 1:
    #     window hide 
    #     show шлепун довольный:
    #         toLeftShlepa
    #         yalign 0.6


    scene фон дом_гг спальня_вечер_выключенный_свет with fade

    show гг:
        toCenterGG

    pause 1

    scene чёрный_фон with fade

    pause 1

    scene фон дом_гг спальня with fade

    show гг:
        toCenterGG

    pause 1

    if (clearPhoto):
        scene фон офис кабинет_гг_кодвс_заливка with fade
    else:
        scene фон офис кабинет_гг_с_пылью_кодвс_заливка with fade

    show гг без_ног:
        toLeftGG
        xalign 0.0

    show визуалка код_до_никиты:
        toCenter
        xalign 0.325
        yalign 0.15

    $ code_input31 = renpy.input("Напишите {color=#e5ff00}define nikita = Character('Никита', color=\"#f12b10\"){/color}", exclude=None)
    $ code_input31 = code_input31.strip()

    while (code_input31 != "define nikita = Character('Никита', color=\"#f12b10\")"):
        pause 1
        gg "Я ошибся, ничего страшного, напишу заново."
        $ code_input31 = renpy.input("Напишите {color=#e5ff00}define nikita = Character('Никита', color=\"#f12b10\"){/color}", exclude=None)
        $ code_input31 = code_input31.strip()

    show визуалка код:
        toCenter
        xalign 0.325
        yalign 0.15

    pause 3

    scene фон дом_гг спальня_вечер_выключенный_свет with fade

    show гг:
        toCenterGG

    pause 1

    scene чёрный_фон with fade

    pause 1

    scene фон дом_гг спальня with fade

    show гг:
        toCenterGG

    pause 1

    if (clearPhoto):
        scene фон офис кабинет_гг_белая_заливка with fade
    else:
        scene фон офис кабинет_гг_с_пылью_белая_заливка with fade

    show гг без_ног:
        toLeftGG
        xalign 0.0

    show билд ренпай:
        xalign 0.39 yalign 0.1
        xzoom 0.78
        yzoom 0.78

    pause 1

    "Соберите игру."

    call screen buildGame

    stop sound fadeout 2.0

    play music "audio/фоновая музыка.mp3" fadein 4.0 fadeout 4.0 loop volume 0.2

    jump scene38

label scene38:

    hide билд ренпай

    show фон офис общий with fade

    show гг:
        toLeftGG

    gg "Игра наконец-то готова, моя команда её выложила и у неё шикарные оценки пользователей. Это успех."

    gg "За считанные дни все игровые журналы разрываются от рецензий на новую визуальную новеллу про Шлепуна."
    
    gg "Она даже обгоняет популярную игру про котика - SСat."

    jump scene39

label scene39:
    
    scene фон кафе_внутри
    with fade

    show гг with dissolve:
        toLeftGG
        xalign 0.35

    show ярик with dissolve:
        toRightGG
        xalign 0.02

    show алена без_собаки:
        toRightGG
        xalign 1.3
        parallel:
            linear 3.0 xalign 0.6
        parallel:
            linear 0.3 yalign 2.0
            linear 0.3 yalign 1.9
            repeat 5

    pause 3

    gg "Я знал, игра понравится людям, надеюсь, другие помогут мне в поиске Шлепуна."

    if (alenaAgreedToHelp):

        gg "А как ваши успехи в поисках?"

        alena "Я каждый день искала Шлепуна в разных местах, но даже зацепок не было..."

        yarik "У меня тоже... Я обошел все места прогулки с Шлепуном, его там не было.."

        gg "У меня тоже попытки не увенчались успехом... Последние надежды остаются только на игру."

        alena "Точно найдутся люди, которые увидят Шлепуна и благодаря твоей замечательной игре сообщат тебе."

        gg "Спасибо, Алёна. Ладно, пора мне уже, пойду ещё искать Шлепуна, раз игра готова, остаются только поиски и надежда на звонок..."

        yarik "Давай, [playerName], удачи, я тоже продолжу поиски, всем пока."

        alena "Я тоже продолжу, до встречи."

        gg "Удачи всем!"

    else:

        gg "Ярик, как твои успехи в поисках?"

        yarik "Я обошёл все места, где я гулял со Шлепуном, его там не было..."

        gg "У меня тоже попытки не увенчались успехом... Последние надежды остаются только на игру."

        alena "Точно найдутся люди, которые увидят Шлепуна и благодаря твоей замечательной игре сообщат тебе."

        menu:
            alena "Точно найдутся люди, которые увидят Шлепуна и благодаря твоей замечательной игре сообщат тебе."

            "Спасибо за поддержку, Алёна":

                gg "Спасибо, Алёна... Я очень благодарен тебе за поддержку. Надеюсь, ты больше на меня не в обиде."

                $ goodAlenaRelationship = max(badAlenaRelationship + 1, goodAlenaRelationship)

            "Я тоже так думаю":

                gg "Да, я тоже так думаю."

    jump scene40

label scene40:

    scene фон дом прихожая_закрытая_дверь_день with fade

    show гг:
        toLeftGG

    pause 1

    play sound "audio/входящий звонок телефона.mp3" fadein 0.5

    pause 5

    stop sound

    show телефон гг разговор_с_неизвестным:
        toRight
        xzoom 0.4 yzoom 0.4

    gg "{b}(звонок){/b} Да, кто это?"

    nikitaBeforeNamingHimself "{b}(звонок){/b} Алё, это [playerName]?"

    gg "{b}(звонок){/b} Да, верно, что Вы хотели?"

    nikitaBeforeNamingHimself "{b}(звонок){/b} Мне кажется, мы с вами знакомы, ваша игра просто шикарна." 

    nikitaBeforeNamingHimself "{b}(звонок){/b} Кажется, она помогла вам найти вашу пропажу так же, как и в концовке вашей игры."

    gg "{b}(звонок){/b} ЧТО ВЫ ГОВОРИТЕ, ШЛЕПУН НАШЕЛСЯ, ГДЕ ВЫ, Я СКОРО ПРИБУДУ, СКАЖИТЕ МЕСТО."

    nikitaBeforeNamingHimself "{b}(звонок){/b} Там же, где и происходила концовка вашей игры."

    jump scene41

label scene41:

    scene фон дом прихожая_закрытая_дверь_день with fade

    show гг:
        toCenterGG

    gg "Он сказал прийти в то же место, где и происходила концовка моей игры."

    gg "Этот же тот парк, где шёл дождь, когда Шлепун потерялся."

    gg "Нужно срочно выдвигаться туда. В игре время встречи было 17:00. Приду в этот же час."

    jump scene42

label scene42:

    scene фон улица_день with fade

    show гг:
        toLeftGG
        xalign -0.5
        parallel:
            linear 3.0 xalign 0.3
        parallel:
            linear 0.3 yalign 2.0
            linear 0.3 yalign 1.9
            repeat 5

    pause 3

    show никита:
        toRightGG
        xalign 1.5
        parallel:
            linear 3.0 xalign 0.8
        parallel:
            linear 0.3 yalign 1.2
            linear 0.3 yalign 1.25
            repeat 5

    pause 3

    gg "Здравствуйте, это Вы звонили мне?"

    gg "Никита? Никита! Это ты! Сколько мы уже не виделись? После учебы, ни разу???"

    nikita "Да, привет, [playerName], не думал, что наша встреча пройдёт именно так."

    gg "Даа, я тоже."

    window hide

    show шлепун обычный:
        toRightShlepa
        xalign 1.3

        parallel:
            linear 2.0 xalign 0.4

        parallel:
            linear 0.3 yalign 0.9
            linear 0.3 yalign 0.87
            repeat 4
        
    pause 2

    play sound "audio/мурчание.mp3" fadein 0.5 volume 0.4 fadeout 0.5

    window hide

    hide шлепун обычный
    show шлепун довольный:
        toLeftShlepa
        xalign 0.4
        yalign 0.87

    pause 3

    stop sound fadeout 1.0

    if (goodEnding >= badEnding):
        jump goodEndingGeneral
    else:
        jump badEndingGeneral

label goodEndingGeneral:

    scene фон улица_день

    show гг:
        toLeftGG
        xalign 0.3
        yalign 1.9

    show никита:
        toRightGG
        yalign 1.25

    show шлепун довольный:
        toLeftShlepa
        xalign 0.4
        yalign 0.87

    gg "Мальчик мой, где же ты был... Как я соскучился!"

    nikita "Ха-ха-ха, какие прелести. Он очень скучал по тебе!!!"

    gg "Я тоже!"

    nikita "Наверно тебе интересно, как всё же я его нашел."

    gg "Ещё бы!"

    hide шлепун довольный
    show шлепун обычный:
        toLeftShlepa
        xalign 0.4
        yalign 0.87

    nikita "Я преподаю информатику в одной из школ."

    nikita "Один из учеников 11 класса показал мне твою игру. Я решил её полностью пройти."

    nikita "Мне запомнилась та пельменная, на которую Шлепун обратил внимание после прогулки с Яриком." 

    nikita "Эта игра, как я понял, основана на реальной истории?"

    gg "Да, все действия в игре были взяты из жизни."

    nikita "Дак вот, я подумал, что Шлепун сбежал именно туда. Как раз такой вывод я сделал за тебя."

    nikita "А потом я понял, как тебе тяжело сейчас, и решил заняться реальным поиском Шлепуна."

    nikita "Угадай, где пропадал этот красивый зверек???"

    gg "Только не говори, что в той пельменной."

    nikita "Именно там!!! Когда я проходил мимо, он выбежал ко мне, уж не знаю, откуда он там взялся, но от него точно пахло пельмешками!!! Ха-ха-ха."

    gg "Как же я рад, что Шлепун нашёлся!"

    gg "А те пельмешки правда были такие вкусные, теперь я понимаю, почему Шлепун убежал, ха-ха-ха!"

    nikita "Это благодаря тебе Шлепун нашёлся, если бы не твоя игра, я бы вряд ли встретился с тобой и узнал о пропаже твоего питомца."

    nikita "Во всяком случае, я был очень рад с тобой увидеться."

    nikita "Может как-нибудь ещё соберемся, ты, я и Шлепун. Вспомним старые времена во время учебы."

    gg "Да, мы только за!"

    play sound "audio/мурчание.mp3" fadein 0.5 volume 0.4 fadeout 0.5

    window hide

    hide шлепун обычный
    show шлепун довольный:
        toLeftShlepa
        xalign 0.4
        yalign 0.87

    pause 3

    hide шлепун довольный
    show шлепун обычный:
        toLeftShlepa
        xalign 0.4
        yalign 0.87

    nikita "Отлично! Тогда до встречи!"

    gg "До встречи, спасибо тебе ещё раз, я твой должник!!!"

    nikita "Да ты чего, приятно было помочь тебе, друг."

    gg "Всё равно, спасибо тебе, друг."

    nikita "Ещё увидимся, не теряй больше такого милашку."

    gg "Больше никогда не потеряю!!!"

    hide никита
    show никита:
        toRightGG
        yalign 1.2

        parallel:
            linear 3.0 xalign 1.3
        parallel:
            linear 0.3 yalign 1.2
            linear 0.3 yalign 1.25
            repeat 5

    pause 3

    hide никита

    hide гг
    show гг:
        toLeftGG
        xalign 0.3
        yalign 1.9
        parallel:
            linear 2.0 xalign 0.5
        parallel:
            linear 0.3 yalign 2.0
            linear 0.3 yalign 1.9
            repeat 3

    hide шлепун обычный
    show шлепун обычный:
        toLeftShlepa
        xalign 0.4
        yalign 0.87

    pause 2

    play sound "audio/исходящий звонок телефона.mp3" fadein 0.5

    pause 5

    stop sound

    show телефон гг разговор_с_яриком:
        toRight
        xzoom 0.4
        yzoom 0.4

    gg "{b}(звонок){/b} ШЛЕПУН НАШЕЛСЯ!!!"

    yarik "{b}(звонок){/b} УРААА, НЕУЖЕЛИ, А КАК ИЛИ КТО ЕГО НАШЕЛ!!"

    gg "{b}(звонок){/b} НИКИТА! Помнишь? Мы с ним учились."

    yarik "{b}(звонок){/b} Даа, помню, общительный такой был."

    gg "{b}(звонок){/b} Да, он сказал, что нашёл Шлепуна благодаря моей игре. А нашёл он его у той пельменной, где работает Алёна."

    yarik "{b}(звонок){/b} Точно!!! Как мы сами не додумались, он же так смотрел на это кафе во время прогулки со мной."

    gg "{b}(звонок){/b} Даа, я и сам не понимаю. Главное, что сейчас Шлепун с нами."

    gg "{b}(звонок){/b} Ладно, пойду к Алёне, расскажу ей."

    yarik "{b}(звонок){/b} Передай привет Шлепуну, пока!"

    gg "{b}(звонок){/b} Обязательно! Пока!"

    scene фон улица_день

    show гг:
        toCenterGG
        xalign 0.5
        yalign 1.9
        parallel:
            linear 5.0 xalign 1.3
        parallel:
            linear 0.3 yalign 2.0
            linear 0.3 yalign 1.9
            repeat 9
    
    show шлепун обычный:
        toLeftShlepa
        xalign 0.4
        yalign 0.87
        parallel:
            linear 5.0 xalign 1.3
        parallel:
            linear 0.3 yalign 0.9
            linear 0.3 yalign 0.87
            repeat 9

    pause 5

    scene фон кафе_день

    show гг:
        toLeftGG
        xalign -0.3
        parallel:
            linear 5.0 xalign 0.7
        parallel:
            linear 0.3 yalign 2.0
            linear 0.3 yalign 1.9
            repeat 9
    
    show шлепун обычный:
        toLeftShlepa
        xalign -0.5
        parallel:
            linear 3.0 xalign 0.7
        parallel:
            linear 0.3 yalign 0.9
            linear 0.3 yalign 0.87
            repeat 5

    pause 5

    scene фон кафе_внутри with fade

    show гг:
        toLeftGG
        xalign 0.4

    show шлепун обычный:
        toLeftShlepa
        xalign 0.2

    show алена без_собаки:
        toRightGG
        xalign 1.3
        parallel:
            linear 4 xalign 0.6
        parallel:
            linear 0.3 yalign 2.0
            linear 0.3 yalign 1.9
            repeat 7
            
    pause 4

    if (goodAlenaRelationship >= badAlenaRelationship):
        jump goodEndingGeneralGoodAlenaEnding
    else:
        jump goodEndingGeneralBadAlenaEnding
    

label goodEndingGeneralGoodAlenaEnding:

    scene фон кафе_внутри

    show гг:
        toLeftGG
        xalign 0.4

    show шлепун обычный:
        toLeftShlepa
        xalign 0.2

    show алена без_собаки:
        toRightGG
        xalign 0.6
        yalign 1.9

    alena "А кто это у нас тут, ШЛЕПУН!!!"

    alena "Мальчик мой, ты нашёлся, ой, то есть твой мальчик, прости, [playerName]."

    gg "А знаешь, пускай будет уже наш мальчик. Я давно хотел тебе сказать..."

    gg "В общем, ты мне нравишься!"

    alena "Если честно, ты мне тоже, ещё с нашей первой встречи!"

    gg "Правда??? Я так боялся это тебе говорить, но находка Шлепуна придала мне смелости и сил."

    alena "Шлепун просто незаменим. Как и ты, [playerName]."

    gg "Я тебя люблю!"

    alena "И я тебя люблю!"

    window hide
    pause 1

    gg "Пошли ко мне?"

    alena "Я только за, тем более моя смена уже закончилась."

    scene фон кафе_день with fade

    show гг:
        toRightGG
        xalign 0.7
        parallel:
            linear 3.0 xalign 1.3
        parallel:
            linear 0.3 yalign 2.0
            linear 0.3 yalign 1.9
            repeat 5
    
    show алена без_собаки:
        toRightGG
        xalign 0.5
        xzoom -1 yzoom 1
        parallel:
            linear 4.0 xalign 1.3
        parallel:
            linear 0.3 yalign 2.0
            linear 0.3 yalign 1.9
            repeat 7

    show шлепун обычный:
        toLeftShlepa
        xalign 0.3
        xzoom 0.6 yzoom 0.6
        parallel:
            linear 3.0 xalign 1.3
        parallel:
            linear 0.3 yalign 0.9
            linear 0.3 yalign 0.87
            repeat 5
            
    pause 4

    scene фон дом_гг спальня with fade

    show гг:
        toLeftGG
        xalign 0.4

    show шлепун обычный:
        toLeftShlepa
        xalign 0.2

    show алена без_собаки:
        toRightGG
        xalign 0.6

    alena "Слушай, у меня ведь так и не было возможности сыграть в твою игру."

    gg "Ничего страшного, сейчас я запущу игру и ты в неё сыграешь. Хорошо, что и ты, и Шлепун рядом со мной."

    scene фон загрузка_игры with fade

    image loadingGame:
        "загрузка игры/0.gif"
        0.02
        "загрузка игры/1.gif"
        0.02
        "загрузка игры/2.gif"
        0.02
        "загрузка игры/3.gif"
        0.02
        "загрузка игры/4.gif"
        0.02
        "загрузка игры/5.gif"
        0.02
        "загрузка игры/6.gif"
        0.02
        "загрузка игры/7.gif"
        0.02
        "загрузка игры/8.gif"
        0.02
        "загрузка игры/9.gif"
        0.02
        "загрузка игры/10.gif"
        0.02
        "загрузка игры/11.gif"
        0.02
        "загрузка игры/12.gif"
        0.02
        "загрузка игры/13.gif"
        0.02
        "загрузка игры/14.gif"
        0.02
        "загрузка игры/15.gif"
        0.02
        "загрузка игры/16.gif"
        0.02
        "загрузка игры/17.gif"
        0.02
        "загрузка игры/18.gif"
        0.02
        "загрузка игры/19.gif"
        0.02
        "загрузка игры/20.gif"
        0.02
        "загрузка игры/21.gif"
        0.02
        "загрузка игры/22.gif"
        0.02
        "загрузка игры/23.gif"
        0.02
        "загрузка игры/24.gif"
        0.02
        "загрузка игры/25.gif"
        0.02
        "загрузка игры/26.gif"
        0.02
        "загрузка игры/27.gif"
        0.02
        "загрузка игры/28.gif"
        0.02
        "загрузка игры/29.gif"
        0.02
        "загрузка игры/30.gif"
        0.02
        "загрузка игры/31.gif"
        0.02
        "загрузка игры/32.gif"
        0.02
        "загрузка игры/33.gif"
        0.02
        "загрузка игры/34.gif"
        0.02
        "загрузка игры/35.gif"
        0.02
        "загрузка игры/36.gif"
        0.02
        "загрузка игры/37.gif"
        0.02
        "загрузка игры/38.gif"
        0.02
        "загрузка игры/39.gif"
        0.02
        "загрузка игры/40.gif"
        0.02
        "загрузка игры/41.gif"
        0.02
        "загрузка игры/42.gif"
        0.02
        "загрузка игры/43.gif"
        0.02
        "загрузка игры/44.gif"
        0.02
        "загрузка игры/45.gif"
        0.02
        "загрузка игры/46.gif"
        0.02
        "загрузка игры/47.gif"
        0.02
        "загрузка игры/48.gif"
        0.02
        "загрузка игры/49.gif"
        0.02
        "загрузка игры/50.gif"
        0.02
        "загрузка игры/51.gif"
        0.02
        "загрузка игры/52.gif"
        0.02
        "загрузка игры/53.gif"
        0.02
        "загрузка игры/54.gif"
        0.02
        "загрузка игры/55.gif"
        0.02
        "загрузка игры/56.gif"
        0.02
        "загрузка игры/57.gif"
        0.02
        "загрузка игры/58.gif"
        0.02
        "загрузка игры/59.gif"
        0.02
        "загрузка игры/60.gif"
        0.02
        "загрузка игры/61.gif"
        0.02
        "загрузка игры/62.gif"
        0.02

        repeat 5

    stop music fadeout 1.0

    show loadingGame:
        toCenter
        yalign 0.3

    pause 6.3

    play music "audio/фоновая музыка.mp3" fadein 1.0 fadeout 1.0 loop volume 0.02

    scene фон дом_гг спальня with fade

    "Каждый день нашего разработчика компьютерных игр ничем не отличался от остальных, но было кое-что особенное в его жизни..."

    $ playerName = renpy.input("Выберите имя для главного героя:")
    $ playerName = playerName.strip()
    if playerName == "":
        $ playerName = "Михаил"

    scene конец with fade

    "Ваша концовка" "{color=#00ff15}Хорошая\n{/color}Шлепун — {color=#00ff15}✔{/color}\nАлёна — {color=#00ff15}✔{/color}"

    window hide
    pause 10

    return

label goodEndingGeneralBadAlenaEnding:

    scene фон кафе_внутри

    show гг:
        toLeftGG
        xalign 0.4

    show шлепун обычный:
        toLeftShlepa
        xalign 0.2

    show алена без_собаки:
        toRightGG
        xalign 0.6
        yalign 1.9

    alena "А кто это у нас тут, ШЛЕПУН!!!"

    alena "Мальчик мой, ты нашёлся, ой, то есть твой мальчик, прости, [playerName]."

    gg "А знаешь, пускай будет уже наш мальчик. Я давно хотел тебе сказать..."

    gg "В общем, ты мне нравишься!"

    alena "Если честно, ты очень хороший, добрый и красивый, но я не могу ответить тебе взаимностью, прости..."

    gg "Это твои чувства, я не могу на них повлиять... Всё хорошо, я понимаю..."

    alena "Прости, ты правда не плохой, просто дело во мне."

    gg "Хорошо, хорошо, я понял, ну мы со Шлепуном наверное пойдем."

    alena "Только приходите ещё!"

    gg "Обязательно зайдём, пока."

    alena "Пока и прости ещё раз."

    window hide
    pause 1

    scene фон кафе_день with fade

    show гг:
        toRightGG
        xalign 0.7
        parallel:
            linear 3.0 xalign 1.3
        parallel:
            linear 0.3 yalign 2.0
            linear 0.3 yalign 1.9
            repeat 5

    show шлепун обычный:
        toLeftShlepa
        xalign 0.5
        xzoom 0.6 yzoom 0.6
        parallel:
            linear 2.0 xalign 1.3
        parallel:
            linear 0.3 yalign 0.9
            linear 0.3 yalign 0.87
            repeat 5
            
    pause 4

    scene фон дом_гг спальня with fade

    show гг:
        toLeftGG
        xalign 0.4

    show шлепун обычный:
        toLeftShlepa
        xalign 0.2

    gg "Да... У меня щас такое состояние разбитое."

    gg "Надо бы отвлечься. Запущу-ка я свою игру, поиграю. Жаль, что Алёны нет рядом..."

    stop music fadeout 1.0

    scene фон загрузка_игры with fade

    show loadingGame:
        toCenter
        yalign 0.3

    pause 6.3

    play music "audio/фоновая музыка.mp3" fadein 1.0 fadeout 1.0 loop volume 0.02

    scene фон дом_гг спальня with fade

    "Каждый день нашего разработчика компьютерных игр ничем не отличался от остальных, но было кое-что особенное в его жизни..."

    $ playerName = renpy.input("Выберите имя для главного героя:")
    $ playerName = playerName.strip()
    if playerName == "":
        $ playerName = "Михаил"

    scene конец with fade

    "Ваша концовка" "{color=#ffa200}Средняя\n{/color}Шлепун — {color=#00ff15}✔{/color}\nАлёна — {color=#ff0000}✖{/color}"

    window hide
    pause 10

    return

label badEndingGeneral:

    scene фон улица_день

    show гг:
        toLeftGG
        xalign 0.3
        yalign 1.9

    show никита:
        toRightGG
        yalign 1.25

    show шлепун довольный:
        toLeftShlepa
        xalign 0.4
        yalign 0.87


    nikita "Ха-ха-ха, какие прелести. Он очень скучал по тебе!!!"

    gg "Я тоже!"

    nikita "Наверно тебе интересно, как всё же я его нашел."

    gg "Ещё бы!"

    hide шлепун довольный
    show шлепун обычный:
        toLeftShlepa
        xalign 0.4
        yalign 0.87


    nikita "Я преподаю информатику в одной из школ."

    nikita "Один из учеников 11 класса показал мне твою игру. Я решил её полностью пройти."

    nikita "Мне запомнилась та пельменная, на которую Шлепун обратил внимание после прогулки с Яриком." 

    nikita "Эта игра, как я понял, основана на реальной истории?"

    gg "Да, все действия в игре были взяты из жизни."

    nikita "Дак вот, я подумал, что Шлепун сбежал именно туда. Как раз такой вывод я сделал за тебя."

    nikita "А потом я понял, как тебе тяжело сейчас, и решил заняться реальным поиском Шлепуна."

    hide шлепун обычный
    show шлепун обычный:
        toLeftShlepa
        xalign 0.4
        yalign 0.87
        parallel:
            linear 2.0 xalign -0.3
        parallel:
            linear 0.3 yalign 0.9
            linear 0.3 yalign 0.87
            repeat 4

    nikita "Угадай, где пропадал этот красивый зверек???"

    gg "Только не говори, что в той пельменной."

    nikita "Именно там!!! Когда я проходил мимо, он выбежал ко мне, уж не знаю, откуда он там взялся, но от него точно пахло пельмешками!!! Ха-ха-ха."

    gg "Главное что Шлепун нашёлся, я в ответе за него."

    window hide
    pause 1

    gg "ЧТО? КАК? ШЛЕПУНА ОПЯТЬ НЕТ. Такого просто не может быть."

    nikita "Поиски начнутся сначала, я так понимаю."

    gg "Ты думаешь правильно..."

    hide никита
    show никита:
        toRightGG
        yalign 1.2

        parallel:
            linear 3.0 xalign 1.3
        parallel:
            linear 0.3 yalign 1.2
            linear 0.3 yalign 1.25
            repeat 5

    pause 3

    hide гг
    show гг:
        toLeftGG
        xalign 0.3
        yalign 1.9
        parallel:
            linear 2.0 xalign 0.5
        parallel:
            linear 0.3 yalign 2.0
            linear 0.3 yalign 1.9
            repeat 3
        
    pause 2

    play sound "audio/входящий звонок телефона.mp3" fadein 0.5

    pause 5

    stop sound

    show телефон гг разговор_с_яриком:
        toRight
        xzoom 0.4
        yzoom 0.4

    gg "{b}(звонок){/b} ШЛЕПУН НАШЁЛСЯ И ТУТ ЖЕ ОПЯТЬ ПРОПАЛ!!"

    yarik "{b}(звонок){/b} Как так? Такого просто не может быть."

    if (badShlepaRelationship >= goodShlepaRelationship):
        yarik "{b}(звонок){/b} Сказать по правде, Шлепун убежал из-за того, как ты с ним обращался."

        yarik "{b}(звонок){/b} Я бы тоже не вытерпел на его месте... Ты был слишком груб."

        gg "{b}(звонок){/b} Да, ты прав, я же совсем его не ценил, когда мы были вместе. Он убежал из-за меня, это моя вина..."

    gg "{b}(звонок){/b} Пойду расскажу всё Алёне."

    yarik "{b}(звонок){/b} Хорошо, пока."

    gg "{b}(звонок){/b} Пока."

    scene фон улица_день

    show гг:
        toCenterGG
        xalign 0.5
        yalign 1.9
        parallel:
            linear 5.0 xalign 1.3
        parallel:
            linear 0.3 yalign 2.0
            linear 0.3 yalign 1.9
            repeat 9

    pause 5

    scene фон кафе_день

    show гг:
        toLeftGG
        xalign -0.3
        parallel:
            linear 5.0 xalign 0.7
        parallel:
            linear 0.3 yalign 2.0
            linear 0.3 yalign 1.9
            repeat 9

    pause 5

    scene фон кафе_внутри with fade

    show гг:
        toLeftGG
        xalign 0.4

    show алена без_собаки:
        toRightGG
        xalign 1.3
        parallel:
            linear 4 xalign 0.6
        parallel:
            linear 0.3 yalign 2.0
            linear 0.3 yalign 1.9
            repeat 7
            
    pause 4

    if (goodAlenaRelationship >= badAlenaRelationship):
        jump badEndingGeneralGoodAlenaEnding
    else:
        jump badEndingGeneralBadAlenaEnding

label badEndingGeneralGoodAlenaEnding:

    scene фон кафе_внутри

    show гг:
        toLeftGG
        xalign 0.4

    show алена без_собаки:
        toRightGG
        xalign 0.6
        yalign 1.9

    alena "[playerName], привет, ну что, Шлепун нашелся?"

    gg "Да, но не все так радостно."

    alena "Почему это?"

    gg "Пока я общался с Никитой, Никита нашёл Шлепуна, Шлепун опять убежал, это я виноват, я плохо с ним обращался..."

    alena "Шлепун... Как же мы без него."

    alena "[playerName], не переживай, мы найдём его вместе, я тебе помогу. Давно хотела тебе сказать, в общем..."

    alena "Ты мне нравишься!"

    gg "Алён, спасибо тебе большое за поддержку, даже как-то страшно говорить это, но ты мне тоже очень нравишься."

    alena "Я тебя люблю!"

    gg "Я тебя люблю!"

    window hide
    pause 1

    gg "Пойдём ко мне?"

    alena "Я только за, тем более моя смена уже закончилась."

    scene фон кафе_день with fade

    show гг:
        toRightGG
        xalign 0.7
        parallel:
            linear 3.0 xalign 1.3
        parallel:
            linear 0.3 yalign 2.0
            linear 0.3 yalign 1.9
            repeat 5
    
    show алена без_собаки:
        toRightGG
        xalign 0.5
        xzoom -1 yzoom 1
        parallel:
            linear 4.0 xalign 1.3
        parallel:
            linear 0.3 yalign 2.0
            linear 0.3 yalign 1.9
            repeat 7
            
    pause 4

    scene фон дом_гг спальня with fade

    show гг:
        toLeftGG
        xalign 0.4

    show алена без_собаки:
        toRightGG
        xalign 0.6

    alena "Слушай, у меня ведь так и не было возможности сыграть в твою игру."

    gg "Ничего страшного, сейчас я запущу её и ты в неё сыграешь. Жаль, что Шлепун этого не увидит."

    stop music fadeout 1.0

    scene фон загрузка_игры with fade

    show loadingGame:
        toCenter
        yalign 0.3

    pause 6.3

    play music "audio/фоновая музыка.mp3" fadein 1.0 fadeout 1.0 loop volume 0.02

    scene фон дом_гг спальня with fade

    "Каждый день нашего разработчика компьютерных игр ничем не отличался от остальных, но было кое-что особенное в его жизни..."

    $ playerName = renpy.input("Выберите имя для главного героя:")
    $ playerName = playerName.strip()
    if playerName == "":
        $ playerName = "Михаил"

    scene конец with fade

    "Ваша концовка" "{color=#ffa200}Средняя\n{/color}Шлепун — {color=#ff0000}✖{/color}\nАлёна — {color=#00ff15}✔{/color}"

    window hide
    pause 10

    return

label badEndingGeneralBadAlenaEnding:

    scene фон кафе_внутри

    show гг:
        toLeftGG
        xalign 0.4

    show алена без_собаки:
        toRightGG
        xalign 0.6
        yalign 1.9

    alena "[playerName], привет, ну что, Шлепун нашёлся?"

    gg "Да, но не всё так радостно."

    alena "Почему это?"

    gg "Пока я общался с Никитой, Никита нашёл Шлепуна, Шлепун опять убежал, это я виноват, я плохо с ним обращался..."

    alena "Ярик мне рассказывал, как ты вёл себя со Шлепуном."

    alena "Наверно Шлепун просто не выдержал такого отношения, прости, но это правда."

    gg "Да, я понимаю, что вы с Яриком правы, но уже ничего не изменить. Хотя, может, с тобой я смогу справиться со всем этим."

    gg "Алёна, ты мне нравишься."

    alena "Если честно, ты очень хороший, добрый и красивый, но я не могу ответить тебе взаимностью, прости..."

    gg "Это твои чувства, я не могу на них повлиять... Всё хорошо, я понимаю..."

    alena "Прости, ты правда не плохой, просто дело во мне."

    gg "Я понимаю, тогда мне наверно пора, надеюсь, как-нибудь еще встретимся, всего тебе хорошего."

    alena "Прости меня, правда, и тебе всего хорошего, до встречи..."

    window hide
    pause 1

    scene фон кафе_день with fade

    show гг:
        toRightGG
        xalign 0.7
        parallel:
            linear 3.0 xalign 1.3
        parallel:
            linear 0.3 yalign 2.0
            linear 0.3 yalign 1.9
            repeat 5

    pause 4

    scene фон дом_гг спальня with fade

    show гг:
        toLeftGG
        xalign 0.4

    gg "Да... У меня щас такое состояние разбитое."

    gg "Надо бы отвлечься. Запущу-ка я свою игру, поиграю. Жаль, что ни Алёны, ни Шлепуна нет рядом..."

    stop music fadeout 1.0

    scene фон загрузка_игры with fade

    show loadingGame:
        toCenter
        yalign 0.3

    pause 6.3

    play music "audio/фоновая музыка.mp3" fadein 1.0 fadeout 1.0 loop volume 0.02

    scene фон дом_гг спальня with fade

    "Каждый день нашего разработчика компьютерных игр ничем не отличался от остальных, но было кое-что особенное в его жизни..."

    $ playerName = renpy.input("Выберите имя для главного героя:")
    $ playerName = playerName.strip()
    if playerName == "":
        $ playerName = "Михаил"

    scene конец with fade

    "Ваша концовка" "{color=#ff0000}Плохая\n{/color}Шлепун — {color=#ff0000}✖{/color}\nАлёна — {color=#ff0000}✖{/color}"

    window hide
    pause 10

    return










    

    
            




        
    

    





    
    







