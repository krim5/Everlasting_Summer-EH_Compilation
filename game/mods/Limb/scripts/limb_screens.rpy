init 5:
    image main_menu_map_atl:
        limb_gui_pref + 'main_menu/map_1.jpg'
        pause 5
        limb_gui_pref + 'main_menu/map_2.jpg' with Dissolve(5)
        pause 5
        limb_gui_pref + 'main_menu/map_3.jpg' with Dissolve(5)
        pause 5
        block:
            limb_gui_pref + 'main_menu/map_1.jpg' with Dissolve(5)
            pause 5
            limb_gui_pref + 'main_menu/map_2.jpg' with Dissolve(5)
            pause 5
            limb_gui_pref + 'main_menu/map_3.jpg' with Dissolve(5)
            pause 5
            repeat

    image anim limb_quit:
        limb_gui_pref + 'limb_door_exit_1.jpg' with Dissolve(5)
        pause 5
        limb_gui_pref + 'limb_door_exit_2.jpg' with Dissolve(5)
        pause 5
        repeat

    transform limb_readhim_transf:
        ypos 0
        20.0
        linear 40.0 ypos -920

    transform limb_horror_zoom:
        anchor (0.5, 0.5)
        align (0.5, 0.05)
        zoom 0.9
        ease 1.0 zoom 1
        ease 1.0 zoom 0.9
        repeat

    transform limb_horror_shake:
        xanchor (0.5, 0.5)
        pos (0.5, 0.5)
        ease 0.02 pos (0.5, 0.499)
        ease 0.04 pos (0.5, 0.501)
        ease 0.02 pos (0.5, 0.5)
        repeat

    $ style.limb_gms_time_alpha = Style(style.default)
    $ style.limb_gms_time_alpha.color = "#000000"
    $ style.limb_gms_time_alpha.italic = False
    $ style.limb_gms_time_alpha.bold = False
    $ style.limb_gms_time_alpha.font = "mods/Limb/resourses/images/gui/fonts/var_4.otf"
    $ style.limb_gms_time_alpha.outlines = [ (1, "#345EBC", 0, 0) ]#FF1493

    $ style.limb_gms_time_day = Style(style.default)
    $ style.limb_gms_time_day.color = "#000000"
    $ style.limb_gms_time_day.italic = False
    $ style.limb_gms_time_day.bold = False
    $ style.limb_gms_time_day.font = "mods/Limb/resourses/images/gui/fonts/var_4.otf"
    $ style.limb_gms_time_day.outlines = [ (1, "#345EBC", 0, 0) ]#FF1493

    $ style.limb_gms_time_sunset = Style(style.default)
    $ style.limb_gms_time_sunset.color = "#000000"
    $ style.limb_gms_time_sunset.italic = False
    $ style.limb_gms_time_sunset.bold = False
    $ style.limb_gms_time_sunset.font = "mods/Limb/resourses/images/gui/fonts/var_4.otf"
    $ style.limb_gms_time_sunset.outlines = [ (1, "#FF001C", 0, 0) ]#FF0000

    $ style.limb_gms_time_night = Style(style.default)
    $ style.limb_gms_time_night.color = "#000000"
    $ style.limb_gms_time_night.italic = False
    $ style.limb_gms_time_night.bold = False
    $ style.limb_gms_time_night.font = "mods/Limb/resourses/images/gui/fonts/var_4.otf"
    $ style.limb_gms_time_night.outlines = [ (1, "#6100E7", 0, 0) ]#9400D3

    $ style.limb_gms_time_prologue = Style(style.default)
    $ style.limb_gms_time_prologue.color = "#000000"
    $ style.limb_gms_time_prologue.italic = False
    $ style.limb_gms_time_prologue.bold = False
    $ style.limb_gms_time_prologue.font = "mods/Limb/resourses/images/gui/fonts/var_4.otf"
    $ style.limb_gms_time_prologue.outlines = [ (1, "#734116", 0, 0) ]#D2691E

    $ style.limb_gms_time_secret = Style(style.default)
    $ style.limb_gms_time_secret.color = "#000000"
    $ style.limb_gms_time_secret.italic = False
    $ style.limb_gms_time_secret.bold = False
    $ style.limb_gms_time_secret.font = "mods/Limb/resourses/images/gui/fonts/var_4.otf"
    $ style.limb_gms_time_secret.outlines = [ (1, "#3EC1B4", 0, 0) ]#7FFFD4

    $ style.limb_gms_time_prolog = Style(style.default)
    $ style.limb_gms_time_prolog.color = "#000000"
    $ style.limb_gms_time_prolog.italic = False
    $ style.limb_gms_time_prolog.bold = False
    $ style.limb_gms_time_prolog.font = "mods/Limb/resourses/images/gui/fonts/var_4.otf"
    $ style.limb_gms_time_prolog.outlines = [ (1, "#734116", 0, 0) ]#D2691E

    $ style.limb_save_load_button = Style(style.button)
    $ style.limb_save_load_button.background = limb_gui_pref + "/save_load/thumbnail_idle.png"
    $ style.limb_save_load_button.hover_background = limb_gui_pref + "/save_load/thumbnail_hover.png"
    $ style.limb_save_load_button.selected_background = limb_gui_pref + "/save_load/thumbnail_selected.png"
    $ style.limb_save_load_button.selected_hover_background = limb_gui_pref + "/save_load/thumbnail_selected.png"
    $ style.limb_save_load_button.selected_idle_background = limb_gui_pref + "/save_load/thumbnail_selected.png"


screen limb_horror_sb_1:
    modal False
    imagebutton:
        auto 'mods/Limb/resourses/images/gui/hor/limb_safe_brick_1_%s.png'
        anchor (0.5, 0.5)
        pos (960, 540)
        focus_mask True
        action Hide('limb_horror_sb_1', Dissolve(2, alpha=True))

screen limb_horror_sb_2:
    modal False
    imagebutton:
        auto 'mods/Limb/resourses/images/gui/hor/limb_safe_brick_2_%s.png'
        anchor (0.5, 0.5)
        pos (960, 540)
        focus_mask True
        action Hide('limb_horror_sb_2', Dissolve(2, alpha=True))

screen limb_horror_sb_3:
    modal False
    imagebutton:
        auto 'mods/Limb/resourses/images/gui/hor/limb_safe_brick_3_%s.png'
        anchor (0.5, 0.5)
        pos (960, 540)
        focus_mask True
        action Hide('limb_horror_sb_3', Dissolve(2, alpha=True))

screen limb_horror_sb_4:
    modal False
    imagebutton:
        auto 'mods/Limb/resourses/images/gui/hor/limb_safe_brick_4_%s.png'
        anchor (0.5, 0.5)
        pos (960, 540)
        focus_mask True
        action Hide('limb_horror_sb_4', Dissolve(2, alpha=True))

screen limb_horror_sb_5:
    modal False
    imagebutton:
        auto 'mods/Limb/resourses/images/gui/hor/limb_safe_brick_5_%s.png'
        anchor (0.5, 0.5)
        pos (960, 540)
        focus_mask True
        action Hide('limb_horror_sb_5', Dissolve(2, alpha=True))

