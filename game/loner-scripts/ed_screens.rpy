label ed_stop_channels:
    stop sound
    stop music
    stop ambiencecall
    return

label ed_main_menu_mus:
    play music ed_big_daddy_kills
    window hide
    return    #call screen ed_main_menu

label ed_preview:
    $ default_mouse = "ed_mouse"
    play music ed_snare fadein 3
    show ed_preview with dissolve2
    pause 60
    stop music fadeout 3
    jump ed_d1_start

label ed_quit_menu:
    $ renpy.block_rollback()
    stop sound
    stop music
    stop ambience
    #call ed_stop_channels
    $ ed_screens_diactiv()
    #play music music_list["blow_with_the_fires"]
    #call screen main_menu
    return

  ## Главное меню

screen ed_main_menu:
    tag menu
    modal True
    
    $ change_cursor("ed_mouse")

    add 'ed_menu_ground_anim'
    for i in [
    ['achievements', (150, 350)],
    ['galery',       (150, 550)],
    ['materials',    (150, 750)],
    ['quit',         (1250, 150)],
    ['load',         (700, 150)]
    ]:
        imagebutton:
            auto ed_images + "gui/menu/buttons_mm/" + i[0] + "_%s.png"
            pos i[1]
            action [Hide("ed_main_menu", transition = Dissolve(1)), Show('ed_' + i[0], transition = Dissolve(1))]

    imagebutton:
        auto ed_images + "gui/menu/buttons_mm/new_game_%s.png"
        xpos 150
        ypos 150
        action [Hide("ed_main_menu", transition = Dissolve(1)), Start("ed_preview")]

screen ed_achievements(ed_ach_str = 1):
    tag menu
    modal True
    $ ed_ach_l = ed_ach_str
    add ed_images + "gui/ach/ach_ground_" + str(ed_ach_str) + '.jpg'
    for i in ed_ach_day_dict[ed_ach_str]:
        if persistent.ed_acm_list[i[0]] == True:
            add 'acm_ed_' + i[0] pos i[1]
        else:
            add ed_images + "gui/ach/acm_e.png" pos i[1]

    hbox:
        yalign .45
        xpos 15
        spacing 1600
        imagebutton:
            auto ed_images + "gui/authors/arr_left_%s.png"
            if ed_ach_str == 1:
                action Hide('ed_achievements'), Show("ed_achievements", ed_ach_str = 4, transition = Dissolve(1))

            else:
                action Hide('ed_achievements'), Show("ed_achievements", ed_ach_str = ed_ach_str - 1, transition = Dissolve(1))

        imagebutton:
            auto ed_images + "gui/authors/arr_right_%s.png"
            if ed_ach_str == 4:
                action Hide('ed_achievements'), Show("ed_achievements", ed_ach_str = 1, transition = Dissolve(1))

            else:
                action Hide('ed_achievements'), Show("ed_achievements", ed_ach_str = ed_ach_str + 1, transition = Dissolve(1))

    imagebutton:
        auto ed_images + "gui/authors/back_%s.png"
        align(.5,0.96)
        action Hide('ed_achievements'), Show("ed_main_menu", transition = Dissolve(1))
    

screen ed_galery:
    tag menu
    modal True

    $ gallery_table = []
    if gallery_mode == "cg":
        $ gallery_table = ed_gallery_dict['cg']
    else:
        $ gallery_table = ed_gallery_dict['bg']

    $ len_table = len(gallery_table)

    frame background ed_images + "gui/menu/ed_gmg.jpg":

        grid rows cols:
            yspacing 10
            area(185,288,1600, 585)
            $ cg_displayed = 0
            $ next_page = page + 1
            if next_page > int(len_table/cells):
                $ next_page = 0
            for n in range(0, len_table):
                if n < (page+1)*cells and n>=page*cells:
                    python:
                        if gallery_mode == "cg":
                            _t = im.Crop(ed_images + "cg/"+gallery_table[n]+".jpg", (0,0,1920,1080))
                        elif gallery_mode == "bg":
                            _t = im.Crop(ed_images + "bg/"+gallery_table[n]+".jpg", (0,0,1920,1080))
                        th = im.Scale(_t, 320, 180)
                        img = im.Composite((336,196),(8,8),im.Alpha(th,0.9),(0,0),im.Image(ed_images + "gui/menu/buttons_galery/thumbnail_idle.png"))
                        imgh = im.Composite((336,196),(8,8),th,(0,0),im.Image(ed_images + "gui/menu/buttons_galery/thumbnail_hover.png"))
                    add ed_g.make_button(gallery_table[n], get_image("gui/gallery/blank.png"), None, imgh, img, style="blank_button", bottom_margin=50, right_margin=50)
                    $ cg_displayed += 1

                    if n+1 == len_table:
                        $ next_page = 0

            for j in range(0, cells-cg_displayed):
                null

        if page != 0:
            imagebutton auto ed_images + "gui/menu/buttons_galery/arrow_left_%s.png" pos(0, 40) action (SetVariable('page', page-1), ShowMenu("ed_galery"))
        imagebutton auto ed_images + "gui/menu/buttons_galery/arrow_right_%s.png" pos(1610,20) action (SetVariable('page', next_page), ShowMenu("ed_galery"))

        python:
            def abc(n,k):
                l = float(n)/float(k)
                if l-int(l) > 0:
                    return int(l)+1
                else:
                    return l
            pages = str(page+1)+"/"+str(int(abc(len_table,cells)))
        text pages style "ed_player" xalign 0.985 yalign 0.92

    hbox:
        spacing 350
        align(.5,0.17)
        for i in [
            ['new_cg',   'cg'],
            ['background', 'bg']]:
                imagebutton:
                    auto ed_images + "gui/menu/buttons_galery/" + i[0] + "_%s.png"
                    action (SetVariable('gallery_mode', i[1]), SetVariable('page', 0), ShowMenu("ed_galery"))

    imagebutton:
        auto ed_images + "gui/menu/buttons_galery/back_%s.png"
        pos (80,920)
        action [Hide("ed_galery"), Show("ed_main_menu",  transition = Dissolve(1))]

