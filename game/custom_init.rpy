init -999 python:

    ##      Версия      ##
    current_ver = "1.0"




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

    if persistent._use_custom_menu:
        config.main_menu_music = "mods/Limb/resourses/sound/music/pl_uc_good_morning_morgan.mp3"
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
        persistent.ed_old_music = True

    
init 100:
    ##      Стили       ##
    $ style.custom_save_load_button = Style(style.button)
    $ style.custom_save_load_button.background = "custom_gui/save_load/thumbnail_idle.png"
    $ style.custom_save_load_button.hover_background = "custom_gui/save_load/thumbnail_hover.png"
    $ style.custom_save_load_button.selected_background = "custom_gui/save_load/thumbnail_selected.png"
    $ style.custom_save_load_button.selected_hover_background = "custom_gui/save_load/thumbnail_selected.png"
    $ style.custom_save_load_button.selected_idle_background = "custom_gui/save_load/thumbnail_selected.png"


    ##      Грозы-sfx и дождь       ##
    $ sfx_thunder_1 = "sound/sfx/thunder/thunder_1.mp3"
    $ sfx_thunder_2 = "sound/sfx/thunder/thunder_2.mp3"
    $ sfx_thunder_3 = "sound/sfx/thunder/thunder_3.mp3"
    $ sfx_thunder_4 = "sound/sfx/thunder/thunder_4.mp3"

    $ sound_rain = "sound/ambiences/rain/camp_rain.mp3"

    python:
        def play_sfx_thunder_1(trans, st, at):
            renpy.play(sfx_thunder_1, channel="sound")

        def play_sfx_thunder_2(trans, st, at):
            renpy.play(sfx_thunder_2, channel="sound")

        def play_sfx_thunder_3(trans, st, at):
            renpy.play(sfx_thunder_3, channel="sound")

        def play_sfx_thunder_4(trans, st, at):
            renpy.play(sfx_thunder_4, channel="sound")

        # once = False                  НЕ ТРОГАТЬ. УБЬЁТ!
        # def play_ambience_rain():
        #     global once
        #     if not once:
        #         renpy.music.play(sound_rain, channel = "ambience", loop=True)
        #         once = True
        #     else:
        #         NullAction()
                

    ##      Дисклеймер      ##
    define custom_disclaimer = "images/custom_gui/custom_disclaimer.png"

    ##      Бэкграунд       ##
    image custom_background_none:
        contains:
            'bg ext_camp_entrance_dark_1'
            pause 1
            choice:
                pause 5
                'bg ext_camp_entrance_dark_1' with flash
                function play_sfx_thunder_1
                pause 1
            choice:
                pause 10
                'bg ext_camp_entrance_dark_1' with flash
                function play_sfx_thunder_2
                pause 1
            choice:
                pause 15
                'bg ext_camp_entrance_dark_1' with flash
                function play_sfx_thunder_3
                pause 1
            choice:
                pause 20
                'bg ext_camp_entrance_dark_1' with flash
                function play_sfx_thunder_4
                pause 1
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


