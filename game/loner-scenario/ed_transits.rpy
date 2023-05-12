label cold_end: ## Царский обед

    $ ed_time('prologue')
    stop ambience fadeout 2
    $ _window_show(dissolve)
    play music ed_snare fadein 2
    scene cg ed_snow_camp_1
    show prologue_dream
    with flash

    "Ледяной ветер пронизывает моё тело до костей, ведь рубашка плохо защищает от мороза."
    "Ноги вмёрзли в снег, и, даже если бы я хотел встать, не смог бы."

    scene cg ed_snow_camp_2
    show prologue_dream
    with dissolve2

    "Я с трудом дотронулся обмороженной рукой до щеки, но ничего не понял. "
    "Уверен, что по ним текут ледяные дорожки."

    scene cg ed_snow_camp_3
    show prologue_dream
    with dissolve2

    "Слёзы бессилия и отчаяния."
    "Больно{w=0.3}.{w=0.3}.{w=0.3}."

    $ _window_hide(dissolve)
    stop music fadeout 2
    scene bg white with dissolve2
    $ persistent.ed_lif_achieve_cold_heart = True
    $ show_ed_achiv("cold_heart")
    return

label void_end: ## Прячется на стадионе

    $ ed_time('prologue')
    stop ambience fadeout 2
    $ _window_show(dissolve)
    play music ed_snare fadein 2
    scene cg ed_stars
    show prologue_dream
    with dissolve2

    "Поражающая воображение пустота. "
    "И одновременно{w=0.3}.{w=0.3}.{w=0.3}."
    "Сотни звёзд."
    "Одновременно пустое и заполненное, мёртвое и живое, ужасное и прекрасное пространство."
    "Куда бы не взглянув, я вижу лишь множество коридоров - и свет в конце каждого из них."
    "Подумать только, я мог столь многое{w=0.3}.{w=0.3}.{w=0.3}."
    "Становится холодно."

    scene bg black with Dissolve(4.0)

    "Я{w=0.3}.{w=0.3}.{w=0.3}."

    $ renpy.pause(1)
    $ _window_hide(dissolve)
    stop music fadeout 2
    $ persistent.ed_lif_achieve_starboy = True
    $ show_ed_achiv("starboy")
    return

label heat_end: ## Сжечь автобус

    $ ed_time('prologue')
    stop ambience fadeout 2
    play music ed_snare fadein 2
    scene bg int_dining_hall_burn_bright
    show prologue_dream
    with ed_night_dis
    $ _window_show(dissolve)

    "Жар опаляет лицо."
    edhe "Это куда круче бани!"
    eds "Всё могло быть иначе!"
    edhe "Нет, не могло!"
    eds "Мне лучше знать! Останови это!"

    scene bg int_dining_hall_burn_dark
    show prologue_dream
    with dissolve2

    edhe "Ты вообще {b}ничего{/b} не знаешь! Защищайся, размазня! Или ты сдрейфил?!"
    "Наши клинки столкнулись, и я чуть не угодил в лаву."
    eds "Сука!"
    edhe "Не выражайся."
    "Страшный удар в лицо{w=0.3}.{w=0.3}.{w=0.3}."
    "Кто он? Кто Он? Я дерусь сам с собой? Когда это было? Я сошёл с ума полностью? Почему мне так больно?! Больно!.."
    "Я будто вижу себя и стараюсь сам себе причинить боль; я будто и подсудимый на скамье, и судья, выносящий приговор; и даже присяжные - тоже я... другие Я."
    "А в качестве зала суда - объятое пламенем здание столовой, где все Мы сидим за разными столами, и Ольга подходит к каждому из нас..."
    "Когда это началось?{w=1} Не знаю. "
    "Когда придёт конец?{w=1} Не знаю. "
    "Я тону в бесконечном водовороте отчаяния, моя душа навеки погребена под виной содеянного, и наказание моё - не просто пылающее в огне раскаяния тело... а отсутствие памяти о том, что я совершил. "
    "Я горю... Горю! Больно! Помогите! Я... "

    $ _window_hide(dissolve)
    stop music fadeout 2
    scene bg black with dissolve2
    $ persistent.ed_lif_achieve_lava_floor = True
    $ show_ed_achiv("lava_floor")
    return

