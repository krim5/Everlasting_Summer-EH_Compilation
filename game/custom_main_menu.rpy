
##      Экран кастомного главного меню      ##
screen custom_main_menu:

    tag menu
    modal True

    default flag = renpy.sound.is_playing(channel="ambience")

    $ change_cursor("custom")
    python:
        if flag == False:
            renpy.sound.play(sound_rain, channel="ambience", loop=True)
        else:
            NullAction()

    default n = 0
    showif n == 1:
        add "custom_background_ed" at sw_transform
        frame at sw_transform:
            background Frame(get_image("gui/choice/day/choice_box.png"),50,50)
            xalign 0.2
            yalign 0.5
            left_padding 75 
            right_padding 75 
            bottom_padding 50 
            top_padding 50
            xsize 1000
            ysize 1000
            vbox:
                spacing 10
                xsize 900
                xalign 0.5
                text "{font=[gabriola]}Что будет с человеком, запертым в одном месте в течении пяти лет? А десяти?{/font}" size 40
                text "{font=[gabriola]}Давайте сосредоточимся на психологической стороне вопроса.{/font}" size 40
                text "{font=[gabriola]}Он глубоко уйдет в себя, станет безумцем или будет искать утешение в саморазвитии?{/font}" size 40
                text "{font=[gabriola]}У него будут приступы апатии или вспышки ярости?{/font}" size 40
                text "{font=[gabriola]}А если Семён проведет там еще больше лет? Скажем... тысячу?{/font}" size 40 
                text "{font=[gabriola]}По какой же причине он заперт в своей одиночной камере? Почему он до сих пор один?{/font}" size 40
                text "{font=[gabriola]}Как же устроен Совёнок? И как... как не сойти с ума окончательно?{/font}" size 40
                text "{font=[gabriola]}\n\nСемён провёл в лагере много лет. Так много, что он не помнит, жил ли он когда-то иначе.{/font}" size 40
                text "{font=[gabriola]}Нескончаемые циклы накладываются друг на друга, формируя причудливое сплетение воспоминаний.{/font}" size 40
                text "{font=[gabriola]}История скоро закончится... или только начинается?{/font}" size 40
    elif n == 2:
        add "custom_background_limb" at sw_transform
        frame at sw_transform:
            background Frame(get_image("gui/choice/day/choice_box.png"),50,50)
            xalign 0.2
            yalign 0.5
            left_padding 75 
            right_padding 75 
            bottom_padding 50 
            top_padding 50
            xsize 1000
            ysize 1000
            vbox:
                spacing 10
                xsize 900
                xalign 0.5
                text "{font=[gabriola]}\"Лимб\" — это вызов.{/font}" size 30
                text "{font=[gabriola]}Ничего подобного Ты не видел.{/font}" size 30
                text "{font=[gabriola]}Это настоящий arthouse, я бы даже сказал pleasantly, но по-новому.{/font}" size 30
                text "{font=[gabriola]}Это вызов мне, как сценаристу и визуализатору.{/font}" size 30
                text "{font=[gabriola]}Это вызов нашей команде, её терпению, трудолюбию и воображению.{/font}" size 30
                text "{font=[gabriola]}Это вызов Мастерской, Летосфере и устоявшимся тут шаблонам того, какими могут быть визуальные новеллы и их модификации.{/font}" size 30
                text "{font=[gabriola]}И, конечно же, это вызов Тебе.{/font}" size 30
                text "{font=[gabriola]}Сможешь ли Ты найти выход?{/font}" size 30
                text "{font=[gabriola]}Справишься ли Ты со своими эмоциями?{/font}" size 30
                text "{font=[gabriola]}Найдёшь ли Ты сейф, не говоря уже о том, чтобы открыть его?{/font}" size 30
                text "{font=[gabriola]}Это — всего лишь модификация на Бесконечное Лето.{/font}" size 30
                text "{font=[gabriola]}Лишь небольшая история о дружбе, надежде и родном доме.{/font}" size 30
                text "{font=[gabriola]}Это — более чем 10 часов нелинейного закрученного сюжета, уникального геймплея, оригинальной музыки от 6 исполнителей и круговерти из сотен созданных специально для мода цг, фонов, спрайтов и спецэффектов.{/font}" size 30
                text "{font=[gabriola]}Это — многоуровневые игры разума, лабиринт, в котором нужно не только искать ответы на вопросы, но и суметь сохранить себя.{/font}" size 30
                text "{font=[gabriola]}\nВсё это — \"Лимб\". Вызов.{/font}" size 30
                text "{font=[gabriola]}\nПоверь — если Ты его примешь, то многое переживёшь, многое увидишь, многому поразишься...{/font}" size 30
                text "{font=[gabriola]}И вряд ли об этом пожалеешь.{/font}" size 30
    else:
        add "custom_background_none" at sw_transform
        
    text "{alpha=0.3}{font=[gabriola]}Версия: [config.version]{/font}{/alpha}" size 30 xalign 0.01 yalign 0.99

    vbox:
        spacing 10
        xalign 0.95
        yalign 0.03
        text "{alpha=0.7}{font=[gabriola]}Бесконечное лето:{/font}{/alpha}" size 70
        text "{alpha=0.7}{font=[gabriola]}  Endless Horizons{/font}{/alpha}" size 70

    vbox:
        spacing 5
        xalign 0.97
        yalign 0.9
        imagebutton: ## ОДИНОЧКА
            idle  "custom_gui/buttons/loner_idle.png"
            hover "custom_gui/buttons/loner_hover.png"
            action [Play("sound", "sound/button_click.wav"), SetField(persistent, "jump_to", "ed_work_prep"), Start()]
            hovered SetScreenVariable("n", 1)
            unhovered SetScreenVariable("n", 0)

        imagebutton: ## ЛИМБ
            idle  "custom_gui/buttons/limb_idle.png"
            hover "custom_gui/buttons/limb_hover.png"
            action [Play("sound", "sound/button_click.wav"), SetField(persistent, "jump_to", "limb_intro"), Start()]
            hovered SetScreenVariable("n", 2)
            unhovered SetScreenVariable("n", 0)

        imagebutton: ## Загрузить
            idle  "custom_gui/buttons/load_idle.png"
            hover "custom_gui/buttons/load_hover.png"
            action [ShowMenu('custom_load'), Play("sound", "sound/button_click.wav")]

        imagebutton: ## Настройки
            idle "custom_gui/buttons/options_idle.png"
            hover "custom_gui/buttons/options_hover.png"
            action [ShowMenu('custom_preferences'), Play("sound", "sound/button_click.wav")]

        imagebutton: ## Информация
            idle  "custom_gui/buttons/info_idle.png"
            hover "custom_gui/buttons/info_hover.png"
            action [ShowMenu('custom_help'), Play("sound", "sound/button_click.wav")]

        imagebutton: ## Выйти
            idle  "custom_gui/buttons/exit_idle.png"
            hover "custom_gui/buttons/exit_hover.png"
            action [ShowMenu('custom_quit'), Play("sound", "sound/button_click.wav")]

      
    key "~" action [SetField(persistent, "_use_custom_menu", False), Function(renpy.reload_script), Return()]