screen ed_materials:
    tag menu
    modal True
    add ed_images + "gui/menu/ed_matmg.jpg"
    for i in [
    ['authors',(520,190)],
    ['music',(1090,190)],
    ['links',(625,520)]]:
        imagebutton:
            auto ed_images + "gui/menu/buttons_materials/" + i[0] + "_%s.png"
            pos i[1]
            action [Hide("ed_materials"), Show('ed_' + i[0], transition = Dissolve(1))]

    imagebutton:
        auto ed_images + "gui/menu/buttons_materials/back_%s.png"
        xpos 1030
        ypos 850
        action [Hide("ed_materials"), Show("ed_main_menu", transition = Dissolve(1))]

screen ed_music:
    add ed_images + "gui/player/ground_player.jpg"

    side 'c r':
        area(.443,.298,800,475)
        viewport id "ed_player":
            draggable True
            mousewheel True
            scrollbars None
            vbox:
                for name, track in ed_music_dict.iteritems():
                    textbutton name style "log_button" text_style "ed_player" action ed_mr.Play(track)

        vbar value YScrollValue("ed_player"):
            bottom_bar ed_images + "gui/authors/vbar.png"
            top_bar ed_images + "gui/authors/vbar.png"
            thumb ed_images + "gui/authors/thumb.png"
            xmaximum 50

    hbox:
        yalign .45
        xpos 15
        spacing 1600
        imagebutton:
            auto ed_images + "gui/authors/arr_left_%s.png"
            action Hide('ed_player'), Show("ed_links", transition = Dissolve(1))

        imagebutton:
            auto ed_images + "gui/authors/arr_right_%s.png"
            action Hide('ed_player'), Show("ed_authors", transition = Dissolve(1))

    imagebutton:
        auto ed_images + "gui/authors/back_%s.png"
        align(.5,0.96)
        action Hide('ed_player'), Show("ed_materials", transition = Dissolve(1))

screen ed_say:
    $ timeofday = persistent.timeofday
    if persistent.font_size == "large":
        imagebutton:
            auto ed_images + "gui/dialogue_box/backward_%s.png"
            xpos 38
            ypos 924
            action ShowMenu("ed_text_history_screen")
        add ed_images + "gui/dialogue_box/"+timeofday+"/dialogue_box_large.png":
            xpos 174
            ypos 866
        imagebutton:
            auto ed_images + "gui/dialogue_box/hide_%s.png"
            xpos 1508
            ypos 883
            action HideInterface()
        imagebutton:
            auto ed_images + "gui/dialogue_box/save_%s.png"
            xpos 1567
            ypos 883
            action ShowMenu('save')
        imagebutton:
            auto ed_images + "gui/dialogue_box/menu_%s.png"
            xpos 1625
            ypos 883
            action ShowMenu('game_menu_selector')
        imagebutton:
            auto ed_images + "gui/dialogue_box/load_%s.png"
            xpos 1682
            ypos 883
            action ShowMenu('load')
        if not config.skipping:
            imagebutton:
                auto ed_images + "gui/dialogue_box/forward_%s.png"
                xpos 1768
                ypos 924
                action Skip()
        else:
            imagebutton:
                auto ed_images + "gui/dialogue_box/fast_forward_%s.png"
                xpos 1768
                ypos 924
                action Skip()
        text what:
            id "what"
            if persistent.timeofday == "prologue":
                color "#96aabb"
            elif persistent.timeofday == "day":
                color "#F1D076"
            elif persistent.timeofday == "sunset":
                color "#96aabb"
            elif persistent.timeofday == "night":
                color "#fe9502"
            xpos 200
            ypos 920
            xmaximum 1521
            size 35
            line_spacing 1
        if who:
            text who:
                id "who"
                xpos 200
                ypos 879
                size 35
                line_spacing 1
    elif persistent.font_size == "small":
        imagebutton:
            auto ed_images + "gui/dialogue_box/backward_%s.png"
            xpos 38
            ypos 949
            action ShowMenu("ed_text_history_screen")
        add ed_images + "gui/dialogue_box/"+timeofday+"/dialogue_box.png":
            xpos 174
            ypos 916
        imagebutton:
            auto ed_images + "gui/dialogue_box/hide_%s.png"
            xpos 1508
            ypos 933
            action HideInterface()
        imagebutton:
            auto ed_images + "gui/dialogue_box/save_%s.png"
            xpos 1567
            ypos 933
            action ShowMenu('save')
        imagebutton:
            auto ed_images + "gui/dialogue_box/menu_%s.png"
            xpos 1625
            ypos 933
            action ShowMenu('game_menu_selector')
        imagebutton:
            auto ed_images + "gui/dialogue_box/load_%s.png"
            xpos 1682
            ypos 933
            action ShowMenu('load')
        if not config.skipping:
            imagebutton:
                auto ed_images + "gui/dialogue_box/forward_%s.png"
                xpos 1768
                ypos 949
                action Skip()
        else:
            imagebutton:
                auto ed_images + "gui/dialogue_box/fast_forward_%s.png"
                xpos 1768
                ypos 949
                action Skip()
        text what:
            if persistent.timeofday == "prologue":
                color "#96aabb"
            elif persistent.timeofday == "day":
                color "#F1D076"
            elif persistent.timeofday == "sunset":
                color "#96aabb"
            elif persistent.timeofday == "night":
                color "#fe9502"
            id "what"
            xpos 200
            ypos 966
            xmaximum 1521
            size 28
            line_spacing 2
        if who:
            text who:
                id "who"
                xpos 200
                ypos 929
                size 28
                line_spacing 2

