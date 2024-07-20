init:
    $ mods['ed_work_prep'] = u"{color=#FF0000}{size=30}{font=[ed_font]}Одиночка{/font}{/color}{/size}"
    

    image ed_preview = ed_images + "gui/menu/ed_preview.jpg"
    image ed_new_logo = ed_images + "gui/menu/ed_new_logo.jpg"
    image ed_mmg = ed_images + "gui/menu/ed_mmg.png"

    image ed_transition_1 = ed_images + "cg/anim_transition_1.jpg"
    image ed_transition_2 = ed_images + "cg/anim_transition_2.jpg"
    image ed_transition_3 = ed_images + "cg/anim_transition_3.jpg"

    image ed_logo_1 = im.Recolor(ed_images + "gui/logo/emblem_1.jpg", 139, 0, 0, 255)
    image ed_logo_2 = ed_images + "gui/logo/emblem_2.jpg"
    image ed_logo_3 = ed_images + "gui/logo/emblem_3.jpg"

    image ed_qte_F2:
        'ed_qte_F1'
        'ed_qte_F1_2' with ed_alpha_diss_fast
        pause 0.8
        ease 0.3 alpha 0

  ########################## Спрайты ##########################

    image ed_alpha_kostyl:
        'ed_un_d2_silhouette'
        align (0.5, 0.5)
        alpha 0
    image ed_mi_moth_blot:
        'ed_mi_moth'
        'ed_alpha_kostyl' with ed_blot2
        pause 2
        'ed_mi_moth' with ed_blot2
        pause 2
        repeat
    image ed_mt_mite_blot:
        'ed_mt_mite'
        'ed_alpha_kostyl' with ed_blot2
        pause 2
        'ed_mt_mite' with ed_blot2
        pause 2
        repeat
    image ed_pi_silhouette = im.MatrixColor("images/sprites/far/pi/pi_1_pioneer.png", im.matrix.tint(0, 0, 0))
    image ed_sl_fly_blot:
        'ed_sl_fly'
        'ed_alpha_kostyl' with ed_blot2
        pause 2
        'ed_sl_fly' with ed_blot2
        pause 2
        repeat
    image ed_un_d2_smile_pioneer_2_red = im.Recolor(ed_images + "sprites/ed_un_d2_smile_pioneer_2.png", 139, 0, 0, 255)
    image ed_us_yula:
        'ed_us_bucket'
        anchor (0.5, 0.5)
        pos (-0.25, 0.5)
        ease 0.75 pos (1.25, 0.5)
        pause 2
        repeat

  ########################## Изображения ##########################

    transform ed_bus_move:
        choice:
            ease 0.02 pos (0.001, 0.001)
            ease 0.02 pos (0, 0)
        choice:
            ease 0.02 pos (-0.001, 0.001)
            ease 0.02 pos (0, 0)
        choice:
            ease 0.02 pos (0.001, 0.001)
            ease 0.02 pos (0, 0.001)
        choice:
            ease 0.02 pos (-0.001, 0.001)
            ease 0.02 pos (0, 0.001)
        repeat
    transform ed_custom_pos(xp=0.5,yp=0.5,xz=1,yz=1,a=1):
        anchor (0.5, 0.5)
        pos (xp, yp)
        xzoom xz
        yzoom yz
        alpha a
    transform ed_dinneraway:
        xalign 0.8 yalign 0.5 zoom 1.7
        linear 2 zoom 1 xalign 0.5 yalign 0.5
    transform ed_get_achievement:
        pos(0.2, 0.8)
        anchor(0.5, 0.5)
        zoom 0.0
        ease 1.5 zoom 1.05
        ease 0.25 zoom 0.95
        ease 0.25 zoom 1.0
        pause 4.0
        ease 0.5 pos(-0.8, 0.85)
        ease 0.5 pos(-1.0, 0.85) alpha 0.0
    transform ed_kneeling:
        anchor (0.5, 0.5)
        pos (0.5, 0.8)
    transform ed_libentrance:
        anchor (0.5, 0.5)
        xalign 0.5 yalign 0.5 zoom 1
        linear 2 zoom 3 xalign 0.9 yalign 0.8
    transform ed_left_to_right:
        anchor (0.5, 0.5)
        pos (-0.3, 0.5)
        linear 3 xpos 1.3
    transform ed_move(t=2,x1=-0.5,x2=0.5):
        anchor (0.5, 0.5)
        pos (x1, 0.5)
        ease t xpos x2
    transform ed_punch(x=0,y=0):
        anchor (0.5, 0.5)
        pos (0.5+x, 0.5+y)
        rotate 0
        parallel:
            ease 0.4 pos (0.75+x, 1.33+y)
        parallel:
            ease 0.5 rotate 90
    transform ed_running:
        anchor (0.0, 0.0) pos (0.0, 0.0)
        linear 0.1 pos (-7, -5)
        linear 0.1 pos (0, 0)
        linear 0.1 pos (7, -5)
        linear 0.1 pos (0, 0)
        repeat
    transform ed_running_fast:
        truecenter
        zoom 1.25
        parallel:
            ease 0.25 zoom 1.30 rotate 0.75
            ease 0.20 zoom 1.25 rotate -0.75
            ease 0.25 zoom 1.30 rotate 0.75
            ease 0.20 zoom 1.35 rotate -0.75
            repeat
        parallel:
            ease 0.25 xpos 0.495
            ease 0.20 xpos 0.505
            repeat
        parallel:
            ease 0.25 ypos 0.495
            ease 0.30 ypos 0.505
            repeat
    transform ed_running_light:
        align (0.5, 0.5)
        zoom 1.01
        ease 0.2 xalign 0.35 yalign 0.65
        ease 0.2 xalign 0.50 yalign 0.50
        ease 0.2 xalign 0.65 yalign 0.65
        ease 0.2 xalign 0.50 yalign 0.50
        repeat
    transform ed_un_swings:
        pos (0.685, 0.505)
        anchor(0.5, 0.5)
        linear 2 ypos 0.51 zoom 1.05
        linear 2 ypos 0.505 zoom 1
        repeat
    transform ed_walking:
        align (0.5, 0.5)
        zoom 1.01
        ease 0.5 xalign 0.35 yalign 0.65
        ease 0.5 xalign 0.50 yalign 0.50
        ease 0.5 xalign 0.65 yalign 0.65
        ease 0.5 xalign 0.50 yalign 0.50
        repeat

    image ed_blinking:
        contains:
            "anim blink_up"
            pos (0,-1080)
            ease 0.5 xalign 0yalign 0
        contains:
            "anim blink_down"
            pos (0,1080)
            ease 0.5 xalign 0yalign 0
        pause 0.25
        contains:
            "anim blink_up"
            xalign 0yalign 0
            ease 0.5 pos (0,-1080)
        contains:
            "anim blink_down"
            xalign 0yalign 0
            ease 0.5 pos (0,1080)
    image ed_my_name = ParameterizedText(style="ed_call_name")
    image ed_call_my_name:
        'ed_my_name ed_my_name_text_1'
        subpixel True
        zoom 1 align (0.5, 0.5) alpha 1 zoom 0
        parallel:
            linear 1.5 zoom 5
        parallel:
            pause 1
            linear 0.5 alpha 0
        'ed_my_name ed_my_name_text_2'
        subpixel True
        zoom 1 align (0.5, 0.5) alpha 1 zoom 0
        parallel:
            linear 1.5 zoom 5
        parallel:
            pause 1
            linear 0.5 alpha 0
        'ed_my_name ed_my_name_text_3'
        subpixel True
        zoom 1 align (0.5, 0.5) alpha 1 zoom 0
        parallel:
            linear 1.5 zoom 5
        parallel:
            pause 1
            linear 0.5 alpha 0
        'ed_my_name ed_my_name_text_4'
        subpixel True
        zoom 1 align (0.5, 0.5) alpha 1 zoom 0
        parallel:
            linear 1.5 zoom 5
        parallel:
            pause 1
            linear 0.5 alpha 0
        'ed_my_name ed_my_name_text_5'
        subpixel True
        zoom 1 align (0.5, 0.5) alpha 1 zoom 0
        parallel:
            linear 1.5 zoom 5
        parallel:
            pause 1
            linear 0.5 alpha 0
    $ ed_my_name_text_1 = 'НЕ!'
    $ ed_my_name_text_2 = 'НАЗЫВАЙ!'
    $ ed_my_name_text_3 = 'МЕНЯ!'
    $ ed_my_name_text_4 = 'ПО!'
    $ ed_my_name_text_5 = 'ИМЕНИ!'

    image ed_died = ParameterizedText(style="ed_call_name")
    image ed_wasted:
        'ed_died ed_wasted_text'
        subpixel True
        zoom 3 align (0.5, 0.5) alpha 0
        linear 2 alpha 1
    $ ed_wasted_text = 'wasted'

    image ed_show_titre = ParameterizedText(style="ed_titre_show")
    image ed_fake_titre:
        'ed_show_titre ed_titre_text_1'
        subpixel True
        zoom 1 align (0.5, 0.5) alpha 1 zoom 0
        parallel:
            linear 3 zoom 2
        parallel:
            pause 7
            linear 0.5 alpha 0
        pause 3
        'ed_show_titre ed_titre_text_2'
        subpixel True
        zoom 1 align (0.5, 0.5) alpha 1 zoom 0
        parallel:
            linear 3 zoom 2
        parallel:
            pause 7
            linear 0.5 alpha 0
        pause 3
        'ed_show_titre ed_titre_text_3'
        subpixel True
        zoom 1 align (0.5, 0.5) alpha 1 zoom 0
        parallel:
            linear 3 zoom 2
        parallel:
            pause 7
            linear 0.5 alpha 0
        pause 3
        'ed_show_titre ed_titre_text_4'
        subpixel True
        zoom 1 align (0.5, 0.5) alpha 1 zoom 0
        parallel:
            linear 3 zoom 2
        parallel:
            pause 7
            linear 0.5 alpha 0
    $ ed_titre_text_1 = 'Здесь должны были\n        быть титры'
    $ ed_titre_text_2 = 'Но вы уже видели\n       их в Лимбе'
    $ ed_titre_text_3 = 'Всех авторов можно\n      найти в меню'
    $ ed_titre_text_4 = '         Так что просто\nнаслаждайтесь музыкой'

    image ed_sparkle_black:
        ed_images + "gui/misc/sparkle_black.png"
        anchor (0.5, 0.5)
        align (0.5, 0.5)
        alpha 0.9 zoom 0.75
        pause 3
        ease 3 alpha 0
    image ed_sparkle_red:
        ed_images + "gui/misc/sparkle_red.png"
        anchor (0.5, 0.5)
        align (0.5, 0.5)
        alpha 0.9 zoom 0.75
        pause 3
        ease 3 alpha 0
    image ed_eff_sparkles_black:
        SnowBlossom(ImageReference("ed_sparkle_black"), 50, 50, (15, 30), (25, 125)) #, 10, 10, (5, 10), (75, 100))
        anchor (0.5, 0.5)
        align (0.5, 0.5)
        rotate 180
    image ed_eff_sparkles_red:
        SnowBlossom(ImageReference("ed_sparkle_red"), 50, 50, (15, 30), (25, 125)) #, 10, 10, (5, 10), (75, 100))
        anchor (0.5, 0.5)
        align (0.5, 0.5)
        rotate 180
    image ed_menu_ground_anim:
        contains:
            ed_images + "gui/menu/ed_mmg.png"
        contains:
            "ed_eff_sparkles_red"
            alpha 0
            pause 7
            ease 0
        contains:
            "ed_eff_sparkles_red"
            anchor (0.5, 0.5)
            align (0.5, 0.55)
            alpha 0
            pause 7
            ease 0 alpha 1

    image ed_eff_light_snow:
        contains:
            SnowBlossom(im.Alpha(im.FactorScale("images/anim/snow.png", 0.75), 0.75), 50, 50, (15, 30), (25, 125))
        contains:
            SnowBlossom(im.Alpha(im.FactorScale("images/anim/snow.png", 0.5), 0.50), 75, 50, (15, 30), (25, 100))
        contains:
            SnowBlossom(im.Alpha(im.FactorScale("images/anim/snow.png", 0.25), 0.25), 100, 50, (15, 30), (25, 75))
        contains:
            SnowBlossom(im.Alpha(im.FactorScale("images/anim/snow.png", 0.25), 0.15), 200, 50, (15, 30), (25, 50))
        contains:
            SnowBlossom(im.Alpha(im.FactorScale("images/anim/snow.png", 0.2), 0.1), 200, 50, (15, 30), (25, 50))
    image ed_eff_hard_snow:
        contains:
            "ed_eff_light_snow"
        contains:
            "ed_eff_light_snow"
        contains:
            "ed_eff_light_snow"

    image anim ed_agony:
        contains:
            'bg ext_path_sunset'
            subpixel True
            anchor (0.5, 0.5)
            pos (0.5, 0.5)
            ease 1 zoom 1 rotate 0
            ease 0.5 zoom 1.85 rotate 30
            ease 0.9 zoom 1.45 rotate -15
            ease 0.75 zoom 1.3 rotate 10
            ease 1 zoom 2 rotate -25
            ease 0.5 zoom 1.5 rotate 20
            repeat
        contains:
            'bg black'
            ease 1 alpha 0
            ease 1.35 alpha 0.75
            ease 1.05 alpha 0
            ease 0.5 alpha 1
            ease 0.85 alpha 0.35
            ease 0.75 alpha 0.65
            repeat
        contains:
            pause 3
            'ed_blinking'
            pause 5
            'ed_blinking'
            pause 2.25
            'ed_blinking'
            pause 4
            'ed_blinking'
            repeat
    image anim ed_aidpost:
        contains:
            'bg int_aidpost_gray' with ed_blot8
            pause 8
            'bg int_aidpost_red' with ed_blot8
            pause 8
            repeat
        subpixel True
        anchor (0.5, 0.5)
        pos (0.5, 0.5)
        zoom 1
        ease 10 zoom 2.1
        block:
            linear 20 rotate 360
            rotate 0
            repeat
    image anim ed_prolog:
        'anim prolog_1' with Dissolve(5)
        pause 5
        'anim prolog_2' with Dissolve(5)
        pause 5
        repeat
    image anim ed_space:
        'bg space_ed_1' with Dissolve(5)
        pause 5
        'bg space_ed_2' with Dissolve(5)
        pause 5
        repeat

    image bg ext_beach_gray:
        'bg ext_beach_day'
        im.Grayscale("images/bg/ext_beach_day.jpg") with Dissolve(5)
    image bg ext_camp_entrance_behind_zoom_day:
        'bg ext_camp_entrance_day'
        subpixel True
        anchor (0.5, 0.5)
        align (0.5, 0.75) xzoom -2.25 yzoom 2.25
        pause 5
        ease 25 align (0.4, 0.75) xzoom -1.3 yzoom 1.3
    image bg ext_library_red = im.Recolor("images/bg/ext_library_day.jpg", 139, 0, 0, 255)
    image bg ext_library_gray:
        'bg ext_library_fire'
        im.Grayscale(ed_images+"/bg/ext_library_fire.jpg") with Dissolve(10)
    image bg ext_musclub_ignite:
        'bg ext_musclub_day'
        'bg ext_musclub_fire_1' with Dissolve(10)
    image bg ext_musclub_red = im.Recolor(ed_images + "/bg/int_musclub_sunset_ed.jpg", 139, 0, 0, 255)
    image bg ext_sky_red_ed = im.Recolor(ed_images + "/bg/ext_musclub_sunset_ed.jpg", 139, 0, 0, 255)
    image bg ext_square_blood_getting_dark:
        'bg ext_square_day_blood'
        'bg ext_square_sunset_blood' with Dissolve(30)
    image bg ext_square_changing:
        'bg ext_square_red'
        pause 1.5
        'bg ext_square_night'
    image bg ext_square_getting_dark:
        'bg ext_square_day'
        'bg ext_square_sunset' with Dissolve(30)
    image bg ext_warehouse_itai:
        contains:
            'bg ext_warehouse_day_ed'
            im.Recolor(ed_images + "/bg/ext_warehouse_day_ed.jpg", 139, 0, 0, 255) with dissolve_fast
            pause 0.5
            'bg ext_warehouse_day_ed' with dissolve_fast
            pause 0.6
            im.Recolor(ed_images + "/bg/ext_warehouse_day_ed.jpg", 139, 0, 0, 255) with dissolve_fast
            pause 0.5
            'bg ext_warehouse_day_ed' with dissolve_fast
            pause 1.5
            repeat
        contains:
            'ed_un_d2_smile_pioneer_2'
            anchor (0.5, 0.5)
            pos (0.5, 0.5)
            'ed_un_d2_smile_pioneer_2_red' with dissolve_fast
            pause 0.5
            'ed_un_d2_smile_pioneer_2' with dissolve_fast
            pause 0.6
            'ed_un_d2_smile_pioneer_2_red' with dissolve_fast
            pause 0.5
            'ed_un_d2_smile_pioneer_2' with dissolve_fast
            pause 1.5
            repeat
    image bg ext_warehouse_red:
        'bg ext_warehouse_day_ed'
        im.Recolor(ed_images + "/bg/ext_warehouse_day_ed.jpg", 139, 0, 0, 255) with Dissolve(5)
    image bg ext_warehouse_un:
        contains:
            'bg ext_warehouse_day_ed'
        contains:
            'ed_un_d2_smile_pioneer_2'
            align (0.5, 0.5)
        contains:
            'prologue_dream'
            alpha 1
            pause 4
            ease 2 alpha 0
    image bg ext_warehouse_trip:
        'bg ext_warehouse_un'
        subpixel True
        anchor (0.5, 0.5)
        pos (0.5, 0.5)
        zoom 1
        parallel:
            ease 0.95 pos (0.4, 0.65) zoom 1.935
            pause 0.15
            easein 0.55 pos (0.5, 0.5) zoom 1.2
            pause 0.05
            easeout 0.65 pos (0.7, 0.4) zoom 2.15
            pause 0.1
            ease 1.3 pos (0.5, 0.5) zoom 1
        parallel:
            ease 1.1 rotate 20
            easein 0.6 rotate -2.5
            easeout 0.8 rotate -25
            ease 1.3 rotate 0
    image bg int_aidpost_blooded:
        'bg int_aidpost_day'
        'bg int_aidpost_blood' with Dissolve(15)
    image bg int_aidpost_carousel:
        'bg int_aidpost_carousel_1' with Dissolve(3)
        pause 4
        'bg int_aidpost_carousel_2' with Dissolve(3)
        pause 4
        repeat
    image bg int_aidpost_gray = im.MatrixColor(im.Grayscale(ed_images + "/bg/int_aidpost_blood.jpg"), im.matrix.tint(0.25, 0.25, 0.25))
    image bg int_aidpost_red = im.Recolor(ed_images + "/bg/int_aidpost_blood.jpg", 139, 0, 0, 255)
    image bg int_bus_red_sl_fly:
        contains:
            'bg int_bus_red'
        contains:
            'ed_sl_fly'
            center
    image bg int_musclub_red = im.Recolor(ed_images + "/bg/int_musclub_sunset_ed.jpg", 139, 0, 0, 255)
    image bg int_pantry_dark = im.MatrixColor(ed_images + "/bg/int_pantry.jpg", im.matrix.tint(0.35, 0.35, 0.35))
    image bg int_storage_ruined_dark = im.MatrixColor(ed_images + "/bg/int_storage_ruined.jpg", im.matrix.tint(0.25, 0.25, 0.25))

    image cg ed_another_camp:
        choice:
            'bg ext_bus_red' with Dissolve(3)
        choice:
            'bg ext_camp_entrance_red' with Dissolve(3)
        choice:
            'bg ext_road_red' with Dissolve(3)
        choice:
            'bg ext_sea_red' with Dissolve(3)
        choice:
            'bg ext_square_red' with Dissolve(3)
        choice:
            'bg ext_house_of_mt_red' with Dissolve(3)
        pause 2
        repeat

    ## 1.05
    image cg ed_beach_fire_un_shadow_anim:
        'cg ed_beach_fire_un_shadow'
        zoom 1.5
        xalign 0.5 yalign 0.0
        ease 3 xalign 0.5 yalign 0.7 zoom 2
        ease 2.5 xalign 0.5 yalign 1.0 zoom 1.0

    image bg ext_beach_fire_red_anim:
        'bg ext_beach_fire_red'
        xalign 0.5 yalign 1.0
        ease 2 xalign 0.5 yalign 0.0 zoom 2.0
    ## 1.05

    image anim ed_quit:
        choice:
            ed_images + "gui/quit_menu/anim_quit_2.jpg" with Dissolve(5.0)
            pause 5
            ed_images + "gui/quit_menu/anim_quit_1.jpg" with Dissolve(5.0)
            pause 5
            repeat
        choice:
            ed_images + "gui/quit_menu/anim_quit_1.jpg" with Dissolve(5.0)
            pause 5
            ed_images + "gui/quit_menu/anim_quit_2.jpg" with Dissolve(5.0)
            pause 5
            repeat
    image ground_prologue_yesno:
        choice:
            ed_images + "gui/orly/prologue/ground_1.png" with Dissolve(2)
            pause 2
            ed_images + "gui/orly/prologue/ground_2.png" with Dissolve(2)
            pause 2
            repeat

        choice:
            ed_images + "gui/orly/prologue/ground_2.png" with Dissolve(2)
            pause 2
            ed_images + "gui/orly/prologue/ground_1.png" with Dissolve(2)
            pause 2
            repeat
    image ground_day_yesno:
        choice:
            ed_images + "gui/orly/day/ground_1.png" with Dissolve(2)
            pause 2
            ed_images + "gui/orly/day/ground_2.png" with Dissolve(2)
            pause 2
            repeat

        choice:
            ed_images + "gui/orly/day/ground_2.png" with Dissolve(2)
            pause 2
            ed_images + "gui/orly/day/ground_1.png" with Dissolve(2)
            pause 2
            repeat
    image ground_sunset_yesno:
        choice:
            ed_images + "gui/orly/sunset/ground_1.png" with Dissolve(2)
            pause 2
            ed_images + "gui/orly/sunset/ground_2.png" with Dissolve(2)
            pause 2
            repeat

        choice:
            ed_images + "gui/orly/sunset/ground_2.png" with Dissolve(2)
            pause 2
            ed_images + "gui/orly/sunset/ground_1.png" with Dissolve(2)
            pause 2
            repeat
    image ground_night_yesno:
        choice:
            ed_images + "gui/orly/night/ground_1.png" with Dissolve(2)
            pause 2
            ed_images + "gui/orly/night/ground_2.png" with Dissolve(2)
            pause 2
            repeat

        choice:
            ed_images + "gui/orly/night/ground_2.png" with Dissolve(2)
            pause 2
            ed_images + "gui/orly/night/ground_1.png" with Dissolve(2)
            pause 2
            repeat

    image tit_elems:
        on idle:
            ed_images + "gui/authors/tit_elems_0.png" with dissolve

        on hover:
            ed_images + "gui/authors/tit_elems_1.png" with dissolve

        on selected_idle:
            ed_images + "gui/authors/tit_elems_0.png" with dissolve

        on selected_hover:
            ed_images + "gui/authors/tit_elems_1.png" with dissolve
    image tit_madn:
        on idle:
            ed_images + "gui/authors/tit_madn_0.png" with dissolve

        on hover:
            ed_images + "gui/authors/tit_madn_1.png" with dissolve

        on selected_idle:
            ed_images + "gui/authors/tit_madn_0.png" with dissolve

        on selected_hover:
            ed_images + "gui/authors/tit_madn_1.png" with dissolve
    image tit_tulp:
        on idle:
            ed_images + "gui/authors/tit_tulp_0.png" with dissolve

        on hover:
            ed_images + "gui/authors/tit_tulp_1.png" with dissolve

        on selected_idle:
            ed_images + "gui/authors/tit_tulp_0.png" with dissolve

        on selected_hover:
            ed_images + "gui/authors/tit_tulp_1.png" with dissolve
    image tit_vedm:
        on idle:
            ed_images + "gui/authors/tit_vedm_0.png" with dissolve

        on hover:
            ed_images + "gui/authors/tit_vedm_1.png" with dissolve

        on selected_idle:
            ed_images + "gui/authors/tit_vedm_0.png" with dissolve

        on selected_hover:
            ed_images + "gui/authors/tit_vedm_1.png" with dissolve

  ########################## Эффекты ##########################

    $ ed_alpha_diss_fast = Dissolve(0.5, alpha=True)
    $ ed_blot2 = ImageDissolve(ed_images + "gui/dissolves/ed_blot.jpg", 2.0)
    $ ed_blot8 = ImageDissolve(ed_images + "gui/dissolves/ed_blot.jpg", 8.0)
    $ ed_earth_draw = ImageDissolve(ed_images + "gui/dissolves/ed_earth_draw.jpg", 5.0)
    $ ed_lap = ImageDissolve(ed_images + "gui/dissolves/ed_lap.png", 2.0)
    $ ed_night_dis = ImageDissolve(ed_images + "gui/dissolves/ed_night_dis.jpg", 5.0)
    $ ed_flash_red = Fade(0.3, 0.0, 0.2, color='#F80000')

  ########################## Переменные ##########################

    $ ed_achiv_sound = 1
    $ ed_fran_cycle = 0
    $ ed_OB = 0
    $ ed_OS = False
    $ ed_d1_victim = False
    $ ed_gas_action_lose = False
    $ ed_all_d2_achieve = False
    $ ed_death_first = False
    $ ed_fran_all = False
    $ ed_fran_un = False
    $ ed_fran_dv = False
    $ ed_fran_sl = False
    $ ed_fran_mi = False
    $ ed_fran_us = False
    $ ed_qte_fire = False
    $ ed_qte_gas = False
    $ ed_qte_glass = False

  ########################## GUI ##########################

    $ style.ed_player = Style(style.default)
    $ style.ed_player.font = ed_font
    $ style.ed_player.size = 60
    $ style.ed_player.color = "#909CA3"
    $ style.ed_player.hover_color = "#FFFFFF"
    $ style.ed_player.selected_color  = "#909CA3"
    $ style.ed_player.selected_idle_color = "#FF0000"
    $ style.ed_player.selected_hover_color = "#FFFFFF"
    $ style.ed_player.insensitive_color = "#4F4F4F"

    $ style.ed_player.drop_shadow = [(1, 1), (1, 1), (1, 1), (1, 1)]
    $ style.ed_player.drop_shadow_color = "#000"

    $ style.ed_gms_time_day = Style(style.default)
    $ style.ed_gms_time_day.color = "#C11C1C"
    $ style.ed_gms_time_day.italic = False
    $ style.ed_gms_time_day.bold = False

    $ style.ed_gms_time_sunset = Style(style.default)
    $ style.ed_gms_time_sunset.color = "#7B28A4"
    $ style.ed_gms_time_sunset.italic = False
    $ style.ed_gms_time_sunset.bold = False

    $ style.ed_gms_time_night = Style(style.default)
    $ style.ed_gms_time_night.color = "#FE9502"
    $ style.ed_gms_time_night.italic = False
    $ style.ed_gms_time_night.bold = False

    $ style.ed_gms_time_prologue = Style(style.default)
    $ style.ed_gms_time_prologue.color = "#96AABB"
    $ style.ed_gms_time_prologue.italic = False
    $ style.ed_gms_time_prologue.bold = False

    $ style.ed_call_name = Style(style.default)
    $ style.ed_call_name.color = "#FF0000"
    $ style.ed_call_name.size = 80
    $ style.ed_call_name.font = ed_font
    $ style.ed_call_name.drop_shadow = [(1, 1), (1, 1), (1, 1), (1, 1)]
    $ style.ed_call_name.drop_shadow_color = "#000"

    $ style.ed_titre_show = Style(style.ed_call_name)
    $ style.ed_titre_show.color = "#C0C0C0"

    $ style.ed_save_load_button = Style(style.button)
    $ style.ed_save_load_button.background = ed_images + "gui/menu/buttons_galery/thumbnail_idle.png"
    $ style.ed_save_load_button.hover_background = ed_images + "gui/menu/buttons_galery/thumbnail_hover.png"
    $ style.ed_save_load_button.selected_background = ed_images + "gui/save_load/thumbnail_selected.png"
    $ style.ed_save_load_button.selected_hover_background = ed_images + "gui/save_load/thumbnail_selected.png"
    $ style.ed_save_load_button.selected_idle_background = ed_images + "gui/save_load/thumbnail_selected.png"

