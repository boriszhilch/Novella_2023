﻿
define e = Character('Эльмир', color="#414141ff")
define hoz = Character('Хозяин', color="#353535ff")
define goloc = Character('Голос в голове', color="#5e605eff")
define golname = Character('[goloc_name]', color="#5e605eff")


label start:
    label prolog:
        scene bg temnica:
            yalign (0.55)
            xalign (0.5)
        "Эх... вспомнить бы какой вчера был день недели, вроде, среда."
        "А вроде, и понедельник. А хотя хуй его знает."
        "Я вчера пахал, сегодня пахаю и завтра буду. 19 лет уже пахаю, заебался..."
        hoz "7 УТРА ЦИПОЧКИ, ПОРА РАБОТАТЬ !!!!"
        "Заебал..."
        e "\"Закрыл глаза\""
        "Интересно... Есть ли жизнь на воле? Какого это?"
        hoz "ЭЙ ТЫ..."
        hoz "ХУИХ..."
        hoz "Хэиуль..."
        hoz "КОРОЧЕ, МНЕ ПОХУЙ, ПАШИ ХУЕМ."
        e "Что делать?"
        hoz "А ты че, дохуя тупой? ИДИ РАБОТАЙ!!!"
        e "Да блять.. Да я не мог... ДА я... ДА сука..."
        hoz "Ща опять на 4 дня без еды оставлю."
        e "Да понял, понял."

        scene pole_vecher
        '' "Как же я устал от этой жизни. Нужно что-то менять."
        '' "Доработаю и пойду посплю. Завтра новый день, новая жизнь..."
        hoz "Ну блин, 15 дней тебя не кормил... ну еще 3 потерпишь."
        e "Да... -_-"
        
        scene bg dark
        '' '\"Следующее утро\"'
        hoz "ОП, че, всю ночь спал, да? Ну блин, выспался, наверное."
        "Да бля, ему чо не спиться... Который час вообще?"
        "???" "Да че кого, я не твой хозяин, я твой новый кентюрик :)"
        e "Всё... умер..."
        e "Умер..."
        e "С духами уже общаться начал."
        goloc "Да не умер ты, еще столько же проживешь, не ссы."
        goloc "Крч заебало меня твое ничтожное существование, я решил тебя спасти..."
        goloc "Все что тебе нужно, это слушаться меня... Уверенно звучит, да? :)"
        

    label znakomctvo_c_golocom:
        menu:
            "\"Проигнорировать голос\"":
                goloc "Аууу... "
                menu:
                    "\"Продолжать игнорировать\"":
                        jump CHSV
                    "Ладно так уж и быть, что тебе нужно?":
                        jump question2
                label question2:
                    jump do_it
                label CHSV:
                    goloc 'Ладно, чел, до завтра'
                    "Ура... Я снова в одиночестве :("
                    jump sleep

            "Кто ты?... Что ты?":  
                goloc "Кто я? КТО БЛЯТЬ Я?"
                goloc "Я твой голос, в твоей голове."
                e "Но там же ведь пусто."
                goloc "Ну есть чучуть пространства свободного, ничего страшного."
                e "Да пошёл ты, козёл."
                goloc "Да ну вот и пойду, все, обидел ты меня."
                e "Ну и куда ты пошел?"
                '\'молчание\''
                "Ура... Я снова в одиночестве :("
                jump sleep
                

            "\"Лечь спать\"":
                jump sleep
        

            "Ну ладно, делать нефиг, что нужно?":
                jump do_it

        label sleep:
            '\'Лег обратно спать\''
            goloc 'Да еб...Да... ЭЭЭЙ!'
            goloc 'ПРОСНИСЬ!!!!'
            e 'Да емае, да отстань ты от меня.'
            goloc "Крч, ты меня заебал, я тебе объясняю, что тебе нужно делать... а дальше делай что хочешь."
            jump do_it

        label do_it:
            goloc "Каждый день одно и то же, тебе это не надоело?"
            goloc "Я помогу изменить твою жизнь."
            goloc "Просто каждый раз перед сном..."
            e "Да реклама даже в голове, надоели блин."
            e "То одна блин, в 300 метрах от меня, то еще что-то"
            goloc "Да лан, все, все, успокойся."
            goloc "Твоя цель это довериться мне и запомнить все, что я скажу. Значит завтра, когда солнце будет в самой пиковой точке в небе"
            goloc "У тебя будет один из немногих шансов сбежать, просто доверься мне."
            goloc "Я = доверие"
            e "Ты думаешь я не пытался сбежать?"
            goloc "Да"
            e "Это че бля, на столько очевидно?"
            goloc "Крч бля не переживай."
            'Эльмир задумался'
            goloc "Когда солнце будет в самой пиковой точке, у тебя будет ровно 3 минуты и 14 секунд, именно столько на тебя никто не будет смотеть"
            goloc "Беги в сторону захода солнца, как только забежишь за 3 больших дуба, ты будешь в безопастности."
            goloc "Все понял?"
            e "Не понял."
            goloc "Что не понял?"
            e "3 минуты."
            e "Это сколько?"
            goloc '...'
            goloc 'Это дохуя, тебе хватит.'
            menu:
                'Не довериться':
                    goloc "-_-"
                    scene
                    ##Следующее утро"
                    "Эх... вспомнить бы какой вчера был день недели, вроде, среда."
                    "А вроде, и понедельник. А хотя хуй его знает."
                    "Я вчера пахал, сегодня пахаю и завтра буду. 19 лет уже пахаю, заебался..."
                    ##Следующее утро"
                    "Эх... вспомнить бы какой вчера был день недели, вроде, среда."
                    "А вроде, и понедельник. А хотя хуй его знает."
                    "Я вчера пахал, сегодня пахаю и завтра буду. 19 лет уже пахаю, заебался..."
                    "На следующее утро Эльмир скончался от жажды и голода."
                    jump bad_end_1

                "Довериться":
                    e 'Хорошо, звучит сомнительно, но заебался так жить уже, поэтому пофиг'
                    e 'Поэтому я просто доверюсь странному голосу в голове.'
                    goloc "Вот и славно :) а теперь ложись спать, тебе завтра понадобится много сил."
                    jump next_day

    label bad_end_1:
    scene
    "\'Вы прошли игру.\'"

    label next_day:
        "\'Следующее утро\'"
        hoz "Новые день, новые силы. Сегодня, конечно, солнца не видно из-за туч, но поверьте, сейчас утро!"
        e "Блять."
        goloc "Блять."
        #scene pole
        e "Ты знал, что у меня есть ровно 3 минуты, ровно 14 секунд, что мне нужно бежать во время самой пиковой точке солнца."
        e "НО ТЫ НЕ ЗНАЛ БЛЯТЬ, ЧТО СЕГОДНЯ НЕ ВИДНО СОЛНЦА???"
        goloc "Да я чо, ебу."
        goloc "Оглянись вокруг, видишь кого-нибудь?"
        e "Нет."
        goloc "Ну так беги."
        "'Эльмир оглянулся, действительно убедился, что его никто не видит...'"
        "'Но...'"
        "'Он не знал, что если он никого не видит, то это не значит, что никто не видит его.'"
        e "Ну... с богом."

        "'Элмир перевёл дыхание, бросил грабли и побежал.'"
        "'Бежал, как в первый раз... без оглядки, с дрожью в руках, со страхом в глазах.'"
        #memories
        e "Каждый грёбанный день я вкалывал по 20 часов, на протяженнии 19 лет на этого 30-летнего старика."
        e "Я его, конечно, ненавижу, но за счёт всех этих усилий, моя выносливасть достигла пика человеческих возможностей."
        e "Для меня этот бег вообще ни о чём, хоть я и бегал только в своём воображении."
        "'Пока Эльмир летал в своих мыслях, он осознал, что уже в чаще леса.'"
        "'Эльмир, запыхавшимся голосом, спрашивает у голоса.'"
        
        e "Ну что, как я бежал? Меня сильно было заметно?"
        goloc "Да, блять, я кричал, что за тобой ДВЕ СОБАКИ БЛЯТЬ БЕГУТ, СОБАКИ БЛЯТЬ!"
        goloc "ТЫ ТАК БЛЯТЬ ДРАПУ ДАЛ, ЧТО ДАЖЕ СОБАКИ НЕ ДОГНАЛИ."
        goloc "Я блять впервые такое вижу."
        e "А чо ты не сказал, что собаки за мной бегут?"
        goloc "Так я блять тебе еще 6 минут назад это говорил."
        e "6 минут? А сколько я бежал?"
        goloc "15 МИНУТ НАХУЙ"
        e "Ох... Нифига, наверно, много пробежал, киллометра 2, наверно."
        goloc "Да не, 150 метров... Повезло, что собаки на цепи были."
        goloc "Ты калитку только минут 10 искал, а потом минут 5 думал как её открыть."
        e "Так, ладно. Где там говоришь твои 3 дуба?"
        goloc "Да там на самом деле не важно куда бежать надо было. Просто бежать надо было."
        e "-_-"
        e "Слышь, чипушила, а как тебя зовут хотя бы?"
        goloc "Меня не зовут, я сам прихожу :)"
        e "Понятно..."
        e "Ладно, дам тебе имя, щас только подумаю чучуть."
        "*Спустя 5 минут...*"

        python:
            goloc_name = renpy.input("Блять, ты меня заебал, я буду звать тебя")
            goloc_name = goloc_name.strip() or "Всё ещё голос"

        if goloc_name == "Всё ещё голос":
            e "Не придумал я тебе имени."
            golname "Ну ты и дебил, даже для голоса в голове имя придумать не можешь."

            python:
                goloc_name = renpy.input("Ладно, задолбал, ща ещё подумаю")
                goloc_name = goloc_name.strip() or "Всё ещё голос"

            if goloc_name in {"Эльмир", "Ильмир", "Эльмира", "Эльнар", "Ильнур", "Эльдар"}:
                golname "Серьёзно?"
                e "Да бля, я больше имён не знаю."
                golname "Даже имя \"Толя\" лучше, чем это.\nПодумай ещё, пожалуйста."

                python:
                    goloc_name = renpy.input("Ну ща, подожди:")
                    goloc_name = goloc_name.strip() or "Всё ещё голос"

                if goloc_name == "Всё ещё голос":
                    e "Ээуу аыа... А мне твоё старое имя нравилось больше. Давай ты останешься голосом?"
                    golname "Бля, я 5 минут ждал, чтобы ты ничего не придумал?\n-_-"
                    golname "Ладно, фиг с тобой, пошли дальше."

            elif goloc_name == "Всё ещё голос":
                e "Ээуу аыа... А мне твоё старое имя нравилось больше. Давай ты останешься голосом?"
                golname "Бля, я 5 минут ждал, чтобы ты ничего не придумал?\n-_-"
                golname "Ладно, фиг с тобой, пошли дальше."
            else:
                golname "Эээх... всё лучше, чем ничего."
                e "Ладно, пошли дальше."

        elif goloc_name in {"Толя", "Толик", "Вадим", "Вадик"}:
            golname "Не не не, такое уебанское имя мне давать не нужно."
            e "У меня так бабушку вообще-то звали..."
            golname "Мне жалко твою бабушку."
            e "Э, о мёртвый либо хорошо, либо плохо."
            golname "Если выбирать между именем \"Толя\" и не выбирать вовсе, то я.. аыа... бля..."
            golname "В пизду кароче. Я предпочту остаться голосом."
            e "Ладно, фиг с тобой, пошли дальше."
            python:
                golname = "Всё ещё голос"

        elif goloc_name in {"Эльмир", "Ильмир", "Эльмира", "Эльнар", "Ильнур", "Эльдар"}: # goloc_name == "Эльмир" or "Ильмир"
            golname "Серьёзно?"
            e "Да бля, я больше имён не знаю."
            golname "Даже имя \"Толя\" лучше, чем это.\nПодумай ещё, пожалуйста."

            python:
                goloc_name = renpy.input("Ну ща, подожди:")
                goloc_name = goloc_name.strip() or "Всё ещё голос"

            if goloc_name == "Всё ещё голос":
                e "Ээуу аыа... А мне твоё старое имя нравилось больше. Давай ты останешься голосом?"
                golname "Бля, я 5 минут ждал, чтобы ты ничего не придумал?\n-_-"
                golname "Ладно, фиг с тобой, пошли дальше."
            
            else:
                golname "Ладно, фиг с тобой, пошли дальше."
        else:
            golname "Ну и уёбищное имя."
            e "Да бля :("
            golname "Ладно, фиг с тобой, пошли дальше."

        label pravo:
            menu:
                "Пойти в город":  ## город
                    $ ostalca_v_lecy = False
                    pass

                "Остаться в лесу":  ## лес
                    e "Я решил, что останусь в лесу на некоторое время."
                    golname "Ну да, залечь на дно тебе не помешает."
                    
                    ## forest screen
                    jump forest

                "Пойти направо":
                    "*Эльмир обошел владения хозяина вокруг и снова вернулся в тоже место*"
                    $ count = 1
                    $ Pravo = True

                    if count == 1:
                        golname "Ты че. Дебил?"
                    elif count == 2:
                        golname "СЕРЬЕЗНО БЛЯТЬ?"
                        golname "ТЫ 15 МИНУТ ПОТРАТИЛ НА ТО, ЧТОБЫ ЕЩЕ РАЗ СДЕЛАТЬ ЭТОТ МАНЕВР?"
                        e "Да..."
                        e "Да я подумал, что блин....\nАй да ладно крч, мне лучше не думать."
                        golname "Верно подметил."
                    elif count == 3:
                        golname "Я..."
                        golname "Я не хочу с тобой общаться..."
                        $ Pravo = False
                    elif count == 4:
                        golname "..."
                        e "Я не знаю зачем я так делаю... Прости("

                    jump pravo

                "Вернуться обратно":
                    "*Эльмир поворачивается обратно, открывает калитку, заходит обратно, берёт в руки грабли и начинает работать.*"

            

    label forest:
        $ ostalca_v_lecy = True
        " *И блуждая, Эльмир понимает лишь одно. Он проголодался.*"
        e "Голос, я впервые нахожусь в лесу и я хочу жрать."
        golname "Да а я то тебе чем помогу?...\nладно, сколько ты там не ел?"
        e "Ну сегодня 16 сутки, как я голодаю"
        golname "Ахуеть, люди столько не живут, сколько ты голодаешь"
        golname "Ладно, смотри... видишь белый гриб?"
        #картинка с яблоком 
        e "Бля, это яблолки, дебил"
        golname "А ты откуда знаешь как яблоки выглядят?"
        e "А ты откуда знаешь как грибы выглядят?"
        golname "ТЫ ЧЕ БЛЯТЬ, ЗНАЕШЬ КАК ГРИБЫ ВЫГЛЯДЯТ?"
        $ poel_v_lesy = False

        menu:
            "Да.":
                golname "А вот слева тогда что? "
                e "Тоже яблоки."
                golname "Чел, там нихуя нет."
                "*Эльмир подбирает яблоко и кидает его влево."
                e "Теперь есть."

            "Нет.":
                golname "Ну вот и всё нахуй. Ты бы ещё сказал, что это волки блять." #напоминалочка


        golname "Ладно, вот это типа яблоко, и его типа можно есть."
        "*Эльмир берет яблоко, и делает первый укус.*"
        "*Из яблока вылезает червь и предлагает ему интим. От ужаса, Эльмир роняет яблоко из рук и начинает кричать.*"
        golname "Оу, оу, оу, оу, все нормально? Что с тобой?... Пизда, я же пошутил, что это яблоки. Нахуя ты гриб то сожрал?"
        e "Да бля, ща, подожди, мне плохо"
        "*Из кустов слышатся странные шорохи.*"
        golname "Слышал это?"
        golname "Сходи проверь."
        e "Если там медведь, то моя смерть будет на твоей совести."
        golname "Да какой медведь блять, ты яблоки от грибов не можешь отлечить."
        "*Медленно и острожно Эльмир подходит к зарослям. Отодвигая ветви кустарника он пытается взяглядом уловить источник странных шорохов*"
        "*Подбираясь все ближе, Эльмир замечает...*"
        e "ААААА ВОЛКИ!!!!!!"
        golname "А ты откуда знаешь как волки выглядят?"
        e "А что это нахуй, яблоки?"
        "Первый волк" "Хуйню не неси. Олег, доставай чекушку, у нас гости."
        "Волк Олег" "уау.ауу...а.у.у..уа.."
        "*Волк Олег уснул*"
        "Первый волк" "Бля, Олег уснул. Ну похуй, че, хотите анекдот расскажу?"

        menu:
            "Да":
                "Первый волк" "Поймал волк колобка, хочет выебать его. Крутит вертит и говорит:\n
                    — Ну и куда тебя ебать?\n
                    — Меня не надо ебать!\n
                    — Откуда сказал?"

                e "Эй, [golname], мне это кажется, или нам реально волк анекдот читает?"
                golname "ПЗАХВАПХВАПХВАПХ ИДИ НАХУЙ, ЭТО ВАЩЕ РАЗЪЕБ"

                "Первый волк" "Хочешь еще один анекдот?"
                golname "СОГЛАШАЙСЯ ЕБАНАТ!!!"

                menu:
                    "Да":
                        "Первый волк" "Идёт Серый волк по лесу, а навстречу ему Красная Шапочка.\n
                            — Куда путь держишь, девочка?, —  спрашивает Серый волк.\n
                            — Я иду к бабушке, несу ей пирожки и горшочек с маслом!\n
                            — Пирожки и горшочек с маслом?! Вот это удачно я тебя встретил: и пожрать есть, и чем жопу теб...!"
                        e "Я думаю достаточно на сегодня анекдотов."
                        golname "Да ебать ты душнила, я бы нахуй лучше бы с этим волком остался, чем с тобой."
                        e "[golname], я до сих пор есть вообще - то хочу, нам.. ну как бы... торопиться пора."
                        "Первый волк" "Что, уже уходите?"
                        golname "НЕЕЕЕЕЕТ, Я ХОЧУ ОСТАТЬСЯ."
                        "*И тут Эльмир резким движением обратно прыгает в те кусты, откуда он сюда пришел.*"
                        "Первый волк" "*Удаляющимся голосом*\n
                            У меня еще анекдоты есть :("
                        golname "Ладно, хуй с тобой, пойдем искать пожрать."
                        jump forest_road

                    "Нет":
                        "*Волк Олег просыпается, бухим и буйным голосом начинает быковать на Эльмира*"
                        "Волк Олег" "Да че... б.. да че ты лама.ешся. Я вот ваще.. по .. пятна...попя.. крч по 15 анекдотов слушаю.. и ни.че. "
                        "*Эльмир думает про себя: \"Лучше бы тут были медведи, анекдоты про медведей мне больше нравятся\"*"
                        "*[golname] думает про себя: \"ЕБАТЬ,ЕЩЕ ОДИН ПРОСНУЛСЯ, ЕЩЕ БОЛЬШЕ АНЕКДОТОВ. СЮДА НАХУЙ\"*"
                        "Первый волк" "Олежа, друг мой дорогой, налей ещё чучуть."
                        "Волк Олег" "Волк не кактус, ему нужно пить."
                        "Первый волк" "Хорошо сказал, звучит как тост."
                        e "Ладно, ребят, хорошо посидели, мне пора идти."
                        "Волк Олег" "Да пиздуй ты уже, заебал."
                        golname "НЕЕЕЕЕТ, ПУСТИ МЕНЯ К ВОЛКАМ!"
                        e "Напоминаю, что я голодный."
                        golname "Ладно, хуй с тобой, пойдем искать пожрать."
                        jump forest_road
                
            "Нет":
                "Первый волк" "Ебать ты душнила ебанная, пиздуй отсюда."
                golname "Блять... в чьей я голове нахожусь, боже."
                "*А ведь деййствительно душнила ебанная.*"
                e "Ладно, хуй с ним, давай анекдот."
                "Первый волк" "Да всё уже, иди нахуй, ты меня заебал :("
                "*Волк Олег просыпается, бухим и буйным голосом начинает гнать на Эльмира*"
                "Волк Олег" "ТЫ Ху...Ли МаеГо КЕН..та... РаСТРО.ИЛ? Мне ЧО, УПАКО.ВАТЬ ТиБЯ ИЛИ ЧО НА?"
                e "Я из тех людей, которые способны долго терпеть, а потом еще столько терпеть-терпеть."
                "Волк Олег" "БЛя... понял, баз...ара *икает* не имею."
                "Первый волк" "Олег, ёптвую мать, не кипишуй."
                "Волк Олег" "ЧЬЮ ТЫ ТАМ МАТЬ *икает* ЕБАЛ?"
                "*Эльмир под их рамсы начинает съёбываться*"
                golname "Эээй, куда ты? Дай мне посмотреть. Не каждый же день смотришь на пьяных волков."
                e "Так вот именно, никто не выживает после рамсов пьянных волков."
                $ volk_agressive = True
                jump ubezhat

            "Убежать":
                $ volk_agressive = False
                e "[golname], а может убежать?"
                golname "Так они же не на цепи, куда ты, блять, убежишь?"
                e "Ну я всё таки попробую."
                jump ubezhat

        label ubezhat:
            "*Затаив дыхание, резко повернувшись, уже было начал бежать...*"
            "*Задумавшись, Эльмир осознал, что забыл откуда пришёл.*"
            "*Эльмир поворачивается к волкам и спрашивает у них.*"
            e "Ребят, а откуда я пришёл, не подскажите?"

            if volk_agressive:
                "*Волки деруться и перегрызают друг другу глотки.*"
                golname "АХХПХП ЕБАААААТЬ УГАР, ЭТО ЛУЧШЕ ЛЮБОГО АНЕКДОТА... АХХПХАП"
                "*Эльмир резко вспоминает откуда он пришел, поворачивается и спокойным шагом уходит.*"
                jump forest_road

            else:
                "Первый волк" "Ты уже уходишь? Даже не послушаешь анекдот? :("
                golname "Бля, да дай анекдот послушать, душнила."
                "*Эльмир, игнорируя [golname], отвечает волку...*"
                e "Я на самом деле случайно на вас набрёл. Искал еду, наелся грибов и теперь мне какие-то волки мерещаться."
                "Первый волк" "Так ты голодный? Что же ты сразу не сказал?"
                "*Первый волк протягивает Эльмиру корзину с яблоками*"
                "*Эльмир задумался...*"
                "Бля, а откуда он нахуй её достал?"

                menu:
                    "Принять щедрый подарок":
                        $ poel_v_lesy = True
                        "*Эльмир берёт несколько яблок из этой корзинки и жадно начинает их грызть.*"
                        golname "Опять на яблоки повёлся, ну ты и олень."
                        e "ДА ЗАВАЛИ ТЫ СВОЁ ЕБАЛО, Я ВПЕРВЫЕ ЗА 16 ДНЕЙ ПОЕЛ."
                        "Первый волк" "Да я, вроде чбы, молчал :("
                        "*Из-за крика Эльмира просыпается пьяный волк Олег, встаёт из-за стола, подходит к Эльмиру, выхватывает у него яблоко из рук и говорит пьяным голосом...*"
                        "Волк Олег" "Вот ты *икает* ешь.... а вот я бл... за них воевал ёпт."
                        "Первый волк" "Это как надо воевать блять, что ты только за эти яблоки воевал?"
                        "Волк Олег" "Да пошёл *икает* ты нах....хыуй, душнила ебаная."
                        "*Расстроенный волк Олег отправился дальше спать.*"
                        e "Спасибо тебе за яблоки! Ты самый лучший волк, правда, спас меня)"
                        "Первый волк" "Пиздец ты душишь, пошёл нахуй отсюда и яблоки отдай, за них Олег воевал."
                        "*Эльмир отдаёт яблоки Первому волку и с обиженным лицом идёт туда, куда глаза глядят.*"
                        golname "Ну хотя бы поел :)"
                        jump forest_road

                    "Отказаться":
                        $ poel_v_lesy = False
                        e "Ага блять, я еще раз на эту хуйню не поведусь."
                        "*Эльмир развернулся и ушёл куда глаза глядят.*"
                        "*Спустя 5 минут...*"
                        "Первый волк" "Ты ебанутый? Может ты перестанешь кругами ходить?"
                        "*После этих слов Эльмир фыркнул на волка и ушёл туда, откуда пришёл.*"
                        "*Даже волк Олег ахуел от стальных яиц Эльмира.*"
                        golname "Ахуеть..."
                        jump forest_road
                        

    label forest_road:
        if poel_v_lesy == True:
            "*Спустя 2 часа*"
            golname "Ебать, тебя так вштырило от этих яблок. Ты часа 2 валялся с пеной у рта, про волков каких-то бормотал."
            golname "Потом очнулся с бешенными глазами, начал снова блять жрать эти яблоки и кричать \"Спасибо тебе за яблоки! Ты самый лучший волк, правда, спас меня.\""
            golname "Ну это вообще пиздец, я в ахуе"
            e "Зато с таким кайфом поел, почти не чувствую голода."
            golname "Так, чувак, на улице уже прилично стемнело, поэтому давай быстро раскинем ночлег, а с утра подумаем, что будем делать."
            e "Бля, а где я спать то буду, у нас ни палатки, нихуя."
            golname "Чел... ты 19 лет на каком-то говне в виде сена и камня спал, не выделывайся."
            e "И то верно."
            "*Лежавшие неподалеку лиственные ветки Эльмир скинул в кучу, чтобы не спать уж на совсем голой земле.*"
            "*Положив свое тело на импровизированную кровать, Эльмир заговорил со своим новым другом.*"
            e "Слушай, [golname], А почему ты вообще мне помогаешь? "
            golname "Я бы ответил тебе на твой вопрос, но боюсь ты сейчас не поймешь, прошло сликом мало времени... Прошу, просто подожди еще немного и ты сам все поймешь."
            "*И лишь только договорив, голос осознал, что Эльмир не спавший нормально последние двое суток, уже поддался искушению и давно уже отправлися в следующий день."
            e "*Храп...*"
            golname "Пидорас."
            jump day_3

        if poel_v_lesy == False:
            "*Спустя 2 часа*"
            golname "Ебать, тебя так вштырило от этого гриба. Ты часа 2 валялся с пеной у рта, про волков каких-то бормотал."
            e "*Начинает блевать*"
            golname "Я же говорил, что это гриб..."
            e "Да блять. Подожди *блюет* я впервые пустотой блюю."
            golname "Пустая твоя жизнь, а блюешь ты грибами."
            "*Эльмир чуть-ли не плача отвечает.*"
            e "Да я откусил чуть-чуть гриба, а выблевал как минимум целое грибное царство."
            golname "Хорошее это дело, грибы разводить."
            "*Спустя какое-то время."
            e "Ладно, [golname], мне уже стало лучше, и пока я окончательно не помер от голода, нужно соорудить ночлег... "
            golname "Ты че еблан, из чего ты ночлег там собрался делать?"
            e "Бля, внатуре."
            "*Не долго думая, Эльмир уложился на холодную землю и начал фантазировать о еде.*"
            e "*Храп...*"
            golname "Да... Не много тебе времени потребовалось."
            jump day_3

    
    label day_3:
        "*Наступило утро.*"
        "*Эльмир просыпается.* "
        if poel_v_lesy:
            golname "С добрым утром, красавица, как спалось?"
            e "Мы че бля, в романтических отношениях?"
            golname "..."
            golname "Ебать ты душнила ебаная."
            e "Да бля, бля, нормально я поспал, нормально."
            e "Ну сытости мне хватит еще на несколько дней, а вот чего мне действительно не хватает, так это..."
            golname "Чего же? "
            e "Молиться хочу."
            golname "... Ну так молись, в чем проблемама?"
            e "ЭЭЭЭЭ. Не по христиански как-то... Здесь же даже церкви нет. Крч мне похуй, отправляемся в город."
            golname "Ну там.... проблемка маленькая есть...."
            e "Да не переживай ты. Беглый раб нафиг никому не сдался, никто меня искать не будет."
            golname "Не в этом суть...."
            golname "Ну крч сам все увидишь, когда в церковь придем."
            e "-_-\n
            пон."
            jump city


        else:
            "*Наступило утро.*"
            "*Эльмир просыпается.* "
            e "Еще день.... Еще один блятский день я не протяну... Сил почти не осталось..."
            e "[golname], нам срочно нужно направиться в город. В лесу нереально выжить без нее."
            golname "А ты не боишься, что тебя поймают?"
            e "Да не переживай ты. Беглый раб нафиг никому не сдался, никто меня искать не будет."
            golname "Ну смотри... Будь осторожнее"
            jump city



    label city:

        if ostalca_v_lecy:


            if poel_v_lesy:
                pass
            
            if poel_v_lesy == False:
                pass


        if ostalca_v_lecy == False:
            pass
      
    return  