##      Экран загрузки      ##
screen custom_load:

    tag menu
    modal True

    window background get_image("custom_gui/save_load/custom_load_bg.png"):

        textbutton "Сохранить" text_font gabriola style "log_button" text_style "settings_link" xalign 0.98 yalign 0.08 action ShowMenu('custom_save')
        textbutton "Настройки" text_font gabriola style "log_button" text_style "settings_link" xalign 0.02 yalign 0.08 action ShowMenu('custom_preferences')

        hbox xalign 0.5 yalign 0.08:
            add "custom_gui/misc/sparkle_gloomy.png" yalign 0.3
            text " "+"ЗАГРУЗИТЬ"+" " font gabriola style "settings_link" yalign 0.5 color "#ffffff"
            add "custom_gui/misc/sparkle_gloomy.png" yalign 0.3

        textbutton "Назад" text_font gabriola style "log_button" text_style "settings_link" xalign 0.015 yalign 0.92 action Return()

        textbutton "Загрузить игру" text_font gabriola style "log_button" text_style "settings_link" yalign 0.92 xalign 0.5 action (FunctionCallback(on_load_callback,selected_slot), FileLoad(selected_slot))

        textbutton "{size=-12}{b}x{/b} {/size}"+"Удалить" text_font gabriola style "log_button" text_style "settings_link" yalign 0.92 xalign 0.97 action FileDelete(selected_slot)

        vbox xalign 0.023 yalign 0.5:
            grid 1 10:
                for i in range(0, 10):
                    if i == 0:
                        textbutton "Авто" text_font gabriola text_size 50 style "log_button" text_style "settings_link" action (FilePage("auto"), SetVariable("selected_slot", False))
                    else:
                        textbutton str(i) text_font gabriola text_size 50 right_padding 50 style "log_button" text_style "settings_link" action (FilePage(i), SetVariable("selected_slot", False))

        grid 4 3 xpos 0.13 ypos 0.2 xmaximum 0.81 ymaximum 0.65:
            transpose False
            xfill True
            yfill True
            for i in range(1, 13):

                fixed:
                    add FileScreenshot(i) xpos 10 ypos 10

                    button:
                        action SetVariable("selected_slot", i)
                        xfill False
                        yfill False
                        style "custom_save_load_button"
                        has fixed
                        text ( "%s." % i
                                + FileTime(i, format=' %d.%m.%y, %H:%M', empty=" Пустой слот")
                                + "\n" +FileSaveName(i)) style "file_picker_text" xpos 15 ypos 15

