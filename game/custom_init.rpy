init 100 python:
    ##      Курсоры       ##
    config.mouse = {}
    config.mouse["default"] = [('images/misc/mouse/default_mouse.png', 0, 0)]
    config.mouse["custom"] = [('images/misc/mouse/custom_mouse.png', 0, 0)]
    config.mouse["ed_mouse"] = [('images/misc/mouse/ed_mouse.png', 0, 0)]
    config.mouse["limb_mouse"] = [('images/misc/mouse/limb_mouse.png', 0, 0)]


    def change_cursor(name="default"):
        global default_mouse
        default_mouse = str(name)

    ##      Активация кастомного меню      ##
    if persistent._use_custom_menu is None:
        persistent._use_custom_menu = True 
    

    ##      Музыка главного меню        ##
    def menu_music(name="sound/music/blow_with_the_fires.ogg"):
        global main_menu_music
        config.main_menu_music = str(name)

    ##      Музыка главного меню       ##
    if persistent._use_custom_menu:
        config.main_menu_music = limb_music + "pl_uc_good_morning_morgan.mp3"
    else:
        config.main_menu_music = "sound/music/blow_with_the_fires.ogg"

    ##      Рестарт     ##
    def restart():
        renpy.full_restart()


    ##      Шрифты      ##
    bolero_script = "custom_gui/fonts/bolero_script.ttf"
    gabriola = "custom_gui/fonts/gabriola.ttf"

    ##      Трейлеры     ##
    if persistent.trailers_on is None:
        persistent.trailers_on = True

    ##      Музыка Одиночки     ##
    if persistent.ed_old_music is None:
        persistent.ed_old_music = False


    
init 100:
    ##      Стили       ##
    $ style.custom_save_load_button = Style(style.button)
    $ style.custom_save_load_button.background = "custom_gui/save_load/thumbnail_idle.png"
    $ style.custom_save_load_button.hover_background = "custom_gui/save_load/thumbnail_hover.png"
    $ style.custom_save_load_button.selected_background = "custom_gui/save_load/thumbnail_selected.png"
    $ style.custom_save_load_button.selected_hover_background = "custom_gui/save_load/thumbnail_selected.png"
    $ style.custom_save_load_button.selected_idle_background = "custom_gui/save_load/thumbnail_selected.png"


    # if persistent._use_custom_menu:
    #     $ style.settings_link.font  = gabriola

    ##      Дисклеймер      ##
    define custom_disclaimer = "images/custom_gui/custom_disclaimer.png"

    ##      Бэкграунд       ##
    image custom_background_none:
        contains:
            'bg ext_camp_entrance_dark_1' with Dissolve(3)
            pause 3
            choice:
                pause 4
                'bg ext_camp_entrance_dark_2' with Dissolve(1)
                pause 1
            choice:
                pause 6
                'bg ext_camp_entrance_dark_2' with Dissolve(2)
                pause 2
            choice:
                pause 8
                'bg ext_camp_entrance_dark_2' with Dissolve(3)
                pause 3
            choice:
                pause 10
                'bg ext_camp_entrance_dark_2' with Dissolve(2)
                pause 2
            repeat
        contains:
            'limb_eff_hard_rain'
        contains:
            'limb_eff_light_rain'

    image custom_background_ed:
        contains:
            'bg ext_camp_entrance_mars'
        contains:
            'limb_eff_blood_rain_r'
        contains:
            'limb_eff_blood_rain_r'
        contains:
            'limb_eff_blood_rain_r'

    image custom_background_limb:
        contains:
            'bg ext_camp_entrance_dark_2'
        contains:
            'limb_eff_hard_rain_l'
        contains:
            'limb_eff_light_rain_l'
        

    ##      Анимации        ##
    transform sw_transform:
        on appear:
            alpha 1.0
        on show:
            linear .5 alpha 1.0
        on hide:
            linear .5 alpha 0.0