screen ed_choice_main:
    modal True
    $ timeofday = persistent.timeofday
    python:
        choice_colors_hover={
                'day': "#FFFAFA",
                'night': "#FFFF00",
                'sunset': "#F0F8FF",
                'prologue': "#FF0000"
                                    }

        choice_colors={
                'day': "#FF0000",
                'night': "#FF4500",
                'sunset': "#BA55D3",
                'prologue': "#C0C0C0"
                                    }

        choice_colors_selected={
                    'day': "#B22222",
                    'night': "#B22222",
                    'sunset': "#B22222",
                    'prologue': "#B22222",
                                }
    window:
        background Frame(ed_images + "gui/choice_box/"+ timeofday +"/choice_box.png", 50, 50)
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
                            idle_color choice_colors[persistent.timeofday]
                            color choice_colors_selected[persistent.timeofday]
                            hover_color choice_colors_hover[persistent.timeofday]
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
                            idle_color choice_colors[persistent.timeofday]
                            color choice_colors_selected[persistent.timeofday]
                            hover_color choice_colors_hover[persistent.timeofday]
                            xcenter 0.5

screen ed_game_menu_selector:
    tag menu
    modal True

    $ timeofday = persistent.timeofday
    $ time_of_day = persistent.timeofday
    button:
        style "blank_button"
        xalign 0
        yalign 0
        xfill True
        yfill True
        action Return()

    add ed_images + "gui/quick_menu/"+timeofday+"/quick_menu.png":
        xalign 0.5
        yalign 0.5

    imagebutton:
        auto ed_images + "gui/quick_menu/"+timeofday+"/main_menu_%s.png"
        xpos 703
        ypos 375
        action MainMenu()

    imagebutton:
        auto ed_images + "gui/quick_menu/"+timeofday+"/save_%s.png"
        xpos 703
        ypos 440
        action ShowMenu('ed_save') #ShowMenu('save')

    imagebutton:
        auto ed_images + "gui/quick_menu/"+timeofday+"/load_%s.png"
        xpos 703
        ypos 508
        action ShowMenu('ed_load') #ShowMenu('load')

    imagebutton:
        auto ed_images + "gui/quick_menu/"+timeofday+"/preferences_%s.png"
        xpos 703
        ypos 575
        action ShowMenu('ed_preferences')

    imagebutton:
        auto ed_images + "gui/quick_menu/"+timeofday+"/quit_%s.png"
        xpos 738
        ypos 643
        action ShowMenu('quit')

    python:
        ui.fixed()

        ui.button(clicked=None, xalign=0.49, ypos=950, style="ed_gms_time_%s"%time_of_day)
        ui.text ("%s" % (save_name), style="ed_gms_time_%s"%time_of_day, size=35)
        ui.button(clicked=None, xalign=0.49, ypos=1030, style="ed_gms_time_%s"%time_of_day)
        ui.text ("%s: %s" % ("Прошло времени", ed_time_from_seconds(renpy.get_game_runtime())), style="ed_gms_time_%s"%time_of_day, size=35)
        ui.close()

screen ed_nvl:
    $ timeofday = persistent.timeofday
    window:
        background Frame(ed_images + "gui/choice_box/"+ timeofday +"/choice_box.png", 50, 50)
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
                                    size 35
                            text what:
                                id what_id
                                size 35
                                if persistent.timeofday == "prologue":
                                    color "#96aabb"
                                elif persistent.timeofday == "day":
                                    color "#F1D076"
                                elif persistent.timeofday == "sunset":
                                    color "#96aabb"
                                elif persistent.timeofday == "night":
                                    color "#fe9502"
                        elif persistent.font_size == "small":
                            if who is not None:
                                text who:
                                    id who_id
                                    size 28
                            text what:
                                id what_id
                                size 28
                                if persistent.timeofday == "prologue":
                                    color "#96aabb"
                                elif persistent.timeofday == "day":
                                    color "#F1D076"
                                elif persistent.timeofday == "sunset":
                                    color "#96aabb"
                                elif persistent.timeofday == "night":
                                    color "#fe9502"

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
    imagebutton:
        auto ed_images + "gui/dialogue_box/backward_%s.png"
        xpos 38
        ypos 924
        action ShowMenu("ed_text_history_screen")

    if not config.skipping:
        imagebutton:
            auto ed_images + "gui/dialogue_box/forward_%s.png"
            xpos 1768
            ypos 924
            action Skip()
    else:
        imagebutton:
            auto ed_images + "gui/dialogue_box/fast_forward_%s.png"
            xpos 1768
            ypos 924
            action Skip()

screen ed_quit:
    tag menu
    modal True
    add "anim ed_quit"
    text translation["Quit_confirm"][_preferences.language]:
        style "settings_link"
        size 70
        text_align 0.5
        xalign 0.5
        yalign 0.3
        color '#FFFFFF'
        antialias True
        kerning 2

    textbutton "Да":
        text_size 70
        style "log_button"
        text_style "settings_link"
        xalign 0.3
        yalign 0.55
        text_color '#FFFFFF'
        text_hover_color '#FF0000'
        action Start("ed_quit_menu") #ЭТО ПОБЕДА, УРА!

    textbutton "Нет":
        text_size 70
        style "log_button"
        text_style "settings_link"
        xalign 0.7
        yalign 0.55
        text_color '#FFFFFF'
        text_hover_color '#FF0000'
        action Return()

screen ed_yesno_prompt:
    $ timeofday = persistent.timeofday
    modal True
    add "ground_"+ timeofday +"_yesno"
    text _(message):
        text_align 0.5
        yalign 0.46
        xalign 0.5
        color '#FFFFFF'
        font header_font
        size 30

    textbutton "Да":
        text_size 60
        style "log_button"
        text_style "settings_link"
        yalign 0.65
        xalign 0.3
        text_color '#FFFFFF'
        text_hover_color '#FF0000'
        action yes_action

    textbutton "Нет":
        text_size 60
        style "log_button"
        text_style "settings_link"
        yalign 0.65
        xalign 0.7
        text_color '#FFFFFF'
        text_hover_color '#FF0000'
        action no_action