label lib_end: ## Библиотека

    $ ed_time('prologue')
    stop ambience fadeout 2
    play music ed_snare fadein 2
    scene cg ed_shadow_around
    show prologue_dream
    with ed_night_dis
    $ _window_show(dissolve)

    "Я наношу удары направо и налево, рублю и колю их бесчисленные тела, как дрова."
    "А они наносят удары мне. Царапают, рвут и кусают меня, пытаясь разорвать на части. "
    "Кровь заливает глаза, я уже почти ничего не вижу и очень, очень устал. "
    "Я двигаюсь всё медленнее, а эти бестии не устают! "
    "Не успеваю{w=0.3}.{w=0.3}.{w=0.3}."

    $ _window_hide(dissolve)
    stop music fadeout 2
    scene bg black with dissolve2
    $ persistent.ed_lif_achieve_un_library = True
    $ show_ed_achiv("un_library")
    return

label silence_end: ## Хочу супа или кашу

    $ ed_time('prologue')
    stop ambience fadeout 2
    play music ed_snare fadein 2
    scene cg ed_silhouette
    show prologue_dream
    with ed_night_dis
    $ _window_show(dissolve)

    "Тишина."
    "У меня нет сил кричать. Или двигаться."
    "Всё, что осталось - это возможность испытывать боль. Каждой клеткой тела."
    "Не знаю, сколько времени длится пытка."
    "И уже не понимаю, кто кого пытает."
    "Не важно, что дальше."
    "Останови это{w=0.3}.{w=0.3}.{w=0.3}."
    "ОСТАНОВИ ЭТО!!!"

    $ _window_hide(dissolve)
    stop music fadeout 2
    scene bg black with dissolve2
    $ persistent.ed_lif_achieve_no_harm_in_trying = True
    $ show_ed_achiv("no_harm_in_trying")
    return

label idleness_end: ## Пристань. Не делать ничего

    show black
    $ ed_time('prologue')
    stop ambience fadeout 2
    play music ed_snare fadein 2
    scene bg ext_forest_rainy_1 at ed_running
    show prologue_dream
    with dissolve2
    $ _window_show(dissolve)

    "Я хриплю и задыхаюсь, но невыносимый ужас не позволяет стоять на месте. "
    "Не вижу дороги в этой мерзкой темноте, но у меня нет выхода."
    "Я несусь сквозь лес, спотыкаясь о кочки и коряги. Очень устал{w=0.3}.{w=0.3}.{w=0.3}. "
    "Но останавливаться никак нельзя!"
    "Нельзя{w=0.3}.{w=0.3}.{w=0.3}."

    scene bg ext_forest_rainy_2
    show prologue_dream
    with dissolve
    play sound sfx_bodyfall_1

    "Я бессильно провалился к стволу дерева и сполз на землю, пытаясь отдышаться."
    "Пот затекает в глаза и уши."
    "Я закашлялся."
    "И в этот же момент за спиной раздались ЗВУКИ. Негромкие, даже вкрадчивые. "
    "Мы знакомы. Я взвыл."
    eds "НЕЕЕЕТ!!!"

    scene bg ext_forest_rainy_2 at ed_running
    show prologue_dream
    with dissolve

    "Я снова рванул в тьму, но в этот раз меня уже не отпустили."

    scene bg ext_forest_rainy_2
    show prologue_dream
    with vpunch

    "Внезапно отнялась левая нога."
    "Я обречённо посмотрел на неё{w=0.3}.{w=0.3}.{w=0.3}."

    $ _window_hide(dissolve)
    stop music fadeout 2
    scene bg black with dissolve2
    $ persistent.ed_lif_achieve_earth_center = True
    $ show_ed_achiv("earth_center")
    return

label darkness_end: ## Повернуть назад

    $ ed_time('prologue')
    stop ambience fadeout 2
    play music ed_snare fadein 2
    scene cg ed_red_eyes
    show prologue_dream
    with dissolve2
    $ _window_show(dissolve)

    "Холодные пальцы все глубже впиваются в горло."
    "А красные глаза, в которых нет ничего человеческого, бесстрастно смотрят на смерть."
    eds "Ех{w=0.3}.{w=0.3}.{w=0.3}. Ле{w=0.3}.{w=0.3}.{w=0.3}. Х{w=0.3}.{w=0.3}.{w=0.3}."
    "Пальцы бессильно скребут по руке убийцы."
    "Ноги извиваются в воздухе."
    "Глаза закатываются."
    "Падаю в темноту. "
    "Я ничего не способен противопоставить"

    $ _window_hide(dissolve)
    stop music fadeout 2
    scene bg black with ed_night_dis
    $ persistent.ed_lif_achieve_femdom = True
    $ show_ed_achiv("femdom")
    return