screen limb_main_menu:
    tag menu
    modal True

    $ change_cursor("limb_mouse")
    #
    # key "game_menu":
    #         action NullAction()
    #
    # key "screenshot":
    #    action NullAction()

    if persistent.limb_story_end == True:
        add 'limb_menu_background_end'
    else:
        add 'limb_menu_background'

    add limb_gui_pref + 'main_menu/menu_ground.png'

    if persistent.limb_story_end == True:
        add limb_gui_pref + 'main_menu/menu_filter_end.png'

    # imagebutton:
    #     auto limb_gui_pref + "main_menu/    .png"
    #     xpos
    #     ypos
    #     if persistent.limb_menu_sound == False:
    #         action SetVariable('persistent.limb_menu_sound', 'True')
    #     else:
    #         hovered Play('sound', 'mods/Limb/resourses/sound/sfx/sfx_limb_menu_1.mp3')
    #         action SetVariable('persistent.limb_menu_sound', 'False')

    imagebutton:
        auto limb_gui_pref + "main_menu/steam_%s.png"
        xpos 610
        ypos 11
        # if persistent.limb_menu_sound == True:
        hovered Play('sound', 'mods/Limb/resourses/sound/sfx/sfx_limb_menu_3.mp3')
        action OpenURL('steam://url/CommunityFilePage/1374637382')#1126116478')

    imagebutton:
        auto limb_gui_pref + "main_menu/vk_%s.png"
        xpos 465
        ypos 10
        # if persistent.limb_menu_sound == True:
        hovered Play('sound', 'mods/Limb/resourses/sound/sfx/sfx_limb_menu_3.mp3')
        action OpenURL('https://vk.com/bloner')

    imagebutton:
        auto limb_gui_pref + "main_menu/start_%s.png"
        xpos 865
        ypos 503
        # if persistent.limb_menu_sound == True:
        hovered Play('sound', 'mods/Limb/resourses/sound/sfx/sfx_limb_menu_1.mp3')
        action [Stop("music"), Start('limb_prolog')]

    if persistent.origin_end == True or persistent.all_be_good_end == True or persistent.un_dead_end == True or persistent.near_happiness_end == True or persistent.other_story_end == True or persistent.eternal_shining_end == True or persistent.coma_effect_end == True or persistent.blue_lagoon_end == True or persistent.fine_mars_end == True:
        imagebutton:
            auto limb_gui_pref + "main_menu/map_%s.png"
            xpos 1112
            ypos 685
            # if persistent.limb_menu_sound == True:
            hovered Play('sound', 'mods/Limb/resourses/sound/sfx/sfx_limb_menu_1.mp3')
            action ShowMenu('limb_map_atl')

    imagebutton:
        auto limb_gui_pref + "main_menu/quit_%s.png"
        xpos 0
        ypos 950
        focus_mask True
        # if persistent.limb_menu_sound == True:
        hovered Play('sound', 'mods/Limb/resourses/sound/sfx/sfx_limb_menu_2.mp3')
        action [Function(limb_screens_load), Start('lumb_main_menu_or_label')]#MainMenu(confirm = False)]

    if persistent.origin_end == True and persistent.all_be_good_end == True and persistent.un_dead_end == True and persistent.near_happiness_end == True and persistent.other_story_end == True and persistent.eternal_shining_end == True:
        imagebutton:
            auto limb_gui_pref + "main_menu/safe_%s.png"
            xpos 573
            ypos 408
            focus_mask True
            action Play('sound', sfx_limb_ahahaha),Hide('limb_main_menu', limb_razlom), Start('limb_safe')#ShowMenu('limb_safe')

    if persistent.origin_end:
        add limb_gui_pref + "main_menu/point.png":
            pos(385,40)
        imagebutton:
                idle limb_gui_pref + 'achievements/acm_pl_origin_amanda.png'
                hover limb_gui_pref + 'achievements/acm_pl_origin.png'
                pos (0,10)
                # if persistent.limb_menu_sound == True:
                hovered Play('sound', 'mods/Limb/resourses/sound/sfx/sfx_limb_menu_1.mp3')
                action SetVariable('limb_ach_show', 'origin'), ShowMenu('limb_show_ach_scr')

    if persistent.all_be_good_end:
        add limb_gui_pref + "main_menu/point.png":
            pos(385,143)
        imagebutton:
                idle limb_gui_pref + 'achievements/acm_pl_all_be_good_amanda.png'
                hover limb_gui_pref + 'achievements/acm_pl_all_be_good.png'
                pos (0,112)
                # if persistent.limb_menu_sound == True:
                hovered Play('sound', 'mods/Limb/resourses/sound/sfx/sfx_limb_menu_1.mp3')
                action SetVariable('limb_ach_show', 'all_be_good'), ShowMenu('limb_show_ach_scr')

    if persistent.coma_effect_end:
        imagebutton:
                idle limb_gui_pref + 'achievements/acm_pl_coma_effect_amanda.png'
                hover limb_gui_pref + 'achievements/acm_pl_coma_effect.png'
                pos (0,215)
                # if persistent.limb_menu_sound == True:
                hovered Play('sound', 'mods/Limb/resourses/sound/sfx/sfx_limb_menu_1.mp3')
                action SetVariable('limb_ach_show', 'coma_effect'), ShowMenu('limb_show_ach_scr')

    if persistent.un_dead_end:
        add limb_gui_pref + "main_menu/point.png":
            pos(385,348)
        imagebutton:
                idle limb_gui_pref + 'achievements/acm_pl_un_dead_amanda.png'
                hover limb_gui_pref + 'achievements/acm_pl_un_dead.png'
                pos (0,315)
                # if persistent.limb_menu_sound == True:
                hovered Play('sound', 'mods/Limb/resourses/sound/sfx/sfx_limb_menu_1.mp3')
                action SetVariable('limb_ach_show', 'un_dead'), ShowMenu('limb_show_ach_scr')

    if persistent.blue_lagoon_end:
        imagebutton:
            idle limb_gui_pref + 'achievements/acm_pl_blue_lagoon_amanda.png'
            hover limb_gui_pref + 'achievements/acm_pl_blue_lagoon.png'
            pos (0,420)
            # if persistent.limb_menu_sound == True:
            hovered Play('sound', 'mods/Limb/resourses/sound/sfx/sfx_limb_menu_1.mp3')
            action SetVariable('limb_ach_show', 'blue_lagoon'), ShowMenu('limb_show_ach_scr')

    if persistent.fine_mars_end:
        imagebutton:
            idle limb_gui_pref + 'achievements/acm_pl_fine_mars_amanda.png'
            hover limb_gui_pref + 'achievements/acm_pl_fine_mars.png'
            pos (0,525)
            # if persistent.limb_menu_sound == True:
            hovered Play('sound', 'mods/Limb/resourses/sound/sfx/sfx_limb_menu_1.mp3')
            action SetVariable('limb_ach_show', 'fine_mars'), ShowMenu('limb_show_ach_scr')

    if persistent.near_happiness_end:
        add limb_gui_pref + "main_menu/point.png":
            pos(385,663)
        imagebutton:
                idle limb_gui_pref + 'achievements/acm_pl_near_happiness_amanda.png'
                hover limb_gui_pref + 'achievements/acm_pl_near_happiness.png'
                pos (0,630)
                # if persistent.limb_menu_sound == True:
                hovered Play('sound', 'mods/Limb/resourses/sound/sfx/sfx_limb_menu_1.mp3')
                action SetVariable('limb_ach_show', 'near_happiness'), ShowMenu('limb_show_ach_scr')

    if persistent.other_story_end:
        add limb_gui_pref + "main_menu/point.png":
            pos(385,767)
        imagebutton:
                idle limb_gui_pref + 'achievements/acm_pl_other_story_amanda.png'
                hover limb_gui_pref + 'achievements/acm_pl_other_story.png'
                pos (0,735)
                # if persistent.limb_menu_sound == True:
                hovered Play('sound', 'mods/Limb/resourses/sound/sfx/sfx_limb_menu_1.mp3')
                action SetVariable('limb_ach_show', 'other_story'), ShowMenu('limb_show_ach_scr')

    if persistent.eternal_shining_end:
        add limb_gui_pref + "main_menu/point.png":
            pos(385,870)
        imagebutton:
                idle limb_gui_pref + 'achievements/acm_pl_eternal_shining_amanda.png'
                hover limb_gui_pref + 'achievements/acm_pl_eternal_shining.png'
                pos (0,840)
                # if persistent.limb_menu_sound == True:
                hovered Play('sound', 'mods/Limb/resourses/sound/sfx/sfx_limb_menu_1.mp3')
                action SetVariable('limb_ach_show', 'eternal_shining'), ShowMenu('limb_show_ach_scr')

    if persistent.origin_end == True or persistent.all_be_good_end == True or persistent.un_dead_end == True or persistent.near_happiness_end == True or persistent.other_story_end == True or persistent.eternal_shining_end == True:
        window:
            background None
            window:
                maximum (464, 1800)
                anchor (0, 0)
                pos (1450, -6)
                background None
                hbox:
                    viewport id "limb_player":
                        yinitial 9999
                        mousewheel True
                        draggable True
                        vbox:
                            for x in limb_track_list.items():
                                textbutton x[0]:
                                    minimum (int(464), int(80))
                                    background "limb_music_button_idle"
                                    hover_background "limb_music_button_hover"
                                    selected_background "limb_music_button_hover"
                                    text_font limb_font_4
                                    text_color "#828282"
                                    text_hover_color "#ADFFFF"
                                    text_selected_color "#33FFFF"
                                    text_selected_idle_color "#33FFFF"
                                    text_selected_hover_color "#E0FFFF"
                                    text_insensitive_color "#33FFFF"
                                    text_outlines [(2,"#000",0,0)]
                                    text_size 30
                                    # if persistent.limb_menu_sound == True:
                                    hovered Play('sound', 'mods/Limb/resourses/sound/sfx/sfx_limb_menu_4.mp3')
                                    action [Stop("music", fadeout=1.5), Play("music", x[1], loop=True)]
                            imagebutton:
                                minimum (int(464), int(80))
                                idle "limb_music_button_idle_stop"
                                hover "limb_music_button_hover_stop"
                                # if persistent.limb_menu_sound == True:
                                hovered Play('sound', 'mods/Limb/resourses/sound/sfx/sfx_limb_menu_2.mp3')
                                action [Stop("music", fadeout=1.0)]
                    vbar:
                        yfill True
                        thumb limb_gui_pref + 'player/thumb.png'
                        value YScrollValue("limb_player")
    else:
        add limb_gui_pref + 'main_menu/menu_filter_start.png'

