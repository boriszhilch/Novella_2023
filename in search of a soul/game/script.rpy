﻿
define e = Character('Эльмир', color="#5e605eff")
define hoz = Character('Хозяин', color="#0c0c0cff")
define goloc = Character('Голос в голове', color="#5e605eff")



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
            goloc 'это дохуя, тебе хватит.'
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
                    jump bad_end

                "Довериться":
                    jump igraem_dalche
                    
            label igraem_dalche:
                e 'Хорошо, звучит сомнительно, но заебался так жить уже, поэтому пофиг'
                e 'Поэтому я просто доверюсь странному голосу в голове.'
                goloc "Вот и славно :) а теперь ложись спать, тебе завтра понадобится много сил"
                jump next_day
    
    
label bad_end:
    scene
    "\'Вы прошли игру.\'"
    
    return
        



    