label dv_us_end: ## К домику

    $ ed_time('prologue')
    stop ambience fadeout 2
    play music ed_snare fadein 2
    scene cg ed_sem_old_building
    show prologue_dream
    with flash
    $ _window_show(dissolve)

    "Я верю только в то, что вижу."
    "Всегда так было. "
    "Я смотрю в свои собственные глаза - глаза человека, познавшего невообразимое."
    "Я сжимаю руки на своём же горле, желая лишь одного - не позволить страдать так, как страдал Я."
    "Я убиваю."
    "Я умираю."
    "Я умер, и Я стою над своим телом, сжимая и разжимая кулаки."

    $ _window_hide(dissolve)
    stop music fadeout 2
    scene bg black with dissolve2
    $ persistent.ed_lif_achieve_my_shadow = True
    $ show_ed_achiv("my_shadow")
    return

label sa_end: ## Уныние

    $ ed_time('prologue')
    stop ambience fadeout 2
    play music ed_snare fadein 2
    scene bg ext_boathouse_night
    show prologue_dream
    with dissolve2
    $ _window_show(dissolve)

    "Улыбаясь сквозь песок и слёзы, я подбираю вёсла и бреду, пока не натыкаюсь на лодку. Она спокойно качается в воде озера, не зная горестей."

    scene cg ed_un_boat_no_un
    show prologue_dream
    with dissolve2

    "Как же мне всё опостылело!"
    "Я смотрю на лодку, на вёсла, на верёвку, которой пришвартована лодка к пристани, на умиротворённую гладь озера…"

    scene cg ed_lake_night_2
    show prologue_dream
    with dissolve2

    "Решение просто."
    "Я просто закончу всё здесь и сейчас. И никогда, никогда больше не вернусь в проклятый Совёнок…"

    $ _window_hide(dissolve)
    stop music fadeout 2
    scene bg black with dissolve2
    $ persistent.ed_lif_achieve_carousel = True
    $ show_ed_achiv("carousel")
    return

label run_end: ## Она может что-то знать

    $ ed_time('prologue')
    stop ambience fadeout 2
    play music ed_snare fadein 2
    scene bg int_white_hall at ed_running
    show prologue_dream
    with dissolve
    $ _window_show(dissolve)

    "Я бегу из тьмы туннеля к свету, понимая, что у меня осталась всего минута. "
    "Я должен успеть, я должен, должен!"
    "Впереди – закрывающиеся двери."
    "Позади – нарастающий гул. "
    "Я прыгаю вперёд, неудачно приземляюсь на правую ногу. Подвернул…"
    eds "Нееет!"
    "Оборачиваюсь, и…"

    $ _window_hide(dissolve)
    stop music fadeout 2
    scene bg black with dissolve2
    $ persistent.ed_lif_achieve_not_called = True
    $ show_ed_achiv("not_called")
    return

label beach_end: ## Заснуть

    $ ed_time('prologue')
    stop ambience fadeout 2
    play music ed_snare fadein 2
    scene bg ext_bright_beach
    show prologue_dream
    with flash
    $ _window_show(dissolve)

    "Играет типичная музыка с курорта"
    "Я лежу под палящим солнцем, но бриз дарует ощущение комфорта, забирая излишки тепла, а море нежно ласкает слух шумом прибоя. "
    "Я счастлив."

    show dv smile swim at cleft behind prologue_dream
    with dissolve

    edfdv "Семён, ты хочешь поиграть в мяч?"

    show un grin dress at cright behind prologue_dream
    with dissolve

    edfun "Сеня, давай позагораем!"

    show dv grin behind prologue_dream

    edfdv "Эй, это мой парень!"

    show un shy behind prologue_dream

    edfun "А вот и нет, скажи ей, Сеня!"
    me "Девочки, девочки, тише, меня на всех хватит!"

    show dv laugh behind prologue_dream:
        pos(0.35, 0.5)
        anchor(0.5, 0.5)
        zoom 1
        linear 1 zoom 1.25
    show un laugh behind prologue_dream:
        pos(0.65, 0.5)
        anchor(0.5, 0.5)
        zoom 1
        linear 1 zoom 1.25
        pause 1.5
        linear 0.5 zoom 1.6

    "Я протягиваю к ним руки, а мои любимые радостно бегут ко мне. Лена наклоняется к моему уху и шепчет:"

    edfun "Ты в курсе, что умер? И я, кстати, не Лена."
    me "Э?"

    $ _window_hide(dissolve)
    stop music fadeout 2
    scene bg black with ed_earth_draw
    $ persistent.ed_lif_achieve_beach_madness = True
    $ show_ed_achiv("beach_madness")
    return