init -1 python:

    ed_font = "mods/Loner/resources/images/gui/menu/var_6.ttf"
    ed_images = "mods/Loner/resources/images/"
    ed_sounds = "mods/Loner/resources/sound/"
    if persistent.ed_old_music == False:
        ed_music = ed_sounds + "music/"
    else:
        ed_music = ed_sounds + "old_music/" 

  ########################## Файлы ##########################

    ed_g = Gallery()

    ed_page = 0
    ed_gallery_mode = "cg"

    ed_g.locked_button = ed_images + "gui/menu/buttons_galery/not_opened_idle.png"
    ed_g.navigation = False

    ed_g.transition = fade

    ed_gallery_dict = {
    'bg' : [],
    'cg' : []}

    for f in renpy.list_files():
        if f.startswith(ed_images):
            for fold in ('bg','cg'):
                if f[len(ed_images):].startswith(fold+'/'):
                    ed_imgs_name = fold+' '+f[len(ed_images)+3:-(len(f.split('.')[-1])+1)]
                    if not ed_imgs_name[3:].startswith(('anim_transition_', 'ed_bucket_', 'ed_un_picture')):
                        ed_gallery_dict[fold].append(ed_imgs_name[3:])
                        ed_g.button(ed_imgs_name[3:])
                        ed_g.image(im.Crop(f, (0,0,1920,1080)))
                        ed_g.unlock(ed_imgs_name)
                    renpy.image(ed_imgs_name,f)

            for fold in ('gui/menu/buttons/','sprites/'):
                if f[len(ed_images):].startswith(fold):
                    renpy.image(f[len(ed_images+fold):-(len(f.split('.')[-1])+1)],f)
        elif f.startswith(ed_sounds):
            if persistent.ed_old_music == False:
                for fold in ('music/','sfx/','ambience/'):
                    if f[len(ed_sounds):].startswith(fold):
                        renpy.python.store_dicts['store'][f[len(ed_sounds+fold):-(len(f.split('.')[-1])+1)]] = f
            else:
                for fold in ('old_music/','sfx/','ambience/'):
                    if f[len(ed_sounds):].startswith(fold):
                        renpy.python.store_dicts['store'][f[len(ed_sounds+fold):-(len(f.split('.')[-1])+1)]] = f

  ########################## Музыка ##########################

    ed_mr = MusicRoom(fadeout=1.0)
    ed_music_dict = dict()

    ed_all_music = []
    for i in renpy.list_files():
        if (i.startswith(ed_music)) and (i.endswith((".mp3", ".ogg"))):
            ed_all_music.append(i)
            ed_mr.add(i)
            ed_music_name_P = i.split('/')
            ed_music_name_P = ed_music_name_P[-1][3:-4]
            ed_music_name_P = ed_music_name_P.split('_')
            ed_music_name_P[0] = ed_music_name_P[0].title()
            ed_music_name_P = ' '.join(ed_music_name_P)
            ed_music_dict[ed_music_name_P] = i

    ed_track_list={((str((i[30:-4])).replace("ed_", "")).title())[0:40]: str(i) for i in ed_all_music}

    ed_chs_list = (('second_sound','sfx',False),('ed_cycle_sound','sfx',True))
    for n,c,l in ed_chs_list:
        renpy.music.register_channel(n,c,l)

    def ed_mute(fade = 2.5):
        for channel in ["sound", "second_sound", "sound_loop", "ambience", "music"]:
            renpy.music.stop(channel = channel, fadeout = fade)

    def ed_set_volume(channel, value, fade):
        renpy.music.set_volume(volume = value, delay = fade, channel = channel)

  ########################## Изображения ##########################

    ed_sprite_painting = [
        "ed_dv_kowai",
        "ed_el_kowai",
        "ed_elena_1",
        "ed_elena_2",
        "ed_mz_kowai",
        "ed_sem_pioneer",
        "ed_sh_angry_bar",
        "ed_sh_kowai",
        "ed_sl_kowai",
        "ed_un_d2_scary_right_2",
        "ed_un_d2_smile_pioneer_2",
        "ed_us_kowai"
        ]
    for sprite_name in ed_sprite_painting:
        renpy.image(sprite_name+'_night',(im.MatrixColor(ed_images + 'sprites/'+sprite_name+'.png', im.matrix.tint(0.63, 0.78, 0.82))))
        renpy.image(sprite_name+'_sunset',(im.MatrixColor(ed_images + 'sprites/'+sprite_name+'.png', im.matrix.tint(0.94, 0.82, 1.0))))

    def ed_black_sparkles(sh=1):
        if sh == 1:
            renpy.show('ed_eff_sparkles_black', layer='widgetoverlay')
        elif sh == 0:
            renpy.hide('ed_eff_sparkles_black', layer='widgetoverlay')
        renpy.transition(dissolve)

    # Нагло стырил, каюсь...
    def ed_offset_defocusing(imgn, xstep=4, ystep=2, intensity=3):
        args = list()
        for i in range(1, intensity+1):
            offset = {1:(xstep, 0), 2:(0, ystep), 3:(-xstep, 0), 4:(0, -ystep)}
            for j in offset.values():
                args.append((j[0]*i, j[1]*i))
                args.append(Transform(imgn, alpha=random.uniform(0.1, 0.2)))
        return LiveComposite((config.screen_width, config.screen_height), (0, 0), imgn, *args)

  ########################## GUI ##########################

    def ed_screens_activ():
        global default_mouse
        config.window_title = u"Одиночка"
        config.name = "Loner"
        config.version = "1.0.0"
        renpy.display.screen.screens[("main_menu", None)] =                  renpy.display.screen.screens[("ed_main_menu", None)]
        renpy.display.screen.screens[("say", None)] =                        renpy.display.screen.screens[("ed_say", None)]
        renpy.display.screen.screens[("nvl", None)] =                        renpy.display.screen.screens[("ed_nvl", None)]
        renpy.display.screen.screens[("game_menu_selector", None)] =         renpy.display.screen.screens[("ed_game_menu_selector", None)]
        renpy.display.screen.screens[("quit", None)] =                       renpy.display.screen.screens[("ed_quit", None)]
        renpy.display.screen.screens[("choice", None)] =                     renpy.display.screen.screens[("ed_choice_main", None)]
        renpy.display.screen.screens[("yesno_prompt", None)] =               renpy.display.screen.screens[("ed_yesno_prompt", None)]
        renpy.display.screen.screens[("save", None)] =                       renpy.display.screen.screens[("ed_save", None)]
        renpy.display.screen.screens[("load", None)] =                       renpy.display.screen.screens[("ed_load", None)]
        renpy.display.screen.screens[("preferences", None)] =                renpy.display.screen.screens[("ed_preferences", None)]

        change_cursor("ed_mouse")
        if persistent.ed_old_music == False:
            config.main_menu_music = ed_sounds + "music/ed_big_daddy_kills.mp3"
        else:
            config.main_menu_music = ed_sounds + "old_music/ed_big_daddy_kills.mp3"

    def ed_save_screens_old():
        renpy.display.screen.screens[("ed_main_menu_old", None)] =           renpy.display.screen.screens[("main_menu", None)]
        renpy.display.screen.screens[("ed_say_old", None)] =                 renpy.display.screen.screens[("say", None)]
        renpy.display.screen.screens[("ed_nvl_old", None)] =                 renpy.display.screen.screens[("nvl", None)]
        renpy.display.screen.screens[("ed_game_menu_selector_old", None)] =  renpy.display.screen.screens[("game_menu_selector", None)]
        renpy.display.screen.screens[("ed_quit_old", None)] =                renpy.display.screen.screens[("quit", None)]
        renpy.display.screen.screens[("ed_choice_old", None)] =              renpy.display.screen.screens[("choice", None)]
        renpy.display.screen.screens[("ed_yesno_prompt_old", None)] =        renpy.display.screen.screens[("yesno_prompt", None)]
        renpy.display.screen.screens[("ed_save_old", None)] =                renpy.display.screen.screens[("save", None)]
        renpy.display.screen.screens[("ed_load_old", None)] =                renpy.display.screen.screens[("load", None)]
        renpy.display.screen.screens[("ed_preferences_old", None)] =         renpy.display.screen.screens[("preferences", None)]


    def ed_screens_diactiv():
        if not persistent._use_custom_menu:
            config.window_title = u"Бесконечное лето"
            config.name = "Everlasting_Summer"
            config.version = "1.2"
        else:
            config.window_title = u"Бесконечное лето: Endless Horizons"
            config.name = "Everlasting Summer: EH"
            config.version = current_ver
        renpy.display.screen.screens[("main_menu", None)] =                  renpy.display.screen.screens[("ed_main_menu_old", None)]
        renpy.display.screen.screens[("say", None)] =                        renpy.display.screen.screens[("ed_say_old", None)]
        renpy.display.screen.screens[("nvl", None)] =                        renpy.display.screen.screens[("ed_nvl_old", None)]
        renpy.display.screen.screens[("game_menu_selector", None)] =         renpy.display.screen.screens[("ed_game_menu_selector_old", None)]
        renpy.display.screen.screens[("quit", None)] =                       renpy.display.screen.screens[("ed_quit_old", None)]
        renpy.display.screen.screens[("choice", None)] =                     renpy.display.screen.screens[("ed_choice_old", None)]
        renpy.display.screen.screens[("yesno_prompt", None)] =               renpy.display.screen.screens[("ed_yesno_prompt_old", None)]
        renpy.display.screen.screens[("save", None)] =                       renpy.display.screen.screens[("ed_save_old", None)]
        renpy.display.screen.screens[("load", None)] =                       renpy.display.screen.screens[("ed_load_old", None)]
        renpy.display.screen.screens[("preferences", None)] =                renpy.display.screen.screens[("ed_preferences_old", None)]

        change_cursor()
        if persistent._use_custom_menu == True:
            config.main_menu_music = limb_music + "pl_uc_good_morning_morgan.mp3"
        else:
            menu_music()


    ed_save_screens_old()

    def ed_time(ed):
        if ed == 'prolog':
            ed = 'prologue'
        if ed == 'prologue':
            persistent.sprite_time = 'day'
        else:
            persistent.sprite_time = ed
        persistent.timeofday = ed

    def ed_pause_block(t, h):
        renpy.pause(t, hard=h)
        renpy.block_rollback()

  ########################## Достижения ##########################

    #ed_ach_str = 0
    ed_ach_day_dict = {
        1 : [
            ['brobbits',(835, 410)],
            ['date',(208,471)],
            ['everlast_suicide',(249,603)],
            ['five_min',(214,742)],
            ['never_sleep',(134,891)],
            ['phoenix',(865,675)],
            ['sparkle',(954,800)]
            ],

        2 : [
            ['berserk',(265,275)],
            ['bulki_kefir',(265,425)],
            ['night_dna',(265,583)],
            ['kurlyk',(1098,275)],
            ['true_solo',(1098,425)],
            ['soloplay',(1098,583)]
            ],

        3 : [
            ['beach_madness',(762,25)],
            ['carousel',(762,139)],
            ['cold_heart',(881,247)],
            ['darvin',(881,353)],
            ['earth_center',(881,458)],

            ['femdom',(209,465)],
            ['in_the_end',(209,568)],
            ['lava_floor',(209,679)],
            ['my_shadow',(209,788)],
            ['no_harm_in_trying',(209,896)],

            ['not_called',(1097,568)],
            ['only_chance',(1097,679)],
            ['starboy',(1097,788)],
            ['un_library',(1097,896)]
            ],

        4 : [
            ['fastest_hand',(764,117)],
            ['fran',(355,323)],
            ['full_desp',(1046,321)],
            ['Loner',(851,536)],
            ['titre',(1161,735)]
            ]
            }

    if persistent.ed_acm_list == None:
        persistent.ed_acm_list = {
            "beach_madness" : False,
            "berserk" : False,
            "brobbits" : False,
            "bulki_kefir" : False,
            "carousel" : False,
            "cold_heart" : False,
            "darvin" : False,
            "date" : False,
            "earth_center" : False,
            "everlast_suicide" : False,
            "fastest_hand" : False,
            "femdom" : False,
            "five_min" : False,
            "fran" : False,
            "full_desp" : False,
            "in_the_end" : False,
            "kurlyk" : False,
            "lava_floor" : False,
            "Loner" : False,
            "my_shadow" : False,
            "never_sleep" : False,
            "night_dna" : False,
            "no_harm_in_trying" : False,
            "not_called" : False,
            "only_chance" : False,
            "phoenix" : False,
            "soloplay" : False,
            "sparkle" : False,
            "starboy" : False,
            "step_to_abyss" : False,
            "titre" : False,
            "true_solo" : False,
            "un_library" : False,
            "update" : False
        }

    for i in persistent.ed_acm_list.keys():
        renpy.image("acm_ed_" + i, im.Scale(ed_images + "gui/acm_ed_" + i + ".png", 600, 100))
    def show_ed_achiv(acm):
        persistent.ed_acm_list[acm] = True
        renpy.play(sfx_achievement)
        renpy.show("acm_ed_" + acm, [ed_get_achievement], layer = "overlay")
        if acm != 'fastest_hand':
            renpy.play(ed_sounds+'sfx/sfx_ed_die_'+str(ed_achiv_sound)+'.mp3')
        renpy.pause(7, hard = True)
        renpy.hide("acm_ed_" + acm, layer = "overlay")
        renpy.transition(dissolve2)

  ########################### Отмотка ############################

    for i in range(1,53):
        renpy.image('ed_screen_'+str(i), ed_images + 'gui/reverse/'+ str(i)+'.jpg')
    def ed_timeback(num=1, p=0.4):
        for i in range(num, 53):
            renpy.block_rollback()
            renpy.scene()
            renpy.show('ed_screen_%s'%i)
            renpy.show('prologue_dream')
            renpy.pause(p,hard=True)
            if i%10==0:
                p -= 0.08
        renpy.scene()
        renpy.show('bg black')
        renpy.with_statement(flash)
        renpy.pause(1)
        renpy.jump("ed_d1_start")