##      Экран сохранения        ##
screen custom_save:

    tag menu
    modal True

    window background get_image("custom_gui/save_load/custom_save_bg.png"):

        textbutton "Загрузить" text_font gabriola style "log_button" text_style "settings_link" xalign 0.98 yalign 0.08 action ShowMenu('custom_load')
        textbutton "Настройки" text_font gabriola style "log_button" text_style "settings_link" xalign 0.02 yalign 0.08 action ShowMenu('custom_preferences')
        hbox xalign 0.5 yalign 0.08:
            add "custom_gui/misc/sparkle_gloomy.png" yalign 0.3
            text " "+"СОХРАНИТЬ"+" " font gabriola style "settings_link" yalign 0.5 color "#ffffff"
            add "custom_gui/misc/sparkle_gloomy.png" yalign 0.3
        
        textbutton "Назад" text_font gabriola style "log_button" text_style "settings_link" xalign 0.015 yalign 0.92 action Return()

        textbutton "Сохранить игру" text_font gabriola style "log_button" text_style "settings_link" yalign 0.92 xalign 0.5 action (FunctionCallback(on_save_callback, selected_slot), FileSave(selected_slot))
        textbutton "{size=-12}{b}x{/b} {/size}"+"Удалить" text_font gabriola style "log_button" text_style "settings_link" yalign 0.92 xalign 0.97 action FileDelete(selected_slot)

        vbox xalign 0.023 yalign 0.5:
            grid 1 10:
                for i in range(0, 10):
                    if i == 0:
                        textbutton "Авто" text_font gabriola text_size 50 style "log_button" text_style "settings_link" action (FilePage("auto"), SetVariable("selected_slot", False))
                    else:
                        textbutton str(i) text_font gabriola text_size 50 right_padding 50 style "log_button" text_style "settings_link" action (FilePage(i), SetVariable("selected_slot", False))

        grid 4 3 xpos 0.13 ypos 0.2 xmaximum 0.81 ymaximum 0.65:
            transpose False
            xfill True
            yfill True
            for i in range(1, 13):
                fixed:
                    add FileScreenshot(i) xpos 10 ypos 10

                    button:
                        action SetVariable("selected_slot", i)
                        xfill False
                        yfill False
                        style "custom_save_load_button"
                        has fixed
                        text ( "%s." % i
                               + FileTime(i, format=' %d.%m.%y, %H:%M', empty=" Пустой слот")
                               + "\n" +FileSaveName(i)) style "file_picker_text" xpos 15 ypos 15