screen ed_save: #запомните твари
    tag menu
    modal True

    window background ed_images + "gui/save_load/save_ground.jpg":
        textbutton "Загрузить" text_font ed_images + "gui/save_load/save_load_font.ttf" style "log_button" text_style "settings_link" xalign 0.98 yalign 0.08 action ShowMenu('ed_load')
        textbutton "Настройки" text_font ed_images + "gui/save_load/save_load_font.ttf" style "log_button" text_style "settings_link" xalign 0.02 yalign 0.08 action ShowMenu('ed_preferences')
        
        hbox xalign 0.5 yalign 0.08:
            add ed_images + "gui/preferences/sparkle_red.png" yalign 0.3
            text " "+"СОХРАНИТЬ"+" " font ed_images + "gui/save_load/save_load_font.ttf" style "settings_link" yalign 0.5 color "#ffffff"
            add ed_images + "gui/preferences/sparkle_red.png" yalign 0.3
        
        textbutton "Назад" text_font ed_images + "gui/save_load/save_load_font.ttf" style "log_button" text_style "settings_link" xalign 0.015 yalign 0.92 action Return()

        textbutton "Сохранить игру" text_font ed_images + "gui/save_load/save_load_font.ttf" style "log_button" text_style "settings_link" yalign 0.92 xalign 0.5 action (FunctionCallback(on_save_callback, selected_slot), FileSave(selected_slot))
        textbutton "{size=-12}{b}x{/b} {/size}"+"Удалить" text_font ed_images + "gui/save_load/save_load_font.ttf" style "log_button" text_style "settings_link" yalign 0.92 xalign 0.97 action FileDelete(selected_slot)

        vbox xalign 0.023 yalign 0.5:
            grid 1 10:
                for i in range(0, 10):
                    if i == 0:
                        textbutton "Авто" text_font ed_images + "gui/save_load/save_load_font.ttf" text_size 50 style "log_button" text_style "settings_link" action (FilePage("auto"), SetVariable("selected_slot", False))
                    else:
                        textbutton str(i) text_font ed_images + "gui/save_load/save_load_font.ttf" text_size 50 right_padding 50 style "log_button" text_style "settings_link" action (FilePage(i), SetVariable("selected_slot", False))

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
                        style "ed_save_load_button"
                        has fixed
                        text ( "%s." % i
                               + FileTime(i, format=' %d.%m.%y, %H:%M', empty=" Пустой слот")
                               + "\n" +FileSaveName(i)) style "file_picker_text" xpos 15 ypos 15

screen ed_load: #вспомните твари
    tag menu
    modal True

    window background ed_images + "gui/save_load/load_ground.jpg":

        textbutton "Сохранить" text_font ed_images + "gui/save_load/save_load_font.ttf" style "log_button" text_style "settings_link" xalign 0.98 yalign 0.08 action ShowMenu('ed_save')
        textbutton "Настройки" text_font ed_images + "gui/save_load/save_load_font.ttf" style "log_button" text_style "settings_link" xalign 0.02 yalign 0.08 action ShowMenu('ed_preferences')

        hbox xalign 0.5 yalign 0.08:
            add ed_images + "gui/preferences/sparkle_red.png" yalign 0.3
            text " "+"ЗАГРУЗИТЬ"+" " font ed_images + "gui/save_load/save_load_font.ttf" style "settings_link" yalign 0.5 color "#ffffff"
            add ed_images + "gui/preferences/sparkle_red.png" yalign 0.3

        textbutton "Назад" text_font ed_images + "gui/save_load/save_load_font.ttf" style "log_button" text_style "settings_link" xalign 0.015 yalign 0.92 action Return()

        textbutton "Загрузить игру" text_font ed_images + "gui/save_load/save_load_font.ttf" style "log_button" text_style "settings_link" yalign 0.92 xalign 0.5 action (FunctionCallback(on_load_callback,selected_slot), FileLoad(selected_slot))

        textbutton "{size=-12}{b}x{/b} {/size}"+"Удалить" text_font ed_images + "gui/save_load/save_load_font.ttf" style "log_button" text_style "settings_link" yalign 0.92 xalign 0.97 action FileDelete(selected_slot)

        vbox xalign 0.023 yalign 0.5:
            grid 1 10:
                for i in range(0, 10):
                    if i == 0:
                        textbutton "Авто" text_font ed_images + "gui/save_load/save_load_font.ttf" text_size 50 style "log_button" text_style "settings_link" action (FilePage("auto"), SetVariable("selected_slot", False))
                    else:
                        textbutton str(i) text_font ed_images + "gui/save_load/save_load_font.ttf" text_size 50 right_padding 50 style "log_button" text_style "settings_link" action (FilePage(i), SetVariable("selected_slot", False))

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
                        style "ed_save_load_button"
                        has fixed
                        text ( "%s." % i
                                + FileTime(i, format=' %d.%m.%y, %H:%M', empty=" Пустой слот")
                                + "\n" +FileSaveName(i)) style "file_picker_text" xpos 15 ypos 15

screen ed_authors:
    add ed_images + "gui/authors/ground_authors.jpg"

    side 'c r':
        area(.443,.298,800,475)
        viewport id "ed_authors":
            draggable True
            mousewheel True
            scrollbars None
            vbox:
                for i in ['vedm', 'tulp', 'madn', 'elems']:
                    button:
                        add "tit_" + i
                        background None
                        action NullAction()

        vbar value YScrollValue("ed_authors"):
            bottom_bar ed_images + "gui/authors/vbar.png"
            top_bar ed_images + "gui/authors/vbar.png"
            thumb ed_images + "gui/authors/thumb.png"
            xmaximum 50

    hbox:
        yalign .45
        xpos 15
        spacing 1600
        imagebutton:
            auto ed_images + "gui/authors/arr_left_%s.png"
            action Hide('ed_authors'), Show("ed_music", transition = Dissolve(1))

        imagebutton:
            auto ed_images + "gui/authors/arr_right_%s.png"
            action Hide('ed_authors'), Show("ed_links", transition = Dissolve(1))

    imagebutton:
        auto ed_images + "gui/authors/back_%s.png"
        align(.5,0.96)
        action Hide('ed_authors'), Show("ed_materials", transition = Dissolve(1))