screen limb_save:

    tag menu
    modal True

    window background limb_gui_pref + "/save_load/limb_save_bg.png":

        textbutton "Загрузить" text_font gabriola style "log_button" text_style "settings_link" xalign 0.98 yalign 0.08 action ShowMenu('limb_load')
        textbutton "Настройки" text_font gabriola style "log_button" text_style "settings_link" xalign 0.02 yalign 0.08 action ShowMenu('limb_preferences')
        hbox xalign 0.5 yalign 0.08:
            add limb_gui_pref + "main_menu/point.png" 
            text " "+"СОХРАНИТЬ"+" " font gabriola style "settings_link" yalign 0.5 color "#ffffff"
            add limb_gui_pref + "main_menu/point.png" 
        
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
                        style "limb_save_load_button"
                        has fixed
                        text ( "%s." % i
                               + FileTime(i, format=' %d.%m.%y, %H:%M', empty=" Пустой слот")
                               + "\n" +FileSaveName(i)) style "file_picker_text" xpos 15 ypos 15

screen limb_load:

    tag menu
    modal True

    window background limb_gui_pref + "save_load/limb_load_bg.png":

        textbutton "Сохранить" text_font gabriola style "log_button" text_style "settings_link" xalign 0.98 yalign 0.08 action ShowMenu('limb_save')
        textbutton "Настройки" text_font gabriola style "log_button" text_style "settings_link" xalign 0.02 yalign 0.08 action ShowMenu('limb_preferences') 

        hbox xalign 0.5 yalign 0.08:
            add limb_gui_pref + "main_menu/point.png" 
            text " "+"ЗАГРУЗИТЬ"+" " font gabriola style "settings_link" yalign 0.5 color "#ffffff"
            add limb_gui_pref + "main_menu/point.png" 

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
                        style "limb_save_load_button"
                        has fixed
                        text ( "%s." % i
                                + FileTime(i, format=' %d.%m.%y, %H:%M', empty=" Пустой слот")
                                + "\n" +FileSaveName(i)) style "file_picker_text" xpos 15 ypos 15

screen limb_preferences:

    tag menu
    modal True

    $ bar_null = Frame(limb_gui_pref + "preferences/bar_null.png",36,36)
    $ bar_full = Frame(limb_gui_pref + "preferences/bar_full.png",36,36)

    window background limb_gui_pref + "preferences/limb_preferences_bg02.png":

        textbutton "Сохранить" text_font gabriola style "log_button" text_style "settings_link" xalign 0.02 yalign 0.08 action ShowMenu('limb_save')
        textbutton "Загрузить" text_font gabriola style "log_button" text_style "settings_link" xalign 0.98 yalign 0.08 action ShowMenu('limb_load')
        hbox xalign 0.5 yalign 0.08:
            add limb_gui_pref + "main_menu/point.png" 
            text " "+"НАСТРОЙКИ"+" " font gabriola style "settings_link" yalign 0.5 color "#ffffff"
            add limb_gui_pref + "main_menu/point.png" 
        
        textbutton "Назад" text_font gabriola style "log_button" text_style "settings_link" xalign 0.015 yalign 0.92 action Return()

        side "c b r":
            area (0.25, 0.23, 0.51, 0.71)
            viewport id "limb_preferences":
                mousewheel True
                scrollbars None

                has grid 1 17 xfill True spacing 15
                text translation_new["Window_mode"] style "settings_header" xalign 0.5
                grid 2 1 xfill True:

                    hbox xalign 0.5:
                        if _preferences.fullscreen:
                            add limb_gui_pref + "preferences/hthumb.png" ypos 0.12
                        else:
                            null width 22
                        textbutton translation_new["Fullscreen"] style "log_button" text_style "settings_text" action Preference("display", "fullscreen")

                    hbox xalign 0.5:
                        if not _preferences.fullscreen:
                            add limb_gui_pref + "preferences/hthumb.png" ypos 0.12
                        else:
                            null width 22
                        textbutton translation_new["Window"] style "log_button" text_style "settings_text" action Preference("display", "window")



                text translation_new["Skip"] style "settings_header" xalign 0.5
                grid 2 1 xfill True:

                    hbox xalign 0.5:
                        if _preferences.skip_unseen:
                            add limb_gui_pref + "preferences/hthumb.png" ypos 0.12
                        else:
                            null width 22
                        textbutton translation_new["Skip_all"] style "log_button" text_style "settings_text" action Preference("skip", "all")

                    hbox xalign 0.5:
                        if not _preferences.skip_unseen:
                            add limb_gui_pref + "preferences/hthumb.png" ypos 0.12
                        else:
                            null width 22
                        textbutton translation_new["Skip_seen"] style "log_button" text_style "settings_text" action Preference("skip", "seen")


                text translation_new["Volume"] style "settings_header" xalign 0.5

                grid 2 1 xfill True:
                    textbutton translation_new["Music_lower"] style "log_button" text_style "settings_text" xpos 0.1
                    bar value Preference("music volume") left_bar bar_full right_bar bar_null thumb limb_gui_pref + "preferences/vthumb.jpg" hover_thumb limb_gui_pref + "preferences/vthumb.jpg" xmaximum 1.35 ymaximum 36 xpos -0.55

                grid 2 1 xfill True:
                    textbutton translation_new["Sound"] style "log_button" text_style "settings_text" xpos 0.1
                    bar value Preference("sound volume") left_bar bar_full right_bar bar_null thumb limb_gui_pref + "preferences/vthumb.jpg" hover_thumb limb_gui_pref + "preferences/vthumb.jpg" xmaximum 1.35 ymaximum 36 xpos -0.55

                grid 2 1 xfill True:
                    textbutton translation_new["Ambience"] style "log_button" text_style "settings_text" xpos 0.1
                    bar value Preference("voice volume") left_bar bar_full right_bar bar_null thumb limb_gui_pref + "preferences/vthumb.jpg" hover_thumb limb_gui_pref + "preferences/vthumb.jpg" xmaximum 1.35 ymaximum 36 xpos -0.55

                text translation_new["Text_speed"] style "settings_header" xalign 0.5
                bar value Preference("text speed") left_bar bar_full right_bar bar_null thumb limb_gui_pref + "preferences/vthumb.jpg" hover_thumb limb_gui_pref + "preferences/vthumb.jpg" xalign 0.5 xmaximum 0.8 ymaximum 36

                text translation_new["Autoforward"] style "settings_header" xalign 0.5
                grid 2 1 xfill True:

                    hbox xalign 0.5:
                        if _preferences.afm_time != 0:
                            add limb_gui_pref + "preferences/hthumb.png" ypos 0.12
                        else:
                            null width 22
                        textbutton translation_new["Adult_content_on"] style "log_button" text_style "settings_text" action Preference("auto-forward after click", "enable")

                    hbox xalign 0.5:
                        if _preferences.afm_time == 0:
                            add limb_gui_pref + "preferences/hthumb.png" ypos 0.12
                        else:
                            null width 22
                        textbutton translation_new["Adult_content_off"] style "log_button" text_style "settings_text" action (Preference("auto-forward time", 0), Preference("auto-forward after click", "disable"))

                text translation_new["Autoforward_time"] style "settings_header" xalign 0.5
                bar value Preference("auto-forward time") left_bar bar_full right_bar bar_null thumb limb_gui_pref + "preferences/vthumb.jpg" hover_thumb limb_gui_pref + "preferences/vthumb.jpg" xalign 0.5 xmaximum 0.8 ymaximum 36


                text translation_new["Font"] style "settings_header" xalign 0.5
                grid 2 1 xfill True:
                    hbox xalign 0.5:
                        if persistent.font_size == "small":
                            add limb_gui_pref + "preferences/hthumb.png" ypos 0.12
                        else:
                            null width 22
                        textbutton translation_new["Normal_font"] style "log_button" text_style "settings_text" action SetField(persistent, "font_size", "small")

                    hbox xalign 0.5:
                        if not persistent.font_size == "small":
                            add limb_gui_pref + "preferences/hthumb.png" ypos 0.12
                        else:
                            null width 22
                        textbutton translation_new["Big_font"] style "log_button" text_style "settings_text" action SetField(persistent, "font_size", "large")



                
                null

            bar value XScrollValue("limb_preferences") left_bar "images/misc/none.png" right_bar "images/misc/none.png" thumb "images/misc/none.png" hover_thumb "images/misc/none.png"
            vbar value YScrollValue("limb_preferences") bottom_bar limb_gui_pref + "preferences/vbar.jpg" top_bar limb_gui_pref + "preferences/vbar.jpg" thumb limb_gui_pref + "preferences/thumb.png" ymaximum 750