init 2 python:

    ed_names_list = {'s'   :['семён',(255, 0, 0, 255)],             'pe'  :['персунов',(255, 0, 0, 255)],
                     'g'   :['девушка',(148, 124, 147, 255)],       'ub'  :['убиваша',(71, 37, 125, 255)],
                     'un'  :['тихоня',(71, 37, 125, 255)],          'len' :['лена',(71, 37, 125, 255)],
                     'cs'  :['шлюха',(165, 165, 255, 255)],         'mi'  :['зверёк',(0, 222, 225, 255)],
                     'sl'  :['блондинка',(255, 215, 0, 255)],       'el'  :['гермафродит',(255, 255, 0, 255)],
                     'sh'  :['четырёхглазый',(255, 242, 38, 255)],  'mz'  :['ещё один четырехглазый',(74, 134, 255, 255)],
                     'us'  :['хулиганка',(255, 50, 0, 255)],        'm'   :['малявка',(255, 50, 0, 255)],
                     'fdv' :['алиса',(255, 232, 204, 255)],         'fun' :['лена',(230, 230, 250, 255)],
                     'v'   :['голос',(129, 134, 148, 255)],         'nv'  :['голос в ночи',(129, 134, 148, 255)],
                     'he'  :['он',(255, 0, 0, 255)]}

    eds_bs = Character(u'{color=#FF0000}Семён {/color}{color=#696969}(басом){/color}', drop_shadow=[(2,2),(3,3)], drop_shadow_color='000', what_drop_shadow=[(2,2)], what_drop_shadow_color='000')
    eds_br = Character(u'{color=#FF0000}Семён {/color}{color=#FFF226}(баритоном){/color}', drop_shadow=[(2,2),(3,3)], drop_shadow_color='000', what_drop_shadow=[(2,2)], what_drop_shadow_color='000')
    eds_fc = Character(u'{color=#FF0000}Семён {/color}{color=#FFFF00}(фальцетом){/color}', drop_shadow=[(2,2),(3,3)], drop_shadow_color='000', what_drop_shadow=[(2,2)], what_drop_shadow_color='000')

    def ed_mode_nvl():
        global DynamicCharacter
        global _show_two_window
        gl = globals()
        for x in ed_names_list.keys():
            gl['ed'+x] = DynamicCharacter("ed%s_name"%x, color=ed_names_list[x][1], kind = nvl, who_suffix=":")
            gl["ed%s_name"%x] = ed_names_list[x][0][:1].upper()+ed_names_list[x][0][1:].lower()
        set_mode_nvl()

    def ed_mode_adv():
        global DynamicCharacter
        global _show_two_window
        gl = globals()
        for x in ed_names_list.keys():
            gl['ed'+x] = DynamicCharacter("ed%s_name"%x, color=ed_names_list[x][1], show_two_window=_show_two_window, kind = adv)
            gl["ed%s_name"%x] = ed_names_list[x][0][:1].upper()+ed_names_list[x][0][1:].lower()
        set_mode_adv()

    ed_mode_adv()