screen ed_links:
    add ed_images + "gui/urls/urls_ground.jpg"
    vbox:
        align(.65,.5)
        for k,v in sorted({
            'Канал на ютубе' : 'https://www.youtube.com/channel/UCHadQhdgeVvBtI0zejN6_rw',
            'Разработчики' : 'https://vk.com/bloner',
            'Визуальная новелла' : 'https://yadi.sk/d/dIAPYhgw3akGq6',
            'Коллекция в Steam' : 'steam://url/CommunityFilePage/1374637382',
            'Реквизиты' : 'https://vk.com/bloner?w=wall-151243760_3091',
            'Беседа в Вконтакте' : 'https://vk.me/join/AJQ1d3W7kAtNhqRvnoHGXtRY'}.iteritems()):

            textbutton k:
                xalign .5
                style "log_button"
                text_style "ed_player"
                text_hover_color '#FFF'
                action OpenURL(v)
    hbox:
        yalign .45
        xpos 15
        spacing 1600
        imagebutton:
            auto ed_images + "gui/authors/arr_left_%s.png"
            action Hide('ed_links'), Show("ed_authors", transition = Dissolve(1))

        imagebutton:
            auto ed_images + "gui/authors/arr_right_%s.png"
            action Hide('ed_links'), Show("ed_music", transition = Dissolve(1))

    imagebutton:
        auto ed_images + "gui/authors/back_%s.png"
        align(.5,0.96)
        action Hide('ed_links'), Show("ed_materials", transition = Dissolve(1))

screen ed_preferences:

    tag menu
    modal True

    $ bar_null = Frame(ed_images + "/gui/preferences/ed_bar_null.png",36,36)
    $ bar_full = Frame(ed_images + "/gui/preferences/ed_bar_full.png",36,36)

    window background ed_images + "gui/preferences/ed_preferences_bg.png":

        textbutton "Сохранить" text_font ed_images + "gui/save_load/save_load_font.ttf" style "log_button" text_style "settings_link" xalign 0.02 yalign 0.08 action ShowMenu('ed_save')
        textbutton "Загрузить" text_font ed_images + "gui/save_load/save_load_font.ttf" style "log_button" text_style "settings_link" xalign 0.98 yalign 0.08 action ShowMenu('ed_load')
        hbox xalign 0.5 yalign 0.08:
            add ed_images + "gui/preferences/sparkle_red.png" yalign 0.3
            text " "+"НАСТРОЙКИ"+" " font ed_images + "gui/save_load/save_load_font.ttf" style "settings_link" yalign 0.5 color "#ffffff"
            add ed_images + "gui/preferences/sparkle_red.png" yalign 0.3
        textbutton "Назад" text_font ed_images + "gui/save_load/save_load_font.ttf" style "log_button" text_style "settings_link" xalign 0.015 yalign 0.92 action Return()

        side "c b r":
            area (0.25, 0.23, 0.51, 0.71)
            viewport id "preferences":
                mousewheel True
                scrollbars None

                has grid 1 17 xfill True spacing 15
                text translation_new["Window_mode"] style "settings_header" xalign 0.5
                grid 2 1 xfill True:

                    hbox xalign 0.5:
                        if _preferences.fullscreen:
                            add ed_images + "gui/preferences/sparkle_black.png"
                        else:
                            null width 22
                        textbutton translation_new["Fullscreen"] style "log_button" text_style "settings_text" action Preference("display", "fullscreen")

                    hbox xalign 0.5:
                        if not _preferences.fullscreen:
                            add ed_images + "gui/preferences/sparkle_black.png"
                        else:
                            null width 22
                        textbutton translation_new["Window"] style "log_button" text_style "settings_text" action Preference("display", "window")



                text translation_new["Skip"] style "settings_header" xalign 0.5
                grid 2 1 xfill True:

                    hbox xalign 0.5:
                        if _preferences.skip_unseen:
                            add ed_images + "gui/preferences/sparkle_black.png"
                        else:
                            null width 22
                        textbutton translation_new["Skip_all"] style "log_button" text_style "settings_text" action Preference("skip", "all")

                    hbox xalign 0.5:
                        if not _preferences.skip_unseen:
                            add ed_images + "gui/preferences/sparkle_black.png"
                        else:
                            null width 22
                        textbutton translation_new["Skip_seen"] style "log_button" text_style "settings_text" action Preference("skip", "seen")


                text translation_new["Volume"] style "settings_header" xalign 0.5

                grid 2 1 xfill True:
                    textbutton translation_new["Music_lower"] style "log_button" text_style "settings_text" xpos 0.1
                    bar value Preference("music volume") left_bar bar_full right_bar bar_null thumb ed_images + "gui/preferences/ed_htumb.png" hover_thumb ed_images + "gui/preferences/ed_htumb.png" xmaximum 1.35 ymaximum 36 xpos -0.55

                grid 2 1 xfill True:
                    textbutton translation_new["Sound"] style "log_button" text_style "settings_text" xpos 0.1
                    bar value Preference("sound volume") left_bar bar_full right_bar bar_null thumb ed_images + "gui/preferences/ed_htumb.png" hover_thumb ed_images + "gui/preferences/ed_htumb.png" xmaximum 1.35 ymaximum 36 xpos -0.55

                grid 2 1 xfill True:
                    textbutton translation_new["Ambience"] style "log_button" text_style "settings_text" xpos 0.1
                    bar value Preference("voice volume") left_bar bar_full right_bar bar_null thumb ed_images + "gui/preferences/ed_htumb.png" hover_thumb ed_images + "gui/preferences/ed_htumb.png" xmaximum 1.35 ymaximum 36 xpos -0.55

                text translation_new["Text_speed"] style "settings_header" xalign 0.5
                bar value Preference("text speed") left_bar bar_full right_bar bar_null thumb ed_images + "gui/preferences/ed_htumb.png" hover_thumb ed_images + "gui/preferences/ed_htumb.png" xalign 0.5 xmaximum 0.8 ymaximum 36

                text translation_new["Autoforward"] style "settings_header" xalign 0.5
                grid 2 1 xfill True:

                    hbox xalign 0.5:
                        if _preferences.afm_time != 0:
                            add ed_images + "gui/preferences/sparkle_black.png"
                        else:
                            null width 22
                        textbutton translation_new["Adult_content_on"] style "log_button" text_style "settings_text" action Preference("auto-forward after click", "enable")

                    hbox xalign 0.5:
                        if _preferences.afm_time == 0:
                            add ed_images + "gui/preferences/sparkle_black.png"
                        else:
                            null width 22
                        textbutton translation_new["Adult_content_off"] style "log_button" text_style "settings_text" action (Preference("auto-forward time", 0), Preference("auto-forward after click", "disable"))

                text translation_new["Autoforward_time"] style "settings_header" xalign 0.5
                bar value Preference("auto-forward time") left_bar bar_full right_bar bar_null thumb ed_images + "gui/preferences/ed_htumb.png" hover_thumb ed_images + "gui/preferences/ed_htumb.png" xalign 0.5 xmaximum 0.8 ymaximum 36


                text translation_new["Font"] style "settings_header" xalign 0.5
                grid 2 1 xfill True:
                    hbox xalign 0.5:
                        if persistent.font_size == "small":
                            add ed_images + "gui/preferences/sparkle_black.png"
                        else:
                            null width 22
                        textbutton translation_new["Normal_font"] style "log_button" text_style "settings_text" action SetField(persistent, "font_size", "small")

                    hbox xalign 0.5:
                        if not persistent.font_size == "small":
                            add ed_images + "gui/preferences/sparkle_black.png"
                        else:
                            null width 22
                        textbutton translation_new["Big_font"] style "log_button" text_style "settings_text" action SetField(persistent, "font_size", "large")
                

                null

            bar value XScrollValue("preferences") left_bar "images/misc/none.png" right_bar "images/misc/none.png" thumb "images/misc/none.png" hover_thumb "images/misc/none.png"
            vbar value YScrollValue("preferences") bottom_bar ed_images + "gui/preferences/ed_vbar.png" top_bar ed_images + "gui/preferences/ed_vbar.png" thumb ed_images + "gui/preferences/ed_thumb.png" xpos 25 xmaximum 50 ymaximum 750