##      Экран настроек      ##
screen custom_preferences:

    tag menu
    modal True

    # $ change_cursor("custom")

    $ bar_null = Frame(get_image("custom_gui/settings/custom_bar_null.png"),36,36)
    $ bar_full = Frame(get_image("custom_gui/settings/custom_bar_full.png"),36,36)

    window background get_image("custom_gui/settings/custom_preferences_bg.png"):

        textbutton "Сохранить" text_font gabriola style "log_button" text_style "settings_link" xalign 0.02 yalign 0.08 action ShowMenu('custom_save')
        textbutton "Загрузить" text_font gabriola style "log_button" text_style "settings_link" xalign 0.98 yalign 0.08 action ShowMenu('custom_load')
        hbox xalign 0.5 yalign 0.08:
            add "custom_gui/misc/sparkle_gloomy.png" yalign 0.3
            text " "+"НАСТРОЙКИ"+" " font gabriola style "settings_link" yalign 0.5 color "#ffffff"
            add "custom_gui/misc/sparkle_gloomy.png" yalign 0.3
        
        textbutton "Назад" text_font gabriola style "log_button" text_style "settings_link" xalign 0.015 yalign 0.92 action Return()

        side "c b r":
            area (0.25, 0.23, 0.51, 0.71)
            viewport id "preferences":
                mousewheel True
                scrollbars None

                has grid 1 21 xfill True spacing 15
                text translation_new["Window_mode"] style "settings_header" xalign 0.5
                grid 2 1 xfill True:

                    hbox xalign 0.5:
                        if _preferences.fullscreen:
                            add get_image("custom_gui/settings/custom_leaf.png") ypos 0.12
                        else:
                            null width 22
                        textbutton translation_new["Fullscreen"] style "log_button" text_style "settings_text" action Preference("display", "fullscreen")

                    hbox xalign 0.5:
                        if not _preferences.fullscreen:
                            add get_image("custom_gui/settings/custom_leaf.png") ypos 0.12
                        else:
                            null width 22
                        textbutton translation_new["Window"] style "log_button" text_style "settings_text" action Preference("display", "window")



                text translation_new["Skip"] style "settings_header" xalign 0.5
                grid 2 1 xfill True:

                    hbox xalign 0.5:
                        if _preferences.skip_unseen:
                            add get_image("custom_gui/settings/custom_leaf.png") ypos 0.12
                        else:
                            null width 22
                        textbutton translation_new["Skip_all"] style "log_button" text_style "settings_text" action Preference("skip", "all")

                    hbox xalign 0.5:
                        if not _preferences.skip_unseen:
                            add get_image("custom_gui/settings/custom_leaf.png") ypos 0.12
                        else:
                            null width 22
                        textbutton translation_new["Skip_seen"] style "log_button" text_style "settings_text" action Preference("skip", "seen")


                text translation_new["Volume"] style "settings_header" xalign 0.5

                grid 2 1 xfill True:
                    textbutton translation_new["Music_lower"] style "log_button" text_style "settings_text" xpos 0.1
                    bar value Preference("music volume") left_bar bar_full right_bar bar_null thumb "images/custom_gui/settings/custom_htumb.png" hover_thumb "images/custom_gui/settings/custom_htumb.png" xmaximum 1.35 ymaximum 36 xpos -0.55

                grid 2 1 xfill True:
                    textbutton translation_new["Sound"] style "log_button" text_style "settings_text" xpos 0.1
                    bar value Preference("sound volume") left_bar bar_full right_bar bar_null thumb "images/custom_gui/settings/custom_htumb.png" hover_thumb "images/custom_gui/settings/custom_htumb.png" xmaximum 1.35 ymaximum 36 xpos -0.55

                grid 2 1 xfill True:
                    textbutton translation_new["Ambience"] style "log_button" text_style "settings_text" xpos 0.1
                    bar value Preference("voice volume") left_bar bar_full right_bar bar_null thumb "images/custom_gui/settings/custom_htumb.png" hover_thumb "images/custom_gui/settings/custom_htumb.png" xmaximum 1.35 ymaximum 36 xpos -0.55

                text translation_new["Text_speed"] style "settings_header" xalign 0.5
                bar value Preference("text speed") left_bar bar_full right_bar bar_null thumb "images/custom_gui/settings/custom_htumb.png" hover_thumb "images/custom_gui/settings/custom_htumb.png" xalign 0.5 xmaximum 0.8 ymaximum 36

                text translation_new["Autoforward"] style "settings_header" xalign 0.5
                grid 2 1 xfill True:

                    hbox xalign 0.5:
                        if _preferences.afm_time != 0:
                            add get_image("custom_gui/settings/custom_leaf.png") ypos 0.12
                        else:
                            null width 22
                        textbutton translation_new["Adult_content_on"] style "log_button" text_style "settings_text" action Preference("auto-forward after click", "enable")

                    hbox xalign 0.5:
                        if _preferences.afm_time == 0:
                            add get_image("custom_gui/settings/custom_leaf.png") ypos 0.12
                        else:
                            null width 22
                        textbutton translation_new["Adult_content_off"] style "log_button" text_style "settings_text" action (Preference("auto-forward time", 0), Preference("auto-forward after click", "disable"))

                text translation_new["Autoforward_time"] style "settings_header" xalign 0.5
                bar value Preference("auto-forward time") left_bar bar_full right_bar bar_null thumb "images/custom_gui/settings/custom_htumb.png" hover_thumb "images/custom_gui/settings/custom_htumb.png" xalign 0.5 xmaximum 0.8 ymaximum 36


                text translation_new["Font"] style "settings_header" xalign 0.5
                grid 2 1 xfill True:
                    hbox xalign 0.5:
                        if persistent.font_size == "small":
                            add get_image("custom_gui/settings/custom_leaf.png") ypos 0.12
                        else:
                            null width 22
                        textbutton translation_new["Normal_font"] style "log_button" text_style "settings_text" action SetField(persistent, "font_size", "small")

                    hbox xalign 0.5:
                        if not persistent.font_size == "small":
                            add get_image("custom_gui/settings/custom_leaf.png") ypos 0.12
                        else:
                            null width 22
                        textbutton translation_new["Big_font"] style "log_button" text_style "settings_text" action SetField(persistent, "font_size", "large")
                
                text "Трейлеры модификаций" style "settings_header" xalign 0.5
                grid 2 1 xfill True:
                    hbox xalign 0.5:
                        if persistent.trailers_on:
                            add get_image("custom_gui/settings/custom_leaf.png") ypos 0.12
                        else:
                            null width 22
                        textbutton "Включить" style "log_button" text_style "settings_text" action SetField(persistent, "trailers_on", True)

                    hbox xalign 0.5:
                        if not persistent.trailers_on:
                            add get_image("custom_gui/settings/custom_leaf.png") ypos 0.12
                        else:
                            null width 22
                        textbutton "Выключить" style "log_button" text_style "settings_text" action SetField(persistent, "trailers_on", False)

                text "Старая музыка для Одиночки" style "settings_header" xalign 0.5
                grid 2 1 xfill True:
                    hbox xalign 0.5:
                        if persistent.ed_old_music:
                            add get_image("custom_gui/settings/custom_leaf.png") ypos 0.12
                        else:
                            null width 22
                        textbutton "Включить" style "log_button" text_style "settings_text" action [ SetField(persistent, "ed_old_music", True), Function(renpy.reload_script) ]

                    hbox xalign 0.5:
                        if not persistent.ed_old_music:
                            add get_image("custom_gui/settings/custom_leaf.png") ypos 0.12
                        else:
                            null width 22
                        textbutton "Выключить" style "log_button" text_style "settings_text" action [ SetField(persistent, "ed_old_music", False), Function(renpy.reload_script) ]


                
                null

            bar value XScrollValue("preferences") left_bar "images/misc/none.png" right_bar "images/misc/none.png" thumb "images/misc/none.png" hover_thumb "images/misc/none.png"
            vbar value YScrollValue("preferences") bottom_bar "images/misc/none.png" top_bar "images/misc/none.png" thumb "images/custom_gui/settings/custom_vthumb.png" thumb_offset -12