screen limb_safe:
    add "mods/Limb/resourses/images/cg/limb_safe_0.jpg"
    text '[limb_safe_pass]':
        style "limb_safe_style"
        color '%s'%limb_access_color
        size 45
        pos(920, 450)

    # textbutton '[limb_safe_access]':
    #     style "limb_safe_style"
    #     align (0.0, 1.0)
    #     hovered Play('sound', 'mods/Limb/resourses/sound/sfx/sfx_limb_menu_1.mp3')
    #     action Function(limb_check_safe)

    imagebutton:
        auto 'mods/Limb/resourses/images/gui/safe/exit_%s.png'
        pos (186,50)
        hovered Play('sound', 'mods/Limb/resourses/sound/sfx/sfx_limb_menu_2.mp3')
        action [Hide('limb_safe', limb_pixel_safe), Jump('limb_menu')]

    grid 4 3:
        area (865, 533, 223,143)
        for i in ('1','2','3','4','5','6','7','8','C','9','0','->'):
            if i == 'C':
                textbutton i:
                    background 'mods/Limb/resourses/images/gui/safe/safe_ground_btn.png'
                    hover_background 'mods/Limb/resourses/images/gui/safe/safe_ground_btn.png'
                    selected_background None
                    text_style "limb_safe_style"
                    action SetVariable('limb_access_color','#00FF00'), Function(limb_nool_safe_var)

            elif i == '->':
                button:
                    background 'mods/Limb/resourses/images/gui/safe/safe_ground_btn.png'
                    hover_background 'mods/Limb/resourses/images/gui/safe/safe_ground_btn.png'
                    selected_background None
                    text '->':
                        style "limb_safe_style"
                    action Function(limb_check_safe)
            else:
                textbutton i:
                    background 'mods/Limb/resourses/images/gui/safe/safe_ground_btn.png'
                    hover_background 'mods/Limb/resourses/images/gui/safe/safe_ground_btn.png'
                    selected_background None
                    text_style "limb_safe_style"
                    action Function(limb_safe_pass_add, i)

screen limb_show_ach_scr:
    add 'limb_menu_background'
    add "limb_" + limb_ach_show:
        align(.5,.5)
    button:
        style "blank_button"
        xpos 0
        ypos 0
        xfill True
        yfill True
        action Hide('limb_show_ach_scr')

screen limb_map_atl:
    tag menu
    modal True
    add 'main_menu_map_atl'

    button:
        style "blank_button"
        xpos 0
        ypos 0
        xfill True
        yfill True
        action Hide('limb_sl_map_show'),Return()
    if persistent.origin_end == True and persistent.all_be_good_end == True and persistent.un_dead_end == True and persistent.near_happiness_end == True and persistent.other_story_end == True and persistent.eternal_shining_end == True:
        imagebutton:
            auto 'mods/Limb/resourses/images/gui/main_menu/readhim_%s.png'
            align(.1,.75)
            hovered Play('sound', 'mods/Limb/resourses/sound/sfx/sfx_limb_menu_3.mp3')
            action Hide('limb_sl_map_show'), Play("music","mods/Limb/resourses/sound/music/pl_gk_blue_note_sessions.mp3"), ShowMenu('limb_readhim')

    key 'f' action ShowMenu('limb_sl_map_show')
    key 'F' action ShowMenu('limb_sl_map_show')
    key 'а' action ShowMenu('limb_sl_map_show')
    key 'А' action ShowMenu('limb_sl_map_show')

screen limb_sl_map_show:
    modal False
    add 'mods/Limb/resourses/images/gui/main_menu/sl_butt.png':
        align(.4,.53)
    timer 3.0 action Hide('limb_sl_map_show')

screen limb_readhim:
    tag menu
    modal True
    add 'mods/Limb/resourses/images/gui/main_menu/limb_you.jpg' at limb_readhim_transf

    button:
        style "blank_button"
        xpos 0
        ypos 0
        xfill True
        yfill True
        action Play('music', pl_ae_blow_with_the_fires_remix), Return()

screen limb_game_menu_selector:
    tag menu
    modal True

    $ timeofday = persistent.timeofday

    button:
        style "blank_button"
        xpos 0
        ypos 0
        xfill True
        yfill True
        action Return()

    add limb_gui_pref + "ingame_menu/"+timeofday+"/ingame_menu.png":
        xalign 0.5
        yalign 0.5

    imagemap:
        auto limb_gui_pref + "ingame_menu/"+timeofday+"/ingame_menu_%s.png"
        xalign 0.5
        yalign 0.5

        hotspot (0, 83, 660, 65):
            focus_mask None
            clicked [Stop("music", fadeout=2.0),ShowMenu('limb_main_menu')] #MainMenu(confirm = False)] #MainMenu()
        hotspot (0, 148, 660, 65):
            focus_mask None
            clicked ShowMenu('save')
        hotspot (0, 213, 660, 65):
            focus_mask None
            clicked ShowMenu('load')
        hotspot (0, 278, 660, 65):
            focus_mask None
            clicked (ShowMenu('preferences'), Hide('game_menu_selector'))
        hotspot (0, 343, 660, 65):
            focus_mask None
            clicked ShowMenu('quit')

    python:
        ui.fixed()

        ui.button(clicked=None, xalign=0.49, ypos=950, style="limb_gms_time_%s"%timeofday)
        ui.text ("%s" % (save_name), style="limb_gms_time_%s"%timeofday, size=35)
        ui.button(clicked=None, xalign=0.49, ypos=1030, style="limb_gms_time_%s"%timeofday)
        ui.text ("%s: %s" % ("Прошло времени", limb_time_from_seconds(renpy.get_game_runtime())), style="limb_gms_time_%s"%timeofday, size=35)

        ui.close()
    vbox:
        ypos 100
        xalign .5
        if renpy.music.get_playing(channel='music'):
            if renpy.music.get_playing(channel='music') in music_list.values():
                text 'Ты почти выбрался!':
                    style "limb_gms_time_%s"%timeofday

            else:
                text [renpy.music.get_playing(channel='music')[len('mods/Limb/resourses/sound/music/'):-4].replace("pl_", "").replace("ae_", "Aendo - ").replace("dn_", "Dunkle Nil - ").replace("ef_", "EconomicFour - ").replace("gk_", "Gek Kosni - ").replace("uc_", "Unfamiliar Ceiling - ").replace("st_", "SanTechnik - ").replace("_", " ").title()]:
                    xalign .5
                    ypos -25
                    style "limb_gms_time_%s"%timeofday
                    size 45

            bar value AudioPositionValue('music', .01):
                    xmaximum 900
                    left_bar Frame("mods/Limb/resourses/images/gui/player/bar_full.png", 0, 0)
                    right_bar Frame("mods/Limb/resourses/images/gui/player/bar_null.png", 0, 0)
                    thumb "mods/Limb/resourses/images/gui/player/hthumb.png"
                    xalign 1.0