init 10 python:

    def ed_after_save_screens_act_un():
        global save_name
        global default_mouse
        if save_name.find(u'Одиночка.') != -1:
            config.window_title = u"Одиночка"
            config.name = "Loner"
            config.version = "1.0.0"
            renpy.display.screen.screens[("main_menu", None)] =               renpy.display.screen.screens[("ed_main_menu", None)]
            renpy.display.screen.screens[("game_menu_selector", None)] =      renpy.display.screen.screens[("ed_game_menu_selector", None)]
            renpy.display.screen.screens[("choice", None)] =                  renpy.display.screen.screens[("ed_choice_main", None)]
            renpy.display.screen.screens[("yesno_prompt", None)] =            renpy.display.screen.screens[("ed_yesno_prompt", None)]
            renpy.display.screen.screens[("say", None)] =                     renpy.display.screen.screens[("ed_say", None)]
            renpy.display.screen.screens[("nvl", None)] =                     renpy.display.screen.screens[("ed_nvl", None)]
            renpy.display.screen.screens[("quit", None)] =                    renpy.display.screen.screens[("ed_quit", None)]
            renpy.display.screen.screens[("preferences", None)] =             renpy.display.screen.screens[("ed_preferences", None)]
            
            change_cursor("ed_mouse")
            if not persistent.ed_old_music:
                config.main_menu_music = ed_sounds + "music/ed_big_daddy_kills.mp3"
            else:
                config.main_menu_music = ed_sounds + "old_music/ed_big_daddy_kills.mp3"

    config.after_load_callbacks.append(ed_after_save_screens_act_un)