label cannibal_end: ## Хочу жареных пионеров

    $ ed_time('prologue')
    stop ambience fadeout 2
    play music music_list["gentle_predator"] fadein 2
    scene cg ed_cannibal_end
    show prologue_dream
    with flash
    $ _window_show(dissolve)

    "Огонь."
    "Пламя!"
    "Жарко!!"
    "Страшно!!!"
    "Он горел и горел, неспешно вращаясь вокруг своей оси, и слишком был занят тем, что кричал, чтобы понять очевидную вещь."
    "А именно то, что его жарят на мангале, наказывая за недостойное главного героя чревоугодие."
    "Всем Семёнам свойственно ошибаться и не выносить уроков из своей жизни. "
    "Но конкретно этот Персунов выделился."
    "Он настолько всех заколебал своим ослиным упорством и желанием жрать людей, что успешно победил и интерес игрока, и желание Автора сохранить ему жизнь."
    "Запомни, Семён: пионерки не для еды! Ты делаешь это неправильно!"

    $ _window_hide(dissolve)
    stop music fadeout 2
    scene bg black with dissolve2
    $ persistent.ed_lif_achieve_darvin = True
    $ show_ed_achiv("darvin")
    return

label no_end: ## Пристань. Нет

    $ ed_time('prologue')
    stop ambience fadeout 2
    play music ed_snare fadein 2
    scene bg ext_old_building_sunset_red_ed
    show prologue_dream
    with dissolve2
    $ _window_show(dissolve)

    "Я подхожу к зданию, подавляя дрожь."
    "Неужели всё закончится здесь и сейчас? "
    "Неужели ответ так и прятался под моим носом?"
    "Возможно ли, что я понимал всё совершенно неверно? Я действительно {b}то{/b}, чем она меня называет?"
    "Кто же тогда она?"
    "И… что же будет дальше?{w=0.3}.{w=0.3}.{w=0.3}."

    $ _window_hide(dissolve)
    stop music fadeout 2
    scene bg black with dissolve2
    $ persistent.ed_lif_achieve_in_the_end = True
    $ show_ed_achiv("in_the_end")
    return

label med_end: ## Пойти в медпункт

    show black
    $ ed_time('prologue')
    stop ambience fadeout 2
    play music ed_snare fadein 2
    scene bg ext_camp_path_night at ed_running_fast
    show prologue_dream
    with flash
    $ _window_show(dissolve)

    "Я резко повернулся и бросился бежать. "

    play sound sfx_slavya_run
    scene bg ext_camp_path_night at ed_running_fast
    show prologue_dream

    "Ни в коем случае нельзя оборачиваться."
    "За спиной слышно шум движения. И дыхание…"
    "Нельзя!"

    play sound sfx_slavya_run

    "Ведь там, за мной, двигается {b}это{/b}."
    "Жажда крови висит в воздухе, мешая бежать."
    "Я бегу изо всех сил, потому что единственный мой шанс – в скорости. "
    "Тогда мы, возможно, сумеем выжить…"

    $ _window_hide(dissolve)
    stop music fadeout 2
    scene bg black with dissolve2
    $ persistent.ed_lif_achieve_only_chance = True
    $ show_ed_achiv("only_chance")
    return

label ed_d2_qte_achiv:
    if persistent.ed_qte_fire != True:
        $ persistent.ed_qte_fire = ed_qte_fire
    if persistent.ed_qte_gas != True:
        $ persistent.ed_qte_gas = ed_qte_gas
    if persistent.ed_qte_glass != True:
        $ persistent.ed_qte_glass = ed_qte_glass

    if persistent.ed_qte_all != True:
        if persistent.ed_qte_fire == True and persistent.ed_qte_gas == True and persistent.ed_qte_glass == True:
            $ persistent.ed_qte_all = True

    if persistent.ed_qte_all == True:
        $ _window_hide(dissolve)
        $ show_ed_achiv("fastest_hand")
        $ _window_show(dissolve)
    return