screen limb_text_history:
    tag menu
    # $ timeofday = persistent.timeofday
    # if not current_line and len(readback_buffer) == 0 and d2_cardgame_block_rollback:
    #     $ lines_to_show = []
    # elif not current_line and len(readback_buffer) == 0:
    #     $ lines_to_show = []
    # elif current_line and len(readback_buffer) == 0:
    #     $ lines_to_show = [current_line]
    # elif current_line and not ( current_line == readback_buffer[-1] or False
    #         if len(readback_buffer) == 1 else (current_line == readback_buffer[-2]) ):
    #     $ lines_to_show = readback_buffer
    # else:
    #     $ lines_to_show = readback_buffer
    # button:
    #     style "blank_button"
    #     xpos 0
    #     ypos 0
    #     xfill True
    #     yfill True
    #     action Return()
    # window:
    #     background Frame(limb_gui_pref + "choice/"+timeofday+"/choice_box.png", 50, 50)
    #     xmaximum 0.83
    #     xalign 0.01
    #     yalign 0.01
    #     left_padding 75
    #     right_padding 75
    #     bottom_padding 50
    #     top_padding 50
    #     style_group "readback"
    #     side "c t r":
    #         viewport:
    #             id "readback"
    #             draggable True
    #             mousewheel True
    #             scrollbars None
    #             yinitial 1.0
    #             vbox:
    #                 null:
    #                     height 10
    #                 python:
    #                     count=1
    #                     total=0
    #
    #                     mass = lines_to_show
    #                     for i in mass:
    #                         if i[1]:
    #                             if not i[2]:
    #                                 total+=1
    #                 for line in lines_to_show:
    #                     if line[0] and line[0] != " ":
    #                         if line[3] and line[3] != " ":
    #                             $ sayer = line[0]
    #                             text sayer:
    #                                 color line[3]
    #                                 style "log_button_text"
    #                                 font limb_font_1
    #                         else:
    #                             text line[0]
    #                     if line[1]:
    #                         if not line[2]:
    #                             python:
    #                                 cn=total-count
    #                                 count+=1
    #                             if persistent.font_size == "small":
    #                                 textbutton __(line[1]):
    #                                     text_size 28
    #                                     style "log_button"
    #                                     text_style "log_button_text"
    #                                     if persistent.timeofday == "prologue":
    #                                         text_color (241, 208, 118, 255)
    #                                     elif persistent.timeofday == "day":
    #                                         text_color (224, 255, 255, 255)
    #                                     elif persistent.timeofday == "sunset":
    #                                         text_color (255, 255, 255, 255)
    #                                     elif persistent.timeofday == "night":
    #                                         text_color (249, 255, 184, 255)
    #                                     elif persistent.timeofday == "secret":
    #                                         text_color (240, 248, 255, 255)
    #                                     action FunctionCallback(do_rollback,cn)
    #                             elif persistent.font_size == "large":
    #                                 textbutton __(line[1]):
    #                                     text_size 35
    #                                     style "log_button"
    #                                     text_style "log_button_text"
    #                                     if persistent.timeofday == "prologue":
    #                                         text_color (241, 208, 118, 255)
    #                                     elif persistent.timeofday == "day":
    #                                         text_color (224, 255, 255, 255)
    #                                     elif persistent.timeofday == "sunset":
    #                                         text_color (255, 255, 255, 255)
    #                                     elif persistent.timeofday == "night":
    #                                         text_color (249, 255, 184, 255)
    #                                     elif persistent.timeofday == "secret":
    #                                         text_color (240, 248, 255, 255)
    #                                     action FunctionCallback(do_rollback,cn)
    #                             else:
    #                                 null:
    #                                     height 1
    #                         else:
    #                             textbutton line[1]:
    #                                 action Play("voice", line[2] )
    #                     null:
    #                         height 10
    #                 python:
    #                     count=None
    #                     total=None
    #                     mass=None
    #     $ vbar_null = Frame(limb_gui_pref + "player/vbar_null.jpg",0,0)
    #     bar:
    #         value XScrollValue("readback")
    #         left_bar "images/misc/none.png"
    #         right_bar "images/misc/none.png"
    #         thumb "images/misc/none.png"
    #         hover_thumb "images/misc/none.png"
    #     vbar:
    #         value YScrollValue("readback")
    #         bottom_bar vbar_null
    #         top_bar vbar_null
    #         thumb limb_gui_pref + "player/thumb.png"
    #         #thumb_offset -12
    #         xalign 1.0
    predict False

    $ timeofday = persistent.timeofday
    $ xmax = 1600
    $ xposition = 100



    if persistent.font_size == "large":
        $ history_text_size = 28
        $ history_name_size = 29

    else:
        $ history_text_size = 21
        $ history_name_size = 22


    button style "blank_button" xpos 0 ypos 0 xfill True yfill True action Return()

    window background Frame(limb_gui_pref + "choice/"+timeofday+"/choice_box.png") left_padding 75 right_padding 75 bottom_padding 120 top_padding 120:


        viewport id "limb_text_history_screen":
            draggable True
            mousewheel True
            scrollbars None
            yinitial 1.0

            has vbox

            for h in _history_list:

                if h.who:

                    text h.who:
                        font main_font
                        ypos 0
                        xpos xposition
                        xalign 0.0
                        size history_name_size
                        if "color" in h.who_args:
                            color h.who_args["color"]

                textbutton h.what:
                    style "log_button"
                    text_style "normal_day"
                    text_size history_text_size
                    action RollbackToIdentifier(h.rollback_identifier)
                    xmaximum xmax
                    xpos 100
                    if persistent.timeofday == "prologue":
                        text_color (241, 208, 118, 255)
                        text_hover_color "#ff4500"
                    elif persistent.timeofday == "day":
                        text_color (224, 255, 255, 255)
                        text_hover_color "#1e90ff"
                    elif persistent.timeofday == "sunset":
                        text_color (255, 255, 255, 255)
                        text_hover_color "#ff0000"
                    elif persistent.timeofday == "night":
                        text_color (249, 255, 184, 255)
                        text_hover_color "#8a2be2"
                    elif persistent.timeofday == "secret":
                        text_color (240, 248, 255, 255)
                        text_hover_color "#00ffff"
        $ vbar_null = Frame(limb_gui_pref + "player/vbar_null.jpg",0,0)

        vbar:
            value YScrollValue("limb_text_history_screen")
            bottom_bar vbar_null
            top_bar vbar_null
            thumb limb_gui_pref + "player/thumb.png"
            #thumb_offset -12
            xalign 1.0
        # vbar:
        #     value YScrollValue("text_history_screen")
        #     bottom_bar "images/misc/none.png"
        #     top_bar "images/misc/none.png"
        #     thumb "images/gui/settings/vthumb.png"
        #     #xoffset 1700

screen limb_choice:
    modal True
    $ timeofday = persistent.timeofday
    python:
        limb_choice_colors_hover={
                'day': "#5EDBDB",
                'night': "#FFFF66",
                'secret': "#40E0D0",
                'sunset': "#FFBB29",
                'prologue': "#FAF0D4"
                        }

        limb_choice_colors={
                'day': "#E0FFFF",
                'night': "#F9FFB8",
                'secret': "#F0F8FF",
                'sunset': "#FFDB8B",
                'prologue': "#F1D076"
                        }

        limb_choice_colors_selected={
                'day': "#47FFFF",
                'night': "#CCCC00",
                'secret': "#ADFFFF",
                'sunset': "#FFECC2",
                'prologue': "#EBB31A",
                        }
    window:
        background Frame(limb_gui_pref + "choice/"+timeofday+"/choice_box.png", 50, 50)
        xfill True
        yalign 0.5
        left_padding 50
        right_padding 50
        bottom_padding 120
        top_padding 120
        vbox:
            xalign 0.5
            for caption, action, chosen  in items:
                if action and caption:
                    button:
                        background None
                        xalign 0.5
                        action action
                        text caption:
                            font header_font
                            size 37
                            hover_size 37
                            color limb_choice_colors[persistent.timeofday]
                            hover_color limb_choice_colors_hover[persistent.timeofday]
                            selected_color limb_choice_colors_selected[persistent.timeofday]
                            xcenter 0.5
                else:
                    button:
                        background None
                        xalign 0.5
                        action action
                        text caption:
                            font header_font
                            size 37
                            hover_size 37
                            color limb_choice_colors[persistent.timeofday]
                            hover_color limb_choice_colors_hover[persistent.timeofday]
                            selected_color limb_choice_colors_selected[persistent.timeofday]
                            xcenter 0.5