init -100 python:

    def ed_time_from_seconds(seconds):
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

init 100:

    image ctc_animation = "images/misc/none.png"
    image ctc_animation_nvl = "images/misc/none.png"

label pod_transit_d2:

    if ed_OB == 1:
        jump pod_transit_d2_1
    elif ed_OB == 2:
        jump pod_transit_d2_2
    else:
        hide screen pod_tr
        $ ed_OB = 1
        jump ed_d2_start

label pod_transit_d2_1:

    $ frame_1()
    $ ed_OB += 1
    $ ed_death_first = True
    show screen pod_tr()
    jump ed_d2_start

label pod_transit_d2_2:

    $ frame_2()
    $ ed_OB += 1
    show screen pod_tr()
    jump ed_d2_start

label ed_work_prep:
    
    $ ed_save_screens_old()
    $ ed_screens_activ()
    $ ed_achiv_sound = 1
    $ ed_fran_cycle = 0
    $ ed_OB = 0
    $ ed_OS = False
    $ ed_d1_victim = False
    $ ed_gas_action_lose = False
    $ ed_all_d2_achieve = False
    $ ed_death_first = False
    $ ed_fran_all = False
    $ ed_fran_un = False
    $ ed_fran_dv = False
    $ ed_fran_sl = False
    $ ed_fran_mi = False
    $ ed_fran_us = False
    $ ed_qte_fire = False
    $ ed_qte_gas = False
    $ ed_qte_glass = False
    #$ store.map_ed = Map_ed(store.map_pics_ed, default)
    if persistent.trailers_on:
        $ renpy.movie_cutscene("video/loner_trailer.webm") ## Трейлер
        $ renpy.pause(2.0)
    jump ed_prolog