screen ed_text_history_screen:
    tag menu
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

    window background Frame(ed_images + "gui/choice_box/"+timeofday+"/choice_box.png") left_padding 75 right_padding 75 bottom_padding 120 top_padding 120:


        viewport id "ed_text_history_screen":
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
                        text_hover_color "#88c3ff"
                    elif persistent.timeofday == "day":
                        text_color (224, 255, 255, 255)
                        text_hover_color  "#ff0000"
                    elif persistent.timeofday == "sunset":
                        text_color (255, 255, 255, 255)
                        text_hover_color "#8a2be2"
                    elif persistent.timeofday == "night":
                        text_color (249, 255, 184, 255)
                        text_hover_color "#ff9c1b"
                
        $ vbar_null = Frame(ed_images + "gui/choice_box/vbar_null.png",0,0)
        vbar:
            value YScrollValue("ed_text_history_screen")
            bottom_bar vbar_null
            top_bar vbar_null
            thumb ed_images + "gui/choice_box/thumb.png"
            xalign 1.0

init -1001 python:
    ed_images = "mods/Loner/resources/images/"
    # def disable_all_chibi_ed(): #НА КОЙ ОНО ВООБЩЕ НАМ НАДО?
    #     global global_zones_ed
    #     for name,data in global_zones_ed.iteritems():
    #         data["map_chibi"] = None