screen limb_yesno_prompt:
    modal True
    add limb_gui_pref + "o_rly/base.png"
    text _(message):
        text_align 0.5
        yalign 0.46
        xalign 0.5
        color "#000000"
        font header_font
        size 40
    textbutton translation["Yes"][_preferences.language]:
        text_size 60
        style "log_button"
        text_style "settings_link"
        text_idle_color "#ffffff"
        text_hover_color "#adadad"
        yalign 0.65
        xalign 0.3
        action yes_action
    textbutton translation["No"][_preferences.language]:
        text_size 60
        style "log_button"
        text_style "settings_link"
        text_idle_color "#ffffff"
        text_hover_color "#adadad"
        yalign 0.65
        xalign 0.7
        action no_action

screen limb_say:
    window:
        background None
        id "window"
        $ timeofday = persistent.timeofday


        if timeofday != 'alpha':
            imagebutton:
                auto limb_gui_pref + "dialogue_box/"+timeofday+"/backward_%s.png"
                xpos 19
                ypos 920
                action ShowMenu("limb_text_history")

        add limb_gui_pref + "dialogue_box/"+timeofday+"/dialogue_box.png":
            align(.5,1.0)

        if timeofday != 'alpha':
            if not config.skipping:
                imagebutton:
                    auto limb_gui_pref + "dialogue_box/"+timeofday+"/forward_%s.png"
                    xpos 1763
                    ypos 920
                    action Skip()

            else:
                imagebutton:
                    auto limb_gui_pref + "dialogue_box/"+timeofday+"/fast_forward_%s.png"
                    xpos 1763
                    ypos 920
                    action Skip()

        if persistent.font_size == "small":
            text what:
                if persistent.timeofday == "prologue":
                    color (241, 208, 118, 255)
                elif persistent.timeofday == "day":
                    color (224, 255, 255, 255)
                elif persistent.timeofday == "sunset":
                    color (255, 255, 255, 255)
                elif persistent.timeofday == "night":
                    color (249, 255, 184, 255)
                elif persistent.timeofday == "secret":
                    color (240, 248, 255, 255)
                elif persistent.timeofday == "alpha":
                    color (226, 199, 120, 255)

                id "what"
                if timeofday != 'alpha':
                    xpos 210
                    ypos 940
                    xmaximum 1510
                    size 32
                    line_spacing 1
                else:
                    xpos 194
                    ypos 964
                    xmaximum 1541
                    size 28
                    line_spacing 2

            if who:
                text who:
                    id "who"
                    if timeofday != 'alpha':
                        xpos 220
                        ypos 894
                        font limb_font_1
                        size 32
                        line_spacing 1
                    else:
                        xpos 194
                        ypos 931
                        size 28
                        line_spacing 2

        elif persistent.font_size == "large":
            text what:
                id "what"
                xpos 210
                ypos 938
                xmaximum 1510
                size 32
                line_spacing 1

            if who:
                text who:
                    id "who"
                    xpos 220
                    ypos 896
                    size 32
                    line_spacing 1

screen limb_nvl:
    $ timeofday = persistent.timeofday
    window:
        background im.Scale(limb_gui_pref + "choice/"+timeofday+"/choice_box.png", 1920, 1080)
        xfill True
        yfill True
        yalign 0.5
        left_padding 175
        right_padding 175
        bottom_padding 150
        top_padding 150
        vbox:
            for who, what, who_id, what_id, window_id  in dialogue:
                window:
                    id window_id
                    hbox:
                        spacing 10
                        if persistent.font_size == "large":
                            if who is not None:
                                text who:
                                    id who_id
                                    font limb_font_1
                                    size 35
                                    line_spacing 1
                            text what:
                                id what_id
                                if persistent.timeofday == "prologue":
                                    color (241, 208, 118, 255)
                                elif persistent.timeofday == "day":
                                    color (224, 255, 255, 255)
                                elif persistent.timeofday == "sunset":
                                    color (255, 255, 255, 255)
                                elif persistent.timeofday == "night":
                                    color (249, 255, 184, 255)
                                elif persistent.timeofday == "secret":
                                    color (240, 248, 255, 255)
                                elif persistent.timeofday == "alpha":
                                    color (226, 199, 120, 255)
                                size 35
                                line_spacing 1
                        elif persistent.font_size == "small":
                            if who is not None:
                                text who:
                                    id who_id
                                    font limb_font_1
                                    size 28
                                    line_spacing 1
                            text what:
                                id what_id
                                if persistent.timeofday == "prologue":
                                    color (241, 208, 118, 255)
                                elif persistent.timeofday == "day":
                                    color (224, 255, 255, 255)
                                elif persistent.timeofday == "sunset":
                                    color (255, 255, 255, 255)
                                elif persistent.timeofday == "night":
                                    color (249, 255, 184, 255)
                                elif persistent.timeofday == "secret":
                                    color (240, 248, 255, 255)
                                elif persistent.timeofday == "alpha":
                                    color (226, 199, 120, 255)
                                size 28
                                line_spacing 1
            if items:
                vbox:
                    id "menu"
                    for caption, action, chosen  in items:
                        if action:
                            button:
                                style "nvl_menu_choice_button"
                                action action
                                text caption:
                                    style "nvl_menu_choice"
                        else:
                            text caption:
                                style "nvl_dialogue"
    if timeofday != 'alpha':
        imagebutton:
            auto limb_gui_pref + "dialogue_box/"+timeofday+"/backward_%s.png"
            xpos 19
            ypos 920
            action ShowMenu("limb_text_history")
        if not config.skipping:
            imagebutton:
                auto limb_gui_pref + "dialogue_box/"+timeofday+"/forward_%s.png"
                xpos 1763
                ypos 920
                action Skip()
        else:
            imagebutton:
                auto limb_gui_pref + "dialogue_box/"+timeofday+"/fast_forward_%s.png"
                xpos 1763
                ypos 920
                action Skip()

screen limb_quit:
    tag menu
    modal True
    add "anim limb_quit"

    textbutton "Да":
        text_size 70
        style "log_button"
        text_style "settings_link"
        xalign 0.3
        yalign 0.75
        text_font limb_font_1
        text_color '#000'
        text_outlines [(3,"#04FEFD",0,0)]
        text_hover_color '#FFFFFF'
        text_hover_outlines [(3,"#04FEFD",0,0)]
        hovered Play('sound', 'mods/Limb/resourses/sound/sfx/sfx_limb_menu_1.mp3')
        action Start('lumb_main_menu_or_label') #SetField(persistent, "_use_custom_menu", True)

    textbutton "Нет":
        text_size 70
        style "log_button"
        text_style "settings_link"
        xalign 0.7
        yalign 0.75
        text_font limb_font_1
        text_color '#000'
        text_outlines [(3,"#04FEFD",0,0)]
        text_hover_color '#FFFFFF'
        text_hover_outlines [(3,"#04FEFD",0,0)]
        hovered Play('sound', 'mods/Limb/resourses/sound/sfx/sfx_limb_menu_1.mp3')
        action Return()

screen limb_room_1:
    tag menu
    modal False
    add 'mods/Limb/resourses/images/bg/int_wonderland_2.jpg'

    imagebutton:
        auto 'mods/Limb/resourses/images/gui/mirrors/room_1_rightcenter_%s.png'
        pos (652,255)
        focus_mask True
        action Jump('limb_aftersafe_stray')

    imagebutton:
        auto 'mods/Limb/resourses/images/gui/mirrors/room_1_right_%s.png'
        pos (1009,275)
        focus_mask True
        action Jump('limb_aftersafe_adventurer')

    imagebutton:
        auto 'mods/Limb/resourses/images/gui/mirrors/room_1_leftcenter_%s.png'
        pos (333,322)
        focus_mask True
        action Jump('limb_aftersafe_workshop')

    imagebutton:
        auto 'mods/Limb/resourses/images/gui/mirrors/room_1_left_%s.png'
        pos (0,316)
        focus_mask True
        action Jump('limb_aftersafe_cosplay')