##      Экран информации        ##
screen custom_help:

    tag menu
    modal True

    window background get_image("custom_gui/info/info_bg.png"):

        hbox xalign 0.5 yalign 0.08:
            add "custom_gui/misc/sparkle_gloomy.png" yalign 0.65
            text " "+"{font=[gabriola]}Информация{/font}"+" " style "settings_link" yalign 0.5 color "#ffffff"
            add "custom_gui/misc/sparkle_gloomy.png" yalign 0.65

        textbutton "{font=[gabriola]}Назад{/font}" style "log_button" text_style "settings_link" xalign 0.015 yalign 0.92 action Return()

        vbox xpos 0.25 ypos 0.15 xsize 1150 spacing 20:
            text "Нашли ошибку или есть вопросы и предложения касательно проекта? Писать мне в {a=https://vk.com/cr1m5}{font=[gabriola]}ВК{/font}{/a}" style "settings_link" font gabriola
            text "Вопросы по поводу сюжета, продолжения, а также поиск актуальных новостей - {a=https://vk.com/endhor}{font=[gabriola]}СЮДА{/font}{/a}" style "settings_link" font gabriola
            text "Проект на {a=https://github.com/krim5/Everlasting_Summer-EH_Compilation}{font=[gabriola]}Git-Hub{/font}{/a}" style "settings_link" font gabriola
            text "Разработчики модификаций: Endless Horizons (ссылки не будет, команда распалась. Press F)" style "settings_link" font gabriola
            text "Страницы {a=https://steamcommunity.com/sharedfiles/filedetails/?id=1126116478}{font=[gabriola]}Одиночки{/font}{/a} и {a=https://steamcommunity.com/sharedfiles/filedetails/?id=1520956125}{font=[gabriola]}Лимба{/font}{/a} в стиме" style "settings_link" font gabriola
            null
            null
            text "Разработчики лета: {a=https://sovietgames.su/}{font=[gabriola]}Soviet Games{/font}{/font}" style "settings_link" font gabriola

        key "f" action(Play("sound", "sound/vine_boom.ogg"))
        key "F" action(Play("sound", "sound/vine_boom.ogg"))
        key "а" action(Play("sound", "sound/vine_boom.ogg"))
        key "А" action(Play("sound", "sound/vine_boom.ogg"))
    


##      Экран выхода        ##
screen custom_quit:

    tag menu
    modal True

    add get_image("custom_gui/custom_exit.jpg")

    text "{font=[limb_font_3]}Вы действительно{vspace=20}хотите выйти из игры?{/font}" size 60 style "settings_link" text_align 0.5 xalign 0.6 yalign 0.4 color "#000000" outlines [(3,"#8d8d8d",0,0)] antialias True kerning 2

    textbutton "{font=[limb_font_3]}Да{/font}":
        text_size 70 
        style "log_button" 
        text_style "settings_link" 
        xalign 0.41 
        yalign 0.6 
        text_color "#000000" 
        text_hover_color "#ffffff"
        text_outlines [(3,"#8d8d8d",0,0)]
        text_hover_outlines [(3,"#ff7b02",0,0)]
        action Quit(confirm=False)
    
    textbutton "{font=[limb_font_3]}Нет{/font}": 
        text_size 70 
        style "log_button" 
        text_style "settings_link" 
        xalign 0.75 
        yalign 0.6 
        text_color "#000000" 
        text_hover_color "#ffffff"
        text_outlines [(3,"#8d8d8d",0,0)]
        text_hover_outlines [(3,"#ff7b02",0,0)]
        action Return()