init -997 python:
    def bg_tmp_image(bgname):
        renpy.image("text "+bgname,LiveComposite((config.screen_width, config.screen_height),(0, 0),"#ffff7f",(50, 150),Text(u"А здесь будет фон про "+bgname, size=40, color="6A7183")))
        return "text "+bgname

    store.map_pics_ed = {
        "bgpic_ed": ed_images + "gui/map/map_ed.jpg",
        "avaliable_ed": ed_images + "gui/map/map_available_ed.jpg",
        "selected_ed": ed_images + "gui/map/map_selected_ed.jpg"
    }

    #init -996 python:
    store.map_zones_ed = {
            "me_mt_house_ed":   {"position":[960,168,1020,227],"default_bg":bg_tmp_image(u"Мой домик")},
            "estrade_ed":       {"position":[1062,54,1154,135],"default_bg":bg_tmp_image(u"Эстрада")},
            "music_club_ed":    {"position":[627,255,692,337],"default_bg":bg_tmp_image(u"Музклуб")},
            "square_ed":        {"position":[887,360,998,545],"default_bg":bg_tmp_image(u"Площадь")},
            "dining_hall_ed":   {"position":[1010,458,1140,585],"default_bg":bg_tmp_image(u"Столовая")},
            "sport_area_ed":    {"position":[1220,481,1574,658],"default_bg":bg_tmp_image(u"Спорткомплекс")},
            "beach_ed":         {"position":[1198,674,1488,831],"default_bg":bg_tmp_image(u"Пляж")},
            "boat_station_ed":  {"position":[832,801,957,855],"default_bg":bg_tmp_image(u"Лодочный причал")},
            "clubs_ed":         {"position":[437,437,650,605],"default_bg":bg_tmp_image(u"Клубы")},
            "library_ed":       {"position":[1158,271,1285,372],"default_bg":bg_tmp_image(u"Библиотека")},
            "medic_house_ed":   {"position":[1042,357,1138,444],"default_bg":bg_tmp_image(u"Медпункт")},
            "camp_entrance_ed": {"position":[284,440,412,554],"default_bg":bg_tmp_image(u"Ворота в лагерь")},
            "forest_ed":        {"position":[90,590,200,820],"default_bg":bg_tmp_image(u"о. Лес")},
            "mine_ed":          {"position":[562,50,690,193],"default_bg":bg_tmp_image(u"Рудник")},

            "un_mi_house_ed":   {"position":[811,154,848,195],"default_bg":bg_tmp_image(u"Лена и Мику")},
            "sl_mz_house_ed":   {"position":[1027,257,1058,300],"default_bg":bg_tmp_image(u"Славя и Женя")},
            "el_sh_house_ed":   {"position":[854,292,884,331],"default_bg":bg_tmp_image(u"Эл и Шурик")},
            "dv_us_house_ed":   {"position":[717,624,758,670],"default_bg":bg_tmp_image(u"Алиса и Ульяна")},
            "shed_ed":          {"position":[1144,488,1211,584],"default_bg":bg_tmp_image(u"Склад")},
            "admin_house_ed":   {"position":[790,350,860,447],"default_bg":bg_tmp_image(u"Администрация")},
            "old_house_ed":     {"position":[238,1005,340,1071],"default_bg":bg_tmp_image(u"Старый корпус")}
    }

    #init -51 python:
    global_map_result_ed="error"

    def init_map_zones_realization_ed(zones_ed,default):
        global global_zones_ed
        global_zones_ed=zones_ed
        for i,data in global_zones_ed.iteritems():
            #data["chibi"] = None
            data["label"] = default
            data["avaliable"] = True
            data["been_here"] = 0

    class Map_ed(renpy.Displayable):
        def __init__(self,pics,default):
            renpy.Displayable.__init__(self)
            self.pics=pics
            self.default=default
            config.overlay_functions.append(self.overlay)

        def disable_all_zones(self):
            global global_zones_ed
            for name,data in global_zones_ed.iteritems():
                data["label"] = self.default
                data["avaliable"] = False
                data["been_here"] = 0

        def enable_all_zones(self):
            global global_zones_ed
            for name,data in global_zones_ed.iteritems():
                data["label"] = self.default
                data["avaliable"] = True
                data["been_here"] = 0

        def set_zone(self,name,label):
            global global_zones_ed
            global_zones_ed[name]["label"] = label
            global_zones_ed[name]["avaliable"] = True

        def reset_zone(self,name):
            global global_zones_ed
            global_zones_ed[name]["label"] = self.default
            global_zones_ed[name]["avaliable"] = False
            global_zones_ed[name]["been_here"] = 0

        def enable_empty_zone(self,name):
            global global_zones_ed
            self.set_zone(name,self.default)
            global_zones_ed[name]["avaliable"] = True

        def reset_current_zone(self):
            self.enable_empty_zone(global_map_result_ed)

        def disable_current_zone(self):
            global global_zones_ed
            global_zones_ed[global_map_result_ed]["avaliable"] = False

        def been_there(self):
            global global_zones_ed
            return global_zones_ed[global_map_result_ed]["been_here"]

        def event(self, ev, x, y, st):
            return

        def render(self, width, height, st, at):
            return renpy.Render(1, 1)

        def zoneclick(self,name):
            global global_zones_ed
            global global_map_result_ed
            store.map_enabled_ed=False
            renpy.scene('mapoverlay')
            global_zones_ed[name]["been_here"] += 1
            global_map_result_ed = name
            renpy.scene()
            ui.jumps(global_zones_ed[name]["label"])()

        def overlay(self):
            if  store.map_enabled_ed:
                global global_zones_ed
                renpy.scene('mapoverlay')
                ui.layer('mapoverlay')
                for name,data in global_zones_ed.iteritems():
                    if data["avaliable"]:
                        pos = data["position"]
                        ui.imagebutton(
                            im.Crop(self.pics["avaliable_ed"],pos[0],pos[1],pos[2]-pos[0],pos[3]-pos[1]),
                            im.Crop(self.pics["selected_ed"], pos[0],pos[1],pos[2]-pos[0],pos[3]-pos[1]), # добавляем сюда суффикс, и в альт_сторе тоже
                            clicked = renpy.curry(self.zoneclick)(name),
                            xpos = pos[0],
                            ypos = pos[1]
                        )
                ui.close()

    store.map_ed = Map_ed(store.map_pics_ed, default)# store.map_chibi, default)

    # import pygame
    # import os
    # import os.path
    # from renpy.store import *
    # from renpy.display.im import ImageBase, image, cache, Composite
    #
    store.map_enabled_ed = False
    store.map_enabled_ed_tmp = False

    def disable_stuff():
        store.map_enabled_ed_tmp = store.map_enabled_ed_tmp or store.map_enabled_ed
        store.map_enabled_ed = False
    def enable_stuff():
        store.map_enabled_ed = store.map_enabled_ed_tmp
        store.map_enabled_ed_tmp = False

init 5 python:
    import renpy.store as store
    config_session = False

    if not config_session:
        def disable_all_zones_ed():
            store.map_ed.disable_all_zones()
        def enable_all_zones_ed():
            store.map_ed.enable_all_zones()
        def set_zone_ed(name,label):
            store.map_ed.set_zone(name,label)
        def reset_zone_ed(name):
            store.map_ed.reset_zone(name)
        def enable_empty_zone_ed(name):
            store.map_ed.enable_empty_zone(name)
        def reset_current_zone_ed():
            store.map_ed.reset_current_zone()
        def disable_current_zone_ed():
            store.map_ed.disable_current_zone()
        def been_there_ed():
            return store.map_ed.been_there()
        #def set_chibi_ed(name,ch):
        #    store.map_ed.set_chibi(name,ch)
        #def reset_chibi_ed(name):
        #    store.map_ed.reset_chibi(name)
        def show_map_ed():
            ui.jumps("_show_map_ed")()
        def init_map_zones_ed():
            init_map_zones_realization_ed(store.map_zones_ed,"nothing_here")

        #init 5:
        #if not config_session:
        renpy.image('widget map_ed', ed_images + "gui/map/map_ed.jpg")
        renpy.image ('bg map_ed', ed_images + "gui/map/map_ed.jpg")

    #init 52 python:

label _show_map_ed:
    scene widget map_ed
    $ store.map_enabled_ed = True
    $ ui.interact()
    jump _show_map_ed

label new_map:
    $ store.map_ed = Map_ed(store.map_pics_ed, default)
    $ init_map_zones_ed()

    $ disable_all_zones_ed()
    $ set_zone_ed("estrade_ed", "estrade")

    $ set_zone_ed("music_club_ed", "music_club")

    $ set_zone_ed("beach_ed", "beach")

    $ show_map_ed()

# label estrade:
#     sl "Эстрада"
#     jump start
#
# label music_club:
#     sl "Музклуб"
#     jump start
#
# label beach:
#     sl "Пляж"
#     jump start

label estrade:
    sl "Эстрада"
    jump new_map

label music_club:
    sl "Музклуб"
    jump new_map

label beach:
    sl "Пляж"
    jump old_map