screen limb_room_2:
    tag menu
    modal False
    add 'mods/Limb/resourses/images/bg/int_wonderland_3.jpg'
    imagebutton:
        auto 'mods/Limb/resourses/images/gui/mirrors/room_2_left_%s.png'
        pos (0,316)
        focus_mask True
        action Jump('limb_aftersafe_runner')

    imagebutton:
        auto 'mods/Limb/resourses/images/gui/mirrors/room_2_leftcenter_%s.png'
        pos (333,322)
        focus_mask True
        action Jump('limb_aftersafe_psychopass')

    imagebutton:
        auto 'mods/Limb/resourses/images/gui/mirrors/room_2_rightcenter_%s.png'
        pos (652,255)
        focus_mask True
        action Jump('limb_aftersafe_garage')

    imagebutton:
        auto 'mods/Limb/resourses/images/gui/mirrors/room_2_right_%s.png'
        pos (1009,275)
        focus_mask True
        action Jump('limb_aftersafe_killer')

screen limb_room_3:
    tag menu
    modal False
    add 'mods/Limb/resourses/images/bg/int_wonderland_4.jpg'
    # text [str(xpos_new) + '  ' + str(ypos_new)]:
    #     align(1.0,.5)
    imagebutton:
        auto 'mods/Limb/resourses/images/gui/mirrors/room_3_%s.png'
        pos (0,254)
        focus_mask True
        action Return('none')

screen limb_horror_run:
    tag menu
    modal False
    add 'bg int_old_building_sepia_1'
    add 'pl_un_monster_cycle_1'
    add limb_gui_pref + 'hor/limb_run_0.png' at limb_horror_zoom
    #$ renpy.play(sfx_limb_horrorbeat, 'sound_loop')
    #$ renpy.play(sfx_limb_slow_time, 'sound')
    timer 15 action [Hide("limb_horror_run"), Jump("limb_life_horror_scream")]
    imagebutton:
        anchor (0.5, 0.5)
        align (0.1, 0.4)
        idle limb_gui_pref + 'hor/limb_run_dish.png'
        hover im.MatrixColor(limb_gui_pref + 'hor/limb_run_dish.png', im.matrix.brightness(0.2))
        action [Hide('limb_horror_run', flash_red), Jump('limb_life_horror_4')]

    imagebutton:
        anchor (0.5, 0.5)
        align (0.25, 0.675)
        idle limb_gui_pref + 'hor/limb_run_bunker.png'
        hover im.MatrixColor(limb_gui_pref + 'hor/limb_run_bunker.png', im.matrix.brightness(0.2))
        action [Hide('limb_horror_run', flash_red), Jump('limb_life_horror_8')]

    imagebutton:
        anchor (0.5, 0.5)
        align (0.5, 0.9)
        idle limb_gui_pref + 'hor/limb_run_car.png'
        hover im.MatrixColor(limb_gui_pref + 'hor/limb_run_car.png', im.matrix.brightness(0.2))
        action [Hide('limb_horror_run', flash_red), Jump('limb_life_horror_3')]

    imagebutton:
        anchor (0.5, 0.5)
        align (0.625, 0.6)
        idle limb_gui_pref + 'hor/limb_run_closet.png'
        hover im.MatrixColor(limb_gui_pref + 'hor/limb_run_closet.png', im.matrix.brightness(0.2))
        action [Hide('limb_horror_run', flash_red), Jump('limb_life_horror_6')]

    imagebutton:
        anchor (0.5, 0.5)
        align (0.9, 0.425)
        idle limb_gui_pref + 'hor/limb_run_safe.png'
        hover im.MatrixColor(limb_gui_pref + 'hor/limb_run_safe.png', im.matrix.brightness(0.2))
        action [Hide('limb_horror_run', flash_red), Jump('limb_life_horror_7')]

screen limb_horror_safe_brick_1:
    modal False
    imagebutton:
        auto 'mods/Limb/resourses/images/gui/hor/limb_safe_brick_1_%s.png'
        anchor (0.5, 0.5)
        pos (960, 540)
        focus_mask True
        action Hide('limb_horror_safe_brick_1', Dissolve(2, alpha=True))

screen limb_horror_safe_brick_2:
    modal False
    imagebutton:
        auto 'mods/Limb/resourses/images/gui/hor/limb_safe_brick_2_%s.png'
        anchor (0.5, 0.5)
        pos (960, 540)
        focus_mask True
        action Hide('limb_horror_safe_brick_2', Dissolve(2, alpha=True))

screen limb_horror_safe_brick_3:
    modal False
    imagebutton:
        auto 'mods/Limb/resourses/images/gui/hor/limb_safe_brick_3_%s.png'
        anchor (0.5, 0.5)
        pos (960, 540)
        focus_mask True
        action Hide('limb_horror_safe_brick_3', Dissolve(2, alpha=True))

screen limb_horror_safe_brick_4:
    modal False
    imagebutton:
        auto 'mods/Limb/resourses/images/gui/hor/limb_safe_brick_4_%s.png'
        anchor (0.5, 0.5)
        pos (960, 540)
        focus_mask True
        action Hide('limb_horror_safe_brick_4', Dissolve(2, alpha=True))

screen limb_horror_safe_brick_5:
    modal False
    imagebutton:
        auto 'mods/Limb/resourses/images/gui/hor/limb_safe_brick_5_%s.png'
        anchor (0.5, 0.5)
        pos (960, 540)
        focus_mask True
        action Hide('limb_horror_safe_brick_5', Dissolve(2, alpha=True))

screen limb_horror_safe_brick_6:
    modal False
    imagebutton:
        auto 'mods/Limb/resourses/images/gui/hor/limb_safe_brick_6_%s.png'
        anchor (0.5, 0.5)
        pos (960, 540)
        focus_mask True
        action Hide('limb_horror_safe_brick_6', Dissolve(2, alpha=True))

screen limb_butterfly:
    imagebutton:
        idle 'pl_butterfly'
        hover 'pl_butterfly'
        action Jump("limb_life_butterfly")
        at limb_fly

screen limb_kuroneko_1:
    imagebutton:
        anchor (0.5, 0.5)
        pos (0.6, 0.59)
        idle im.Scale(limb_images + "sprites/kuroneko_1.png", 75, 135)
        hover im.Scale(limb_images + "sprites/kuroneko_2.png", 75, 135)
        action Jump("limb_life_nekochan")

screen limb_kuroneko_2:
    imagebutton:
        anchor (0.5, 0.5)
        pos (0.6, 0.59)
        idle im.Scale(limb_images + "sprites/kuroneko_1.png", 75, 135)
        hover im.Scale(limb_images + "sprites/kuroneko_2.png", 75, 135)
        action NullAction()

screen limb_mushroom:
    imagebutton:
        anchor (0.5, 0.5)
        pos (0.43, 0.74)
        idle im.Scale(limb_images + "sprites/mush_1.png", 75, 135)
        hover im.Scale(limb_images + "sprites/mush_2.png", 75, 135)
        action [SetVariable("limb_eat_mushroom", True), Hide("limb_mushroom", dissolve)]

screen limb_keys:
    imagebutton:
        anchor (0.5, 0.5)
        pos (0.095, 0.31)
        idle im.Scale('mods/Limb/resourses/images/sprites/keys.png', 130, 130)
        hover im.Scale('mods/Limb/resourses/images/sprites/keys.png', 130, 130)
        action [Jump('limb_life_horror_5'), Hide('limb_keys')] #Play(звук ключей)

label limb_quit_lbl:
    $ limb_screens_load()
    return

label lumb_main_menu_or_label:
    $ limb_screens_load()
    return

init -100 python:

    def limb_time_from_seconds(seconds):
        mins, secs = divmod(int(float(seconds)), 60)
        hours, minutes = divmod(mins, 60)
        playhours = str(hours)
        if len(str(minutes)) == 1:
            playminutes = "0" + str(minutes)
        else:
            playminutes = str(minutes)

        if len(str(seconds)) == 1:
            playsecs = "0" + str(secs)
        else:
            playsecs = str(secs)
        return playhours+":"+playminutes
    #удалить потом это!!
    xpos_new = 0
    ypos_new = 0
    def fasjkfhsdkjfhasgkdfgashk(d,t,s):
        global xpos_new, ypos_new
        xpos_new,ypos_new = renpy.get_mouse_pos()
        d.xpos = xpos_new
        d.ypos = ypos_new
        return 0

init python:

    limb_pixel_safe = ImageDissolve(limb_images + "gui/effects/pixel_3.png", 1.0, ramplen = 50, reverse = False, alpha = False)
    gdsgsdgfdsg_1 = ''
    gdsgsdgfdsg_2 = ''
    limb_ach_show = ''
    limb_gui_pref = "mods/Limb/resourses/images/gui/"
    limb_safe_access = False
    limb_safe_pass = ' '
    limb_access_color = '#00FF00'
    limb_sl_map_show = False
    #limb_default_music_var = ""
    #limb_default_music_var_2 = ''
    limb_ach_list_show = [
            "all_be_good",
            "blue_lagoon",
            "coma_effect",
            "eternal_shining",
            "fine_mars",
            "near_happiness",
            "origin",
            "other_story",
            "un_dead"
        ]
    for i in limb_ach_list_show:
        renpy.image('limb_' + i, limb_gui_pref + 'achievements/acm_pl_' + i + '_big.png')

    style.limb_safe_style = Style(style.default)
    style.limb_safe_style.font  = "mods/Limb/resourses/images/gui/fonts/var_4.otf"
    style.limb_safe_style.color = "#FF4000"
    style.limb_safe_style.italic = False
    style.limb_safe_style.bold = False
    style.limb_safe_style.size = 35

    def limb_screens_save():
        renpy.display.screen.screens[("limb_old_main_menu", None)] =          renpy.display.screen.screens[("main_menu", None)]
        renpy.display.screen.screens[("limb_old_game_menu_selector", None)] = renpy.display.screen.screens[("game_menu_selector", None)]
        renpy.display.screen.screens[("limb_old_choice", None)] =             renpy.display.screen.screens[("choice", None)]
        renpy.display.screen.screens[("limb_old_yesno_prompt", None)] =       renpy.display.screen.screens[("yesno_prompt", None)]
        renpy.display.screen.screens[("limb_old_say", None)] =                renpy.display.screen.screens[("say", None)]
        renpy.display.screen.screens[("limb_old_nvl", None)] =                renpy.display.screen.screens[("nvl", None)]
        renpy.display.screen.screens[("limb_old_quit", None)] =               renpy.display.screen.screens[("quit", None)]
        renpy.display.screen.screens[("limb_old_save", None)] =               renpy.display.screen.screens[("save", None)]
        renpy.display.screen.screens[("limb_old_load", None)] =               renpy.display.screen.screens[("load", None)]
        renpy.display.screen.screens[("limb_old_preferences", None)] =        renpy.display.screen.screens[("preferences", None)]

    def limb_screens_act():
        config.window_title = u"Лимб"
        config.name = "Limb"
        config.version = "1.0.0"
        renpy.display.screen.screens[("main_menu", None)] =                   renpy.display.screen.screens[("limb_main_menu", None)]
        renpy.display.screen.screens[("game_menu_selector", None)] =          renpy.display.screen.screens[("limb_game_menu_selector", None)]
        renpy.display.screen.screens[("choice", None)] =                      renpy.display.screen.screens[("limb_choice", None)]
        renpy.display.screen.screens[("yesno_prompt", None)] =                renpy.display.screen.screens[("limb_yesno_prompt", None)]
        renpy.display.screen.screens[("say", None)] =                         renpy.display.screen.screens[("limb_say", None)]
        renpy.display.screen.screens[("nvl", None)] =                         renpy.display.screen.screens[("limb_nvl", None)]
        renpy.display.screen.screens[("quit", None)] =                        renpy.display.screen.screens[("limb_quit", None)]
        renpy.display.screen.screens[("save", None)] =                        renpy.display.screen.screens[("limb_save", None)]
        renpy.display.screen.screens[("load", None)] =                        renpy.display.screen.screens[("limb_load", None)]
        renpy.display.screen.screens[("preferences", None)] =                 renpy.display.screen.screens[("limb_preferences", None)]
        

        change_cursor("limb_mouse")
        config.main_menu_music = pl_ae_blow_with_the_fires_remix

    def limb_screens_load():
        if not persistent._use_custom_menu:
            config.window_title = u"Бесконечное лето"
            config.name = "Everlasting_Summer"
            config.version = "1.2"
        else:
            config.window_title = u"Бесконечное лето: Endless Horizons"
            config.name = "Everlasting Summer: EH"
            config.version = "0.95"
        renpy.display.screen.screens[("main_menu", None)] =                   renpy.display.screen.screens[("limb_old_main_menu", None)]
        renpy.display.screen.screens[("game_menu_selector", None)] =          renpy.display.screen.screens[("limb_old_game_menu_selector", None)]
        renpy.display.screen.screens[("choice", None)] =                      renpy.display.screen.screens[("limb_old_choice", None)]
        renpy.display.screen.screens[("yesno_prompt", None)] =                renpy.display.screen.screens[("limb_old_yesno_prompt", None)]
        renpy.display.screen.screens[("say", None)] =                         renpy.display.screen.screens[("limb_old_say", None)]
        renpy.display.screen.screens[("nvl", None)] =                         renpy.display.screen.screens[("limb_old_nvl", None)]
        renpy.display.screen.screens[("quit", None)] =                        renpy.display.screen.screens[("limb_old_quit", None)]
        renpy.display.screen.screens[("save", None)] =                        renpy.display.screen.screens[("limb_old_save", None)]
        renpy.display.screen.screens[("load", None)] =                        renpy.display.screen.screens[("limb_old_load", None)]
        renpy.display.screen.screens[("preferences", None)] =                 renpy.display.screen.screens[("limb_old_preferences", None)]

        change_cursor()
        if persistent._use_custom_menu == True:
            config.main_menu_music = limb_music + "pl_uc_good_morning_morgan.mp3"
        else:
            menu_music()

    limb_screens_save()

    def limb_safe_pass_add(i):
        global limb_safe_pass
        if len(limb_safe_pass) < 3:
            limb_safe_pass += i

    def limb_nool_safe_var():
        global limb_safe_pass
        limb_safe_pass = ''

    def limb_check_safe():
        global limb_safe_pass, limb_access_color
        if str(limb_safe_pass) in ['006','007','013','019','069','111','410','666','999', '091']:
            limb_safe_access = True
            renpy.hide_screen('limb_safe')
            renpy.transition(limb_pixel_safe)
            renpy.play('mods/Limb/resourses/sound/sfx/sfx_limb_opening.mp3', 'sound')
            if str(limb_safe_pass) == '091':
                renpy.jump('limb_safe_neplohaya_popitka')
            renpy.jump('limb_safe_' + str(limb_safe_pass))
        else:
            renpy.play('mods/Limb/resourses/sound/sfx/sfx_limb_menu_2.mp3', 'sound')
        limb_access_color = "#FF4000"
        #renpy.call_screen('limb_safe')
            #jump куда надо если вызов скрина напиши в лс, придумаю другой алгоритм

init 10 python:

    def limb_after_save_screens_act_un():
        global save_name
        if save_name.find(u'Лимб.') != -1:
            config.window_title = u"Лимб"
            config.name = "Limb"
            config.version = "1.0.0"
            renpy.display.screen.screens[("main_menu", None)] =                   renpy.display.screen.screens[("limb_main_menu", None)]
            renpy.display.screen.screens[("game_menu_selector", None)] =          renpy.display.screen.screens[("limb_game_menu_selector", None)]
            renpy.display.screen.screens[("choice", None)] =                      renpy.display.screen.screens[("limb_choice", None)]
            renpy.display.screen.screens[("yesno_prompt", None)] =                renpy.display.screen.screens[("limb_yesno_prompt", None)]
            renpy.display.screen.screens[("say", None)] =                         renpy.display.screen.screens[("limb_say", None)]
            renpy.display.screen.screens[("nvl", None)] =                         renpy.display.screen.screens[("limb_nvl", None)]
            renpy.display.screen.screens[("quit", None)] =                        renpy.display.screen.screens[("limb_quit", None)]
            renpy.display.screen.screens[("save", None)] =                        renpy.display.screen.screens[("limb_save", None)]
            renpy.display.screen.screens[("load", None)] =                        renpy.display.screen.screens[("limb_load", None)]
            renpy.display.screen.screens[("preferences", None)] =                 renpy.display.screen.screens[("limb_preferences", None)]

            change_cursor("limb_mouse")
            config.main_menu_music = pl_ae_blow_with_the_fires_remix

    config.after_load_callbacks.append(limb_after_save_screens_act_un)