label estrade1:
    sl "Эстрада1"
    jump old_map

label music_club1:
    sl "Музклуб1"
    jump old_map

label beach1:
    sl "Пляж1"
    return

label old_map:
    $ store.map = Map(store.map_pics, store.map_chibi, default)
    $ init_map_zones()
    $ disable_all_zones()
    $ set_zone("estrade", "estrade1")

    $ set_zone("music_club", "music_club1")

    $ set_zone("beach", "beach1")

    $ show_map()

screen pod_tr:
    $ viewoffon = persistent.viewoffon # Переменная которая автоматом выбирает нужную папку
    add ed_images + "gui/frames/"+viewoffon+"/pod_frame.png"

screen ed_fran_lena:
    key "y" action [SetVariable("ed_fran_un", True), Hide("ed_fran_lena", flash)]
    key "Y" action [SetVariable("ed_fran_un", True), Hide("ed_fran_lena", flash)]
    key "н" action [SetVariable("ed_fran_un", True), Hide("ed_fran_lena", flash)]
    key "Н" action [SetVariable("ed_fran_un", True), Hide("ed_fran_lena", flash)]

screen ed_fran_alisa:
    key "j" action [SetVariable("ed_fran_dv", True), Hide("ed_fran_alisa", flash)]
    key "J" action [SetVariable("ed_fran_dv", True), Hide("ed_fran_alisa", flash)]
    key "о" action [SetVariable("ed_fran_dv", True), Hide("ed_fran_alisa", flash)]
    key "О" action [SetVariable("ed_fran_dv", True), Hide("ed_fran_alisa", flash)]

screen ed_fran_slavya:
    key "d" action [SetVariable("ed_fran_sl", True), Hide("ed_fran_slavya", flash)]
    key "D" action [SetVariable("ed_fran_sl", True), Hide("ed_fran_slavya", flash)]
    key "в" action [SetVariable("ed_fran_sl", True), Hide("ed_fran_slavya", flash)]
    key "В" action [SetVariable("ed_fran_sl", True), Hide("ed_fran_slavya", flash)]

screen ed_fran_miku:
    key "f" action [SetVariable("ed_fran_mi", True), Hide("ed_fran_miku", flash)]
    key "F" action [SetVariable("ed_fran_mi", True), Hide("ed_fran_miku", flash)]
    key "а" action [SetVariable("ed_fran_mi", True), Hide("ed_fran_miku", flash)]
    key "А" action [SetVariable("ed_fran_mi", True), Hide("ed_fran_miku", flash)]

screen ed_fran_ulyana:
    key "z" action [SetVariable("ed_fran_us", True), Hide("ed_fran_ulyana", flash)]
    key "Z" action [SetVariable("ed_fran_us", True), Hide("ed_fran_ulyana", flash)]
    key "я" action [SetVariable("ed_fran_us", True), Hide("ed_fran_ulyana", flash)]
    key "Я" action [SetVariable("ed_fran_us", True), Hide("ed_fran_ulyana", flash)]

init python:
    def frame_1():
        persistent.viewoffon='frame_1'
    def frame_2():
        persistent.viewoffon='frame_2'

    ## Счётчик очков

    # init:
    #     $ filters["ed_pod_counter"] = u"{font=[ed_font]}{size=30}{color=#FF0000}(Одиночка){/color} Счётчик очков.{/font}{/size}"

python early:
    def ed_pod_counter():
        def editoverlay():
            ui.button(clicked=None, xpos=0.29, xanchor=0.0, ypos=2, xpadding=6, xminimum=200)
            ui.text("%s" % (save_name), style="button_text", size=13, color="#FFFFFF")

            # Счётчик смерти
            ui.button(clicked=None, xpos=0.07, xanchor=0.0, ypos=2, xpadding=6, xminimum=120)
            if ed_OB == 0:
                ui.text("%s: %d" % ("Очки Безумия", ed_OB), style="button_text", size=13, color="#FFFFFF")
            elif ed_OB == 1:
                ui.text("%s: %d" % ("Очки Безумия", ed_OB), style="button_text", size=13, color="#FF5349")
            else:
                ui.text("%s: %d" % ("Очки Безумия", ed_OB), style="button_text", size=14, color="#F80000")

            ui.button(clicked=None, xpos=0.14, xanchor=0.0, ypos=2, xpadding=6, xminimum=120)
            if ed_OB == 0:
                ui.text("%s: %d" % ("Очки Елены", ed_OE), style="button_text", size=13, color="#FFFFFF")
            elif ed_OB == 1:
                ui.text("%s: %d" % ("Очки Елены", ed_OE), style="button_text", size=13, color="#AB1352")
            else:
                ui.text("%s: %d" % ("Очки Елены", ed_OE), style="button_text", size=14, color="#560319")

            # Очко Слави
            ui.button(clicked=None, xpos=0.21, xanchor=0.0, ypos=2, xpadding=6, xminimum=120)
            if ed_OB == 0:
                ui.text("%s: %d" % ("Очки Гордыни", ed_OG), style="button_text", size=13, color="#FFFFFF")
            elif ed_OB == 1:
                ui.text("%s: %d" % ("Очки Гордыни", ed_OG), style="button_text", size=13, color="#F0E1B4")
            else:
                ui.text("%s: %d" % ("Очки Гордыни", ed_OG), style="button_text", size=14, color="#D4AE38")

            # DELETE
            ui.button(clicked=None, xpos=0.48, xanchor=1.0, ypos=2, xpadding=6, xminimum=120)
            if ed_d1_victim == 'OD':
                ui.text("%s" % ("Вожатая мертва"), style="button_text", size=13, color="#539466")
            elif ed_d1_victim == 'MI_DV':
                ui.text("%s" % ("Музыкантши мертвы"), style="button_text", size=13, color="#78A2B7")
            elif ed_d1_victim == 'EL_SH':
                ui.text("%s" % ("Техники мертвы"), style="button_text", size=13, color="#E8D6A0")
            else:
                ui.text("%s" % ("Всё ещё впереди"), style="button_text", size=13, color="#FFFFFF")

        config.overlay_functions.append(editoverlay)
