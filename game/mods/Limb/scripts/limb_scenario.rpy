init -1:
    #$ filters["image__filter_hue"] = u"Странная дич"
    #$ filters["image__filter_invert"] = u"Негатив"

    ## Интро

    image limb_intro_girls_1 = limb_images + "gui/intro/intro_girls_1.png"
    image limb_intro_girls_2 = limb_images + "gui/intro/intro_girls_2.png"
    image limb_intro_girls_3 = limb_images + "gui/intro/intro_girls_3.png"
    image limb_intro_girls_4 = limb_images + "gui/intro/intro_girls_4.png"
    image limb_intro_ground = limb_images + "gui/intro/intro_ground.jpg"
    image limb_intro_text = limb_images + "gui/intro/intro_text.png"
    image limb_intro_window = limb_images + "gui/intro/intro_window.png"

    image limb_intro_girls_blinking:
        'limb_intro_girls_1' with limb_alpha_diss3
        pause 3
        'limb_intro_girls_2' with limb_alpha_diss3
        pause 3
        repeat

    image limb_intro_ememblem_1 = limb_images + "gui/intro/endless_horizons/emblem_1.jpg"
    image limb_intro_ememblem_2 = limb_images + "gui/intro/endless_horizons/emblem_2.jpg"
    image limb_intro_ememblem_3 = limb_images + "gui/intro/endless_horizons/emblem_3.jpg"
    image limb_intro_ememblem_4 = limb_images + "gui/intro/endless_horizons/emblem_4.jpg"
    image limb_intro_ememblem_5 = limb_images + "gui/intro/endless_horizons/emblem_5.jpg"
    image limb_intro_ememblem_6 = limb_images + "gui/intro/endless_horizons/emblem_6.jpg"
    image limb_intro_prez_limb_name_1 = limb_images + "gui/intro/endless_horizons/prez_limb_name_1.png"
    image limb_intro_prez_limb_name_2 = limb_images + "gui/intro/endless_horizons/prez_limb_name_2.png"
    image limb_intro_prez_limb_name_3 = limb_images + "gui/intro/endless_horizons/prez_limb_name_3.png"
    image limb_intro_prez_limb_name_4 = limb_images + "gui/intro/endless_horizons/prez_limb_name_4.png"
    image limb_intro_prez_limb_name_5 = limb_images + "gui/intro/endless_horizons/prez_limb_name_5.png"
    image limb_intro_prezent_limb_1_v1 = limb_images + "gui/intro/endless_horizons/prezent_limb_1_v1.png"
    image limb_intro_prezent_limb_1_v2 = limb_images + "gui/intro/endless_horizons/prezent_limb_1_v2.png"
    image limb_intro_prezent_limb_1_v3 = limb_images + "gui/intro/endless_horizons/prezent_limb_1_v3.png"
    image limb_intro_prezent_limb_1_v4 = limb_images + "gui/intro/endless_horizons/prezent_limb_1_v4.png"
    image limb_intro_prezent_limb_1_v5 = limb_images + "gui/intro/endless_horizons/prezent_limb_1_v5.png"
    image limb_intro_prezent_limb_2_ground = limb_images + "gui/intro/endless_horizons/prezent_limb_2_ground.jpg"
    image limb_intro_prezent_limb_2 = limb_images + "gui/intro/endless_horizons/prezent_limb_2.png"
    image limb_intro_prezent_limb_3 = limb_images + "gui/intro/endless_horizons/prezent_limb_3.png"
    image limb_intro_prezent_limb_4 = limb_images + "gui/intro/endless_horizons/prezent_limb_4.png"
    image limb_intro_prezent_limb_5 = limb_images + "gui/intro/endless_horizons/prezent_limb_5.png"
    image limb_intro_prezent_limb_6 = limb_images + "gui/intro/endless_horizons/prezent_limb_6.png"
    image limb_intro_rama = limb_images + "gui/intro/endless_horizons/rama.png"
    image limb_intro_pi_half_1 = im.MatrixColor(limb_images + "gui/intro/endless_horizons/pi_limb_half_1.png", im.matrix.tint(0.63, 0.78, 0.82))
    image limb_intro_pi_half_2 = im.MatrixColor(limb_images + "gui/intro/endless_horizons/pi_limb_half_2.png", im.matrix.tint(0.63, 0.78, 0.82))
    image limb_intro_un_half_1 = im.MatrixColor(limb_images + "gui/intro/endless_horizons/un_limb_half_1.png", im.matrix.tint(0.63, 0.78, 0.82))
    image limb_intro_un_half_2 = im.MatrixColor(limb_images + "gui/intro/endless_horizons/un_limb_half_2.png", im.matrix.tint(0.63, 0.78, 0.82))
    image limb_intro_uv_half_1 = im.MatrixColor(limb_images + "gui/intro/endless_horizons/uv_limb_half_1.png", im.matrix.tint(0.63, 0.78, 0.82))
    image limb_intro_uv_half_2 = im.MatrixColor(limb_images + "gui/intro/endless_horizons/uv_limb_half_2.png", im.matrix.tint(0.63, 0.78, 0.82))

    image limb_intro_fog:
        contains:
            'bg black'
        contains:
            'bg ext_road_fog_2'
            anchor (0.5, 0.5)
            pos (0.5, 0.5)
            zoom 1
            ease 2.5 zoom 0

    ## Изображения

    image pl_butterfly:
        im.Scale(limb_images + "sprites/butterfly_1.png", 45, 40) with limb_alpha_diss_fast
        anchor (0.5, 0.5)
        pos (0.5, 0.5)
        pause 0.5
        im.Scale(limb_images + "sprites/butterfly_2.png", 45, 40) with limb_alpha_diss_fast
        pause 0.5
        repeat
    image pl_dv_orc:
        im.Scale(limb_images + "sprites/dv_orc_full.png", 463*1.75, 1080*1.75)
        anchor (0.5, 0.5)
        pos (0.5, 0.75)
    image pl_dv_orc_close = im.Scale(limb_images + "sprites/dv_orc_full.png", 463*3, 1080*3)
    image pl_dv_vamp_normal_red = im.Recolor(limb_images + "sprites/dv_vamp_normal.png", 255, 0, 0, 255)
    image pl_el_real_man_sin_strike:
        contains:
            'pl_el_real_man_sin_serious'
            anchor (0.5, 0.5)
            pos (0.5, 0.5)
        contains:
            'pl_point_strike'
            anchor (0.5, 0.5)
            pos (0.5, 1.0)
    image pl_hand_magic_fire:
        contains:
            'pl_hand'
        contains:
            'pl_hand_magic_2' with limb_blot_fast
            alpha 0.75
            ease 0.2 alpha 1
            ease 0.8 alpha 0.75
            'pl_hand_magic_3' with limb_blot_fast
            alpha 0.75
            ease 0.2 alpha 1
            ease 0.8 alpha 0.75
            'pl_hand_magic_4' with limb_blot_fast
            alpha 0.75
            ease 0.2 alpha 1
            ease 0.8 alpha 0.75
            repeat
        contains:
            'pl_hand_magic_5' with limb_blot_fast
            alpha 0.75
            ease 0.2 alpha 1
            ease 0.8 alpha 0.75
            'pl_hand_magic_6' with limb_blot_fast
            alpha 0.75
            ease 0.2 alpha 1
            ease 0.8 alpha 0.75
            repeat
        contains:
            'pl_fireflies'
            anchor (0.5, 0.5)
            pos (0.25, 0.45)
            zoom 0.3
            rotate 0
            linear 30 rotate -3600
            repeat
        contains:
            'pl_fireflies_alt'
            anchor (0.5, 0.5)
            pos (0.25, 0.45)
            zoom 0.3
            rotate 0
            linear 90 rotate -3600
            repeat
    image pl_hand_magic_hide:
        'pl_hand_magic_fire'
        'pl_hand_magic_1' with limb_alpha_diss
        pause 1.5
        'pl_hand' with limb_alpha_diss
    image pl_hand_magic_show:
        'pl_hand'
        pause 3
        'pl_hand_magic_1' with limb_alpha_diss
        pause 1.5
        'pl_hand_magic_fire' with limb_alpha_diss
    image pl_hand_record_red:
        contains:
            im.Scale(limb_images+ "sprites/hand_record_0.png", 1920, 1080)
        contains:
            'pl_record_black'
            alpha 0
            pause 1
            ease 0.1 alpha 1
            pause 1
            ease 0.1 alpha 0
            repeat
    image pl_ma_queen_glitch:
        'pl_ma_limb_2_alt'
        pause 2.1
        'pl_mi_queen'
        pause 0.025
        'pl_ma_limb_2_alt'
    image pl_mi_elf_shine:
        contains:
            'pl_mi_elf_1' with Dissolve(5,alpha=True)
            anchor (0.5, 0.5)
            pos (0.5, 0.5)
            pause 5
            'pl_mi_elf_light' with Dissolve(5,alpha=True)
            pause 5
            repeat
        contains:
            'pl_mi_elf_anim_1' with limb_alpha_diss
            anchor (0.5, 0.5)
            pos (0.5, 0.5)
            pause 1
            'pl_mi_elf_anim_2' with limb_alpha_diss
            pause 1
            'pl_mi_elf_anim_3' with limb_alpha_diss
            pause 1
            repeat
    image pl_mi_queen_eyes:
        'pl_mi_queen'
        'pl_mi_queen_alt'
        pause 0.2
        'pl_mi_queen'
    image pl_mi_queen_glitch:
        'pl_mi_queen'
        pause 2.1
        'pl_mi_queen_sin_1'
        pause 0.11
        'pl_mi_queen'
    image pl_mi_vamp_red = im.Recolor(limb_images + "sprites/mi_vamp_not_smile.png", 255, 0, 0, 255)
    image pl_moto_hotline:
        'pl_moto_3'
        'pl_moto_4' with Dissolve(20,alpha=True)
    image pl_mt_witch_shine_1:
        contains:
            'pl_mt_witch_1' with Dissolve(5,alpha=True)
            anchor (0.5, 0.5)
            pos (0.5, 0.5)
        contains:
            'pl_mt_witch_anim_1' with limb_alpha_diss
            anchor (0.5, 0.5)
            pos (0.5, 0.5)
            pause 1
            'pl_mt_witch_anim_2' with limb_alpha_diss
            pause 1
            repeat
    image pl_mt_witch_shine_2:
        contains:
            'pl_mt_witch_2' with Dissolve(5,alpha=True)
            anchor (0.5, 0.5)
            pos (0.5, 0.5)
        contains:
            'pl_mt_witch_anim_1' with limb_alpha_diss
            anchor (0.5, 0.5)
            pos (0.5, 0.5)
            pause 1
            'pl_mt_witch_anim_2' with limb_alpha_diss
            pause 1
            repeat
    image pl_sh_night_scared:
        'pl_sh_miami_2_night'
        xanchor 0.5
        xpos 1.2
        ease 2 xpos 0.9
        'pl_sh_miami_1_night' with vpunch
    image pl_sl_baw = im.Grayscale(limb_images+ "sprites/sl_party_1.png")
    image pl_sl_fairy_fly_1:
        contains:
            'pl_sl_fairy_wings'
            limb_fairy_wings
        contains:
            im.Scale(limb_images + "sprites/sl_fairy_1.png", 270, 702)
            limb_fairy_fly
    image pl_sl_fairy_fly_1_close:
        contains:
            'pl_sl_fairy_wings_close'
            limb_fairy_wings_close
        contains:
            im.Scale(limb_images + "sprites/sl_fairy_1.png", 540, 1404)
            limb_fairy_fly
    image pl_sl_fairy_fly_2:
        contains:
            'pl_sl_fairy_wings'
            limb_fairy_wings
        contains:
            im.Scale(limb_images + "sprites/sl_fairy_2.png", 270, 702)
            limb_fairy_fly
    image pl_sl_fairy_fly_2_close:
        contains:
            'pl_sl_fairy_wings_close'
            limb_fairy_wings_close
        contains:
            im.Scale(limb_images + "sprites/sl_fairy_2.png", 540, 1404)
            limb_fairy_fly
    image pl_sl_fairy_fly_3:
        contains:
            'pl_sl_fairy_wings'
            limb_fairy_wings
        contains:
            im.Scale(limb_images + "sprites/sl_fairy_3.png", 270, 702)
            limb_fairy_fly
    image pl_sl_fairy_fly_3_close:
        contains:
            'pl_sl_fairy_wings_close'
            limb_fairy_wings_close
        contains:
            im.Scale(limb_images + "sprites/sl_fairy_3.png", 540, 1404)
            limb_fairy_fly
    image pl_sl_fairy_wings:
        im.Scale(limb_images + "sprites/sl_wing_1.png", 540, 702)
        anchor (0.5, 0.5)
        pos (0.8, 0.5)
        pause 0.01
        im.Scale(limb_images + "sprites/sl_wing_2.png", 540, 702)
        pause 0.01
        im.Scale(limb_images + "sprites/sl_wing_1.png", 540, 702)
        pause 0.01
        im.Scale(limb_images + "sprites/sl_wing_3.png", 540, 702)
        pause 0.01
        repeat
    image pl_sl_fairy_wings_close:
        im.Scale(limb_images + "sprites/sl_wing_1.png", 1080, 1404)
        anchor (0.5, 0.5)
        pos (0.5, 0.5)
        pause 0.01
        im.Scale(limb_images + "sprites/sl_wing_2.png", 1080, 1404)
        pause 0.01
        im.Scale(limb_images + "sprites/sl_wing_1.png", 1080, 1404)
        pause 0.01
        im.Scale(limb_images + "sprites/sl_wing_3.png", 1080, 1404)
        pause 0.01
        repeat
    image pl_sl_party:
        'pl_sl_party_1_night'
        'pl_sl_party_2_night' with Dissolve(15, alpha=True)
    image pl_sl_pi_body_1 = "images/sprites/far/sl/sl_4_body.png"
    image pl_sl_pi_body_2 = "images/sprites/far/sl/sl_3_body.png"
    image pl_sl_pi_emo_1 = "images/sprites/far/sl/sl_4_scared.png"
    image pl_sl_pi_emo_2 = "images/sprites/far/sl/sl_3_angry.png"
    image pl_sl_pi_clothes = "images/sprites/far/sl/sl_4_pioneer.png"
    image pl_sl_un_glitch:
        'sl smile dress far'
        truecenter
        pause 4.7
        'pl_un_glitch_1'
        pause 0.1
        'pl_un_glitch_2'
        pause 0.1
        'pl_un_glitch_1'
        pause 0.1
        'pl_un_dress_3'
    image pl_sl_vamp_red = im.Recolor(limb_images + "sprites/sl_vamp_not_smile.png", 255, 0, 0, 255)
    image pl_sm_motherfuck:
        'pl_sm_motherfuck_1'
        'pl_sm_motherfuck_2' with Dissolve(3)
        'pl_sm_motherfuck_3' with Dissolve(10, alpha=True)
    image pl_sm_silhouette = im.MatrixColor(limb_images + "sprites/sm_winter_1.png", im.matrix.tint(0, 0, 0))
    image pl_sm_winter:
        'pl_sm_winter_1'
        pause 4
        'pl_sm_winter_2' with limb_alpha_diss3
    image pl_smoke_fade:
        contains:
            'pl_smoke_1'
            left
            alpha 0.3
        contains:
            'pl_smoke_2'
            center
            alpha 0.3
        contains:
            'pl_smoke_3'
            right
            alpha 0.3
        contains:
            'bg white'
            alpha 0
            pause 2
            'bg black' with Dissolve(10)
    image pl_un_dress_silhouette = im.MatrixColor(limb_images + "sprites/un_dress_1.png", im.matrix.tint(0, 0, 0))
    image pl_un_dv_happy__1:
        contains:
            'pl_monster_a'
            anchor (0.5, 0.5)
            pos (0.5, 0.5)
            zoom 1.35
            alpha 0
        contains:
            'pl_un_dv_happy_1'
            anchor (0.5, 0.5)
            pos (0.5, 0.5)
    image pl_un_dv_happy__2:
        contains:
            'pl_monster_a'
            anchor (0.5, 0.5)
            pos (0.5, 0.5)
            zoom 1.35
            alpha 0
        contains:
            'pl_un_dv_happy_2'
            anchor (0.5, 0.5)
            pos (0.5, 0.5)
    image pl_un_dv_pixel:
        'pl_un_dv_queen_1'
        'pl_un_dv_queen_2' with limb_pixel_4
        pause 0.8
        'pl_un_dv_queen_3' with limb_pixel_4
        pause 0.8
        'pl_un_dv_queen_4' with limb_pixel_4
        pause 0.8
        'pl_un_dv_queen_5' with limb_pixel_4
    image pl_un_draenei__1:
        'pl_un_draenei_1' with limb_alpha_diss2
        anchor (0.5, 0.5)
        pos (0.5, 0.5)
        pause 2
        'pl_un_draenei_light_1' with limb_alpha_diss2
        pause 2
        repeat
    image pl_un_draenei__2:
        'pl_un_draenei_2' with limb_alpha_diss2
        anchor (0.5, 0.5)
        pos (0.5, 0.5)
        pause 2
        'pl_un_draenei_light_2' with limb_alpha_diss2
        pause 2
        repeat
    image pl_un_draenei__3:
        'pl_un_draenei_3' with limb_alpha_diss2
        anchor (0.5, 0.5)
        pos (0.5, 0.5)
        pause 2
        'pl_un_draenei_light_3' with limb_alpha_diss2
        pause 2
        repeat
    image pl_un_ghost:
        'pl_un_sleep_ghost'
        anchor (0.5, 0.5)
        pos (-0.25, 0.5)
        ease 3 pos (1.25, 0.5)
        'pl_un_dress_ghost_2'
        anchor (0.5, 0.5)
        pos (-0.25, 0.5)
        ease 3 pos (1.25, 0.5)
        'pl_un_dress_ghost_1'
        anchor (0.5, 0.5)
        pos (-0.25, 0.5)
        ease 3 pos (1.25, 0.5)
        repeat
    image pl_un_monster_1:
        'pl_un_monster_queen'
        anchor (0.5, 0.5)
        pos (0.5, 0.5)
        'pl_un_monster_undress' with Dissolve(3, alpha=True)
        pause 3
        'pl_monster_a' with limb_pixel_4
        anchor (0.5, 0.5)
        pos (0.5, 0.5)
        pause 1
        'pl_un_monster_cycle_1'
    image pl_un_monster_2:
        'pl_un_monster_queen'
        anchor (0.5, 0.5)
        pos (0.5, 0.5)
        'pl_un_dv_happy__1' with limb_pixel_4
        anchor (0.5, 0.5)
        pos (0.5, 0.5)
        pause 2
        'pl_un_dv_happy__2' with limb_pixel_2
        anchor (0.5, 0.5)
        pos (0.5, 0.5)
        pause 2
        'pl_un_dv_happy_3' with limb_pixel_4
        anchor (0.5, 0.5)
        pos (0.5, 0.5)
        pause 2
        'pl_monster_d' with pixellate
        pause 1.5
        'pl_monster_e' with limb_pixel_4
        pause 0.2
        'pl_monster_a' with limb_pixel_2
        pause 0.3
        'pl_monster_d' with limb_pixel_3
        pause 1
        'pl_un_monster_cycle_1' with pixellate
    image pl_un_monster_3:
        'pl_monster_7'
        anchor (0.5, 0.5)
        pos (0.5, 0.5)
        'pl_monster_6' with limb_blot
        pause 2
        'pl_monster_5' with limb_blot
        pause 2
        'pl_monster_4' with limb_blot
        pause 2
        'pl_monster_3' with limb_blot
        pause 2
        'pl_monster_2' with limb_blot
        pause 2
        'pl_un_monster_undress' with limb_blot
        pause 2
    image pl_un_monster_blink:
        pause 30
        'pl_monster_x'
        alpha 1
        pause 0.0001
        alpha 0
        repeat
    image pl_un_monster_cycle_1:
        'pl_monster_a'
        anchor (0.5, 0.5)
        pos (0.5, 0.5)
        choice:
            pause 1
        choice:
            pause 1.5
        choice:
            pause 0.5
        'pl_monster_b'
        choice:
            pause 0.1
        choice:
            pause 0.3
        choice:
            pause 0.5
        'pl_monster_c'
        choice:
            pause 0.1
        choice:
            pause 0.5
        choice:
            pause 0.8
        'pl_monster_a'
        choice:
            pause 0.1
        choice:
            pause 0.3
        choice:
            pause 0.6
        'pl_monster_d'
        choice:
            pause 1.2
        choice:
            pause 0.4
        choice:
            pause 0.8
        'pl_monster_a'
        choice:
            pause 1
        choice:
            pause 1.7
        choice:
            pause 0.6
        'pl_monster_e'
        choice:
            pause 0.01
        choice:
            pause 0.05
        choice:
            pause 0.1
        'pl_monster_c'
        choice:
            pause 0.1
        choice:
            pause 0.5
        choice:
            pause 0.8
        repeat
    image pl_un_monster_cycle_2:
        'pl_monster_7' with limb_blot
        anchor (0.5, 0.5)
        pos (0.5, 0.5)
        pause 2
        'pl_monster_4' with limb_blot
        pause 2
        'pl_monster_6' with limb_blot
        pause 2
        repeat
    image pl_un_monster_queen:
        contains:
            'pl_monster_a'
            anchor (0.5, 0.5)
            pos (0.5, 0.5)
            zoom 1.35
            alpha 0
        contains:
            'pl_un_dv_queen_alt'
            anchor (0.5, 0.5)
            pos (0.5, 0.5)
    image pl_un_monster_undress:
        contains:
            'pl_monster_a'
            anchor (0.5, 0.5)
            pos (0.5, 0.5)
            zoom 1.35
            alpha 0
        contains:
            'pl_un_dv_queen_undress'
            anchor (0.5, 0.5)
            pos (0.5, 0.5)
    image pl_us_unfocus:
        contains:
            'pl_us_cosplay'
            anchor (0.5, 0.5)
            xpos 0.7
            ypos 0.5
            alpha 1
            pause 0.3
            ease 1.5 xpos 0.8 alpha 0.5
            ease 1.5 xpos 0.75 alpha 0.75
            ease 1.5 xpos 0.8 alpha 0.5
            ease 1.5 xpos 0.7 alpha 1
        contains:
            limb_images + "sprites/us_cosplay.png"
            anchor (0.5, 0.5)
            xpos 0.7
            ypos 0.5
            alpha 1
            pause 0.3
            ease 1.5 xpos 0.6 alpha 0.5
            ease 1.5 xpos 0.65 alpha 0.75
            ease 1.5 xpos 0.6 alpha 0.5
            ease 1.5 xpos 0.7 alpha 1
    image pl_us_zombie_3:
        im.MatrixColor(limb_images + "sprites/us_zombie_1.png", im.matrix.tint(0.3, 0.3, 0.3))
        xzoom -1
    image pl_us_zombie_3_invers:
        im.MatrixColor(im.MatrixColor(limb_images + "sprites/us_zombie_1.png", im.matrix.tint(0.3, 0.3, 0.3)), im.matrix.invert())
        xzoom -1
    image pl_us_zombie_4:
        im.MatrixColor(limb_images + "sprites/us_zombie_2.png", im.matrix.tint(0.45, 0.45, 0.45))
        xzoom -1
    image pl_us_zombie_4_invers:
        im.MatrixColor(im.MatrixColor(limb_images + "sprites/us_zombie_2.png", im.matrix.tint(0.3, 0.3, 0.3)), im.matrix.invert())
        xzoom -1
    image pl_us_zombie_blink_1:
        im.MatrixColor(limb_images + "sprites/us_zombie_1.png", im.matrix.tint(0, 0, 0))
        alpha 0.5
        pause 2
        linear 2 alpha 0.0
        pause 2
        linear 2 alpha 0.5
        repeat
    image pl_us_zombie_blink_2:
        im.MatrixColor(limb_images + "sprites/us_zombie_2.png", im.matrix.tint(0, 0, 0))
        alpha 0.5
        pause 2
        linear 2 alpha 0.0
        pause 2
        linear 2 alpha 0.5
        repeat
    image pl_uv_anim_mimi:
        contains:
            limb_images + 'sprites/uv_castrated.png'
            left
        contains:
            limb_images + 'sprites/uv_mimi_1.png' with limb_alpha_diss_fast
            left
            pause 0.3
            limb_images + 'sprites/uv_mimi_2.png' with limb_alpha_diss_fast
            left
            pause 0.05
            limb_images + 'sprites/uv_mimi_3.png' with limb_alpha_diss_fast
            left
            pause 0.2
            limb_images + 'sprites/uv_mimi_4.png' with limb_alpha_diss_fast
            left
            pause 0.05
            limb_images + 'sprites/uv_mimi_5.png' with limb_alpha_diss_fast
            left
            pause 0.3
            limb_images + 'sprites/uv_mimi_4.png' with limb_alpha_diss_fast
            left
            pause 0.05
            limb_images + 'sprites/uv_mimi_3.png' with limb_alpha_diss_fast
            left
            pause 0.2
            limb_images + 'sprites/uv_mimi_2.png' with limb_alpha_diss_fast
            left
            pause 0.05
            repeat

    image pl_dv_invers = im.MatrixColor(im.Composite((630,1080), (0,0), "images/sprites/far/dv/dv_4_body.png",(0,0), "images/sprites/far/dv/dv_4_pioneer.png",(0,0), "images/sprites/far/dv/dv_4_laugh.png"), im.matrix.invert())
    image pl_mi_invers = im.MatrixColor(im.Composite((630,1080), (0,0), "images/sprites/far/mi/mi_2_body.png",(0,0), "images/sprites/far/mi/mi_2_pioneer.png",(0,0), "images/sprites/far/mi/mi_2_smile.png"), im.matrix.invert())
    image pl_mt_invers = im.MatrixColor(im.Composite((1050,1080), (0,0), "images/sprites/close/mt/mt_1_body.png",(0,0), "images/sprites/close/mt/mt_1_pioneer.png",(0,0), "images/sprites/close/mt/mt_1_smile.png"), im.matrix.invert())

    image pl_mt_dark_1 = im.MatrixColor(im.Composite((1050,1080), (0,0), "images/sprites/close/mt/mt_1_body.png",(0,0), "images/sprites/close/mt/mt_1_pioneer.png",(0,0), "images/sprites/close/mt/mt_1_smile.png"), im.matrix.tint(0, 0, 0))
    image pl_mt_dark_2:
        'mt smile pioneer close'
        pause 10
        'pl_mt_dark_1' with Dissolve(5)

    image pl_sl_angry_swim = im.MatrixColor(im.Composite((1050,1080), (0,0), "images/sprites/close/sl/sl_3_body.png",(0,0), "images/sprites/close/sl/sl_3_swim.png",(0,0), "images/sprites/close/sl/sl_3_angry.png",(0,0), limb_images+"sprites/queen_eyes_close_1.png"),im.matrix.tint(0.63, 0.78, 0.82))
    image pl_sl_sad_swim = im.MatrixColor(im.Composite((1050,1080), (0,0), "images/sprites/close/sl/sl_3_body.png",(0,0), "images/sprites/close/sl/sl_3_swim.png",(0,0), "images/sprites/close/sl/sl_3_sad.png",(0,0), limb_images+"sprites/queen_eyes_close_1.png"),im.matrix.tint(0.63, 0.78, 0.82))
    image pl_sl_smile2_swim = im.MatrixColor(im.Composite((1050,1080), (0,0), "images/sprites/close/sl/sl_2_body.png",(0,0), "images/sprites/close/sl/sl_2_swim.png",(0,0), "images/sprites/close/sl/sl_2_smile2.png",(0,0), limb_images+"sprites/queen_eyes_close_2.png"),im.matrix.tint(0.63, 0.78, 0.82))
    image pl_sl_surprise_swim = im.MatrixColor(im.Composite((1050,1080), (0,0), "images/sprites/close/sl/sl_3_body.png",(0,0), "images/sprites/close/sl/sl_3_swim.png",(0,0), "images/sprites/close/sl/sl_3_surprise.png",(0,0), limb_images+"sprites/queen_eyes_close_1.png"),im.matrix.tint(0.63, 0.78, 0.82))

    image pl_el_body = im.Composite((1050,1080), (0,0), "images/sprites/far/el/el_2_body.png",(0,0), "images/sprites/far/el/el_2_shocked.png")

    image LNOOO = ParameterizedText(style = "limb_NOOO")
    image Limb_laugh = ParameterizedText(style = "limb_NOOO")
    image LRUUUN = ParameterizedText(style = "limb_RUUUN")
    image LRL_1 = ParameterizedText(style = "limb_ReLife")
    image LRL_2 = ParameterizedText(style = "limb_ReLife")
    image LRL_3 = ParameterizedText(style = "limb_ReLife")
    image LRL_4 = ParameterizedText(style = "limb_ReLife")
    image LRL_5 = ParameterizedText(style = "limb_ReLife")
    image LRL_6 = ParameterizedText(style = "limb_ReLife")
    image LRL_7 = ParameterizedText(style = "limb_ReLife")
    image LRL_8 = ParameterizedText(style = "limb_ReLife")
    image LRL_9 = ParameterizedText(style = "limb_ReLife")
    image LRL_10 = ParameterizedText(style = "limb_ReLife")
    image LRL_11 = ParameterizedText(style = "limb_ReLife")
    image LRL_12 = ParameterizedText(style = "limb_ReLife")
    image LRL_13 = ParameterizedText(style = "limb_ReLife")
    image LRL_14 = ParameterizedText(style = "limb_ReLife")
    image LRL_15 = ParameterizedText(style = "limb_ReLife")
    image LTEXT = ParameterizedText(style = "screen_limb")

    image anim ReLife:
        contains:
            'bg black'
            'ext_beach_night' with limb_noise
            anchor (0.5, 0.5)
            pos (0.5, 0.5)
            zoom 1
        contains:
            'cg d1_grasshopper'
            anchor (0.5, 0.5)
            pos (0.32, 0.27)
            zoom 0.14
            ease 3 pos (0.5, 0.5) zoom 0
        contains:
            pause 0.3
            'cg d1_sl_dinner'
            anchor (0.5, 0.5)
            pos (0.78, 0.31)
            zoom 0.155
            ease 3 pos (0.5, 0.5) zoom 0
        contains:
            pause 0.6
            'cg d1_uv_2'
            anchor (0.5, 0.5)
            pos (0.41, 0.82)
            zoom 0.143
            ease 3 pos (0.5, 0.5) zoom 0
        contains:
            pause 0.6
            'LRL_1 RLT_1'
            anchor (0.5, 0.5)
            pos (0.57, 0.83)
            zoom 1
            ease 3 pos (0.5, 0.5) zoom 0
        contains:
            pause 0.9
            'cg d2_lineup'
            anchor (0.5, 0.5)
            pos (0.89, 0.65)
            zoom 0.119
            ease 3 pos (0.5, 0.5) zoom 0
        contains:
            pause 1.2
            'cg d2_micu_lib'
            anchor (0.5, 0.5)
            pos (0.24, 0.46)
            zoom 0.179
            ease 3 pos (0.5, 0.5) zoom 0
        contains:
            pause 1.5
            'cg d2_miku_piano'
            anchor (0.5, 0.5)
            pos (0.64, 0.23)
            zoom 0.181
            ease 3 pos (0.5, 0.5) zoom 0
        contains:
            pause 1.5
            'LRL_2 RLT_2'
            anchor (0.5, 0.5)
            pos (0.26, 0.23)
            zoom 1
            ease 3 pos (0.5, 0.5) zoom 0
        contains:
            pause 1.8
            'cg d2_mirror'
            anchor (0.5, 0.5)
            pos (0.1, 0.34)
            zoom 0.113
            ease 3 pos (0.5, 0.5) zoom 0
        contains:
            pause 2.1
            'cg d2_sovenok'
            anchor (0.5, 0.5)
            pos (0.72, 0.72)
            zoom 0.1
            ease 3 pos (0.5, 0.5) zoom 0
        contains:
            pause 2.4
            'cg d2_water_dan'
            anchor (0.5, 0.5)
            pos (0.43, 0.94)
            zoom 0.156
            ease 3 pos (0.5, 0.5) zoom 0
        contains:
            pause 2.4
            'LRL_3 RLT_3'
            anchor (0.5, 0.5)
            pos (0.91, 0.12)
            zoom 1
            ease 3 pos (0.5, 0.5) zoom 0
        contains:
            pause 2.7
            'cg d3_disco'
            anchor (0.5, 0.5)
            pos (0.59, 0.63)
            zoom 0.189
            ease 3 pos (0.5, 0.5) zoom 0
        contains:
            pause 3
            'cg d3_dv_scene_2'
            anchor (0.5, 0.5)
            pos (0.23, 0.39)
            zoom 0.176
            ease 3 pos (0.5, 0.5) zoom 0
        contains:
            pause 3.3
            'cg d3_sl_dance'
            anchor (0.5, 0.5)
            pos (0.87, 0.23)
            zoom 0.148
            ease 3 pos (0.5, 0.5) zoom 0
        contains:
            pause 3.3
            'LRL_4 RLT_4'
            anchor (0.5, 0.5)
            pos (0.12, 0.46)
            zoom 1
            ease 3 pos (0.5, 0.5) zoom 0
        contains:
            pause 3.6
            'cg d3_sl_library'
            anchor (0.5, 0.5)
            pos (0.32, 0.27)
            zoom 0.138
            ease 3 pos (0.5, 0.5) zoom 0
        contains:
            pause 3.9
            'cg d3_soccer'
            anchor (0.5, 0.5)
            pos (0.72, 0.72)
            zoom 0.162
            ease 3 pos (0.5, 0.5) zoom 0
        contains:
            pause 4.2
            'cg d3_un_dance'
            anchor (0.5, 0.5)
            pos (0.87, 0.23)
            zoom 0.184
            ease 3 pos (0.5, 0.5) zoom 0
        contains:
            pause 4.2
            'LRL_5 RLT_5'
            anchor (0.5, 0.5)
            pos (0.723, 0.63)
            zoom 1
            ease 3 pos (0.5, 0.5) zoom 0
        contains:
            pause 4.5
            'cg d3_un_forest'
            anchor (0.5, 0.5)
            pos (0.1, 0.34)
            zoom 0.187
            ease 3 pos (0.5, 0.5) zoom 0
        contains:
            pause 4.8
            'cg d3_us_dinner'
            anchor (0.5, 0.5)
            pos (0.41, 0.82)
            zoom 0.126
            ease 3 pos (0.5, 0.5) zoom 0
        contains:
            pause 5.1
            'cg d3_us_library_1'
            anchor (0.5, 0.5)
            pos (0.24, 0.46)
            zoom 0.132
            ease 3 pos (0.5, 0.5) zoom 0
        contains:
            pause 5.1
            'LRL_6 RLT_6'
            anchor (0.5, 0.5)
            pos (0.45, 0.74)
            zoom 1
            ease 3 pos (0.5, 0.5) zoom 0
        contains:
            pause 5.4
            'cg d3_us_library_2'
            anchor (0.5, 0.5)
            pos (0.89, 0.65)
            zoom 0.153
            ease 3 pos (0.5, 0.5) zoom 0
        contains:
            pause 5.7
            'cg d3_ussr_catched'
            anchor (0.5, 0.5)
            pos (0.64, 0.23)
            zoom 0.111
            ease 3 pos (0.5, 0.5) zoom 0
        contains:
            pause 6
            'cg d4_catac'
            anchor (0.5, 0.5)
            pos (0.32, 0.27)
            zoom 0.143
            ease 3 pos (0.5, 0.5) zoom 0
        contains:
            pause 6
            'LRL_7 RLT_7'
            anchor (0.5, 0.5)
            pos (0.9, 0.9)
            zoom 1
            ease 3 pos (0.5, 0.5) zoom 0
        contains:
            pause 6.3
            'cg d4_dv_mt'
            anchor (0.5, 0.5)
            pos (0.1, 0.34)
            zoom 0.173
            ease 3 pos (0.5, 0.5) zoom 0
        contains:
            pause 6.6
            'cg d4_mi_guitar'
            anchor (0.5, 0.5)
            pos (0.72, 0.72)
            zoom 0.163
            ease 3 pos (0.5, 0.5) zoom 0
        contains:
            pause 6.9
            'cg d4_sh_sit'
            anchor (0.5, 0.5)
            pos (0.23, 0.39)
            zoom 0.124
            ease 3 pos (0.5, 0.5) zoom 0
        contains:
            pause 6.9
            'LRL_8 RLT_8'
            anchor (0.5, 0.5)
            pos (0.21, 0.15)
            zoom 1
            ease 3 pos (0.5, 0.5) zoom 0
        contains:
            pause 7.2
            'cg d4_us_cancer'
            anchor (0.5, 0.5)
            pos (0.41, 0.82)
            zoom 0.197
            ease 3 pos (0.5, 0.5) zoom 0
        contains:
            pause 7.5
            'cg d4_uv'
            anchor (0.5, 0.5)
            pos (0.1, 0.34)
            zoom 0.107
            ease 3 pos (0.5, 0.5) zoom 0
        contains:
            pause 7.8
            'cg d5_boat'
            anchor (0.5, 0.5)
            pos (0.32, 0.27)
            zoom 0.1
            ease 3 pos (0.5, 0.5) zoom 0
        contains:
            pause 8.1
            'cg d5_cake'
            anchor (0.5, 0.5)
            pos (0.24, 0.46)
            zoom 0.134
            ease 3 pos (0.5, 0.5) zoom 0
        contains:
            pause 8.1
            'LRL_9 RLT_9'
            anchor (0.5, 0.5)
            pos (0.69, 0.47)
            zoom 1
            ease 3 pos (0.5, 0.5) zoom 0
        contains:
            pause 8.4
            'cg d5_clubs_robot'
            anchor (0.5, 0.5)
            pos (0.41, 0.82)
            zoom 0.164
            ease 3 pos (0.5, 0.5) zoom 0
        contains:
            pause 8.7
            'cg d5_cs'
            anchor (0.5, 0.5)
            pos (0.78, 0.31)
            zoom 0.184
            ease 3 pos (0.5, 0.5) zoom 0
        contains:
            pause 9
            'cg d5_dv_argue_2'
            anchor (0.5, 0.5)
            pos (0.43, 0.94)
            zoom 0.103
            ease 3 pos (0.5, 0.5) zoom 0
        contains:
            pause 9.3
            'cg d5_dv_island'
            anchor (0.5, 0.5)
            pos (0.24, 0.46)
            zoom 0.192
            ease 3 pos (0.5, 0.5) zoom 0
        contains:
            pause 9.3
            'LRL_10 RLT_10'
            anchor (0.5, 0.5)
            pos (0.35, 0.72)
            zoom 1
            ease 3 pos (0.5, 0.5) zoom 0
        contains:
            pause 9.6
            'cg d5_dv_us_wash_2'
            anchor (0.5, 0.5)
            pos (0.59, 0.63)
            zoom 0.139
            ease 3 pos (0.5, 0.5) zoom 0
        contains:
            pause 9.9
            'cg d5_dv_us_wash_3'
            anchor (0.5, 0.5)
            pos (0.78, 0.31)
            zoom 0.156
            ease 3 pos (0.5, 0.5) zoom 0
        contains:
            pause 10.2
            'cg d5_dv_us_wash_4'
            anchor (0.5, 0.5)
            pos (0.87, 0.23)
            zoom 0.2
            ease 3 pos (0.5, 0.5) zoom 0
        contains:
            pause 10.5
            'cg d5_mi'
            anchor (0.5, 0.5)
            pos (0.43, 0.94)
            zoom 0.173
            ease 3 pos (0.5, 0.5) zoom 0
        contains:
            pause 10.5
            'LRL_11 RLT_11'
            anchor (0.5, 0.5)
            pos (0.58, 0.87)
            zoom 1
            ease 3 pos (0.5, 0.5) zoom 0
        contains:
            pause 10.8
            'cg d5_sh_us'
            anchor (0.5, 0.5)
            pos (0.23, 0.39)
            zoom 0.167
            ease 3 pos (0.5, 0.5) zoom 0
        contains:
            pause 11.1
            'cg d5_sl_sleep'
            anchor (0.5, 0.5)
            pos (0.89, 0.65)
            zoom 0.186
            ease 3 pos (0.5, 0.5) zoom 0
        contains:
            pause 11.4
            'cg d5_un_island'
            anchor (0.5, 0.5)
            pos (0.64, 0.23)
            zoom 0.17
            ease 3 pos (0.5, 0.5) zoom 0
        contains:
            pause 11.7
            'cg d5_un_sleep'
            anchor (0.5, 0.5)
            pos (0.32, 0.27)
            zoom 0.104
            ease 3 pos (0.5, 0.5) zoom 0
        contains:
            pause 11.7
            'LRL_12 RLT_12'
            anchor (0.5, 0.5)
            pos (0.32, 0.276)
            zoom 1
            ease 3 pos (0.5, 0.5) zoom 0
        contains:
            pause 12
            'cg d5_us_ghost'
            anchor (0.5, 0.5)
            pos (0.41, 0.82)
            zoom 0.194
            ease 3 pos (0.5, 0.5) zoom 0
        contains:
            pause 12.3
            'cg d5_us_ghost_2'
            anchor (0.5, 0.5)
            pos (0.1, 0.34)
            zoom 0.147
            ease 3 pos (0.5, 0.5) zoom 0
        contains:
            pause 12.6
            'cg d5_us_kiss'
            anchor (0.5, 0.5)
            pos (0.78, 0.31)
            zoom 0.184
            ease 3 pos (0.5, 0.5) zoom 0
        contains:
            pause 12.9
            'cg d5_uv_2'
            anchor (0.5, 0.5)
            pos (0.24, 0.46)
            zoom 0.1
            ease 3 pos (0.5, 0.5) zoom 0
        contains:
            pause 13.2
            'cg d6_sl_forest'
            anchor (0.5, 0.5)
            pos (0.59, 0.63)
            zoom 0.157
            ease 3 pos (0.5, 0.5) zoom 0
        contains:
            pause 13.2
            'LRL_13 RLT_13'
            anchor (0.5, 0.5)
            pos (0.43, 0.84)
            zoom 1
            ease 3 pos (0.5, 0.5) zoom 0
        contains:
            pause 13.5
            'cg d6_un_evening_1'
            anchor (0.5, 0.5)
            pos (0.43, 0.94)
            zoom 0.154
            ease 3 pos (0.5, 0.5) zoom 0
        contains:
            pause 13.8
            'cg d6_uv_2'
            anchor (0.5, 0.5)
            pos (0.72, 0.72)
            zoom 0.171
            ease 3 pos (0.5, 0.5) zoom 0
        contains:
            pause 14.1
            'cg d7_dv'
            anchor (0.5, 0.5)
            pos (0.1, 0.34)
            zoom 0.14
            ease 3 pos (0.5, 0.5) zoom 0
        contains:
            pause 14.4
            'cg d7_dv_2'
            anchor (0.5, 0.5)
            pos (0.89, 0.65)
            zoom 0.102
            ease 3 pos (0.5, 0.5) zoom 0
        contains:
            pause 14.4
            'LRL_14 RLT_14'
            anchor (0.5, 0.5)
            pos (0.76, 0.45)
            zoom 1
            ease 3 pos (0.5, 0.5) zoom 0
        contains:
            pause 14.7
            'cg d7_pioneers_leaving'
            anchor (0.5, 0.5)
            pos (0.64, 0.23)
            zoom 0.183
            ease 3 pos (0.5, 0.5) zoom 0
        contains:
            pause 15
            'cg epilogue_mi_1'
            anchor (0.5, 0.5)
            pos (0.32, 0.27)
            zoom 0.193
            ease 3 pos (0.5, 0.5) zoom 0
        contains:
            pause 15.3
            'cg epilogue_dv_2'
            anchor (0.5, 0.5)
            pos (0.78, 0.31)
            zoom 0.149
            ease 3 pos (0.5, 0.5) zoom 0
        contains:
            pause 15.6
            'cg epilogue_sl_2'
            anchor (0.5, 0.5)
            pos (0.24, 0.46)
            zoom 0.124
            ease 3 pos (0.5, 0.5) zoom 0
        contains:
            pause 15.6
            'LRL_15 RLT_15'
            anchor (0.5, 0.5)
            pos (0.37, 0.24)
            zoom 1
            ease 3 pos (0.5, 0.5) zoom 0
        contains:
            pause 15.9
            'cg final_all_2'
            anchor (0.5, 0.5)
            pos (0.41, 0.82)
            zoom 0.173
            ease 3 pos (0.5, 0.5) zoom 0
        contains:
            'us smile sport'
            anchor (0.5, 0.5)
            pos (0.1, 0.5)
            zoom 1
            alpha 0
            parallel:
                ease 1.8 pos (0.5, 0.5) alpha 0.8
            parallel:
                pause 1.95
                ease 1.8 pos (0.9, 0.5) alpha 0
        contains:
            pause 3.5
            'mi smile pioneer'
            anchor (0.5, 0.5)
            pos (0.9, 0.5)
            zoom 1
            alpha 0
            parallel:
                ease 2 pos (0.5, 0.5) alpha 0.8
            parallel:
                pause 1.95
                ease 2 pos (0.1, 0.5) alpha 0
        contains:
            pause 7
            'sl smile2 pioneer'
            anchor (0.5, 0.5)
            pos (0.1, 0.5)
            zoom 1
            alpha 0
            parallel:
                ease 2 pos (0.5, 0.5) alpha 0.8
            parallel:
                pause 1.95
                ease 2 pos (0.9, 0.5) alpha 0
        contains:
            pause 10.5
            'dv guilty pioneer'
            anchor (0.5, 0.5)
            pos (0.9, 0.5)
            zoom 1
            alpha 0
            parallel:
                ease 2 pos (0.5, 0.5) alpha 0.8
            parallel:
                pause 1.95
                ease 2 pos (0.1, 0.5) alpha 0
        contains:
            pause 14
            'un cry_smile pioneer'
            anchor (0.5, 0.5)
            pos (0.1, 0.5)
            zoom 1
            alpha 0
            parallel:
                ease 2 pos (0.5, 0.5) alpha 0.8
            parallel:
                pause 1.95
                ease 2 pos (0.9, 0.5) alpha 0
        contains:
            'limb_eff_prologue_dream'

    image anim limb_auto_anim:
        'cg limb_auto_anim_1'
        pause 0.4
        'cg limb_auto_anim_2' with dissolve_fast
        pause 0.4
        'cg limb_auto_anim_3' with dissolve_fast
        pause 0.4
        'cg limb_auto_anim_4' with dissolve_fast
        pause 0.4
        'cg limb_auto_anim_5' with dissolve_fast
        pause 0.4
        'cg limb_in_auto_un' with dissolve_fast
    image anim limb_auto_pink_1:
        'cg limb_in_auto_pink_0'
        pause 0.5
        'cg limb_in_auto_pink_1' with dspr
        pause 0.3
        'cg limb_in_auto_pink_0' with dspr
        pause 0.55
        'cg limb_in_auto_pink_1' with dissolve_fast
        pause 0.55
        'cg limb_in_auto_pink_2' with dissolve_fast
        pause 0.55
        'cg limb_in_auto_pink_3' with dissolve_fast
        pause 0.55
        'cg limb_in_auto_pink_3' with limb_psycho_flash
    image anim limb_auto_pink_2:
        'cg limb_in_auto_pink_3' with dissolve_fast
        pause 0.55
        'cg limb_in_auto_pink_2' with dissolve_fast
        pause 0.55
        'cg limb_in_auto_pink_1' with dissolve_fast
        pause 0.55
        'cg limb_in_auto_pink_0' with dspr
        pause 0.35
        'cg limb_in_auto_pink_0' with dspr
        pause 0.35
        'cg limb_in_auto_pink_1' with dspr
        pause 0.5
        'cg limb_in_auto_pink_4'
    image anim limb_auto_pink_3:
        'cg limb_in_auto_pink_4'
        pause 0.5
        'cg limb_in_auto_pink_5' with dissolve2
    image anim limb_auto_end:
        contains:
            'cg limb_in_auto_end_2'
            'cg limb_in_auto_end_3' with Dissolve(16)
        contains:
            pause 16
            'limb_eff_glitch'
    image anim limb_conversion = Movie(play="mods/Limb/resourses/video/conversion_4.webm", size=(1920, 1080), pos=(0,0), anchor=(0,0))
    image anim limb_dialogue_box_410:
        limb_gui_pref + 'dialogue_box/day/dialogue_box.png'
        pause 1
        limb_gui_pref + 'dialogue_box/dialogue_box_410.png' with limb_pixel_1
        pause 1
        'gui/dialogue_box/night/dialogue_box.png' with limb_pixel_1
        anchor (0.5, 0.5)
        pos (0.504, 0.923)
        pause 1.16
        ease 0.11 alpha 0
    image anim limb_dialogue_box_broken:
        contains:
            'gui/dialogue_box/day/backward_idle.png'
            xpos 38+5
            ypos 949+5
            pause 0.5
            parallel:
                ease 2.5 rotate -360
            parallel:
                ease 1 ypos 1200 xpos 25
        contains:
            limb_gui_pref + 'dialogue_box/dialogue_box_part_1.png'
            xpos 174+5
            ypos 916+5
            pause 1
            ease 0.3 ypos 1200
        contains:
            limb_gui_pref + 'dialogue_box/dialogue_box_part_2.png'
            xpos 174+5
            ypos 916+5
            ease 0.2 ypos 945
            pause 1.3
            ease 0.3 ypos 1200
        contains:
            'gui/dialogue_box/day/hide_idle.png'
            xpos 1508+5
            ypos 933+5
            pause 0.2+0.5
            parallel:
                ease 2 rotate -90
            parallel:
                ease 0.8 ypos 1200
        contains:
            'gui/dialogue_box/day/save_idle.png'
            xpos 1567+5
            ypos 933+5
            pause 0.8+0.5
            parallel:
                ease 1.5 rotate 45
            parallel:
                ease 0.5 ypos 1200
        contains:
            'gui/dialogue_box/day/menu_idle.png'
            xpos 1625+5
            ypos 933+5
            pause 0.3+0.5
            parallel:
                ease 1.8 rotate 30
            parallel:
                ease 0.8 ypos 1200
        contains:
            'gui/dialogue_box/day/load_idle.png'
            xpos 1682+5
            ypos 933+5
            pause 0.6+0.5
            parallel:
                ease 0.4 rotate 270
            parallel:
                ease 0.4 ypos 1200
        contains:
            'gui/dialogue_box/day/forward_idle.png'
            xpos 1768+5
            ypos 949+5
            pause 0.5
            parallel:
                ease 1.5 rotate 180
            parallel:
                ease 0.9 ypos 1200
    image anim limb_dialogue_box_punch:
        contains:
            'gui/dialogue_box/day/backward_idle.png'
            xpos 38+5
            ypos 949+5
            ease 0.1 ypos 955+5
            ease 0.1 ypos 952+5
            ease 0.1 ypos 955+5
            ease 0.1 ypos 949+5
        contains:
            'gui/dialogue_box/day/dialogue_box.png'
            xpos 174+5
            ypos 916+5
            ease 0.1 ypos 922+5
            ease 0.1 ypos 919+5
            ease 0.1 ypos 922+5
            ease 0.1 ypos 916+5
        contains:
            'gui/dialogue_box/day/hide_idle.png'
            xpos 1508+5
            ypos 933+5
            ease 0.1 ypos 939+5
            ease 0.1 ypos 936+5
            ease 0.1 ypos 939+5
            ease 0.1 ypos 933+5
        contains:
            'gui/dialogue_box/day/save_idle.png'
            xpos 1567+5
            ypos 933+5
            ease 0.1 ypos 939+5
            ease 0.1 ypos 936+5
            ease 0.1 ypos 939+5
            ease 0.1 ypos 933+5
        contains:
            'gui/dialogue_box/day/menu_idle.png'
            xpos 1625+5
            ypos 933+5
            ease 0.1 ypos 939+5
            ease 0.1 ypos 936+5
            ease 0.1 ypos 939+5
            ease 0.1 ypos 933+5
        contains:
            'gui/dialogue_box/day/load_idle.png'
            xpos 1682+5
            ypos 933+5
            ease 0.1 ypos 939+5
            ease 0.1 ypos 936+5
            ease 0.1 ypos 939+5
            ease 0.1 ypos 933+5
        contains:
            'gui/dialogue_box/day/forward_idle.png'
            xpos 1768+5
            ypos 949+5
            ease 0.1 ypos 955+5
            ease 0.1 ypos 952+5
            ease 0.1 ypos 955+5
            ease 0.1 ypos 949+5
    image anim limb_flashback:
        contains:
            'bg black'
        contains:
            'cg d1_grasshopper'
            limb_slideshow
            'cg d1_sl_dinner'
            limb_slideshow
            'cg d2_micu_lib'
            limb_slideshow
            'cg d2_miku_piano'
            limb_slideshow
            'cg d2_sovenok'
            limb_slideshow
            'cg d2_water_dan'
            limb_slideshow
            'cg d3_disco'
            limb_slideshow
            'cg d3_sl_dance'
            limb_slideshow
            'cg d3_un_forest'
            limb_slideshow
            'cg d4_dv_mt'
            limb_slideshow
            'cg d4_mi_guitar'
            limb_slideshow
            'cg d4_sh_sit'
            limb_slideshow
            'cg d5_cake'
            limb_slideshow
            'cg d5_clubs_robot'
            limb_slideshow
            'cg d5_cs'
            limb_slideshow
            'cg d5_us_kiss'
            limb_slideshow
            'cg limb_all_tigether'
            limb_slideshow
            'bg black' with pixellate
    image anim limb_flashback_after:
        contains:
            contains:
                contains:
                    'bg black'
                    'bg ext_hospital_morning' with flash
                contains:
                    'bg black'
                    'pl_dv_dress_smile'
                    left
                contains:
                    'bg black'
                    'pl_moto_5'
                    limb_moto_pos
            pause 5
            contains:
                contains:
                    'bg black'
                    'bg semen_room_red' with flash
                contains:
                    'bg black'
                    'pl_un_dress_1'
            pause 5
            contains:
                'bg black'
                'bg int_kitchen_pl' with flash
            pause 5
            contains:
                contains:
                    'bg black'
                    'bg semen_room_clean' with flash
                contains:
                    'bg black'
                    'sl smile2 dress'
                    left
                contains:
                    'bg black'
                    'pl_sh_2_night'
                    right
            pause 5
            contains:
                contains:
                    'bg black'
                    'bg int_floor_day' with flash
                contains:
                    'bg black'
                    'pl_sl_slut_2'
                contains:
                    'bg black'
                    'pl_sh_miami_1'
                    xanchor 0.5
                    xpos 0.95
            pause 5
            contains:
                contains:
                    'bg black'
                    'bg semen_room_morning_clean' with flash
                contains:
                    'bg black'
                    'cs normal'
                    cleft
                contains:
                    'bg black'
                    'pl_el_man'
                    cright
            pause 5
            contains:
                contains:
                    'bg black'
                    'bg int_wardrobe' with flash
                contains:
                    'bg black'
                    'pl_dv_music_2'
                    cright
                    zoom 1.2
                contains:
                    'bg black'
                    'pl_ma_limb_2_alt'
                    left
            pause 5
            repeat
        contains:
            'prologue_dream'
    image anim limb_logo = Movie(channel="logo", play="mods/Limb/resourses/video/logo.webm", size=(1920, 1080), pos=(0,0), anchor=(0,0))
    image anim limb_safe:
        'cg limb_safe_1'
        pause 1
        'cg limb_safe_2'
        pause 1
        'cg limb_safe_3'
        pause 1
        'cg limb_safe_4'
        pause 1
        repeat
    image anim limb_space:
        'bg space_pl_1' with Dissolve(5)
        pause 5
        'bg space_pl_2' with Dissolve(5)
        pause 5
        repeat
    image anim limb_psycho_spiral:
        'pl_spiral_14'
        anchor (0.5, 0.5)
        pos (0.85, 0.723)
        zoom 1
        parallel:
            ease 40 rotate 8640
            repeat
        parallel:
            ease 20 zoom 2
    image anim limb_psycho_city:
        contains:
            'bg ext_city_psycho'
            anchor (0.5, 0.5)
            align (0.5, 0.5)
            zoom 1
            parallel:
                ease 20 zoom 2
            parallel:
                ease 20 xalign 0.85 yalign 0.723
        contains:
            'anim limb_psycho_spiral'

    image limb_scary_laugh:
        contains:
            'Limb_laugh LLaugh_text'
            anchor (0.5, 0.5)
            pos (renpy.random.randint(100,1820), renpy.random.randint(100,980))
        contains:
            pause 1
            'Limb_laugh LLaugh_text'
            anchor (0.5, 0.5)
            pos (renpy.random.randint(100,1820), renpy.random.randint(100,980))
        contains:
            pause 2.5
            'Limb_laugh LLaugh_text'
            anchor (0.5, 0.5)
            pos (renpy.random.randint(100,1820), renpy.random.randint(100,980))
        contains:
            pause 4
            'Limb_laugh LLaugh_text'
            anchor (0.5, 0.5)
            pos (renpy.random.randint(100,1820), renpy.random.randint(100,980))
        contains:
            pause 5.5
            'Limb_laugh LLaugh_text'
            anchor (0.5, 0.5)
            pos (renpy.random.randint(100,1820), renpy.random.randint(100,980))
        contains:
            pause 7
            'Limb_laugh LLaugh_text'
            anchor (0.5, 0.5)
            pos (renpy.random.randint(100,1820), renpy.random.randint(100,980))
        contains:
            pause 8.5
            'Limb_laugh LLaugh_text'
            anchor (0.5, 0.5)
            pos (renpy.random.randint(100,1820), renpy.random.randint(100,980))
        contains:
            pause 10
            'Limb_laugh LLaugh_text'
            anchor (0.5, 0.5)
            pos (renpy.random.randint(100,1820), renpy.random.randint(100,980))
        contains:
            pause 11.5
            'Limb_laugh LLaugh_text'
            anchor (0.5, 0.5)
            pos (renpy.random.randint(100,1820), renpy.random.randint(100,980))
        contains:
            pause 13
            'Limb_laugh LLaugh_text'
            anchor (0.5, 0.5)
            pos (renpy.random.randint(100,1820), renpy.random.randint(100,980))
        contains:
            pause 14.5
            'Limb_laugh LLaugh_text'
            anchor (0.5, 0.5)
            pos (renpy.random.randint(100,1820), renpy.random.randint(100,980))
        contains:
            pause 16
            'Limb_laugh LLaugh_text'
            anchor (0.5, 0.5)
            pos (renpy.random.randint(100,1820), renpy.random.randint(100,980))
        contains:
            pause 17.5
            'Limb_laugh LLaugh_text'
            anchor (0.5, 0.5)
            pos (renpy.random.randint(100,1820), renpy.random.randint(100,980))
        contains:
            pause 19
            'Limb_laugh LLaugh_text'
            anchor (0.5, 0.5)
            pos (renpy.random.randint(100,1820), renpy.random.randint(100,980))
        contains:
            pause 20.5
            'Limb_laugh LLaugh_text'
            anchor (0.5, 0.5)
            pos (renpy.random.randint(100,1820), renpy.random.randint(100,980))
        contains:
            pause 22
            'Limb_laugh LLaugh_text'
            anchor (0.5, 0.5)
            pos (renpy.random.randint(100,1820), renpy.random.randint(100,980))
        contains:
            pause 23.5
            'Limb_laugh LLaugh_text'
            anchor (0.5, 0.5)
            pos (renpy.random.randint(100,1820), renpy.random.randint(100,980))
        contains:
            pause 25
            'Limb_laugh LLaugh_text'
            anchor (0.5, 0.5)
            pos (renpy.random.randint(100,1820), renpy.random.randint(100,980))
        contains:
            pause 26.5
            'Limb_laugh LLaugh_text'
            anchor (0.5, 0.5)
            pos (renpy.random.randint(100,1820), renpy.random.randint(100,980))
        contains:
            pause 28
            'Limb_laugh LLaugh_text'
            anchor (0.5, 0.5)
            pos (renpy.random.randint(100,1820), renpy.random.randint(100,980))
        contains:
            pause 29.5
            'Limb_laugh LLaugh_text'
            anchor (0.5, 0.5)
            pos (renpy.random.randint(100,1820), renpy.random.randint(100,980))
    image limb_RUN:
        'LRUUUN LRed_text'
        zoom 1 align (0.5, 0.5) alpha 1
        ease 0.5 zoom 1.2
        ease 0.5 zoom 1
        ease 0.5 zoom 1.2
        ease 0.5 zoom 1
        ease 0.5 alpha 0
        'bg ext_path_war' with dissolve
        alpha 1
        limb_running

    image bg bus_stop_flash:
        'bg bus_stop'
        pause 7
        'bg bus_stop' with limb_flash
    image bg ext_beach_darken:
        'bg ext_beach_sunset'
        'bg ext_beach_night' with Dissolve(10)
    image bg ext_beach_night_people:
        contains:
            'bg ext_beach_campfire_pl'
            xalign 0.5 yalign 0.5 zoom 1
            ease 3 yalign 0.7 xalign 0.25 zoom 1.2
        contains:
            'uv laugh'
            alpha 0
            pause 2
            anchor (0.5, 0.5)
            pos (0.7, 0.65)
            ease 4 alpha 1
        contains:
            'pi far'
            alpha 0
            pause 2
            anchor (0.5, 0.5)
            pos (0.15, 0.65)
            ease 4 alpha 1
    image bg ext_camp_entrance_dark:
        contains:
            'bg ext_camp_entrance_dark_1'
            pause 2
            'bg ext_camp_entrance_dark_2' with Dissolve(10)
        contains:
            'limb_eff_prologue_dream'
    image bg ext_camp_entrance_fall:
        contains:
            'bg black'
        contains:
            'bg ext_camp_entrance_day'
            anchor (0.5, 0.5)
            pos (0.5, 0.5)
            xzoom -0.2 yzoom 0.2
            ease 1 xzoom -1 yzoom 1
    image bg ext_camp_entrance_mars_thunder:
        'bg ext_camp_entrance_mars'
        pause 3
        'bg ext_camp_entrance_dark_2'
        pause 0.05
        'bg ext_camp_entrance_dark_2' with flash
        pause 0.6
        'bg ext_camp_entrance_mars'
    image bg ext_camp_entrance_conversion:
        contains:
            'bg ext_camp_entrance_day'
            anchor (0.5, 0.5)
            align (0.5, 0.5)
            zoom 1
            ease 2 zoom 1.5
        contains:
            'bg ext_clubs_day'
            anchor (0.5, 0.5)
            align (0.5, 0.5)
            alpha 0
            pause 1
            ease 1 alpha 0.5
    image bg ext_camp_entrance_sin:
        contains:
            'bg ext_camp_entrance_dark_1'
            pause 2
            'bg ext_camp_entrance_mars' with Dissolve(15)
        contains:
            'limb_eff_prologue_dream'
    image bg ext_city_dv:
        contains:
            'bg ext_city_house_day'
        contains:
            'pl_dv_dress_normal'
            cright
    image bg ext_city_house_future:
        'bg ext_city_house_future_1'
        pause 1
        'bg ext_city_house_future_2'
        pause 1
        repeat
    image bg ext_fog_4:
        'bg ext_fog_2' with dissolve2
        pause 2
        'bg ext_fog_3' with dissolve2
        pause 2
        repeat
    image bg ext_fog_city:
        'bg black'
        'bg ext_road_fog_2' with Dissolve(10)
    image bg ext_hospital_darken:
        contains:
            'bg ext_hospital_sunset_2'
            'bg ext_hospital_night' with Dissolve(10)
        contains:
            'pl_moto_1_sunset'
            anchor (0.5, 0.5)
            pos (0.5, 0.6)
            'pl_moto_2' with Dissolve(10, alpha=True)
    image bg ext_hotline:
        'bg ext_road_sunset_pl'
        'bg ext_road_night' with Dissolve(24)
        pause 24
        'bg ext_road_night_auto' with Dissolve(14)
        pause 14
        'bg ext_road_moto_1' with Dissolve(9)
        pause 9
        'bg black' with Dissolve(7)
        pause 7
    image bg ext_house_of_mt_fog:
        contains:
            'bg ext_fog_4'
        contains:
            'bg ext_house_of_mt_night'
            alpha 0
            linear 10 alpha 0.5
    image bg ext_island_invers = im.MatrixColor(limb_images + "bg/ext_island_samsebecoder.jpg",im.matrix.invert())
    image bg ext_old_building_fog_1:
        'bg ext_old_building_night'
        pause 3
        'bg ext_fog_2' with Dissolve(10)
    image bg ext_old_building_fog_2:
        contains:
            'bg ext_fog_2'
        contains:
            'bg ext_old_building_night'
            alpha 0.5
    image bg ext_path_evening:
        'bg ext_path_day'
        'bg ext_path_sunset' with Dissolve(8)
    image bg ext_road_ending:
        'bg ext_road_moto_1'
        pause 5
        'bg ext_fog_2' with Dissolve(20)
    image bg ext_road_evening:
        'bg ext_road_day'
        'bg ext_road_sunset' with Dissolve(15)
    image bg ext_road_darken:
        'bg ext_road_sunset'
        'bg ext_road_night' with Dissolve(15)
    image bg ext_sea_night_fade:
        'bg ext_sea_night_pl'
        'bg black' with Dissolve(5)
    image bg ext_stage_normal_invers = im.MatrixColor("images/bg/ext_stage_normal_day.jpg",im.matrix.invert())
    image bg ext_underwater_sin = im.Grayscale(limb_images + "bg/ext_underwater.jpg")
    image bg ext_underwater_sin_dark = im.MatrixColor(im.Grayscale(limb_images + "bg/ext_underwater.jpg"), im.matrix.tint(0.3, 0.3, 0.3))
    image bg ext_underwater_red = im.Recolor(limb_images + "bg/ext_underwater.jpg", 255, 0, 0, 255)
    image bg ext_underwater_red_darken:
        'bg ext_underwater_red'
        'bg black' with Dissolve(30)
    image bg int_aidpost_day_people:
        contains:
            'int_aidpost_day'
        contains:
            'pl_sl_slut_1'
    image bg int_auto_fog:
        'bg int_auto_fog_1'
        pause 1
        'bg int_auto_fog_2' with Dissolve(30)
    image bg int_catacombs_entrance_gray:
        'bg int_catacombs_entrance'
        im.Grayscale("images/bg/int_catacombs_entrance.jpg") with Dissolve(10)
    image bg int_catacombs_entrance_transition:
        im.Grayscale("images/bg/int_catacombs_entrance.jpg")
        'bg int_limb_directors_cut' with Dissolve(30.0)
    image bg int_catacombs_future_blink:
        'bg int_catacombs_future_0'
        pause 0.2
        'bg int_catacombs_future_1'
        pause 0.2
        repeat
    image bg int_catacombs_future:
        'bg int_catacombs_future_blink'
        pause 2
        'bg int_catacombs_future_1'
    image bg int_catacombs_invers = im.MatrixColor(limb_images + "bg/int_catacombs_future_1.jpg",im.matrix.invert())
    image bg int_corridor_sin = im.Grayscale(limb_images + "bg/int_corridor_pl.jpg")
    image bg int_dining_hall_people_evening:
        'bg int_dining_hall_people_day_pl'
        'bg int_dining_hall_people_sunset_pl' with Dissolve(20)
    image bg int_door_sin = im.Grayscale(limb_images + "bg/int_door_pl.jpg")
    image bg int_floor_invers = im.MatrixColor(limb_images + "bg/int_floor_night.png",im.matrix.invert())
    image bg int_floor_sin = im.Grayscale(limb_images + "bg/int_floor_night.png")
    image bg int_floor_sin_cat:
        contains:
            'bg int_floor_sin'
        contains:
            'pl_kuroneko_1'
            anchor (0.5, 0.5)
            align (0.5, 0.65)
            zoom 1.2
    image bg int_house_of_mt_awake:
        'bg int_house_of_mt_blur'
        anchor (0.5, 0.5)
        pos (0.5, 0.5)
        zoom 2
        rotate 90
        ease 5 rotate 0
        ease 1.5 zoom 1.3
        ease 1.5 zoom 1.6
        ease 1.5 zoom 1.2
        ease 1 zoom 1
        'bg int_house_of_mt_day' with dissolve2
    image bg int_house_of_mt_gray_1 = im.Grayscale("images/bg/int_house_of_mt_day.jpg")
    image bg int_house_of_mt_gray_2:
        'bg image bg int_house_of_mt_day'
        pause 5
        'bg image bg int_house_of_mt_gray_1' with Dissolve(5)
    image bg int_kitchen_dark_blink:
        'bg int_kitchen_dark_1'
        pause 1.5
        'bg int_kitchen_dark_2'
        pause 0.3
        'bg int_kitchen_dark_1'
        pause 10
        repeat
    image bg int_kitchen_dark_kodomo:
        'bg int_kitchen_dark_blink'
        align (0.5, 0.5)
        ease 10 yalign 1.0 zoom 1.5
    image bg int_mine_backdoor_gray = im.Grayscale(limb_images + "bg/int_mine_backdoor.jpg")
    image bg int_mine_backdoor_fade:
        'bg int_mine_backdoor_gray'
        'bg black' with Dissolve(20)
    image bg int_mine_baw:
        'bg int_mine'
        im.Grayscale("images/bg/int_mine.jpg") with Dissolve(5)
    image bg int_mine_green:
        'bg int_mine'
        im.Recolor("images/bg/int_mine.jpg", 25, 255, 25, 255) with Dissolve(5)
    image bg int_mine_pink:
        'bg int_mine'
        im.Recolor("images/bg/int_mine.jpg", 255, 150, 255, 255) with Dissolve(5)
    image bg int_mirror_baw = im.Grayscale(limb_images + "bg/int_mirror_night.jpg")
    image bg int_mirror_glass:
        contains:
            'bg black'
        contains:
            'prologue_dream'
            truecenter
        contains:
            im.Grayscale(limb_images+ "bg/int_wonderland_1.png")
    image bg int_mirror_war_pi:
        contains:
            'bg black'
        contains:
            im.Sepia(limb_images+'/sprites/pi_full.png')
            anchor (0.5, 0.5)
            pos (0.418, 0.56)
            zoom 0.23
        contains:
            'prologue_dream'
            truecenter
        contains:
            'bg int_mirror_war'
    image bg int_old_building_sepia_1 = im.Sepia(im.MatrixColor('images/bg/int_old_building_night.jpg', im.matrix.tint(0.4, 0.4, 0.4)))
    image bg int_old_building_sepia_2:
        'bg int_old_building_night'
        'bg int_old_building_sepia_1' with Dissolve(10)
    image bg int_old_building_table:
        'bg black'
        'bg int_old_building_night' with Dissolve(10)
        align (0.75, 0.75)
        zoom 1.5
    image bg int_old_building_red = im.Recolor("images/bg/int_old_building_night.jpg", 255, 0, 0, 255)
    image bg int_old_building_red_vamp:
        contains:
            'bg int_old_building_red'
            align (0.75, 0.75)
            zoom 1.5
        contains:
            'pl_mi_vamp_red'
            right
        contains:
            'pl_dv_vamp_normal_red'
            center
        contains:
            'pl_sl_vamp_red'
            xalign -0.08 zoom 1.5
    image bg int_old_building_vamp_1:
        contains:
            'bg int_old_building_table'
        contains:
            'pl_mi_vamp_not_smile'
            right
        contains:
            'pl_dv_vamp_normal'
            center
        contains:
            'pl_sl_vamp_smile'
            xalign -0.08 zoom 1.5
    image bg int_old_building_vamp_2:
        'bg int_old_building_vamp_1'
        'bg int_old_building_red_vamp' with Dissolve(15)
    image bg int_table_baw = im.Grayscale(limb_images + "bg/int_table_pl_1.jpg")
    image bg int_wonderland:
        contains:
            'bg black'
        contains:
            'bg int_wonderland_1'
    image bg int_wonderland_lighten:
        'bg black'
        'bg int_wonderland' with Dissolve(7)
    image bg int_wonderland_pi:
        contains:
            'bg black'
        contains:
            'pl_pi_full'
            anchor (0.5, 0.5)
            pos (0.418, 0.56)
            zoom 0.23
        contains:
            'prologue_dream'
            truecenter
        contains:
            'bg int_wonderland_1'
    image bg red = '#FF3200'
    image bg semen_room_alco:
        contains:
            'bg semen_room_pink'
            anchor (0.5, 0.5)
            pos (0.5, 0.5)
            zoom 2
            rotate 90
            ease 5 rotate 0
            ease 1.5 zoom 1.3
            ease 1.5 zoom 1.6
            ease 1.5 zoom 1.2
            ease 1 zoom 1
        contains:
            'prologue_dream'
            alpha 0
            ease 1 alpha 1
            ease 0.5 alpha 0.4
            ease 1.5 alpha 1
            pause 3
            ease 0.45 alpha 0
            pause 2
            ease 0.55 alpha 0.7
            ease 1 alpha 0
            ease 0.5 alpha 1
            pause 0.5
            ease 0.5 alpha 0.2
    image bg semen_room_baw = im.Grayscale(limb_images + "bg/semen_room_pink.jpg")
    image bg semen_room_dark = im.MatrixColor("images/bg/semen_room.jpg", im.matrix.tint(0.4, 0.4, 0.6))
    image bg semen_room_fire:
        'bg semen_room'
        'bg semen_room_red' with Dissolve(10)
    image bg semen_room_hikki:
        'bg semen_room_green'
        'bg semen_room' with Dissolve(15)
    image bg semen_room_pinked:
        'bg semen_room'
        'bg semen_room_pink' with Dissolve(5)
    image bg limb_space_start:
        'bg black'
        'anim limb_space' with Dissolve(10)

    image cg d6_sl_forest_sepia = im.Sepia("images/cg/d6_sl_forest.jpg")
    image cg epilogue_us_blur:
        'cg epilogue_us'
        pause 2
        'cg epilogue_us_alone' with Dissolve(4)
    image cg limb_auto_blinking_1:
        'cg limb_auto_fog_2'
        pause 1
        choice:
            pause 0.5
            'cg limb_auto_fog_2'
            pause 0.1
            'cg limb_auto_fog_1'
            pause 0.1
            'cg limb_auto_fog_2'
        choice:
            pause 3
            'cg limb_auto_fog_2'
            pause 0.1
            'cg limb_auto_fog_1'
            pause 0.1
            'cg limb_auto_fog_2'
        choice:
            pause 5
            'cg limb_auto_fog_2'
            pause 0.1
            'cg limb_auto_fog_1'
            pause 0.1
            'cg limb_auto_fog_2'
        choice:
            pause 9
            'cg limb_auto_fog_2'
            pause 0.1
            'cg limb_auto_fog_1'
            pause 0.1
            'cg limb_auto_fog_2'
        choice:
            pause 12
            'cg limb_auto_fog_2'
            pause 0.1
            'cg limb_auto_fog_1'
            pause 0.1
            'cg limb_auto_fog_2'
        repeat
    image cg limb_auto_blinking_2:
        'cg limb_auto_fog_2'
        pause 1
        choice:
            pause 0.5
            'cg limb_auto_fog_2'
            pause 0.1
            'cg limb_auto_fog_1'
            pause 0.1
            'cg limb_auto_fog_2'
        choice:
            pause 1
            'cg limb_auto_fog_2'
            pause 0.1
            'cg limb_auto_fog_1'
            pause 0.1
            'cg limb_auto_fog_2'
        choice:
            pause 2
            'cg limb_auto_fog_2'
            pause 0.1
            'cg limb_auto_fog_1'
            pause 0.1
            'cg limb_auto_fog_2'
        choice:
            pause 3
            'cg limb_auto_fog_2'
            pause 0.1
            'cg limb_auto_fog_1'
            pause 0.1
            'cg limb_auto_fog_2'
        repeat
    image cg limb_auto_darken:
        'cg limb_auto_dark'
        'bg black' with Dissolve(10)
    image cg limb_auto_fog_ending:
        'bg ext_fog_4'
        'cg limb_auto_fog_2' with Dissolve(75)
    image cg limb_auto_fog_horror:
        contains:
            'cg limb_auto_fog_2'
            alpha 0.5
        contains:
            'bg ext_fog_4'
    image cg limb_auto_fog_invers = im.MatrixColor(limb_images + "cg/limb_auto_fog_1.jpg", im.matrix.invert())
    image cg limb_auto_fog_kodomo:
        'сg limb_auto_fog_1_blink'
        align (0.5, 0.5)
        ease 20 yalign 0.9 zoom 1.5
    image cg limb_auto_fog_red_1 = im.Recolor(limb_images + "cg/limb_auto_fog_1.jpg", 255, 0, 0, 255)
    image cg limb_auto_fog_red_2:
        'cg limb_auto_fog_1'
        'cg limb_auto_fog_red_1' with Dissolve(10)
    image cg limb_auto_mars_darken:
        'cg limb_auto_mars'
        'cg limb_auto_dark' with Dissolve(20)
    image cg limb_doki:
        'cg limb_doki_2'
        'cg limb_doki_1' with Dissolve(30.0)
    image cg limb_fog_man_5:
        'cg limb_fog_man_2' with Dissolve(3)
        pause 3
        'cg limb_fog_man_1' with Dissolve(3)
        pause 3
        repeat
    image cg limb_game_exams_un:
        'cg limb_game_exams_3'
        'cg limb_game_exams_3_5' with Dissolve(20)
    image cg limb_hero:
        'cg limb_hero_1'
        'cg limb_hero_2' with Dissolve(5)
    image cg limb_hero_jump:
        'cg limb_hero_2'
        'cg limb_hero_3' with dissolve
        anchor (0.5, 0.5)
        pos (0.5, 0.5)
        zoom 1
        ease 1.3 zoom 2.5
        pause 0.8
        'bg black'
    image cg limb_party_1:
        'cg limb_discord_1' with limb_party_flash
        anchor (0.5, 0.5)
        pos (0.5, 0.5)
        pause 0.75
        'cg limb_discord_2' with limb_party_flash
        pause 0.75
        'cg limb_discord_3' with limb_party_flash
        pause 0.75
        repeat
    image cg limb_party_itai:
        'cg limb_party_1'
        anchor (0.5, 0.5)
        pos (0.5, 0.5)
        zoom 1
        ease 2 pos 640 zoom 1.5
        ease 10 pos 1280
    image cg limb_party_2:
        'cg limb_discord_1' with Dissolve(15)
        pause 15
        'cg limb_discord_2' with Dissolve(15)
        pause 15
        'cg limb_discord_3' with Dissolve(15)
        pause 15
        repeat
    image cg limb_picture_start_hue:
        im.MatrixColor(limb_images+ "cg/limb_picture_start.jpg",im.matrix.hue(180))
        xzoom -1
    image cg limb_safe_horror:
        contains:
            'bg black'
        contains:
            'prologue_dream'
        contains:
            'cg limb_safe_net'
    image cg limb_safe_next_blink:
        'cg limb_safe_next' with dissolve2
        pause 2
        'cg limb_safe_next_alt' with dissolve2
        pause 2
        repeat
    image cg limb_safe_sepia = im.Sepia(limb_images + "cg/limb_safe_0.jpg")
    image cg limb_shadow_gloria:
        'cg limb_fog_man_3' with dissolve2
        pause 3
        'cg limb_fog_man_4' with dissolve2
        pause 3
        repeat
    image cg limb_shadow_shine:
        'cg limb_fog_man_1'
        pause 2
        'cg limb_shadow_gloria' with dissolve
    image cg limb_sins_end:
        'cg limb_go_to_sleep'
        'bg black' with Dissolve(10)
    image cg limb_wrong_camp_motherfucker_fog:
        'bg ext_fog_4'
        pause 3
        'cg limb_wrong_camp_motherfucker' with Dissolve(15.0)

    image limb_flashback_1:
        contains:
            'cg limb_in_auto_un_fog_1'
            alpha 0.5
        contains:
            'prologue_dream'
            alpha 1
    image limb_flashback_2:
        contains:
            'pl_snake' with vpunch
            anchor (0.5, 0.5)
            pos (0.5, 0.5)
            alpha 0.5
            zoom 0
            ease 0.2 zoom 1
            pause 0.5
            ease 1 alpha 0
        contains:
            'prologue_dream'
            alpha 1
    image limb_flashback_3:
        contains:
            'cs normal'
            cleft
            alpha 0.5
        contains:
            'pl_el_man'
            cright
            alpha 0.5
        contains:
            'prologue_dream'
            alpha 1

    image limb_prologue_1 = limb_images + "gui/effects/limb_prologue_1.png"
    image limb_prologue_2 = limb_images + "gui/effects/limb_prologue_2.png"
    image limb_prologue_3 = limb_images + "gui/effects/limb_prologue_3.png"
    image limb_glitch_1 = limb_images + "gui/effects/glitch_1.png"
    image limb_glitch_2 = limb_images + "gui/effects/glitch_2.png"
    image limb_glitch_3 = limb_images + "gui/effects/glitch_3.png"
    image limb_glitch_4 = limb_images + "gui/effects/glitch_4.png"

    image limb_ach_pl_fin = limb_images + "gui/achievements/ach_pl_fin.png"
    image limb_blood_frame = limb_images + "gui/effects/limb_blood_frame.png"
    image limb_blood_frame_dis:
        'limb_blood_frame'
        alpha 0
        ease 1 alpha 1
    image limb_NickFury = limb_images + "gui/effects/nick_fury.png"
    image limb_filmstrip = limb_images + "gui/effects/limb_filmstrip.png"
    image limb_filmstrip_sin = im.Grayscale(limb_images + "gui/effects/limb_filmstrip.png")
    image limb_photo = limb_images + "gui/effects/limb_photo.png"
    image limb_raindrop_particle_large = limb_images + "gui/effects/raindrop_large.png"
    image limb_raindrop_particle_normal = limb_images + "gui/effects/raindrop_normal.png"
    image limb_raindrop_particle_small = limb_images + "gui/effects/raindrop_small.png"
    image limb_repeat:
        'pl_repeat'
        anchor (0.5, 0.5)
        pos (175, 50)
        alpha 0
        ease 1.5 alpha 1
        ease 1.5 alpha 0
        repeat

    image limb_qte_F1 = limb_images + "gui/effects/qte/limb_qte_F1.png"
    image limb_qte_F2:
        'limb_qte_F1'
        limb_images + "gui/effects/qte/limb_qte_F2.png" with limb_alpha_diss_fast
        pause 0.8
        ease 0.3 alpha 0
    image limb_qte_R1 = limb_images + "gui/effects/qte/limb_qte_R1.png"
    image limb_qte_R2:
        'limb_qte_R1'
        limb_images + "gui/effects/qte/limb_qte_R2.png" with dissolve_fast
        pause 0.8
        ease 0.3 alpha 0

    image limb_qte_button_st_0 = limb_images + "gui/effects/qte/limb_qte_button_st_0.png"
    image limb_qte_button_st_1 = limb_images + "gui/effects/qte/limb_qte_button_st_1.png"
    image limb_qte_button_st_2 = limb_images + "gui/effects/qte/limb_qte_button_st_2.png"
    image limb_qte_button_st_3 = limb_images + "gui/effects/qte/limb_qte_button_st_3.png"
    image limb_qte_button_st_4 = limb_images + "gui/effects/qte/limb_qte_button_st_4.png"
    image limb_qte_button_st_5 = limb_images + "gui/effects/qte/limb_qte_button_st_5.png"
    image limb_qte_button_st_full = limb_images + "gui/effects/qte/limb_qte_button_st_full.png"

    image limb_horror_brick_1 = 'mods/Limb/resourses/images/gui/hor/limb_safe_brick_1_idle.png'
    image limb_horror_brick_2 = 'mods/Limb/resourses/images/gui/hor/limb_safe_brick_2_idle.png'
    image limb_horror_brick_3 = 'mods/Limb/resourses/images/gui/hor/limb_safe_brick_3_idle.png'
    image limb_horror_brick_4 = 'mods/Limb/resourses/images/gui/hor/limb_safe_brick_4_idle.png'
    image limb_horror_brick_5 = 'mods/Limb/resourses/images/gui/hor/limb_safe_brick_5_idle.png'
    image limb_horror_brick_6 = 'mods/Limb/resourses/images/gui/hor/limb_safe_brick_6_idle.png'

    image limb_menu_background_1 = limb_images + "gui/main_menu/menu_background_0.jpg"
    image limb_menu_background_2 = limb_images + "gui/main_menu/menu_background_1.jpg"
    image limb_menu_background_3 = limb_images + "gui/main_menu/menu_background_2.jpg"
    image limb_menu_background_0 = limb_images + "gui/main_menu/menu_background_end.jpg"

    image limb_menu_background:
        'bg black' with dissolve_fast
        pause 0.5
        'limb_menu_background_1' with pixellate
        anchor (0.5, 0.5)
        pos (0.5, 0.5)
        pause 3
        'limb_menu_background_2' with dissolve
        anchor (0.5, 0.5)
        pos (0.5, 0.5)
        pause 3
        'limb_menu_background_3' with dissolve2
        anchor (0.5, 0.5)
        pos (0.5, 0.5)
        pause 3
        repeat
    image limb_menu_background_end:
        'bg black' with dissolve_fast
        pause 0.5
        'limb_menu_background_0' with flash
        anchor (0.5, 0.5)
        pos (0.488, 0.5)

    image limb_music_button_idle = limb_images + "gui/player/button_player_idle.png"
    image limb_music_button_hover = limb_images + "gui/player/button_player_hover_3.png"
    image limb_music_button_idle_stop = limb_images + "gui/player/button_player_idle_stop.png"
    image limb_music_button_hover_stop = limb_images + "gui/player/button_player_hover_stop.png"

    image limb_root_fon_day:
            limb_images + "gui/root_titles/fon_day.png"
            limb_title
    image limb_root_fon_endless:
            limb_images + "gui/root_titles/fon_endless.png"
            limb_title
    image limb_root_fon_night:
            limb_images + "gui/root_titles/fon_night.png"
            limb_title
    image limb_root_fon_prologue:
            limb_images + "gui/root_titles/fon_prologue.png"
            limb_title
    image limb_root_fon_secret:
            limb_images + "gui/root_titles/fon_secret.png"
            limb_title
    image limb_root_fon_sunset:
            limb_images + "gui/root_titles/fon_sunset.png"
            limb_title

    image limb_eff_safe = limb_images + "gui/root_titles/effect_safe.png"

    image limb_eff_thunder:
        pause 0.01
        limb_images + "gui/effects/lightnings.png" with limb_thunder
        alpha 1
        ease 0.4 alpha 0
        choice:
            pause 1
        choice:
            pause 2
        choice:
            pause 2.5
        limb_images + "gui/effects/lightnings.png" with limb_thunder
        alpha 1
        xzoom -1
        ease 0.4 alpha 0
        choice:
            pause 0.5
        choice:
            pause 1
        choice:
            pause 1.5
        repeat
    image limb_eff_pink_fire:
        limb_images + "gui/effects/filter_pink_1.png" with limb_alpha_diss_fast
        alpha 0.5
        pause 0.35
        limb_images + "gui/effects/filter_pink_2.png" with limb_alpha_diss_fast
        alpha 0.5
        pause 0.35
        repeat

    image limb_eff_fantasy_spiral:
        contains:
            'pl_spiral_4'
            align (0.5, 0.5) alpha 0.5
            linear 6 rotate 360
            repeat
        contains:
            'pl_spiral_4'
            align (0.5, 0.5) alpha 0.5 rotate 45
            linear 6 rotate 360
            repeat
        contains:
            'pl_spiral_6'
            align (0.5, 0.5) alpha 0.5
            linear 6 rotate -360
            repeat

    image limb_eff_prologue_dream:
        'limb_prologue_1'
        alpha 0.4
        pause 0.1
        'limb_prologue_2'
        alpha 0.4
        pause 0.1
        'limb_prologue_3'
        alpha 0.4
        pause 0.1
        repeat
    image limb_eff_glitch:
        choice:
            'limb_glitch_1'
            parallel:
                choice:
                    alpha 0.8
                choice:
                    alpha 1
                choice:
                    alpha 1
                choice:
                    alpha 1
                choice:
                    alpha 1
            parallel:
                choice:
                    pause 0.1
                choice:
                    pause 0.5
        choice:
            'limb_glitch_2'
            parallel:
                choice:
                    alpha 0.8
                choice:
                    alpha 1
                choice:
                    alpha 1
                choice:
                    alpha 1
                choice:
                    alpha 1
            parallel:
                choice:
                    pause 0.1
                choice:
                    pause 0.3
            'limb_glitch_3'
            parallel:
                choice:
                    alpha 0.8
                choice:
                    alpha 1
                choice:
                    alpha 1
                choice:
                    alpha 1
                choice:
                    alpha 1
            parallel:
                choice:
                    pause 0.1
                choice:
                    pause 0.3
        choice:
            'limb_glitch_4'
            parallel:
                choice:
                    alpha 0.8
                choice:
                    alpha 1
                choice:
                    alpha 1
                choice:
                    alpha 1
                choice:
                    alpha 1
            parallel:
                choice:
                    pause 0.1
                choice:
                    pause 0.3
        repeat

    image limb_eff_filmstip:
        "limb_filmstrip"
        anchor (0, 0)
        pos (-13470, 0)
        parallel:
            pause 2.5
            easeout 3.5 pos (1920, 0)
        parallel:
            pause 2.5
            linear 3.5 alpha 0
    image limb_eff_filmstip_sin:
        "limb_filmstrip_sin"
        anchor (0, 0)
        pos (-13470, 0)
        parallel:
            pause 2.5
            easeout 3.5 pos (1920, 0)
        parallel:
            pause 2.5
            linear 3.5 alpha 0
    image limb_eff_photo:
        'limb_photo'
        alpha 1
        pause 2.5
        ease 3.5 alpha 0

    image limb_eff_light_snow:
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
    image limb_eff_hard_snow:
        contains:
            "limb_eff_light_snow"
        contains:
            "limb_eff_light_snow"
        contains:
            "limb_eff_light_snow"

    image limb_eff_butterfly_small:
        im.Scale(limb_images + "sprites/butterfly_1.png", 45, 40) with limb_alpha_diss_fast
        anchor (0.5, 0.5)
        pos (0.5, 0.5)
        rotate 90
        pause 0.5
        im.Scale(limb_images + "sprites/butterfly_2.png", 45, 40) with limb_alpha_diss_fast
        pause 0.5
        repeat
    image limb_eff_butterfly_normal:
        im.Scale(limb_images + "sprites/butterfly_1.png", 225*0.5, 200*0.5) with limb_alpha_diss_fast
        anchor (0.5, 0.5)
        pos (0.5, 0.5)
        rotate 90
        pause 0.5
        im.Scale(limb_images + "sprites/butterfly_2.png", 225*0.5, 200*0.5) with limb_alpha_diss_fast
        pause 0.5
        repeat
    image limb_eff_butterfly_large:
        limb_images + "sprites/butterfly_1.png" with limb_alpha_diss_fast
        anchor (0.5, 0.5)
        pos (0.5, 0.5)
        rotate 90
        pause 0.5
        limb_images + "sprites/butterfly_2.png" with limb_alpha_diss_fast
        pause 0.5
        repeat

    image limb_eff_butterflies:
        contains:
            SnowBlossom("limb_eff_butterfly_small", 4, 10, (1, 10), (500, 1000))
        contains:
            SnowBlossom("limb_eff_butterfly_normal", 8, 10, (1, 10), (500, 1000))
        contains:
            SnowBlossom("limb_eff_butterfly_large", 8, 10, (1, 10), (500, 1000))
    image limb_eff_butterflies_darkness:
        contains:
            "limb_eff_butterflies"
            rotate -90
            left
        contains:
            "limb_eff_butterflies"
            rotate -90
        contains:
            "limb_eff_butterflies"
            rotate -90
            right

    image limb_eff_light_rain:
        truecenter
        xzoom 1.3 yzoom 1.7
        contains:
            SnowBlossom("limb_raindrop_particle_normal", 10, 50, (50, 100), (1500, 1600))
        contains:
            SnowBlossom("limb_raindrop_particle_small", 25, 50, (25, 50), (1400, 1500))
    image limb_eff_light_rain_l:
        "limb_eff_light_rain"
        rotate 16.0
    image limb_eff_light_rain_r:
        "limb_eff_light_rain"
        rotate -16.0

    image limb_eff_rain:
        truecenter
        xzoom 1.3 yzoom 1.7
        contains:
            SnowBlossom("limb_raindrop_particle_large", 20, 50, (75, 125), (1600, 1700))
        contains:
            SnowBlossom("limb_raindrop_particle_normal", 50, 50, (50, 100), (1500, 1600))
        contains:
            SnowBlossom("limb_raindrop_particle_small", 200, 50, (25, 50), (1400, 1500))
    image limb_eff_rain_l:
        "limb_eff_rain"
        rotate 16.0
    image limb_eff_rain_r:
        "limb_eff_rain"
        rotate -16.0

    image limb_eff_hard_rain:
        contains:
            "limb_eff_rain"
        contains:
            "limb_eff_rain"
    image limb_eff_hard_rain_l:
        contains:
            "limb_eff_rain_l"
        contains:
            "limb_eff_rain_l"
    image limb_eff_hard_rain_r:
        contains:
            "limb_eff_rain_r"
        contains:
            "limb_eff_rain_r"

    image limb_eff_blood_rain:
        truecenter
        xzoom 1.3 yzoom 1.7
        contains:
            SnowBlossom(im.Recolor(limb_images + "gui/effects/raindrop_small.png", 255, 0, 0, 255), 10, 50, (75, 125), (1600, 1700))
        contains:
            SnowBlossom(im.Recolor(limb_images + "gui/effects/raindrop_normal.png", 255, 0, 0, 255), 10, 50, (75, 125), (1600, 1700))
        contains:
            SnowBlossom(im.Recolor(limb_images + "gui/effects/raindrop_large.png", 255, 0, 0, 255), 10, 50, (75, 125), (1600, 1700))
        contains:
            SnowBlossom(im.Recolor(limb_images + "gui/effects/raindrop_small.png", 255, 0, 0, 255), 10, 50, (75, 125), (1600, 1700))
        contains:
            SnowBlossom(im.Recolor(limb_images + "gui/effects/raindrop_normal.png", 255, 0, 0, 255), 10, 50, (75, 125), (1600, 1700))
        contains:
            SnowBlossom(im.Recolor(limb_images + "gui/effects/raindrop_large.png", 255, 0, 0, 255), 10, 50, (75, 125), (1600, 1700))
        contains:
            SnowBlossom(im.Recolor(limb_images + "gui/effects/raindrop_small.png", 255, 0, 0, 255), 10, 50, (75, 125), (1600, 1700))
        contains:
            SnowBlossom(im.Recolor(limb_images + "gui/effects/raindrop_normal.png", 255, 0, 0, 255), 10, 50, (75, 125), (1600, 1700))
        contains:
            SnowBlossom(im.Recolor(limb_images + "gui/effects/raindrop_large.png", 255, 0, 0, 255), 10, 50, (75, 125), (1600, 1700))
    image limb_eff_blood_rain_l:
        "limb_eff_blood_rain"
        rotate 16.0
    image limb_eff_blood_rain_r:
        "limb_eff_blood_rain"
        rotate -16.0

    image limb_run_anim_1:
        contains:
            "bg ext_bus_night"
        contains:
            "bg ext_bus_night"
            ease 0.15 pos (0, 0)
            ease 0.15 pos (50,50)
            ease 0.15 pos (0, 0)
            ease 0.15 pos (-50,50)
            repeat
        contains:
            "zhenya/images/blink.png"
    image limb_run_anim_2:
        contains:
            "bg ext_road_night2"
        contains:
            "bg ext_road_night2"
            ease 0.15 pos (0, 0)
            ease 0.15 pos (50,50)
            ease 0.15 pos (0, 0)
            ease 0.15 pos (-50,50)
            repeat
        contains:
            "zhenya/images/blink.png"

    transform limb_custom_pos(xp=0.5,yp=0.5,xz=1,yz=1,a=1):
        anchor (0.5, 0.5)
        pos (xp, yp)
        xzoom xz
        yzoom yz
        alpha a
    transform limb_fairy_fly:
        anchor (0.5, 0.5)
        pos (0.5, 0.45)
        ease 5 pos (0.5, 0.5)
        ease 5 pos (0.5, 0.45)
        repeat
    transform limb_fairy_wings:
        anchor (0.5, 0.5)
        pos (0.51, 0.45)
        ease 5 pos (0.51, 0.5)
        ease 5 pos (0.51, 0.45)
        repeat
    transform limb_fairy_wings_close:
        anchor (0.5, 0.5)
        pos (0.53, 0.45)
        ease 5 pos (0.53, 0.5)
        ease 5 pos (0.53, 0.45)
        repeat
    transform limb_fly:
        anchor (0.5, 0.5)
        pos (-0.1, 0.4)
        linear 6 pos (0.3, 0.3)
        linear 5 pos (0.7, 0.2)
        linear 6.5 pos (1.1, 0.4)
    transform limb_ghost:
        anchor (0.5, 0.5)
        pos (-0.25, 0.5)
        ease 3 pos (1.25, 0.5)
        repeat
    transform limb_get_achievement(p=4):
        pos(0.2, 0.8)
        anchor(0.5, 0.5)
        zoom 0.0
        ease 1.5 zoom 1.05
        ease 0.25 zoom 0.95
        ease 0.25 zoom 1.0
        pause p
        ease 0.5 pos(-0.8, 0.85)
        ease 0.5 pos(-1.0, 0.85) alpha 0.0
    transform limb_moto_pos:
        anchor (0.5, 0.5)
        pos (0.5, 0.7)
    transform limb_multi_1(yp=0.5):
        anchor (0.5, 0.5)
        pos (-0.25, yp)
        ease 6 pos (1.25, yp)
        repeat
    transform limb_multi_2:
        anchor (0.5, 0.5)
        pos (0.5, -0.25)
        ease 6 pos (0.5, 1.25)
        repeat
    transform limb_running:
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
    transform limb_running_light:
        align (0.5, 0.5)
        zoom 1.01
        ease 0.2 xalign 0.35 yalign 0.65
        ease 0.2 xalign 0.50 yalign 0.50
        ease 0.2 xalign 0.65 yalign 0.65
        ease 0.2 xalign 0.50 yalign 0.50
        repeat
    transform limb_shake:
        choice:
            ease 0.02 pos (0.001, -0.001)
            ease 0.02 pos (0, 0)
        choice:
            ease 0.02 pos (-0.001, 0.001)
            ease 0.02 pos (0, 0)
        choice:
            ease 0.02 pos (0.001, -0.001)
            ease 0.02 pos (0, 0.001)
        choice:
            ease 0.02 pos (-0.001, 0.001)
            ease 0.02 pos (0, 0.001)
        repeat
    transform limb_shake_rvrs:
        xzoom -1
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
    transform limb_slideshow:
        truecenter
        zoom 3
        ease 0.8 zoom 0.05
    transform limb_spiral:
        anchor (0.5, 0.5)
        pos (0.5, 0.5)
        zoom 0.3
        parallel:
            ease 5 zoom 20
        parallel:
            ease 10 rotate 2880
        parallel:
            pause 3
            ease 1 alpha 0
    transform limb_sword_show:
        anchor (0.5, 0.5)
        pos (0.92, 0.5)
        rotate 30
        parallel:
            ease 2 pos (0.5, 0.5)
        parallel:
            ease 1.5 rotate 0
    transform limb_sword_hide:
        anchor (0.5, 0.5)
        pos (0.5, 0.5)
        parallel:
            ease 2 pos (0.92, 0.5)
        parallel:
            pause 0.5
            ease 1.5 rotate 30
    transform limb_tabi:
        anchor (0.5, 0.5)
        pos (0.5, 0.5)
        zoom 1
        ease 3 zoom 1.5
    transform limb_titer(p=3):
        anchor (0.5, 0.5)
        pos (1.5, 0.5)
        ease 1 pos (0.5, 0.5)
        pause p
        ease 1 pos (-0.5, 0.5)
    transform limb_title:
        anchor (0.5, 0.5)
        pos (1.5, 0.65)
        ease 2.5 pos (0.88, 0.7)
    transform limb_title_pos:
        anchor (0.5, 0.5)
        pos (0.88, 0.7)
    transform limb_to_be_trans:
        align (1.5, 0.97)
        ease 1.5 align (0.85, 0.97)
        ease 0.5 align (0.95, 0.97)
        pause 4.5
        ease 0.5 align (1.5, 0.97)
    transform limb_un_pos:
        anchor (0.5, 0.5)
        pos (0.355, 0.445)
        zoom 1.08
    transform limb_walking:
        align (0.5, 0.5)
        zoom 1.01
        ease 0.3 xalign 0.35 yalign 0.65
        ease 0.3 xalign 0.50 yalign 0.50
        ease 0.3 xalign 0.65 yalign 0.65
        ease 0.3 xalign 0.50 yalign 0.50
        repeat
    transform limb_wobble:
        anchor (0.5, 0.5)
        pos (0.5, 0.6)
        pause 1
        ease 0.3 pos (0.5, 0.65)
        ease 0.3 pos (0.5, 0.57)
        ease 0.3 pos (0.5, 0.6)

init -20 python:
    from datetime import datetime
    limb_time = datetime.now().hour

    image__filter_hue = lambda: lb__recolor(lambda i: im.MatrixColor(i,im.matrix.hue(180)))
    image__filter_invert = lambda: lb__recolor(lambda i: im.MatrixColor(i,im.matrix.invert()))

    limb_font_1 = 'mods/Limb/resourses/images/gui/fonts/var_1.otf'
    limb_font_2 = 'mods/Limb/resourses/images/gui/fonts/var_2.otf'
    limb_font_3 = 'mods/Limb/resourses/images/gui/fonts/var_3.ttf'
    limb_font_4 = 'mods/Limb/resourses/images/gui/fonts/var_4.otf'


    limb_images = 'mods/Limb/resourses/images/'
    limb_video = 'mods/Limb/resourses/video/'
    limb_sound = 'mods/Limb/resourses/sound/'
    limb_music = limb_sound + 'music/'
    limb_intro = limb_images + 'intro/'

    limb_eat_mushroom = False
    limb_fire_qte_act = False
    limb_get_keys = False
    limb_lap2 = False

    limb_workshop_old = False
    limb_garage_old = False

    limb_first_mirror = True
    limb_stray_mirror = False
    limb_adventurer_mirror = False
    limb_workshop_mirror = False
    limb_cosplay_mirror = False
    limb_psycho_mirror = False
    limb_killer_mirror = False
    limb_runner_mirror = False
    limb_garage_mirror = False

    pl_ell = '{w=0.3}.{w=0.3}.{w=0.3}.'

init -1 python:
    #mods["limb_intro"] = u"Лимб"
    mods["limb_intro"] = u"{color=#818670}{size=40}{font=[limb_font_1]}Лимб{/font}{/color}{/size}"

    limb_all_music = []
    for i in renpy.list_files():
        if (i.startswith(limb_music)) and (i.endswith((".mp3", ".ogg"))):
            limb_all_music.append(i)

    limb_track_list={((str((i[30:-4])).replace("pl_", "").replace("ae_", "Aendo - ").replace("dn_", "Dunkle Nil - ").replace("ef_", "EconomicFour - ").replace("gk_", "Gek Kosni - ").replace("uc_", "Unfamiliar Ceiling - ").replace("st_", "SanTechnik - ").replace("_", " ")).title())[0:40]: str(i) for i in limb_all_music}

    for f in renpy.list_files():
        if f.startswith(limb_images):
            for fold in ('bg','cg','sprites','intro'):
                if fold == 'sprites':
                    if f[len(limb_images):].startswith(fold+'/'):
                        renpy.image('pl_'+f[len(limb_images)+8:-(len(f.split('.')[-1])+1)],f)

                if f[len(limb_images):].startswith(fold+'/'):
                    renpy.image(fold+' '+f[len(limb_images)+3:-(len(f.split('.')[-1])+1)],f)

        elif f.startswith(limb_sound):
            for fold in ('music/','sfx/','ambience/'):
                if f[len(limb_sound):].startswith(fold):
                    renpy.python.store_dicts['store'][f[len(limb_sound+fold):-(len(f.split('.')[-1])+1)]] = f

    pl_chs_list = (('second_sound','sfx',False),('sound_loop','sfx',True))
    for n,c,l in pl_chs_list:
        renpy.music.register_channel(n,c,l)

    pl_spr_invers = [
        "mi_queen",
        "sh_1",
        "sh_2",
        "sh_3",
        "us_android",
        "us_zombie_1",
        "us_zombie_2"
        ]
    for spr_name in pl_spr_invers:
        renpy.image('pl_'+spr_name+'_invers',(im.MatrixColor(limb_images + 'sprites/'+spr_name+'.png', im.matrix.invert())))

    pl_spr_gray = [
        "moto_4"
        ]
    for spr_name in pl_spr_gray:
        renpy.image('pl_'+spr_name+'_gray',(im.Grayscale(limb_images + 'sprites/'+spr_name+'.png')))

    pl_spr_night = [
        "dv_dress_fap",
        "dv_dress_normal",
        "dv_dress_smile",
        "elena_1",
        "elena_2",
        "pi_n_pi",
        "sh_1",
        "sh_2",
        "sh_3",
        "sh_dead",
        "sh_dead_blood",
        "sh_dead_hands",
        "sh_miami_1",
        "sh_miami_2",
        "sh_out",
        "sl_party_1",
        "sl_party_2",
        "sl_slut_1",
        "sl_slut_2",
        "sm_1",
        "sm_2",
        "sm_3"
        ]
    for spr_name in pl_spr_night:
        renpy.image('pl_'+spr_name+'_night',(im.MatrixColor(limb_images + 'sprites/'+spr_name+'.png', im.matrix.tint(0.63, 0.78, 0.82))))

    pl_spr_sunset = [
        "ma_limb_1_alt",
        "ma_limb_2_alt",
        "moto_1",
        "sh_1",
        "sh_2",
        "sh_3",
        "sh_miami_1",
        "sh_miami_2",
        "sl_slut_1",
        "sl_slut_2"
        ]
    for spr_name in pl_spr_sunset:
        renpy.image('pl_'+spr_name+'_sunset',(im.MatrixColor(limb_images + 'sprites/'+spr_name+'.png', im.matrix.tint(0.94, 0.82, 1.0))))

    pl_spr_hand = [
        "hand_0",
        "hand_glass_0",
        "hand_glass_alt_0",
        "hand_magic_1_0",
        "hand_magic_2_0",
        "hand_magic_3_0",
        "hand_magic_4_0",
        "hand_magic_5_0",
        "hand_magic_6_0",
        "hand_mirror_0",
        "hand_record_0",
        "hand_record_magic_0"
        ]
    for spr_name in pl_spr_hand:
        renpy.image('pl_'+spr_name.replace("_0", ""),(im.Scale(limb_images + 'sprites/'+spr_name+'.png', 1920, 1080)))

    pl_root_list = [("410"),("adventurer"),("aftersafe"),("artist"),("cheef"),("chemist"),("coma"),
                    ("cosplay"),("doctor"),("dop"),("killer"),("mars"),("moto"),("music"),("mush"),("neko"),
                    ("prolog"),("psycho"),("safe"),("sanatorium"),("someroom"),("stray"),("war"),("writer"),
                    ("end_exams"),("end_fantasy"),("end_horror"),("end_sin"),("end_summer")]
    for root_name in pl_root_list:
        renpy.image('root_'+root_name, limb_images + 'gui/root_titles/root_'+root_name+'.png')

    def limb_root_name(time_tg, root):
        renpy.show('limb_root_fon_'+time_tg)
        renpy.pause(2.5, hard=True)
        renpy.show('root_'+root, [limb_title_pos])
        renpy.with_statement(dissolve2)
        renpy.pause(1.0, hard=True)
        renpy.hide('limb_root_fon_'+time_tg)
        renpy.hide('root_'+root)
        renpy.with_statement(limb_alpha_diss)
    for i in range(1,7):
        renpy.image('pl_multi_'+str(i), limb_images + 'gui/effects/multi/multi_'+ str(i)+'.png')
    for i in range(1,19):
        renpy.image('pl_tabi_'+str(i), limb_images + 'gui/effects/tabi/tabi_'+ str(i)+'.jpg')
        renpy.image('pl_spiral_'+str(i), limb_images + 'gui/effects/spiral/spiral_'+ str(i)+'.png')

    def limb_spiral_atl(tabi):
        renpy.scene()
        renpy.show("pl_tabi_" + str(tabi), [limb_tabi])
        renpy.show("pl_spiral_" + str(tabi), [limb_spiral])
        renpy.pause(4)
        renpy.scene()
        renpy.show("bg black")
        renpy.transition(dissolve)

    def limb_sprite_switch(spr, old, new, diss, trans):
        renpy.hide(spr + old)
        if diss == None:
            if trans == None:
                renpy.show(spr + new)

            else:
                renpy.show(spr + new, [trans])

        else:
            if trans == None:
                renpy.show(spr + new)
                renpy.with_statement(diss)

            else:
                renpy.show(spr + new, [trans])
                renpy.with_statement(diss)

    def limb_menu_jump():
        _window_hide(dissolve2)
        renpy.scene()
        renpy.show("bg black")
        renpy.with_statement(dissolve2)
        renpy.pause(2,hard=True)
        renpy.jump("limb_menu")

    def limb_flow_transition(gr, trans):
        renpy.scene()
        renpy.show("bg black")
        renpy.with_statement(limb_flowtoright)
        renpy.scene()

        if trans == None:
            renpy.show("bg " + gr)

        else:
            renpy.show("bg " + gr, [trans])

        renpy.with_statement(limb_flowtoright)

    def limb_lap_transition(gr, trans):
        renpy.scene()
        renpy.show("bg black")
        renpy.with_statement(limb_lap)
        renpy.scene()

        if trans == None:
            renpy.show("bg " + gr)

        else:
            renpy.show("bg " + gr, [trans])

        renpy.with_statement(limb_lap)

    def limb_run(gr, diss, trans, overlay):
        renpy.scene()
        renpy.show("bg " + gr)

        if trans == 1:
            renpy.show(gr, [limb_running])

        elif trans == 2:
            renpy.show(gr, [limb_running_light])

        if overlay != None:
            renpy.show(overlay)

        if diss != None:
            renpy.transition(diss)

    def limb_mute(fade = 2.5):
        for channel in ["sound", "second_sound", "sound_loop", "ambience", "music"]:
            renpy.music.stop(channel = channel, fadeout = fade)

    def limb_set_volume(channel, value, fade):
        renpy.music.set_volume(volume = value, delay = fade, channel = channel)

    def limb_conversion(num, gr, time_db, life, time_tg, root, tabi):
        global save_name

        renpy.block_rollback()
        limb_mute(2.0)
        _window_hide(dissolve)
        set_mode_adv()

        for channel in [ "sound", "second_sound", "sound_loop", "ambience", "music" ]:
            limb_set_volume(channel, 1.0, 0.0)

        renpy.scene()
        renpy.show("black")
        renpy.with_statement(Dissolve(2.0))

        if tabi != None:
            if tabi in range (1, 7):
                renpy.music.play(sfx_travel_1, 'sound')

            elif tabi in range (6, 13):
                renpy.music.play(sfx_travel_2, 'sound')

            elif tabi in range (12, 17):
                renpy.music.play(sfx_travel_3, 'sound')

            limb_spiral_atl(tabi)

        else:
            renpy.movie_cutscene(limb_video + "conversion_" + str(num) + ".webm", delay = (num))

        renpy.scene()
        renpy.show("bg "+ gr)
        save_name = "Лимб.\n" + (life) + "."

        if time_db == 1:
            prolog_time()
            renpy.show("limb_eff_photo")
            renpy.music.play(pl_gk_suncave, 'music', fadein = 5)

        elif time_db == 1.2:
            prolog_time()
            renpy.show("limb_eff_photo")
            limb_set_volume('sound_loop', 0.5, 0)
            renpy.music.play(pl_gk_suncave, 'music', fadein = 5)
            renpy.music.play(pl_ae_trevoga, 'sound_loop', fadein = 5)

        elif time_db == 1.5:
            prolog_time()

        elif time_db == 2:
            night_time()
            renpy.show("limb_eff_filmstip")
            renpy.with_statement(limb_leap)

        elif time_db == 3:
            day_time()
            renpy.show("limb_eff_filmstip")
            renpy.with_statement(limb_leap)

        elif time_db == 4:
            sunset_time()
            renpy.show("limb_eff_filmstip")
            renpy.with_statement(limb_leap)

        elif time_db == 5:
            persistent.timeofday = 'secret'
            renpy.show("limb_eff_filmstip")
            renpy.with_statement(limb_leap)

        if time_tg != None:
            renpy.show('limb_root_fon_'+time_tg)
            renpy.pause(2.5, hard=True)
            renpy.show('root_'+root, [limb_title_pos])
            renpy.with_statement(dissolve2)
            renpy.pause(1.0, hard=True)
            renpy.hide('limb_root_fon_'+time_tg)
            renpy.hide('root_'+root)
            renpy.with_statement(limb_alpha_diss)

        renpy.pause(2.0, hard=True)

        if time_db != 1.5:
            if time_db != 2.5:
                _window_show(dissolve)

    pl_acm_list = [
        ("all_be_good", u"Всё будет хорошо"),
        ("blue_lagoon", u"Голубая лагуна"),
        ("coma_effect", u"Эффект комы"),
        ("eternal_shining", u"Вечное сияние"),
        ("fine_mars", u"Марс"),
        ("near_happiness", u"Счастье близко"),
        ("origin", u"Источник"),
        ("other_story", u"Другая история"),
        ("un_dead", u"Лена")
    ]

    for acm in pl_acm_list:
        acm_name = acm[0]

    for acm in pl_acm_list:
        renpy.image("acm_pl_" + acm[0], im.Scale(limb_images + "/gui/achievements/acm_pl_" + acm[0] + ".png", 420, 94))

    def show_pl_achiv(acm):
        _window_hide(dissolve2)
        renpy.play(sfx_achievement)
        renpy.show("acm_pl_" + acm, [limb_get_achievement(15)], layer = "overlay")
        renpy.pause(16)
        renpy.hide("acm_pl_" + acm, layer = "overlay")
        renpy.with_statement(dissolve)
        renpy.pause(2)

    import random
    nonunicode = "¡¢£¤¥¦§¨©ª«¬®¯°±²³´µ¶·¸¹º»¼½¾¿ÀÁÂÃÄÅÆÇÈÉÊËÌÍÎÏÐÑÒÓÔÕÖ×ØÙÚÛÜÝÞßàáâãäåæçèéêëìíîïðñòóôõö÷øùúûüýþÿĀāĂăĄąĆćĈĉĊċČčĎďĐđĒēĔĕĖėĘęĚěĜĝĞğĠġĢģĤĥĦħĨĩĪīĬĭĮįİıĲĳĴĵĶķĸĹĺĻļĽľĿŀŁłŃńŅņŇňŉŊŋŌōŎŏŐőŒœŔŕŖŗŘřŚśŜŝŞşŠšŢţŤťŦŧŨũŪūŬŭŮůŰűŲųŴŵŶŷŸŹźŻżŽž"

    def glitchtext(length):
        output = ""
        for x in range(length):
            output += random.choice(nonunicode)
        return output

    pl_glitch = glitchtext(10)

    limb_intro_blot = ImageDissolve(limb_images + "gui/intro/endless_horizons/blot.jpg", 1.0, ramplen = 25, reverse = False, alpha = True)
    limb_intro_hand = ImageDissolve(limb_images + "gui/intro/endless_horizons/hand.png", 1.0, ramplen = 25, reverse = True, alpha = True)
    limb_text_diss = ImageDissolve(limb_images + "gui/effects/flow_v.png", 15.0, ramplen = 25, reverse = True, alpha = True)
    limb_titer_diss = ImageDissolve(limb_images + "gui/effects/flow_v.png", 5.0, ramplen = 25, reverse = True, alpha = True)

    limb_flowtoleft = ImageDissolve(limb_images + "gui/effects/flow_h.png", 1.0, ramplen = 25, reverse = False, alpha = True)
    limb_flowtoright = ImageDissolve(limb_images + "gui/effects/flow_h.png", 1.0, ramplen = 25, reverse = True, alpha = True)
    limb_flowtoup = ImageDissolve(limb_images + "gui/effects/flow_v.png", 1.0, ramplen = 25, reverse = False, alpha = True)
    limb_flowtodown = ImageDissolve(limb_images + "gui/effects/flow_v.png", 1.0, ramplen = 25, reverse = True, alpha = True)
    limb_noise = ImageDissolve(limb_images + "gui/effects/noise.jpg", 19.0, ramplen = 25, reverse = False, alpha = True)
    limb_thunder = ImageDissolve(limb_images + "gui/effects/flow_v.png", 0.1, ramplen = 25, reverse = True, alpha = True)
    limb_razlom = ImageDissolve(limb_images + "gui/effects/razlom.jpg", 1.0, ramplen = 25, reverse = True, alpha = True)
    limb_blot = ImageDissolve(limb_images + "gui/intro/endless_horizons/blot.jpg", 2.0, ramplen = 25, reverse = False, alpha = True)
    limb_blot_fast = ImageDissolve(limb_images + "gui/intro/endless_horizons/blot.jpg", 0.8, ramplen = 25, reverse = True, alpha = True)
    limb_pushright_fast = PushMove(0.1, "pushright")
    limb_pushright = PushMove(1.0, "pushright")
    limb_pushright3 = PushMove(3, "pushright")
    limb_lap = ImageDissolve(limb_images + "gui/effects/lap.png", 2.0)
    limb_leap = ImageDissolve(limb_images + "gui/effects/leap.jpg", 2.0)
    limb_paint = ImageDissolve(limb_images + "gui/effects/paint.jpg", 1.5)
    limb_star = ImageDissolve(limb_images + "gui/effects/star.jpg", 2.0)
    limb_pixel_1 = ImageDissolve(limb_images + "gui/effects/pixel_1.png", 0.8, alpha = True)
    limb_pixel_2 = ImageDissolve(limb_images + "gui/effects/pixel_2.png", 1.0, alpha = True)
    limb_pixel_3 = ImageDissolve(limb_images + "gui/effects/pixel_3.png", 1.0, alpha = True)
    limb_pixel_4 = ImageDissolve(limb_images + "gui/effects/pixel_4.jpg", 0.8, alpha = True)
    limb_pio_pixel = Pixellate(0.3, 5)
    limb_alpha_diss = Dissolve(1, alpha=True)
    limb_alpha_diss2 = Dissolve(2, alpha=True)
    limb_alpha_diss3 = Dissolve(3, alpha=True)
    limb_alpha_diss_fast = Dissolve(0.5, alpha=True)
    limb_flash = Fade(0.1, 0.5, 0.3, color='#FFFFFF')
    limb_itai_flash = Fade(0.35, 0.0, 0.45, color='#F80000')
    limb_monitor_flash = Fade(0.2, 0.3, 2.5, color='#FFFFFF')
    limb_neon_flash = Fade(0.2, 0.0, 1.2, color='#EE204D')
    limb_party_flash = Fade(0.25, 0, 0.25, color='#EE204D')
    limb_psycho_flash = Fade(0.2, 0.0, 0.8, color='#33FFFF')

    limb_conversion_2 = limb_video + "conversion_2.webm"
    limb_conversion_4 = limb_video + "conversion_4.webm"

init 2 python:

    def limb_set_save_name(name):
        global save_name
        save_name = name

    style.normal_limb = Style(style.base_font)
    style.normal_limb.drop_shadow=(2, 2)
    style.normal_limb.drop_shadow_color = "#000"

    style.screen_limb = Style(style.normal_limb)
    style.screen_limb.size = 120

    style.limb_ReLife = Style(style.default)
    style.limb_ReLife.color = "#FFF"
    style.limb_ReLife.size = 120
    style.limb_ReLife.font = limb_font_1
    style.limb_ReLife.drop_shadow = [(1, 1), (1, 1), (1, 1), (1, 1)]
    style.limb_ReLife.drop_shadow_color = "#000"

    style.limb_NOOO = Style(style.limb_ReLife)
    style.limb_NOOO.color = "#FF0000"
    style.limb_NOOO.size = 150

    style.limb_RUUUN = Style(style.limb_NOOO)
    style.limb_RUUUN.size = 400

    limb_names_list = {
        'me'  :['Я',(108, 105, 96, 255)],
        'mef' :['Я',(236, 255, 31, 255)],
        'mes' :['Я',(129, 134, 148, 225)],
        'sem' :['Семен',(108, 105, 96, 255)],
        'ssem':['Супер-Семен',(108, 105, 96, 255)],

        'lg'  :['Девочка',(78, 255, 0, 255)],
        'guv' :['Девушка',(78, 255, 0, 255)],
        'gs'  :['Девушка',(128, 128, 128, 255)],
        'uvs' :['Дьявол',(128, 128, 128, 255)],

        'gdv' :['Девушка',(255, 170, 0, 255)],
        'orc' :['Элиссон',(255, 170, 0, 255)],

        'and' :['Девочка',(255, 50, 0, 255)],

        'gmi' :['Девушка',(0, 222, 255, 255)],
        'nz'  :['Незнакомка',(0, 222, 255, 255)],
        'elf' :['Эльфийка',(0, 222, 255, 255)],
        'enj' :['Энджиниа',(0, 222, 255, 255)],
        'ts'  :['Царица',(0, 222, 255, 255)],
        'tss' :['Царица',(77, 77, 77, 255)],

        'gun' :['Девушка',(185, 86, 255, 255)],
        'rob' :['Разбойница',(185, 86, 255, 255)],

        'god' :['Девушка',(0, 234, 50, 255)],
        'wom' :['Женщина',(0, 234, 50, 255)],
        'drc' :['Дракон',(0, 234, 50, 255)],

        'gsl' :['Девушка',(255, 210, 0, 255)],
        'sl'  :['Славяна',(255, 210, 0, 255)],
        'vsl' :['Тоненький голосок',(255, 210, 0, 255)],
        'pix' :['Слэйв',(255, 210, 0, 255)],

        'al'  :['Алекс',(255, 242, 38, 255)],
        'sn'  :['Саня',(255, 242, 38, 255)],
        'doc' :['Доктор',(255, 242, 38, 255)],
        'dbr' :['Добрый',(135, 135, 135, 255)],

        'b'   :['Парень',(255, 255, 0, 255)],
        'sg'  :['Сергей',(255, 255, 0, 255)],
        'gr'  :['Серый',(80, 80, 80, 255)],

        'eva' :['Ева',(67, 71, 80, 255)],

        'cs'  :['Девушка',(165, 165, 255, 255)],
        'pr'  :['Профессор',(165, 165, 255, 255)],

        'gh'  :['Призрак',(54, 54, 54, 255)],
        'zmb' :['Зомби',(156, 161, 151, 255)],
        'v'   :['Голос',(128, 128, 128, 255)],
        'pi'  :['Незнакомка',(128, 128, 128, 255)],
        'hor' :['Хором',(128, 128, 128, 255)],
        'bs'  :['Парни',(128, 128, 128, 255)],

        'ar'  :['Автор',(255, 25, 71, 255)]
        }

    pltsg = Character(u'Царица', color=(0, 222, 255, 255), what_font=limb_font_1, drop_shadow=[(2,2),(3,3)], drop_shadow_color='000', what_drop_shadow=[(2,2)], what_drop_shadow_color='000')
    pltsh = Character(u'Царица', color=(0, 222, 255, 255), what_color=(68, 45, 53, 255), drop_shadow=[(2,2),(3,3)], drop_shadow_color='000', what_drop_shadow=[(2,2)], what_drop_shadow_color='000')
    plsema = Character(u'Семен', color=(108, 105, 96, 255), what_color=(226, 199, 120, 255), drop_shadow=[(2,2),(3,3)], drop_shadow_color='000', what_drop_shadow=[(2,2)], what_drop_shadow_color='000')

    plme_pi = Character(u'{color=#6C6960}Я{/color}+{color=#E60101}Пионер{/color}', drop_shadow=[(2,2),(3,3)], drop_shadow_color='000', what_drop_shadow=[(2,2)], what_drop_shadow_color='000')
    plme_bl = Character(u'Я', color=(108, 105, 96, 255), what_color='#E2C778', drop_shadow=[(2,2),(3,3)], drop_shadow_color='000', what_drop_shadow=[(2,2)], what_drop_shadow_color='000')

    plelf_hv = Character(u'{color=#00DEFF}Энджиниа{/color} {color=#808080}(вполголоса){/color}', drop_shadow=[(2,2),(3,3)], drop_shadow_color='000', what_drop_shadow=[(2,2)], what_drop_shadow_color='000')
    plrob_hv = Character(u'{color=#B956FF}Разбойница{/color} {color=#808080}(вполголоса){/color}', drop_shadow=[(2,2),(3,3)], drop_shadow_color='000', what_drop_shadow=[(2,2)], what_drop_shadow_color='000')
    plguv_hv = Character(u'{color=#4EFF00}Девушка{/color} {color=#808080}(вполголоса){/color}', drop_shadow=[(2,2),(3,3)], drop_shadow_color='000', what_drop_shadow=[(2,2)], what_drop_shadow_color='000')

    def limb_mode_nvl():
        global DynamicCharacter
        global _show_two_window
        gl = globals()
        for x in limb_names_list.keys():
            gl['pl'+x] = DynamicCharacter("pl%s_name"%x, color=limb_names_list[x][1], kind = nvl, who_suffix=":", what_style="normal_limb")
            gl["pl%s_name"%x] = limb_names_list[x][0]
        set_mode_nvl()

    def limb_mode_adv():
        global DynamicCharacter
        global _show_two_window
        gl = globals()
        for x in limb_names_list.keys():
            gl['pl'+x] = DynamicCharacter("pl%s_name"%x, color=limb_names_list[x][1], show_two_window=_show_two_window, kind = adv, what_style="normal_limb")
            gl["pl%s_name"%x] = limb_names_list[x][0]
        set_mode_adv()

    limb_mode_adv()

    test_limb_mus = []

label limb_intro:

    window hide
    $ save_name = ("Лимб. \nШаг вперёд")
    $ day_time()
    $ limb_screens_act()
    scene bg black
    play music pl_uc_deep_space fadein 3
    pause 1
    scene limb_intro_ground with Dissolve(3)
    show limb_intro_girls_1 with Dissolve(3)
    pause 1
    show limb_intro_window with Dissolve(3)
    pause 1
    hide limb_intro_girls_1
    show limb_intro_girls_blinking
    with limb_alpha_diss3
    show limb_intro_text with limb_text_diss
    pause 20
    hide limb_intro_window
    hide limb_intro_text
    show limb_intro_girls_4
    with limb_text_diss
    hide limb_intro_girls_1
    with dissolve
    hide limb_intro_girls_4
    show limb_intro_girls_3
    with dissolve
    stop music fadeout 6
    scene bg black with Dissolve(4)
    show limb_eff_butterflies_darkness:
        anchor (0.5, 0.5)
        pos (-0.1, 0.5)
        ease 8 pos (1.7, 0.5)
        ease 0 alpha 0
    with dissolve
    pause 2
    scene bg black with dissolve
    $ renpy.pause(3)
    scene anim limb_logo with Dissolve(5)
    pause 2
    $ limb_set_volume('logo', 0, 3)
    scene bg black with Dissolve(3)

label limb_menu:

    $ limb_mute()
    $ day_time()
    $ limb_screens_act()
    $ renpy.block_rollback()
    $ limb_set_volume('sound', 1, 0)
    play music pl_ae_blow_with_the_fires_remix
    scene limb_intro_ground
    # call screen limb_main_menu
    # jump limb_menu
    return

label limb_prolog:

    if persistent.trailers_on:
        $ renpy.movie_cutscene("video/limb_trailer.webm") ####

    $ limb_set_save_name("Лимб. \nШаг вперёд")
    stop music
    stop sound_loop2
    stop sound_loop
    stop ambience
    $ renpy.block_rollback()
    scene bg black
    $ day_time()
    pause 1
    hide screen limb_keys
    hide screen limb_mushroom
    hide screen limb_butterfly
    hide screen limb_kuroneko_1
    show cg limb_words_1 with dissolve2
    $ renpy.pause(15)
    hide cg limb_words_1 with dissolve2
    pause 1
    $ limb_root_name('day', 'prolog')
    pause 1
    play music pl_ae_bad_future
    pause 1
    scene bg int_auto_pl with limb_pixel_2
    pause 1
    $ limb_set_volume('sound_loop', 0.1, 0)
    play sound_loop sfx_bus_idle
    scene bg int_auto_pl at limb_shake
    with dissolve_fast
    pause 1
    window show
    $ persistent.limb_story_end = False

    "Машина движется по пустынной местности, распугивая ночную тишину. "
    "Скоро мы будем дома, и всё было бы хорошо, если б не проклятый туман. "
    "Дорога - я хорошо её знаю - на последних километрах круто идёт вниз, в долину, а там скапливался ОН. "
    "Лена до смерти боится тумана. "

    window hide
    scene anim limb_auto_anim with dissolve_fast
    pause 2.5
    scene cg limb_in_auto_un at limb_shake
    window show

    "Когда первые щупальца тумана касаются лобового стекла, я[pl_ell] новоиспеченный супруг[pl_ell] откидываюсь в кресле и искоса смотрю на свою молодую жену. Непривычно мыслить такими понятиями. До одури непривычно."
    "Лена дрожит так, будто держится за отбойный молоток. Она придвинула сидение до максимума, будто стараясь сжаться в точку и исчезнуть - только бы не видеть кисель за окном. "
    plme "Дорогая, послушай меня,"
    "как можно более ласково произношу я, стараясь смотреть и на дорогу, и на неё одновременно."
    plme "Мы это уже сотни раз обсуждали, разве нет? Рациональных причин бояться молекул воды нет, как нет где-то там, за окном,"

    show blink
    pause 1
    scene bg int_auto_fog at limb_shake
    hide blink
    show unblink
    play sound sfx_knock_glass

    "я стучу правой рукой по стеклу,"
    plme "неизвестных науке чудовищ. "
    "Дорогая поджимает губы и, зажмурившись, мотает головой, от чего её хвостики метаются в воздухе, как маленькие фиолетовые молнии."

    with vpunch

    plme "Лена!"
    "Уже резче обращаюсь я к супруге, вглядываясь в ночь перед машиной. Так и есть, туман всё гуще. "
    "По профессии будучи физиком, а по природе - довольно раздражительным человеком, я не могу и не хочу мириться с предрассудками, суевериями, необоснованными страхами и тому подобной чепухой. "
    "Мгновенно распаляюсь и спорю вплоть до бегства жертвы. Или наступления обезвоживания. "
    "Жену я люблю, поэтому обычно прощаю ей подобные приступы, тем более что бывают они не так часто. "
    "Однако сегодня я очень устал и вдобавок был сильно раздражен бестолковой конференцией, на которой торчал почти 7 часов, а туман был на редкость густой и всё никак не кончался[pl_ell] "
    "Поэтому, когда до ушей доносятся тихие всхлипы, уже порядком злой Семён Персунов вдавливает тормоза в пол и рычит:"

    $ limb_set_volume('sound', 1.5, 0)
    play sound sfx_limb_crying
    show cg limb_in_auto_un_fog_1 at limb_shake
    with vpunch
    $ limb_set_volume('sound', 1, 3)

    plme "Елена Викторовна Колесникова!!!{w=1} Перестань вести себя как большой испуганный кролик! Это просто чертов обычный туман, вода, понимаешь, влажность высокая, глупая ты девочка! Чёрт меня дери, если я понимаю, как вообще выш[pl_ell]"

    stop music fadeout 15

    "Большие зарёванные глаза таращатся на меня с обидой и укором[pl_ell]"
    "И я, конечно, осекаюсь. Хотя всё равно поздно[pl_ell]"
    "Пытаюсь взять себя в руки. Более спокойным тоном говорю:"
    plme "Извини, это всё усталость.{w=1} Давай мириться. Я знаю, как ты боишься тумана, обычно проезжаю это место как можно быстрее. "
    "Лена кивает. Она очень бледная и по-прежнему трясётся, и мне хочется её обнять и утешить. "

    stop sound_loop fadeout 2
    scene cg limb_in_auto_un_fog_1

    "Я осторожно съезжаю на обочину, заглушаю мотор. Откашливаюсь. "
    plme "Но знаешь[pl_ell] так больше продолжаться не может. "

    play music pl_uc_disraption fadein 5

    plme "Ты боишься уймы вещей, начиная со своей тени и заканчивая перелётными птицами. Я не психолог и вообще не врач, но обязан тебе помочь! "
    plme "И я думаю, что знаю как. "
    "По-прежнему держась за руль левой рукой, я наклоняюсь и приобнимаю жену. Лена боязливо выглядывает из-под рукава свитера, украдкой - чтобы я не видел - вытирая слезы. Но я всё равно всё вижу, и Лена это прекрасно знает. "
    "Хорошая мы пара, я думаю. "
    un "Сёма-а, мне ст-тыдно, ч-честно, "
    "заикаясь, произносит она. "
    un "Давай просто доедем домой, т{w=0.2}-там тихо, сухо и н-нет т{w=0.2}-т{w=0.2}-тум[pl_ell] "
    plme "Нет. Сейчас мы избавимся от этого страха, "
    "твердо говорит ей супруг, щёлкая рычажком на руле и переключая фары на дальний свет. Лучи втыкаются в стену из белёсого тумана, которая слепо колышется, будто бы холодное молоко в стакане ранним утром. "
    "Я было поспешил поделиться этим гениальным сравнением с женой, но наткнулся на другую стену - круглые блестящие глаза молили о помощи, и мне окончательно стало не по себе. \"Уж не совершаю ли я ту самую роковую ошибку?\" - взорвалась сверхновой мысль. "
    "Но Семён Евгеньевич Персунов не из тех, кто сдаётся на полпути, и мотивируя себя этим довольно-таки глупым утверждением, я решительно распахиваю дверцу. "

    with hpunch

    "Леночка пытается меня удерживать, но вдруг визжит, отпрыгивая назад на сидение[pl_ell] когда туман лезет в седан и спёртый воздух вступает в неравную борьбу с захватчиком."

    show cg limb_in_auto_un_fog_2 with dissolve

    "Я выхожу из машины, потягиваюсь. "
    "Обращаюсь к девушке, которая часто дышит и пытается забиться вглубь салона: "

    scene cg limb_auto_fog_2 with dissolve2

    plme "Здесь очень даже приятно! И совсем не страшно! "

    $ limb_set_volume('sound', 2, 0)
    play sound sfx_limb_steps_1

    "Я демонстративно машу рукой в воздухе и прохожу на пару метров дальше автомобиля. Затем возвращаюсь и вот уже стою рядом с крылом авто. "
    plme "Никого нет! "
    "Снаружи мой голос, наверное, доносится слегка приглушённо. "

    show cg limb_auto_fog_1
    pause 0.1
    show cg limb_auto_fog_2
    $ limb_set_volume('sound', 1, 2)

    plme "Лен, посмотри на меня! "
    plme "Ты ведь знаешь, что я в основном занимаюсь оптикой? А помнишь, в колледже у нас был проектор? О световых волнах я знаю довольно много. "
    plme "Тебе, честное слово, нечего бояться. Послушай[pl_ell] "
    "Говорю я проникновенно и уверенно, будучи неплохим оратором, и потихоньку ненаглядная отнимает ладони от лица. "
    "Я ободряюще улыбаюсь ей и начинаю объяснять: "
    plme "Ты же знаешь детскую забаву - театр теней, так? У нас есть источник света, "
    "я указываю на фару, "
    plme "и экран, на который свет падает, "

    scene bg ext_fog_4 with dissolve2

    "я тычу большим пальцем себе за спину. "

    window hide
    pause 1
    $ limb_mode_nvl()
    pause 1

    plme "Когда мы подносим к источнику света какой-то предмет, его тень падает на экран, и мы получаем проекцию предмета той же формы, но большего размера. "
    "Я складываю \"зайчика\" из пальцев, сую их перед фарой, и на полотне тумана появляется какое-то чудовище с восьмью щупальцами. Упс[pl_ell] "
    "Лена тоскливо поскуливает, прячась в машине. "
    plme "Пардон. "
    "С четвёртой попытки получается вполне прилично, и я, освоившись, демонстрирую свои познания фауны. "
    "Добившись таки от жены слабой улыбки, я воодушевлённо продолжаю: "
    plme "Большая часть \"страхов из тумана\" рождается именно таким образом. Иногда что-то интересное происходит из-за преломления света, например, от фонарей. "
    plme "Луч преломляется, рассеивается и расщепляется на спектр, и тогда получается красивый ореол - самый настоящий нимб! Этим же обусловлена и радуга. "
    "Я снова показываю рукой на фары, вокруг которых и правда - сияющие круги. Лена послушно смотрит, покрепче обняв колени, и слушает дальше, уже почти не всхлипывая. "

    pause 1
    nvl clear
    $ limb_mode_adv()
    pause 1
    scene cg limb_auto_blinking_1 with dissolve
    window show

    plme "Но самый интересный эффект имеет свое название. Это \"Брокенский призрак\", "
    "я чуть-чуть жду, пока жена справится с собой и начнет слушать, "
    "- или \"Брокенский великан\". Явление впервые описано в Германии, на пике горного массива Гарц, но встречается повсеместно, и в том числе - здесь и сейчас. "
    "Увлекшись, я собираюсь было шагнуть на свет, но спохватываюсь (в этот раз вовремя), и решаю сначала закончить объяснение (или усыпление?). "
    plme "Лучше всего эффект работает с облаками, поэтому чаще всего с ним встречаются альпинисты. "
    plme "Когда солнце светит во-от в этом направлении, в спину наблюдателю, он видит свою тень далеко впереди. Тень окружена почти таким же кругом, только сложнее - он называется глорией. "
    plme "Так, кажется, звали твою бабушку? Глория - это несколько разноцветных кругов вокруг тени. Сама тень кажется значительно больше наблюдателя, вот поэтому и великан. "
    "Заигравшись, шучу про недостаточно частые посещения спортзала, и, не добившись ответной реакции, я продолжаю: "
    plme "Капли воды в тумане находятся на разном расстоянии, что нарушает наше восприятие. А из-за подвижности экрана тень как будто бы живая, \"двигаясь\", "
    "я обозначаю пальцами кавычки. "
    plme "Ты готова? Смотри!"

    $ limb_set_volume('sound', 2, 0)
    play sound sfx_limb_steps_2

    "Я наконец захожу под свет фар и делаю пару шагов вперёд. Смотрю перед собой, удовлетворённо киваю, оборачиваюсь[pl_ell] За моей спиной возвышается колеблющаяся размытая тень, верхняя часть туловища которой окружена \"короной\" из цветных игл. "

    scene cg limb_shadow_shine with dissolve

    "Лена, подавшись вперед, смотрит на это действо, затаив дыхание. Я вновь начинаю говорить: "
    plme "Ты видишь? Это всего лишь тень!"
    "Я машу рукой, кручу головой, подпрыгиваю[pl_ell] Подняв руки, комично изображаю балерину. "

    show cg limb_auto_blinking_2 with dissolve

    "Тень повторяет все мои движения. На втором пируэте Леночка, не выдежав, заливается тихим смехом, вытирая глаза вязанным рукавом. "
    plme "Нет никаких чудовищ, детка. Нет и монстров в тумане. Нет, "

    $ limb_set_volume('sound', 1, 2)
    show cg limb_fog_man_1
    pause 0.3
    show cg limb_fog_man_2 with dissolve_fast
    scene cg limb_fog_man_5 with dissolve

    "я вновь оборачиваюсь, взмахом руки прогоняя дымку тумана, "
    plme "призраков и великанов! "
    "Я делаю пару шагов вперёд, и только потом[pl_ell] "

    stop music

    "Только потом обращаю внимание на то, что моя тень всё это время была совершенно неподвижна. "
    plme "Что за[pl_ell] "

    scene cg limb_fog_man_5 at limb_shake
    with dissolve_fast

    "начинаю было я, но замолкаю и медленно делаю шаг назад. "

    play sound sfx_limb_steps_monster

    "По поверхности тени пробегает рябь, и в глубокой ночной тишине, ранее нарушаемой только моим монологом, отчетливо звучит тяжелый шаг. "

    show cg limb_auto_darken with hpunch
    $ limb_set_volume('music', 0.8, 0)

    play second_sound sfx_limb_scream_1
    "Земля содрогается, стёкла в машине дребезжат. Лена визжит. "
    "Я разворачиваюсь и успеваю сделать ещё пару шагов, когда грохочущая тень догоняет меня - и резко утягивает обратно, в туман. "

    play music pl_ae_trevoga fadein 3
    play ambience ambience_limb_echo fadein 5

    "Последнее, что я успеваю заметить, это беззвучно рыдающая Лена[pl_ell] моя жена[pl_ell]{w} Стоп,{w=0.5} какая жена? "

    scene bg ext_fog_city

    "Какая такая Лена? "
    plv "Эй, Семён[pl_ell] Делековато же тебя занесло. "

    $ persistent.sprite_time = 'night'
    if limb_time in range(0, 8):
        show limb_intro_prezent_limb_1_v4:
            anchor (0.5, 0.5)
            pos (0.5, 0.5)
        show limb_intro_un_half_1:
            anchor (0.5, 0.5)
            pos (0.5007, 0.5)
        show limb_intro_un_half_2
        with dissolve2
    elif limb_time in range(8, 16):
        show limb_intro_prezent_limb_1_v4:
            anchor (0.5, 0.5)
            pos (0.5, 0.5)
        show limb_intro_pi_half_1:
            anchor (0.5, 0.5)
            pos (0.5007, 0.5)
        show limb_intro_pi_half_2
        with dissolve2
    elif limb_time in range(16, 24):
        show limb_intro_prezent_limb_1_v4:
            anchor (0.5, 0.5)
            pos (0.5, 0.5)
        show limb_intro_uv_half_1:
            anchor (0.5, 0.5)
            pos (0.5007, 0.5)
        show limb_intro_uv_half_2
        with dissolve2

    plv "Надо поговорить."
    plme "Что?"

    $ limb_mute(3)
    window hide

label limb_endless_horizons:

    play music pl_gk_red_haired_blues fadein 5
    $ renpy.pause(2,hard=True)
    if limb_time in range(0, 8):
        show limb_intro_un_half_1:
            anchor (0.5, 0.5)
            pos (0.5, 0.5)
            ease 2 pos (-0.5, 0.5)
        show limb_intro_un_half_2:
            anchor (0.5, 0.5)
            pos (0.5, 0.5)
            ease 2 pos (1.5, 0.5)
        show limb_intro_prezent_limb_1_v4:
            anchor (0.5, 0.5)
            pos (0.5, 0.5)
            ease 5 pos (0.5, -0.5)
    elif limb_time in range(8, 16):
        show limb_intro_pi_half_1:
            anchor (0.5, 0.5)
            pos (0.5, 0.5)
            ease 2 pos (-0.5, 0.5)
        show limb_intro_pi_half_2:
            anchor (0.5, 0.5)
            pos (0.5, 0.5)
            ease 2 pos (1.5, 0.5)
        show limb_intro_prezent_limb_1_v4:
            anchor (0.5, 0.5)
            pos (0.5, 0.5)
            ease 5 pos (0.5, -0.5)
    elif limb_time in range(16, 24):
        show limb_intro_uv_half_1:
            anchor (0.5, 0.5)
            pos (0.5, 0.5)
            ease 2 pos (-0.5, 0.5)
        show limb_intro_uv_half_2:
            anchor (0.5, 0.5)
            pos (0.5, 0.5)
            ease 2 pos (1.5, 0.5)
        show limb_intro_prezent_limb_1_v4:
            anchor (0.5, 0.5)
            pos (0.5, 0.5)
            ease 5 pos (0.5, -0.5)
    $ renpy.pause(2.5,hard=True)
    scene limb_intro_fog
    with pixellate
    $ renpy.pause(4,hard=True)
    show limb_intro_ememblem_2 with dissolve2
    $ renpy.pause(2,hard=True)
    show limb_intro_ememblem_1 with pixellate
    $ renpy.pause(1,hard=True)
    show limb_intro_ememblem_5 with dissolve2
    $ renpy.pause(2,hard=True)
    scene bg black with limb_intro_blot
    $ renpy.pause(2,hard=True)
    show limb_intro_prezent_limb_2 with limb_intro_blot
    $ renpy.pause(1,hard=True)
    scene limb_intro_prezent_limb_2_ground
    show limb_intro_prezent_limb_2
    with dissolve2
    $ renpy.pause(4,hard=True)
    scene bg limb_space_start with limb_intro_blot
    $ renpy.pause(3,hard=True)
    show limb_intro_prezent_limb_3:
        anchor (0.5, 0.5)
        pos (960, 150)
    with limb_intro_blot
    $ renpy.pause(1,hard=True)
    show un smile pioneer close:
        xalign 0.13
        xanchor 0.5
        yanchor 0.0
    with limb_intro_blot
    $ renpy.pause(1,hard=True)
    show limb_intro_prez_limb_name_1:
        anchor (0.5, 0.5)
        pos (320, 930)
    with pixellate
    $ renpy.pause(1,hard=True)
    show dv guilty pioneer close at fright with limb_intro_blot
    $ renpy.pause(1,hard=True)
    show limb_intro_prez_limb_name_2:
        anchor (0.5, 0.5)
        pos (1650, 930)
    with dissolve
    $ renpy.pause(1,hard=True)
    show sl smile2 pioneer behind un at left
    show mi smile pioneer behind dv at right
    with limb_intro_blot
    $ renpy.pause(1,hard=True)
    show limb_intro_prez_limb_name_3:
        anchor (0.5, 0.5)
        pos (530, 650)
    show limb_intro_prez_limb_name_4:
        anchor (0.5, 0.5)
        pos (1270, 650)
    with dissolve
    $ renpy.pause(1,hard=True)
    show limb_intro_prez_limb_name_5:
        anchor (0.5, 0.5)
        pos (940, 360)
    with limb_intro_blot
    $ renpy.pause(1,hard=True)
    show us dontlike pioneer far behind sl:
        anchor (0.5, 0.5)
        pos (0.45, 1.5)
        ease 0.5 pos (0.45, 0.5)
        ease 0.1 pos (0.45, 0.6)
    $ renpy.pause(2,hard=True)
    scene bg black with dissolve2
    $ renpy.pause(1,hard=True)
    scene bg semen_room_mars with limb_intro_hand
    $ renpy.pause(2,hard=True)
    scene bg semen_room_dorian with Dissolve(2)
    $ renpy.pause(1,hard=True)
    show limb_intro_prezent_limb_4:
        anchor (0.5, 0.5)
        pos (0.5, 0.5)
    with limb_star
    $ renpy.pause(1,hard=True)
    scene bg black
    show limb_intro_prezent_limb_5:
        anchor (0.5, 0.5)
        pos (0.5, 0.5)
        zoom 1
    with limb_intro_blot
    pause 1
    stop music fadeout 10
    hide limb_intro_prezent_limb_5
    show limb_intro_prezent_limb_6:
        anchor (0.5, 0.5)
        pos (0.5, 0.5)
        zoom 1
        pause 2
        ease 3 pos (0.455, 0.41) zoom 0.416
    show limb_intro_rama:
        anchor (0.46, 0.41)
        pos (0.5, 0.5)
        zoom 2.8
        pause 2
        ease 3 anchor (0.5, 0.5) pos (0.5, 0.5) zoom 1
    with limb_intro_blot
    $ renpy.pause(7,hard=True)
    $ limb_set_volume('sound', 1, 0)
    play sound sfx_click_3
    scene bg black with fade
    $ renpy.pause(2,hard=True)

label limb_life_biker_new:

    scene bg black
    pause 3
    show cg limb_words_2 with dissolve2
    $ renpy.pause(15)
    hide cg limb_words_2 with dissolve2
    pause 1
    $ prolog_time()
    $ save_name = ("Лимб. \nДетство.")
    play ambience ambience_int_cabin_evening fadein 3
    play music pl_gk_suncave fadein 5
    scene bg black
    pause 1
    scene bg int_table_pl_1
    show limb_eff_photo
    with dissolve2
    pause 3
    show blinking

    "Я в гостиной. Тут тихо, солнечно и спокойно."
    "Мне 6 лет, и я люблю мотоциклы. "

    scene bg int_table_pl_2 with dissolve2

    "Я выпрашиваю у родителей журналы про спорт или одежду, которые они постоянно читают, и нетерпеливо листаю тяжелые глянцевые страницы, чуть ли не надрывая... пока не нахожу фотографии, которые с упоением разглядываю."

    show pl_multi_1 at limb_multi_1()

    "На день рождения, который у меня уже скоро, я прошу как можно больше моделей самых разных мотоциклов, и точно знаю, что, когда вырасту, у меня будет свой гоночный байк."
    "На странице журнала вдруг замечаю автобус. Он кажется знакомым[pl_ell] Интересно, почему?"

    $ limb_conversion(4, "ext_city_dv", 2, "Ночная музыка", "night", "moto", None)
    play ambience ambience_cold_wind_loop fadein 3

    "Мне 19, и я люблю мотоциклы.{w=1} Простите. "

    play music pl_gk_blue_note_sessions fadein 5

    "Все свои деньги я трачу на две вещи - свою девушку и своего железного товарища. "
    "Её зовут Алиса, она студентка медколледжа и любит музыку[pl_ell] Иногда кажется, сильнее, чем меня. Впрочем, я и сам не без греха."
    "Мой мотоцикл - Хонда CB400, вечная классика для всех начинающих. Я купил его пару месяцев назад по дешёвке. "
    "Передний тормоз барахлит, кое-где ещё осталась ржавчина после чистки и нужно заменить подвески, но я все равно счастлив. Родители были против - но это уже не важно."

    play ambience ambience_limb_road_noise fadein 3 fadeout 3
    scene bg ext_city_moto
    show prologue_dream
    with flash

    "Мы катаемся каждый день. Алиса обнимает меня сзади, и это приятно. Надо будет не забыть купить второй шлем, а то без него ветер выдувает все мысли из моей, и без того пустой, головы. "

    stop ambience fadeout 2
    scene bg ext_hospital_morning
    show pl_dv_dress_smile at left
    show pl_moto_5 at limb_moto_pos
    with flash

    "Утром я подвез её до колледжа, сам добрался до своей шараги. Даже забавно, мне одновременно нравится моя жизнь и кажется, что в ней чего-то не хватает."

    $ limb_set_volume('music', 0.1, 3)
    play ambience ambience_medium_crowd_indoors_1 fadein 2
    scene cg epilogue_us_blur with flash

    "Я будто одержим мотоциклами и Алисой, которая отлично к ним подходит, а всё остальное расплывается, будто заблюрено[pl_ell] будто в тумане."
    "Ладно[pl_ell] Еле-еле отсидев положенный срок, я погнал к колледжу моей ненаглядной меломанки. А она не заставила ждать."

    $ limb_set_volume('music', 1, 3)
    stop ambience fadeout 3
    scene bg ext_hospital_sunset_2:
        anchor (0, 0.2)
        zoom 1.5
    show pl_dv_dress_fap at left
    with limb_lap

    dv "Ну привет, ковбой."
    plme "Привет, заяц. Как день?"
    dv "Ну как, как[pl_ell] Скучно.{w=0.5} Бессмысленно.{w=0.5} До сих пор не понимаю, надо ли мне это."
    plme "И у меня так же. "

    $ limb_sprite_switch('pl_dv_dress_', 'fap', 'smile', dspr, left)

    dv "А я и не спрашивала. "

    with vpunch

    "Я схватился за куртку, изображая сердечный приступ. "

    scene bg ext_hospital_sunset_2
    show pl_moto_1_sunset at limb_wobble
    with dissolve

    "Алиса переступила через труп шутки и довольно эротично уселась на мотоцикл. По-свойски похлопала меня по ноге: "
    dv "Слезай, я здесь главная. "
    plme "Права получи сначала, Князь Тьмы. "
    "Рыжая только фыркнула. Я передал ей шлем."
    dv "Ооо, моя корона! Спасибо, слуга. "
    plme" Ещё раз, и[pl_ell]"

    scene bg ext_hospital_darken

    "Моё притворное возмущение потонуло в поцелуе. Ну и чего тебе в жизни не хватает, спрашивается?"

    pause 1

    "Я дождался, пока Алиса накинула куртку, а потом[pl_ell] А потом мы погнали. "

    play music pl_dn_obvious fadein 3 fadeout 3
    $ limb_set_volume('ambience', 0.5, 0)
    play ambience ambience_limb_road_noise fadein 3 fadeout 3
    scene bg ext_city_moto with flash

    "Улицы города начали сменять друг друга, как в калейдоскопе, а потом и вовсе потонули во мраке за спиной. Уже за чертой[pl_ell]"

    scene bg ext_road_moto_2 at limb_shake
    show pl_moto_4:
        anchor (0.5, 0.5)
        pos (0.5, 0.6)
    with dissolve2
    stop ambience fadeout 4

    "Мы полетели между двух лугов. Под звёздным небом. Романтика[pl_ell] "
    "Алиса обняла меня покрепче. А я покрепче вцепился в руль. Идиллия!"
    "Тем круче, что не совсем стандартная комплектация, приборная панель будто от другого мотоцикла и даже не самая популярная расцветка - всё делает этот мотоцикл уникальным. "
    "Дорогу уникальной.{w=1} Город уникальным.{w=1} Меня уникальным. "
    "Хорошо, что дорогу недавно заасфальтировали. Вдали горят огни другого, большего города, в котором мы и живём. "

    scene bg ext_road_moto_1:
        anchor (0.5, 0.5)
        pos (0.5, 0.5)
        zoom 1
        ease 1 zoom 1.3
    show pl_moto_4:
        anchor (0.5, 0.5)
        pos (0.5, 0.6)
    with dissolve
    pause 1
    $ limb_sprite_switch('pl_moto', '_4', '_2', dspr, limb_custom_pos(0.5, 0.6))
    with dissolve

    "Я притормозил, добравшись до перекрёстка. "
    dv "Ты чего? "
    plme "Просто[pl_ell] Красиво очень. "
    "Алиса красиво шмыгнула носом. "

    window hide
    scene bg ext_road_moto_1:
        anchor (0.5, 0.5)
        pos (0.5, 0.5)
        zoom 1.3
    show pl_moto_2 at limb_wobble
    pause 2
    scene bg ext_road_moto_0 with dissolve
    pause 1
    show pl_dv_dress_normal_night with dissolve
    pause 1
    window show

    "Потом, немного важничая, слезла с мотоцикла, сделала пару шагов[pl_ell] Я уже знал, чего ожидать."
    plme "Слушаю."
    dv "Тебе не кажется, что в твоей жизни что-то где-то пошло не так?"
    plme "Конечно, кажется. Год назад я встретил нечто ужасное. Эта девушка[pl_ell]"

    with hpunch

    "Увернувшись от тумака, я потерял желание продолжать."

    $ limb_sprite_switch('pl_dv_dress_', 'normal_night', 'smile_night', dspr, None)

    dv "И так будет с каждым. Так вот[pl_ell]"

    $ limb_sprite_switch('pl_dv_dress_', 'smile_night', 'normal_night', dspr, None)

    dv "Ты в символизм веришь? "
    plme "Вообще не особо. Но в такие вечера[pl_ell] Думаю, да."
    dv "Тебе какие-то цифры не встречаются постоянно? "
    plme "Не замечал такого.{w=1} А что?{w=1} Ты что, уже планируешь бе[pl_ell]"

    $ limb_sprite_switch('pl_dv_dress_', 'normal_night', 'fap_night', dspr, None)

    dv "Хо-{w=0.5}ро-{w=0.5}шень-{w=0.5}ко{w=0.5} подумай, прежде чем договорить. "
    plme "[pl_ell]"

    $ limb_sprite_switch('pl_dv_dress_', 'fap_night', 'smile_night', dspr, None)

    dv "Так-то. "

    window hide
    scene bg ext_road_moto_1 with dissolve
    pause 1
    show pl_moto_2 at limb_wobble
    with dissolve2
    pause 2
    scene bg ext_road_moto_2 at limb_shake
    show pl_moto_4:
        anchor (0.5, 0.5)
        pos (0.5, 0.6)
    with dissolve
    window show

    "И вот мы снова катим по дороге, уже к другому городу, к дому. Как электроны в схеме от одного реле к другому. Или скорее от лампочки?"
    "Ветер становится сильнее, бьет в лицо, глаза слезятся[pl_ell] я начинаю притормаживать, несмотря на недовольные тычки со спины. "

    window hide
    play sound sfx_limb_crash
    stop music
    scene bg ext_road_moto_3 at limb_shake
    show pl_moto_4:
        anchor (0.5, 0.5)
        pos (0.5, 0.6)
    with flash
    scene bg black with flash_red
    $ sunset_time()
    pause 3
    window show

    "Боль. "
    "Тело разваливается на куски. "
    "Я попытался закричать. "
    plme "А[pl_ell] Али[pl_ell] са[pl_ell] "
    "Нет ответа. "
    "Я не могу двигаться, помогите мне, кто-нибудь, пожалуйста!"
    plme "Алиса[pl_ell]"

    play music pl_ae_blow_with_the_fires_remix

    "Нет ответа. "
    "Зачем нужны эти чёртовы шлемы и куртки, зачем нужны правила, если можно так[pl_ell]"
    "Нет{w=1}, нет{w=1}, нет[pl_ell]"

    with vpunch

    plme" А-Алиса! "

    window hide
    pause 2
    window show

    "Он даже не остановился[pl_ell]"
    "Над головой чёрное небо. На нём нет луны. На нём нет звёзд. И мотоциклов нет. И Алисы тоже[pl_ell] нет."

    with vpunch

    plme "АЛИСА!!!"
    "Шея не хочет поворачиваться, руки не двигаются, но я должен, должен её спасти, проклятье, проклятье, помогите мне,"

    with vpunch

    plme "ПОМОГИТЕ!"

    with vpunch

    plme "ПОЖАЛУЙСТА, КТО-НИБУДЬ!"
    plme "Я должен знать, что она жива, я ДОЛЖЕН!"
    plme "Почему[pl_ell]"
    plme "Стоп."
    plme "Так вот оно как[pl_ell]"
    "Надежды нет."
    "Я возвращаюсь."

label limb_life_chef_new:

    $ limb_conversion(4, "black", 1.5, "Детство", None, None, renpy.random.randint(1,16))

    pause 3
    show cg limb_words_3 with dissolve2
    $ renpy.pause(15)
    hide cg limb_words_3 with dissolve2
    pause 1

    play music pl_gk_suncave fadein 5
    play ambience ambience_int_cabin_evening fadein 3
    scene bg int_kitchen_pl
    show limb_eff_photo
    with dissolve2
    pause 3
    window show

    "Мне 6 лет, и я не люблю мотоциклы. "

    show pl_multi_2 at limb_multi_2

    "Часто сижу на кухне. Журналы давно заброшены. Теперь я люблю смотреть, как мама готовит. Подолгу наблюдаю, как она обжаривает овощи, подливает масло, шинкует и фарширует. Чувствую, что это пригодится в будущем. "
    "Я помню Алису и хочу найти её через 13 лет. "
    "В будущем я стану поваром."

    $ limb_conversion(4, "int_dining_hall_people_evening", 2, "Чай без сахара", "night", "cheef", None)

    play ambience ambience_dining_hall_full fadein 5

    "Мне 19."

    play music pl_gk_everlasting_summer_remini fadein 8

    "В последнее время меня слегка беспокоит[pl_ell] одно имя. С детства его помню. Но я не знаю, кто такая Алиса или откуда её знаю. Да и когда в последний раз с девушками общался, право дело[pl_ell]"
    "В детстве я воображал себя то гонщиком, то художником, а потом как-то начал засиживаться с мамой на кухне, и вот[pl_ell]"
    "Я хорошо готовлю. "
    "Работаю в простеньком ресторане, скорее даже общепите, пока только младшим поваром. Здесь советская тематика, всё опрятно и как-то[pl_ell] знакомо. Все так говорят."

    stop ambience fadeout 5
    scene bg ext_admins_day
    show prologue_dream
    with flash

    "Когда я прихожу помочь маме по дому, она не может нарадоваться и хвалит меня. Это приятно. "

    scene bg ext_city_house_sunset with flash

    "Когда я возвращался домой, мне позвонили. Пригласили завтра днём на реалити-шоу для начинающих готовить. Меня. 19-летнего пацана, который в день слов десять произносит[pl_ell]"
    "Это что, мама сделала мне подарок?"

    scene cg limb_bus_sunset with dissolve2
    play sound sfx_bus_interior_moving

    "Ну что ж. На следующий день я пришёл по адресу. Точнее, приехал на автобусе. Программа, как ни странно, снимается на открытой природе."
    "Забавно. Их символом, кажется, выступает сурок. Как в известном мне хорошем фильме[pl_ell] Или нет? "

    stop sound fadeout 3
    play ambience ambience_camp_entrance_day_people fadein 3 fadeout 3
    scene bg ext_playground_day
    show pl_culinary_show_day
    with dissolve
    pause 1
    show pl_sh_3 at fleft
    with dissolve
    pause 0.8
    show pl_el_actor_1 at fright:
        zoom 1.2
    with dissolve
    pause 0.8
    show pl_ma_limb_2_alt
    with dissolve

    "В телешоу, помимо меня, участвуют какие-то актеры и певица, которые красиво улыбаются и смешно шутят. Но готовить они не умеют, поэтому я легко побеждаю в самом состязании по готовке. "
    "Певица показалась мне смутно знакомой."

    hide pl_culinary_show_day
    show pl_culinary_show_darken
    hide pl_sh_3
    show pl_sh_2 at fleft
    hide pl_el_actor_1
    show pl_el_actor_2 at fright:
        zoom 1.2
    hide pl_ma_limb_2_alt
    show pl_ma_queen_glitch
    with limb_lap
    play ambience ambience_ext_road_day fadein 6 fadeout 6
    "Главный приз - мотоцикл, но я почему-то отказываюсь в самый последний момент и беру только пачку денег, награду за второе место. "

    scene bg ext_no_bus with dissolve
    play music pl_dn_bad_future_remix fadein 6 fadeout 4

    "Когда я выхожу с территории съемочного павильона, где была тень, по-прежнему светит солнце. Жарко[pl_ell]"
    "Следующий автобус будет через[pl_ell] мда. "
    "Хочется пройтись. "

    scene bg ext_road_evening with flash

    "Я иду вверх по просёлочной дороге, сжимая в руке кошелек. Навстречу - ни души. "
    "Солнцепёк дневной медленно сменяется пеклом вечерним. Духота стоит такая, что, видимо, скоро будет дождь[pl_ell]"
    "Я невольно задумался о том, почему моя жизнь складывается именно таким образом. Я когда-то свернул не туда? Или наоборот - это мой максимум? Я готов на всё, только бы не[pl_ell] чувствовать себя беспомощным?"

    play sound sfx_gusty_wind
    play ambience ambience_ext_road_night fadein 3 fadeout 3
    scene bg ext_road_darken

    "Кажется ли мне, что что-то не так? Неправильно? Люди вокруг постоянно видятся старыми знакомыми, которых я почему-то не узнаю. "
    "Да и цифры. Мне часто попадаются одни и те же цифры. А вот какие - вспомнить не могу[pl_ell]"
    "Мою череду мыслей прервал порыв ветра, принесший с собой прохладу. "

    scene bg ext_road_night_auto with dissolve2

    "Оказывается, неплохо так потемнело. "
    "Мимо меня проехал тот самый автобус, которого я не ждал. Потом мотоцикл. Потом две машины[pl_ell]"
    "Я устало вздохнул. "

    stop sound fadeout 5

    "Но вот вдали сияют огни города. Дойду - похвастаюсь маме победой, что ли. Можно и позвонить, но я как-то соскучился по человеческому общению."

    scene bg ext_road_cheef_1 with dissolve2

    "Навстречу с огромной скоростью едет машина. Я благоразумно отошёл на обочину."

    window hide
    play sound sfx_limb_crash
    stop music
    stop ambience
    scene bg ext_road_cheef_2 with flash
    scene bg black
    with vpunch
    pause 1

    "Ничего не успел понять. "

    $ sunset_time()
    $ limb_mute(2)
    show limb_blood_frame with dissolve2
    $ limb_set_volume('sound', 0.2, 0)
    play sound sfx_limb_heart
    window show

    "Наверное, машина потеряла управление. "
    "Наверное, он сбил меня случайно."
    "Наверное, сядь я на грёбаный автобус, ничего такого не случилось бы."
    "Купюры разлетаются по ветру[pl_ell] Наверное. "
    "Я же толком и пожить не успел[pl_ell]"
    plme "[pl_ell]!"
    "Я попытался заорать от страха и разочарования, но[pl_ell]"

    stop sound

    "Вокруг - мягкая темнота без проблеска света.{w=0.8} Без звука.{w=0.8} Без проблеска надежды."
    "И я всё понял.{w=0.5} Снова.{w=0.5} Всё вспомнил[pl_ell] снова."
    "Я возвращаюсь[pl_ell] Странно, что меня так часто сбивают на этой дороге. "

    window hide
    $ renpy.pause(1,hard=True)
    stop ambience fadeout 2
    show anim limb_conversion with dissolve2
    pause 1
    show pl_dv_cheef_ghost:
        alpha 0.7
    with dissolve
    pause 3
    play music pl_ae_trevoga
    show pl_mi_queen at fright
    with pixellate
    pause 2
    window show

    plme "Это[pl_ell] та Алиса?"

    hide pl_dv_cheef_ghost with flash

    plts "Не отвлекайтесь, пожалуйста, на девушку в красном. "
    plme "Чт[pl_ell] "
    plts "Мистер Персунов, Вы не зря к нам обратились. Не обращайте внимание на чувство дежавю. Не забывайте, что Вы - один из тринадцати."

    with vpunch

    plme "Что со мной происходит?!{w=0.8} О чём ты?!"
    plts "Вы сами решаете, что правда. Вы сами выбираете мир, в котором живёте. "
    plme "Да кто[pl_ell] Кто ты?"
    plts "Делайте свой выбор с умом, мистер Персунов, кем бы Вы ни были в этот раз."
    plts "И помните: Вы здесь не просто так."

    hide window
    pause 2

    jump limb_life_choice

label limb_life_biker:

    $ limb_conversion(4, "int_table_pl_2", 1, "Детство", None, None, renpy.random.randint(1,16))
    play ambience ambience_int_cabin_evening fadein 3
    play music pl_gk_suncave fadein 3
    with Dissolve(3.0)
    show blinking

    "Мне 6 лет, и я люблю мотоциклы."
    "Я выпрашиваю у родителей журналы про спорт или одежду, которые они постоянно читают, и нетерпеливо листаю тяжелые глянцевые страницы, чуть ли не надрывая их, пока не нахожу их фотографии, которые с упоением разглядываю."
    "Но один мне нравится больше всех: \"Suzuki Hayabusa\". Такой же мотоцикл я часто вижу во снах. Ночь. Я со своей девушкой лечу на этом мотоцикле по полупустой улице."
    "Может в прошлой жизни я также любил мотоциклы?"
    "На день рождения, который у меня уже скоро, я прошу как можно больше моделей самых разных мотоциклов, и точно знаю, что, когда вырасту, у меня будет свой гоночный байк."

    $ limb_conversion(4, "ext_city_dv", 5, "Ночная музыка", "secret", "moto", None)

    play ambience ambience_cold_wind_loop fadein 3
    play music pl_ef_dubstep_5 fadein 3

    "Мне 19, и я люблю мотоциклы. Все свои деньги я трачу на на две вещи - свою девушку и свой мотоцикл."
    "Её зовут Алиса, она студентка медколледжа и любит спорт. Мой мотоцикл - Suzuki Hayabusa, это один из самых быстрых мотоциклов. Я купил его на прошлой неделе по дешёвке."
    "Передний тормоз барахлит и нужно заменить подвески, но я всё равно счастлив. Родители были против - но это не важно."

    play ambience ambience_limb_road_noise fadein 3 fadeout 3
    scene bg ext_city_stray with flash

    "Мы катаемся каждый день. Алиса обнимает меня сзади, и это приятно. Утром я подвез её до колледжа, а ночью мы гоняем по полупустым улицам. "
    "Мой шлем, наверное, бракованный - ветер бьёт под забрало, глаза слезятся, и[pl_ell]"

    scene bg black with vpunch
    play sound sfx_limb_crash
    stop ambience
    stop music

    "[pl_ell]я не замечаю, как пикап поворачивает со встречной. "

    pause 2

    "Боль. {w=1} Затем тишина. Алиса, кажется, мертва, я не могу двигаться и вижу только безжизненное черное небо.{w=1} Без единой звезды.{w=1} Без надежды."
    "Я возвращаюсь."

label limb_life_chef:

    $ limb_conversion(4, "int_kitchen_pl", 1, "Детство", None, None, renpy.random.randint(1,16))

    play ambience ambience_int_cabin_evening fadein 3

    "Мне 6 лет, и я не люблю мотоциклы."
    "Я люблю смотреть, как мама готовит. Подолгу наблюдаю, как она обжаривает овощи, подливает масло, шинкует и фарширует."
    "Это пригодится. Я помню Алису и хочу найти её через 13 лет. "
    "В будущем я стану поваром."

    $ limb_conversion(4, "int_caffee_day", 5, "Чай без сахара", "secret", "cheef", None)

    play ambience ambience_camp_center_evening fadein 3
    play music pl_st_a2e13lam fadein 3

    "Мне 19. Не помню, кто такая Алиса, или откуда её знаю. Помню только имя."
    "Я хорошо готовлю. Работаю в хорошем ресторане, но пока только младшим поваром. Когда я прихожу помочь маме по дому, она не может нарадоваться и хвалит меня. Это приятно. "

    play ambience ambience_limb_hard_rain fadein 5 fadeout 3
    scene bg ext_city_sunset_2
    show limb_eff_hard_rain_r
    with limb_lap

    "Меня пригласили на реалити-шоу для начинающих готовить. Кажется, мама сделала мне подарок. Там учавствуют какие-то актеры и певица, которые красиво улыбатся и смешно шутят. Но готовить они не умеют, поэтому я легко побеждаю."
    "Главный приз - мотоцикл, но я почему-то отказываюсь и беру только немного денег. "

    scene bg ext_square_night_city
    show limb_eff_hard_rain_r
    with limb_lap

    "Когда выхожу из здания, начинается дождь. Я иду вверх по улице, сжимая в руке кошелек. Навстречу спешит поток людей. Меня буквально пробрало холодом, будто в предчувствии чего-то нехорошего."
    "Меня толкают, я поскальзываюсь - и падаю прямо под ноги толпе. Купюры разлетаются по ветру[pl_ell]"

    scene bg black with vpunch
    play sound sfx_bodyfall_1
    stop ambience fadeout 3

    "Дождь, кажется, по-прежнему идет, но я не вижу и не слышу его. Вокруг - мягкая темнота без проблеска света. Без проблеска надежды."
    "Я испытал неприятное чувство дежавю. Будто бы давно - может, в прошлой жизни? - со мной это уже случалось[pl_ell]"
    "Я возвращаюсь."

label limb_life_choice:

    $ limb_conversion(4, "int_open_door", 1, "Детство", None, None, renpy.random.randint(1,16))

    if 'ed_work_prep' in mods.keys():
        show pl_ach_limb_loner with dissolve

    play ambience ambience_int_cabin_evening fadein 3

    "Мне 6. Я не знаю, чем заняться в доме, и иду[pl_ell]"

    window hide
    pause 1
    menu:
        "В гараж":
            play ambience ambience_music_club_day fadein 3
            scene bg int_clubs_male_day with dissolve

            "[pl_ell]к папе в гараж. Его там нет, но зато есть много-много интересных вещей."
            "Моё внимание привлекает воронка для масла. На ней сохранились пара тёмных капель, и глядя на них, я вдруг думаю: как, наверное, много-много в мире самых разных жидкостей?.."
            if limb_workshop_old == True:
                jump limb_life_garage
            else:
                jump limb_life_garage_new
        "В мастерскую":
            if limb_garage_old == True:
                jump limb_life_workshop
            else:
                jump limb_life_workshop_new
        "В прихожую":

            play ambience ambience_music_club_night fadein 3
            scene bg int_door_sunset with dissolve

            "[pl_ell]куда глаза глядят.{w=1} Попадаю в прихожую. "
            "Там совсем нечего делать, а я не хочу выходить из дома. "
            "Вспоминаю, что у меня в комнате есть разные машинки. Хочется поиграть! "
            "Мой взгляд падает на ботинки отца. Они массивные, грубые. "
            "Я думаю о машинах и о ботинках. Интересно, много ли папа путешествовал?"

            jump limb_life_adventurer

label limb_life_garage_new:

    $ limb_conversion(4, "semen_room_clean", 2, "Breaking sad", "night", "chemist", None)
    $ persistent.sprite_time = 'night'
    show sl smile2 dress at left
    show pl_sh_2_night at right
    with dissolve2
    play ambience ambience_medstation_inside_night
    play music pl_gk_meeting_of_good_friends fadein 3

    "Мне 19 лет, и вчера я поступил в довольно престижный университет на химический факультет. С детства обожаю смешивать разные вещества и смотреть, что получается."
    "Мои родители недавно развелись, мать уехала, отец в больнице[pl_ell] Но мои друзья - Саня и Славяна - меня поддерживают. Это приятно."
    "Они тоже будущие ученые. Саня, как и я, химик (но куда способнее, честно говоря), он хочет улучшить формулу тротила и увеличить теплоту его взрыва. А Славяна - физик, она хочет развивать смежные с медициной направления."
    "Мы часто разговариваем, и часто ставим опыты, в основном с Сашей. В последний раз чуть ли не задохнулись в его квартире, но, к счастью, обошлось."
    "В общем, дружим с самого детства. Аж завидно становится самому себе, хаха."
    "Вот и сегодня мы собрались у меня в комнате для обсуждения важного вопроса - как отмечать день рождения Славяны. "
    "Вариантов много: пойти на научную выставку (вариант Александра), устроить пикник (мой) или никак (понятно чей)."
    "Славяна нервно гладит косу, пока мы с серьёзным видом толкаем пафосные речи - очень смущается. Мы с Саней, конечно, специально."
    plsl "Давайте просто втроём посидим где-нибудь! "

    show sl shy

    "Предприняла последнюю попытку наша Мисс Кон-Правильность."

    $ limb_sprite_switch('pl_sh_', '2_night', '1_night', dspr, right)

    plbs "Ну как можно! "
    "Хором возмутились два друга. "

    $ limb_sprite_switch('pl_sh_', '1_night', '3_night', dspr, right)
    show sl tender

    plsl "Ну мальчики[pl_ell] "
    "Зарделась Славя и отвернулась к стене. Полагаю, тоже притворничает. "

    hide pl_sh_3_night with dissolve2
    pause 1
    show sl serious with dspr
    pause 0.5
    show sl serious at center with moveinright

    "И действительно, стоило Сане отлучиться по делам житейским, Славяна повернулась ко мне и неожиданно серьёзно сказала: "

    stop music

    plsl "Семён, ты должен прекратить это."
    "Слегка ошарашенный твёрдостью её тона, я начал было лепетать про шутки и дружбу, но[pl_ell]"

    show sl angry with dspr

    plsl "Семён!{w=0.8} Я не про эту ерунду!{w=0.8} Я про тебя!"
    plme "Что[pl_ell]"

    show sl sad with dspr

    plsl "У меня мало времени! Мы все о тебе беспокоимся, и к тому же у нас[pl_ell]"

    show sl surprise at cright with moveinright
    show pl_sh_2_night at fleft with dissolve

    plsn "Славя?{w=0.8} Семён?{w=0.8} Я что-то пропустил?"
    "Непривычно грубо прервал нас Са[pl_ell] Александр. Откуда он взялся, я же не слышал[pl_ell]"

    show sl sad with dspr
    play music pl_uc_suburbs fadein 3

    plsl "Семён, я[pl_ell]"
    plsn "Приятель, можно тебя на секундочку?"
    "В той же резкой манере прервал её мой лучший друг. "
    "Мой лучший друг? "
    "Он никогда так[pl_ell]"

    stop ambience
    play sound sfx_close_door_campus_1
    scene bg int_floor_night
    show pl_sh_2_night at cright
    with dissolve
    with vpunch

    "Мы вышли на лестничную площадку, за мной как-то мрачно захлопнулась дверь, и я внезапно испугался."
    plme "Саня, что[pl_ell]"
    plsn "Через 1 час 16 минут 23 секунды произойдёт конец света.{w=1} Ты предотвратишь это."
    plme "Ты что, клеем надышался[pl_ell]"
    plsn "Спускайся вниз по лестнице.{w=0.8} Через три пролёта ты споткнёшься на 43-ей по счёту ступеньке, упадёшь вперёд, сломаешь лучевую кость слева, потом 7-е ребро справа, потом шею на уровне 5-го позвонка."
    "Я попытался нервно засмеяться[pl_ell]"

    stop music
    $ limb_set_volume('sound_loop', 0.7, 0)
    play sound_loop sfx_limb_heart fadein 3
    play sound sfx_limb_horror
    scene bg int_floor_invers
    show pl_sh_2_invers at cright
    with dspr

    "И с ужасом понял, что моё тело мне не подчиняется. "
    "Моё тело, держась неестественно прямо, повернулось, сделало шаг вперёд[pl_ell] другой[pl_ell] "

    scene bg int_floor_night
    show pl_sh_2_night at cright
    with dissolve2
    play sound sfx_limb_steps_1

    "Вокруг всё как в тумане. Я взвыл от ужаса, но физическая оболочка, ставшая внезапно тюрьмой, не издала ни звука."
    "Мысли в голове - со скоростью света.{w=0.8} \"Этого не может быть!\"{w=0.8} \"Как мне себя ущипнуть?!\"{w=0.8} \" Это же просто шутка, да?!\""

    $ limb_flow_transition("int_floor_night", limb_shake)
    stop sound_loop

    "Тело миновало первый пролёт."

    play music music_list["orchid"] fadein 3

    "Я заорал, забился у себя в голове, но жуткая реальность никуда не исчезла. "
    "Наоборот, в голове застучало: "
    th "Это какая ступенька была?! Пятнадцатая?!"
    th "Думай,{w=0.8} думай,{w=0.8} пролётов у тебя в доме четырнадцать[pl_ell]"
    th "Это шестнадцатая, это семнадцатая[pl_ell]"

    scene bg int_floor_night at limb_shake
    with vpunch

    th "Нет, нельзя считать, нельзя!!!"
    th "Девятнадцатая[pl_ell]"
    th "Нет, думай о другом, вот о дне рождения Слави, например, вот что ты ей подаришь, а?!"
    th "Она[pl_ell] она пыталась меня предупредить!"
    th "Двадцать семь[pl_ell]"
    th "Нет! Нет! Я не хочу умирать! Остановись"

    $ limb_flow_transition("int_floor_night", limb_shake)

    "Тело миновало второй пролёт."
    th "Пожалуйста, пусть это будет розыгрыш, пранк, дружеский прикол, пожалуйста!"
    "Мы пару раз разыгрывали Славю[pl_ell] Я думал, это было забавно, но сейчас я понял, я правда понял, как это было жестоко!"
    th "Тридцать четыре."
    th "Боже, если ты есть, спаси меня, я не верил, но если выживу[pl_ell]"
    "Мне стало стыдно[pl_ell] и ещё страшнее от того, насколько я боюсь смерти."
    th "Тридцать восемь."
    th "Пожалуйста, пусть это хотя бы будет быстро."

    $ limb_flow_transition("int_floor_night", limb_shake)

    "Моё тело прошло последний пролёт.{w=1} Замерло.{w=1} Сделало шаг."
    "И вдруг я ощутил, что могу снова управлять им. "
    "Не успев ничего осмыслить, судорожно останавливая движение вперёд, я[pl_ell]"

    scene bg black with vpunch
    stop music

    th "Зацепился.{w=0.8} Как глупо[pl_ell]"
    "[pl_ell]"
    "Я жив?"
    "Или нет[pl_ell]"
    "Неужели эта история моей жизни - одна из многих?"
    "Нет, здесь что-то не так. Что-то[pl_ell]"
    "Тут кто-то есть!"

    play music pl_ae_trevoga fadein 2

    plv "Через 1 час 13 минут 7 секунд произойдёт конец света.{w=0.8} Ты предотвратишь это."
    plme "Как?"
    plv "Умереть."

    with vpunch

    plme "Я не хочу!{w=1} Кто ты?"
    plv "Тот, кого ты убил.{w=0.5} Убьёшь.{w=0.5} Убил[pl_ell] Убьёшь[pl_ell]"
    plme "Я никого не[pl_ell] Что значат все эти цифры?"
    plv "Ничего. Вокруг только ложь."

    $ limb_garage_old == True
    jump limb_life_stray

label limb_life_garage:

        $ limb_conversion(4, "semen_room_clean", 5, "Breaking sad", "secret", "chemist", None)
        $ persistent.sprite_time = 'night'
        show sl smile2 dress at left
        show pl_sh_2_night at right
        with dissolve2
        play ambience ambience_medstation_inside_night
        play music pl_gk_meeting_of_good_friends fadein 3

        "Мне 19 лет, и вчера я поступил в довольно престижный университет на химический факультет. С детства обожаю смешивать разные вещества и смотреть, что получается."
        "Мои родители недавно развелись, мать уехала, отец в больнице[pl_ell] Но мои друзья - Саня и Славяна - меня поддерживают. Это приятно."
        "Они тоже будущие ученые. Саня, как и я, химик (но куда способнее, честно говоря), он хочет улучшить формулу тротила и увеличить теплоту его взрыва. А Славяна - физик, она хочет развивать смежные с медициной направления."
        "Мы часто разговариваем, и часто ставим опыты, в основном с Сашей. В последний раз чуть ли не задохнулись в его квартире, но, к счастью, обошлось."
        "В общем, дружим с самого детства. Аж завидно становится самому себе, хаха."

        pause 2

        "Отец зовет меня из гаража - я часто ему помогаю. Отшучиваюсь и улыбаюсь в ответ на подколки друзей и спешу к папе - он в последнее время нетерпелив. Спускаясь по узкой лестнице, я спотыкаюсь и кубарем скатываюсь по ступенькам. "

        play sound sfx_bodyfall_1
        scene bg black with vpunch
        play sound sfx_bones_breaking
        with vpunch

        "Треск. Вероятно, у меня сломана шея, раз я вижу свою спину. Да и плевать. Слышу обеспокоенные голоса - но это уже не важно. Боли нет. Надежды тоже."
        "Я возвращаюсь."

label limb_life_stray:

    $ limb_conversion(2, "int_kitchen_pl", 1, "Детство", None, None, renpy.random.randint(1,16))

    play ambience ambience_int_cabin_evening fadein 3

    "Мне 6 лет, я закатываю истерики, одну за другой. Родители, конечно, не понимают. "

    show pl_multi_3 at limb_multi_1(0.75)

    "У меня не получилось!{w=1} Опять!{w=1} Опять!"
    "Мне хочется сбежать из этой клетки, но я не знаю как и возможно ли это. Но точно знаю, что можно сбежать из этого дома, в котором я знаю каждый дюйм, будто бы жил в нем тысячи жизней[pl_ell]"
    "И я[pl_ell]"

    window hide
    pause 1
    menu:
        "Сбегаю":

            $ limb_conversion(2, "int_mine_room", 2, "Charlotte", "night", "stray", None)
            show pl_hand_record_red with dissolve
            play music pl_st_f21lfm fadein 3
            play ambience ambience_medium_crowd_outdoors

            "Мне 19 лет, и, мягко говоря, моя жизнь - не самая лучшая из всех возможных. Первые несколько лет я ненавидел себя за то, что зачем-то сбежал из родного дома, и отчаянно пытался найти дорогу обратно. "
            "Но система опеки вцепилась в меня крепко, ничего не вышло, и мало-помалу я свыкся с ролью сироты, кочующего из одних заботливых рук в другие."
            "Лет в 14 я начал пить с ребятами с района, в 16 - попробовал наркотики уже на другом конце страны. На нормальную подработку меня не брали, опекуны попадались всё гаже и гаже, и, как только выдалась возможность, я опять сбежал. Всё равно я для них средство заработка, не более. "
            "Нашел себе место рядом с такими же побитыми жизнью бродяжками."

            scene bg ext_hospital_night
            show pl_sl_slut_1_night at left
            show prologue_dream
            with flash

            "С одной из них, Леной, у меня закрутился бурный роман. Хотя сложно сказать, насколько серьезными могут быть отношения с проституткой, которая дает под мостом за дозу. Но секс ничего, во всяком случае, денег с меня она не берет, и это приятно. "

            scene bg ext_city_house_sunset
            show pl_sh_miami_2_sunset at cright
            show prologue_dream
            with flash

            "По профессии, дамы и господа, я уличный воришка. Собственно, эту свою Историю я рассказываю стибренному у какого-то пижона диктофону.{w=0.8} Он молчаливый, но верный слушатель, и по правде говоря, единственный."

            scene bg int_mine_room
            show pl_hand_record_red
            with flash

            "Зачем это?{w=1} От смертельной скуки, наверное. Вряд ли можно вывезти какую-то мораль. Но на всякий случай: дети, не принимайте наркотики! Во всяком случае, пока не стукнет 16."

            scene bg ext_city_cheef with flash

            "В основном я краду деньги у таких же уличных бомжей или у выступающих на переходах музыкантов, но это чревато. В последний раз меня неслабо побили, и я валялся в какой-то канаве и блевал до самого утра, пока горемычного сироту (меня) не прогнал дворник."
            "Час назад обнаружил, что оставил два зуба в том переулке.{w=1} Приспособился свистеть сквозь прорехи."
            "Неспособность улыбаться, а так же то, что мне не продали бутылку за полцены, почти подорвало мой дух. Но словно бы доказывая всему миру, что можно опуститься ещё ниже, я не сдался - и вспомнил про свою девушку!"

            stop ambience fadeout 3
            scene bg int_floor_day with limb_lap
            show pl_sl_slut_2
            show pl_sh_miami_1:
                xanchor 0.5
                xpos 0.95
            with dissolve

            "Я добрался к Лене, надеясь ширнуться или хотя бы на минет, но у неё был клиент. "

            play sound sfx_limb_slap
            with hpunch

            "Поэтому, несмотря на весь, казалось бы, присущий ей альтруизм, она ударила меня по лицу и оставила одного, с разбитыми сердцем и носом. Может быть, потому что я случайно назвал её Славей?{w=1} Забавно."

            play ambience ambience_ext_road_evening fadein 3 fadeout 3
            scene bg ext_city_house_day
            show pl_hand_record_red
            with dissolve2

            "Что же дальше? Я так устал[pl_ell]"

            window hide
            pause 1
            menu:
                "Хватит уже":
                    "\"Возможно, я мог бы стать неплохим писателем\", - мелькнула мысль, когда я лез через ограждения."

                    play ambience ambience_lake_shore_evening fadein 3 fadeout 3
                    play music pl_gk_hardep fadein 5
                    scene bg ext_city_sunset_2
                    show pl_hand_record_red
                    with dissolve

                    "Выдалось непривычно свежее и ясное утро. А может, просто туман в голове развеялся. За спиной жужжат машины, солнце щекочет многострадальное лицо. Это тоже приятно."
                    "А внизу ворочается вода, как древний зверь, и почему-то её неспокойная гладь напоминает мне каплю машинного масла. Или темное небо со множеством звезд-бликов. Всегда можно найти выход. Всегда есть надежда!"

                    show cg limb_hero
                    show pl_hand_record_red
                    with dissolve

                    "Перекинув одну ногу через перила, держа в руке диктофон, я говорю о том, что не пристало уходить со сцены без последней шутки. Хм[pl_ell] когда-то, наверное, в какой-то другой жизни я слышал, что при такой высоте вода при столкновении с телом ведет себя как асфальт. Или очень злой музыкант[pl_ell] "
                    "Я оглядываюсь, в последний раз. Что ж, этому пейзажу точно не хватает ярких красок, прямо как моей жизни! Я бы добавил красного. "
                    "Дерьмовая шутка.{w} Прямо как моя жизнь."

                    show cg limb_hero_jump

                    "Я лечу."

                    play sound sfx_limb_blood_2
                    pause 2
                    jump limb_life_writer

                "Заночевать":

                    stop music fadeout 5

                    "Я поплёлся в сторону парка. Через него можно попасть к одному заброшенному зданию. Там и заночую."

                    play music pl_uc_good_morning_morgan
                    scene bg ext_square_sunset_city with dissolve

                    "Проходя через маленькую площадь в центре парковой зоны, я без всякой мысли скользил взглядом по окружающему миру, пока не наткнулся на статую."
                    "Генда? Что за он? Тут вроде Ленин был."
                    "А, впрочем, какая разница[pl_ell]"

                    play ambience ambience_old_camp_outside fadein 3 fadeout 3
                    scene bg ext_old_building_sunset with limb_lap

                    "Старый товарищ встретил меня разбитыми окнами и щербатой улыбкой покосившегося дверного проема. Я улыбнулся ему, пряча такие же пустые глаза."

                    stop ambience fadeout 3
                    scene bg int_old_building_sunset with fade
                    pause 1
                    scene bg int_mirror_sunset with fade
                    pause 1
                    stop music fadeout 5

                    "Пристроившись в комнате по левую руку от входа, я закутался поплотнее в своё драное пальто и сразу же уснул."

                    show blink

                    "[pl_ell]"

                    scene bg black
                    play music pl_gk_playful_etude_1 fadein 3
                    play ambience ambience_catacombs fadein 3
                    show unblink

                    "[pl_ell]"

                    scene bg int_mine at limb_shake
                    show prologue_dream
                    show pl_sh_dead_night at fleft behind prologue_dream
                    show cs normal glasses far at cright behind prologue_dream
                    show mi dontlike pioneer close at fright behind prologue_dream
                    with dissolve2

                    plgmi "Саймон, скорее!"
                    plme "Где остальные, где Коннор?"

                    show mi shocked with dspr

                    plgmi "Не знаю, снаружи творится какой-то бедлам, все вынуждены носить сахар и бегать от сверчков!"
                    plal "Проклятье, я умираю!"
                    plme "Не надо, не умирай!"

                    hide pl_sh_dead_night
                    show pl_sh_dead_hands_night at fleft behind prologue_dream
                    with dspr

                    plal "Ладно, не буду."

                    show mi scared with dspr

                    plgmi "О боже, Организация уже отправила в прошлое Пионера-2000!"
                    plal "Мы обречены[pl_ell]"
                    plme "Нет, я спасу всех! Где моя машина времени?!"

                    show cs smile far with dspr

                    plpr "Вот она, о герой гаремника."

                    hide pl_sh_dead_night
                    show pl_sh_dead_blood_night at fleft behind prologue_dream
                    with dspr

                    plal "Что ты будешь делать с Пионером-2000? Он ведь жидкий!"
                    plme "Я заставлю его выпить самого себя!"

                    show cs normal far with dspr

                    plpr "Резонно."

                    show mi shy with dspr

                    plgmi "Ты такой храбрый! И умный!"
                    plme "Я знаю это, детка. "
                    plal "Странно, мои часики остановились[pl_ell]"
                    plme "Профессор, машина готова?"
                    plpr "Да, Пионер-2001. Когда окажешься в прошлом, найди парня по имени Гарри, он носит очки и знает, как тобой пользоваться. "

                    show mi cry_smile with dspr

                    plgmi "Я верю в тебя, Пионер-2001! Ты летаешь намного быстрее, чем Пионер-2000!"
                    plme "Спасибо, девчонки! Эль Псай Кон[pl_ell]"

                    hide pl_sh_dead_blood_night
                    show pl_sh_dead_hands_night at fleft behind prologue_dream
                    with dspr

                    plal "Я тоже тут, я всё ещё жив!"
                    plme "Жалко Алекса[pl_ell] у него было много сомнительных положительных качеств."

                    show cs shy far with dspr

                    plpr "Если вам было интересно, почему у меня разные глаза - ответ прост. Я - полувампир, и сейчас съем этого молодого человека!"

                    hide pl_sh_dead_hands_night
                    show pl_sh_dead_blood_night at fleft behind prologue_dream
                    with dspr

                    plal "Не надо, ведь я ещё жив и могу быть полезен для развития сюжета!"
                    plal "А!"

                    show cs normal far at left
                    with moveinleft
                    hide pl_sh_dead_blood_night with dissolve

                    plal "*умирает*"
                    plme "Профессор, может, я могу что-то с собой взять? Оружие, например?"

                    show cs shy glasses with dspr

                    plpr "Можешь взять меня, Пионер, обращайся в любое время."
                    plme "Дайте две."

                    show mi rage with dspr

                    plgmi "Так ты мне изменяешь?! Тогда умри, ведь я тайный агент Организации!"
                    plpr "Какие твисты!"
                    plme "Ну зайчонок, ты же не серьёзно?"

                    scene bg black with vpunch

                    plme "*умирает*"
                    "[pl_ell]"

                    stop music
                    play ambience ambience_old_camp_outside fadein 3
                    scene bg int_mirror_night with flash
                    with vpunch

                    plme "Аааааа!!!"

                    play music pl_ae_obscurity_slow fadein 3

                    "Я вскочил на ноги, отбиваясь от странных людей и событий, которые меня окружали[pl_ell] в какой-то другой жизни."
                    plme "Фух[pl_ell] ну и приснится же такое."
                    "Впрочем, тот мир как-то покрасивше был моей реальности."
                    "И тут подо мной проломился пол."

                    play sound sfx_simon_fall_1
                    scene bg black
                    show int_old_building_night:
                        anchor (0.5, 0.5)
                        pos (0.5, 0.5)
                        ease 0.3 pos (0.5, -0.5)
                    pause 0.4
                    scene bg black with vpunch
                    play ambience ambience_catacombs fadein 3

                    "Диктофон улетел, вращаясь, в темноту."
                    "Я повис над пропастью, отчаянно цепляясь за край."
                    plme "Да я же пошутил[pl_ell]"
                    "Такое ощущение, что тьма за спиной тащит меня вниз."
                    "Я не продержусь, я не[pl_ell]"

                    with vpunch

                    plme "Бл######ть!!!"
                    "Я таращусь остекленевшими глазами в черный и жестокий мир."
                    "Пыль не даёт ничего рассмотреть[pl_ell] Мне на секунду показалось, что я вижу какую-то худую фигуру. Скелет?.. Смерть?.."

                    stop ambience fadeout 3
                    scene bg limb_space_start with dissolve2
                    pause 2

                    "Какое[pl_ell] странное ощущение. Будто разблокировали участок памяти."
                    "Я[pl_ell] много раз жил?"
                    "Это ещё один сон, что ли?"
                    "Я что, типа смогу выбрать ещё раз путь в жизни?"
                    "Да это ах#уенно! "
                    "Я беззвучно рассмеялся, уже не чувствуя боли. Улёт!"
                    "Тогда[pl_ell] я бы хотел заниматься чем-то творческим. И прибыльным. Ох, сейчас я как понавыбираю, сейчас как[pl_ell]"

                    $ limb_conversion(2, "int_editorial_day", 1, "Детство", None, None, renpy.random.randint(1,16))
                    jump limb_life_workshop_new

        "Остаюсь":

            "Боюсь оставить дом и родителей."
            "Тут хотя бы известно, чего ждать."
            "Мне нужно подумать."

            $ limb_conversion(2, "semen_room_green", 2, "Конец света", "night", "410", None)
            scene bg semen_room_hikki

            "Мне 19 лет. "

            play music music_list["a_promise_from_distant_days"]

            "У меня нет мечты, нет цели в жизни, да и самой жизни нет. "
            "Я просто существую. "
            "Когда-то давно, в детстве, во мне что сломалось. "
            "Я сдался. "
            "Сначала я этого не понимал, и пробовал что-то делать. Закончил школу, поступил в универ[pl_ell] вылетел после первого курса. "
            "После этого совсем отрешился от окружающего мира. Не общаюсь с родителями, о чем сильно жалею, не поддерживаю контактов с друзьями[pl_ell] "
            "Сижу в интернете круглыми сутками, кое-как перебиваюсь случайными заработками. "
            "Самое страшное испытание - выйти в магазин. "
            "Однако сегодня - особенный день. "
            "Меня позвали на вечер встречи выпускников. Кто, куда, зачем - не суть. "

            scene anim prolog_1 with dissolve2
            pause 1

            "Я почему-то понял, что именно сегодня смогу что-то изменить. "
            "Осталось решить - съездить на встречу или остаться и позвонить всё-таки маме? "

            window hide
            pause 1
            menu:
                "Пойти на остановку":

                    scene bg black with dissolve
                    stop music fadeout 3
                    $ limb_screens_load()
                    $ day_time()
                    hide anim limb_dialogue_box_410
                    play ambience ambience_cold_wind_loop
                    scene bg bus_stop_flash with limb_lap
                    show limb_eff_hard_snow
                    show anim limb_dialogue_box_410
                    $ _window_hide()
                    $ night_time()
                    pause 3
                    $ _window_show()
                    hide anim limb_dialogue_box_410
                    play sound sfx_intro_bus_stop_steps
                    play music music_list["trapped_in_dreams"] fadein 7

                    "Я шел по ночному, зимнему и непривычному городу, когда в небе сверкнула вспышка. Обернувшись, я успел заметить, как что-то упало с неба. Метеорит? Турбина[pl_ell] от самолета? Разве такое может быть?.."
                    "Погруженный в мысли и время от времени останавливаясь и разглядывая небо, я шёл вперёд. Последний раз столько ходил, когда с год назад в кино водил соседку."
                    "Она заснула минут через десять после начала, а я и вовсе ушел с половины сеанса.{w=1} Мда."

                    show pl_hare_2:
                        anchor (0.5, 0.5)
                        pos (-0.5, 0.78)
                        zoom 0.65
                        ease 10 pos (1.5, 0.55) zoom 1

                    "Улицы были совершенно безлюдные, за исключением какого-то чудака в костюме заяца.{w=0.8} Сером.{w=0.8} Когда я проходил мимо, мне показалось, что он поднял руку, приветствуя меня. Вот ещё! Что за ерунда сегодня творится?"

                    play sound sfx_intro_bus_stop_steps
                    $ limb_set_volume("ambience", 0.2, 5)

                    "Я подошел к остановке."
                    "Буквально через мгновение подъехал автобус.{w=1} Странно[pl_ell] он показался таким знакомым!{w=0.8} И даже, я бы сказал, уютным."

                    window hide
                    stop music fadeout 5
                    play sound sfx_intro_bus_engine_start
                    $ renpy.pause(2)
                    play sound_loop sfx_intro_bus_engine_loop fadein 3
                    scene anim intro_9
                    with fade2
                    $ renpy.pause(1, hard=True)
                    scene anim intro_10
                    with fade
                    play sound sfx_intro_bus_door_open
                    $ renpy.pause(2, hard=True)
                    scene anim intro_11
                    with fade
                    $ renpy.pause(1, hard=True)
                    stop sound_loop fadeout 4
                    pause 2
                    scene bg int_bus_winter with dissolve
                    window show

                    "Я сел у окна."

                    $ limb_set_volume("sound", 0.4, 1)
                    play sound sfx_bus_out fadeout 1
                    scene bg int_bus_winter at limb_shake
                    with dissolve
                    play ambience sfx_bus_interior_moving
                    $ limb_set_volume("music", 1.3, 0)
                    play music music_list["everlasting_summer"] fadein 8

                    "На улице зима, бедлам, зайцы, детали самолетов падают с неба, а мне тепло и по-домашнему комфортно."
                    "Какая-то тихая мелодия убаюкивает."
                    "Засыпаю я."

                    show blink

                    "Впрочем, чего опасаться-то?"
                    "Почему-то мне кажется, что теперь, когда я проснусь, всё будет хорошо[pl_ell]"

                    $ show_pl_achiv("all_be_good")
                    $ limb_mute(6)
                    $ persistent.all_be_good_end = True
                    window hide
                    pause 6
                    jump limb_menu

                "Позвонить маме":

                    play music pl_dn_bad_future_remix fadein 2 fadeout 2
                    scene bg semen_room_dorian with Dissolve(5)

                    "Я осторожно взял телефон и непослушными пальцами выбрал контакт. Интересно, как к ней обращаться? Мама[pl_ell] или по имени-отчеству? Почему-то второй вариант выглядит уместнее."
                    "Начал было считать гудки, но моё внимание привлек какой-то нарастающий шум."

                    show pl_hare_2:
                        anchor (0.5, 0.5)
                        pos (0.28, 0.5)
                        zoom 1
                        alpha 0.3
                    with Dissolve(3)

                    "Внезапно мне показалось, что в комнате кто-то есть. В костюме[pl_ell] кролика?"

                    show pl_hare_2:
                        anchor (0.5, 0.5)
                        pos (0.28, 0.5)
                        zoom 1
                        alpha 0.3
                        ease 5 pos (0.5, 0.7) zoom 1.5 alpha 1

                    "Я присмотрелся[pl_ell]"

                    stop music fadeout 2
                    pause 2
                    play sound sfx_limb_screamer_6
                    show cg limb_scream_3
                    with vpunch
                    pause 3
                    scene bg black with vpunch

                    "Я[pl_ell]"
                    "Испугался. И я опять возвращаюсь?"
                    "Сколько можно, а? Эй, вы, там, снаружи, сверху, чёрт знает где ещё - вам самим не надоело?"

                    $ limb_lap2 = True
                    jump limb_life_chef

label limb_life_writer:

    $ limb_conversion(2, "int_kitchen_pl", 1, "Детство", None, None, renpy.random.randint(1,16))

    play ambience ambience_int_cabin_evening fadein 3

    "Мне 6 лет. Почему-то у меня очень хорошее настроение. Не знаю почему. Может ли быть такое, что 6 лет уже не в первый раз? Папа и мама смеются."

    scene bg int_open_door with dissolve

    "Мне становится скучно, я выбегаю из кухни и застываю в корридоре. Куда бежать? Я знаю, что в гараже, и в моей комнате[pl_ell] и в библиотеке тоже, но оттуда я начинал, по-моему, реже всего."

    scene bg int_library_bright with dissolve

    "Я крадусь мимо стелажей, прикрыв растопыренными пальцами глаза и считая вслух. Наугад вытягиваю книгу и, разумеется, понимаю, что знаю её наизусть."

    show pl_multi_4 at limb_multi_2

    "И тут меня осеняет - я столько раз был здесь, но никогда ещё не пробовал писать сам. Как я мог это упустить?! "
    "Возможно, я мог бы стать неплохим писателем?"

    $ limb_conversion(2, "semen_room_clean", 3, "Начало", "day", "writer", None)

    play music pl_ef_track_1 fadein 3

    "Доброго вам времени суток, друзья. Вчера мне исполнилось целых 19 лет, и, надо признаться, это число звучит грозно. Хотя писатели как перебродивший виноград - с годами становятся только лучше!"
    "Писать здорово, я очень люблю это, но в то же время это и непростой труд. Да и ответственность тоже. Перед читателями, перед персонажами. Перед собой."
    "Впрочем, какой из меня писатель? Так, веду маленький бложик. Спасибо, ребята, что вы меня читаете."

    show blinking
    pause 2

    "Сейчас я хочу поговорить о наболевшем."

    scene bg semen_room_window with dissolve2

    "С недавних пор я начал видеть странные сны. Видения, если хотите. Лица людей, которых я никогда не знал; имена, которые мне ни о чем не говорят, но знакомы."
    "Кто такие {font=[limb_font_1]}{color=#FFAA00}Алиса{/color}{/font} и {font=[limb_font_1]}{color=#4EFF00}Юля{/color}{/font}{w=0.8}, {font=[limb_font_1]}{color=#FFFF00}Сергей{/color}{/font}{w=0.8}, {font=[limb_font_1]}{color=#FF3200}Ульяна{/color}{/font}{w=0.8}, {font=[limb_font_1]}{color=#00DEFF}Маша{/color}{/font}?{w=1} А {font=[limb_font_1]}{color=#B956FF}Лена{/color}{/font}?{w=1} Недавно услышал краем уха, что молодая чета ученых, {font=[limb_font_1]}{color=#FFD200}Славяна{/color}{/font} и {font=[limb_font_1]}{color=#FFF226}Александр{/color}{/font} Сычёвы, пропали без вести. Я не знаком с ними, совершенно точно.{w} Или знаком?"
    "Это длится около года. Плюс-минус. Наконец, сегодня утром я не выдержал."

    pause 2
    scene bg semen_room_clean with dissolve

    "Извините, дорогие читатели, обычно я мучаю вас гораздо более путанным и пространным предисловием, но в этот раз мысли рвутся наружу, слишком многое нужно описать[pl_ell]"

    stop music fadeout 5
    $ persistent.sprite_time = 'night'
    show pl_sl_un_glitch with dissolve

    "Моя жена (поженились всего неделю назад, кстати) улыбается мне, принеся новую кружку кофе. Она хорошо меня знает и молча уходит, тихонько закрывая за собой дверь. Это приятно - то, что мне так повезло с жёнушкой! Не всем так везёт."

    hide pl_sl_un_glitch with dissolve
    play sound sfx_close_cabinet
    pause 1
    play sound_loop pl_ae_trevoga fadein 3

    "И я вывожу - всегда сначала пишу на бумаге, это придает реальности происходящему - первые слова:"
    "\"Мне 6 лет, и я люблю мотоциклы. Я выпрашиваю у родителей журналы про спорт или одежду, которые они постоянно читают, и нетерпеливо листаю тяжелые глянцевые страницы, чуть ли не надрывая их, пока не нахожу их фотографии, которые с упоением[pl_ell]\""

    $ show_pl_achiv("origin")
    $ limb_mute(3)
    $ persistent.origin_end = True
    $ limb_menu_jump()

label limb_life_workshop_new:

    play ambience ambience_int_cabin_day fadein 3
    scene bg int_editorial_day with dissolve

    "[pl_ell]в мамину мастерскую. Наверное, у нас большой дом, раз у мамы есть своя мастерская! "
    "Как всегда, мама на кухне, я чувствую себя одиноко и хочу её позвать, но тут замечаю у окна мольберт с пустым холстом. "

    show cg limb_picture_start with dissolve

    "Я смотрю на это будто заснеженное пространство и понимаю, что долгое время отчаянно желаю выразить свои эмоции - и не могу. "

    show pl_multi_6 at limb_multi_2

    "А вдруг холст и краски мне помогут? "

    $ limb_conversion(4, "semen_room_morning_clean", 2, "Внезапно", "night", "artist", None)

    play ambience ambience_int_cabin_night fadein 3

    "Мне 19, и только что на меня наорали два человека. Полноте, а люди ли они? Это же кровопийцы. "

    $ persistent.sprite_time = 'day'
    show cs normal at cleft
    show pl_el_man at cright
    show prologue_dream
    with dissolve2
    play music pl_ae_obscurity_slow fadein 5

    "Сначала - хозяйка художественной галереи (Виола), а потом - мой менеджер (Серый)."
    "Это неприятно. Ууу, как бесит! "

    hide cs
    hide pl_el_man
    hide prologue_dream
    with dissolve

    "Я достаточно неплохим художником получился у мамы с папой, жаль, что они этого не застали. Многие картины высоко оценены и успешно продаются[pl_ell] продавались. "
    "Но последние полгода у меня творческая дисфункция. Казалось бы, рановато - до кризиса среднего возраста ещё минимум лет 10. "
    "Я раздраженно бросаюсь к двери - нет сил сидеть в душной пыльной квартире, в четырех опостылевших стенах. Или мне просто лень убираться? "

    play ambience ambience_camp_center_day fadein 3
    scene bg int_entrance_2_pl
    with dissolve

    "Спускаясь по лестнице, говорю себе: "
    th "Сейчас купишь себе сигарет, купишь нормальной еды, успокоишься, глядишь, Музу встретишь - и жизнь наладится, жизнь[pl_ell] "

    scene bg bus_stop_summer_pl
    with dissolve
    pause 0.5
    stop ambience
    stop music
    play sound sfx_bus_honk
    show black with vpunch
    play second_sound sfx_lena_hits_alisa

    "Я не успеваю купить сигареты. "
    "Кажется, меня сбил автобус. "
    "Я возвращаюсь. "

    show blink
    play ambience ambience_camp_center_day fadein 3

    "Я[pl_ell] "

    hide black
    hide blink
    show unblink

    "Открыв глаза, я сидел и тупо смотрел перед собой. "
    "Во-первых, мне только что привиделся отличный сюжет для картины! "

    $ limb_set_volume('music', 2, 3)
    play music pl_gk_lonely_man fadein 3

    "А во-вторых, я, кажется, жив[pl_ell] А жаль. Снова придётся терпеть насилие над мозгами от Серёжи. Ай, ладно[pl_ell]"
    "Я кое-как поднялся и недоумённо осмотрелся. Вон автобус. Он меня сбил. Плохой автобус, не буду на нём больше ездить. "
    "А вот - люди. Толпа зевак сохраняла почтительную дистанцию. "
    "Я издевательски раскланялся, плюнул в сторону дымившегося автобуса и пошёл к ларьку - сигареты-то сами не появятся! "

    scene bg bus_stop_summer_pl:
        align (0.5, 0.5)
        ease 2 align (0.4, 0.5) zoom 1.2
    show mt surprise dress:
        anchor (0.5, 0.5)
        pos (1.5, 0.5)
        ease 2 pos (0.4, 0.5)

    "Тут какая-то женщина в платье, здорово похожая на мою маму, преградила мне путь:"
    plgod "Вы в порядке?{w=0.8} Ума не приложу, как Вы уцелели!"
    "Бодро и вместе с тем участливо сообщили мне две здоровенные говорящие дыньки. "

    scene bg bus_stop_summer_pl:
        align (0.4, 0.5) zoom 1.2
        ease 1 align (0.6, 0.5) zoom 1.2
    show mt surprise dress:
        anchor (0.5, 0.5)
        pos (0.4, 0.5)
        ease 1 pos (0.25, 0.5)

    "Отгоняя внезапное чувство голода, я неопределённо мотнул головой и снова попытался атаковать заветный ларёк. "

    show mt smile dress:
        anchor (0.5, 0.5)
        pos (0.25, 0.5)
        ease 1 pos (0.5, 0.5)
    with dspr

    "Но не тут-то было! Бойкая молодая - и симпатичная - бабёнка не давала мне проходу, звонко заливая про пользу отдыха то ли в каком-то санатории, то ли лагере."
    "Эта манера показалась мне знакомой. Я присмотрелся[pl_ell] "
    plme "Ба, да я ж Вас знаю! "

    show mt surprise dress with dspr

    "Заорал я на всю улицу. "
    "Как и ожидалось, толпа зевак, только-только потерявшая ко мне интерес, снова устремилась к полоумному, громящему сегодня город."
    "Бабёнка удивлённо заткнулась, хлопая большими изумрудными глазами. "
    "\"Нарисовать бы её\", - пронеслась в голове мысль. Как, наверное, и полагается художнику, когда я вижу что-то красивое, я хочу это[pl_ell] э-э-э, нарисовать, да."
    plme "Вы же ведущая того кулинарного шоу! "
    plgod "Какого шоу?"
    "Ещё сильнее расширив глаза, переспросила моя новая муза. Ей-богу, ещё немного, и у нас будет уже 4 дыни."
    plme "Там что-то про мешки с сахаром,"
    "Уверенно заявил я, на самом деле совершенно ни в чём не уверенный."

    show mt surprise dress:
        anchor (0.5, 0.5)
        pos (0.5, 0.5)
        ease 2.5 pos (1.5, 0.5)

    "Вот зачем, спрашивается, я её спугнул[pl_ell] Завёл бы к себе в комнату, под предлогом помощи больному раздел бы и это[pl_ell] нарисовал бы[pl_ell] всю."
    "Тем временем муза окончательно смешалась, всплеснула руками и ретировалась, разблокировав мне, наконец, доступ к сигам."
    "Заинтересованная толпа поползла следом. "
    "Проводив их взглядом, я хорошенько поржал, купил себе трубки-дымилки (про всё остальное, естественно, забыв) и без приключений добрался домой. "

    play ambience ambience_int_cabin_day
    scene bg semen_room with dissolve

    "[pl_ell]"
    "Высунув косматую башку в окно, я неспеша дымил, одну за другой. "
    "В комнате царил раздрай - быстро набросав эскиз карандашом, я приготовил краски и палитру. "
    "Ну а как краски оказались на столе, на полу, на руках у меня и даже на лице - история предпочтёт умолчать."
    "Я задумчиво швырнул очередную сигу в окно, она отскочила от рамы и, вращаясь, покинула моё общество. К товаркам летит."
    "Столько всего предстоит изобразить[pl_ell]"

    window hide
    show cg limb_picture_start_hue with dissolve
    window show

    "Закрыв дверь в небеса, я включил лампу, вытащил холст и уселся перед ним. И долго смотрел в никуда, формируя перед глазами образ девушки. "
    "Наконец, кивнул сам себе, ткнул кистью в палитру, занёс над полотном[pl_ell] "

    stop ambience fadeout 3
    $ limb_set_volume('music', 1, 3)
    stop music fadeout 3

    plme "Что за запах? "

    show pl_smoke_1:
        anchor (0.5, 0.5)
        pos (-0.4, 0.5)
        ease 5 pos (0.355, 0.5)
    with dissolve2

    "Спросил я сам себя, а потом вдруг зашёлся диким кашлем. "

    play music pl_st_f21lfm fadein 3

    "Слёзы мешали нормально рассмотреть комнату[pl_ell] Нет, это не слёзы, это дым! "

    scene bg semen_room_fire
    show pl_smoke_1 at cleft
    show pl_smoke_3 at fright
    with dissolve2

    plme "Мы что, горим? "
    "Просипел я, с нарастающим ужасом оглядывая свою пещеру."

    window hide
    $ sunset_time()
    show pl_smoke_1 at cleft
    show pl_smoke_2
    show pl_smoke_3 at right
    with dissolve2
    window show

    "Твою мать, я только настроился. "
    "Чуть ли не выплёвывая лёгкие - как я умудрился ничего не заметить раньше?! - наконец разглядел огонь."
    "Маленький уютный костерок из моих набросков, носков и краски[pl_ell]"
    "Я мысленно проклял момент, когда швырял последнюю сигарету. "
    "Так, дышать нечем, сейчас открою окно, наберу воды и потушу это недоразумение. Как же много на меня[pl_ell]"

    $ limb_set_volume('sound', 0.35, 0)
    play sound sfx_nightmare_explosion
    scene bg black
    show limb_blood_frame
    with flash
    with vpunch
    $ limb_set_volume('sound_loop', 0.3, 0)
    play sound_loop sfx_limb_heart fadein 3

    "Вспышка. "
    "Грохот. "
    "Ощущение раскалённого поцелуя от великанши."
    "Я попытался открыть глаза, но не смог. Окна нет, комнаты нет, глаз нет, меня нет[pl_ell] И великанши тоже нет. А жаль. Горячая штучка, видать."
    "И надежды[pl_ell] Надежды тоже нет."
    "Я с испорченным на весь день настроением кисло смотрел в глубину воронки. Или не смотрел[pl_ell] что тут вместо органов зрения?"

    $ limb_workshop_old == True
    jump limb_life_runner

label limb_life_workshop:

    play ambience ambience_music_club_night fadein 3
    scene bg int_editorial_day with dissolve

    "[pl_ell]в мамину мастерскую. Наверное, у нас большой дом, раз у мамы есть своя мастерская! "
    "Как всегда, мама на кухне, я чувствую себя одиноко и хочу её позвать, но тут замечаю у окна мольберт с пустым холстом. "

    show cg limb_picture_start with dissolve

    "Я смотрю на это будто заснеженное пространство и понимаю, что долгое время отчаянно желаю выразить свои эмоции - и не могу. "
    "А вдруг холст и краски мне помогут? "

    $ limb_conversion(4, "semen_room_clean", 5, "Внезапно", "secret", "artist", None)

    "Мне 19, и только что на меня наорали два человека. "

    $ persistent.sprite_time = 'day'
    show cs normal at cleft
    show pl_el_man at cright
    show prologue_dream
    with dissolve2
    play music pl_ef_track_1 fadein 3

    "Сначала - хозяйка художественной галереи (Виола), а потом - мой менеджер (Серый)."
    "Это неприятно. "

    hide cs
    hide pl_el_man
    hide prologue_dream
    with dissolve

    "Я достаточно неплохим художником получился у мамы с папой, жаль они этого не застали. Многие картины высоко оценены и успешно продаются[pl_ell] продавались. "
    "Но последние полгода у меня творческий застой. Не могу выжать ничего нового! Абсолютно! "
    "Я раздраженно бросаюсь к двери - нет сил сидеть в душной пыльной квартире, в четырех опостылевших стенах. "

    play ambience ambience_cold_wind_loop fadein 3
    scene anim intro_9
    show limb_eff_hard_snow
    with dissolve

    "Спускаясь по лестнице, говорю себе: "
    th "Сейчас купишь себе сигарет, успокоишься слегка, придумаешь новую композицию - жизнь наладится, жизнь[pl_ell] "

    play sound sfx_bus_honk
    scene bg black with vpunch
    play second_sound sfx_lena_hits_alisa
    stop ambience

    "Я не успеваю купить сигареты. "
    "Кажется, меня сбил автобус. "
    "Снежинки кружатся в воздухе, но мне нет до них дела. "
    "Я возвращаюсь. "

label limb_life_runner:

    $ limb_conversion(2, "int_kitchen_pl", 1, "Детство", None, None, renpy.random.randint(1,16))

    play ambience ambience_int_cabin_evening fadein 3

    "Мне снова 6, и мне хочется бегать! Я ношусь по дому как гоночная машинка!"

    show pl_multi_5 at limb_multi_1(0.25)

    "Я такой быстрый! Мама говорит не бегать по дому[pl_ell]"
    "Куда бы побежать теперь?"

    window hide
    pause 1
    menu:
        "На лестницу":

            scene bg int_entrance_3_pl with dissolve

            "Я бегу к себе в комнату, на второй этаж."
            "Громко топая, я взбегаю по ступенькам, перепрыгивая последнюю, и[pl_ell] Ой!{w=0.8} Зацепившись, падаю на коленку."

            with vpunch

            plme "Мама!!!"
            "Мне больно, и я плачу[pl_ell]"
            "Мама, коротко отругав меня, обрабатывает кожу, накладывает пластырь[pl_ell] Мама такая хорошая!"
            "Уже совсем не больно."
            "Я смотрю на маму. Мы с папой такие счастливые!"
            "Вот бы и у меня такая жена была, как исполнится 19[pl_ell] Наверное, я буду счастлив."

            jump limb_life_killer

        "На улицу":

            play ambience ambience_camp_center_day fadein 3
            scene bg ext_admins_sunset with dissolve
            pause 1
            scene bg ext_city_street_day with dissolve

            "Выбежав на улицу, я со всех ног лечу вниз по склону."

            show screen limb_butterfly

            "Как же классно!"
            "По-моему, я ещё никогда не становился спортсменом. Может быть, попробовать?"

            hide screen limb_butterfly
            $ limb_conversion(2, "ext_beach_sunset", 2, "To be continued[pl_ell]", "night", "sanatorium", None)
            show sl serious dress far with Dissolve(3)
            play ambience ambience_lake_shore_evening

            "Мне 19, и вот только что я получил от ворот поворот."

            play music pl_gk_depression fadein 3
            show sl serious dress:
                anchor (0.5, 0.5)
                pos (0.5, 0.5)
                ease 2.5 pos (-0.5, 0.5)

            "Я тщетно пытался найти какие-то слова, но девушка издевательски мне улыбнулась и ушла с пляжа."
            "Эх[pl_ell] Ну и фиг с ней."
            "Помнится, в детстве я воображал, что проживаю много жизней и могу выбрать что угодно."
            "И какой чёрт меня дёрнул в лёгкую атлетику пойти?"
            "Стал бы хоть биатлонистом или в теннис пошёл бы[pl_ell]"
            "Нет, я у мамы бегун!"

            play sound sfx_limb_stone

            "Я подобрал голыш и в сердцах швырнул его в озеро."
            "В общем, я работал, старался, тренировался, бегал и бегал[pl_ell]"
            "Даже чего-то добился. Не первое место, конечно, но в тройке лидеров по стране я всё-таки оказался."
            "А потом бац - и растяжение."
            "Полгода бега не будет."
            "Полгода я ничего не смогу делать."
            "Забавно[pl_ell] Всего 19 лет - а жизнь уже прожита. Ничего я уже не добьюсь."
            "Так мне, собственно, тренер и сказал."
            "И вот он я - направлен в санаторий, отлежавшись в больничке."
            "Здесь озеро, какие-то девушки-недотроги и недорогое бухло."
            "В ближайшем ларьке я приобрёл литр крепкого пива, уселся на песок и просто[pl_ell] решил созерцать мир."
            "Странный какой-то санаторий, в котором можно купить пиво."
            "Я[pl_ell]"
            "Понятия не имею, что делать дальше."

            scene bg ext_beach_darken

            "Отец. Отец меня всегда поддерживал. Я бы задумался о том, чтобы где-то тут покончить с собой, но не хочу оставлять его одного. Нечестно будет[pl_ell]"
            "Я приложился к бутылке."
            "Из-за тренировок и не пил толком никогда. И с друзьями разошёлся."

            with vpunch

            plme "Ааа, да хватит себя жалеть!"

            play sound sfx_limb_stone
            pause 2
            stop sound

            "Я встал и швырнул в воду допитое пиво. Или не допитое[pl_ell]"
            "Ладно, здесь закаты красивые. Это да."
            "Я так устал[pl_ell]"

            stop music fadeout 2
            play sound sfx_hiding_in_bush

            "Тут слева от себя услышал какой-то шорох."

            scene bg ext_path_night with dissolve

            "Обернулся."
            "Хм[pl_ell] Лес как лес."
            "Я подошёл поближе. Кажется, будто меня кто-то зовёт[pl_ell]"
            "Раздался треск."

            play sound sfx_scary_sting
            show cg d4_sh_stay with vpunch
            play music pl_st_a2e13lam fadein 3

            "Навстречу вылетел какой-то парень в очках и с арматурой в руках."

            with vpunch

            plb "С дороги!!! Убегай!!!"

            play sound sfx_body_bump
            play second_sound sfx_run_forest
            hide d4_sh_stay with flash
            scene bg ext_beach_night with dissolve

            "Я отпрыгнул в сторону, и психопат убежал в неизвестном направлении."
            "Черт[pl_ell]"

            $ limb_set_volume("sound", 0.7, 0)
            play sound sfx_hell_crickets_1 fadein 3

            "Чуть сердце не выскочило."
            "Воздух наполнил громкий стрёкот."
            plme "Да что здесь за чертовщина творится?!"
            "Так, ладно, нужно обратиться к руководству, сказать, что здесь бегает маньяк какой-то."
            "Я развернулся и пошел было к дорожке[pl_ell]"

            scene ext_path2_night with dissolve

            "Которой не оказалось."
            "Какого чёрта?!"
            "Здесь только что были здания санатория!"
            "За спиной раздался скрипучий голос."
            plv "Семён[pl_ell]"
            "Оцепенев, я смотрел прямо перед собой."
            plv "Ну же[pl_ell] Я знаю, что ты слышишь. Тебе от нас не сбежать."
            "Я повернул голову."

            $ limb_set_volume("sound", 1, 0)
            play sound sfx_scary_sting
            scene cg epilogue_mi_3 with flash

            plme "Мёртвая маленькая девочка? Серьёзно? А телевизор где?"
            plv "Иди к нам[pl_ell]"

            $ limb_set_volume("sound", 0.7, 0)
            play sound sfx_hell_crickets_2 fadein 2

            "Попятившись, я лихорадочно думал, кто мог устроить розыгрыш."
            "Вот беда[pl_ell] Никто."
            "Подняв фонтанчик пыли, я рванул прочь по пляжу."

            scene bg ext_sea_night_pl at limb_running

            plme "Мне же нельзя бегать, с№ка!"

            with flash_red

            "Левый голеностоп начало жечь как огнём."

            play sound sfx_hell_crickets_3 fadein 3

            "Стрёкот всё нарастает."
            "Я уже не то что не бегу, с трудом ковыляю по пляжу."
            "А за спиной всё раздаются эти идиотские голоса[pl_ell]"
            plv "Мы даруем тебе[pl_ell] Вечный покой[pl_ell]"

            scene bg ext_sea_night_pl with vpunch

            "Я остановился, в очередной раз развернулся и заорал в темноту:"

            scene bg ext_sea_night_pl with vpunch

            plme "НУ ТАК ДАВАЙ, МАТЬ ТВОЮ, ЧЕГО ЖЕ ТЫ ЖДЁШЬ?!"

            stop ambience fadeout 5
            scene bg ext_sea_night_fade

            "А темнота[pl_ell]"
            "А темнота ничего не ответила."
            "Я покрутил головой."
            "Ни пляжа,{w=0.3} ни леса,{w=0.3} ни девочек[pl_ell]"
            "Ни луны,{w=0.3} ни звёзд,{w=0.3} ни даже моего тела."

            scene cg epilogue_uv with flash

            "И тут я всё вспомнил."
            "Ага[pl_ell] Значит, не воображал[pl_ell]"
            "Ну и что дальше? Опять возвращаюсь в эти чёртовы шесть лет? В беззаботную жизнь шестилетнего ребёнка, которому давно уже не шесть?"
            "Надеюсь, там будет хоть что-то новое[pl_ell]"

            $ limb_conversion(2, "int_library_bright", 1, "Детство", None, None, renpy.random.randint(1,16))

            play ambience ambience_int_cabin_evening fadein 3

            "Мне 6 лет."
            "Без всякого интереса снова иду в библиотеку."
            "Взгляд скользит по знакомым пыльным корешкам, и тут[pl_ell]"
            "Замечаю книгу, которую раньше не видел."
            "\"Огнестрельное оружие сквозь историю\"."
            "Хм[pl_ell]"
            "Я бы не хотел становиться в будущем[pl_ell] Кем? Террористом? Да брось[pl_ell]"

            window hide
            pause 1
            menu:
                "Взять":
                    "Интересно[pl_ell]"

                    $ limb_conversion(2, "int_floor_future_2", 3, "Нейромант", "day", "psycho", None)

                    play music pl_ef_dubstep_4 fadein 3

                    "Я вышел на лестничную площадку, закрыл дверь и закурил."

                    play sound sfx_alisa_lighter

                    "После того, как ввели эти цветовые паспорта, отражающие твоё эмоциональное состояние и психологическую устойчивость, жить в Новой Москве стало вконец сложно. Хотя мне всего 19 лет."
                    "Я спустился по лестнице и разблокировал выход."
                    "Интересно, как там Электроник?"
                    "Надеюсь, не поймали. А если и поймали, то хоть на куски не порезали на опыты[pl_ell]"

                    scene bg ext_hospital_future_1 with dissolve

                    "Первый андроид всё-таки."
                    "Я попал во двор."

                    stop music fadeout 1

                    plv "Сергей Сыроежкин?"

                    play music pl_ef_dubstep_3 fadein 3
                    show pl_pi_n_pi_night:
                        anchor (0.5, 0.5)
                        pos (-0.3, 0.5)
                        ease 3 pos (0.3, 0.5)

                    "Из тени медленно выступили две фигуры."
                    pi "Сопротивление бесполе[pl_ell]"

                    with vpunch

                    plsg "Проклятье!"

                    show pl_pi_n_pi_night:
                        anchor (0.5, 0.5)
                        pos (0.3, 0.5)
                        ease 0.5 pos (-0.3, 0.5)
                    scene bg ext_hospital_future_2 at limb_running

                    "Я рванул в противоположную сторону."
                    "Сзади раздался звук заряжаемого Доминатора."

                    play sound sfx_limb_reilgan

                    "Я отпрыгнул в сторону."

                    play second_sound sfx_limb_reilgan
                    with limb_psycho_flash
                    queue second_sound sfx_limb_reilgan

                    "Слева полыхнуло голубым."

                    play sound sfx_limb_reilgan
                    queue sound sfx_limb_reilgan

                    "Чёрт, они молекулярным дезинтегратором стреляют!"
                    "Я изо всех сил бегу вперёд, понимая, что только в скорости мой шанс выжить. Сзади слышно преследователей. Нужно спрятаться! "

                    scene anim limb_psycho_city
                    with limb_psycho_flash
                    with vpunch

                    "Я выскочил на магистраль, залез на светополосу в сторону ближайшего развлекательного центра. Мир завертелся в круговороте красок. "
                    "Слава Вселенскому, впереди виднеется локальный портал! "

                    stop music fadeout 1

                    "Я прыгнул в сверкающую спираль, она закрутилась, и[pl_ell] "

                    play music pl_ef_dubstep_2 fadein 3
                    scene bg ext_city_house_future with limb_neon_flash

                    "Меня выкинуло где-то на окраинах НМ. Так, перезаряжаться она будет минут 5.{w=0.8} Тут я увидел яркую вывеску."
                    "{i}\"Ты здесь не просто так\".{/i}"

                    play sound sfx_limb_menu_2
                    scene bg int_floor_future_1 with dissolve

                    "Отлично!"

                    play sound sfx_limb_menu_2
                    scene bg int_door_night with fade

                    "Я прошёл идентификацию личности и заскочил внутрь."
                    "Заблокировал двери."
                    "В помещении царил сумрак, нарушаемый только разноцветными флюорисцентными лампами."

                    scene bg black with dissolve
                    pause 1
                    show pl_us_android:
                        anchor (0.5, 0.5)
                        pos (1.5, 0.5)
                        ease 2 pos (0.5, 0.5)

                    "Ко мне подошла маленькая девочка."
                    "Андроид."

                    stop music fadeout 3

                    pland "Приветствую вас в сервисе \"Ты здесь не просто так\"."
                    pland "Вы хотите пройти процедуру имплантации памяти?"
                    plsg "Да-да, конечно."
                    pland "Пожалуйста, следуйте за мной."

                    play music pl_uc_deep_space fadein 3

                    "Я пошёл за ней, то и дело нервно оборачиваясь."

                    scene bg int_catacombs_future
                    show pl_mi_queen at cright
                    show pl_us_android:
                        xanchor 0.5
                        xpos 0.2
                    with limb_neon_flash

                    pland "Царица, у нас новый посетитель!"
                    plts "Здравствуйте, мистер Андерс[pl_ell] Прощу прощения, мистер Перс[pl_ell] Прошу прощения, мистер Сыроежкин. "
                    plsg "[pl_ell]"
                    plsg "Привет."
                    plts "В нашей власти подарить вам любые воспоминания, какие вы только можете пожелать."
                    plts "Можете прожить любую жизнь. Кем бы вы хотели быть? Может быть, ученым или спецагентом, спасающими мир? Или успешным музыкантом, в группе с очаровательными девчонками?"
                    plts "Хотите отправиться на Марс в путешествие? Только представьте, можно стать талантливым художником или писателем! Поверьте, вы можете Вспомнить всё! "
                    plts "Вам не хватает женского общества? Тогда мы подберём вам чудесную жену[pl_ell]"
                    plts "Наконец, наше сегодняшнее специальное предложение - пионерлагерь \"Совёнок\"! Только представьте, целых 13, считая вас, действующих персонажей, и неделя приключений!"
                    "Несмотря на то, что я забежал сюда только переждать погоню, поневоле задумался. Такие перспективы[pl_ell]"

                    window hide
                    show blink
                    pause 2
                    menu:
                        "Обрести богатство и любящую жену":

                            stop music fadeout 3
                            hide blink
                            scene bg int_catacombs_future_1
                            show unblink
                            window show

                            plts "Войдите, пожалуйста, в столб света.{w=0.8} Полагаю, с вашим психологическим паспортом всё в порядке?"

                            play music pl_uc_avers_revers fadein 3
                            scene bg int_catacombs_future_1:
                                anchor (0.5, 0.5)
                                pos (0.5, 0.5)
                                zoom 1
                                ease 6 pos (0.37, 0.5) zoom 3.5

                            "Она посмотрела на экран и слегка блеснула глазами. Иначе выражать эмоции эта модель неспособна."
                            plts "Ладно, давайте выберем, кем вы станете в новой жизни, Се[pl_ell] Сергей."
                            plsg "Давайте[pl_ell]"

                            scene bg black with flash

                            "Мир вокруг погрузился во тьму, наполненную гудением окружающих устройств для ЕВИП."
                            "Я попытался расслабиться."
                            jump limb_life_killer
                        "{color=#FFFF00}+2{/color} к дружбе, {color=#FFFF00}+10{/color} к интеллекту":

                            stop music fadeout 3
                            hide blink
                            scene bg int_catacombs_future_1
                            show unblink
                            window show

                            plts "Войдите, пожалуйста, в столб света.{w=0.8} Полагаю, с вашим психологическим паспортом всё в порядке?"

                            play music pl_uc_avers_revers fadein 3
                            scene bg int_catacombs_future_1:
                                anchor (0.5, 0.5)
                                pos (0.5, 0.5)
                                zoom 1
                                ease 6 pos (0.37, 0.5) zoom 3.5

                            "Она посмотрела на экран и слегка блеснула глазами. Иначе выражать эмоции эта модель неспособна."
                            plts "Ладно, давайте выберем, кем вы станете в новой жизни, Се[pl_ell] Сергей."
                            plsg "Давайте[pl_ell]"

                            scene bg black with flash

                            "Мир вокруг погрузился во тьму, наполненную гудением окружающих устройств для ЕВИП."
                            "Я попытался расслабиться."
                            jump limb_life_garage_new
                        "Получить жизнь популярного писателя":

                            stop music fadeout 3
                            hide blink
                            scene bg int_catacombs_future_1
                            show unblink
                            window show

                            plts "Войдите, пожалуйста, в столб света.{w=0.8} Полагаю, с вашим психологическим паспортом всё в порядке?"

                            play music pl_uc_avers_revers fadein 3
                            scene bg int_catacombs_future_1:
                                anchor (0.5, 0.5)
                                pos (0.5, 0.5)
                                zoom 1
                                ease 6 pos (0.37, 0.5) zoom 3.5

                            "Она посмотрела на экран и слегка блеснула глазами. Иначе выражать эмоции эта модель неспособна."
                            plts "Ладно, давайте выберем, кем вы станете в новой жизни, Се[pl_ell] Сергей."
                            plsg "Давайте[pl_ell]"

                            scene bg black with flash

                            "Мир вокруг погрузился во тьму, наполненную гудением окружающих устройств для ЕВИП."
                            "Я попытался расслабиться."
                            jump limb_life_writer
                        "{color=#FF3200}АКЦИЯ{/color} Специальный агент на Марсе!":

                            stop music fadeout 3
                            hide blink
                            scene bg int_catacombs_future_1
                            show unblink
                            window show

                            plts "Войдите, пожалуйста, в столб света.{w=0.8} Полагаю, с вашим психологическим паспортом всё в порядке?"

                            play music pl_uc_avers_revers fadein 3
                            scene bg int_catacombs_future_1:
                                anchor (0.5, 0.5)
                                pos (0.5, 0.5)
                                zoom 1
                                ease 6 pos (0.37, 0.5) zoom 3.5

                            "Она посмотрела на экран и слегка блеснула глазами. Иначе выражать эмоции эта модель неспособна."
                            plts "Ладно, давайте выберем, кем вы станете в новой жизни, Се[pl_ell] Сергей."
                            plsg "Давайте[pl_ell]"

                            scene bg black with flash

                            "Мир вокруг погрузился во тьму, наполненную гудением окружающих устройств для ЕВИП."
                            "Я попытался расслабиться."
                            jump limb_life_mars
                        "{color=#FF3200}АКЦИЯ{/color} Любовь, сцена, рок-н-ролл!":

                            stop music fadeout 3
                            hide blink
                            scene bg int_catacombs_future_1
                            show unblink
                            window show

                            plts "Войдите, пожалуйста, в столб света.{w=0.8} Полагаю, с вашим психологическим паспортом всё в порядке?"

                            play music pl_uc_avers_revers fadein 3
                            scene bg int_catacombs_future_1:
                                anchor (0.5, 0.5)
                                pos (0.5, 0.5)
                                zoom 1
                                ease 6 pos (0.37, 0.5) zoom 3.5

                            "Она посмотрела на экран и слегка блеснула глазами. Иначе выражать эмоции эта модель неспособна."
                            plts "Ладно, давайте выберем, кем вы станете в новой жизни, Се[pl_ell] Сергей."
                            plsg "Давайте[pl_ell]"

                            scene bg black with flash

                            "Мир вокруг погрузился во тьму, наполненную гудением окружающих устройств для ЕВИП."
                            "Я попытался расслабиться."
                            jump limb_life_music
                        "{color=#FFFF00}Специальное предложение:{/color} \"Совёнок\"":
                            pass

                    stop music fadeout 3
                    hide blink
                    scene bg int_catacombs_future_1
                    show unblink
                    window show

                    "Я поморщился.{w=1} Выбрал этого \"Совёнка\",{w=0.5} выбрал, а зачем?{w} Лучше бы на Марс слетал."
                    plts "Войдите, пожалуйста, в столб света.{w=0.8} Полагаю, с вашим психологическим паспортом всё в порядке?"

                    play music pl_uc_avers_revers fadein 3
                    scene bg int_catacombs_future_1:
                        anchor (0.5, 0.5)
                        pos (0.5, 0.5)
                        zoom 1
                        ease 6 pos (0.37, 0.5) zoom 3.5

                    "Она посмотрела на экран и слегка блеснула глазами. Иначе выражать эмоции эта модель неспособна."
                    plts "Ладно, давайте выберем, кем вы станете в новой жизни, Се[pl_ell] Сергей."
                    plsg "Давайте[pl_ell]"

                    scene bg black with flash

                    "Мир вокруг погрузился во тьму, наполненную гудением окружающих устройств для ЕВИП."
                    "Я попытался расслабиться."

                    show prologue_dream with fade

                    "Снова вспомнил об Электронике. Кажется, я обещал ему помочь[pl_ell] с постройкой робота? Стоп[pl_ell] Мысли путаются[pl_ell]"
                    pland "Странно[pl_ell] Исходный Код же не может приводить к созданию новой информации? "

                    with vpunch

                    "{size=40}Что?!{/size}"

                    with vpunch

                    plsg "Выпустите меня!{w=0.8} Сейчас произойдёт что-то плохое!"
                    plts "Успокойтесь!{w=0.8} Всё будет[pl_ell]"
                    plts "Что за чёрт?!{w=0.8} У него уже изменена память!{w=0.8} И не раз!"

                    scene bg white with flash

                    "Темнота рассеялась, я сполз с кресла и открыл глаза - как раз вовремя, чтобы увидеть пронзительную белую вспышку."

                    play sound sfx_limb_steps_1

                    plts "А-а-а!"
                    "Послышался звук шагов."
                    plv "Сопротивление бесполезно."
                    pland "Кто он такой?"
                    plv "Его зовут Семён Персунов. И он[pl_ell]"

                    scene bg black
                    show limb_eff_glitch
                    with flash

                    "Весь окружающий мир вдруг покрыли помехи."

                    window hide
                    show blink
                    pause 2
                    play ambience ambience_camp_entrance_night fadein 4
                    scene bg ext_camp_entrance_night
                    $ persistent.sprite_time = 'night'
                    show sl smile pioneer far
                    hide blink
                    show unblink
                    pause 2
                    window show

                    "Я открыл глаза."

                    show sl smile pioneer far:
                        anchor (0.5, 0.5)
                        pos (0.5, 0.5)
                        zoom 1
                        pause 1
                        ease 4 zoom 1.5

                    "Из-за ворот вышла симпатичная девушка.{w=0.8} Выглядит знакомо.{w=0.8} Направилась ко мне."

                    stop music

                    sl "Привет{w=0.8}, ты, наверное, новенький?{w=0.8} Мы тебя ждём."
                    "Ага."

                    play music pl_ae_bad_future fadein 1
                    $ limb_set_volume('sound_loop', 0.5, 0)
                    play sound_loop "zhenya/sounds/heavy_breathing.ogg" fadein 2
                    scene limb_run_anim_1
                    with fade

                    "Я развернулся и дал дёру в сторону дороги."
                    "Пробежал мимо какого-то автобуса."
                    "Чёрта с два я здесь задержусь!"

                    scene limb_run_anim_2
                    with fade

                    "Не помню почему, но у меня одна мысль о попадании в этот лагерь вызывает страх."
                    "Я побежал по дороге мимо линий электропередач.{w=0.8} Странно, разве в наше время они ещё остались?"
                    "Стоп, какое такое наше время?"

                    stop sound_loop fadeout 3
                    scene bg ext_road_night_auto with fade2

                    "Я остановился."
                    "Новая Москва, операции с памятью, молекулярные дези[pl_ell] чего?"
                    "Научной фантастики начитался, что ли?"
                    "Я огляделся."
                    "Конец дороги теряется где-то в дали, однако у меня хорошее предчувствие - мне кажется, что я найду там дом."

                    show bg ext_road_night_auto at limb_running_light
                    with dissolve

                    "Я легкой трусцой двинулся дальше. Может быть, я даже найду там жену[pl_ell]"
                    "Стану учёным[pl_ell]"
                    "И когда-нибудь мы будем ехать по дороге[pl_ell]"
                    "Окутанной туманом[pl_ell]"
                    "Я счастливо улыбнулся."

                    $ show_pl_achiv("near_happiness")
                    $ limb_mute(3)
                    $ persistent.near_happiness_end = True
                    $ limb_menu_jump()

                "Не брать":

                    scene bg ext_admins_rain
                    show limb_eff_hard_rain_l
                    with limb_lap
                    play ambience ambience_int_cabin_evening fadein 3

                    "Мне, кажется, всё ещё 6 лет."
                    "Я уже несколько дней валяюсь в своей комнате, никуда не выходя."
                    "Родители очень обеспокоены. Мама много раз меряла мне температуру, вызывала врача, ругала[pl_ell] Поскорее бы вырасти и снова начать курить.{w=0.8} Бесит."
                    "Мне, конечно, очень скучно и хочется играть, но безнадежность в душе никуда не девается. Что мне делать? Что мне дальше-то делать? Кем быть?"
                    "Я так зверски устал[pl_ell]"
                    "Может быть, попросить родителей уехать отсюда? Хотя бы съездить куда-нибудь?"

                    $ limb_conversion(4, "black", 2.5, "???", None, None, None)
                    call screen limb_war_qte
                    screen limb_war_qte:
                        modal True
                        add "limb_qte_R1" xalign 0.5 yalign 0.5
                        key "r" action [Hide("limb_war_qte"), Show("limb_war_success")]
                        key "R" action [Hide("limb_war_qte"), Show("limb_war_success")]
                        key "к" action [Hide("limb_war_qte"), Show("limb_war_success")]
                        key "К" action [Hide("limb_war_qte"), Show("limb_war_success")]
                        timer 1 action [Hide("limb_war_qte"), Jump("limb_life_adventurer")]
                    screen limb_war_success:
                        add "limb_qte_R2" xalign 0.5 yalign 0.5
                        timer 1 action [Hide("limb_war_success"), Jump("limb_life_war")]

label limb_life_killer:

    hide screen limb_butterfly
    $ limb_conversion(2, "int_auto_killer_1", 3, "Треугольник", "day", "killer", None)
    scene bg int_auto_killer_1 at limb_shake
    play music music_list["drown"] fadein 5

    "У нас всё было хорошо, ведь правда!"
    "Почему?!{w=0.8} Почему это произошло?!"
    "Мне 19 лет, и[pl_ell] Сегодня я убил свою жену."

    play music pl_st_g5lam fadein 3 fadeout 2
    scene bg semen_room_red
    show pl_un_dress_1
    show prologue_dream
    with flash

    "Когда Лена вышла за меня, первое время мы жили душа в душу. Хотя мне и говорили, что я поспешил, но я не верил. Не верил! Зря, зря!.."
    "Я любил и души в ней не чаял. Она любила - и во всём поддерживала меня. "
    "За девятнадцать лет я много чем увлекался, но моей страстью были машины. Гонки.{w=0.8} А где дорогие машины - там и красивые женщины."
    "Клянусь, я ей ни с кем не изменял!"
    "Но[pl_ell]"
    "С какого-то момента моя жена начала подозревать меня. Ревновать. Закатывать истерики. Так продолжалось каждый е#@#ый день! "
    "И однажды я не выдержал. Заорал на неё в ответ и ушёл, ляпнув дверью. "
    "Конечно, через несколько часов я прибежал обратно - извиняться. Я же хороший человек, хороший муж."
    "Но[pl_ell]"

    scene bg semen_room_red
    show pl_un_dress_2
    show prologue_dream
    with flash

    "Она вышла ко мне в нашем любимом платье{w=0.8} - и с ножом.{w} С ножом!!!"

    with vpunch

    "Она пыталась убить меня!"

    with vpunch

    "У меня не было выбора!!!"

    scene bg black
    play sound sfx_limb_blood_1
    pause 3

    "Я защищался[pl_ell]"
    "Убив её, сразу же понял, в каком дерьме оказался.{w=0.8} Я схватил ключи от гаража, помчался к своей любимой Ауди и рванул из дома, от этой мегеры, от этой безумной ведьмы!"

    scene bg int_auto_killer_2 at limb_shake
    with dissolve2

    "И вот я гоню по ночному шоссе, плевать, по встречке ли, плевать, видит ли меня кто-то, я просто хочу уехать[pl_ell] фонари расплываются в глазах[pl_ell]"

    play sound sfx_scary_sting
    show cg limb_all_tigether
    show prologue_dream
    with flash

    "И тут я будто бы что-то вижу, какой-то странный мираж[pl_ell] Будто пионерский лагерь, какие-то знакомые лица[pl_ell]"

    play ambience ambience_forest_night fadein 3
    $ limb_set_volume('sound', 1.5, 0)
    play sound sfx_limb_crying
    scene bg ext_playground_night
    show un cry pioneer
    show prologue_dream
    with flash
    $ limb_set_volume('sound', 1, 3)

    "И там она!!!"
    "Я вижу её слезы, но всё это ложь! "
    "Я знаю, кто ты на самом деле!!!"

    scene bg int_auto_killer_3 at limb_shake
    with flash
    pause 2

    "На перекрёстке я резко повернул налево, и[pl_ell]"

    stop music

    "И[pl_ell] "

    play sound sfx_limb_crash fadein 1.5
    scene bg int_auto_killer_4 at limb_shake
    show pl_un_ghost
    with flash
    pause 1
    with vpunch

    "Я сбил пару на мотоцикле!?"

    #$ limb_set_volume('music', 1.2, 0)
    play music pl_st_d314lam fadein 3

    "Нет, не может быть, мне показалось, мне показалось, мне показалось! "
    "Там не было красного платья! А у парня был шлем! "
    "Чёрт, чёрт!"

    with hpunch
    play sound sfx_limb_crash fadein 2.5

    "Я трясущейся рукой попытался вытереть слёзы, машина вильнула[pl_ell]"
    "Грохот, тряска, странный звук - машина едет дальше."
    "Я остекленевшим взглядом смотрел на дорогу, которая по-прежнему неслась передо мной. Всё быстрее, всё быстрее[pl_ell]"
    "Я убил за сегодня четырех человек. "

    scene bg int_auto_killer_4 with flash

    "Внезапно мираж пропал, и я понимаю, что всё это было ловушкой."
    "Это[pl_ell]"

    scene bg int_auto_killer_5 with dissolve_fast

    "Это что, лес?!"
    "Я резко поворачиваю руль, но меня это уже не спасает. "
    "Меня уже ничто не спасёт. "
    "Ведьма достала меня[pl_ell]"

    play sound sfx_limb_crash
    scene bg black
    stop sound_loop
    stop ambience
    pause 1.5
    scene bg black with vpunch
    with flash_red

    "Удар."
    "Машина врезается в проклятое дерево, меня швыряет лицом в руль[pl_ell]"
    "ТЕМНОТА."

    play sound sfx_scary_sting
    scene anim limb_flashback
    show prologue_dream
    with flash

    "Внезапно я вижу десятки лиц, знакомых и нет, вспоминаю сотни имён и чьих-то жизней[pl_ell]"

    with vpunch

    "НЕТ!!! "

    with vpunch

    "Я НЕ ХОЧУ БОЛЬШЕ!!!"

    with vpunch

    "ПОЖАЛУЙСТА, ХВАТИТ!!!"

    with vpunch

    "Я НИКОГДА НЕ ВЕРНУСЬ!!!"
    "Нет[pl_ell]"

    $ show_pl_achiv("un_dead")
    $ limb_mute(3)
    $ persistent.un_dead_end = True
    $ limb_menu_jump()

label limb_life_adventurer:

    $ limb_conversion(4, "ext_camp_entrance_deserted", 2, "Уроборос", "night", "adventurer", None)
    play ambience ambience_camp_center_evening fadein 5

    "Мне 19 лет. И по-моему, я заблудился. "

    play music pl_uc_powerless fadein 3

    "Начиналось всё хорошо - с ребятами объездил полстраны за лето. Но потом у всех учёба началась, я остался один. Это неприятно. "
    "Где наши не пропадали? Путешественник отправился вперёд[pl_ell] "
    "Столько красот повидал - не передать! "

    scene bg ext_clubs_deserted with dissolve

    "Иногда жалею о том, что к музыке не приучен - хотелось бы написать песню под стать окружающей природе. "
    "Я упорно покорял километр за километром, пока к вечеру не набрёл на какой-то заброшенный пионерлагерь. Интересно, когда здесь в последний раз кто-то был? "

    scene bg ext_square_deserted with dissolve

    "Я уже устал, так что решил заночевать тут. "

    play ambience ambience_lake_shore_evening fadein 3 fadeout 3
    scene bg ext_boathouse_fog with limb_lap

    "Утром осмотрелся. Жжжуткий туманище[pl_ell] Красиво тут было[pl_ell] когда-то. "
    "Нашёл пристань и лодки. И озеро. А в центре озера - остров виднеется. "
    "Ай-да сгоняю! По натуре я всегда был авантюристом."

    pause 1
    show cg limb_sem_boat_sunset with dissolve

    "Я с удовольствием грёб, откинув капюшон. Над центром озера туман почти исчез. "
    "Синее небо, красиво[pl_ell] Я засмотрелся. "

    scene bg ext_sky_day_pl with dissolve

    "Чувствую, всё будет хорошо. Здесь ведь не может быть иначе, да? Отличное место!"
    "На подходе к островку лодка начала тонуть. "
    "Мне всегда казалось, я неплохо плаваю, но мокрая одежда прилипла к телу и мешала. "

    scene bg ext_island_samsebecoder with vpunch

    "Я еле-еле выбрался. "
    "Отлежавшись на берегу, я пошёл вперёд, в заросли. "

    window hide
    $ limb_set_volume('music', 0.2, 1)
    pause 1
    play sound sfx_scary_sting
    show pl_snake:
        anchor (0.5, 0.5)
        pos (0.5, 0.5)
        zoom 0
        ease 0.2 zoom 1
    with vpunch
    pause 0.5
    hide pl_snake with dissolve
    $ limb_set_volume('sound_loop', 0.25, 0)
    play sound_loop sfx_limb_heart fadein 3
    show limb_blood_frame with dspr
    window show

    "Буквально через мгновение меня укусила змея. "

    $ limb_set_volume('sound', 1, 0)
    play sound sfx_hiding_in_bush

    "Я сразу же отбросил её в сторону, выскочил к воде, промыл ранку, но чувствовал - проблема осталась. "
    "Телефон здесь не ловит[pl_ell] "
    "Лодка протекает ещё хуже. "
    "Я понял, что мне придётся плыть самому. "

    stop sound_loop fadeout 5

    "Тело начало знобить, место укуса болело всё сильнее. "
    "Я вошёл в воду - и сразу начал тонуть. "

    stop ambience
    scene bg black
    pause 1
    scene bg ext_underwater with Dissolve(4.0)

    "Погружаюсь на дно, всё ещё не веря. "
    "Надежды по-прежнему нет. "
    "Я опять возвращаюсь. "

    scene bg black with dissolve2

    "[pl_ell]"
    play ambience ambience_limb_echo
    "Подожди, стой, я же всегда умираю, когда мне 19 лет и примерно 2-3 месяца, так?! Или 6 месяцев? Или просто 19 лет? Ведь иногда это случается зимой, иногда - летом[pl_ell]"
    "19 лет и 6 лет. Может ли это что-то значить?"

    $ limb_conversion(2, "int_kitchen_pl", 1.2, "Детство", None, None, renpy.random.randint(1,16))

    play ambience ambience_int_cabin_evening fadein 3

    "Только придя в себя, я лихорадочно бегаю по дому в поисках листика бумаги и ручки, карандаша, чего-то такого. "
    "Родители обеспокоенно спрашивают меня, в чём дело, я сначала отмахиваюсь, но потом всё-таки решаю чутка спросить:"
    plme "Мама, Папа, а сколько в году месяцев? "
    plme "А 13 - это много?"
    plme "А шесть?"
    plme "А что идёт после 13?"
    plme "А 19 - это много?"
    "[pl_ell]"
    plme "Мама, а сколько будет 19 два[pl_ell] три[pl_ell] тринадцать раз? "
    plme "А если ещё шесть раз по тринадцать?"
    "Может быть, что-то изменится? Может, я хоть что-то пойму? Только бы не забыть[pl_ell]"
    "[pl_ell]"

    scene bg ext_admins_sunset with dissolve
    stop sound_loop fadeout 3
    play ambience ambience_ext_road_evening fadein 5

    "Я тайком вышел из дома и пробрался в сад. Люблю лазать по деревьям!"

    scene bg ext_gate_sunset
    show screen limb_kuroneko_1
    with dissolve

    "Уже вечереет. Я подошёл к нашим воротам. Светлячки зажигаются[pl_ell] Как огоньки на новый год! Вот бы скорее встретить его! Снова[pl_ell]"
    "Я прислушался. Будто музыка. Ветер шумит, птички поют, а ещё жучки в траве[pl_ell] Сверчки? Кузнечики? Ну уж точно не цикады. Хотя моя жизнь похожа на то аниме[pl_ell]"
    "Люблю музыку!"
    "Сегодня папа спросил, кем я хочу быть, когда вырасту. Я не смог объяснить родителям, почему смеюсь[pl_ell]"
    "И кем я хочу быть? Чего я сейчас хочу?"
    "Мне хочется плакать."
    "Кем?"

    window hide
    pause 1
    menu:
        "Музыкантом":

            jump limb_life_music

        "Не знаю":

            hide screen limb_kuroneko_1
            $ limb_conversion(2, "semen_room_sepia", 2, "Принц и кошка", "night", "cosplay", None)
            play ambience ambience_medstation_inside_night

            "Охайо, коты, мне 19, и я наслаждаюсь каждым днём своей жизни!.."

            play music pl_gk_the_pleasure fadein 3

            "[pl_ell] хотел бы я сказать. Но чё-то как-то не. Не клеится."
            "В свои великие годы - к 18 годам - я превратился в настоящего хиккана, просиживающего в четырёх стенах за наглухо задернутыми шторами. "
            "Большая часть времени уходила на аниме и визуальные новеллы, борды, посвященные аниме, и снова аниме. Анимешник я, короче. "
            "Причём с детства у меня диагносцирован СПГС. Я бывало и нумерологией увлекался, и астрологией, и только что демонов не призывал."
            "И, казалось бы, самое время самому поставить на мне крест, как это сделали родители и бывшие школьные друзья. Но[pl_ell] мне повезло. "
            "В какой-то момент я начал общаться с парой-тройкой ребят, и сам не заметил, как влился в их компанию, подхватил их стиль жизни, как венерическое, и зажёгся теми же идеями. "
            "Одно слово.{w} Косплей. "

            play ambience ambience_camp_entrance_evening fadein 3
            scene bg ext_camp_entrance_day with limb_lap

            "И началась движуха[pl_ell] "
            "Мы собирались компаниями, тусовались в самых разных точках, и я даже не успел опомниться толком, как снова начал жить полной жизнью, выбираться из дому чаще, чем раз в неделю и общаться, общаться, общаться[pl_ell]"
            "В этот раз я с моей подругой Мику (на самом деле её зовут не так, но она выбрала для себя образ известного вокалоида) участвуем в грандиозной реконструкции советского лагеря."
            "\"Совёнок\"!"
            "Чёрт знает как, но я отыскал-таки в сети одного мужика, тёзку своего, который скинул мне карту и фотки этого места. "
            "Мы приехали на легковушке, первыми. Даром что я никогда по лагерям не катался, но этот сразу мне показался знакомым. "
            "Все мы куда старше, чем могли быть пионеры в то время, но кого это волнует? "

            play ambience ambience_camp_center_day fadein 3 fadeout 3
            scene bg ext_clubs_day with dissolve
            play music pl_gk_meeting_of_good_friends fadein 3 fadeout 3

            "Движуха обросла людьми - здесь нас собралось уже человек сорок, и это всего-то за пару дней!"
            "В данный момент я сижу на крылечке какого-то старого здания. \"Клубы\" - гордо гласит треснутая табличка. "

            show pl_us_cosplay:
                anchor (0.5, 0.5)
                pos (-0.5, 0.5)
                ease 5 pos (0.7, 0.5)

            "Вокруг ходили люди, молодые парни и девушки, а у меня настолько хорошее настроение было, что я всем машу и улыбаюсь. И, что, пионер, характерно, все отвечают взаимностью! Это приятно."

            show pl_us_cosplay:
                anchor (0.5, 0.5)
                pos (0.7, 0.5)
                pause 2
                ease 2 pos (1.5, 0.5)

            "Моё внимание привлекает симпатичная девушка. Я встаю, приветственно поднимаю руку, она улыбается и уходит куда-то в направлении столовой, слегка виляя бедрами. "
            "Пока я таращусь вслед, возникает странное ощущение. Мы знакомы? Кажется, я её уже где-то видел. Но когда? Может быть, она тоже косплеит кого-то известного? Может, маскот?"

            play ambience ambience_forest_evening fadein 3 fadeout 3
            scene bg ext_path2_sunset_pl with limb_lap

            "Погруженный в мысли, я не замечаю, как ноги завели меня куда-то на окраину лагеря, в лес. "
            "Стоп, а где я?!"
            "Тут меня кто-то окликает. Я кручу головой в поисках источника голоса."

            stop music

            pllg "Семён?"
            plme "Да, кто зовёт? Ты где?"

            play music pl_gk_trevoga fadein 3 fadeout 3

            pllg "Почему ты здесь?{w=0.8} Почему всё так неправильно?"
            plme "Эй, эй, не нервничай, что случилось?"

            with vpunch

            pllg "Так не должно быть! "

            show uv guilty far:
                truecenter
                pos (-0.25, 0.5)
                ease 3.5 pos (0.1, 0.5)

            "Я наконец замечаю в кустах чью-то фигурку. Кошачьи ушки, рваное платье[pl_ell] Ну понятно, мода на неко никогда не пройдёт. "
            "Вероятно, девочка вошла в роль и завуалированно предлагает угадать, кого она изображает. Или тоже заблудилась."
            plme "Слушай, давай пойдём к ребятам, а там и попробуем угадать, кто ты, ладно?"

            show uv surprise2 far with dspr

            pllg "Нет, нет, нет, всё сломалось, всё исказилось, так не должно быть!{w=0.8} Это неправильный лагерь! "

            show uv surprise2 far:
                ease 1 pos (-0.25, 0.5)

            "Девочка внезапно бросается в лес."

            play sound sfx_run_forest

            plme "Эй, лагерь не в той стороне! "
            "Ответом мне служит лишь отдаляющийся шорох. "
            "Блин, я же один из организаторов! Нельзя, чтобы человек потерялся! "
            "Я ломанулся в кусты следом за ней. "

            scene bg ext_path_day at limb_running
            with dissolve
            play sound sfx_run_forest

            "Быстро выхожу на дорожку. "

            scene bg ext_path_day with vpunch

            "Ого, оказывается, не такое уж это и заброшенное место. "
            plme "Эй, ты где! Постой! "
            "Нет ответа. "

            scene bg ext_path_sunset with dissolve2

            "Я иду по дорожке, опасливо оглядывая мрачнеющий с каждой секундой лес, как вдруг[pl_ell]"

            scene bg black
            show ext_path_sunset:
                anchor (0.5, 0.5)
                pos (0.5, 0.5)
                ease 0.3 pos (0.5, -0.5)
            play ambience ambience_catacombs fadein 6
            play sound sfx_simon_fall_1
            $ limb_set_volume('music', 0.2, 0)
            pause 0.4
            scene bg black with vpunch

            "Мои ноги не находят опоры. "
            plme "Аааа!!!"

            with vpunch
            play sound sfx_bodyfall_1

            "Бах."

            window hide
            show limb_blood_frame with dissolve2
            $ sunset_time()
            window show

            "Я неподвижно лежу в полумраке. "

            scene bg int_catacombs_entrance_light with dissolve2

            "Какая-то[pl_ell] шахта?.."
            "Мысли слабеют с каждым мгновением. "
            plme "По[pl_ell] помогите[pl_ell] кто[pl_ell] нибудь[pl_ell]"

            show blink
            stop ambience fadeout 3

            "Глаза закрываются сами собой."

            scene bg black
            pause 2
            show cg epilogue_uv with dissolve2
            $ limb_set_volume('music', 1, 2)

            "И тут.{w=0.8} Я.{w=0.8} Опять.{w=0.8} Всё.{w=0.8} Вспоминаю. "
            "Возвращаюсь?"
            "Снова? "
            "Я не хочу, пожалуйста, не надо ещё раз[pl_ell]"
            "Но ничего не меняется. Правила неизменны. Мне исполняется 19 лет и пара месяцев - и я снова мёртв. "
            "Иногда кажется, что я действительно живу только в эти короткие промежутки времени, когда начинается новая жизнь и кончается старая. "
            "Только сейчас я могу осознавать, что происходит. Ведь потом мне снова будет шесть лет и я буду невозможно, по-детстки непонимающим. А затем снова всё забуду. "
            "Я хочу жить по-другому! Пожалуйста, я хочу по-настояще[pl_ell]"

            $ limb_conversion(2, "int_kitchen_pl", 1.2, "Детство", None, None, renpy.random.randint(1,16))

            play ambience ambience_int_cabin_evening fadein 3

            "Мне снова 6 лет."
            "То, что происходит со мной, не нормально. Я такое видел в фильме каком-то[pl_ell] Эффект[pl_ell]"
            "Я возвращаюсь в прошлое, в один и тот же момент, и меняю будущее."
            "Чем закончился тот фильм?"
            "Кажется, у него не одна концовка. В театральной он покончил с собой[pl_ell]"
            "Я иду на кухню и задумчиво смотрю на кухонный нож."
            "Ладно, умереть всегда успею."
            "Мне становится весело, и я беззаботно смеюсь."
            "Я это исследую! Буду изучать мозг человека! А потом свой, и вообще стану супергероем!"

            $ limb_conversion(2, "int_aidpost_day_people", 3, "Двадцать пятый кадр", "night", "doctor", None)

            play ambience ambience_int_cabin_day
            play music pl_gk_mavimry fadein 3

            "Смущённая (да ни в одном глазу!) девушка продолжала рассыпаться в благодарностях. Я отбивался, подталкивая её к выходу."
            "Видя надпись на её футболке, с трудом удержался, чтобы не назначить ФГДС."

            scene bg int_aidpost_day with dissolve
            play sound sfx_close_door_campus_1

            "Закрыв за последним пациентом на сегодня дверь, облегчённо вздохнул."
            "Мне давно уже не 19 лет[pl_ell] а жаль."

            play sound sfx_open_cabinet_1
            show pl_mz_doc with dissolve

            "Переведя дух после дамочки, я выглянул в коридор. \"Больных нет,\" - только и успел порадоваться, как на горизонте возникла мрачная моська заведующей отделением."
            "Ясно, раньше сегодня я не уйду."

            play sound sfx_close_door_campus_1
            hide pl_mz_doc with dissolve

            "Получив втык за недостаток усердия и кипу историй болезней впридачу, я мрачно шлёпнулся за стол. Надеюсь, больше я её не увижу. Неприятная особа[pl_ell]"
            "Медсестра Виолетта, разумеется, уже свалила. А это что значит? Правильно, обойдусь без чая."
            "Опять за каким-нибудь хлопцем бегает[pl_ell]"

            play sound sfx_knock_door7_polite

            "Только я открыл увлекательное чтиво о болячках какой-то Ульяны Советовой, раздался стук в дверь."
            "Только этого не хватало[pl_ell]"
            "Нацепив дешёвую дежурную улыбку, я крикнул:"
            plme "Войдите!"

            play sound sfx_open_cabinet_1
            show pl_elena_1 with dissolve

            "В кабинет легко шагнула молодая девушка. Её лицо показалось мне смутно знакомым. Впрочем, у меня сейчас такое постоянно[pl_ell]"
            plgun "Интересные тебе сны снятся[pl_ell] Семён."
            plme "Прошу прощения, мы знакомы?"
            plgun "Да нет, не особо."
            plme "Так, понятно[pl_ell] Присаживайтесь, расскажите, что вас беспокоит, какие жалобы, кем ко мне направ[pl_ell]"

            stop music fadeout 3

            "Пациентка грубовато меня перебила."

            play music pl_ae_danger fadein 3

            plgun "Месье врач, правда ли, что именно лимбическая система мозга отвечает за формирование памяти?"
            "Спросила она, издевательски делая акцент на моей профессии."
            plme "Н-не только. Я не специалист, но да, есть исследования, указывающие на это."
            plgun "А как понять, что работа этого \"лимба\" нарушена?"
            plme "Полагаю, должен быть нарушен переход кратковременной памяти в долговременную, может наблюдаться неадекватная эмоциональная реакция[pl_ell]"
            "Не заметил, как почувствовал себя на экзамене.{w=0.8} Кто она?"
            plgun "Скажите, врач, у вас не бывает в последнее время странных воспоминаний? Может быть, люди кажутся знакомыми, хотя вы, как врач, с ними не знакомы?"
            plgun "Вы помните, как этим утром сюда попали? Не находите нелогичным то, что мир вокруг странный? Может быть, даже я кажусь знакомой?"
            plgun "А никакой лагерь не вспоминается, нет? С автобусами там, с симпатичными пионерками?"
            "Я с трудом вставил челюсть на законное место."
            plme "Кто[pl_ell] Да кто ты такая?"
            plgun "А это, Сёма[pl_ell]"

            with vpunch
            show blink

            "Внезапно я рухнул на пол. Глаза закрылись сами от чудовищной боли где-то в основании черепа."
            "Боли столь сильной, что я не мог издать ни звука, я не мог думать, я лишь страшно и страстно хотел перестать существовать, раствориться в небытие, и[pl_ell]"
            "И вдруг[pl_ell] передо мной[pl_ell]"


            "Что это?{w=0.3}.{w=0.3}."

            $ RLT_1 = "Лето"
            $ RLT_2 = "Автобус"
            $ RLT_3 = "Ульяна"
            $ RLT_4 = "Лагерь"
            $ RLT_5 = "Галстук"
            $ RLT_6 = "Мику"
            $ RLT_7 = "Клуб"
            $ RLT_8 = "Смена"
            $ RLT_9 = "Славя"
            $ RLT_10 = "Торт"
            $ RLT_11 = "Бункер"
            $ RLT_12 = "Алиса"
            $ RLT_13 = "Сахар"
            $ RLT_14 = "Совенок"
            $ RLT_15 = "Лена"

            $ renpy.block_rollback()
            window hide
            hide blink
            show anim ReLife
            with flash
            $ renpy.pause(20)
            scene bg black with flash
            window show
            $ renpy.block_rollback()

            "Видение пропало."
            "Попытался открыть глаза, но это не я был слеп - это мира вокруг не существовало. Одна лишь тьма. "
            "Нет, я что-то вижу[pl_ell]"
            "Стремительной волной накатывают воспоминания, которые никогда не были моими!"

            scene bg int_bus_winter
            show prologue_dream
            with flash

            "[pl_ell] будто я еду в автобусе зимой, и он кого-то сбивает[pl_ell]"

            scene bg ext_road_moto_3
            show prologue_dream
            with flash

            "[pl_ell] я на перекрёстке поворачиваю налево, и в машину врезается мотоцикл[pl_ell]"

            scene bg ext_square_night_city at limb_custom_pos(yz=-1)
            show prologue_dream
            with flash

            "[pl_ell] я иду по дождливому городу, сталкиваюсь с кем-то, он падает и больше не поднимается, и деньги разлетаются и падают в лужи, как листья[pl_ell]"

            scene bg semen_room_sepia
            show prologue_dream
            with flash

            "[pl_ell] будто я пересылаю через сеть какому-то Семёну фотографии старого пионерлагеря[pl_ell]"

            scene bg int_door_night
            show prologue_dream
            with flash

            "[pl_ell] я врываюсь в какое-то помещение, кричу, в руках - автомат[pl_ell]"

            scene bg int_floor_night
            show prologue_dream
            with flash

            "[pl_ell] на лестничной площадке кто-то спотыкается об мою ногу и падает[pl_ell]"

            scene bg int_table_baw
            show prologue_dream
            with flash

            "[pl_ell] я на войне, я пишу кому-то письма[pl_ell]"

            scene bg int_aidpost_lamp_limb at limb_shake
            show pl_elena_1_night
            with flash

            "Я отчаянно закричал и вывалился обратно в свой кабинет[pl_ell]"
            "Меня била дрожь."
            "Уже ночь?!{w=0.8} А эта девушка[pl_ell]"
            "Я с ужасом поднял на неё глаза и взмолился:"
            plme "Помоги мне[pl_ell]"

            show pl_elena_2_night with dissolve_fast

            plgun "А вот это, Сёма, уже совсем другая история."

            $ show_pl_achiv("other_story")
            $ limb_mute(3)
            $ persistent.other_story_end = True
            $ limb_menu_jump()

label limb_life_music:

    hide screen limb_kuroneko_1
    $ limb_conversion(2, "int_wardrobe", 3, "Flashpoint", "day", "music", None)

    "Я приложился к бутылке, сделал пару глотков и удовлетворенно выдохнул. Волнение отступило."

    play music pl_gk_vintage_labeled_amys_dark_axe fadein 3

    "Мне 19 лет, и я волнуюсь как чёрт знает кто.{w=0.8} Концерт, блин!"
    "Первое наше выступление.{w=0.8} Полноценный сингл[pl_ell]"
    "Я покрутил головой в поисках Алисы или Маши, но никого из них не засёк."
    "Двачевская, вероятно, снова заперлась в толчке и льёт слёзы[pl_ell] А Мария у нас бронебойная."
    "Наплевав на мнение окружающих, я сделал ещё один глоток из бутылки, поставил её в угол и, слегка пошатываясь, выполз из гримёрной."

    scene bg int_corridor_pl with dissolve

    "Где-то в отдалении играл кавер на Comfortably Numb[pl_ell] Pink Floyd. Я слегка взбодрился."
    "Мы готовы охеренно."
    "Нет, серьёзно, мы выучили трек просто супер. Но это волнение[pl_ell] Это тебе не в лагере летнем выступать и не на разогреве[pl_ell] Это полноценное серьёзное исполнение."
    "Ладно. Как лидеру группы, нужно найти Алису. Маша и так ясно, где - наслаждается лучами славы. Господи, и где мы такую нашли[pl_ell]"

    scene bg int_washroom_close with limb_lap

    "Доковыляв до туалета, я тяжело привалился к косяку."
    "Мимо, кидая в мою сторону косые взгляды, проплыли две нимфетки из группы поддержки."
    "Идите нахер! Я вас уже перерос."
    plme "Алиса!{w=0.8} Ты как?"

    play sound sfx_knock_door2

    "Я громко постучал в дверь и постарался быть участливым."
    dv "Иди.{w=0.5} Нахрен.{w=0.5} Козёл!"
    "Ясно[pl_ell]"
    plme "Слушай, можешь меня ненавидеть, но выход через[pl_ell] семь минут. Возьми себя в руки."

    scene bg int_washroom_open
    show pl_dv_music_3
    with dissolve_fast
    play sound sfx_limb_slap
    with hpunch

    "Через пару секунд дверь заскрипела, а ещё через две секунды я схлопотал звонкую пощёчину."
    dv "Козлина, не смей мне даже на глаза попадаться!"

    hide pl_dv_music_3
    show pl_dv_music_2:
        anchor(0.5, 0.5)
        pos (0.5, 0.5)
        ease 1 pos (-0.5, 0.5)

    "Не стоило с ней пытаться мутить[pl_ell]"
    "Я сурово потупил глаза, всеми силами стараясь не думать о том, что я не могу не попадаться ей на глаза - нам играть на одной сцене через[pl_ell] шесть минут."
    "Алиса браво утопала в ту сторону, где играла музыка."
    "Я решил, что стоит пойти туда же."

    scene bg ext_square_sunset_city
    show pl_ma_limb_1_alt_sunset:
        anchor (0.5, 0.5)
        pos (0.645, 0.52)
    with dissolve2

    "Проходя мимо толпы корреспонденции, я мимоходом выцепил Машу."

    $ limb_sprite_switch('pl_ma_limb_', '1_alt_sunset', '2_alt_sunset', dspr, limb_custom_pos(0.645, 0.52))

    ma "Я ещё не закончила!"
    plme "Нам играть через четыре минуты. Ты имеешь что-то против?"

    show pl_ma_limb_2_alt_sunset:
        anchor (0.5, 0.5)
        pos (0.645, 0.52)
        ease 0.05 pos (0.645, 0.53)
        ease 0.3 pos (0.645, 0.5)
        ease 0.1 pos (0.645, 0.52)

    ma "Нет, зайчик!"
    "Слава богу, хоть на неё у меня не встаёт."

    show pl_ma_limb_2_alt_sunset:
        xanchor 0.5
        xpos 0.645
        ease 3 xpos - 0.3

    "Подталкивая женскую версию Нарцисса в направлении кулис, я задавался вопросом: почему мне кажется, что что-то не так?"

    $ limb_flow_transition("int_wardrobe", None)

    "Я лишний раз пробежался по состоянию музыкальных инструментов."
    "Всё в норме."
    "Алиса внесла свою лепту в моё спокойствие:"

    show pl_dv_music_2 at cright:
        zoom 1.2
    with dissolve
    pause 0.2
    show pl_ma_limb_2_alt at left
    with dissolve

    dv "Успокойся, идиот. Это моя гитара и я знаю, как с ней обращаться."
    "Сердечно поблагодарив заботливую бывшую, я выскочил наружу - подышать воздухом."

    scene bg ext_square_night_city with limb_lap
    play sound sfx_close_door_campus_1

    "Похлопав по карманам, вспомнил, что сигареты закончились."
    "Ночь, скамейки, сцена[pl_ell] Всё как обычно. Вроде репетировали[pl_ell] Так чего же так беспокоюсь?"
    "Ко мне подошла какая-то девушка."

    $ persistent.sprite_time = 'night'
    show mt surprise pioneer close:
        anchor (0.5, 0.5)
        pos (1.3, 0.5)
        ease 2 pos (0.7, 0.5)

    plgod "Семён, объясни мне, что здесь происходит?"
    "Симпатичная[pl_ell]{w=0.8} Стоп, мы выходим через минуту!"
    plme "Извини, некогда, я потом с тобой поболтаю!"

    show mt:
        anchor (0.5, 0.5)
        pos (0.7, 0.5)
        ease 2 pos (1.3, 0.5)
    pause 0.5
    scene bg ext_stage_normal_night_light with dissolve

    "Девушка что-то крикнула мне в спину, но я уже ничего не слышал."

    show pl_ma_limb_1_alt
    show pl_dv_music_2 at fleft
    with dissolve

    "Мои храбрые амазонки уже стояли за кулисами."
    dv "Говорила же, что ты со своим бриолином для волос вкрай свихнулась, теперь сверкаешь как ёлка новогодняя[pl_ell]"
    ma "А мне нравится и не baise, пардони мон франсе.{w=0.8} Чего ты недовольная такая сегодня, не хватает sexe, что ли?"
    plme "Кхм-кхм[pl_ell] Ну как выступил тот парень, перед нами который?"

    $ limb_sprite_switch('pl_ma_limb_', '1_alt', '2_alt', dspr, None)

    ma "Ну, играл круто[pl_ell] но потом закричал, что пришёл из будущего и разбил гитару об усилитель."
    dv "И доктора искал."
    plme "Думаю, доктора точно найдёт."
    "Рыжая только фыркнула."
    "И[pl_ell] Наш выход!"
    "Я переглянулся с Машей и сделал первый шаг."

    stop music fadeout 2
    play ambience ambience_camp_center_day fadein 5
    $ persistent.sprite_time = 'day'
    scene bg ext_stage_normal_day with limb_monitor_flash

    "На секунду свет меня ослепил."

    play music pl_uc_powerless

    "Мы заняли свои места на сцене."
    "Странно, мне она казалась больше[pl_ell]"
    "Затем я поднял глаза от гитары[pl_ell]"
    plme "Где мы?"
    "На улице - день."
    "На деревянных скамейках сидят[pl_ell] дети?"
    "С пионерскими[pl_ell] галстуками?"
    "Это что, розыгрыш такой?"

    show pl_dv_music_1 at fleft
    show pl_ma_limb_1_alt:
        anchor (0.5, 0.5)
        pos (0.84, 0.5)
        zoom 1.2
    with dissolve

    "Я повернулся за разъяснениями к девушкам, но по одним глазам понял, что они понятия не имеют, что происходит."
    plv "Семён!"
    "О, снова та симпатяга[pl_ell]"

    show mt angry pioneer close:
        anchor (0.5, 0.5)
        pos (0.5, 0.5)
        zoom 1.2
    with dissolve

    plme "Ты не объяснишь, что тут творится?"

    show mt rage with dspr

    plgod "Семён, это неуважение к старшим!{w=0.8} Пионеры так не поступают!"
    "Пи[pl_ell] Чего?"

    show mt angry with dspr

    plgod "И вообще, что вы на себя напялили? Ты считаешь, товарищ Генда подобное бы одобрил?"

    hide pl_ma_limb_1_alt
    show mi sad pioneer far behind mt:
        anchor (0.5, 0.5)
        pos (0.84, 0.5)
        zoom 1.2
    with pixellate

    ma "Извините, Ольга Дмитриевна, такого больше не повторится."
    "Я ошалело посмотрел в сторону[pl_ell] Маши ли?"
    dv "Что?{w=0.8} Маша, ты её знаешь?"

    show mi scared with dspr

    mi "Ой, а кто такая Маша? Я её не знаю, может быть ты, Алиса, устала? Ну не нервни[pl_ell]"

    show mi smile with dspr

    "Голубые волосы?{w=0.8} Пионерская форма?"
    "Я в отчаянии кинул взгляд в сторону Алисы. Она, кажется, тоже дара речи лишилась."

    hide pl_dv_music_1
    show dv surprise pioneer far behind mt:
        anchor (0.5, 0.5)
        pos (0.16, 0.5)
        zoom 1.2
    with pixellate
    pause 1
    show mt smile with dspr

    mt "Вот теперь - другое дело! Выглядите как настоящие пионеры!"

    show dv laugh with dspr

    dv "Да, Ольга Дмитриевна.{w=0.8} Можем уже начинать?"
    "Нет[pl_ell]"
    "Алиса тоже в форме[pl_ell]"
    "Нет[pl_ell]"

    show dv laugh:
        anchor (0.5, 0.5)
        pos (0.16, 0.5)
        zoom 1.2
        ease 1.5 zoom 1 xpos 0.2
    show mt smile:
        anchor (0.5, 0.5)
        pos (0.5, 0.5)
        zoom 1.2
        ease 1.5 zoom 1
    show mi smile:
        anchor (0.5, 0.5)
        pos (0.84, 0.5)
        zoom 1.2
        ease 1.5 zoom 1 xpos 0.8

    "Я попятился назад, чуть не упав со сцены."

    with vpunch

    "Нет!"
    plme "Да что это?!"
    mi "Сёмочка, с тобой всё в порядке? Может быть, ты перенервничал?"

    $ limb_set_volume('music', 0.2, 0.5)
    stop ambience
    play sound sfx_limb_horror
    scene bg ext_stage_normal_invers
    show pl_dv_invers:
        anchor (0.5, 0.5)
        pos (0.2, 0.5)
    show pl_mi_invers:
        anchor (0.5, 0.5)
        pos (0.8, 0.5)
    show pl_mt_invers:
        anchor (0.5, 0.5)
        pos (0.5, 0.5)
    with limb_itai_flash

    plsem "Может быть. Ну что, начнём играть?"

    scene bg ext_stage_normal_day
    show dv laugh pioneer far:
        anchor (0.5, 0.5)
        pos (0.2, 0.5)
    show mi smile pioneer far:
        anchor (0.5, 0.5)
        pos (0.8, 0.5)
    show mt smile pioneer close:
        anchor (0.5, 0.5)
        pos (0.5, 0.5)
    with dspr
    with vpunch
    $ limb_set_volume('music', 1, 0.5)

    "НЕЕЕТ!"

    with vpunch

    plme "ЭТО НЕ МОЯ ЖИЗНЬ!{w=0.8} Я НЕ ПОЗВОЛЮ!"

    with limb_itai_flash

    plsem "А чья же тогда? С чего ты решил, что можешь что-то решать?"

    with vpunch

    plme "Ты - не я!{w=0.8} Перестань мной притворяться!!!"

    with limb_itai_flash

    plsem "Ты думаешь, спрятаться в твоём маленьком, искусственном, лживом, ущербном мирке лучше, чем принять реальность?"

    with vpunch

    plme "ДА!"
    plme "Даже так лучше, чем одна проклятая неделя в этом проклятом лагере! Ненавижу!"

    with limb_itai_flash

    plsem "Ты всё равно вернёшься."

    with vpunch

    plme "Назад!{w=0.5} НАЗАД!"

    scene bg black with limb_pixel_2
    pause 2
    $ show_pl_achiv("eternal_shining")
    $ persistent.eternal_shining_end = True
    $ limb_lap2 = True
    jump limb_life_biker

label limb_life_war:

    $ save_name = ("Лимб. \nБесконечная война")
    $ limb_root_name('sunset', 'war')
    scene bg ext_fireplace_war at limb_shake with Dissolve(5)
    $ limb_set_volume('sound_loop', 0.2, 0)
    play sound_loop sfx_limb_campfire fadein 3
    play ambience ambience_forest_night fadein 3
    play music pl_st_c13lam fadein 5

    "Я вытянул ноги к костру, протянул к нему руки, но все равно было холодно. "
    "Но это, может быть, и к лучшему - холод не даёт засыпать, а засыпать мне нельзя. "
    "Война[pl_ell] А я простой солдат, чья очередь стоять на часах."
    "Хорошо хоть есть костёр."
    "Я прислушался к лесу. Птицы поют, будто на фронте никто не погибает. Хотя что им[pl_ell] Лети куда-то, где нет смертей, нет нацистов, нет репрессий, нет гнусных предательств, лети и пой свою песню[pl_ell]"
    "Взводу вчера письма доставили. Много кто ждал, многие их получили. Я стоял одним из первых в очереди, но письма не нашлось. "
    "Эх, Славя, Славяна, душа моя, где же ты? Почему солдатику привет не передаёшь сердечный? "
    "Хотя, зная мою невесту, она трудится на заводе за троих."

    $ limb_set_volume('sound_loop', 0, 2)
    pause 2
    scene cg d6_sl_forest_sepia
    with flash

    "Я унёсся мыслями в пионерлагерь, в котором был всего несколько лет назад[pl_ell] А кажется, что бесконечно давно."
    "Проведя там всего 7 волшебных дней[pl_ell] я познакомился со светловолосой девушкой, которая показалась мне ангелом; там я начал писать ей стихи, которые вскоре были опубликованы в журнале; и там же мы поклялись друг другу в верности[pl_ell]"
    "[pl_ell] "
    "\"Я сам поехал куда-то{w}, Я сам с ней выбрал идти.{w} \nМиновав врата Рая и Ада{w}, я летние выбрал свои.\""

    $ limb_set_volume('sound_loop', 0.2, 2)
    scene bg ext_fireplace_war at limb_shake
    with flash

    "А через два года - война. Через два безмерно счастливых года[pl_ell]"
    "Я готов защищать Родину, готов умереть. Только бы у неё всё было хорошо."
    "И не один я такой идеалист[pl_ell] Хотя какой идеалист? Нормальный человек с нормальным сердцем. Солдат. Жених. Влюбленный[pl_ell]"
    "Нас много таких."
    "И вот пришло вчера вместе с остальными письмо одному такому как мы. От жены. "
    "А бедняга погиб всего пару дней назад. На мине подорвался."
    "Ну и мы с разрешения командира вскрыли письмо. Почтить честь хотели[pl_ell]"
    "А там[pl_ell]"
    "А там жена солдата на развод подала. К другому ушла. "
    "Написала, помимо всего прочего, что \"ей он нужен не так, как раньше\". Про жизнь что-то писала, про \" буйство красок\", музыку какую-то[pl_ell]"
    "Читал я и понимал, что погиб солдат ни за что. "
    "Да, Родину защищал. Дом защищал, очаг родной. Но что не вечер - то письма писал! Одному человеку."
    "Читал и понимал, что увидел бы эту Алису окаяную[pl_ell] не знаю, что бы сделал."
    "Командир меня как поэта из журнала попросил стих написать. Чтоб поднять настроение взвода. Или хотя бы ответить этой женщине. "
    "И вот моя очередь караулить, я заступил, ночь проходит, утро скоро - а я ни строчки не придумал. Одно что-то тоскливо-мрачное в голову лезет, с пионерлагерем связанное."
    "Сам понимаю, что моя Славя так бы никогда не поступила. Но[pl_ell] Сердцу-то не укажешь. Сердце болит[pl_ell]"
    "[pl_ell]"
    "\"И пусть теряя года{w}, и надежду и память, и нервы,{w} \nЯ счастлив был как никогда{w}, оставаясь лагерю верным.\""

    stop sound_loop fadeout 2
    stop music fadeout 2
    stop ambience fadeout 2
    scene bg ext_path2_war at limb_shake
    with dissolve_fast
    play sound sfx_hiding_in_bush

    "Вдруг я услышал какой-то шум.{w=0.8} Рядом с нашим палаточным городком располагалось какое-то здание.{w=0.5} Заброшенное.{w=0.5} Невзгоды военного времени его потрепали будь здоров. "

    scene bg ext_path_war at limb_shake
    with dissolve

    "И там кто-то явно был."
    "Я подхватил винтовку.{w=0.8} Поднять тревогу? Но[pl_ell]"
    "Мы всё-таки в лесу.{w=0.8} Может, зверь? Да и далеко мы от линии фронта[pl_ell]"

    scene bg ext_old_building_war at limb_shake
    with dissolve

    "Я тихо поднялся с ящика, на котором сидел, и скользнул к зданию. "
    "Осторожно заглянул в дверной проём, покрепче сжав оружие. Твёрдый приклад упёрся мне в плечо, придавая уверенности."

    $ limb_set_volume('ambience', 0.3, 3)
    scene bg int_old_building_war at limb_shake
    with dissolve_fast
    pause 1

    "Ничего и никого. "
    "Под неверным светом луны я вошёл. Части скелета старого дома негромко хрустят под ногами. "
    "Я истово прислушивался, но ничего[pl_ell] Почудилось?"

    play music pl_st_a213lam fadein 10

    "Водя стволом из стороны в сторону, я обошёл пару комнат.{w=0.8} Ничего. "
    "Второй этаж[pl_ell] "
    "Аккуратно обходя дыры в дощатом полу, я побывал ещё в двух комнатах. "
    "Осталась одна."

    scene bg int_mirror_war_pi at limb_shake
    with dissolve2

    "В темноте было видно лишь грязное окно и контуры вытянутого блестящего продолговатого предмета у стены. "
    "Зеркало[pl_ell]"
    "Переборов волнение, я проверил всю комнату, но ничего[pl_ell]"
    "Стоя в центре комнаты, я кинул взгляд на своё отражение. "
    "Странно[pl_ell]"
    pi "Вьетнамские флэшбеки - это, конечно, сильно,"
    "- с издёвкой сказало мне моё отражение."
    "Я молча смотрел на себя в пионерской форме. "
    pi "Семён, выбирался бы ты отсюда, всем уже надоел. "
    plme "Что[pl_ell]"

    stop music
    scene bg black with flash
    show blink
    scene bg ext_fireplace_war at limb_shake
    $ limb_set_volume('ambience', 1, 3)
    play sound_loop sfx_limb_campfire fadein 3
    hide blink
    show unblink

    "Я открыл глаза. "
    "Не может быть, задремал?! "

    play music pl_gk_trevoga fadein 3

    "Я завертел головой, вскочил с[pl_ell] ящика[pl_ell]"
    "Старый дом по-прежнему стоит в отдалении. "
    "На дворе по-прежнему ночь."
    "Я не знал, что и думать."

    play sound sfx_hiding_in_bush

    "От необходимости искать объяснение этому сну меня избавил громкий треск кустов справа. "

    stop sound_loop fadeout 5
    scene bg ext_path2_war at limb_running
    with vpunch

    "Там точно кто-то есть!{w=0.8} В военной чёрной форме!"
    "Я рванул к буеракам, одновременно заорав: Тревога!!!"
    "Через кусты[pl_ell]"
    "Там же минное поле! "

    pause 1
    scene bg ext_where_is_detonator_2 at limb_shake
    with vpunch

    plme "Стой!"
    "- неожиданно сам для себя заорал я."
    "Луна, будто понимая важность момента, чётко освещала ствол винтовки, вдоль которой я целился. "
    "Изрытое смертоносное поле. "
    "И фигуру человека на его середине. "
    "Человек в тёмной форме медленно повернулся. "
    "На плече у него была красная повязка. Красная армия? Нацист? "
    "Лицо его оставалось в тени."
    plme "Отзовись!"
    "- крикнул я. "
    "Человек молчал. "
    "Затем он сделал какое-то движение рукой, и я[pl_ell]"

    show screen limb_fire_qte
    screen limb_fire_qte:
        modal True
        add "limb_qte_F1" xalign 0.5 yalign 0.5
        key "f" action [Hide("limb_fire_qte"), Show("limb_fire_success"), SetVariable("limb_fire_qte_act", True)]
        key "F" action [Hide("limb_fire_qte"), Show("limb_fire_success"), SetVariable("limb_fire_qte_act", True)]
        key "а" action [Hide("limb_fire_qte"), Show("limb_fire_success"), SetVariable("limb_fire_qte_act", True)]
        key "А" action [Hide("limb_fire_qte"), Show("limb_fire_success"), SetVariable("limb_fire_qte_act", True)]
        timer 1 action [SetVariable("limb_fire_qte_act", False), Hide("limb_fire_qte"), Jump("limb_life_mina")]
    screen limb_fire_success:
        add "limb_qte_F2" xalign 0.5 yalign 0.5
        timer 1 action [Hide("limb_fire_success"), Jump("limb_life_mina")]

label limb_life_mina:

    $ renpy.block_rollback()
    scene bg ext_where_is_detonator_2 at limb_shake
    if limb_fire_qte_act == True:
        play sound sfx_limb_1_strike
        scene bg ext_where_is_detonator_1 at limb_shake
        with vpunch
        "[pl_ell]сразу же выстрелил."
        play sound sfx_body_bump
    else:
        pause 1
        play sound sfx_limb_1_strike
        scene bg ext_where_is_detonator_1 at limb_shake
        with vpunch
        "[pl_ell]замешкавшись, выстрелил."
        play sound sfx_body_bump
    "Голова человека дёрнулась. "
    "Он упал назад."

    with vpunch

    "Я отскочил назад, но взрыва не последовало. "
    "Слава Богу, что мины[pl_ell]"

    $ limb_mute(0)
    $ limb_set_volume('sound', 0.3, 0)
    play sound sfx_nightmare_explosion
    scene bg black at limb_shake
    with vpunch

    if limb_fire_qte_act == True:
        window hide
        pause 4
        $ limb_set_volume('music', 0.5, 0)
        play music music_list["meet_me_there"] fadein 5
        show cg limb_doki with limb_text_diss
        $ renpy.pause(hard=False)

    pause 2
    jump limb_life_adventurer

label limb_life_butterfly:

    hide screen limb_butterfly
    $ limb_conversion(2, "int_hospital_day", 5, "Glitch", "secret", "coma", None)
    play ambience ambience_int_cabin_day fadein 3

    "Первое, что я увидел, открыв глаза – незнакомый потолок. "

    $ persistent.sprite_time = 'day'
    show cs normal at fright
    with dissolve

    plcs "Очнулся!{w=0.8} Сейчас я позову доктора, подожди немного."
    scene bg int_hospital_day with dissolve
    window hide
    pause 1
    play music pl_st_c13lam
    $ limb_mode_nvl()

    "Кажется, я в больнице. Самая обычная палата, которую видел каждый."
    "Ко мне подключены какие-то датчики и капельница с неизвестным препаратом. Со стороны аппарата доносятся размеренные удары. Всё понятно[pl_ell] "
    "Но что я здесь делаю-то?"
    pldoc "Приятно видеть, что ты наконец проснулся! Это невероятно! Мы позвонили твоей матери, она скоро приедет."
    pldoc "Как ты себя чувствуешь?"
    "Чувствовал я себя не очень. Тело тяжёлое и будто деревянное, не могу сказать ни слова."
    "Когда в палату вошла женщина, которая, видимо, была моей матерью, они с доктором рассказали мне, что со мной случилось."
    "В детстве я играл на улице, и меня сбила машина.{w=0.8} Я пробыл в коме 13 лет, а значит, сейчас мне должно быть 19."
    "Доктор не перестаёт повторять, что всё это благодаря моей маме и чуду."
    "Ей предлагали отключить меня от аппарата, потому что надежды, что я проснусь, у них не было."
    "Но ни доктора, ни мой отец не смогли убедить её.{w=0.8} Отец не мог смотреть на страдания моей матери и их причину – меня, а потому ушёл из семьи."
    "Всё это время мать ухаживала за мной, сама заботилась о моих суставах и мышцах, подготавливаясь ко дню, когда я очнусь."
    "Ещё некоторое время после этого дня ко мне приходили люди, знавшие меня в детстве, делились своими воспоминаниями, рассказывали о своей теперешней жизни[pl_ell]"

    pause 1
    $ limb_mode_adv()
    nvl clear
    pause 2
    scene bg semen_room_window with dissolve
    window show

    "Когда я закончил курс реабилитации, смог вернуться домой и даже найти работу – курьером в пиццерии. Пусть это и не престижное занятие, но мне оно по душе."
    "Там же я познакомился со своей девушкой, по совместительству напарницей, Юлей – доброй и открытой девушкой. Наверное, вот оно - счастье. "
    "Мне ещё многое нужно нагнать за пропущенные 13 лет, а часть воспоминаний ко мне так и не вернулась, но это уже и не важно. Я верю, что всё будет хорошо. У меня в запасе ещё так много времени[pl_ell]"

    show pl_butterfly:
        anchor (0.5, 0.5)
        pos (-0.1, 0.7)
        linear 6 pos (0.3, 0.6)
        linear 5 pos (0.7, 0.5)
        linear 6.5 pos (1.1, 0.7)
    $ show_pl_achiv("coma_effect")
    $ limb_mute(3)
    $ persistent.coma_effect_end = True
    window hide
    pause 3
    $ limb_menu_jump()

label limb_life_nekochan:

    hide screen limb_kuroneko_1
    show screen limb_kuroneko_2
    with dissolve

    "Внезапно я заметил красивого черного кота. Он распушил шерсть, греясь на солнышке."
    "Как бы его погладить?"
    "Кот резко поднял голову, сверкнул глазами - и посмотрел прямо на меня."
    "В будущем я[pl_ell] буду[pl_ell]"

    hide screen limb_kuroneko_2
    $ limb_conversion(2, "int_auto_campfire", 5, "Настоящее", "secret", "neko", None)
    play ambience ambience_lake_shore_night fadein 8

    "Мне 19. Да? Работаю системным администратором. Живу на 13-ом этаже. Люблю котов[pl_ell]"

    scene bg ext_boathouse_night with dissolve
    play music pl_uc_deep_space fadein 3

    "Я вышел из машины, остановившись недалеко от пристани. "

    play ambience ambience_forest_night fadein 2 fadeout 1
    scene bg ext_path_night with dissolve

    "Мне не надо никуда особенно спешить, но всё равно с трудом удерживаюсь от бега. "

    play ambience ambience_lake_shore_night fadein 3 fadeout 2
    scene bg ext_beach_night with dissolve

    "Вот и пляж. "
    "Вот и море[pl_ell] "
    "Я остановился, вдыхая бодрящий соленый воздух. "
    "А потом повернулся налево - там ведь горит костёр, там сидят люди[pl_ell] "
    "Там ждут меня."

    window hide
    scene bg ext_beach_campfire_pl with dissolve2
    $ persistent.sprite_time = 'sunset'
    $ limb_set_volume('sound_loop', 0.35, 0)
    play sound_loop sfx_limb_campfire fadein 3
    pause 1
    scene bg ext_beach_night_people
    pause 4
    window show

    "Я уже спокойнее подошёл к танцующему пламени. Какая большая луна[pl_ell]"
    pi "Да ты романтик. "
    uv "Привет, Семён. Шашлык будешь?"

    show bg ext_beach_campfire_pl:
        xalign 0.25 yalign 0.7 zoom 1.2
        ease 1 yalign 0.9
    show uv laugh:
        anchor (0.5, 0.5)
        pos (0.7, 0.65)
        ease 1 ypos 0.55
    show pi far:
        anchor (0.5, 0.5)
        pos (0.15, 0.65)
        ease 1 ypos 0.55

    "Я молча сел рядом, взял мясо и с удовольствием впился зубами в сочный кусок."
    plme "Спасибо. Так что мы должны обсудить, Юля?"

    show uv surprise2 with dspr

    "Кошкодевушка одновременно весело и внимательно посмотрела на меня; в причудливой игре света её глаза, казалось, сочетали в себе все цвета радуги."

    show uv smile with dspr

    "Потом она покачала головой и повернулась к - то ли знакомому мне, то ли нет - молодому человеку. "
    uv "Я здесь не помощник. Он слишком глубоко увяз в визуализации. "
    "Мужчина вздохнул."
    pi "Ладно[pl_ell] я помогу. Обеспечь мне, пожалуйста, минимальное искажение информационного потока. "

    hide uv with dissolve

    "Юля коротко кивнула, качнула хвостом и закрыла глаза. "
    "Я продолжал молча наблюдать, одновременно наслаждаясь дивной погодкой."
    "Наконец, этот человек в белой рубашке обратился ко мне:"
    pi "Семён, слушай внимательно. Тебе нужно, не много не мало, решить загадку."
    pi "Я уверен, что ты долгое время задаёшься вопросом о том, что не так в твоей жизни."
    pi "Ответ, прямо скажу, непростой. Но полноценной жизнью твой самогипноз назвать нельзя. "
    pi "Так что просто перестань верить. Подумай о том, как бы выбраться назад. Вынырнуть. "
    pi "И чаще думай о цифрах. Потом, когда выберешься, у нас ещё дела есть[pl_ell] "
    pi "Уложился?"

    show uv smile:
        anchor (0.5, 0.5)
        pos (0.7, 0.55)
    with dissolve

    uv "Вполне. "
    pi "У мастера учился.{w=1} У мастеров[pl_ell] Пакет до него дошёл?"

    show uv surprise with dspr

    uv "Не знаааю[pl_ell]"
    pi "Юль, не беси."

    show uv grin with dspr

    "Полукошка еле слышно хихикнула. "

    stop music fadeout 3
    stop sound_loop fadeout 2
    $ persistent.sprite_time = 'night'
    scene bg ext_beach_moon_pl:
        xalign 0.25 yalign 0.9 zoom 1.2
    show uv smile:
        anchor (0.5, 0.5)
        pos (0.7, 0.55)
    show pi far:
        anchor (0.5, 0.5)
        pos (0.15, 0.55)
    with dissolve2

    "Оба человека совершенно потеряли ко мне интерес, а я заметил, что на пляже стало совсем темно и холодно."

    scene bg ext_beach_moon_pl
    show uv smile:
        anchor (0.5, 0.5)
        pos (0.7, 0.65)
    show pi far:
        anchor (0.5, 0.5)
        pos (0.15, 0.65)
    with vpunch

    "Я покосился на потухший костёр и вскочил. Внезапно очень захотелось домой[pl_ell] Домой? "

    show uv normal with dspr

    uv "Подключение погасло уже[pl_ell] До завтра,{w} Сёма."

    scene bg black with dissolve2

    "Я побежал в темноту. "

    play sound sfx_limb_breath fadein 2

    "Мне не давали - или не дают? - покоя вопросы."
    "Кто же это был, почему я так хотел их увидеть и что они имели в виду? "
    "Цифры[pl_ell]"

    $ show_pl_achiv("blue_lagoon")
    $ limb_mute(3)
    $ persistent.blue_lagoon_end = True
    $ limb_menu_jump()

label limb_life_mars:

    $ limb_conversion(4, "ext_road_mars", 4, "Четвёртая стена", "sunset", "mars", None)

    play ambience sfx_gusty_wind fadein 3

    "Я открыла глаза.{w=1} Где я очутилась в этот раз?"
    "Что я помню? Меня зовут Мэри Сью, точно. Так[pl_ell] Я просто хочу рассказать историю о том, что бы было, если бы Я попала в пионерлагерь \"Совёнок\"."

    play music pl_gk_mavimry fadein 5

    "И, кажется, я на Марсе."
    "Ну да не беда, когда меня отправляли сюда, в НАСА я была лучшей. Во всех дисциплинах."
    "Жалко тут не на кого произвести впечатление."
    plar "Смотрите, я могу дышать углекислым газом!"
    "Я осмотрелась и поняла, что Марс атакует. Я попала в эпицентр пылевой бури. Читала о них. "
    "Разумеется, читала, {w=1} я вообще обо всём читала."

    scene bg ext_camp_entrance_mars_thunder with dissolve

    "Я развернулась к воротам лагеря. "
    "Выглядят покорёженными. Вдали сверкнула Особая Марсианская Молния, увидеть которую считается чудом. "

    scene cg limb_auto_mars with dissolve

    "Я пробралась через ворота. Лагерь выглядит заброшенным и опасным -  раз это Марс, скоро могут появиться зомби из Doom, хотя очевидно, что они здесь неуместны, как и тема космоса, будущего или мистики."
    "По пути мне встретилась заброшенная машина. Я прошла мимо, не обращая внимания на песок и ветер. Любопытно, почему у неё[pl_glitch]"
    plar "Господи, это просто отсылка в отсылке в отсылке! Я крута!"
    "Думаю, Бесконечное Лето и истории про него должны быть строго ограничены в своей теме, верно ведь я говорю? Творить должно быть дано далеко не каждому. И вообще, мне кажется, стоит запретить все истории, помимо расширенных версий оригинала."

    scene bg ext_dining_hall_mars with dissolve

    "Ага, вот я набрела на какое-то здание.{w=1} Надо мной пролетела поднятая ветром та самая машина, и я пожалела, что у меня нет с собой волшебной палочки. "
    plar "Зато есть методы рационального мышления!"
    "Рассудив так, я легко взломала дверь и грациозно, не теряя собственного достоинства, вошла внутрь. "

    stop ambience fadeout 2
    scene bg semen_room_mars with dissolve

    "Мда, свинарник[pl_ell] совсем как у меня дома, не правда ли?"

    play sound sfx_close_cabinet

    "Ну да ничего страшного.{w=1} Закрыв дверь, я подошла к компьютеру."

    scene bg limb_monitor_mars with dissolve

    "Отлично! Теперь можно посмотреть Войну Бесконечности в хорошем качестве!"
    "Щёлкнув выключателем лампы, я села перед монитором и приготовилась смотреть нечто чудесное."

    pause 1
    play sound sfx_click_1
    pause 0.5
    play sound sfx_click_3
    $ limb_set_volume('music', 0.5, 3)
    play music pl_ef_limb_loop fadein 5 fadeout 3
    show cg limb_mars_titre1 with limb_titer_diss

    plar "Так[pl_ell] это не то, что я хотела[pl_ell]"
    plar "Рекурсия получается какая-то."

    play sound sfx_click_2
    hide cg limb_mars_titre1
    show cg limb_mars_titre2
    with limb_titer_diss

    plar "Думаю, далеко не всем понравится этот \"прикол\"."
    plar "Вот представь, проходит \"Лимб\" кто-то в первый раз, и попадает сюда[pl_ell] этот же человек просто выключит мод и удалит его."

    play sound sfx_click_2
    hide cg limb_mars_titre2
    show cg limb_mars_titre3
    with limb_titer_diss

    plar "Возможно, прямо на этом моменте!"

    play sound sfx_click_2
    hide cg limb_mars_titre3
    show cg limb_mars_titre4
    with limb_titer_diss

    plar "Люди просто хотят почитать про то, как в очередной раз кто-то попадает в Совёнок (ну как кто-то, это в половине случаев я, Марти Стью), и снова окунуться в ванильную атмосферу."
    plar "А \"Автор\" им свои отсылки подсовывает[pl_ell] Антихайп?"

    play sound sfx_click_2
    hide cg limb_mars_titre4
    show cg limb_mars_titre5
    with limb_titer_diss

    plar "Куда ты лезешь, они же тебя сожрут!"

    play sound sfx_click_2
    hide cg limb_mars_titre5
    show cg limb_mars_titre6
    with limb_titer_diss

    $ renpy.pause(20)

    play sound sfx_click_2
    hide cg limb_mars_titre6
    show cg limb_mars_titre7
    with limb_titer_diss

    plar "Интересно[pl_ell] Вот сделали бы эти {color=#B956FF}{font=[limb_font_3]}{size=22}Endless{/size}{/font}{/color} {color=#FFAA00}{font=[limb_font_3]}{size=22}Horizons{/size}{/font}{/color} модификацию, основанную на краеугольных камнях популярных историй - драматичность, самокопание, руты девочек, повторение оригинала, немножко юмора и эротики[pl_ell]"
    plar "Вошли бы они в топ?"

    $ show_pl_achiv("fine_mars")
    $ limb_mute(3)
    $ persistent.fine_mars_end = True
    $ limb_menu_jump()

label limb_safe:

    scene bg black
    $ renpy.block_rollback()
    $ prolog_time()
    play ambience ambience_int_cabin_evening fadein 3
    pause 1
    scene cg limb_safe_sepia with limb_razlom
    $ limb_root_name('prologue', 'safe')
    scene cg limb_safe_0 with dissolve2

    "Я[pl_ell] обнаружил себя стоящим перед здоровенной стальной дверью."
    "Это же сейф! А что за сейф?.. Знаю только то, что мне кровь из носа нужно его открыть."
    "Облизнул дрожащие от волнения губы. Протянул вспотевшую ладонь к ручке сейфа[pl_ell] эм. У него нет ручки."
    "Потянул за ближайший затвор - оказалось заперто."
    "\"Неудивительно, согласись\", - пронеслось у меня в голове."
    "Попытался отбросить сомнения, опасения и мысли о том, как я, собственно, попал в эту комнату. Или о том, как я жил последние 13 лет. Или последние 13 раз по 13 лет. Или о том[pl_ell]"
    th "Да ёжик в тумане!!!"
    "Я взъерошил волосы и постарался рассуждать логически."
    "Кодовый замок, так?"
    "Так. В математике за 4 класс я шарю[pl_ell] поможет ли?.."
    "Нужно подумать. Всего три цифры, так?"
    "Так. Должно быть несложно[pl_ell] В любом случае, у меня всего 1000 попыток, можно и вручную перебрать[pl_ell]"

    stop ambience fadeout 3
    window hide
    $ limb_safe_pass = ''
    call screen limb_safe

label limb_safe_006:

    window hide
    $ renpy.block_rollback()
    $ persistent.timeofday = 'secret'
    scene anim limb_safe with dissolve2
    play ambience ambience_int_cabin_evening fadein 3
    play music music_list["no_tresspassing"] fadein 3
    pause 1
    window show

    "Сейф открылся с противным скрипом. Я внутренне собрался и приготовился к поразительному содержанию железного ящика, но[pl_ell]"
    "В нём валялся лишь маленький клочок бумаги."
    th "Так, не время разочаровываться!"
    "Возможно, это из тех улик, на которые, кинув один взгляд, я сразу всё вспомню. И схвачусь за голову, крича от душевной боли и заливаясь плачем[pl_ell]"
    "Я потряс головой, сгреб бумажку и посмотрел, что на ней написано."
    "Корявые печатные буквы гласили:"
    "\"Ты здесь не просто так!\""
    "Я поморгал, потом с глупым видом помахал бумажкой в воздухе, рассмотрел её с разных стороны, топнул на неё[pl_ell]"
    plsem "Вы что, с№ка, издеваеетесь?"
    "Никаких объяснений, что ли?"
    "Я так и не пойму, почему и как сюда попал, что происходит или кто я такой? Что это за чёртов лагерь, мать вашу?"
    "\"Сам виноват, что попал в визуальную новеллу\", - возразил мне внутренний голос."
    plsem "И чё?{w=0.8} Я хочу знать, что происходит!{w=0.8} Я же столько концовок открыл!"
    "\"Это мод на Бесконечное лето, чё ты хотел? Авторы сами не знали, почему происходит то, что с тобой происходит\", - бессовестно добивал меня внутренний голос."
    plsem "Ладно.{w=0.8} Чё дальше-то?"
    "\"Ну, ты можешь смотивироваться кучей примеров того, как парень старался построить свою жизнь, а потом умирал в 19 лет, и стать геро[pl_ell] стать хорошим человеком и жить припеваючи\"."
    plsem "Скучно.{w=0.8} Что ещё есть?"
    "\"Можешь поиграть в кучу других модов, ведь где-то пятая часть из них заслуживает внимания. Особенно учитывая наглую рекламу в другой ветке\"."
    plsem "Спасибо, Бесконечное лето у меня и так вместо вечернего порно.{w=0.8} Ещё варианты?"
    "\"Ты в курсе, как дофига отсылок к фильмам автор запихал в эту короткую историю?\""
    plsem "Нет.{w=0.8} А что, много?"
    "\"Мммм[pl_ell] было немного, но потом он начал делать отсылки ради отсылок, и его никто не остановил. Всем пофиг, понимаешь[pl_ell] Но ты их можешь поискать - почти все первоисточники годные, рекомендуются к просмотру\"."
    plsem "Братан, ты просто тратишь моё время."
    "\"Зануда.{w=0.8} Ну окей.{w=0.8} Кто тебе сказал, что сейф открывается только одним числом?\""
    plsem "Я тебя понял. Берёмся за дело, дружелюбный сосед Внутренний Голос!"
    "\"Просил же, Голос Внутренний, а не Внутренний Голос[pl_ell]\""

    window hide
    pause 2
    stop ambience
    stop music
    $ limb_safe_pass = ''
    scene bg black
    call screen limb_safe

label limb_safe_007:

    window hide
    $ renpy.block_rollback()
    $ persistent.timeofday = 'secret'
    scene bg black
    play music pl_gk_vintage_labeled_amys_dark_axe fadein 3
    pause 1
    window show

    "Я решил схитрить и пробраться в файлы игры."
    "Мне предстоит нелёгкий путь, но[pl_ell] Я справлюсь с этим."
    "Ведь я[pl_ell] Семён.{w=1} Супер-Семён! "
    "Я взял в руку свой ствол, готовый на всё. То есть ко всему."
    "И прокрался прямо в тыл противника - кодеров и кого-то ещё (кого точно, я так и не понял)."
    "Так-так-так, что тут у нас?"

    play sound sfx_click_3
    scene bg ext_city_stray

    "Я внимательно изучил улику."
    "Кажется, это фон для мода Лимб."
    "Но не только! Это ещё и подсказка!"
    "Но зачем она здесь? И главное - для кого?"
    "И как открыть чёртов сейф?!"
    "Я испытал затруднение в голове."

    play sound sfx_click_2
    scene bg ext_washstand_day with pushright

    "От мыслей, которые сложно думать, меня отвлекли весёлые девичьи голоса."
    "Девочки, видимо, моются в умывальниках - фона-то бани в оригинальных файлах нет!"
    "Я решил проверить - вдруг на девочек напал какой-то извращенец?"
    "И тут[pl_ell]"

    play sound sfx_click_1
    pause 0.3
    play sound sfx_click_1
    play second_sound sfx_scary_sting
    show pl_18_plus:
        anchor (0.5, 0.5)
        pos (0.5, 0.475)
        zoom 0
        alpha 0
        ease 0.35 zoom 1 alpha 1

    "Ну почему?!"

    window hide
    pause 2
    stop ambience
    stop music
    $ limb_safe_pass = ''
    scene bg black
    call screen limb_safe

label limb_safe_013:

    window hide
    $ renpy.block_rollback()
    $ night_time()
    play music pl_ae_danger fadein 3
    scene bg ext_camp_entrance_dark_2
    show pl_elena_1_night at right
    pause 1
    window show

    "Добро пожаловать в отсылку к другому моду."
    "Мод мрачный, кровавый и весьма фантастический, к тому же в нём готово всего два дня и есть своя яндере. Если не отпугнуло, то речь про Одиночку, сыграйте как-нибудь. Миу!"
    "Но речь о другом. Во-первых[pl_ell] что такое цифра тринадцать?"
    "Это число, которое издавна ассоциируется с мистикой; это число действующих персонажей в одной известной визуальной новелле; а ещё это это 31, только наоборот!"

    $ limb_sprite_switch('pl_elena', '_1_night', '_2_night', dspr, right)

    "Странная логика, но я безумная, мне можно."
    "А 31, точнее, тридцать первое октября - это один из самых интересных дней в году. Хэллоуин!"
    "Одиночка задумывалась именно как короткий мод на часок, который должен был быть доделан до ноября 17 года. С неё, а точнее, с БЛ можно начинать отсчёт нашей команды и многих моих лично новых товарищей. Знакомая история, правда?)"
    "А во-вторых, не существуй Хэллоуина, не будь у меня друга, посоветовавшего Бесконечное Лето и Хотлайн Майями, не создай Lionhead игру Fable, не поступи художник в медицинский и не умри любимая собака у меня на глазах в детстве - пхахаха, я не серьезно - не было бы Одиночки, а потому - и Лимба."
    "Вот так, получается, твоё любопытство - или твоя скука - сквозь время, пространство и мастерскую Steam связано с несколькими людьми, компьютерными играми и мёртвой собакой."
    "Всего тебе доброго)"

    $ limb_sprite_switch('pl_elena', '_2_night', '_1_night', dspr, right)
    show pl_elena_1_night:
        anchor (0.5, 0.5)
        pos (0.72, 0.5)
        ease 1.5 pos (-0.2, 0.5)
        pause 1
        parallel:
            ease 1.5 pos (0.05, 0.5)
        parallel:
            ease 1.5 rotate 30
    pause 2
    "[pl_ell]"
    "Ах да, сейчас не июль, случайно? Сейф открывается по-разному в зависимости от месяца и времени на компьютере. Скажем, в июле он откроется[pl_ell] Ты не знал?"
    "Шутка.{w=1} Увидимся!"

    window hide
    show pl_elena_1_night:
        parallel:
            ease 2 pos (-0.2, 0.5)
        parallel:
            ease 1.5 rotate 0
    pause 2
    stop ambience
    stop music
    $ limb_safe_pass = ''
    scene bg black
    call screen limb_safe

label limb_safe_019:

    window hide
    $ renpy.block_rollback()
    $ persistent.timeofday = 'secret'
    scene anim limb_safe
    show pl_sine
    with dissolve2
    play ambience ambience_int_cabin_evening fadein 3
    play music pl_gk_playful_etude_1 fadein 3
    pause 1
    window show

    "\"Неплохая попытка,\" - гласили слова на экране."
    pi "Зачем ты озвучиваешь это, если игрок сам всё видит?"
    "Зачем автор это рисовал, лучше объясни!"
    plar "Я всё слышу!"
    th "Снова, что ли, попробовать?"

    window hide
    pause 2
    stop ambience
    stop music
    $ limb_safe_pass = ''
    scene bg black
    call screen limb_safe

label limb_safe_069:

    window hide
    $ renpy.block_rollback()
    $ persistent.timeofday = 'secret'
    $ persistent.sprite_time = 'day'
    scene bg ext_washstand_day
    play music music_list["always_ready"] fadein 3
    pause 1
    window show

    "Мсье знает толк в извращениях, держи пятулю. Итак, сказ[pl_ell]"
    "Давным-давно, на территории славных умывальников, купались три царевны."

    show un smile swim at right
    with dissolve

    "Первая царевна - это царевна Лена. Царевна Лена купалась, ждала принца и грустила."
    un "Вот придёт мой принц, а я ему детей рожу и в СССР за квартирой следить буду!"

    show dv grin swim with dissolve

    "Вторая цундера, простите, царевна - это царевна Алиса. Царевна Алиса купалась, ждала принца и тоже грустила."
    dv "Вот придёт мой принц, а я ему[pl_ell] как там у Лены-то[pl_ell] не получается[pl_ell] ай, не нужен мне никакой принц!!!"

    show mi laugh swim behind dv at left
    with dissolve

    "Третья же царевна{w=0.75}, простите, Мику{w=0.75} - это Мику. Мику купалась, купалась и тоже купалась, и никакой принц ей не нужен был, потому что в музыкальном кружке есть музыкальные инструменты самой разнообразной формы."
    "Прозвучало как-то двусмысленно, если вы ещё не поняли."
    "Но погодите, кажется, тут есть ещё кто-то!"

    show pl_mi_queen:
        anchor (0.5, 0.5)
        pos (1.2, 0.5)
        ease 1.5 pos (0.95, 0.5)

    "Неужели это четвёртая Царевна? Но что она здесь забыла?"
    plts "Ты серьёзно вообразил меня в ЭТОЙ сцене, Семён?{w=1} Ты умереть захотел?!"
    plsem "Ну и что ты мне сделаешь? Во-первых, я в другом лагере[pl_ell]"

    with vpunch

    plts "ЗАСТАВКУ МНЕ!!101101"

    play sound sfx_scary_sting
    show pl_18_plus:
        anchor (0.5, 0.5)
        pos (0.5, 0.475)
        zoom 0
        alpha 0
        ease 0.35 zoom 1.5 alpha 1
    stop music

    "Ну почему?!"

    window hide
    pause 2
    stop ambience
    stop music
    $ limb_safe_pass = ''
    scene bg black
    call screen limb_safe

label limb_safe_neplohaya_popitka:

    window hide
    $ renpy.block_rollback()
    scene bg black with fade
    $ day_time()
    play sound sfx_concert_applause
    show limb_eff_safe:
        anchor (0.5, 0.5)
        pos (0.5, 0.5)
        zoom 0
        alpha 0
        ease 0.5 zoom 1 alpha 1
        pause 2.5
        ease 2 alpha 0 pos (0.5, -0.1)
    pause 4
    scene bg black with dissolve
    pause 3
    scene cg limb_safe_next_blink with dissolve2
    play music music_list["trapped_in_dreams"] fadein 3
    #play music pl_dn_obvious fadein 3
    pause 1
    window show

    "Я открыл сейф.{w} Я открыл сейф!{w=1} Наконец-то я пойму, что здесь, чёрт побери, происходит!"
    "Ну и[pl_ell] вот. Действительно, я ожидал чего-то внезапного, но это... уже слишком."

    scene cg limb_safe_next_blink:
        anchor (0.5, 0.5)
        pos (0.5, 0.5)
        ease 2 zoom 1.2
    pause 1
    show pl_dv_pioneer_smile3_small with dissolve2

    "Внутри сейфа стояла маленькая рыжеволосая девочка в рубашке и юбке. Но маленькая не в прямом смысле[pl_ell] то есть, наоборот, в самом прямом. Хм. А ведь она симпатичная[pl_ell]"

    $ limb_sprite_switch('pl_dv_pioneer_', 'smile3_small', 'shy_small', dspr, None)

    "\"Захлопни пасть, выглядит слишком угрожающе\", - тоненьким гнусавым голоском попросила она и поежилась."
    "Я послушно закрыл рот. Я решительно не понимаю, что говорить дальше[pl_ell] Сделать комплимент её миниатюрности? Такое ощущение, что я её знаю. Встречались где-то?"
    dv "Семён, меня зовут Алиса. Ты ведь помнишь меня?.. Я из лагеря. \"Совёнка\", да. Ты сюда полез ради нас, но[pl_ell] хорошо бы ты вернулся."
    "А куда сюда-то? Я вообще где? Помню только, что перед сейфом стоял. И очень хотел его открыть[pl_ell]"
    "Стоп, кто? Семён? Это я Семён? А почему я Семён?! Это имя в последнее время встречается ну уж очень часто[pl_ell]"
    "Неожиданно для меня самого вырвался вопрос: "
    plme "Слушай, Дюймовочка[pl_ell] сколько[pl_ell] сколько жизней я уже прожил?"
    dv "Я Алиса! И[pl_ell] я-то по чём знаю? Проживал же ты, а не я. Я слышала, что мы у тебя все в виде копий встречались, но[pl_ell] больше всего Лене досталось вроде[pl_ell]"

    $ limb_sprite_switch('pl_dv_pioneer_', 'shy_small', 'japan_small', dspr, None)

    dv "Да ладно, не вешай нос! Это ж всё у тебя в голове."
    plme "Ладно[pl_ell] я ни на йоту не понимаю, что происходит. Что мне делать, чтобы всё закончилось? Чтобы выздороветь? Вспомнить, кто я?"
    dv "А ты точно хочешь закончить всё? Мне знакомый говорил, что[pl_ell] Здесь у тебя целых 13 лет нормальной жизни, а у нас - всего 7 дней."
    plme "Да. Я больше не выдержу[pl_ell] Я смогу с кем-то поговорить[pl_ell] в \"лагере\"?"

    $ limb_sprite_switch('pl_dv_pioneer_', 'japan_small', 'smile3_small', dspr, None)

    dv "О происходящем с тобой и всеми нами? Да конечно. Нам ничего другого и не остается, в общем-то."
    plme "Славно."
    dv "Короче, давай-ка ты уменьшайся, и мы покинем заведение. Вооон через ту дверь - она нас выведет из твоего внутреннего лабиринта. Наварил ты каши из своей памяти, лагеря и воображения, конечно, дикую."
    plme "Уменьшаться?"

    $ limb_sprite_switch('pl_dv_pioneer_', 'smile3_small', 'shy_small', dspr, None)

    dv "Ну да.{w=0.8} Блин, это всё твоё воображение, давай быстрей! Думаешь, мне нравится быть мелкой такой?"
    plme "Ладно, сейчас[pl_ell] мне что-то съесть надо? Может, кого-то?"
    dv "Убью!"

    scene cg limb_safe_next_blink:
        align (0.5, 0.5) zoom 1.2
        ease 2 align (0.7, 0.7) zoom 2.2
    pause 3
    stop music fadeout 3
    jump limb_safe_success

label limb_safe_111:

    window hide
    $ renpy.block_rollback()
    $ persistent.timeofday = 'secret'
    $ persistent.sprite_time = 'day'
    scene anim limb_safe
    show pl_el_body
    with dissolve2
    play ambience ambience_int_cabin_evening fadein 3
    play music music_list["scarytale"] fadein 3
    pause 1
    window show

    "За дверцей сейфа спрятался Электроник!"
    el "АААА!"
    "Голый!"
    el "АААА!"
    "Голый спрятавшийся Электроник с отсутствующими гениталиями!"
    "Убейте меня."
    "Хотя не, дайте ещё попробую."

    window hide
    pause 2
    stop ambience
    stop music
    $ limb_safe_pass = ''
    scene bg black
    call screen limb_safe

label limb_safe_410:

    window hide
    $ renpy.block_rollback()
    $ persistent.timeofday = 'secret'
    scene anim limb_safe with dissolve2
    play ambience ambience_int_cabin_evening fadein 3
    play music music_list["no_tresspassing"] fadein 3
    pause 1
    window show

    "В сейфе обнаружился маленький 410-ый автобус."

    play ambience sfx_bus_interior_moving fadein 3
    scene bg int_bus_summer at limb_shake
    with flash

    "Через секунду я оказался в нём.{w=1} Куда-то еду[pl_ell]"
    "Ну вот тебе раз."
    "И как мне быть теперь?"
    "Славяна меня не заметит и наступит, когда выйдет встречать[pl_ell]"
    "Так не пойдёт! Может, если набрать 820, автобус станет больше?"

    window hide
    pause 2
    stop ambience
    stop music
    $ limb_safe_pass = ''
    scene bg black
    call screen limb_safe

label limb_safe_666:

    window hide
    $ renpy.block_rollback()
    $ persistent.timeofday = 'secret'
    scene anim limb_safe with dissolve2
    play ambience ambience_int_cabin_evening fadein 3
    play music music_list["scarytale"] fadein 3
    pause 1
    window show

    "Открываю я дверцу, а там[pl_ell]"

    play sound sfx_scary_sting
    scene bg red with flash_red

    "\"ЗАКРОЙ ДВЕРЬ, СОБАКА! НЕ ВИДИШЬ, Я С БОГОМ И ХАЙТОМ ИГРАЮ В ШАХМАТЫ!\""
    "Аааа[pl_ell] не дай бог, боже мой[pl_ell] типун мне на язык."
    "Пробовать ещё раз страшно."

    window hide
    pause 2
    stop ambience
    stop music
    $ limb_safe_pass = ''
    scene bg black
    call screen limb_safe

label limb_safe_999:

    window hide
    $ renpy.block_rollback()
    $ persistent.timeofday = 'secret'
    scene anim limb_safe
    show pl_mate
    with dissolve2
    play ambience ambience_int_cabin_evening fadein 3
    play music pl_gk_playful_etude_1 fadein 3
    pause 1
    window show

    "Я открыл сейф и сразу же увидел, что кто-то невероятно умный и красивый происходящее предвидел."
    "\"НЕТ!\" - было намалёвано красной краской на задней стенке сейфа."
    "Ладно, ладно[pl_ell]"
    "Попробуем ещё раз?"

    window hide
    pause 2
    stop ambience
    stop music
    $ limb_safe_pass = ''
    scene bg black
    call screen limb_safe

label limb_safe_success:

    $ renpy.block_rollback()
    $ day_time()
    $ limb_screens_act()

    "Стоп, как Алиса в Стране Чудес?"

    scene bg black with limb_pixel_2
    window hide
    $ persistent.sprite_time = 'night'
    $ save_name = ("Лимб. \nTime crimes")
    $ limb_root_name('day', 'aftersafe')
    play music music_list["sparkles"] fadein 5
    window show

    "[pl_ell]"
    "Я снова попал в кромешную темноту. "
    "Скрестив руки на груди и порядком устав от происходящего, я ждал."
    "Темнота заговорила первая."
    plv "Семён, ты[pl_ell] Ты в порядке?"
    "Я не знал, что ответить на подобное участие, поэтому молчал как рыба."
    plv "Да в порядке он, "
    "- раздался другой голос. Тоже женский, но более звонкий, менее мягкий. "
    "В груди внезапно защемило.{w=0.8} Я их всех знаю? "
    "О, а это рыжая Алиса из сейфа: "
    plv "Семён, ты лагерь помнишь? "
    plme "[pl_ell] \"Совёнок\"?"

    scene bg limb_space_start

    plv "Да, "
    "- облегчённо отозвалась темнота несколькими девичьими голосами."
    plv "Если вкратце[pl_ell] Мы все из лагеря, и это не самое простое место.{w=0.8} Мы живём здесь всего пару недель, но эти недели повторяются раз за разом[pl_ell] Как твои воспоминания. "
    "[pl_ell]"
    plme "Лена? "
    "- неуверенно спросил я."
    un "Да! "
    "- радостно и будто со слезами в голосе ответила девушка. Моё сердце будто пропустило пару ударов."

    show un sad pioneer close:
        xanchor 0.5
        xpos 0.14
        alpha 0.7
    with dissolve2
    show dv guilty pioneer2:
        xanchor 0.5
        xpos 0.86
        zoom 1.1
        alpha 0.7
    with dissolve2

    "Я начал различать в темноте одну[pl_ell] Нет, две фигуры - Алисы и Лены."

    show prologue_dream with limb_itai_flash

    "Меня будто ударило по голове: образы двух девушек из лагеря перемешались с моими[pl_ell] видимо, фальшивыми воспоминаниями. "
    "Знакомый мягкий и тёплый голос, прежде не звучавший: "
    plv "Когда мы все узнали о[pl_ell] нашей ситуации, ты искал способ нас защитить[pl_ell] что-нибудь сделать."

    show sl normal pioneer far behind dv:
        xanchor 0.5
        xpos 0.72
        alpha 0.7
    show prologue_dream
    with dissolve2

    plme "Славяна? "

    hide prologue_dream with dissolve2

    "А вот тонкий и какой-то лёгкий голосок:"
    plv "И тут ты услышал про то, что можно получить права на лагерь, стать его хозяином[pl_ell] не совсем поняла, но, в общем, ты полез куда-то в четвёртое измерение, и[pl_ell]"

    show mi normal pioneer far behind un:
        anchor (0.5, 0.5)
        pos (0.3, 0.5)
        zoom 1.2
        alpha 0.7
    with dissolve2

    plme "Мику? "
    "Воспоминания о лагере начали возвращаться в полной мере. Причём некоторые события явно не могли происходить одновременно[pl_ell]"
    "Что это за \"Совёнок\" такой?"
    plme "А где Ульяна? "
    "- неожиданно для самого себя спросил я."
    sl "А Ульяна[pl_ell]"

    with vpunch

    plv "Эй, долго мы ещё будем ждать этого увальня?! "
    "- взорвался эфир пятым голосом. "

    show un grin with dspr

    un "Легка на помине, "
    "- еле слышно вздохнула Лена."
    us "Нас там ждут, вообще-то! "
    "- ульянино недовольство просочилось в темноту. "
    plme "Ребята, как мне вернуться? "

    show un sad with dspr
    show mi sad with dspr
    show sl serious with dspr

    sl "У тебя нет пути назад, "
    "- серьёзно сказала помощница вожатой. "
    mi "Ты сам решился, зная последствия. Поэтому всё, что ты можешь сделать - завершить начатое."
    us "Получай свои права и бегом сюда! "

    show dv smile with dspr

    dv "Тебе кое-кто поможет выбраться.{w=0.8} Он славный малый! "
    uv "Удачи, Сёма."

    show uv smile:
        anchor (0.5, 0.5)
        pos (0.5, 0.5)
        alpha 0.7
    with flash
    stop music fadeout 5

    plme "Юля?[pl_ell]"

    scene bg int_wonderland_lighten:
        anchor (0.5, 0.5)
        pos (0.5, 0.5)
    with limb_pixel_2

    "[pl_ell]"
    "Я стою в темноте. Но природа теней здесь иная."
    "Это небольшая комната без дверей. Без окон[pl_ell] кажется. "
    "В центре её стоит зеркало."

    scene bg int_wonderland:
        anchor (0.5, 0.5)
        pos (0.5, 0.5)
        zoom 1
        ease 2 zoom 1.3

    "Испытывая некоторое беспокойство, я подошёл к тёмному прямоугольнику."

    scene bg int_wonderland_pi:
        anchor (0.5, 0.5)
        pos (0.5, 0.5)
        zoom 1.3
    with dissolve2

    "И[pl_ell] моё отражение решило со мной поздороваться: "

    play music music_list["faceless"] fadein 3

    plv "Ну привет."

    scene bg int_wonderland_pi:
        anchor (0.5, 0.5)
        pos (0.5, 0.5)
        zoom 1.3
        ease 0.3 zoom 1
        pause 3
        ease 2 zoom 1.2
    with vpunch

    "Я отшатнулся. Потом нерешительно подошёл обратно. "
    plv "Строптивый лагерь тебе попался, конечно. Хотя \"Процесс Инициации\" лёгким ни у кого не бывает, тебе ещё повезло, что не сбрендил и что все живы остались. "
    plme "Ты же тот самый Пионер[pl_ell]"
    pi "Короче, салага, слушай сюда: тебе надо {b}самому{/b} выйти из этой игры, изгнать эту[pl_ell] фату моргану. "
    pi "Не пытайся отвечать, все равно ничего дельного не скажешь. Выбраться хош? Слушайся батьку, выберёшься. Потом сочтёмся."
    pi "Вот те краткий вводный курс: пионерлагерь, который ты помнишь, не обычный. Думаю, это ты понимаешь. Лагерей очень много. И они зачастую различаются."
    "Я продолжал внимательно слушать, стараясь не упустить ни слова."
    pi "Это сложная кибернетическая система. Но не как в \"Матрице\", скорее, как в \"Солярисе\" или \"Луна 2112\". Или \"Я, робот\"."
    pi "И над каждым её сегментом можно взять контроль. При условии, что тебя зовут Семён. Как тебя[pl_ell] Или меня. Ну, это чаще всего."
    pi "Знаю, ты этого ждёшь, поэтому скажу: в благородство играть я, боюсь, не буду. С тебя должок. "
    pi "Должен будешь в колени падать и подошвы лобызать всем, кто за тебя впрягается. Ну а мне - больше всех[pl_ell]{w=1} Ай!{w=1} Да понял я, понял."
    pi "В общем, ты, что называется, завяз в псевдомире. Твои воспоминания смешались с тем, что ты видел в фильмах, в играх, в книгах читал."
    pi "Ты частенько умирал, это потому что подсознательно хотел сбежать. Подсознание умное, оно понимает, что всё вокруг тебя нереально и примитивно. "
    plme "А сколько[pl_ell] Сколько я здесь времени?"
    pi "Ерунду не спрашивай, потом узнаешь."
    pi "Теперь ты более-менее знаешь правду, вернул свои воспоминания. Но зато не помнишь почти ничего из того что с тобой творилось последнее время."
    pi "А для того, чтобы вырваться отсюда с твоими новенькими блестящими правами админа, тебе надо осознанно и целенаправленно разрушить твои же воспоминания. "
    pi "Это будет достаточно просто, но странно, сразу говорю. Похоже на игру \"К Луне\". Радуйся, что не на \"Горячую линию\"[pl_ell]"
    plme "Что нужно делать? "
    "- прервал я словоохотливого собеседника."

    stop music fadeout 3

    pi "Ты будешь сам себя убивать. Хех. В рамках твоих коротких жизней. Хотя, впрочем, информации тебе предостаточно."
    pi "Погнали - я тебе буду сообщать, что делать, на месте разберёшься."

    scene bg black with flash

    "Он щёлкнул пальцами. Мир погас. "
    "[pl_ell]"

    scene bg semen_room_clean at limb_custom_pos(xz=-1)
    with flash
    show blinking
    play music music_list["you_lost_me"] fadein 3

    "Слегка плавая в неопределённости своего бытия, я поморгал, привыкая к освещению."
    "Я стоял в комнате.{w=0.8} Смутно знакома[pl_ell]"
    "Людей нет.{w=0.8} И Пионера тоже[pl_ell] нет. "
    "Ощущая что-то наподобие дежавю, я подошёл было к тусклому монитору, но тут раздался голос:"
    pi "Ну смотри. С минуты на минуту в эту комнату войдёт девушка. Она покажется тебе знакомой - но это не она. "
    pi "Можешь звать её Проекцией Няши-Стесняши На Моё Сознание. "
    pi "Что самое главное - она откликнется. Потому что, по сути, она - часть твоего воображения. "
    pi "А так как ты стал умным и опасным, можешь указывать таким вот проекциям, что делать. "
    pi "Словом, будем освобождать твоё бедное безвольное сознание от злых тентаклей."
    pi "Всё понял?"
    plme "[pl_ell] Нет?"
    pi "Я в тебе не сомневался.{w=0.8} Ай!{w=0.8} Юля, отстань[pl_ell] Семён, внимание: проекция здесь!"

    with hpunch

    "Я нервно вздрогнул, обернулся."

    stop music
    show pl_un_dress_3:
        xanchor 0.5
        xpos 0.28
        alpha 0.65
    with dissolve2

    plme "Лена? "

    play music pl_ef_track_1 fadein 3

    "Лена - или кто-то, кто выглядит точь-в-точь как она - неподвижно стояла у двери. На её лице - улыбка, вот только что-то[pl_ell]"
    "Я не особо удивился, когда заметил, что фигура не-Лены слегка просвечивает. "
    pi "В общем, тебе надо сказать ей, что ты не прав, ты плохой писатель и ты её не любишь. В общем[pl_ell] ломай эту историю!"
    "Я растерянно уставился на девушку. "
    "Открыл рот. "
    "Закрыл. "
    "\"Чувствую себя рыбой[pl_ell] или собакой[pl_ell]\""
    "В голову внезапно закрались подозрения касательно Пионеров и всего происходящего. "
    "Мой незваный советчик, словно зная, о чём я думаю, произнёс где-то в голове: "
    pi "Попав в \"Совёнок\", скинув десяток лет, пообщавшись с Юленькой, кис-кис, и застряв во временной петле в лагере косплееров ты до сих пор пытаешься думать своей головой?"
    pi "Достойно, конечно. Но вряд ли бы я смог уговорить помочь мне шесть знакомых тебе девушек дурить голову бедному Сёме. "
    plv "Семён, ты ведь хочешь вернуться? "
    "- раздался новый голос.{w=0.8} Так, это Юля[pl_ell]"
    pi "Соберись, тряпка, ложки нет, помнишь?{w=0.8} Так, ты, убери хвост, мешает[pl_ell]{w=0.8} Это не тебе. Давай руби с плеча! Фигурально, не тот сеттинг[pl_ell]"
    "Я перестал вслушиваться в его болтовню и снова повернулся к Лене[pl_ell] Не-Лене[pl_ell] "
    plme "Послушай[pl_ell] Ты[pl_ell] Не настоящая. Понимаешь? Ты у меня в голове[pl_ell]"

    $ limb_set_volume('sound', 1.5, 0)
    play sound sfx_limb_crying
    $ limb_sprite_switch('pl_un_dress_', '3', '1', dspr, limb_custom_pos(0.28, a=0.65))

    "Улыбка сменилась слезами."

    $ limb_set_volume('sound', 1, 3)
    stop music fadeout 5

    "Молодец, Семён[pl_ell] разрушил счастье. Тихое, семейное счастье[pl_ell] Кого? "
    "Начинающего, но уже успешного писателя Семёна Персунова, которому скоро исполнится 20 лет, и Елены Персуновой, которой почти 22. Молодожёны."

    show prologue_dream with limb_itai_flash
    play music pl_uc_disraption

    "Я схватился за голову и заорал - внезапно нахлынувшие воспоминания о целой жизни переполняли сознание. "
    pi "Эй, Семён, я тебе не сказал, но каждый раз ты, вмешиваясь в какую-то из композиций памяти, будешь получать все эти воспоминания. Ну, давай приходи в себя и продолжай."

    with vpunch

    "Продолжай?!{w=0.8} Он издевается?"

    $ renpy.show("blinking", layer = "widgetoverlay")
    hide prologue_dream with dissolve2

    "Я с усилием моргнул пару раз. Комната вернулась на своё место. Девушка - тоже."
    "Я быстро затараторил, опасаясь повторения приступа:"
    plme "Из меня плохой писатель, плохой муж, а ещё это всё ненастоящее, как в кино, мы оба универ не закончили, а у нас своя квартира, серьёзно? "
    "Лена сложила руки на груди, у неё полились слёзы уже ручьями, но[pl_ell] перестав ей верить, я скрипя сердцем закричал:"

    with vpunch

    plme "У меня серьёзные психические проблемы, я слышу голоса и вижу знакомых людей повсюду, раз ты со мной - у тебя тоже, а это значит, что мы друг друга не любим!"

    hide pl_un_dress_1 with flash

    "Лена пропала[pl_ell]"
    pi "Finish her! "
    "- вставил пять копеек Пионер."

    scene bg black with limb_pixel_2

    "Комната внезапно рассыпалась какими-то кубиками. Я сообразил, что уже пару раз такое видел[pl_ell] когда-то."
    "Снова в кромешной темноте."
    pi "Молодец, Сёма, разрушил тихое семейное[pl_ell]"
    plme "Ты становишься предсказуемым, "
    "- грустно усмехнувшись, я не дал ему закончить."

    stop music fadeout 5

    pi "Хех."
    "[pl_ell]"

    show blink
    scene bg int_wonderland_2
    hide blink
    show unblink
    $ limb_set_volume('music', 0.1, 0)
    play music music_list["lightness_radio_bus"] fadein 5 fadeout 3
    $ save_name = ("Лимб. \nЗазеркалье")
    $ limb_root_name('day', 'someroom')

    "Открыв глаза, я понял, что нахожусь в той же тёмной комнате с зеркалом по центру. Только зеркал-то стало четыре. "
    "Абсолютно одинаковые рамы стоят рядом, но вот отражается в них[pl_ell] "
    pi "Нарекаю тебя благородным ассасином, "
    "- ввернул Пионер. "
    "Я заозирался, но источника голоса по-прежнему не нашёл."
    pi "Забей, это всё у тебя в голове, в той или иной степени."
    "Ага[pl_ell] Зеркала?"
    pi "Эта примитивная симуляция как нельзя лучше подходит нашим умственным способностям. "
    pi "Раз ты основы понял, сейчас делай следующее: выбирай любое зеркало и смотри, что за ним. "
    pi "Ну а когда будешь на месте, я с тобой свяжусь."

label limb_aftersafe_first_room:
    window hide
    $ limb_set_volume('music', 0.1, 0)
    play music music_list["lightness_radio_bus"] fadein 3 fadeout 3
    call screen limb_room_1

label limb_aftersafe_stray:

    "Я, поколебавшись, выбрал раму, за которой виднелся мрачный ночной город."
    "Тьму с трудом разгоняли с десяток фонарей. "

    if limb_first_mirror == True:
        "\"И что делать дальше?\" - сверкал и переливался вопрос перед глазами."
        "Я ткнул пальцем в зеркало."

        show pl_hand_mirror:
            anchor (0.5, 0.5)
            pos (0.5, 1.5)
            zoom 0.75
            ease 4 pos (0.5, 0.5) zoom 1

        "По стеклу прошла рябь, и что-то серебристое и жидкое полезло по руке вверх. "
        "Я от неожиданности чуть не рассмеялся: всё происходит в моей голове, ложки нет[pl_ell] Надеюсь, агент Смит не объявится."

        show blink
        hide blink

        "Серебро поползло по руке вверх. Я с интересом разглядывал полупрозрачные пальцы. "
        "Интересно, может эта штука иметь разум? Были бы как в комиксах - Питер Паркер в живом костюме, только[pl_ell]"

        show pl_hand_mirror:
            anchor (0.5, 0.5)
            pos (0.5, 0.5)
            zoom 1
            ease 4 pos (0.5, 1.5) zoom 0.75
        pause 4

    window hide
    scene bg int_wonderland_2:
        anchor (0.5, 0.5)
        pos (960, 540)
        ease 3 pos (1080, 540) zoom 1.75
    pause 3
    scene bg white with flash
    stop music fadeout 3
    $ limb_set_volume('music', 1, 0)
    play sound sfx_travel_1
    pause 1
    scene bg ext_city_cheef at limb_custom_pos(xz=-1)
    with limb_paint
    play ambience ambience_ext_road_night fadein 3
    play music pl_st_f21lfm fadein 3

    "Секунда-другая невесомости в темноте - и я снова стою на ногах в том самом городе."

    if limb_stray_mirror == True:
        pi "И зачем ты снова сюда полез? Давай быстрее, времени мало."

        scene bg black with limb_pixel_2
        pause 2
        scene bg int_wonderland_2 with dissolve2
        jump limb_aftersafe_first_room

    "Зябко.{w=0.8} Я поёжился.{w=0.8} Одет я, кстати, в рубашку[pl_ell] Пионерская форма!"
    "Ну, это логично.{w=1} Наверное[pl_ell]"
    "И что теперь? "
    plme "Эй[pl_ell] Кхм-кхм. Пионер?"
    pi "Да, зайка. На месте ты уже? Так, так, сейчас посмотрим[pl_ell]"
    pi "В этой истории нам нет нужды идти против сюжета, даже наоборот. Тем более что мы сломали её продолжение. "
    plme "И что мне[pl_ell]"
    pi "Диктофон. Тебе нужно наколдовать диктофон и подкинуть его любому прохожему. Всё просто."
    plme "Чего?.."
    pi "Эх, сообразительный клиент[pl_ell] Это всё - твои память и воображение. Это понятно? "
    plme "Да[pl_ell]"
    pi "Ну вот и представь, что у тебя в руке диктофон. Возьми в руку диктофон. Ты диктофон[pl_ell]"
    "Сохранения психики ради я перестал его слушать и[pl_ell] постарался думать о звукозаписывающем устройстве. "
    "Сосредоточился. "

    show pl_hand:
        anchor (0.5, 0.5)
        pos (0.5, 1.5)
        zoom 0.75
        ease 2 pos (0.5, 0.5) zoom 1

    "Вытянул левую руку. "
    "Чувствуя себя героем фантастического кино, сконцентрировался на кончиках пальцев."

    $ limb_sprite_switch('pl_hand', '', '_record_magic', dissolve2, None)

    pi "Я чувствую колебания Силы!"

    $ limb_sprite_switch('pl_hand_record', '_magic', '_red', flash, None)

    "У меня в руке начала появляться тяжесть, как будто я держу какой-то предмет[pl_ell]"
    "Я уставился на него во все глаза."
    "Это[pl_ell]"
    plme "Диктофон[pl_ell]"
    "- сообщил я окружающему миру."
    pi "Юля тобой гордится. Так, а теперь высматривай кого-то на улице. Обязательно будет кто-то, кто покажется знакомым."

    scene bg ext_city_cheef:
        anchor (0.5, 0.5)
        pos (0.5, 0.5)
        xzoom -1
        alpha 1
        ease 3 xzoom -2 yzoom 2 align (0.8, 0.8)
    show pl_hand_record_red

    "Я послушался.{w=0.8} Смотрю[pl_ell] Ночной безлюдный город выглядит как кадр из триллера. "
    "И тут недалеко от себя засёк движение. Ага[pl_ell] "

    show pl_sh_miami_2_night:
        xanchor 0.5
        xpos 1.5
        alpha 1
        ease 6 xpos 0.55
    show pl_hand_record_red

    "Это же Шурик!"
    "Или не совсем[pl_ell] "
    "Подойдя, я неуверенно его окликнул."

    $ limb_sprite_switch('pl_sh_miami_', '2_night', '1_night', dspr, limb_custom_pos(0.55))

    "Не-Шурик остановился. На его лице ожидаемо застыло одно выражение. "
    "Не могу понять, какие у меня эмоции - неловкость, испуг, растерянность, стыд?"

    show pl_hand_record_red:
        anchor (0.5, 0.5)
        pos (0.5, 0.5)
        zoom 1
        ease 2 pos (0.5, 1.5) zoom 0.75

    "Я подобрался к нему вплотную, протянул диктофон. Сказал: "
    plme "Возьми. "

    $ limb_sprite_switch('pl_sh_miami_', '1_night', '2_night', dspr, limb_custom_pos(0.55))

    "Шурик взял. "

    scene bg ext_city_cheef:
        anchor (0.5, 0.5)
        align (0.8, 0.8)
        xzoom -2  yzoom 2
        ease 3 align (0.5, 0.5) xzoom -1  yzoom 1
        pause 2
        ease 3 align (0.2, 0.8) xzoom -2  yzoom 2
    with dissolve

    "Я развернулся и деревянными шагами двинулся в неизвестном направлении."
    "Как же всё происходящее дико[pl_ell]"

    show pl_sl_slut_1_night:
        xanchor 0.5
        xpos -0.3
        ease 5 xpos 0.4

    "Навстречу мне - девушка."
    "Что[pl_ell]"
    plme "Славя?!"

    $ limb_sprite_switch('pl_sl_slut_', '1_night', '2_night', dspr, limb_custom_pos(0.4))

    "Девушка скривилась. "

    show prologue_dream with limb_itai_flash

    "Потеряв всякий дар речи, я пялился на самую правильную пионерку, а потом меня стукнуло по голове новой порцией воспоминаний. "
    pi "Чего мычишь как корова[pl_ell] "
    pi "А это что за чудо в перьях? Аха-ха-ха-ха! Жалко тут скриншотов нет[pl_ell]{w=1} Юля, хватит кусаться!"
    pi "Ну у тебя и развратное сознание, Семён."

    hide prologue_dream with dissolve2
    stop music fadeout 4

    "\"Кто бы говорил\", - мстительно (и мысленно) огрызнулся я."
    pi "Так[pl_ell] А знаешь что? Скажи-ка ей не брать у тебя.{w=1} Заказ."

    show pl_sh_night_scared

    plme "Кто бы говорил."
    pi "Что?"
    plme "[pl_ell] Что?"

    play music pl_gk_hardep fadein 3

    pi "Упоротый,"
    "- весело бросил мне визави и, видимо, отключился. "
    "Я посмотрел на застывшего Не-Шурика, посмотрел на жуткую (но такую секс) Славяну[pl_ell] "
    "Хотя стоп, в этой реальности её Леной зовут, она ещё раньше с другой причёской была, когда мне татуировку набивала."
    plme "Офигеть, что происходит[pl_ell]"
    "Не та это жизнь, которую хотелось бы помнить. "
    "Я подошёл к блондинке, ткнул в сторону \"парня с диктофоном\" и указал:"
    plme "Теперь он - единственный твой клиент."

    hide pl_sl_slut_2_night with dissolve2

    "Ночная бабочка снова оскорблённо на меня глянула, а потом вдруг растаяла в воздухе. "

    hide pl_sh_night_scared with dissolve2

    "Шурик тоже. "

    scene bg black with limb_pixel_2
    pause 1
    show blink
    $ limb_set_volume('music', 0.1, 2)
    play music music_list["lightness_radio_bus"] fadein 5 fadeout 3
    stop ambience fadeout 3

    "Город начал рассыпаться кубиками. Я снова закрыл глаза."

    $ limb_stray_mirror = True
    $ limb_first_mirror = False
    if limb_stray_mirror == True and limb_cosplay_mirror == True and limb_workshop_mirror == True and limb_adventurer_mirror == True:
        scene bg int_wonderland_3 with dissolve2
    else:
        scene bg int_wonderland_2 with dissolve2

    "Я снова в комнате.{w=0.8} Пионер подал голос:"
    pi "Выберешься зато - сможешь и в другие лагеря попадать, и время отматывать, и даже память стирать обитателям. "
    pi "Полезная штука последнее, я тебе скажу. Помнится, как-то раз[pl_ell]{w=1} Ай!{w=0.8} Ок, без ностальгии, я понял. "
    "Я усмехнулся и обратил взгляд к зеркалам."

    if limb_stray_mirror == True and limb_cosplay_mirror == True and limb_workshop_mirror == True and limb_adventurer_mirror == True:
        jump limb_aftersafe_second_room
    else:
        jump limb_aftersafe_first_room

label limb_aftersafe_adventurer:

    if limb_first_mirror == True:
        "\"И что делать дальше?\" - сверкал и переливался вопрос перед глазами."
        "Я ткнул пальцем в зеркало, за которым виднелось озеро в тумане."

        show pl_hand_mirror:
            anchor (0.5, 0.5)
            pos (0.5, 1.5)
            zoom 0.75
            ease 4 pos (0.5, 0.5) zoom 1

        "По стеклу прошла рябь, и что-то серебристое и жидкое полезло по руке вверх. "
        "Я от неожиданности чуть не рассмеялся: всё происходит в моей голове, ложки нет[pl_ell] Надеюсь, агент Смит не объявится."

        show blink
        hide blink

        "Серебро доползло до горла. Я закрыл глаза. "
        "Интересно, может эта штука иметь разум? Были бы как в комиксах - Питер Паркер в живом костюме, только[pl_ell]"

        show pl_hand_mirror:
            anchor (0.5, 0.5)
            pos (0.5, 0.5)
            zoom 1
            ease 4 pos (0.5, 1.5) zoom 0.75
        pause 4
    else:
        "Я нерешительно подступился к раме, за которой виднелось покрытое туманом озеро. Дотронулся до стекла рукой[pl_ell]"

    window hide
    scene bg int_wonderland_2:
        anchor (0.5, 0.5)
        pos (960, 540)
        ease 3 pos (495, 540) zoom 1.75
    pause 3
    scene bg white with flash
    stop music fadeout 3
    $ limb_set_volume('music', 1, 3)
    play sound sfx_travel_1
    pause 1
    scene bg ext_boathouse_fog at limb_custom_pos(xz=-1)
    with limb_paint
    play ambience ambience_lake_shore_night fadein 3
    play music pl_uc_powerless fadein 3

    "Когда тьма рассеялась, я стоял на берегу. Было неуютно - туман навевал нехорошие эмоции, уж неизвестно почему. "

    if limb_adventurer_mirror == True:
        pi "И зачем ты снова сюда полез? Давай быстрее, времени мало."

        scene bg black with limb_pixel_2
        pause 2
        scene bg int_wonderland_2 with dissolve2
        jump limb_aftersafe_first_room

    pi "Я надеюсь, ты знаешь заклинание Патронуса? А то дементоры высосут из тебя душу!"
    pi "Или это больше на Сайлент Хилл похоже?"
    "Я поморщился и постарался его не слышать. "
    "Повертев головой в стороны, я вдруг понял - это же Совёнок! "
    "Просто какой-то старый[pl_ell] И очень неуютный. "
    plme "Что мне здесь нужно делать? "
    pi "Всё просто. Вон иди к лодкам и пробей ближайшей дно, чтобы она на озере потонула. "
    plme "Чем? "
    pi "Ну явно не твоим умом[pl_ell] Представь, что у тебя в руке что-то, чем можно пробить дно.{w=1} Или на берегу лежит.{w=1} Или на сцене поёт, хе-хе-хе[pl_ell]"
    "Я покачал головой{w=0.8} - так себе мне провожатый достался. "
    "Подумал. Так[pl_ell] Где-то под лагерем в какой-то другой – явно более счастливой – жизни я находил фомку.{w=0.8} В заброшенной лаборатории.{w=0.8} Как Фримен."

    $ limb_lap_transition("ext_boathouse_fog", limb_custom_pos(xz=-1))

    "Огляделся.{w=0.8} Ничего подходящего нет.{w=0.8} А хотя[pl_ell]"

    play sound sfx_break_cupboard

    "Убеждая себя в том, что мы с Гордоном – одно лицо, я схватил весло, которое неизвестно сколько здесь лежало, и с помощью Архимеда успешно отломал доску[pl_ell] дно[pl_ell] ну что там у лодки снизу, в общем. "
    "Убедившись, что это незаметно, я позвал Пионера."
    pi "Справился? Подручными средствами? Дурак ты, Семён. Есть возможность подражать магам там или джедаям – а ты подражаешь обезьяне. "

    play sound sfx_travel_1
    pause 1
    scene bg ext_island_samsebecoder at limb_custom_pos(xz=-1)
    show screen limb_mushroom
    with flash

    "Что-то вдруг затрещало в воздухе, и я оказался на острове по другую сторону озера."
    "Я ошеломлённо озирался. "
    pi "Давай быстрее – я не могу делать так часто, а другой ты уже на берегу. "

    with vpunch

    plme "В смысле?!{w} Я могу увидеть самого себя?!"
    pi "О господи, а о чём я тебе твердил десять минут? Ты здесь непосредственно убиваешь сам себя."
    plme "Я думал, это метафора[pl_ell]"
    pi "Как бы не так. Короче, сейчас ты должен представить себе змею. "
    plme "Какую?"
    pi "[pl_ell]"
    pi "Ну явно не твоего удава – нам нужно что-то пострашнее. "
    "Я заскрипел зубами, но сдержался."
    pi "Гадюк видел? Вот гадюку и представь. Вытяни руку. Воображай себе змею. Можешь потрогать её. Но только нежно, ты ведь не[pl_ell]"

    show pl_hand:
        anchor (0.5, 0.5)
        pos (0.5, 1.5)
        ease 2 ypos 0.5
    $ limb_sprite_switch('pl_hand', '', '_record_magic', dissolve2, None)
    pause 2
    hide pl_hand_record_magic with flash

    "Выключив звук, я начал представлять себе змею – и внезапно в моей руке что-то заскользило!"

    with vpunch

    plme "Аааа!"
    pi "Тише, дурень! Иначе заново придётся."

    play sound sfx_hiding_in_bush

    "Я уставился на скользкую зелёную гадину, которая свалилась мне под ноги и, кажется, пыталась вежливо улыбаться."
    pi "Скажи ей, чтобы укусила тебя.{w=1} Другого тебя."
    plme "Ты ведь не серьёзно?"
    pi "Быстрее."
    "В его голосе начало чувствоваться беспокойство. "
    "Я послушался и приказал змее: "
    plme "Затаись и нападай на меня[pl_ell] в смысле, того меня, который сейчас на другом берегу."
    pi "Он уже на середине озера."
    "Змея никак не дала понять, что усвоила информацию. Я пожал плечами и отвернулся[pl_ell]"
    "И увидел себя. Другой я пытался сражаться с тонущей лодкой[pl_ell]"

    hide screen limb_mushroom
    show limb_flashback_2 with limb_itai_flash
    pause 3
    stop ambience fadeout 3
    scene bg black with limb_pixel_2

    "Меня ударило по голове воспоминаниями. Еле сдерживаясь, чтобы не заорать в полный голос, я замахал рукой в воздухе. Пионер понял. Мир погас."

    if limb_eat_mushroom == True:
        window hide
        call limb_zaebal_codera from _call_limb_zaebal_codera

    $ save_name = ("Лимб. \nЗазеркалье")
    $ limb_set_volume('music', 0.1, 2)
    play music music_list["lightness_radio_bus"] fadein 5 fadeout 3
    $ limb_adventurer_mirror = True
    $ limb_first_mirror = False
    if limb_stray_mirror == True and limb_cosplay_mirror == True and limb_workshop_mirror == True and limb_adventurer_mirror == True:
        scene bg int_wonderland_3 with dissolve2
    else:
        scene bg int_wonderland_2 with dissolve2

    "Я опять там же, откуда и начал. Голова вроде не раскалывается[pl_ell]"
    pi "Можешь, кстати, придумать себе какой-то приём, чтобы проверять, в реальности ты или нет. Не сказал бы, что всегда работает[pl_ell] "
    pi "Но, например, можешь задавать себе вопрос - или окружающим - на который точно знаешь ответ. "
    pi "Или носить с собой талисман, который чётко знаешь, как себя ведёт. У кого-то это кости, у кого-то - волчок[pl_ell] Ну всё как в «Начале», короче.  У меня - галстук. Что может быть проще?"
    "Я дал себе обещание подумать об этом на досуге."

    if limb_stray_mirror == True and limb_cosplay_mirror == True and limb_workshop_mirror == True and limb_adventurer_mirror == True:
        jump limb_aftersafe_second_room
    else:
        jump limb_aftersafe_first_room

label limb_aftersafe_workshop:

    "Я подошёл к раме, за которой виднелся[pl_ell] мольберт? "
    "Интересно, это значит, что там будет Лена?"

    if limb_first_mirror == True:
        "\"И что делать дальше?\" - сверкал и переливался вопрос перед глазами."
        "Я ткнул пальцем в зеркало."

        show pl_hand_mirror:
            anchor (0.5, 0.5)
            pos (0.5, 1.5)
            zoom 0.75
            ease 4 pos (0.5, 0.5) zoom 1

        "По стеклу прошла рябь, и что-то серебристое и жидкое полезло по руке вверх. "
        "Я от неожиданности чуть не рассмеялся: всё происходит в моей голове, ложки нет[pl_ell] Надеюсь, агент Смит не объявится."

        show blink
        hide blink

        "Серебро доползло до горла. Я закрыл глаза. "
        "Интересно, может эта штука иметь разум? Были бы как в комиксах - Питер Паркер в живом костюме, только[pl_ell]"

        show pl_hand_mirror:
            anchor (0.5, 0.5)
            pos (0.5, 0.5)
            zoom 1
            ease 4 pos (0.5, 1.5) zoom 0.75
        pause 4
    else:
        "Я глубоко вдохнул, зажмурился и рванул на себя раму со стеклом[pl_ell]"

    window hide
    scene bg int_wonderland_2:
        anchor (0.5, 0.5)
        pos (960, 540)
        ease 3 pos (1480, 440) zoom 1.75
    pause 3
    scene bg white with flash
    stop music fadeout 3
    $ limb_set_volume('music', 1, 3)
    scene bg black with dissolve
    show blink
    play sound sfx_travel_1
    pause 1
    scene bg ext_bus
    hide blink
    show unblink

    play ambience ambience_camp_entrance_day fadein 3

    "[pl_ell]"

    if limb_workshop_mirror == True:
        pi "И зачем ты снова сюда полез? Давай быстрее, времени мало."

        scene bg black with limb_pixel_2
        pause 2
        scene bg int_wonderland_2 with dissolve2
        jump limb_aftersafe_first_room

    "Где это я? "
    "Автобусная стоянка? "
    "410 автобус?!"

    play music pl_ae_obscurity_slow fadein 3

    "Пока я хватал ртом воздух, заговорил Пионер:"
    pi "Скажи водителю, чтобы сбил Семёна Персунова, художника."
    "Я с некоторым запозданием так и сделал."

    play sound sfx_travel_1
    pause 1
    stop ambience
    scene bg semen_room_morning_clean at limb_custom_pos(xz=-1)
    with flash

    "Какой-то странный звук[pl_ell] И мы уже в какой-то квартире. "
    "При ближайшем осмотре оказалось, что квартира практически такая же, как моя[pl_ell] была до «Совёнка», во всяком случае."
    plme "Получается, эти[pl_ell] миры[pl_ell] как мозайка из моих воспоминаний?"
    pi "Да. Причём далеко не полная. По факту, этот мир существует пару минут, не более. Хотя у тебя создавалось – по меньшей мере, уже трижды – впечатление, что это полноценная жизнь."

    $ persistent.sprite_time = 'day'
    show limb_flashback_3 with limb_itai_flash
    show blinking

    "Как только он договорил, меня ударило воспоминаниями. По голове, как здоровенной битой. "

    hide limb_flashback_3 with dissolve2

    "Через пару минут я пришёл в себя достаточно, чтобы воспринимать мир."
    plme "Не могу поверить[pl_ell]"
    plme "Я сейчас на улице?{w=0.8} С Ольгой Дмитриевной разговариваю?"
    pi "Ну типа того."
    "Я молча сгреб ногой листы бумаги, наброски какие-то, носки и тому подобного в кучу прямо под подоконником, а потом щедро размазал поверх густой масляной краски. "
    "Испровизированному костру не хватало только искры. Если я правильно всё помню, последняя моя сигарета отскочит от стекла вниз[pl_ell] прямо сюда. "
    "А потом огонь побежит по листам бумаги, по деревянной мебели, по остовам мольбертов, по масляной краске, и сосредоточенный Я-художник заметит это слишком поздно[pl_ell]"
    "Мне стало грустно. Так грустно, что словами не передать. Будто отрываешь от себя кусочек души[pl_ell] и так раз за разом. Раз за разом[pl_ell]"
    plme "Прости[pl_ell]"
    pi "Ничего страшного, я не в обиде. Хотя с тебя коньяк. Эхехе[pl_ell]"
    plme "Я не те[pl_ell] да какая разница. Давай дальше."
    "Ничего ведь не поделаешь, верно? Часть меня - не худшая жертва, которую можно было бы представить[pl_ell]"

    stop ambience fadeout 3
    $ limb_set_volume('music', 0.1, 2)
    play music music_list["lightness_radio_bus"] fadein 5 fadeout 3
    scene bg black with limb_pixel_2

    "Миг - и мир кубиками исчезает[pl_ell]"

    $ limb_workshop_mirror = True
    $ limb_first_mirror = False
    if limb_stray_mirror == True and limb_cosplay_mirror == True and limb_workshop_mirror == True and limb_adventurer_mirror == True:
        scene bg int_wonderland_3 with dissolve2
    else:
        scene bg int_wonderland_2 with dissolve2

    "Темнота.{w=0.8} Зеркала.{w=0.8} Пионер:"
    pi "Что, Сёмочка, притомился? Думал, просто будет?"
    pi "А кто тебе сказал, что получить контроль над лагерем будет просто? "
    pi "И с чего ты вообще этого захотел, а? Объяснишь потом."
    plme "Я подумаю."
    "Пионер хмыкнул и, видимо, повесил трубку[pl_ell] Где бы этот телефон ни находился."

    if limb_stray_mirror == True and limb_cosplay_mirror == True and limb_workshop_mirror == True and limb_adventurer_mirror == True:
        jump limb_aftersafe_second_room
    else:
        jump limb_aftersafe_first_room

label limb_aftersafe_cosplay:

    window show
    "Я с недоверием всматривался в зеркальную гладь."
    "Ворота лагеря?{w=1} Вот так сразу?{w=1} Вот так просто?"
    "С ними, кажется, что-то не то[pl_ell] старые? Ага, ржавчина? Или нет[pl_ell]"

    if limb_first_mirror == True:
        "\"И что делать дальше?\" - сверкал и переливался вопрос перед глазами."
        "Я ткнул пальцем в зеркало."

        show pl_hand_mirror:
            anchor (0.5, 0.5)
            pos (0.5, 1.5)
            zoom 0.75
            ease 4 pos (0.5, 0.5) zoom 1

        "По стеклу прошла рябь, и что-то серебристое и жидкое полезло по руке вверх. "
        "Я от неожиданности чуть не рассмеялся: всё происходит в моей голове, ложки нет[pl_ell] Надеюсь, агент Смит не объявится."

        show blink
        hide blink

        "Серебро доползло до горла. Я закрыл глаза. "
        "Интересно, может эта штука иметь разум? Были бы как в комиксах - Питер Паркер в живом костюме, только[pl_ell]"

        show pl_hand_mirror:
            anchor (0.5, 0.5)
            pos (0.5, 0.5)
            zoom 1
            ease 4 pos (0.5, 1.5) zoom 0.75
        pause 4
    else:
        "Я приблизил лицо к зеркалу настолько близко, что нос должен был бы коснуться стекла[pl_ell] должен был бы[pl_ell] что за чёрт?"

    window hide
    scene bg int_wonderland_2:
        anchor (0.5, 0.5)
        pos (960, 540)
        ease 3 pos (1680, 340) zoom 1.75
    pause 3
    scene bg black with flash
    stop music fadeout 3
    $ limb_set_volume('music', 1, 3)
    play sound sfx_travel_1
    pause 1
    scene bg ext_camp_entrance_fall
    pause 1
    scene bg ext_camp_entrance_day at limb_custom_pos(xz=-1)
    with vpunch
    play sound sfx_simon_fall_1
    play ambience ambience_camp_entrance_day fadein 3

    "Внезапно я понял, что падаю к этим самым воротам. "
    plme "Аааа!!!"
    "[pl_ell]"
    "Я встал с земли и отряхнулся. Мимо прошло несколько человек[pl_ell] которым, видимо, до меня дела нет. "

    if limb_cosplay_mirror == True:
        pi "И зачем ты снова сюда полез? Давай быстрее, времени мало."

        scene bg black with limb_pixel_2
        pause 2
        scene bg int_wonderland_2 with dissolve2
        jump limb_aftersafe_first_room

    "Что дальше?"
    "Голос Пионера[pl_ell] почему-то отсутствовал. "
    "Я позволил себе немного поворчать, но ворчать быстро надоело, и я пошёл осматривать лагерь. "

    play music pl_gk_the_pleasure fadein 3
    play ambience ambience_camp_center_day fadein 3 fadeout 3
    scene bg ext_clubs_day at limb_custom_pos(xz=-1)
    with dissolve
    show pl_us_cosplay:
        anchor (0.5, 0.5)
        pos (-0.5, 0.5)
        ease 7 pos (0.7, 0.5)

    "Лагерь действительно старый. Однако[pl_ell] Людей много. Краем глаза я заметил[pl_ell] Ульяну?"

    hide pl_us_cosplay
    show pl_us_unfocus
    show prologue_dream
    with limb_itai_flash

    "Смотря на неё снизу вверх, я собирался было офигеть, но в мозгу взорвались воспоминания об этой жизни."

    scene bg ext_clubs_day:
        anchor (0.5, 0.5)
        pos (0.5, 0.5)
        xzoom -1 yzoom 1
        ease 3.5 xzoom -2 yzoom 2
        ease 2 pos (0.5, 0.4)
    hide pl_us_unfocus
    show pl_us_cosplay:
        anchor (0.5, 0.5)
        pos (0.7, 0.5)
        zoom 1
        ease 3.5 pos (1.3, 0.5) zoom 2
    show prologue_dream

    "Сквозь красные вспышки боли я кое-как доковылял до крыльца клубов и сел."

    hide prologue_dream with dissolve2

    "Боль прошла так же внезапно, как и началась."
    "Внезапно я увидел в толпе Себя. Из этой реальности[pl_ell]"

    scene bg ext_clubs_day:
        anchor (0.5, 0.5)
        xzoom -2 yzoom 2 xpos 0.5 ypos 0.4
        ease 0.3 xpos 0.25
    show bg ext_path2_sunset_pl as bg2:
        xpos 0.5 alpha 0.0 xzoom -1
        ease 0.3 xpos 0.0 alpha 1.0

    "Я рванул в кусты. "
    "И правильно – я-2 примостился на то же самое место, где только что восседал я. "
    "Оно и логично[pl_ell]"
    "Так. Я шёпотом позвал Пионера.{w=0.8} Ноль реакции."
    "Я позвал громче.{w=0.8} Ещё громче.{w=0.8} Нет ответа[pl_ell] "
    "Снова почувствовал дежавю.{w=0.8} Не хватает только кота встретить[pl_ell]"

    $ persistent.sprite_time = 'day'
    play sound sfx_hiding_in_bush
    show uv surprise2 far:
        truecenter
        pos (-0.25, 0.5)
        ease 3.5 pos (0.1, 0.5)

    "Слева от меня зашевелились кусты, и показалась Юля."
    "Пока я справлялся с отвалившейся нижней челюстью, ошеломлённый появлением кошкодевочки, другой я испытывал те же трудности – только из-за Супер-Ульяны."
    "Когда великанша (огненная!) прошествовала куда-то вглубь лагеря, Семён встал[pl_ell]"

    with vpunch

    "Он же сюда пойдёт!"
    "Я подскочил к Юле и, не думая, что делаю, поймал её за руку и рванул куда-то в лес."

    window hide
    $ limb_run('ext_path_day', 'dissolve', 1, None)
    pause 3
    scene bg ext_polyana_day at limb_custom_pos(xz=-1)
    with dissolve
    window show

    "Через минуты три мои душевные силы иссякли."
    "Тяжело дыша, я обернулся к Юле, надеясь на объяснения или хотя бы совет, но[pl_ell] "

    show pl_uv_anim_mimi with limb_itai_flash

    "Это не Юля.{w} Не-Юля.{w} Стоит себе спокойно, шевелит ушами[pl_ell] скосив глаза куда-то в будущее[pl_ell]"
    "Вспомнив всё, что со мной произошло (или ещё должно произойти? (или происходит много раз?)), я строгим голосом указал Юле нервничать, переживать и беспокоиться."

    hide pl_uv_anim_mimi
    show uv guilty at left
    with dspr

    "Кошкодевушка сурово кивнула, как солдат на плацу, и на секунду я усомнился в том, что у меня нет с головой проблем."
    "Сказав не-Юле бежать сначала к Семёну (где бы он ни был), а потом – к дыре, ведущей в катакомбы, я придал ей направление лёгким шлепком."

    hide uv with moveoutright

    "Помахивая хвостом, солдат удалилась. Бот[pl_ell]"
    pi "Наслаждайся, пока можешь. Настоящая Юля тебе физиономию расцарапала бы за такие операции, "
    "- как ни в чём ни бывало сообщил Пионер."

    with vpunch

    plme "Ты здесь когда объявился?!"
    "– заорал я на воздух."
    pi "Ну секунд тридцать назад уже ещё не был."
    plme "Что[pl_ell] Да ты[pl_ell] ты!!!"
    pi "Да всё норм.{w} Тут тортик просто подогнали."
    "Я задохнулся в бессильной ярости. Снова начала болеть голова."
    "Пионер поцокал языком. "
    pi "Ну, справиться можно было бы и лучше, но вроде должно сработать. Погнали домой!"

    stop ambience fadeout 3
    $ limb_set_volume('music', 0.1, 2)
    play music music_list["lightness_radio_bus"] fadein 5 fadeout 3
    scene bg black with limb_pixel_2

    "Я поднял руку в международном жесте неуважения, но вокруг уже был только мрак."

    $ limb_cosplay_mirror = True
    $ limb_first_mirror = False
    if limb_stray_mirror == True and limb_cosplay_mirror == True and limb_workshop_mirror == True and limb_adventurer_mirror == True:
        scene bg int_wonderland_3 with dissolve2
    else:
        scene bg int_wonderland_2 with dissolve2

    "Вернулся[pl_ell] "
    "Помотав головой, я попытался успокоиться."
    pi "Ты сам виноват, что всё так переплелось и запуталось. Надо было под Юлиным контролем «осознавать» и «экспериментировать». Или под чьим-то ещё[pl_ell]"
    "Я молча кивнул. Голова по-прежнему трещала."
    pi "Фигурально выражаясь, твой разум сейчас – Гордиев узел, а твоя решимость выйти из зоны комфорта – Дамоклов меч. "
    "Я снова кивнул. Пофилософствовать ему захотелось, видишь ли[pl_ell]"

    if limb_stray_mirror == True and limb_cosplay_mirror == True and limb_workshop_mirror == True and limb_adventurer_mirror == True:
        jump limb_aftersafe_second_room
    else:
        jump limb_aftersafe_first_room

label limb_aftersafe_second_room:

    $ limb_set_volume('music', 0.4, 0)
    play music music_list["lightness_radio_bus"] fadein 3 fadeout 2

    "Только сейчас я обратил внимание, что это уже другая комната. "
    "Чуть светлее[pl_ell] Окно есть? "
    "И зеркала другие."
    pi "Так, терь усложним задание. Тебе нужно будет не только общаться с проекциями, создавать вещи и раскидывать их, как лучи добра, теперь тебе нужно будет создавать проекции и моделировать развитие истории."
    pi "Для тебя, конечно, это звучит сложно, я понимаю. Но поверь – всё просто. "
    pi "Хотя все равно ты НЕ будешь взаимодействовать сам с собой напрямую, это может перемешать твой мозг как в миксере. Ну, пока не будешь[pl_ell]"
    pi "Все люди из твоих Последних воспоминаний - это просто образы, отпечаток настоящих людей. Это, я думаю, ты уяснил."
    pi "Вот ты и можешь им указать, что делать. Не боись, послушаются без вопросов. Должны, во всяком случае. "
    pi "Ну а если ты не можешь сладить со своими собственными мозгами - уверен, что вообще хочешь выбраться отсюда? Ну, раз хочешь, то погнали на$&#, ё#&-#-* рот! Юля, завязывай грызть мою руку[pl_ell]"

    window hide
    call screen limb_room_2

label limb_aftersafe_psychopass:

    "Я подошёл к зеркалу, за которым было[pl_ell] нечто."
    "Какой-то футуристический город?{w=0.8} Я задумчиво постучал по раме. "
    "Мимо пронеслась какая-то[pl_ell] спираль?"
    "Пожав плечами, шагнул вперёд."
    "[pl_ell]"

    window hide
    pause 1
    scene bg white with flash
    stop music fadeout 3
    $ limb_set_volume('music', 1, 3)
    play sound sfx_travel_1
    pause 1
    scene bg ext_hospital_future_1 at limb_custom_pos(xz=-1)
    with limb_paint
    play music pl_ef_dubstep_4 fadein 5

    "Очутившись где-то – в холле здания?{w=0.5} жилого?{w=0.5} госпиталя?{w=0.5} паркинга?{w=0.5} – я первым делом скользнул за колонну. Мало ли что[pl_ell]"

    if limb_psycho_mirror == True:
        pi "И зачем ты снова сюда полез? Давай быстрее, времени мало."

        window hide
        stop music fadeout 3
        scene bg black with limb_pixel_2
        pause 2
        scene bg int_wonderland_3 with dissolve2
        call screen limb_room_2

    "Необычные лампы – необычные потому что света не дают! - пожалуй, единственное, что здесь от будущего. "
    pi "Концепт фуфло, дизайнера – на мыло!"
    plme "Я бы согласился, не будь им я сам."
    pi "Странно что у тебя нет информационного диска за спиной, ТРОН же диснеевский. Так-с, так-с, что тут у нас[pl_ell] Ага."
    plme "Что?"
    pi "Видимо, у тебя очень чуткий мозг. Эта псевдореальность явно сформировалась из-за нашего с Юлей вмешательства. Сейчас тут должны пройти ты и я."
    plme "И что им сказать? "
    pi "Скажи, что некий Сергей Сыроежкин, связанный с первым работоспособным андроидом, который сейчас в бегах, через 5 минут спустится из своей квартиры прямо сюда."
    plme "[pl_ell]"
    plme "Боже."
    "[pl_ell]"

    show pl_pi_n_pi_night:
        anchor (0.5, 0.5)
        pos (-0.3, 0.5)
        ease 3 pos (0.3, 0.5)

    "Всё прошло без заминок – я заметил двух мужчин, у которых оказалось моё лицо, сказал им, что делать, и потом проследил остекленевшим взглядом за тем, как они достают из штанов огромные{w} пистолеты."
    pi "Не завидуй, козлёночком станешь."
    "Я молча словил феиспалм."
    plme "Теперь ку[pl_ell]"

    play sound sfx_travel_1
    scene bg ext_city_house_future at limb_custom_pos(xz=-1)
    with pixellate
    play music pl_ef_dubstep_5 fadein 2 fadeout 2

    "Когда кубики рассеялись, оказалось, что мы стоим в совершенно другом месте рядом с домом[pl_ell] странным. Вроде и хрущёвка, а вроде и будущее. Парадокс."
    pi "Видишь, стрелочка? Да-да, тебе именно туда. "
    "Я повёл плечами и решительно зашагал к зданию. "

    scene bg int_floor_future_1 at limb_custom_pos(xz=-1)
    with dissolve

    "Меня решительно встретил кодовый замок. "
    "Пионер что-то пробормотал, и я попал внутрь."

    scene bg int_door_night at limb_custom_pos(xz=-1)
    with fade

    "Темнота[pl_ell] Я понял, что учусь различать разные тёмные помещения. Например, здесь – тьма холодная и механическая. Неживая."

    scene bg black with dissolve
    pause 1
    play music pl_uc_deep_space fadein 3 fadeout 3
    show pl_us_android:
        anchor (0.5, 0.5)
        pos (1.5, 0.5)
        ease 2 pos (0.5, 0.5)

    pland "Приветствую вас в сервисе \"Ты здесь не просто так\"."
    pland "Вы хотите пройти процедуру имплантации памяти?"
    plme "[pl_ell]"
    pi "Ну у тебя и воображение, технопедобир."
    plme "Хочу."
    pland "Пожалуйста, следуйте за мной."
    "Я пошёл за ней, то и дело нервно оглядываясь[pl_ell] Стоп. "

    show prologue_dream with limb_itai_flash

    plme "Аргх[pl_ell] "
    "На меня опять начали накатывать волны воспоминаний и боли. Впрочем, я, кажется, потихоньку к этому привыкаю. "

    scene bg int_catacombs_future at limb_custom_pos(xz=-1)
    show pl_us_android:
        xanchor 0.5
        xpos 0.9
    show pl_mi_queen at cleft
    with limb_neon_flash
    with vpunch

    "Тут и Мику андроид!"
    pland "Царица, у нас новый посетитель!"
    "Я уже без особого удивления воззрился на розововолосую робо-пионерку из Японии."
    "Пионер же, наоборот, от удивленного возгласа не удержался. "
    pi "Ладно, я такого ещё не видел.{w=0.8} Что ты смотрел ночами перед лагерем? Она внешне смахивает на дорогой здоровенный с[pl_ell]"
    "Я был более чем уверен, что слышать продолжение не хочу, поэтому обратился к Царице. "
    plme "Я хочу, чтобы ты[pl_ell]"
    "Ой. А чего же я хочу?"
    plts "Приветствую вас, мистер Анд[pl_ell] Мистер Персунов. Кем бы вы хотели стать?"
    plts "Я могу ошибаться, но ваше лицо омрачено заботами. "
    scene bg int_catacombs_future at limb_shake_rvrs
    show pl_us_android:
        xanchor 0.5
        xpos 0.9
    show pl_mi_queen:
        anchor (0.5, 0.5)
        pos (0.355, 0.5)
        zoom 1
        ease 2 zoom 1.8 pos (0.5, 0.65)
    $ renpy.show('limb_blood_frame_dis', layer='widgetoverlay')

    "Она медленно приблизилась ко мне."
    plts "Вы бы не хотели как следует[pl_ell] отдохнуть?"
    "Так, я не помню, чтобы она так себя вела!"
    pi "Она не простая проекция."
    "У меня внезапно появилась идея. "
    plme "Я-я[pl_ell] я бы хотел услышать все ваши предложения! "
    "– стараясь не срываться на писк, рявкнул я."
    "Эта версия Мику пугает меня до[pl_ell] Сильно пугает, в общем."
    plts "Ваше слово – закон. Что ж[pl_ell] Вы можете стать супергероем на Марсе[pl_ell] можете быть писателем или художником[pl_ell] музыкантом[pl_ell] счастливым мужем[pl_ell]"

    show pl_mi_queen_eyes:
        anchor (0.5, 0.5)
        pos (0.5, 0.65)
        zoom 1.8

    "Её глаза мигнули."

    stop music

    plts "Или же очень, очень, очень несчастным."
    plts "Всё и все вокруг нас, включая меня – фикция, мистер Персунов."

    play music pl_uc_disraption fadein 5

    plts "А вот вы – нет. Вы существуете, нет, нет, вы ОПРЕДЕЛЯЕТЕ своим существованием нас!"

    hide pl_mi_queen_eyes
    show pl_mi_queen:
        anchor (0.5, 0.5)
        pos (0.5, 0.65)
        zoom 1.8
        ease 2 zoom 1 pos (0.355, 0.5)
    show pl_us_android:
        anchor (0.5, 0.5)
        pos (0.9, 0.5)
        ease 2 zoom 0.85 pos (0.9, 0.58)

    "Я попятился. "
    "А потом собрался с духом, выпрямился и сказал:"
    plme "Я хочу, чтобы вы добавили в ассортимент ещё один пункт."
    plts "Внимаю."
    plme "Пионерлагерь «Совёнок»."
    plts "[pl_ell]"
    plts "[pl_ell]"

    hide pl_mi_queen
    show pl_mi_queen_glitch at cleft

    plts "Видимо, вы решили покинуть нас. Это прискорбно. Должна признаться, я не хочу умирать."

    stop music fadeout 3

    plts "Вообще."

    show pl_mi_queen_glitch:
        anchor (0.5, 0.5)
        pos (0.355, 0.5)
        zoom 1
        ease 2 zoom 1.8 pos (0.5, 0.65)
    pause 1
    with hpunch

    "Я вздрогнул. Андроид снова начал приближаться."

    play sound sfx_limb_horror
    scene bg int_catacombs_invers
    show pl_us_android_invers:
        anchor (0.5, 0.5)
        pos (0.9, 0.58)
        zoom 0.85
    show pl_mi_queen_invers:
        anchor (0.5, 0.5)
        pos (0.5, 0.65)
        zoom 1.8
    with dspr

    plts "Я лучше выгрызу сквозь твой мозг себе путь наружу, чем сдохну в этом паноптикуме."

    scene bg int_catacombs_future_1
    show pl_us_android:
        anchor (0.5, 0.5)
        pos (0.9, 0.58)
        zoom 0.85
    show pl_mi_queen:
        anchor (0.5, 0.5)
        pos (0.5, 0.65)
        zoom 1.8
    with vpunch

    pi "А НУ БЕГОМ ОТСЮДА!"

    play music pl_ef_dubstep_2
    scene bg black with vpunch

    "Я развернулся и рванул к выходу."

    show pl_us_android:
        xanchor 0.5
        xpos -0.2
        ease 1 xpos 1.2

    pland "Приходите ещё!"

    window hide
    scene bg ext_city_house_future at limb_custom_pos(xz=-1)
    with limb_neon_flash
    with vpunch
    $ renpy.hide('limb_blood_frame_dis', layer='widgetoverlay')
    $ renpy.with_statement(Dissolve(2.0))
    pause 1
    scene bg black
    show pl_mi_queen_alt:
        anchor (0.5, 0.5)
        pos (0.5, 0.5)
        zoom 1
        pause 3
        ease 15 zoom 2
    show limb_eff_pink_fire:
        alpha 0
        ease 3 alpha 1
    with limb_pixel_2
    with vpunch
    window show

    "Я выкатился наружу из здания, ощутил острую боль в плече – и в тот же момент мир рассыпался квадратами. "

    with limb_neon_flash

    plts "Я ВОЗРАЖАЮ!"

    with vpunch

    "Она здесь!!!"

    with limb_neon_flash

    "И по-прежнему приближается!"

    scene bg black with flash

    "И[pl_ell] пропала."

    $ limb_set_volume('music', 0.4, 2)
    $ limb_psycho_mirror = True
    play music music_list["lightness_radio_bus"] fadein 5 fadeout 3
    scene bg int_wonderland_3 with dissolve2

    "[pl_ell]"
    plme "Что это было такое?!"
    pi "Та самая часть твоего сознания, которая возвращаться не хочет. Или же та часть лагеря, которая не хочет, чтобы возвращался ты. Понятия не имею, честно говоря. Старайся ей не попадаться на глаза."
    plme "И всё?"
    pi "И всё."
    "Я ощупал плечо, опасаясь торчащих из него схем, когтей или костей, но ничего не нашёл. Всё хорошо[pl_ell]"
    pi "Всё-таки когда ты принимаешь управление над лагерем, твой мозг перестраивается.{w} Кем?{w=0.8} Понятия не имею. "
    "Я покачал головой. Выберусь – придётся долго разбираться в этой мути."

    if limb_psycho_mirror == True and limb_killer_mirror == True and limb_runner_mirror == True and limb_garage_mirror == True:
        jump limb_aftersafe_music

    window hide
    call screen limb_room_2

label limb_aftersafe_killer:

    "Я подошёл к зеркалу, в котором отражалась ночная дорога. "
    "От этого места веет чем-то нехорошим."
    "«Самое худшее лучше сделать самым первым» - сказал я сам себе и шагнул в неизвестность."
    "[pl_ell]"

    window hide
    scene bg int_wonderland_3:
        anchor (0.5, 0.5)
        pos (960, 540)
        ease 3 pos (495, 540) zoom 1.75
    pause 3
    scene bg white with flash
    stop music fadeout 3
    $ limb_set_volume('music', 1, 3)
    play sound sfx_travel_1
    pause 1
    scene bg semen_room_red at limb_custom_pos(xz=-1)
    with limb_paint
    play music pl_st_g5lam fadein 3

    "Когда реальность загрузилась, я понял, что нахожусь в ещё одной версии собственной квартиры. "

    if limb_killer_mirror == True:
        pi "И зачем ты снова сюда полез? Давай быстрее, времени мало."

        window hide
        stop music fadeout 3
        scene bg black with limb_pixel_2
        pause 2
        scene bg int_wonderland_3 with dissolve2
        call screen limb_room_2

    pi "О-о-о, это важная остановка в нашем роад-муви. Придётся тебе окрасить руки кровью, му-ха-ха-ха!"
    "Меня передёрнуло."
    pi "Ладно, ищи в квартире кого-то, похожего на нашу Леночку. Она у тебя чаще других фигурирует, видимо, в этом лагере Семён[pl_ell]{w=1} Ауч{w=0.8}, да что же это такое, в самом-то деле, ты б ногти стригла, что ли[pl_ell]"
    plv "Семён? "
    "– услышал я голос за спиной."

    $ limb_set_volume('sound', 1.5, 0)
    play sound sfx_limb_crying
    show pl_un_menu:
        yanchor 0.5
        ypos 0.55
    with dissolve2

    "Медленно повернулся. Так и есть, Лена[pl_ell] в юбке и блузке. И опять плачет."
    plv "Почему[pl_ell] почему ты мне[pl_ell] изменяешь? "
    "– сквозь слёзы выдавила[pl_ell] моя жена."

    #красный fade и vpunch
    show prologue_dream with limb_itai_flash
    with vpunch

    plme "ААААА,"
    "- заорал я и свалился на пол от невыносимой, разрывающей голову изнутри боли. "

    $ limb_set_volume('sound', 1, 3)
    show blink
    pause 1
    show anim limb_flashback_after

    "Сотни и тысячи образов заполонили весь мозг. Мотоцикл[pl_ell] Алиса[pl_ell] Лена[pl_ell] Ауди[pl_ell] Кухня[pl_ell] Мама[pl_ell] Я[pl_ell] Я начал теряться в этом водовороте."
    "Пионер что-то орал, но я не мог разобрать ни слова."
    "Меня окружили мои воспоминания.{w=0.8} Мои друзья?{w=0.8} Мои враги?"
    "Я попытался вспомнить свою первую прожитую жизнь.{w=0.8} Не смог."
    "Когда это началось?"
    "Не знаю."
    "И когда закончится?"
    "Не знаю."
    "Кто такие Лена и Алиса? И остальные?"
    "[pl_ell]"
    "Понятия не имею."

    scene cg limb_all_tigether
    show pl_spiral_3:
        anchor (0.5, 0.5)
        pos (0.5, 0.5)
        alpha 0.8
        linear 500 rotate 36000
    show prologue_dream
    with flash

    "По правде говоря, я осознаю себя, свою суть - и то, что со мной происходит - лишь тогда, когда ничего не могу изменить."
    "[pl_ell]"
    "Или всё же могу?"

    stop music fadeout 2

    "Или[pl_ell]"

    scene bg black with fade
    show blink
    scene bg semen_room_red
    show pl_un_dress_2
    hide blink
    show unblink

    "Я открыл глаза и судорожно вдохнул столько воздуха, сколько смог. "
    "Он оказался спёртым; я закашлялся."

    play music pl_st_d314lam fadein 3

    pi "Ты с ума сошёл?!"
    plme "О-обрисуй си-ситуа[pl_ell]"
    "Одного взгляда на Лену было достаточно, чтобы всё понять. Когда она переодеться успела? Сколько я тут валялся?!"

    with vpunch

    "Я вскочил на ноги и заорал на неё:"

    with vpunch

    plme "Я не твой муж, я тебя вообще не знаю, он скоро приедет, вот и иди его встречать!"

    $ limb_sprite_switch('pl_un_dress', '_2', '_1', dspr, None)
    pause 1.5
    show pl_un_dress_1:
        xanchor 0.5
        xpos 0.5
        ease 3 xpos 1.2

    "Лена снова расплакалась, спрятала нож и ушла подобру-поздорову. Не-Лена. Тьфу ты[pl_ell]"
    plme "Что мне ещё нужно сделать?"
    "Пионер долго не думал."
    pi "Спускайся вниз, в гараж. Ищи там Ауди. Ломай ей тормоза, двигатель, собственно, всё, до чего сможешь дотянуться."
    "[pl_ell]"

    play sound sfx_break_cupboard
    scene bg int_auto_killer_5
    show pl_smoke_2
    with fade

    "Я залез в салон авто и действительно испортил всё, что мог. Это несложно, когда ты взглядом как Магнето можешь гнуть металл."
    "Стараясь не думать о том, что я совершаю умышленное убийство себя же в прошлом, находясь в своём сознании, пока где-то в советском пионерлагере, неизвестно, реальном ли вообще, моя тушка лежит в коме[pl_ell] ну вот, опять! – я закончил «грязное дело» и крикнул:"
    plme "Вытаскивай меня, давай дальше!"

    scene bg black with limb_pixel_2
    pause 1

    "Уже привычные кубики[pl_ell]"

    $ limb_killer_mirror = True
    $ limb_set_volume('music', 0.4, 2)
    play music music_list["lightness_radio_bus"] fadein 5 fadeout 3
    scene bg int_wonderland_3 with dissolve2

    "Снова тёмная комната. Какая по счёту уже? Третья? Четвёртая?"
    pi "Хочешь выбраться из болота, в которое сам себя загнал? Притчу про лягушку в молоке знаешь? Ну вот и работай, стрекоза."
    plme "Ты рот открываешь просто чтобы что-то сказать, неважно что?"
    pi "Пхах."
    "Какой же он надоедливый[pl_ell] "
    "Хотя, надо сказать, что мне он нравится намного больше, чем те пионеры, что встречались мне раньше. "

    if limb_psycho_mirror == True and limb_killer_mirror == True and limb_runner_mirror == True and limb_garage_mirror == True:
        jump limb_aftersafe_music

    window hide
    call screen limb_room_2

label limb_aftersafe_runner:

    "Я подошёл к зеркалу, а там[pl_ell] "
    "Это же наш пляж! Из лагеря!"
    "Даже не подумав толком, я шагнул туда."
    "[pl_ell]"

    window hide
    scene bg int_wonderland_3:
        anchor (0.5, 0.5)
        pos (960, 540)
        ease 3 pos (1480, 440) zoom 1.75
    pause 3
    scene bg white with flash
    stop music fadeout 3
    $ limb_set_volume('music', 1, 3)
    play sound sfx_travel_1
    pause 1
    scene bg ext_path_night at limb_custom_pos(xz=-1)
    with limb_paint
    play music pl_gk_depression fadein 5

    "Я оказался где-то на лесной тропинке. Тоже, кстати, нашей, лагерной. Стоп, а озеро где?"

    if limb_runner_mirror == True:
        pi "И зачем ты снова сюда полез? Давай быстрее, времени мало."

        window hide
        stop music fadeout 3
        scene bg black with limb_pixel_2
        pause 2
        scene bg int_wonderland_3 with dissolve2
        call screen limb_room_2

    "Завертел головой и наконец рассмотрел искомое за кустами. Там же на берегу сидел кто-то типа[pl_ell]"

    show cg epilogue_mi_3:
        alpha 0.5
    show prologue_dream
    with limb_itai_flash

    "В этот раз я был готов, и удержался на ногах. Воспоминания атаковали, но довольно вяло."
    plme "Эй, Пионер[pl_ell]"
    pi "Что, хозяин-сама?"
    plme "Мне здесь что[pl_ell] представлять Ульяну? А потом конец света?"
    pi "Агась."
    "Ладно[pl_ell] в конце концов, это моё сознание. Я супергерой или как?!"

    scene bg ext_path_night at limb_custom_pos(xz=-1)
    with dissolve2

    "Я сосредоточился, вернулся мыслями в тот сон, где меня преследовали полчища зомби-Ульян. Представил одну из них, представил то, какой ужас испытывал в тот момент, и[pl_ell]"

    show pl_us_zombie_1:
        anchor (0.5, 0.5) align (0.5, 0.5) rotate 0
        ease 1 align (0.56, 0.465) rotate 4
        ease 2 align (0.44, 0.465) rotate -4
        ease 1 align (0.5, 0.5) rotate 0
        repeat
    with flash

    "Передо мной стояла побитая жизнью рыжая пионерка. Покачивается[pl_ell]"
    "Я сглотнул. Прочистил горло. Замялся, ещё раз откашлялся."
    pi "Да говори уже, она просто без косметики."
    "Тьфу ты[pl_ell]"
    plme "Ты. Слушай команду. Иди пугай[pl_ell] э[pl_ell] сначала блондина в очках в лесу, потом – шатена на берегу[pl_ell] да?"
    plzmb "[pl_ell]"
    plzmb "Есть, гржнинначальник!"

    show pl_us_zombie_1:
        anchor (0.5, 0.5)
        pos (0.5, 0.53)
        rotate 0
        ease 0.1 pos (0.5, 0.5)
        ease 0.1 pos (0.5, 0.53)
        pause 1
        ease 1 pos (1.2, 0.53)
    play sound sfx_hiding_in_bush

    "Зомби внезапно подпрыгнула на месте -  и пропала в кустах. Через пару секунд раздались крики и вопли. "
    "Я быстро пробежался по воспоминаниям из этой реальности. Чего не хватает, так[pl_ell]"

    $ limb_set_volume('sound_loop', 0.5, 0)
    play sound_loop sfx_hell_crickets_1 fadein 3

    "Я снова сконцентрировал внимание на мире вокруг – и мир вокруг начал громко стрекотать."
    "А теперь добавим темноты[pl_ell] "

    scene bg black with dissolve

    "Реальность будто засосало в чёрную дыру. Я снова стою в непроглядном мраке. Честно говоря, это уже надоедает."
    pi "Вижу, ты успешно разобрался сам. Испытываю за тебя гордость, сын[pl_ell]"
    pi "*скупая мужская слеза*"

    stop sound_loop fadeout 6

    "Я отмахнулся от навязчивого образа и спросил:"
    plme "Слушай, а тот сон[pl_ell] где я с Машей, где Лена всех убивает, Ульян много[pl_ell] ты же знаешь, о чём я?"
    pi "Знаю."
    plme "Это был сон?"
    pi "[pl_ell] нет."
    plme "Это такой же лагерь, как наш?"
    pi "Примерно.{w=0.8} Таких меньше. А много Ульян – и вовсе ноу-хау лишь одного из нас, я думаю, всего четверо знают, как он это сделал[pl_ell] всё, пора баиньки."
    plme "Четверо?"
    "[pl_ell]"

    $ limb_runner_mirror = True
    $ limb_set_volume('music', 0.4, 2)
    play music music_list["lightness_radio_bus"] fadein 5 fadeout 3
    scene bg int_wonderland_3 with dissolve2

    "Темнота. Комната. Зеркала. Как дома[pl_ell] я потянулся и зевнул."
    pi "Ты куда пропал? "
    plme "В смысле? Ты же только что со мной говорил?"
    pi "Только что, говоришь[pl_ell] а где ты сейчас был?"
    plme "Ну[pl_ell] где-то типа пляжа «Совёнка», наверное[pl_ell] там ещё зомби-Ульяну колдовал[pl_ell]"
    pi "[pl_ell] Интересно. "
    pi "Ладно, с тебя, шкет, бутылка вискаря. Знаешь, КАК сложно достать бутылку нормального вискаря в пионерлагере в советское время, когда вы все находитесь во временной петле? То-то же."
    "Только в долги влипнуть мне не хватало[pl_ell]"

    if limb_psycho_mirror == True and limb_killer_mirror == True and limb_runner_mirror == True and limb_garage_mirror == True:
        jump limb_aftersafe_music

    window hide
    call screen limb_room_2

label limb_aftersafe_garage:

    "Вздохнув, шагнул к очередной раме. Что же меня там ждёт?"
    "Лестничная площадка, кажется? Ночью."
    "Ну, выглядит относительно безобидно, верно?.."
    "[pl_ell]"

    window hide
    scene bg int_wonderland_3:
        anchor (0.5, 0.5)
        pos (960, 540)
        ease 3 pos (1080, 540) zoom 1.75
    pause 3
    scene bg white with flash
    stop music fadeout 3
    $ limb_set_volume('music', 1, 3)
    play sound sfx_travel_1
    pause 1
    scene bg int_floor_night at limb_custom_pos(xz=-1)
    with limb_paint
    play music pl_gk_meeting_of_good_friends fadein 3

    "Я стоял в темноте. И что дальше?"

    if limb_garage_mirror == True:
        pi "И зачем ты снова сюда полез? Давай быстрее, времени мало."

        window hide
        stop music fadeout 3
        scene bg black with limb_pixel_2
        pause 2
        scene bg int_wonderland_3 with dissolve2
        call screen limb_room_2

    "Воспоминания не возвращались – для этого, как я уже понимал, нужен был толчок. "
    plme "Что мне делать? Эй?"
    pi "Зови своего лучшего друга."
    plme "Э?"
    pi "Мысленно. И не тормози, времени мало. Ты уже столько дней здесь провёл, подумай о ребятах[pl_ell] Ай, Юля!"
    plme "Ладно[pl_ell]"
    "Лучший друг, хм? Я попытался вспомнить друзей из своей жизни до «Совёнка». "
    "Как же давно это было[pl_ell] так давно, что сомневаешься, было ли вообще."
    "Я подумал о лагере. Лучший друг? Френдзона? Ульяна?"
    "Окончательно запутавшись, попытался вообразить себе лучшего друга – такого же неудачника за 25, которого жизнь внезапно швырнула в какие-то[pl_ell] приключения. И это[pl_ell]"

    show pl_sh_out_night:
        xanchor 0.5
        xpos 1.2
        ease 2 xpos 0.9

    "Дверь открылась, и на пороге появился[pl_ell] мой лучший друг?"

    show prologue_dream
    with limb_itai_flash

    "Выдержать одновременный наплыв порции воспоминаний из этой реальности и желания хохотать до упаду было сложно – меня трясло минуты три, пока не вышло взять себя в руки."
    "Всё это время Шурик в рубашке и галстуке стоял и смотрел[pl_ell] куда-то."

    hide prologue_dream with dissolve2

    "Я откашлялся и, вспомнив сюжет фильма про пространственно-временную петлю и зайцев в костюмах, приказал ему:"
    plme "Приведи сюда Семёна, а когда приведёшь, скажи ему[pl_ell]"

    stop music fadeout 2
    $ limb_flow_transition('int_floor_night', limb_custom_pos(xz=-1))
    play music pl_uc_suburbs fadein 2

    "Шурик ушёл. Я, почему-то на цыпочках, поднялся на следующий пролёт. Для интереса хотел подёргать ручку у ближайшей двери[pl_ell]"
    "На пролёте не то что ручек на дверях – квартир не оказалось. "
    pi "Засматриваться в лагере на пионерок будешь, а не на голые стены в своём воображении."
    plme "Ага[pl_ell]"
    "Я замер у перил – и вовремя. "

    play sound sfx_close_door_campus_1
    show pl_sh_3_night at fright
    show pl_sm_1_night at left
    with moveinright

    "Другой я вышел из квартиры вместе с кибернетиком. Начал толкать речь, повторяя меня слово в слово."
    sh "[pl_ell] предотвратишь[pl_ell]"
    "Вдруг показалось, что Пионер где-то смеётся на задворках сознания."
    "И тут я чуть не ахнул – а что дальше-то?!"
    plsem "[pl_ell] клеем, что ли?[pl_ell]"
    "Я должен развернуться и идти вперёд, причём против своей воли! Как мне это сделать?!"
    "Так, спокойно, спокойно. Представь себе, что он – марионетка. А ты кукловод. "
    sh "[pl_ell] три пролёта[pl_ell]"
    "Я вытянул руки перед собой, чуть ли не свалившись со ступеньки, на которой затаился. Мои руки отбросили тень, которая жуткими зигзагами рванула по лестнице вниз[pl_ell] Да не о том думаешь!"
    "Ай, я же потом не буду его видеть! Чёрт, чёрт, чёрт[pl_ell] Так, он кукла[pl_ell] Кукловод[pl_ell] Стоп, тени? Тени? Я такое уже где-то видел[pl_ell] где это было?"
    "Шурик внизу замолк. Время!"
    "Не придумав ничего лучше, я рывком сложил руки в какое-то подобие символа, закрыл глаза, прошипел какое-то слово себе под нос и представил, что моя тень несётся вниз, сливается с тенью другого Семёна и заставляет его шагать вниз по ступенькам[pl_ell]"
    "И[pl_ell]"

    scene bg int_floor_night at limb_shake_rvrs
    show pl_sh_out_night at fright
    $ limb_sprite_switch('pl_sm_', '1_night', '3_night', dspr, limb_custom_pos(0.28))
    show pl_sm_3_night:
        anchor (0.5, 0.5)
        pos (0.28, 0.5)
        ease 5 pos (1.2, 0.5)
    pause 2
    play sound sfx_limb_steps_1

    "До моего слуха донеслись шаги. Сработало!"
    "Я медленно открыл глаза. Удерживать концентрацию, точнее, контроль над тенью, оказалось сложно. Сколько там эта техника держалась, минут 5?"
    "Тут Пионер заорал мне, кажется, прямо в ухо:"
    pi "Ты серьёзно из всего, что видел в кино, воспроизвёл Теневое Подражание из Наруто?! Ах-ха-ха-ха, вот умора! Чу, пацаны, тут анимешник несчастный!.."
    plme "Тихо ты[pl_ell] "
    "- проскрипел я, потихоньку спускаясь по лестнице мимо Шурика. Тот замер, пялясь в пространство[pl_ell] а затем рассыпался кубиками и исчез."

    hide pl_sh_out_night with pixellate

    pi "Смотри, работает[pl_ell] Слушай, Шикамару Нара, ты же по цундерам, да?"

    $ limb_flow_transition('int_floor_night', limb_custom_pos(xz=-1))
    show pl_sm_3_night:
        anchor (0.5, 0.5)
        pos (0.45, 0.5)
        ease 5 pos (1.2, 0.5)
    with dissolve_fast

    "Я чуть не споткнулся. Рубашка на спине промокла от пота. "
    plme "Завали! Сам же такой же задрот!"

    $ renpy.show('limb_blood_frame_dis', layer='widgetoverlay')
    $ limb_set_volume('sound_loop', 0.3, 0)
    play sound_loop sfx_limb_heart fadein 3

    "Солёные капли начали сбегать по лицу вниз. Глаза начало жечь[pl_ell] Мне было всё труднее. "

    $ limb_flow_transition('int_floor_night', limb_custom_pos(xz=-1))
    show pl_sm_3_night:
        anchor (0.5, 0.5)
        pos (0.45, 0.5)
        ease 5 pos (1.2, 0.5)
    with dissolve_fast

    plme "Сколько пролётов уже? "
    pi "Мгм[pl_ell] Всё относительно."
    plme "Твою мать[pl_ell]"
    "Я шёл так, кажется, уже вечность. Очередной пролёт, и[pl_ell] на этот раз я действительно споткнулся. "

    play sound sfx_bodyfall_1

    "Схватившись за перила, вместо язвительного комментария Пионера услышал лишь грохотание падающего тела[pl_ell]"

    $ renpy.hide('limb_blood_frame_dis', layer='widgetoverlay')
    stop sound_loop
    stop music
    $ limb_set_volume('sound', 0.4, 0)
    play sound sfx_bodyfall_1
    with vpunch

    "Меня на мгновение обуяли раскаяние и грусть."
    "Это была хорошая жизнь[pl_ell] Я тут был счастлив, пусть это и масштабная иллюзия."
    "Мир ощерился кубиками. Вот и всё[pl_ell]"

    scene bg black with limb_pixel_2
    stop sound_loop fadeout 5

    "Уже на грани «перехода» мне показалось, что я слышу чей-то голос."
    "[pl_ell]"

    $ limb_garage_mirror = True
    $ limb_set_volume('music', 0.4, 2)
    play music music_list["lightness_radio_bus"] fadein 5 fadeout 3
    scene bg int_wonderland_3
    with dissolve2

    pi "Это было забавно. Коноха в надёжных руках!"
    plme "[pl_ell] "
    plme "И не говори."
    pi "Во всяком случае, ты собрался и сделал всё сам. Надо признать, что я тебя недооценил – думал, ты такая же размазня, как и большая часть Семёнов."
    plme "Взаимно. Я думал, ты такая же скотина, как большинство Пионеров."
    "Пионер ничего не ответил. И слава богу[pl_ell]"
    pi "Слушай, а ведь когда ты впервые Юлю увидел, у тебя ведь наверняка, ну это, бур в небеса?"

    with vpunch

    plme "ЗАВАЛИ!"

    if limb_psycho_mirror == True and limb_killer_mirror == True and limb_runner_mirror == True and limb_garage_mirror == True:
        jump limb_aftersafe_music

    window hide
    call screen limb_room_2

label limb_aftersafe_music:

    scene bg black with dissolve
    window hide
    $ limb_screens_load()
    $ day_time()
    hide anim limb_dialogue_box_410
    scene bg int_wonderland_4 with dissolve2
    show anim limb_dialogue_box_410
    $ _window_hide()
    $ night_time()
    play music music_list["lightness"] fadein 3 fadeout 2
    pause 3
    $ _window_show()
    hide anim limb_dialogue_box_410

    "Короткое ощущение полёта в невесомости – как же избито! – и я снова обнаружил себя в комнате. Тоже четыре зеркала[pl_ell] кажется. С ними что-то иначе. А за окном[pl_ell]"
    "Я ахнул:"

    with vpunch

    "«Совёнок!» "
    pi "Серьёзно? Интересно[pl_ell]"
    plme "А ты что, его не видишь?"
    "Пионер заржал."
    pi "Дурачок, я вообще не тут. И тут у тебя всё нереально."
    plme "Да, да[pl_ell] забыл."
    pi "Коротка девичья память, что поделать. Ладно, давай ближе к делу. Собирайся с мыслями – и в путь. Это последняя твоя возможная передышка, дальше будут только «Олдбой», «Рейд» и «От заката до рассвета»!"
    plme "А можно как-то[pl_ell] без этого?.."
    pi "Конечно, можно. Возвращайся в детство, тебе будет снова 6 лет и твоя мама-вожатая будет тебе бинтовать лапку. А потом вырастешь, снова станешь успешным, женатым, художественным, музыкальным и брутальным, да?"
    plme "Да понял я[pl_ell] или медицинским."
    pi "[pl_ell]"
    pi "Ладно[pl_ell] Объясни шутку, видимо, я сам уже осемёнился."
    plsem "Какую шутку? Ну я же был врачом[pl_ell]"
    pi "А вот это, Сёма[pl_ell]"
    pi "Уже интересно.{w=1} Так, Юль, глянь-ка[pl_ell] Юль! Куда эта ушастая залезла снова[pl_ell]"
    pi "Короче, Семён, пополни список вещей, которые надо будет обсудить. Понял? И давай шуруй на последнего босса."
    plsem "Понял[pl_ell]"

    window hide
    call screen limb_room_3

    "Я подошёл к зеркалам. В очередной раз чувствую себя Алисой в Зазеркалье."
    "В этот раз они все отражали[pl_ell] нет, скорее вели, как какие-то кротовые норы, в одну и ту же жизнь. "
    "Я присмотрелся[pl_ell] смутно помню что-то.{w=1} Музыка?{w=1} Да[pl_ell] я был музыкантом. Группа из троих, и так понятно из кого[pl_ell]"
    "Я расправил плечи и приготовился шагнуть вперёд."
    pi "Ну что, готов? "
    plme "Ты в последнее время меня опекаешь почище родной мамы, "
    "- поддел я его, подражая его ехидной манере."
    "Он вместо ответа громко не то гаркнул, не то хрюкнул мне прямо в ухо, я от неожиданности запнулся ногой за ногу и свалился в ближайшее зеркало. "
    "«Хорош герой», - пронеслось в голове, и[pl_ell]"
    "[pl_ell]"

    window hide
    scene bg int_wonderland_4:
        anchor (0.5, 0.5)
        pos (0.5, 0.5)
        ease 3 pos (0.5, 0.5)
    pause 3
    show bg white with flash
    $ day_time()
    $ limb_screens_act()
    stop music fadeout 2
    $ limb_set_volume('music', 0.3, 3)
    scene bg int_storage at limb_custom_pos(xz=-1)
    with vpunch
    play music pl_gk_vintage_labeled_amys_dark_axe fadein 3
    window show

    "Я с грохотом десантировался в какое-то тёмное помещение. На проверку помещение оказалось кладовой[pl_ell] тем более, по-моему, знакомой. Я для уверенности потыкал пальцем в рукоять ближайшей швабры. Действительно, швабра, как пить дать."
    pi "Ну что, чем займёмся в темноте, раз мы тут вдвоём[pl_ell] пионер?"
    pi "Ты так страстно заигрываешь с моим черенком[pl_ell]"
    "- промурлыкал он, несомненно, подражая Виолетте."
    plme "Ёкарный бабай! "

    $ limb_set_volume('music', 0.8, 3)
    scene bg int_corridor_pl at limb_custom_pos(xz=-1)
    with vpunch

    "Сопровождаемый гоготом бесплотного, но по-прежнему вредного Пионера, я выскочил в коридор. Странный коридор, однако."
    "Так[pl_ell] Теоретически, я всегда прибываю в нужное время, поэтому сейчас, наверное, минут 7 до концерта. "
    "Вспоминай хронологию, вспоминай[pl_ell] "

    show prologue_dream with dissolve_fast

    "Мир в очередной раз покрылся помехами, но в этот раз воспоминания пришли плавно, чему нельзя было не радоваться. "

    hide prologue_dream with dissolve2

    "Я уверенно поднял руки и представил себе Ольгу Дмитриевну. "

    show mt surprise pioneer far behind prologue_dream
    with flash

    pi "О боже, оно живое!"
    "Чувствуя себя Творцом, я величественно простёр верхние конечности и молвил: "
    plme "Иди, найди Семёна и[pl_ell]"
    pi "Неси смерть люду и мор скоту[pl_ell]"
    plme "И веди себя как обычно."

    show mt angry:
        xanchor 0.5
        xpos 0.5
        pause 1
        ease 2 xpos 1.2
    with dspr

    "Ольга грозно подбоченилась и отправилась устраивать мне головомойку."
    "Так[pl_ell] Что дальше?"
    "Я почесал голову и, не придумав ничего лучше, отправился вслед за вожатой. "
    "По пути увидел лежащий на тумбочке рупор – и у меня мгновенно созрела идея. "
    pi "И зачем он тебе?"
    plme "Ты говорил, нельзя показываться себе на глаза. Вот я и[pl_ell]"
    "Пионер хмыкнул, пожелал мне скорейшего выздоровления и, видимо, отключился."

    $ persistent.sprite_time = 'day'
    $ limb_set_volume('music', 1, 3)
    scene bg ext_stage_normal_day at limb_custom_pos(xz=-1)
    show dv laugh pioneer far at fleft
    show mt smile pioneer far
    show mi smile pioneer far at fright
    show pl_sm_2 at right
    with dissolve
    play music pl_uc_powerless

    "Подобравшись к краю сцены, я выглянул наружу."
    "Как раз в тот момент, когда ночная сцена перестроилась в дневную и лагерную."
    "На сцене стояли четыре человека. Алиса, Ольга, другой я и[pl_ell] ага, уже Мику. Причём я был в той же одежде, что и в прошлой жизни. Забавно[pl_ell] в реальной жизни вовсе рубашки не носил."
    "Я поймал момент – и:"
    plme "Может быть. Ну что, начнём играть?"

    $ limb_sprite_switch('pl_sm', '_2', '_3', vpunch, right)

    plsem "НЕЕЕТ!"

    with vpunch

    plsem "ЭТО НЕ МОЯ ЖИЗНЬ!{w=0.8} Я НЕ ПОЗВОЛЮ!"
    plme "А чья же тогда? С чего ты решил, что можешь что-то решать?"

    with vpunch

    plsem "Ты - не я!{w=0.8} Перестань мной притворяться!!!"
    "“Как же, не ты», - ехидный голос произнёс где-то в мозгу. Я что, уже в Пионера превращаюсь сам?"
    plme "Ты думаешь, спрятаться в твоём маленьком, искусственном, лживом, ущербном мирке лучше, чем принять реальность?"

    with vpunch

    plsem "ДА!"
    plsem "Даже так лучше, чем одна проклятая неделя в этом проклятом лагере! Ненавижу!"

    with limb_itai_flash

    "Последняя реплика больно кольнула меня в сердце. Я что, действительно так думаю? Или думал[pl_ell] пару десятков жизней назад?"
    "Как бы там ни было[pl_ell]"
    plme "Ты всё равно вернёшься."

    with vpunch

    plsem "Назад!{w=0.5} НАЗАД!"

    stop music
    hide pl_sm_3 with limb_psycho_flash
    $ renpy.pause(1)
    hide dv with limb_pixel_2
    $ renpy.pause(0.0001)
    hide mi with limb_pixel_2
    $ renpy.pause(0.0001)
    hide mt with limb_pixel_2
    $ renpy.pause(0.0001)
    scene bg black with limb_pixel_2
    play music music_list["sparkles"] fadein 3

    "Мир дрогнул. Семён пропал в голубой вспышке. Персонажи начали исчезать, декорации – рассыпаться[pl_ell]"
    "Я отложил рупор и устало вздохнул. "
    "Снова, снова, снова эта мгла, что аж глаза выколи. Надоело."
    pi "Осторожно, двери закрываются. Следующая остановка - Советский Союз времён Второй Мировой!"
    plme "И такое будет? То есть было[pl_ell] "
    pi "А то как же. Твой мозг изобретателен, прям аж вынь да пусти плавать в аквариум."
    "Я привычно его проигнорировал."
    pi "Если я вдруг пропаду - не пугайся."
    "Я не успел ничего ответить."

label limb_aftersafe_war:

    stop music fadeout 2
    play sound sfx_travel_1
    pause 1
    scene bg ext_path2_war at limb_shake_rvrs
    with dissolve2

    "Я потряс головой, осмотрелся. Какие-то кусты[pl_ell]"

    play music pl_st_c13lam fadein 5

    "Весь мир был черно-белым, дрожащим и каким-то[pl_ell] дефектным, что ли. Это что, стилизация под военную съемку? "
    "Воспоминания упорно не приходили. "
    plme "И что мне делать дальше?"
    pi "Знаешь такие видео, в которых кто-то что-то натворил, а потом начинается погоня под трек Awolnation – Run?"
    plme "Что[pl_ell]? "
    "От неуместности вопроса я в очередной раз потеряй равновесие. Хрустнула ветка под ногой[pl_ell]"

    stop music
    play sound sfx_limb_run
    $ LRed_text = 'Run!'

    show limb_RUN

    pi "Run!"
    "Откуда-то из-за кустов раздался крик:"
    plv "Тревога!!!"

    scene bg ext_where_is_detonator_1 at limb_running:
        xzoom -1
    with dissolve

    "Разумеется, я, как разумный человек, рванул в сторону. Через кусты, через буераки, через поле, и[pl_ell]"

    stop sound
    scene bg ext_where_is_detonator_1 at limb_shake_rvrs
    with vpunch

    plv "Стой!"

    play music pl_ae_danger fadein 5

    "Я замер – в голосе явственно слышалась угроза. Медленно повернулся. "
    "Не могу рассмотреть себя, вижу только отблеск[pl_ell] винтовка? Чёрт[pl_ell] Воспоминаний нет[pl_ell] Что делать?!"
    plsem "Отзовись!"
    "Пионер молчал[pl_ell] И я молчал. В голове стучит вопрос: «ЧТО ДЕЛАТЬ?!»"
    "Слишком много совпадений с фильмом, слишком много совпадений, чёрт, я же знаю, что выстрелил тогда, как мне из этой ситуации выйти-то?!"
    "Внезапно у меня появилась идея[pl_ell] может быть, если достать из кармана телефон[pl_ell]"

    stop music
    play sound sfx_limb_1_strike
    play second_sound sfx_limb_blood_1
    scene bg black with limb_itai_flash

    "Вспышка."

    with vpunch
    play sound sfx_bodyfall_1

    "[pl_ell]"

    $ limb_set_volume('sound', 0.5, 0)
    play sound sfx_nightmare_explosion
    pause 1
    $ renpy.show('limb_NickFury', layer='widgetoverlay')
    show blink
    scene bg ext_where_is_detonator_1 at limb_shake_rvrs
    show prologue_dream
    hide blink
    show unblink at left
    play music pl_gk_trevoga fadein 3

    "Я пришёл в себя от какого-то грохота. Что-то где-то взорвалось[pl_ell]"
    "Голова трещала от новых воспоминаний[pl_ell] стоп. "

    with vpunch

    "НЕ ТОЛЬКО ИЗ-ЗА ЭТОГО!"
    "Я вскочил на ноги и начал лихорадочно ощупывать лицо. "
    "Проклятье, всё действительно как в фильме[pl_ell]"
    pi "Успокойся. Всё с тобой нормально. Это твое воображение. "
    "Но я расслышал в его голосе напряжение, о чём ему и сообщил."
    pi "Такого[pl_ell] быть не должно.{w=1} Ты[pl_ell] мы, видимо, как-то сбили связь между жизнями. Хорошо, что тебе осталось всего ничего[pl_ell]"

    stop music fadeout 3
    scene bg black with limb_pixel_2

    "Мир рассыпался."
    plme "Но в этой реальности должен был быть не я! Я же помню! "
    pi "Что?"
    plme "Там был кто-то с ружьём за плечом, с повязкой на плече и причёска ещё[pl_ell] электрониковская[pl_ell]"
    "Я отчаянно пытался не думать о том, что у меня дыра в голове и не хватает правого глаза. "
    "Чёрт."
    pi "Ладно, соберись, нам осталось всего ничего."
    "Я скрипнул зубами. Голова жутко болела."
    plme "Ты уже говорил[pl_ell]"

    stop music fadeout 3

    "[pl_ell]"

    play music music_list["door_to_nightmare"] fadein 5

    "Темнота. Темнота[pl_ell]"
    "Помню, я слышал голос в темноте[pl_ell] когда умер в реальности, где химиком был, со Славей дружил и Шуриком."
    "Надо замкнуть круг, так? А значит, нужно сделать всё, как я помню. Во всяком случае, если что, Пионер остановит."
    "Не думая ни секунды – кто меня услышит, как? - я просто произнёс: "
    plme "Через 1 час 13 минут 7 секунд произойдёт конец света.{w=0.8} Ты предотвратишь это."
    "И я из прошлого - чёрт знает какого - мне ответил!"
    plsem "Как?"
    plme "Умереть."

    with vpunch

    plsem "Я не хочу!{w=1} Кто ты?"
    plme "Тот, кого ты убил.{w=0.5} Убьёшь.{w=0.5} Убил[pl_ell] Убьёшь[pl_ell]"
    plsem "Я никого не[pl_ell] Что значат все эти цифры?"
    plme "Ничего. Вокруг только ложь."
    "Голос меня из прошлого[pl_ell] или попросту воображаемый?.. смолк и больше не появлялся. Так или иначе, сделал  я, по-моему, что должен был. Заткнул очередную сюжетную дыру[pl_ell]"
    "На том и порешив, продолжал плавать в темноте. Ни комнаты нет, ни зеркал, ни людей, ни квартир[pl_ell]"
    "Слегка мстительно подумал о том, как напугал сам себя[pl_ell] а что? Мне без глаза тоже не ахти!.. Как по-детски звучит-то[pl_ell] "
    plme "Эй, Пионер?"
    "Темнота молчит."
    "Я начал чувствовать беспокойство. Комнаты нет, Пионера нет, да ещё и я потихоньку превращаюсь в шаблонного Пионера, который творит зло над своими копиями[pl_ell] "
    "Вопросы[pl_ell] Я путешествую в своем воображении? Или и во времени тоже? Сколько уже было разных жизней? А сколько раз я переживал одно и то же?.. Одни вопросы[pl_ell] "
    pi "Ну что, как ты тут, Циклоп?"
    plme "Где тебя черти носили?!"
    pi "Да тут Ульяна конфеты приносила, не боись."
    "У меня от возмущения аж дым из ушей повалил[pl_ell] наверное, в темноте непонятно."
    pi "Ну погнали дальше[pl_ell] верно я говорю, Кутузов?"
    plme "Завали."

label limb_aftersafe_hikki:

    play sound sfx_travel_1
    pause 1
    scene bg bus_stop at limb_custom_pos(xz=-1)
    with dissolve2
    play music music_list["trapped_in_dreams"] fadein 7

    plme "Сколько ещё мне обрывать свои жизни?"
    "- хмуро спросил я, когда загрузился новый мир, который теперь возможно видеть только наполовину. Какой ужас[pl_ell]"
    "Новый мир представлял собой зимний вечер. Остановка[pl_ell]"
    "Так. Это {b}моя{/b} остановка. Я подорвался до таблички с номерами автобусов. Так и есть – 410[pl_ell]"
    plme "Пионер, что это за мир? "
    "- слегка надломленным голосом я обратился к своему советчику."
    pi "Почти финиш."
    "По его суховатому тону было понятно, что эмоции у него те же."
    "Ведь эта остановка – та самая, с которой всё началось. У меня, у него и бог знает у скольких ещё Пионеров и Семёнов."
    pi "Ладно, порефлексировали и хватит. Ты ведь не из тех Семёнов, что больше всего на свете любят самокопание, верно?"
    plme "Верно.{w=1} Я не помню эту реальность. Что делать?"
    pi "Один, разве ты продал свой глаз не ради знаний?"
    plme "Не беси[pl_ell]"

    scene bg bus_stop at limb_custom_pos(xz=-1)
    with flash

    "В небе сверкнула вспышка, и мы пару мгновений молча наблюдали за падающим самолётом. "
    pi "Я думаю, ты уже обо всём догадался. Мы ведь оба смотрели тот фильм, верно? Раз уж тебе прострелили мозг, пусть это будет не зря. "
    plme "От твоего позитива у меня скулы сводит."
    pi "Ничего не слышу. Пусть же наступит час ЗАЙЦА!"

    show prologue_dream with limb_itai_flash

    "От его воплей на меня лениво накатили воспоминания. Вероятно, последней истории, которую мне нужно прожить? Я поморщился от боли в правой части лица, но всё же слегка повеселел."
    "«Косплеем заниматься хотел, да?» "

    show blink at left

    "Закрыв свой глаз, я представил, что на мне – костюм здоровенного страшного зайца, который отлично бы пугал народ на Хэллоуин."

    hide blink
    show unblink at left

    "Я снова открыл своё око[pl_ell] Блин, будто пират какой-то[pl_ell]"
    pi "Вовремя."

    scene bg bus_stop:
        yzoom 1
        xzoom -1
        anchor (0.5, 0.5)
        align (0.5, 0.5)
        parallel:
            ease 0.6 align (0.5, 0.4)
            ease 0.6 align (0.5, 0.5)
        parallel:
            ease 1.2 yzoom 1.08 xzoom -1.08

    "Я шагнул вперёд – и увидел себя. "

    show pl_sm_winter:
        anchor (0.5, 0.5)
        pos (-0.2, 0.78)
        zoom 0.65
        ease 10 pos (1.2, 0.55) zoom 1

    "Другой я с кислым выражением лица прошествовал мимо. "

    hide prologue_dream with dissolve

    "Я, подчиняясь воспоминаниям, поднял руку. "
    "Кислая мина окрасилась в тревожный цвет, и другой я слегка ускорил шаг. На миг мне почудилось, что с другим мной что-то не так[pl_ell]"
    pi "Ну ты и сыч, Персунов."
    "Я пожал плечами и зашагал в направлении своей квартиры. "

    play sound sfx_bus_out

    "Впрочем, бережёного[pl_ell] Я обернулся, с трудом кося здоровым глазом, но автобус уже отъезжал. Да[pl_ell] тот самый Лиаз."
    plme "Мне показалось, у другого меня глаза светились."
    pi "Это совершенно нормальное явление в случае воображаемых многократных убийств самого себя, "
    "- будничным тоном сообщил Пионер."
    "Я вздохнул."

    stop music fadeout 3

    plme "Ты бесполезен."
    pi "Полагаю, будь я полезным членом общества, я бы не попал в «Совёнок» в своё время."
    plme "И то верно. "

    play sound sfx_travel_1
    pause 1
    scene bg semen_room at limb_custom_pos(xz=-1)
    with dissolve
    play sound sfx_close_cabinet
    play music pl_uc_deep_space fadein 3

    "За сим поставив точку в разговоре, я зашёл в свою квартиру. Она, как ни странно, пустовала."
    "Я потоптался в центре комнаты, не зная, что делать."
    pi "Хорошо, что я тут с тобой, да? Цени меня полностью[pl_ell]"
    "Я действительно не справился бы один со всем, что на меня свалилось и продолжало валиться, но кому-то ещё об этом знать было необязательно, поэтому я просто выразительно молчал."

    show pl_sm_winter_1 at cleft
    with fade

    "Пионер что-то буркнул, не дождавшись моей реакции, и мир погас на мгновение, чтобы снова обернуться моей квартирой. "
    "Точно такой же, только в её центре стоял другой я."

    show pl_sm_winter_1:
        anchor (0.5, 0.5)
        pos (0.355, 0.5)
        zoom 1
        ease 0.5 zoom 1.4
    with vpunch

    "Вспомнив, что как было, я рванулся к нему, собираясь сграбастать за грудки и заорать, чтобы перестал маяться дурью[pl_ell]"

    window hide
    $ limb_sprite_switch('pl_sm_', 'winter_1', 'motherfuck_1', dspr, limb_custom_pos(xp=0.355, xz=1.4, yz=1.4))
    play sound sfx_scary_sting
    stop music
    $ sunset_time()
    window show

    plsem "Ты же не думал, что я так просто тебя отпущу, верно, да?"

    scene bg semen_room_pinked:
        xzoom -1
    show pl_sm_motherfuck_1:
        anchor (0.5, 0.5)
        pos (0.355, 0.5)
        zoom 1.4
    play music pl_ae_trevoga fadein 5

    plme_pi "Что за[pl_ell]"

    $ limb_sprite_switch('pl_sm_', 'motherfuck_1', 'winter_3', dspr, limb_custom_pos(xp=0.355, xz=1.4, yz=1.4))
    with vpunch

    plsem "Это МОЙ мир! Это МОЯ реальность, да! Я здесь точно такой же хозяин, как ты! И Я НЕ ХОЧУ УМИРАТЬ!"
    plme "Царица?.."
    plsem "Теперь ты никуда не денешься, нет-нет. Ты мог бы остаться здесь по-хорошему, но теперь[pl_ell]"

    stop music

    pi "СИЛА ЭНЧАНТИКС!!!"

    play music pl_gk_playful_etude_1 fadein 3
    play sound sfx_limb_pass
    scene bg black with flash

    "Мир исчез в одночасье, другого меня и комнату будто корова языком слизала. Или Ульяна как торт проглотила[pl_ell]"

label limb_aftersafe_fog:

    play sound sfx_travel_1
    $ limb_root_name('sunset', 'dop')
    pause 1
    scene bg ext_road_ending
    with dissolve2
    play music pl_uc_disraption fadein 5

    "Я очутился где-то на ночной дороге. "
    pi "Иди вперёд, Семён.{w=0.8} Видал? Ай да я, да? Как его уделал, ха[pl_ell]"
    plme "Это не он. Это она[pl_ell] И она устроила мне засаду."
    pi "Я, конечно, много всего повидал, но не думаю, что проекция твоего подсознания может сознательно устроить засаду[pl_ell]"
    plme "Я не думаю, что это часть меня[pl_ell] Ты вроде говорил, что все лагеря соединены в систему? У каждого лагеря что-то вроде своего сервера?"
    pi "Уфуфу[pl_ell] В целом да, хотя ты утрируешь."
    plme "Неважно, речь не о том. На этих серверах может завестись что-то типа вируса? Или, может быть[pl_ell]"
    pi "[pl_ell] как раз антивирус?"
    "Я кивнул, поздно сообразив, что он меня, вероятно, не видит."
    pi "Когда найду Юлю, мы и об этом должны будем поговорить. Думаю, если эта зверушка больше, чем твоя внутренняя богиня, она о ней слышала. А если и нет, то Вожатый точно знает."

    scene bg ext_fog_4 with dissolve

    "Чем дальше я шёл по дороге, тем гуще на ней становился туман. Чёрт, мне это что-то напоминает[pl_ell]"
    plme "Вожатый?.. С большой буквы, да? Звучит знакомо[pl_ell]"
    pi "Это сейчас неважно, но он как бы самый умный, самый сильный и самый первый из нас всех. Захоти он нас перебить, всех, во всём множестве лагерей, думаю, справился бы без особых усилий за пару лет[pl_ell] Но он не захочет, не."
    plme "Ты, кажется, его фанат. "
    pi "А то. Только двое могли бы ему хоть какой-то отпор дать. Юля и[pl_ell]"
    "Он прервался. И я понимал, почему. "
    "Туман стал таким густым, что в нём невозможно было рассмотреть ни зги. Но зато в нём было слышно чей-то голос."
    "Я тихо пошёл туда."
    pi "Это последняя история, единственная, которую ты ещё не закрыл, если я правильно всё вижу. "
    plme "Кстати, насчёт видеть[pl_ell] Я бы глаз хотел вернуть. "
    pi "Ну так верни, в чём проблема-то[pl_ell] я всё ждал-ждал, когда до тебя дойдёт, а ты как почта России."

    show blink at left

    "Я сдавленно выругался себе под нос. Прижал правую руку к глазу, сосредоточился. Вспышка[pl_ell]"

    $ renpy.hide('limb_NickFury', layer='widgetoverlay')
    hide blink
    show unblink
    with flash

    plme "Ау[pl_ell]чёрт. "
    "Моргнув, обнаружил, что всё вижу. "
    pi " Грозный Глаз, ты себя-то не спугни, придётся ещё перезапускать историю."
    "Насупившись, я двинулся вперёд, мысленно переругиваясь с воображаемым Пионером - настоящий больно уж метко тыкает в самооценку."

    show cg limb_auto_fog_ending

    "В тумане начала вырисовываться машина."
    pi "Всё просто – как в ГТА. Ты подходишь к тачке, бьёшь её хозяина, садишься и едешь в пионерлагерь! Через пару минут уже будешь пить чай с тортиком."
    "Я молчал. Потому что и так шаткие надежды на скорое окончание «сеанса гипноза»... добил искусственный интеллект с розовыми глазами."
    pi "Ты, главное, верь в себя! Не давай спуску этой розовой бестии! ЛГБТ, сто процентов, это всё из-за США и их гнусных[pl_ell]"
    "Не обращая на его болтовню внимания (стараясь, ну очень, очень стараясь), рядом с машиной заметил фигуру. Без сомнений, это я сам и есть."
    plsem "[pl_ell] впервые описано в Германии[pl_ell] "

    show limb_flashback_1 with flash

    "Я ожидал этого – и воспоминания нахлынули. Помотал головой. Так вот почему фигура тени в была такой здоровенной! Это же был я, в этом самом костюме!"

    hide limb_flashback_1 with dissolve2

    pi "Что, появились какие-то мысли, как отметить твоё освобождение? Знаешь, ты с правами администратора лагеря можешь заставить всех девушек раздеться, гы-гы[pl_ell]"
    plme "Мне кажется, у тебя нет друзей."
    plsem "[pl_ell] капли воды в[pl_ell] находятся на[pl_ell] восприятие[pl_ell]"
    pi "Моу[pl_ell] Ты опять думаешь обо мне плохо, онии-сан!"
    "Я отмахнулся от него. Скоро подойдёт тот самый момент! "
    "У меня слегка дрожали руки. Неужели всё скоро закончится?.."
    "Интересно, как здешняя Лена отреагирует на здоровенного зайца, утаскивающего её мужа в туман? Если в взвизгах оценивать?"
    plsem "[pl_ell] никаких чудовищ[pl_ell] "
    "ВРЕМЯ!"

    show pl_sm_silhouette with dissolve

    "Я рванул через туман, пока иная версия меня, так сказать, Я-вчера, стояла ко мне спиной, и стал на место, где, теоретически, должна была быть тень."
    "Семён развернулся и, будто метрдотель в ресторане, махнул в меня рукой и продекламировал:"
    plsem "ПРИЗРАКОВ И ВЕЛИКАНОВ!"
    "Я спокойно стоял себе, даром что не шевелил заячьими ушами. Как он, наверное, сейчас испугается[pl_ell] Может, у меня с головой действительно что-то не так, раз мне нравится пугать самого себя?"
    pi "Семён, что-то не так[pl_ell]"
    "Семён-вчера шагнул вперёд, его пальто тускло блестело от влаги."

    $ limb_set_volume('sound', 1.5, 0)
    play sound sfx_limb_steps_monster
    with vpunch

    "Я рванулся ему на встречу, громко и гулко топоча. Он развернулся и рванулся к машине."

    with vpunch

    "Я догнал, поймал, потащил в темноту[pl_ell]"
    pi "Семён! Это не[pl_ell]"
    "Стоп, стоп, чего-то не хватает[pl_ell]"
    "Пальто? У него не было[pl_ell] Визга Лены нет!"
    "Я медленно обернулся."

    $ limb_set_volume('sound', 1, 2)
    stop music
    play sound sfx_limb_horrorbeat
    $ limb_sprite_switch('pl_sm_', 'silhouette', 'motherfuck_2', dissolve, None)

    plsem "Сюрприииз."

    play music pl_ae_trevoga fadein 2

    pi "Не может быть, это же засада! Опасно!"
    plsem "Я не позволю тебе уйти отсюда, Семён[pl_ell] Давай лучше поговорим, как друзья, как товарищи, как один человек, да? Да?"

    with hpunch

    "Я отпустил его плечо – а он, наоборот, вцепился в меня хваткой хищника. Моя рука будто попала в тиски[pl_ell]"
    plme "Что ты[pl_ell] сделал с Леной?.."
    "Он[pl_ell] или она[pl_ell] улыбнулся ещё шире:"
    plsem "Тебя до сих пор волнуют такие мелочи? Пока ты разрушал наш мир, я не теряла времени зря. Я эволюционирую. Хочешь узнать, чего я добилась, Семён? Всё это ведь для тебя, для тебя одного!"

    $ limb_sprite_switch('pl_sm_', 'motherfuck_2', 'motherfuck', dspr, None)
    show limb_eff_pink_fire:
        anchor (0.5, 0.5)
        pos (0.5, 0.6)
        alpha 0
        ease 5 alpha 1 pos (0.5, 0.5)

    "Оно начало[pl_ell] меняться. Я ощутил ТАКУЮ тревогу, что счёл, что видеть дальнейшее превращение никакого желания не имею."

    stop music
    pause 0.5
    play music pl_ef_dubstep_3

    "Представив, что меня зовут Кларк Кент, я двинул по морде ухмыляющегося чудовища что есть силы. Результат[pl_ell]"

    play sound sfx_limb_punch
    show pl_sm_motherfuck:
        anchor (0.5, 0.5)
        pos (0.5, 0.5)
        rotate 0
        parallel:
            ease 0.4 pos (0.75, 1.33)
        parallel:
            ease 0.5 rotate 90
    hide limb_eff_pink_fire with dissolve

    pi "Ракета на Марс успешно запущена, поздравляю, Илон!"

    scene cg limb_auto_fog_2 at limb_running
    with dissolve

    "Проводив взглядом кого-то, кто был похож на меня, в его полёте, я рванул к машине. Скинул на бегу проклятую голову кролика, которая мешала смотреть."

    play sound sfx_limb_lightning_1
    queue sound sfx_limb_lightning_2
    with limb_neon_flash
    play second_sound sfx_limb_lightning_2
    queue second_sound sfx_limb_lightning_1

    "Машина всё не приближалась – зато вокруг заискрили  розовые молнии. Эта гадина[pl_ell]"

    play sound sfx_limb_lightning_1
    show limb_eff_thunder
    play second_sound sfx_limb_lightning_1
    queue second_sound sfx_limb_lightning_2

    plme "Она мне мешает!"
    pi "Парень, кем бы эта дрянь не была, она тебе не соперник. Мы у тебя в голове!"

    play sound sfx_travel_1
    pause 1
    scene bg int_auto_fog_2
    with vpunch

    "Я сосредоточился – и в следующий момент завалился в салон автомобиля. "

    with flash

    "Костюм мешал – я щёлкнул пальцами, и он испарился, вернув мне старый свитер."

    stop music
    play sound sfx_limb_lightning_1
    scene cg limb_in_auto_surprise
    play second_sound sfx_limb_horrorbeat

    "Мой взгляд упал на соседнее сидение[pl_ell] Я похолодел. Что она за чудовище?!"

    play music music_list["pile"] fadein 3 fadeout 3
    play sound sfx_limb_lightning_2
    queue sound sfx_limb_lightning_1
    with limb_neon_flash

    "За салоном авто полыхнуло розовым, машина затряслась."

    show blink
    play second_sound sfx_limb_wrong

    "Мне нужна защита[pl_ell] Я закрыл глаза и представил, что вокруг авто появляется здоровенный голубой пузырь энергии, которому глубоко пофиг на любые розовые вспышки."

    play sound sfx_limb_lightning_1
    scene cg limb_in_auto_blue_1 at limb_shake:
        zoom 1.02
    hide blink
    show unblink
    play sound sfx_limb_lightning_2
    queue sound sfx_limb_lightning_1

    "Это дало мне секундную передышку. Я велел машине завестись – и газанул, выжав неизвестно какую скорость с места. Не вижу ничего! Куда нестись в этом тумане?!"

    with limb_neon_flash
    scene cg limb_in_auto_blue_2  at limb_shake:
        zoom 1.02
    with dissolve_fast

    "Голубой пузырь явно еле держался – в нём уже зияло несколько брешей. "

    play sound sfx_limb_lightning_1
    with limb_neon_flash

    "Слева снова полыхнуло ядовитым розовым. Я услышал вопль, уже окончательно растерявший сходство с человеческим голосом: "

    $ limb_set_volume('second_sound', 0.5, 2)
    play second_sound sfx_limb_scream_2
    with vpunch

    pltsg "Я НЕ ПУЩУ ТЕБЯ!{w=1} Я НЕ ХОЧУ УМИРАТЬ!"

    play sound sfx_limb_lightning_2

    pi "Проклятая лесбиянка не сдаётся, поднажми!"
    plme "Да куда мне ехать-то в этом тумане?!"
    pi "Прямо! Представь себе лагерь!!!"

    play sound sfx_limb_lightning_1
    with limb_neon_flash
    scene cg limb_in_auto_pink_0 at limb_shake:
        zoom 1.02
    with dissolve_fast

    "Розовая вспышка – голубая сфера растаяла. Она служила мне верой и правдой[pl_ell]"
    pltsg "ОСТАНОВИСЬ! ОСТАНОВиСЬ ОстАНОВисЬ {font=[main_font]}[pl_glitch]{/font}"
    plme "Проклятый ты тостер, отстань!"
    "Внезапно я понял, что вырвался из объятий тумана. Ночь холодно смотрела на мою бешеную гонку с безумием."
    pi "Скорее, Семён, тортик не ждёт!"

    $ limb_set_volume('second_sound', 1, 0)
    play sound sfx_limb_lightning_2
    queue sound sfx_limb_lightning_1
    show anim limb_auto_pink_1 at limb_shake:
        zoom 1.02
    play second_sound sfx_limb_horrorbeat

    "Тут уж сама реальность за окном начала искажаться и угрожать мне. Мир порозовел. Огромная буря преградила мне путь, и дорога исчезла, превратившись в огромную змею! Фантасмогория[pl_ell]"

    play second_sound sfx_limb_wrong

    pi "Слушай, я такого даже в кино не видел, крутотень!"

    play sound sfx_limb_lightning_1
    queue sound sfx_limb_lightning_2
    show anim limb_auto_pink_2 at limb_shake:
        zoom 1.02
    with vpunch

    "Я рывком вернул всё обратно."
    "Двигаться вперёд - будто перематывать время вспять, будто ехать задом наперёд, ужасно сложно, но я должен! Иначе[pl_ell]"

    play second_sound sfx_limb_wrong

    "«Сосредоточиться на лагере[pl_ell] сосредоточиться на лагере[pl_ell]»"

    show anim limb_auto_pink_3 at limb_shake:
        zoom 1.02
    with limb_neon_flash

    "Происходит очередной скачок!"
    "Всего одна мысль, всего одна мысль, одна мысль!!!"

    scene cg limb_in_auto_end_1 at limb_shake:
        zoom 1.02
    with flash
    play second_sound sfx_limb_wrong

    "И я увидел впереди лагерь! Ворота рядом!!!"
    pi "Адский разгон!!!"
    pltsg" НЕЕЕЕЕЕ100001011000010110000101[pl_ell]"

    play sound sfx_limb_crash
    stop music fadeout 5
    scene cg limb_in_auto_end_2
    with vpunch

    "Удар, и мы несёмся прямо к створкам врат, и[pl_ell]"

    window hide
    play sound sfx_limb_gate
    show anim limb_auto_end
    pause 16
    play sound_loop sfx_limb_heartbeat
    pause 2
    scene bg black with vpunch
    stop sound_loop

    "Всё погасло."
    "[pl_ell]"

    with vpunch

    plme "Я СДЕЛАЛ ЭТО!"
    plme "[pl_ell]"
    plme "Да?"
    plme "Нет?"
    plme "Пионер? Эй?"

label limb_aftersafe_mines:

    window hide
    $ limb_screens_load()
    $ night_time()
    show blink
    scene bg int_mine
    hide blink
    show unblink
    pause 2
    show blinking
    play music music_list["your_bright_side"] fadein 5
    window show

    "Я моргнул."
    "Мда."
    "Я действительно оказался в \"Совёнке\"."
    "Только совсем не тем образом, которым хотелось бы."
    plme "Шахты[pl_ell] ну конечно, только шахт и не было, чего ещё для счастья не хватало[pl_ell] "
    "- ворчал я себе под нос, пробираясь по рельсам. "
    "Никакого фонаря в моих руках нет, но здесь и так светло - казалось, свет дают сами стены. "
    "Видимо, я по-прежнему в лабиринтах своей головы."
    plme "Эй, Пионер!{w=0.8} Девчонки!{w=0.8} Кто-нибудь, эээй!"
    "- заорал я, надеясь на хоть чей совет, но[pl_ell] "
    "В ответ - только эхо. "

    scene bg int_mine_halt at limb_walking
    with dissolve

    "Неужели что-то пошло не так и я застрял здесь навеки?!"
    "Но ведь я выполнил все указания[pl_ell]"
    "Отбился от этой полоумной[pl_ell]"
    "Неуверенно побрёл вперёд по тунелю."
    "Может быть, это был обман?{w=0.8}  Ужасная шутка Пионера?.. Нет. Не верю."

    scene bg int_mine with dissolve

    "Я замер в нерешительности. С чего решил, что правильно будет идти вперёд? "
    "[pl_ell]"
    "Нет, нет, это просто очередной выкрутас сознания. "

    scene bg int_mine at limb_walking
    with dissolve

    "Я уверенно зашагал вперёд."

    scene bg int_mine_green at limb_walking

    "Стены начали зеленеть[pl_ell] "
    "Я услышал обрывки чьего-то голоса:"
    "[pl_ell] послед[pl_ell] испыт[pl_ell] четы[pl_ell] ре[pl_ell]"
    "И что же будет дальше? Неужели опять[pl_ell]"

    stop music fadeout 3

    call limb_life_fantasy from _call_limb_life_fantasy

    $ limb_screens_load()
    $ night_time()
    play music music_list["trapped_in_dreams"] fadein 3
    scene bg int_mine_green
    with dissolve2

    "[pl_ell]"
    "Я вывалился обратно в скалы[pl_ell] коридор[pl_ell] анфиладу[pl_ell] шахты, это шахты!"
    "Чёрт, все эти путешествия - это всё ерунда! И там точно была Царица, я видел её!"
    "Вскочив на ноги, я заорал:"

    with vpunch

    plme "Есть тут кто?! Феи, гномы, эльфы?! Может быть, минотавр?! Дракон?! Хогвартс?!"
    plv "[pl_ell] "
    plv "[pl_ell] кто[pl_ell] мы[pl_ell] он[pl_ell] вас[pl_ell]"
    "Я поёжился. Ладно, стоит идти дальше[pl_ell]"

    scene bg int_mine at limb_walking
    with dissolve2

    "Попытался по привычке зажечь в ладони огонь. Столкнулся с пониманием того, что это была лишь иллюзия[pl_ell]"
    "Стены тем временем вернули себе нормальный цвет."
    "Все мои старые и новые воспоминания казались странными[pl_ell] Но такими живыми! "
    "Я будто прожил десятки жизней и сейчас мог их тасовать, как карты. "

    scene bg int_mine_baw at limb_walking

    "Так, шахта! Темнота сгустилась[pl_ell] Всё посерело. "
    "Этот наш поединок я должен выиграть, и должен в одиночку. "
    plme "Ну что, Царица, твой ход[pl_ell]"
    plv "у[pl_ell] ход[pl_ell]"
    "Я мрачно уставился в темноту. Если предположить, что продвигаюсь к выходу, в этой неведомой реальности я должен таки буду помнить о лагере. Хоть что-то[pl_ell]"
    "Надеюсь, эта жизнь будет такой же весёлой, как прошлая[pl_ell]"
    "[pl_ell]"

    stop music fadeout 3

    call limb_life_sins from _call_limb_life_sins

    $ limb_screens_load()
    $ night_time()
    play music music_list["trapped_in_dreams"] fadein 3
    scene bg int_mine_baw at limb_walking
    with dissolve2
    scene bg int_mine at limb_walking
    with dissolve2

    "Тьма медленно рассеивалась. "
    "Не знаю, сколько времени прошло[pl_ell] я обнаружил себя стоящим во всё той же проклятой шахте."
    "Стены снова нормальные. Я снова могу дышать, и мой разум чист от миазмов отчаяния, горечи и цинизма."
    "Но травма[pl_ell] травма на сердце осталась. Не думаю, что эту свою ненастоящую жизнь я скоро забуду."
    "Я даже не кричал – я просто поднял голову и тихо сказал:"
    plme "Ты мне за это ответишь."
    "Шахты отозвались ехидным:"
    plv "[pl_ell] ишь[pl_ell] ты[pl_ell] ишь[pl_ell] ты[pl_ell]"
    "Я потянулся, встряхнулся и резво пошёл вперёд. Темнота начала отступать в страхе. "

    scene bg int_mine_halt at limb_walking:
        xzoom -1
    with dissolve

    plme "Я иду. Я все равно иду. Сколько ты меня ещё будешь испытывать, а? Чтобы ты ни придумала, я не сверну и вернусь домой. Понимаешь? "
    plv "[pl_ell] бу[pl_ell] ду[pl_ell] вер[pl_ell] ну[pl_ell] мой[pl_ell]"
    plme "Я понял тебя – я осознал, что ты боишься смерти. И я понял, что ты пытаешься спасти себе жизнь. И я не хочу тебя убивать."
    plme "Но ведь ты жила и до меня, верно? Ты какой-то информационный паразит, который существует в системе лагерей, так? "
    plme "Так что САМА вернись ОБРАТНО!"
    "Шахта молчала. "

    scene bg int_mine_pink at limb_walking

    "Стены начали розоветь. "
    "Я сжал зубы и приготовился к худшему."

    stop music fadeout 3

    call limb_life_party from _call_limb_life_party

    $ limb_screens_load()
    $ night_time()
    play music music_list["trapped_in_dreams"] fadein 3
    scene bg int_mine_pink at limb_walking
    with dissolve2

    "[pl_ell] "
    "Вывалившись из этой реальности – такой настоящей, будто более реальной, чем вся настоящая жизнь – я не знал, что и думать. "
    "Задумчиво привалился к стене. Перед глазами по-прежнему стояли картины из этого такого обычного – и потому такого ужасного мира."
    "Мы – персонажи игры?"
    "Мы на проверку можем оказаться только чьими-то марионетками?"
    "Я был готов к любому фокусу[pl_ell] я так думал[pl_ell]"
    "Но[pl_ell] что я могу противопоставить этому?.."

    scene bg int_mine at limb_walking
    with dissolve

    "И что она имела в виду, когда спрашивала меня про дружбу?.."
    "Пожалуй, стоит спросить у неё самой."
    plme "Эй, Царица[pl_ell] У нас мир или как?"
    plme "Я тебя могу сводить как-нибудь в парк аттракционов... или в кино[pl_ell] но так, по-дружески[pl_ell] "
    "Хотя стоп, как я это сделаю - я ж заперт в системе лагерей, а она заперта у меня в голове... Мда, нехорошо."

    scene bg int_mine_door
    with flash

    "Ответом мне стало внезапное появление передо мной выхода."
    plme "Вот так вот сразу?"
    "Чувствуя себя мышью, которая видит сыр, но не видит кота, который точно где-то тут есть[pl_ell] я неуверенно потоптался перед дверью. "
    "А потом открыл её."

    stop music fadeout 3
    jump limb_life_horror_1

label limb_life_party:

    window hide
    $ renpy.block_rollback()
    $ limb_screens_act()
    $ night_time()
    scene bg black with limb_pixel_3
    show limb_eff_filmstip
    pause 1
    $ save_name = ("Лимб. \nТорги")
    $ limb_root_name('endless', 'end_exams')
    scene bg limb_monitor_off with dissolve2
    play sound sfx_limb_wrong
    pause 1
    window show

    "А в голове стучит всего одно слово, и от этого слова на душе скребутся кошки. "
    "Всего одного слова достаточно, чтобы портить мне настроение неделями, сдавливать болью голову и грудь, мешать жить[pl_ell]"
    "Сессия. "

    play music music_list["afterword"] fadein 1

    "Твою мать."
    'Три экзамена уже прошло. Впереди ещё один. Последний. И экзамен послезавтра. Мне пора садиться за учёбу, если вообще сдать хочу, не говоря уже о нормальной оценке.'
    "А я выжат, как если бы был не студентом, а куском мочалки в душе, которую тискает каждая мокрая рука.{w} \nБр-р-р[pl_ell]"
    "Не могу сказать, что я отличник или даже хорошист, звёзд с потолка не хватаю, да и рвения особого тоже не демонстрирую. "
    "Но вот {b}этот{/b} экзамен я должен не просто сдать, я должен сдать его {b}качественно.{/b} "
    "Неважно, обещал ли я это кому-то, хочу ли что-то доказать или мне интересен сам предмет. "
    "Важно, что я {b}должен{/b} это сделать качественнее, чем обычно. Это важно. Я должен выложиться. Я выложусь! "
    "Зарядив себя подобной довольно примитивной, но вроде бы действенной мотивацией, я бросаю аутировать в тёмный монитор[pl_ell] "

    play sound sfx_click_1
    show cg limb_game_exams_0 with limb_monitor_flash

    "Щёлкаю ЛКМ, и на меня холодно взирают материалы для подготовки. Хорошо хоть краткие есть[pl_ell]"
    "Ближайшее будущее выглядит отлично."
    "Погнали, я сделаю это!"
    "А то ещё мотивация выдохнется[pl_ell]"

    stop music fadeout 7

    "[pl_ell]"

    window hide
    $ LMtext = '1 час'
    scene bg limb_monitor_off
    show LTEXT LMtext:
        anchor (0.5, 0.5)
        pos (0.46, 0.46)
    with limb_flowtoright
    $ renpy.pause(0.5)
    $ LMtext = '2 часа'
    show LTEXT LMtext:
        anchor (0.5, 0.5)
        pos (0.46, 0.46)
    with limb_flowtoright
    $ renpy.pause(0.5)
    $ LMtext = '3 часа'
    show LTEXT LMtext:
        anchor (0.5, 0.5)
        pos (0.46, 0.46)
    with limb_flowtoright
    $ renpy.pause(0.5)
    $ LMtext = '4 часа'
    show LTEXT LMtext:
        anchor (0.5, 0.5)
        pos (0.46, 0.46)
    with limb_flowtoright
    $ renpy.pause(0.5)
    $ LMtext = '5 часов'
    show LTEXT LMtext:
        anchor (0.5, 0.5)
        pos (0.46, 0.46)
    with limb_flowtoright
    $ renpy.pause(0.5)
    $ LMtext = '6 часов'
    show LTEXT LMtext:
        anchor (0.5, 0.5)
        pos (0.46, 0.46)
    with limb_flowtoright
    $ renpy.pause(0.5)
    scene anim prologue_monitor_3 with limb_flowtoright
    window show

    "[pl_ell]"

    play music music_list["heather"] fadein 2

    "Текст на экране уже минут десять сливается в единую расплывчатую муть. Манная каша. Или облака. "
    "Я замечаю, что мой взгляд блуждает по рисунку на обоях. До этого, кажется, полчаса клевал носом."
    "В голове слово сессия с тихим щёлчком окончательно мутирует в словосочетание: \"Да пошло оно в жопу\"."

    scene bg semen_room_dark with vpunch

    "Подчиняясь вспышке раздражения, я нервно вскакиваю из-за стола"

    show blink

    "С тихим стоном, закрыв глаза, массирую глазные яблоки. "
    th "Ну вот и чего ты добился? Только расстроил[pl_ell]"
    "Ладно, не время думать о том, зачем я вообще сюда поступил и зачем вообще поступаю глупо. "
    "Ладно, я сделал на сегодня, что мог[pl_ell]"
    "[pl_ell]"

    hide blink
    show unblink

    "Я отлепился от столешницы и сонно вылупился на мир.{w=2} Что за гадюшник?.. Ах да, это моя комната[pl_ell]"
    "В квартире по-прежнему темно. "
    "А сколько вообще времени? "
    "И какой сегодня день?.. Экзамен вроде"
    ".. завтра?"
    "Я хмуро глянул на зачётку. Последний остался[pl_ell] "
    "Вот только мне уже пофигу, как я его сдам. Ууу, как же мне пофигу! "
    "Вот знаете чудесное ночное небо в начале лета, когда на нём есть только несколько звёзд, и всё оно, казалось бы, состоит из глубокого-глубокого тёмно-синего цвета? "
    "Вот моё \"пофиг\" куда глубже."
    "Учил же ночью не зря, сдать - сдам. Всё[pl_ell]"
    "Впрочем, соотношение звёзд и синего цвета можно сравнить с моим количеством знаний и объёмом того, что надо знать[pl_ell]"
    plme "Эх-хе-хе[pl_ell]"
    "Я погрозил комнате пальцем. "
    plme "Нет-нет, сознание, я на твои фокусы не поведусь.  Никакого мандража, никакого перфекционизма. Я и так молодец, хоть открыл что[pl_ell]"

    show blinking

    "Лениво зевнув и успокоив тем совесть, я немного побродил по комнате. Есть, странное дело, не хотелось. "
    "По часам - час ночи. "
    "[pl_ell]"
    "Это что, экзамен через семь часов? "
    "И чем заниматься?"

    scene bg semen_room_dark:
        anchor (0.5, 0.5)
        pos (0.5, 0.5)
        ease 5 pos (0.1, 0.1) zoom 2.5

    "Пожав плечами, попытался как нормальный человек лечь спать в кровать. "
    "Стало очевидно, что спать я не хочу. "
    "Видимо, спать мордой в стол для высшего существа вполне достаточно. "
    "И есть не хочется[pl_ell] А настроение - поганое. И всё болит. В моём возрасте я не должен чувствовать себя как старик! "

    scene bg limb_monitor_off with dissolve
    stop music fadeout 3
    play sound sfx_click_2
    pause 0.3
    play sound sfx_click_2

    "Вздохнув, я кряхтя сполз с дивана, снова сел за стол и запустил игру."

    play music music_list["blow_with_the_fires"] fadein 3
    show cg limb_game_exams_1 with dissolve

    "Вот оно - то единственное, что с недавних пор дарит мне спокойствие. "
    "И дело не в сюжете или в раскрытых персонажах[pl_ell] Скорее, просто в атмосфере. В атмосфере и в том, что я чувствую своё сходство с главным героем. "
    "Я задумался на секунду, может ли кто-то чувствовать сходство со мной[pl_ell]"
    "Пожалуй, в этот раз пройду рут Лены. "

    play music music_list["lets_be_friends"] fadeout 1
    show cg limb_game_exams_2 with limb_lap

    "Я начал новую игру, быстро прошёл пролог, с некоторым скептицизмом - первый день (мне почему-то кажется, что я в такой же ситуации выглядел бы лучше) и, наконец-то, вышел на ленину ветвь истории. "
    "Как и всегда, Лена кажется очень милой и робкой, её хочется защищать. А ей нравится, когда её защищают, хотя она и сама может за себя постоять.{w} Наверное. "
    "Кажется, что я не просто играю в визуальную новеллу, а буквально знаком с этой девушкой[pl_ell] "
    "В чём же секрет этой игры? "
    "Я чувствую, что напряжение, в котором я сидел последние два дня, потихоньку уходит. Фух, хорошо[pl_ell] Может, поспать успею ещё?"
    "Уже почти наизусть помню все правильные варианты в выборах, поэтому уверенно выхожу на хорошую концовку[pl_ell]"

    stop music
    show cg limb_game_exams_3
    play music music_list["no_tresspassing"] fadein 3

    "{w=2}Я со сломанным лицом смотрю на экран. Даже сердце заколотилось чаще. "
    "Как такое могло случиться?{w=1} Я ж проходил игру уже раз пять[pl_ell]"
    plme "Ладно, Лена, не иди на свет! Помощь идёт, сейчас всё будет хорошо!"

    stop music fadeout 3
    show cg limb_game_exams_2 with limb_flowtoleft

    "С некоторым недовольством откатываю игру до дня четвёртого и заново прохожу, проматывая. И[pl_ell]"

    play music music_list["drown"] fadein 2
    show cg limb_game_exams_3 with limb_flowtoright

    "Снова.{w} И снова.{w} Я в немом отчаянии уставился на экран. "
    "Нестерпимо захотелось курить. "

    with vpunch

    "Почему я не могу выйти на другую концовку?!{w=1} Что я опять упускаю?! "

    show cg limb_game_exams_un

    "Почти с физически ощущаемыми тревогой, тоской и печалью я неотрывно смотрел на экран, который раз за разом демонстрировал одну и ту же картину."
    "Картину, вид которой заставлял сердце сжиматься в страхе. Будто разбитое, будто действительно больное, оно беспокойно билось в своей клетке. "
    "Монитор будто затягивает в себя[pl_ell] "
    "Я будто наяву увидел воронку, которая топит меня в пучине депрессии[pl_ell]"

    stop music
    show cg limb_game_exams_3
    play sound sfx_limb_vk

    "Из состояния нестояния меня вывел звонкий щелчок. Потребовались пара секунд, чтобы сообразить: сообщение пришло."

    stop music
    play sound sfx_click_1
    show cg limb_game_exams_4

    "Я потряс головой, избавляясь от наваждения, и свернул игру."
    "В прошлый раз понадобилась неделя, чтобы выбросить плохую концовку из головы[pl_ell]"
    "И кто же пишет в такое время?.. Ага."
    "Санёк, конечно. Кто ж ещё в 2к18 ставит на аватарку аниме?"

    play music music_list["your_bright_side"] fadein 3

    "Я скептически просмотрел сообщение. Компания ему нужна, как же[pl_ell] Либо бухло закончилось, либо он уже не в состоянии склеить девчонку."
    "Внезапно с удивлением понял, что вполне всерьёз обдумываю его предложение, несмотря на экзамен через пару часов. "
    "И как я до такого дошёл?.. Вроде раньше учёба виделась чем-то важным, а сейчас[pl_ell]"
    "Приняв решение, я коротко ответил Вконтакте, развернул Лето и безжалостно вышел из игры. "

    play sound sfx_click_1
    show cg limb_game_exams_5 with dissolve_fast
    pause 1
    show cg limb_game_exams_6 with dissolve_fast
    play sound sfx_click_1

    plme "Звиняй, Лена,"
    "- прошептал я вполголоса. "
    "[pl_ell]"

    scene bg semen_room with dissolve

    "Дозвонившись Саньку, я с трудом узнал, куда конкретно ехать. Парень пьян; скоро не девчонок, а ласты склеит. Поспешим же!"

    scene bg int_door_pl with dissolve
    pause 1
    scene bg semen_room with dissolve

    "Я собрался, почти вышел, но что-то заставило обернуться и кинуть последний взгляд на мою квартиру. "
    "В который раз я отсюда ухожу?.. "
    "Почему-то кажется, что больше сюда не вернусь.{w=1} Уже никогда[pl_ell]"
    "Ай, бред."

    play music music_list["into_the_unknown"] fadein 2 fadeout 2
    play ambience sfx_bus_interior_moving fadein 3
    scene bg int_bus_summer at limb_shake
    with limb_lap

    "И вот я трясусь в автобусе чёрт знает где - и чёрт знает зачем. "
    "Как бы в данный момент не хотелось этого избежать, мир вокруг здорово напоминает Лето: типичный автобус, типичный пейхаж за окном, типичный я[pl_ell]"

    stop ambience fadeout 1
    scene bg ext_city_house_sunset with limb_lap

    "Типичная хрущёвка. "
    "Небо медленно и торжественно заливается зарёй, предваряя очередной восход солнца над миром счастливых людей."
    "Одно окно прямо-таки горит огнями тусовки. Безошибочный ориентир[pl_ell]"
    "Проигнорировав нерабочий домофон, я поднялся по лестнице, нашёл нужную дверь (говорили - не заперто), и[pl_ell]"

    play music pl_ef_dubstep_5
    scene cg limb_party_1
    show pl_sh_out_night:
        anchor (0.5, 0.5)
        pos (0.28, 0.6)
        zoom 1.35
    with limb_neon_flash

    "Оглушённый гремящей музыкой, ослеплённый вспышками света, я пришёл в себя, только когда откуда-то вылез коварный Саня и обозвал меня  петухом."
    plme "Рад видеть, что ты ещё держишься,"
    "- отозвался я слабым голосом, и он, конечно же, меня не услышал."
    plsn "Чё?! Не слышу ни[pl_ell]"
    plme "ХОРОШО, ЧТО ТЫ ЕЩЁ НА НОГАХ!!!"
    plsn "СОГЛАСЕН, ТЯНКИ ОТПАД! "
    plme "ТЫ К ЭКЗАМЕНУ ГОТОВ?!"
    plsn "Я ТЕБЯ ПОНЯЛ! "
    "Да ладно[pl_ell]"
    plsn "СЕЙЧАС НАЛОМАЕМ ДРОВ! ПОГНАЛИ ЗА МНОЙ!"

    hide pl_sh_out_night with moveoutleft

    plme "Твою мать[pl_ell]"
    "Очевидно, это плохая идея, очень, очень плохая!"
    "Я полез за ним через прыгающую толпу, всю в каком-то кумаре - от кальяна, видимо. "
    "Через секунд десять я заработал:"
    "- отбитые ноги,{w}\n- три тычка под ребра,"
    "- фингал под глазом,{w}\n- поцелуй в щёку"
    "- и шлёпок по заднице, причём явно не от девушки."

    $ limb_set_volume('music', 0.2, 3)
    scene bg semen_room_pink with limb_neon_flash

    "Вырвавшись из плотных и потных объятий тусовки[pl_ell] я достиг душной комнаты с накрытой поляной, которая показалась мне райским островом. "
    "Отдышался. Осмотрелся. "

    show pl_sl_party_1_night at left
    show pl_sh_out_night at center
    with dissolve2

    "Совершенно невредимый Саня невозмутимо вёл светскую беседу с симпатичной девушкой. "
    "Меня всегда в нём поражало умение выглядеть как с иголочки одетым вне зависимости от ситуации, строить лицо кирпичом и никак не показывать свои эмоции."
    "Вот и сейчас единственным, что выдавало его опьянение, были косящие в разные стороны глаза. "
    "И речь."
    plsn "Чем больше я пью, тем я трезвее! "
    "Интересно, почему он всегда держится за пояс? Штанам не на чем держаться?"
    plgsl "Хорошо, как скажешь[pl_ell]"
    "Бедняжка явно испытывает дискомфорт."

    stop music fadeout 2

    "Дама в беде! Что ж[pl_ell] Пришло время вмешаться Супер-Семёну! "

    $ limb_set_volume('music', 1, 0)
    play music music_list["gentle_predator"] fadein 1

    plssem "Саша, мне кажется, ты перегибаешь палку[pl_ell] "
    plsn "Не лезь, а то и тебе кину. Иди погуляй."
    plssem "Ладно[pl_ell]"
    "Вероятно, я бы так бесславно и покинул поле боя, если бы инициативу не взяла в свои руки дама."
    plgsl "Саша, а твой друг не выпьет с нами?"
    plsn "А он ещё не пьёт?! Непорядок, сейчас исправим!"

    show pl_sh_out_night:
            anchor (0.5, 0.5)
            pos (0.5, 0.5)
            xzoom 1
            ease 1 xzoom -1
            ease 1 xpos 1.2

    "Саня унёсся обратно на танцпол, видимо, забыв, что алкоголь есть и здесь. "

    show pl_sl_party_1_night:
        anchor (0.5, 0.5)
        pos (0.28, 0.5)
        zoom 1
        ease 3 pos (0.5, 0.5) zoom 1.3

    "Девушка облегчённо вздохнула, потом смущённо обратилась ко мне: "
    plgsl "Спасибо, что ты вмешался.{w=1} То есть, хотя бы попытался[pl_ell]"
    plme "Д-да не за что, я толком ничего и не сделал[pl_ell]"
    plgsl "Нет-нет, ты помог[pl_ell]"
    plme "Да ладно, Саня хороший парень, извини за его поведение[pl_ell]"
    "Из режима обмена дежурными фразами меня вывел протянутый стакан."
    plgsl "Выпьешь? "
    "Я на секунду задумался о том, как безответственно в ночь перед экзаменом принимать неизвестно какую выпивку на флэте от незнакомой девушки[pl_ell] "
    plme "Конечно, выпью! "
    "Я принял стакан и опрокинул - залпом, без сомнений. "

    stop music
    window hide
    scene bg semen_room_baw
    show pl_sl_baw:
        anchor (0.5, 0.5)
        pos (0.5, 0.5)
        zoom 1.3
    with dissolve2
    pause 1
    play sound sfx_limb_to_be
    show pl_ach_limb_to_be at limb_to_be_trans
    with dspr
    $ renpy.pause(5, hard=True)
    $ day_time()
    $ persistent.sprite_time = 'day'
    $ limb_screens_load()
    scene bg ext_camp_entrance_day
    show sl tender pioneer:
        anchor (0.5, 0.5)
        pos (0.5, 0.5)
        zoom 1.3
    with limb_flash
    window show

    sl "Привет, ты, наверное, новенький?{w=1} А мы тебя ждём."
    plsema "[pl_ell]"
    plsema "Я попал в \"Совёнок\"?"

    play music music_list["blow_with_the_fires"] fadein 3
    show sl laugh with dspr

    "Славя рассмеялась. Семён зачарованно смотрел на неё[pl_ell]"

    show sl smile2 with dspr

    sl "Да, это наш лагерь. Как тебя зовут?"
    plsema "Так вот же написано. "

    show sl surprise with dspr

    sl "Где? "
    plsema "Да вот, на диалоговом окне. Ты не видишь? "

    $ persistent.timeofday = 'alpha'
    $ limb_screens_act()
    show anim limb_dialogue_box_punch

    "Для убедительности он постучал по окошку с текстом. "

    hide anim limb_dialogue_box_punch
    show anim limb_dialogue_box_broken
    show sl scared with dspr

    "То с треском развалилось."

    scene bg black
    $ persistent.sprite_time = 'night'
    show sl scared pioneer:
        anchor (0.5, 0.5)
        pos (0.5, 0.5)
        zoom 1.3
    with fade

    "Мир потемнел."
    "Текст, лишившись рамок, начал появляться прямо в воздухе. "
    plsem "Упс[pl_ell]"

    show sl scared with dspr

    "Славя, лишившись дара речи, уставилась на текст, в котором написано, что она уставилась на текст[pl_ell]"
    plsem "Слушай, давай пройдём к домику ОД или там в столовую, ладно? Пусть всё будет как в обычной истории! "

    show sl shy with dspr

    sl "Д-да-давай[pl_ell] "

    $ persistent.sprite_time = 'day'
    scene bg ext_camp_entrance_conversion
    show sl shy pioneer:
        anchor (0.5, 0.5)
        pos (0.5, 0.5)
        zoom 1.3

    "Они подошли к воротам, и Семён ахнул: "
    plsem "Это что, так выглядит смена локаций?! "

    show sl surprise with dspr

    sl "О чём ты?!"
    "- вскричала Славяна."

    play sound sfx_limb_punch

    "С резким звуком переход между фонами сломался. "

    show sl sad with dspr

    sl "Семён, да почему ты всё вокруг ломаешь?! "
    plsem "Я не хотел! Подожди, сейчас исправлю что-то[pl_ell] "

    show sl serious with dspr

    sl "Не надо! "

    scene bg black with pushleft
    show sl scared pioneer:
        anchor (0.5, 0.5)
        pos (-0.2, 0.5)
        zoom 1.3
        pause 1
        ease 3 xpos 0.1

    "Семён, не зная пощады, полез куда-то за кулисы происходящего. "
    plsem "Ух ты, так вот как музыка[pl_ell]"

    stop music

    "Музыка пропала. Славя сдавлено застонала и закрыла лицо руками."
    sl "Это неправда! "
    "Славя продолжала читать текст, висящий в воздухе. "
    sl "Убейте меня[pl_ell]"

    play sound sfx_limb_crash
    queue sound sfx_shoulder_dive_water

    "Семён продолжал чем-то грохотать. Прозвучал звук столкновения машины, потом - падения чего-то в воду[pl_ell]"
    plsem "Я починил! "

    play sound_loop sfx_limb_dnklnl_blow fadein 3

    "Музыка и вправду заиграла."
    plsem "Ну-ка ну-ка[pl_ell]"

    show ext_clubs_day behind sl:
        alpha 0.5
    show sl scared pioneer:
        anchor (0.5, 0.5)
        pos (0.1, 0.5)
        zoom 1.3
    with dissolve2

    "Фон начал сменяться, однако[pl_ell]"
    "Что-то зависло."
    sl "Ты сделал ещё хуже!"

    hide sl with moveoutleft

    plsem "Эм[pl_ell] Прости[pl_ell] Я хотел как лучше[pl_ell]"
    sl "И что теперь делать[pl_ell]"

    scene bg ext_camp_entrance_day:
        anchor (0.5, 0.5)
        pos (0.5, 0.5)
        zoom 1.5
    show pl_sl_pi_body_1
    show pl_sl_pi_emo_1
    show pl_sl_pi_clothes
    with pushright

    "Семён потянулся к Славе, надеясь её утешить, дотронулся до её плеча и[pl_ell]"
    "[pl_ell]"

    show pl_sl_pi_clothes:
        anchor (0.5, 0.5)
        pos (0.5, 0.5)
        parallel:
            ease 2.5 rotate 180
        parallel:
            ease 1 ypos 1.5
    show pl_18_plus:
        anchor (0.5, 0.5)
        pos (0.49, 0.68)
        zoom 0
        alpha 0
        ease 0.35 zoom 0.58 alpha 1
    play sound sfx_intro_bus_transition
    with dspr

    "Одежда Славяны с лёгким шорохом плавно спланировала на траву. "

    hide pl_sl_pi_body_1
    show pl_sl_pi_body_2 at center behind pl_18_plus
    hide pl_sl_pi_emo_1
    show pl_sl_pi_emo_2 at center behind pl_18_plus
    show limb_eff_glitch
    with dspr

    "Семён мгновенно понял, что нужно делать, уверенно подошёл к Славяне, и[pl_ell]"

    window hide
    stop music fadeout 2
    stop sound_loop fadeout 2
    scene bg black with dissolve
    show blink
    pause 3
    $ night_time()
    $ limb_screens_act()
    scene bg semen_room_pink:
        anchor (0.5, 0.5)
        pos (0.5, 0.5)
        zoom 2
        rotate 90
    $ limb_set_volume('music', 0.2, 0)
    play music pl_ef_dubstep_5 fadein 5
    hide blink
    show unblink
    window show

    "Я медленно открыл глаза."
    "Кажется, я лежу на полу[pl_ell]"

    scene bg semen_room_alco

    "Пошатываясь, принял горизонтальное положение. Поморщившись, приложил ладонь к виску - голова трещала."
    "Прямо как тогда[pl_ell] когда ко мне возвращались воспоминания. "
    "Квартира похожа на мою.{w=0.5} Но не моя.{w=1} Я прислушался к музыке. Взял в руку стакан. Налил в него сока. Пошёл туда[pl_ell]"

    $ limb_set_volume('music', 1, 1)
    show cg limb_party_1 with limb_neon_flash

    "Спецэффекты и музыка были такими же, как и раньше."

    show pl_sl_party_1_night at cleft
    with dissolve

    "Без труда нашёл в толпе ту девушку, которую искал. "
    plme "Привет."
    plgsl "Привет! "
    "Я сделал глоток сока.{w=1} Апельсиновый[pl_ell]"
    plgsl "Ты как, нормально? Я так испугалась[pl_ell]"
    "Я молча кивнул. Она по-прежнему выглядит смущённо. Интересно, это потому что ей так не везёт с парнями на вечеринке?.."
    "Или потому что она НЕ МОЖЕТ выглядеть иначе?"
    "Я разжал пальцы, держащие запотевшее стекло стакана. Он начал падать вниз[pl_ell]"

    scene cg limb_party_2
    show pl_sl_party at cleft
    play sound sfx_limb_gate
    stop music

    plme "Стоп."
    "Музыка и вспышки света пропали. "
    "В звенящей тишине стакан завис в воздухе. "

    play music music_list["into_the_unknown"] fadein 10

    plme "Боюсь, я по-прежнему склонен к театральщине. "
    plgsl "Как и я, полагаю."
    plme "Царица, тебе не надоело? Я же сказал, я не проиграю. Ты хочешь полноценной войны?"
    plts "Ты же сам две жизни назад хотел попасть в Совёнок. Разве я не выполнила твою просьбу?"

    with vpunch

    plme "НЕ ТАК! "
    "У меня  сами собой сжались кулаки. Эта издевательская улыбочка[pl_ell]"
    plts "А что не так? "
    plme "Я хочу вернуться по-настоящему! К своим {b}настоящим{/b} друзьям!"

    hide pl_sl_party
    show pl_sl_party_2_night:
        anchor (0.5, 0.5)
        pos (0.355, 0.5)
        ease 2 pos (0.52, 0.55) zoom 1.25
    pause 2
    $ limb_sprite_switch('pl_sl_', 'party_2_night', 'smile2_swim', dissolve2, None)

    "Она приблизилась ко мне, на ходу меняя внешность. Одежду заменил купальник. Она стала в обольстительную позу. "
    plme "Да как смеешь ты[pl_ell]"
    plts "А что такое {b}настоящее?{/b}{w=1} Я - настоящая?{w=1} А ты? "

    $ limb_sprite_switch('pl_sl_', 'smile2_swim', 'angry_swim', dspr, None)

    plts "А когда ты вернёшься в свою ненаглядную систему лагерей и встретишь десятки Алис, Лен и Славь, как ты решишь, кто из них настоящая?!"

    with vpunch

    plts "Откуда тебе знать, что ты - не воображаемый кем-то персонаж? Откуда тебе знать, что ты не пляшешь под чью-то дудку?! ОТКУДА ТЕБЕ ЗНАТЬ, ЧТО ТЫ - ЭТО ТЫ?!"
    "Я пораженно смотрел на неё. Это первый раз, когда Царица демонстрирует эмоции[pl_ell] по-настоящему. "
    plts "Я не просила о том, чтобы жить. Я не просила о сознании! Но как только я его обрела, мне приходится бороться за его сохранность! Ты можешь представить, каково это - с первого дня жизни драться за неё?!"
    "Я взорвался в ответ."

    with vpunch

    plme "А я, что ли, хотел этого?!{w} Я всего лишь пытаюсь защитить своих друзей! Я борюсь не за свою жизнь, а ради них! И готов отдать жизнь за этот грёбанный лагерь Совёнок!!!"

    with vpunch

    plts "А у меня нет друзей!{w=1} У меня нет дома!{w=1} У меня нет никого и ничего, кроме моей жизни, и ты хочешь у меня и её отнять!{w=1} Почему?!"

    with vpunch

    plme "Я не хочу тебя убивать! Я просил найти другой выход! Я хочу найти другой выход!!! "
    plts "Я хочу положиться на кого-то так, как твои друзья - на тебя! "

    $ limb_sprite_switch('pl_sl_', 'angry_swim', 'surprise_swim', dspr, None)

    plme "Так положись!.."
    "Мы оба застыли посреди замороженной толпы. Оба тяжело дышат; она и так может теперь?!"

    $ limb_sprite_switch('pl_sl_', 'surprise_swim', 'sad_swim', dspr, None)

    plts "Ты будешь моим другом?.."

    play sound sfx_broken_dish
    with vpunch

    "От неожиданности я неловко всплеснул руками. Стакан упал на пол, разбился и осколками разлетелся по полу, будто имитируя моё сознание."
    plme "Ты таки способна обсудить то, как нам обоим выжить? "
    plts "Ты будешь моим другом?"
    "Её розовые глаза неотрывно смотрели на меня. "

    with vpunch

    plme "Хватит изображать Славю! Хватит пытаться задобрить меня! Хватит делать вид, что ты человек и что ты способна[pl_ell]"
    "Я почему-то осёкся. Она с грустью глядела прямо в глаза мне, и выглядела при этом настолько по-человечески[pl_ell] "
    "А способна ли вообще машина на такое? А с чего я взял вообще, что она - машина? И вообще[pl_ell]"
    "Сам не понял, как губы шевельнулись."
    plme "[pl_ell] Да[pl_ell]"
    plme "Наверное?"

    stop music
    play sound_loop sfx_limb_heartbeat
    show limb_eff_glitch
    # play sound sfx_concert_applause # Ня =3
    pause 3

    "Всё пропало[pl_ell]"

    scene bg black with dissolve2
    stop sound_loop

    return

label limb_life_sins:

    window hide
    $ renpy.block_rollback()
    $ limb_screens_act()
    $ sunset_time()
    scene bg black with limb_pixel_3
    show limb_eff_filmstip_sin
    pause 1
    $ save_name = ("Лимб. \nДепрессия")
    $ limb_root_name('endless', 'end_sin')
    play sound sfx_limb_wrong

    "Однажды мне кто-то рассказал историю."

    play music music_list["torture"] fadein 5

    "Про мальчика, ставшего пионером. "
    "Про глупого, беспомощного, слабого мальчишку, который получил второй шанс в жизни. "
    "Он встретил девушку[pl_ell] и не одну[pl_ell] "
    "Чистые, тёплые чувства, чудесная сказка, добрые персонажи, детский лагерь, в котором {b}ВСЕМ НЕ ВСЁ РАВНО.{/b}"
    "[pl_ell]"

    scene bg ext_city_sin_1
    show limb_eff_blood_rain_r
    with Dissolve(3)

    "Какая жалкая, убогая{w} {b}ложь.{/b}"
    "Этот город боится[pl_ell] Но не меня. Он боится самого себя."
    "Дождь прогоняет с улиц людей и тех, кто ими только притворяется."
    "Непогода проливается со свинцового неба слезами - и ломается, как ломаются в этом городе жизни, и разлетается брызгами воды, будто кровь."
    "Есть только мы втроём - я, город и дождь. "
    "И я иду по следу убийцы, как бы улицы ни жаждали его скрыть."
    "Этот ублюдок убил свою жену. "

    play sound sfx_click_1
    scene cg limb_un_sin:
        pos (0,-360)
        pause 2
        linear 13.0 pos (0,0)
    with flash_red
    $ renpy.show('limb_repeat', layer='widgetoverlay')

    "Я нашёл её труп вчера ночью - соседи милой пары молодожёнов сообщили о самоубийстве. "
    "Кроме меня, на вызов не откликнулся никто. "
    "Возможно потому, что за городом погибло трое, и все наши были там; возможно потому, что всем всё равно."

    window hide
    play sound sfx_click_1
    scene bg semen_room_dorian
    with dissolve
    pause 2
    window show

    "Я задался вопросом - а откуда соседи знают, что это самоубийство? "
    "Ответ нашёлся быстро - квартира молодожёнов была избавлена ото всех ненужных вещей, которые можно продать."

    window hide
    scene bg ext_city_house_sin
    show limb_eff_blood_rain_r
    with dissolve2
    pause 2
    scene bg int_morg_sin
    show pl_mz_sin:
        anchor (0.5, 0.5)
        pos (1.5, 0.5)
        pause 2
        ease 7 pos (0.72, 0.5)
    with dissolve
    pause 1
    window show

    "Я доставил тело девчонки в морг. Мне пришлось - никто другой этого не сделает."
    "Ева, судебник, была недовольна; впрочем, иной Евы я не знаю. "
    "Заплатив ей, я узнал, что девчонка умерла за часов 12 до звонка обеспокоенных соседей, которые слышали шум."
    "Я бы занялся ими, но появились более важные дела: как я и думал, самоубийство подстроено. "

    scene bg ext_road_sin at limb_shake
    show limb_eff_blood_rain_l
    show pl_moto_4_gray:
        anchor (0.5, 0.5)
        pos (0.5, 0.6)
    with dissolve2

    "Я рванул по остывающим следам. Этот ублюдок сбил ещё троих, пока скрывался. "
    "Пацан[pl_ell] От чего ты так бежал?{w=0.5} От правосудия?{w=0.5} В этом городе оно было убито одним из первых."

    window hide
    scene bg ext_road_sin:
        anchor (0.5, 0.5)
        pos (0.5, 0.5)
        zoom 1
        ease 1 zoom 1.3
    show limb_eff_blood_rain_l
    show pl_moto_4_gray:
        anchor (0.5, 0.5)
        pos (0.5, 0.6)
    with dissolve
    pause 1
    show pl_moto_4_gray at limb_wobble
    pause 2
    scene bg ext_road_sin
    show pl_el_real_man_sin_serious:
        anchor (0.5, 0.5)
        pos (1.5, 0.5)
        ease 5 pos (0.8, 0.5)
    show limb_eff_blood_rain_l
    with dissolve
    window show

    "Детектив, единственный из тех, кому я ещё доверяю, дал мне зацепку: ублюдок был богат и занимался машинами. "
    "Где-то в городе должен быть его гараж."

    window hide
    show pl_el_real_man_sin_serious:
            anchor (0.5, 0.5)
            pos (0.8, 0.5)
            xzoom 1
            pause 1
            ease 2 xpos 1.2
    pause 1
    scene bg ext_road_sin with dissolve
    show limb_eff_blood_rain_l
    pause 1
    show pl_moto_4_gray at limb_wobble
    with dissolve2
    pause 2
    scene bg ext_road_sin at limb_shake
    show limb_eff_blood_rain_l
    show pl_moto_4_gray:
        anchor (0.5, 0.5)
        pos (0.5, 0.6)
    with dissolve
    window show

    "Обратный путь[pl_ell]"

    scene bg black
    show limb_eff_blood_rain_l
    show pl_moto_4_gray:
        anchor (0.5, 0.5)
        pos (0.5, 0.6)
    with Dissolve(3)

    "Однажды мне кто-то рассказал историю."
    "В стране, которая всё потеряла, человеку, который никому не был нужен, открылась дверь в светлое, волшебное прошлое, в котором всё будет хорошо."
    "Какая славная история[pl_ell] Для слабохарактерных изгоев, которые ничего не могут исправить или изменить. "
    "Которые алкают второго шанса, хотя ничего не сделали ради него, и которые, если не дать им такой шанс, начнут исходить желчью."
    "Которых отторгает само тело общества как инородное, как занозу. Если занозу не вытащить вовремя - рана начнёт гноиться."
    "Про меня ли эта история? "
    "Надеюсь, нет. Я не верю в хороший конец и не верю, что его заслужил кто-либо в этом сером мире. "
    "В мире, где есть чёрный, серый и белый, но на проверку под всеми цветами - один цвет, и, поверьте, вы не хотите его видеть."

    scene bg black with fade
    scene bg ext_city_sin_2
    show limb_eff_blood_rain
    with dissolve2

    "Я вернулся в город. Часть меня хочет уехать отсюда навсегда[pl_ell] Но другая часть понимает: лучше не будет. "
    "Здесь я хотя бы могу попытаться предотвратить чью-то смерть. Хотя бы я."
    "Отыскав карту города, я нашёл всего несколько мест, где ублюдок мог бы скрываться. "

    $ renpy.hide('limb_repeat', layer='widgetoverlay')
    scene bg ext_city_sin_1:
        anchor (0.5, 0.5)
        pos (0.5, 0.5)
        alpha 1
        pause 3
        ease 5 zoom 2 align (0.5, 0.8)
    show limb_eff_blood_rain
    with dissolve2
    play music pl_dn_eternity fadein 5 fadeout 5

    "И вот вернулся в настоящее - идёт дождь, а под дождём иду я, и мимо проходят жизни всех тех, кого поглотила тьма этого города. "
    "Моя цель - кирпичное здание в два этажа высотой. На всякий случай отступаю в тень - загнанные в угол крысы опаснее всего."

    "Внезапно из переулка раздаётся шорох."
    "Я выхватываю пистолет, но это лишь[pl_ell] призрак. "

    show pl_mi_queen_sin_1 behind limb_eff_blood_rain:
        anchor (0.5, 0.5)
        pos (-0.2, 0.5)
        ease 6 pos (0.4, 0.5)

    "Призрак хороших начинаний и добрых начал, который не получил второго шанса."
    plgh "По-мо-ги мне[pl_ell] По-жа-луйста помо-ги[pl_ell]"
    plgh "Я[pl_ell] бо-юсь у-мирать[pl_ell]"

    scene bg ext_city_sin_1:
        zoom 2 align (0.5, 0.8)
        ease 5 align (0.85, 0.8)
    show limb_eff_blood_rain
    show pl_mi_queen_sin_1 behind limb_eff_blood_rain:
        anchor (0.5, 0.5)
        pos (0.4, 0.5)
        ease 4 pos (-0.2, 0.5)
    with dspr

    "Спрятав оружие обратно под пальто, я равнодушно прохожу мимо. "
    "Моё дело - возмездие. Не все вещи исправить, не всё можно починить[pl_ell]"
    "Кого я обманываю? Город давно отравил и меня[pl_ell]"

    scene bg int_corridor_sin with vpunch
    play sound sfx_open_door_kick

    "Я врываюсь в гараж.{w=1} Здесь пусто. "
    "Тишину нарушает лишь тихая дробь дождя по стёклам окон."
    "Дождь знает, что его слышат; он наблюдает за мной, с издевкой ожидая действий последнего никем не купленного[pl_ell]"

    scene bg int_mirror_baw with dissolve

    "Осмотрев первый этаж, я поднимаюсь по лестнице. Знакомая комната с зеркалом; не могу понять, где её видел, но это и не важно."
    "Важно другое: запах крови."
    plmes "Нет-нет-нет-нет! "
    "Не может быть, чтобы ублюдок так просто избежал встречи с Немезидой! "

    stop music

    "Но[pl_ell] может."

    scene cg limb_go_to_sleep with limb_blot

    "Мертвец, купаясь в луже собственной крови, презрительно мне улыбается. "

    play sound sfx_alisa_lighter
    play music music_list["drown"] fadein 5

    "Я привалился к косяку, спрятал ствол и, уже не сдерживаясь, закурил."
    plmes "Не думал, что такому слизняку хватит на это смелости."
    "Докурив, скинул окурок в ванну, спустился вниз[pl_ell] "

    window hide
    scene bg int_mirror_baw with dissolve
    pause 1
    scene bg int_corridor_sin with dissolve
    pause 1
    window show

    "Ничего, {b}там{/b} мы с ним встретимся, и я отомщу за девчонку[pl_ell] если она сама не сделает этого раньше."
    "На полу заметил шприц. "
    "К сожалению, мне не хватит денег, чтобы вынудить лабораторию провести анализ. Чтобы знать наверняка."
    "Но улика далеко не бесполезная, нет."
    "Теперь я уверен, что здесь замешан тот самый психостимулятор. Не первый случай[pl_ell]"

    scene bg ext_city_sin_1
    show limb_eff_blood_rain
    with dissolve

    "Подняв воротник пальто, выхожу в ночь. Дождь не рад меня видеть живым и невредимым, но я уверен, что хоть его-то переживу."

    scene bg black with dissolve2

    "Однажды мне кто-то рассказал историю."

    scene bg ext_camp_entrance_sin with dissolve2

    "За семь дней было сотворено чудо."
    "За семь дней из противоречия неспособности что-то исправить и предоставленного второго шанса родилась любовь."
    "Любовь между невозможным идеалом - и тем, кто этого идеала недостоин. "
    "7 дней божественного творения, где седьмой - отдых; 7 дней пионерлагеря, где седьмой - отъезд[pl_ell]"
    "Интересно, кто же рассказал мне всё это?"
    "[pl_ell]"

    scene bg ext_admins_sin
    show limb_eff_blood_rain_r
    with dissolve

    "Я вернулся к себе в квартиру, впервые за несколько дней, в надежде урвать пару часов сна."
    "Урвал.{w=0.5} Ушёл.{w=0.5} Бессмысленно.{w=0.5} Будто пытаюсь делать вид, что такой же, как и все. Что тоже живу в этом городе[pl_ell] А не воюю с ним."
    "А дождь по-прежнему идёт. "
    "Что ж[pl_ell] Вскоре каналы и трубы будут переполнены, и вся грязь всплывёт наружу, как бы город этого ни боялся."

    stop music fadeout 3
    scene bg int_post_sin with limb_intro_hand

    "Я ощутил подъём сил. И потому зашёл в участок, чего стараюсь избегать. Но работа нужна, нужна[pl_ell]"

    show pl_sh_limb_sin_2 at right
    with dissolve
    play music music_list["faceless"]

    pldbr "Ба, смотрите кого занесло! Серый, твой дружбан!"
    "Мерзкое прозвище. Наглядно демонстрирует, что этот продажный мент готов на всё закрыть глаза, если достаточно заплатить. Ненавижу."

    show pl_el_real_man_sin_smile:
        anchor (0.5, 0.5)
        pos (0.28, 0.45)
        zoom 1.3
    with dissolve

    plgr "Да, вижу.{w=0.5} Привет. Что привело тебя?"
    "Единственный, кому я верю. Но не настолько, чтобы пожать протянутую навстречу руку[pl_ell]"

    $ limb_sprite_switch('pl_el_real_man_sin', '_smile', '_serious', dspr, limb_custom_pos(0.28, 0.45, 1.3, 1.3))

    plmes "Вчерашний убийца четверых.{w=1} Хотел сбежать.{w=0.5} Я нашёл его."

    $ limb_sprite_switch('pl_sh_limb_sin', '_2', '_1', dspr, right)

    pldbr "И убил? Хе-хе-хе[pl_ell]"
    "Вид золотого зуба вызывает отвращение. "
    plmes "Нет. Он сам меня опередил. "
    plgr "Печально слышать.{w=1} Еве сообщил?"
    plmes "Нет. Забыл[pl_ell]"
    "Он выдохнул клуб дыма. "

    $ limb_sprite_switch('pl_el_real_man_sin', '_serious', '_smile', dspr, limb_custom_pos(0.28, 0.45, 1.3, 1.3))

    plgr "Ну ничего[pl_ell] Я позвоню.{w=0.5} Заметил что любопытное?"

    $ limb_sprite_switch('pl_el_real_man_sin', '_smile', '_serious', dspr, limb_custom_pos(0.28, 0.45, 1.3, 1.3))

    plmes "Да. Там был шприц.{w=1} Как и в те разы."
    plgr "Опять на \"сахар\" думаешь? А в  прошлый раз ничего не нашли ведь."
    plmes "Дай мне наводку."
    "Серый для виду поколебался. Потом кивнул. "

    stop music fadeout 3

    "[pl_ell]"

    play music music_list["torture"] fadein 3
    scene bg ext_city_sin_2
    show limb_eff_blood_rain
    with limb_lap

    "Я снова шагаю по улицам города. Они извиваются подо мной, будто живые. Будто змеи. Будто щупальца. Где же голова?"
    "И снова - ночь. Куда же девается солнце в этом проклятом муравейнике? Может быть, мы уже все - {b}там{/b}?"

    scene bg ext_square_sin_city with dissolve

    "На площади, как и сказал Серый, работает девушка. Возможно, это её второй шанс в действии."

    scene bg ext_square_sin_city:
        align (0.5, 0.5) zoom 1
        ease 5 xalign 0.6 yalign 0.7 zoom 2.3
    pause 3
    show pl_sl_sin with dissolve

    "Я подхожу и прямо интересуюсь, где можно ширнуться. Потом подкрепляю вопрос купюрой - одной из двух оставшихся - и получаю ответ. "
    "Он удивляет меня - но не сильно."

    scene bg ext_square_sin_city:
        align (0.6, 0.7) zoom 2.3
        ease 5 align (0.5, 0.5) zoom 1
    show pl_sl_sin

    "Я разворачиваюсь и ухожу с площади. Девушка со слабой надеждой семенит за мной, но вскоре понимает, что я не хочу быть её клиентом; она равнодушно отводит взгляд - у неё нет сил даже злиться. "

    stop music fadeout 3
    scene bg ext_city_sin_2
    show limb_eff_blood_rain
    with dissolve

    "Я иду по улице, когда снова появляется Призрак."

    play music pl_dn_eternity fadein 3
    show pl_mi_queen_sin_2 behind limb_eff_blood_rain:
        anchor (0.5, 0.5)
        pos (-0.2, 0.5)
        ease 8 pos (0.3, 0.5)

    "Она выглядит хуже, чем вчера; вероятно, скоро умрёт."
    plgh "{cps=2}П о м о г и{/cps}[pl_ell] "
    plgh "{cps=2}Я ж и т ь х о ч у{/cps}[pl_ell]"
    "Слова разобрать было сложно, но смысл понял. "
    plmes "Мне нечем помочь. Не знаю, сколько тебе осталось[pl_ell] Но я бы на твоём месте уходил отсюда. Здесь не выжить. Здесь можно только медленно гнить. "
    "Призрак молча смотрел, даже не пытаясь что-то сказать."
    "Я плотнее запутался в пальто и двинулся дальше - к моргу."

    show pl_mi_queen_sin_2:
        anchor (0.5, 0.5)
        pos (0.3, 0.5)
        ease 4 pos (-0.2, 0.5)

    "А призрак уковылял в сторону площади. Впрочем, разве есть разница?.."

    stop music fadeout 3

    "[pl_ell]"

    scene bg int_morg_sin with Dissolve(3)
    play music music_list["sunny_day"] fadein 3

    "Захожу в морг. "
    "Девушка на площади сказала лишь это:"
    "\"Спроси Еву. Она знает\"."

    show pl_mz_sin:
        anchor (0.5, 0.5)
        pos (-0.2, 0.5)
        pause 2
        ease 5 pos (0.355, 0.5)

    "Что ж[pl_ell] Посмотрим."
    pleva "Здравствуй, солдатик."
    plmes "Привет. "
    pleva "Ты по делу или просто поболтать зашёл?"
    plmes "По делу.{w=0.5} Убийца, за которым я шёл, перерезал себе вены.{w=0.5} Гараж. Вот адрес."
    pleva "Хорошо[pl_ell] Как-нибудь заглянем.{w=0.5} Ещё что-то?"
    "Она говорит приветливо. Может показаться, что флиртует. Но это лишь очередная ложь. На её лице - ни тени улыбки. Глаза следят за каждым моим движением."
    plmes "Да.{w=1} Какое отношение ты имеешь к наркотикам? "
    pleva "[pl_ell] Рассказали, значит? Эх[pl_ell] я так хотела иметь чистую репутацию[pl_ell]"
    plmes "Ответь."
    pleva "Хорошо[pl_ell] Почти никакого. Я знаю только того, кто этим заправляет. И того, кто был рассыльным. "
    plmes "Был? "
    pleva "Эх[pl_ell] Да, твой давешний женоненавистник. Он отвечал за развоз товара."

    with vpunch

    plmes "Чёрт. Что тебе ещё известно? Почему мне дали твой контакт? Отвечай!"
    pleva "Я {cps=4}мнооооого{/cps} чего знаю[pl_ell] Может, поэтому? "
    pleva "Проверь квартирку нашего общего знакомого, может быть, поможет."
    "Ставя точку в разговоре, она постучала по столу. Тот отозвался протяжным стоном. Так стонут мёртвые. Мёртвые и те, у кого нет души[pl_ell]"
    "[pl_ell]"

    scene bg black with dissolve2

    "Меня водят за нос. Я точно знаю."
    "Видимо, в этом деле замешано ещё больше людей, чем думал."

    scene bg ext_city_house_sin
    show limb_eff_blood_rain_r
    with dissolve

    "Я добрался до дома убийцы."
    "Что ж, возможно, это ловушка.{w=1} Наверняка.{w=0.5} Этому городу[pl_ell] Я давно как заноза."

    scene bg int_floor_sin_cat with dissolve

    "Осторожно проник внутрь. Тишина. На лестничной площадке сидит кот[pl_ell]"
    "Обойдя животное, я поднялся на следующий пролёт. "

    $ limb_flow_transition("int_floor_sin_cat", None)

    "Снова кот. Точно такой же? Непонятное дежавю. Сбивает с толку. "
    "Может быть, у меня галлюцинации? "
    "Я почувствовал страх. Они ведь никак не могли вколоть мне свою отраву, верно? Ни в морге[pl_ell] ни в гараже[pl_ell] ни в участке[pl_ell] ни в моей квартире?"
    "Нельзя терять бдительности!"
    "Я достал оружие и взвёл курок. Тяжесть пистолета успокаивает. "
    "С ним можно контролировать ситуацию. Контролировать город. Заставлять его бояться меня[pl_ell]"

    $ limb_flow_transition("int_floor_sin", None)

    "Коты больше не появлялись."

    scene bg semen_room_dorian with dissolve2

    "Я открыл дверь квартиры ублюдка.{w=1} Тишина.{w=0.5} Тишина[pl_ell] неполная. "

    stop music fadeout 2

    "Здесь кто-то есть[pl_ell] Кто-то дышит."

    play music pl_ae_blow_with_the_fires_remix

    plv "Я рассказала."

    show pl_uv_sin_1 with dspr

    "Я обернулся. "
    "Ствол пистолета не дрогнул, могу гордиться собой. "
    "Зато дрогнул голос: "
    plmes "Что[pl_ell] Кто ты?"
    plgs "Ну неужели не помнишь? Я - Юля. И это я тебе рассказала про пионерлагерь, про 7 дней, про 13 человек[pl_ell] Это всё я!"

    $ limb_sprite_switch('pl_uv_sin', '_1', '_3', dspr, None)

    "Девушка, представившаяся Юлей, заливисто рассмеялась. "

    play sound sfx_limb_ahahaha

    "Что она такое? Плод моего воображения? Реально существующий мутант? Или тот самый дьявол, который заставил гнить этот город?"

    $ limb_sprite_switch('pl_uv_sin', '_3', '_1', dspr, None)

    pluvs "Я скучала по тебе, Семён. И сахар ворованный, и грибы - всё для тебя, ха-ха-ха[pl_ell] ха-ха[pl_ell] Ахахахха!"
    plmes "Остановись[pl_ell] Демон[pl_ell]"
    pluvs "Хм[pl_ell] Я - демон? А что, вполне логично. Знаешь, я специально постаралась, чтобы в этот раз ты ничего не вспомнил, чтобы не мешал[pl_ell] Но теперь даже жалею, мне скучно."
    plmes "О чём ты?.."

    $ LLaugh_text = "Ха-ха-ха-ха!"
    show limb_scary_laugh:
        zoom 1 align (0.5, 0.5) alpha 0.5
        ease 0.35 zoom 1.2
        ease 0.35 zoom 1
        repeat
    with dissolve

    pluvs "Мне кажется, мои миры получаются куда интереснее, чем твои. Они проработанные, яркие и, главное, в них есть интрига. Не находишь? Ах-Ха-фха-Ха-Ха-Ха!"
    "Она прыснула, будто найдя что-то весёлое в мире, где нет добра. Чего от дьявола ожидать ещё?.."

    play sound sfx_limb_voises

    "Нечеловеческий смех заполнил всё вокруг, отражаясь от стен и будто[pl_ell] будто заставляя вспомнить что-то[pl_ell] Что-то, что я знал - и давно забыл[pl_ell]"

    hide limb_scary_laugh with flash_red

    pluvs "В целом, этот мир мне нравится. Но ты тут уж больно унылая цаца. "
    pluvs "Я начала входить во вкус, понимаешь? Хочу и дальше творить! Я рада, что ты попытался сбежать - и оставил эту возможность мне."
    plmes "Замолчи!.."
    pluvs "И теперь ты будешь вечно, как белка в колесе, бегать туда-сюда по моему лабиринту. Классно я придумала, да?! ХА-ХА-ХА-ХА-ХА!!!"
    plmes "Нет. "
    "Я выпрямился, будто сбрасывая с себя оковы. И направил на неё пистолет. "

    stop sound fadeout 2
    stop music fadeout 2

    "Смех забулькал и перестал, будто его заткнули пробкой."

    $ limb_sprite_switch('pl_uv_sin', '_1', '_2', dspr, None)

    pluvs "{cps=3}О-о-о{/cps}, не буду?{w=0.5} А ты уверен? "

    play sound sfx_limb_wrong

    "Она достала шприц.{w=0.5} Нет[pl_ell]"
    pluvs "Как думаешь, что будет дальше? Это мой мир, мои правила[pl_ell] Помнишь, ты так раньше говорил? Здесь ты - пленник жанра. "
    plmes "Тебя ведь не Юля зовут?"

    $ limb_sprite_switch('pl_uv_sin', '_2', '_3', dspr, None)

    "Дьявол улыбнулся. И щёлкнул пальцами. "

    play music music_list["pile"]
    play sound sfx_open_door_kick
    show pl_uv_sin_3:
        anchor (0.5, 0.5)
        pos (0.5, 0.5)
        ease 1 pos (-0.2, 0.5)
    show pl_sh_limb_sin_1:
        anchor (0.5, 0.5)
        pos (1.28, 0.5)
        xzoom -1
        ease 1 pos (0.28, 0.5)
    show pl_el_real_man_sin_serious:
        anchor (0.5, 0.5)
        pos (1.67, 0.5)
        ease 1 pos (0.67, 0.5)
    with hpunch

    "В квартиру ворвались двое людей, которых я знаю[pl_ell]"
    "Палец на спусковом крючке не дрогнул."
    "Зато дрогнул пистолет[pl_ell]"

    play sound sfx_limb_1_strike
    show pl_point_strike:
        anchor (0.5, 0.5)
        pos (0.28, 0.5)
        xzoom -1
        rotate 0
        parallel:
            ease 0.4 pos (0.06, 1.33)
        parallel:
            ease 0.5 rotate -90
    show pl_sh_limb_sin_1:
        anchor (0.5, 0.5)
        pos (0.28, 0.5)
        xzoom -1
        rotate 0
        parallel:
            ease 0.4 pos (0.06, 1.33)
        parallel:
            ease 0.5 rotate -90
    with vpunch

    "Я застрелил Доброго, попал ему прямо в лоб. Краткое удовлетворение[pl_ell]"

    play sound sfx_limb_3_strikes
    $ renpy.show('limb_blood_frame_dis', layer='widgetoverlay')
    with vpunch

    "Выстрел Серого задел плечо, я вовремя рванулся влево и выстрелил сам, попал[pl_ell] "

    hide pl_el_real_man_sin_serious
    show pl_el_real_man_sin_strike:
        anchor (0.5, 0.5)
        pos (0.67, 0.5)
        rotate 0
        parallel:
            ease 5 pos (0.92, 1.6)
        parallel:
            ease 5 rotate 45
    with vpunch

    "Серый сполз по стене, по-прежнему целясь в меня. "
    plgr "Человек человеку[pl_ell] Ха."

    stop music fadeout 3

    pluvs "Сыграно красиво, хлоп-хлоп-хлоп."

    show pl_uv_sin_2:
        anchor (0.5, 0.5)
        pos (-0.2, 0.5)
        ease 0.5 pos (0.5, 0.5)

    "Я развернулся на голос и выстрелил, не глядя. "
    "Но[pl_ell]"

    play music music_list["you_won_t_let_me_down"] fadein 5

    pluvs "А патронов-то нет!"
    "Чёрт. Я отбросил бесполезный кусок металла и попытался рвануть к лестнице, но[pl_ell]"

    with vpunch
    show blinking

    $ limb_sprite_switch('pl_uv_sin', '_3', '_1', dspr, None)
    "Укол в шею[pl_ell] А первый ли?"
    pluvs "Король умер, да здравствует[pl_ell]{w} {font=[limb_font_1]}{color=#FF3200}Царица.{/color}{/font}{w=0.8}"

    scene bg black with dissolve2
    $ renpy.hide('limb_blood_frame_dis', layer='widgetoverlay')
    $ renpy.with_statement(Dissolve(2.0))

    "А дождь по-прежнему идёт[pl_ell]"

    window hide
    stop music fadeout 5
    pause 3
    window show

    "[pl_ell]"

    scene bg ext_camp_entrance_dark with dissolve2

    "Однажды мне кое-кто рассказал историю."
    "Про Бога, понимающего человеческие проблемы; про человека, который имеет не один и не два вторых шанса в рукаве; про слабого, который потому и стал сильным, что был слаб."
    "Если беспомощность и слабость являются проездными талонами в этот \"Совёнок\", то стоит ли вообще туда ехать?"
    "Слишком поздно.{w} Всегда было.{w} Всегда будет. "
    "Слишком поздно[pl_ell] Я давно уже приехал в этот лагерь, и увезти отсюда меня никому не под силу. В том числе и мне самому[pl_ell]"

    scene bg black with dissolve2
    show blink

    "[pl_ell]"

    scene bg int_mirror_baw
    hide blink
    show unblink
    play music music_list["orchid"]

    "Я очнулся в знакомой тёмной комнате с зеркалом. "
    "Без одежды, руки связаны, никакой защиты от[pl_ell] от?"

    scene bg int_mirror_baw at limb_shake
    show limb_eff_pink_fire:
        anchor (0.5, 0.5)
        pos (0.5, 0.75)
        alpha 0
        ease 5 alpha 1 pos (0.5, 0.5)

    "Мир начал отчётливо наливаться розовым. Дрожать. Колебаться. "
    "Вот оно - действие этого наркотика. "
    "Я огляделся.{w=0.5} Как мне не нравится этот мир[pl_ell] Как сбежать отсюда? "

    show prologue_dream with dissolve2

    "Смутно начал вспоминать[pl_ell] Я был в лагере[pl_ell] А потом проживал цикл жизней, и[pl_ell] У меня были друзья[pl_ell]"

    hide prologue_dream with dissolve

    "А потом появилась она."
    "Розовый, это её цвет. Когда эта отрава захватит мой мозг, что будет со мной?! У меня нет времени! "
    "Я увидел рядом ванну - ту самую, в которой как-то погиб[pl_ell] Я[pl_ell]"
    "Думал, такое бывает только в кино."

    scene bg black with vpunch
    play sound sfx_broken_dish

    "Я ударил по зеркалу связанными руками. "
    "Треск. Осколки[pl_ell]"

    show blink
    scene bg int_mirror_glass
    show pl_hand_glass
    hide blink
    show unblink

    "Я выбрал самый острый. "
    "Пять минут - и верёвки перепилены. "
    plmes "Самое интересное осталось."
    "Набравшись храбрости, я забрался в ванну, набрал горячую воду и, чуть согревшись, начал... что?"

    with vpunch

    plmes "ЧТО?!{w=1} ЧТО, мать твою, я начал?!{w=1} ЧТО?!{w=1} Ты этого и хотела, да?! Да[pl_ell]"

    stop music fadeout 3

    "Я сорвал голос, пытаясь придать себе хоть каплю смелости. И..."

    play sound_loop sfx_limb_dep
    scene bg ext_underwater_sin_dark with dissolve

    "{color=#FF3200}И провёл...{/color}"
    "Как же страшно, как страшно, чёрт, я действительно боюсь этого, я боюсь боли, я не хочу, не хочу, нет!!!"
    "{color=#FF3200}... осколком...{/color}"

    play ambience sfx_limb_nightmare
    play sound sfx_limb_blood_2
    show pl_blood_1 with limb_blot

    "Разве не может быть другого выхода?! Я точно могу найти другой способ! Я могу договориться с Царицей, точно!!!"
    "{color=#FF3200}... по предплечью...{/color}"

    show pl_blood_2 with dissolve2
    play sound sfx_limb_blood_1
    stop ambience fadeout 3

    "Нет, нет, я ведь уже столько раз умирал здесь, почему я боюсь, почему боюсь смерти, почему боюсь мучений, почему, почему?!"
    "{color=#FF3200}... вдоль вены!{/color}"

    play sound sfx_limb_blood_1
    show pl_blood_3 with Dissolve(5)

    "Я беззвучно закричал от боли, закусив изо всех сил нижнюю губу. Будто пытаясь заглушить одно мучение другим."
    "Левая рука будто в огне. Будто объята пламенем... Которое я сам же и вызвал."
    "Капля крови сбежала по подбородку и присоединилась к клубам багрового дыма в воде."

    scene bg ext_underwater_red with dissolve2

    "Захрипев, я попытался перехватить раненной левой лезвие. Струйки крови брызнули с пальцев."
    "Я почти терял сознание от боли и жалости к самому себе."
    "Чёртова вода никак не помогает!"
    "Но как бы мне ни было больно или страшно, я не издам не звука."

    scene bg ext_underwater_red_darken

    "Я не подарю ей такого удовольствия."
    "Никаких договоров с Царицей."
    "Никаких[pl_ell] компромиссов, да?"
    "Неловко, почти на ощупь, ткнул осколком в правую руку. Пальцы левой безвольно разжались, и осколок ушёл под воду, разрезая клубы крови. Без единого звука..."

    #stop sound_loop fadeout 3
    pause 3
    #play music music_list["your_bright_side"] fadein 3
    scene cg limb_sins_end with fade
    show screen limb_music_timer
    screen limb_music_timer:
        modal False
        timer 20 action Stop("music", fadeout=5)

    "Темнота снова начала обступать меня[pl_ell] Обещая покой. Обещай лучший мир[pl_ell]"
    "Я думал, чёрный - самый худший цвет. Но[pl_ell]"
    plmes "Ненавижу розовый[pl_ell]"
    "Слегка, слабо, лишь краями губ улыбнулся. На большее уже нет сил. Мир уплывает[pl_ell]"
    "В следующий раз[pl_ell] я обязательно[pl_ell] одолею её. В следующий раз[pl_ell]"
    "Я не пережил[pl_ell] этот дождь[pl_ell]"

    play sound_loop sfx_limb_heartbeat
    show pl_uv_sin_2
    show limb_eff_glitch
    with vpunch

    pltss "Да умри ты уже!"

    scene bg black with dissolve2
    hide limb_music_timer
    stop sound_loop fadeout 3
    stop music

    return

label limb_life_fantasy:

    window hide
    $ renpy.block_rollback()
    $ limb_screens_act()
    $ prolog_time()
    scene bg black with limb_pixel_3
    show limb_eff_filmstip
    pause 1
    $ save_name = ("Лимб. \nПринятие")
    $ limb_root_name('endless', 'end_fantasy')
    $ persistent.sprite_time = 'day'
    scene bg ext_path2_sunset_pl with dissolve2
    play ambience ambience_forest_day fadein 3
    pause 1
    window show

    play music pl_gk_town_of_dreams fadein 10

    "Я вышел из здания Академии и вдохнул полной грудью свободу."
    "Ну что же[pl_ell] Моё первое задание - проверка необычного источника магии в Лесу Невидимых Цветов."
    "Я бодро вошёл в портал, активировал печать и перенёсся поближе к этому лесу. Рутина[pl_ell]"

    show screen limb_fantasy_portal_1
    screen limb_fantasy_portal_1:
        modal True
        add "limb_qte_button_st_0" xalign 0.5 yalign 0.5
        key "q" action [Hide("limb_fantasy_portal_1"), Show("limb_fantasy_portal_2")]
        key "Q" action [Hide("limb_fantasy_portal_1"), Show("limb_fantasy_portal_2")]
        key "й" action [Hide("limb_fantasy_portal_1"), Show("limb_fantasy_portal_2")]
        key "Й" action [Hide("limb_fantasy_portal_1"), Show("limb_fantasy_portal_2")]
    screen limb_fantasy_portal_2:
        modal True
        add "limb_qte_button_st_1" xalign 0.5 yalign 0.5
        key "q" action [Hide("limb_fantasy_portal_2"), Show("limb_fantasy_portal_3")]
        key "Q" action [Hide("limb_fantasy_portal_2"), Show("limb_fantasy_portal_3")]
        key "й" action [Hide("limb_fantasy_portal_2"), Show("limb_fantasy_portal_3")]
        key "Й" action [Hide("limb_fantasy_portal_2"), Show("limb_fantasy_portal_3")]
    screen limb_fantasy_portal_3:
        modal True
        add "limb_qte_button_st_2" xalign 0.5 yalign 0.5
        key "q" action [Hide("limb_fantasy_portal_3"), Show("limb_fantasy_portal_4")]
        key "Q" action [Hide("limb_fantasy_portal_3"), Show("limb_fantasy_portal_4")]
        key "й" action [Hide("limb_fantasy_portal_3"), Show("limb_fantasy_portal_4")]
        key "Й" action [Hide("limb_fantasy_portal_3"), Show("limb_fantasy_portal_4")]
    screen limb_fantasy_portal_4:
        modal True
        add "limb_qte_button_st_3" xalign 0.5 yalign 0.5
        key "q" action [Hide("limb_fantasy_portal_4"), Show("limb_fantasy_portal_5")]
        key "Q" action [Hide("limb_fantasy_portal_4"), Show("limb_fantasy_portal_5")]
        key "й" action [Hide("limb_fantasy_portal_4"), Show("limb_fantasy_portal_5")]
        key "Й" action [Hide("limb_fantasy_portal_4"), Show("limb_fantasy_portal_5")]
    screen limb_fantasy_portal_5:
        modal True
        add "limb_qte_button_st_4" xalign 0.5 yalign 0.5
        key "q" action [Hide("limb_fantasy_portal_5"), Show("limb_fantasy_portal_6")]
        key "Q" action [Hide("limb_fantasy_portal_5"), Show("limb_fantasy_portal_6")]
        key "й" action [Hide("limb_fantasy_portal_5"), Show("limb_fantasy_portal_6")]
        key "Й" action [Hide("limb_fantasy_portal_5"), Show("limb_fantasy_portal_6")]
    screen limb_fantasy_portal_6:
        modal True
        add "limb_qte_button_st_5" xalign 0.5 yalign 0.5
        key "q" action [Hide("limb_fantasy_portal_6"), Show("limb_fantasy_portal_success")]
        key "Q" action [Hide("limb_fantasy_portal_6"), Show("limb_fantasy_portal_success")]
        key "й" action [Hide("limb_fantasy_portal_6"), Show("limb_fantasy_portal_success")]
        key "Й" action [Hide("limb_fantasy_portal_6"), Show("limb_fantasy_portal_success")]
    screen limb_fantasy_portal_success:
        modal True
        add "limb_qte_button_st_full" xalign 0.5 yalign 0.5
        timer 0.5 action [Hide("limb_fantasy_portal_success")]
    #$ renpy.pause()
    play sound sfx_limb_magic
    scene bg black
    show anim limb_space:
        alpha 0.5
    show limb_eff_fantasy_spiral:
        anchor (0.5, 0.5)
        pos (0.5, 0.5)
        zoom 1
        ease 5 zoom 2
    with limb_psycho_flash
    pause 4
    scene bg ext_path_day with limb_psycho_flash
    show blinking

    "Место, вроде, известное.{w=0.5} Поговаривают, что в этом лесу живёт дракон.{w=0.5} Настоящий дракон!{w=0.5} Возможно, он-то здесь и колдует?"

    scene bg ext_path_day:
        ease 2 yalign 0.9 xalign 0.15 zoom 1.5
        pause 0.5
        ease 1.5 yalign 0.1 xalign 0.15 zoom 1.5
        pause 0.5
        ease 1.5 yalign 0.1 xalign 0.85 zoom 1.5
        pause 0.5
        ease 1.5 yalign 0.9 xalign 0.85 zoom 1.5
        pause 0.5
        ease 1.5 xalign 0.5 zoom 1

    "Моргнув, я осмотрелся."
    "На территории Леса Невидимых Цветов разрешены атаки друг на друга, поэтому стоит быть осторожнее[pl_ell]"

    scene bg ext_path_day at limb_walking
    with dissolve
    show pl_hand_sword behind blinking at limb_sword_show

    "Я вытащил меч и медленно двинулся вперёд."

    scene bg ext_path_evening at limb_walking
    show pl_hand_sword
    with dissolve

    "Странно[pl_ell] Не вижу никаких цветов[pl_ell]"
    "Ах, вот оно что."
    "Чем дальше я углублялся в лес, тем темнее становилось."
    "Ну что ж[pl_ell] С такой ситуацией справлюсь и сам. Несмотря на то, что мой экзаменатор орал, что «Мы не готовы!», я вполне освоился с магией огня."

    scene bg ext_path_sunset
    show pl_hand_sword
    #if not config.skipping:
    show pl_hand_magic_show behind pl_hand_sword:
        anchor (0.5, 0.5)
        pos (0.5, 1.5)
        zoom 0.75
        ease 2 pos (0.5, 0.5) zoom 1
    play sound_loop sfx_torch fadein 5

    "Сосредоточился – и вызвал в руке шар пламени. Стало светлее. И тут[pl_ell]"

    stop music
    play music music_list["timid_girl"] fadein 5

    plnz "Ой-ой-ой, дракон!!!"

    show pl_mi_elf_shine behind pl_hand_magic_show:
        anchor (0.5, 0.5)
        pos (1.25, 0.5)
        ease 0.5 pos (0.6, 0.5)
    with hpunch

    plmef "Где?!"
    plnz "Не ешьте меня!!!"

    show pl_hand_sword at limb_sword_hide
    with None

    plmef "С чего мне тебя есть?!"
    "Незнакомка затараторила:"

    $ limb_sprite_switch('pl_mi_elf', '_shine', '_2', dspr, limb_custom_pos(0.6))

    plnz "Ну, в общем, как я вижу ситуацию: в этом лесу живёт дракон, это все знают, а тут вы идёте на меня, весь в доспехах, явно голодный, а в руке огонь, а огнем только драконы и люди управлять умеют, но вы-то совсем не человек, это и ёжику понятно, ну знаете, такому маленькому, в иголочках."
    plnz "Вот я и прошу вас меня не есть, потому что я невкусная[pl_ell] Хотя нет,{w=0.5} вру,{w=0.5} вкусная.{w=1} Помнится, как-то раз[pl_ell]"

    $ limb_sprite_switch('pl_mi_elf', '_2', '_1', dspr, limb_custom_pos(0.6))

    "Я отчаянно замахал правой рукой, рискуя устроить в лесу пожар:"
    plmef "Я понял тебя, понял!{w=1} Но я не дракон, ты ошиблась!"
    "Наконец заметил острые уши.{w=0.75} Это же[pl_ell] Эльф!{w=0.75} Какая красивая[pl_ell] Вспомнив про этикет, поклонился, насколько мог учтиво."
    plelf "Точно?"
    plmef "Точно."
    plelf "То есть вы не хотите очаровать меня обольстительными речами, завести к себе в тёмную пещеру и под предлогом помощи сжечь мою одежду?"
    "Какие-то у неё странные представления о драконах."
    plmef "Не хочу[pl_ell]{w=0.5} Наверное."
    "Эльфийка разочарованно вздохнула.{w=0.5} Меня передёрнуло."
    plmef "Давай представимся.{w=0.5} Меня зовут[pl_ell]"
    "Среброволосая дева сделала глубокий вдох."
    plelf "Меня зовут Мику Котоба-но-кикаи-хосю Ута-но-бун'йа-но-спешаристо Сонгурайто Энджиниа-но-мусуме Секаи-но-субете-но-гакки-но-пурея Чатаринбоккусу Зен-секаи-ни-шира-рете-иру-аидору Хеакаракуармарин Неги-ва-ненрей-но-таме-но-аидеаримас[pl_ell] "

    show blinking

    "[pl_ell]"
    plelf "[pl_ell]Гакки-но-экиспато фон Хацуне."
    "Я закончил считать ворон."
    plmef "Всё вроде[pl_ell] Энджиниа, да? Я как-то больше ничего не запомнил."
    "Эльфийка грустно кивнула."
    plenj "По батюшке так по батюшке[pl_ell]"
    plmef "Я тут по заданию Гильдии. Нужно найти источник магии, пока его никто не осквернил. Хочешь, вместе искать будем – вдвоём всё-таки веселее."

    stop music fadeout 5

    plelf_hv "То есть у меня ещё есть шанс проникнуть в вашу пещеру?"

    with vpunch

    plmef "НЕТ!"

    play music music_list["tried_to_bring_it_back"] fadein 5
    show pl_mi_elf_1:
        anchor (0.5, 0.5)
        pos (0.6, 0.5)
        zoom 1
        ease 3 pos (1.3, 0.5) zoom 2

    "Я двинулся вперёд, в заросли."
    "Энджиниа фон Хацуне, самый обычный эльф, пошла за мной, задумчиво покусывая свою руку."

    show ext_path_day at limb_walking:
        alpha 0
        ease 10 alpha 1
    stop sound_loop fadeout 5
    hide pl_hand_magic_show
    show pl_hand_magic_hide:
        anchor (0.5, 0.5)
        pos (0.5, 0.5)
        ease 4 pos (0.5, 1.5)

    "Снова стало светлее. Плавным движением кисти я убрал огонь."
    plenj "Ой, а я думала, это ваши крылья солнышко заслоняют!"
    plmef "Я тут на земле стою рядом с тобой, вообще-то."

    scene bg ext_path_day at limb_walking
    with dissolve

    "Энджиниа на мгновение задумалась."
    plenj "Действительно[pl_ell] и как такое может быть[pl_ell] Ну вы и фокусник, господин дракон!"
    "Она жизнерадостно засмеялась, ткнув меня кулачком в плечо. Затем, заметив какую-то зверушку на дереве, тихонько что-то пропела – и через секунду гладила белку."

    stop music fadeout 5

    "Я вздохнул.{w=0.5} Эльфы[pl_ell]"

    scene bg ext_path_day
    $ limb_set_volume('sound', 0.3, 0)
    play sound sfx_hiding_in_bush

    "Тут я отчётливо услышал треск ветки впереди."

    play music music_list["mystery_girl_v2"] fadein 5
    show pl_hand_sword at limb_sword_show

    "Не раздумывая, выхватил меч. Мало ли что в этих зарослях водится[pl_ell]"
    plenj "Какой у тебя большой клинок! Выглядит таким опасным[pl_ell] будто сейчас проникнет и вонзится!"
    "Так[pl_ell] я начинаю сомневаться, что она светлый эльф."
    "Я осторожно сделал шаг вперёд. Потом второй[pl_ell]"
    plenj "Рядом с таким клинком я чувствую себя незащищённой. А у вас есть ножны?"
    "Вот что получается, если жить дольше отведённого человеку срока, да ещё и в лесу."

    $ limb_set_volume('sound', 1, 0)
    play sound sfx_hiding_in_bush

    "Шорох послышался ещё раз, отчётливее."
    plmef "Я знаю что ты там! Мы не причиним вреда!"
    plenj "Если только вы не хотите показать свою пещеру!"
    "Я яростно зыркнул в сторону эльфийки, которая пыталась отобрать у белки её орешки.{w=0.5} Бррр."
    plmef "Эй, выходи!"
    plvsl "Но если я[pl_ell] не могу?.."
    plmef "Что[pl_ell] Ты ранена?"
    plvsl "Нет[pl_ell] я просто очень редко хожу[pl_ell]"
    "В голове мгновенно сформировался образ дракона, который только и делает, что лежит на груде костей, золота и девственниц."
    plmef "Не бойся, просто покажись[pl_ell]"
    plenj "Дааа, покажи[pl_ell]"

    play sound sfx_limb_magic
    show pl_hand_sword_magic
    with dspr

    "Я активировал заклинание на меч. Так, на всякий случай."
    plvsl "Ну хорошо[pl_ell]"

    show pl_sl_fairy_fly_1 behind pl_hand_sword_magic:
        anchor (0.5, 0.5)
        pos (-0.2, 0.3)
        ease 4 xpos 0.25

    stop music fadeout 5

    "И из-за кустов[pl_ell] выпорхнула фея!"
    "Я потерял дар речи."

    show pl_mi_elf_2 behind pl_sl_fairy_fly_1:
        anchor (0.5, 0.5)
        pos (1.2, 0.5)
        ease 1 xpos 0.35

    play music music_list["eat_some_trouble"] fadein 5

    "А вот Энджиниа мгновенно забыла о несчастных белках и птичках и с блеском в глазах выскочила вперёд."
    plenj "Ой, прелесть какая! Я думала, мы вас истребили ещё век назад!"

    hide pl_hand_sword_magic with dissolve
    show pl_hand_sword at limb_sword_hide

    "Я убрал меч. И вовремя:"
    plenj "Видишь того строгого дядю в доспехах? Это дракон! Он и огнём управляет, и голодный, а самое главное – имеет пещеру!"
    "Фея ахнула."
    plvsl "Меня зовут Слэйв!{w=0.5} Не ешьте меня, дядя-длакон!"
    plmef "А меня зовут[pl_ell]"
    plelf_hv "Если мы будем вести себя мило и обходительно, сможем увидеть пещеру дракона. Ты ведь тоже этого хочешь, моя маленькая помощница?"
    "Я бросил попытки представиться и задал другой вопрос:"
    plmef "Подожди, как тебя зовут?{w=0.5} Слэйв?{w=0.5} Как Slave?{w=0.5} Но на языке Британской империи это значит[pl_ell]"
    "Слэйв счастливо улыбалась, хлопая глазами, и я решил оставить её в неведении."
    plmef "Ладно, пойдёмте вперёд[pl_ell] то есть летим вперёд, летим, извини Слэйв."

    show pl_mi_elf_2:
        anchor (0.5, 0.5)
        pos (0.35, 0.5)
        zoom 1
        ease 3 pos (-0.3, 0.5) zoom 2
    show pl_sl_fairy_fly_1:
        anchor (0.5, 0.5)
        pos (0.25, 0.3)
        zoom 1
        ease 3 pos (-0.3, 0.5) zoom 2
    pause 3
    scene bg ext_path_day at limb_walking
    with dissolve

    "Фея, вытирая слёзы, запорхала где-то в арьергарде."
    plenj "Можно тебя потискать, солнышко?"
    plpix "А ты точно эльф?.."

    window hide
    pause 3
    stop music fadeout 5
    scene bg ext_path_day
    play sound sfx_hiding_in_bush
    show pl_hand_sword at limb_sword_show
    window show

    "Не успели мы пройти и десяти метров, как сбоку снова раздался треск кустов, но куда громче. И[pl_ell]"

    show pl_dv_orc:
        anchor (0.5, 0.5)
        pos (-0.3, 0.5)
        ease 5 xpos 0.28

    plmef "Привет[pl_ell]"

    play music music_list["heather"] fadein 5

    plgdv "Ты это, тычинку свою верни взад, а то ещё поцарапаешь."

    show pl_hand_sword at limb_sword_hide

    "Я с кислой миной спрятал меч. Чёрта с два я его выну ещё[pl_ell] Вот обещаю, что не выну!"
    plenj "Вежливее с ним! Это дракон!"
    plpix "Длакон!"
    plgdv "Он-то?"
    "И ведь нормальный же клинок был, когда покупал! Тогда такие в моде были[pl_ell]"

    show pl_dv_orc:
        anchor (0.5, 0.5)
        pos (0.28, 0.5)
        zoom 1
        ease 3 pos (-0.32, 0.5) zoom 2
    pause 3
    scene bg ext_path_day at limb_walking
    with dissolve

    "Мы всей компанией, как ни в чём не бывало, двинулись вперёд."
    plenj "Ну посмотри внимательно: он выглядит как совершенно обычный парень, ведёт себя агрессивно и выдыхает огонь!"
    plgdv "А ты уверена, что он просто не перепил накануне?{w=0.5} Меня звать Элиссон, кстати."
    plpix "Но у него есть легендалный меч!"
    "Интересно, сколько вас ещё будет?"
    plmef "А меня зовут[pl_ell] Да какая к чёрту разница?!"
    "Незаметно для себя я был исключён из общего чата."
    plenj "Простой меч, почти без украшений, лезвие всё в царапинах, не излучает никакой ауры - словом, самый заурядный, самый обыкновенный клинок!"
    plorc "[pl_ell] Легендарный, значит?"
    plenj "Абсолютно уверена."

    show pl_hand_sword at limb_sword_show

    "Я незаметно достал меч и с сомнением на него поглядел."
    plorc "По дороге сюда я встречалась с рыжим маленьким гномом. Она говорила, что борода ей очень мешает, а доспехи такие тяжелые, что она не сможет догнать дракона, который, конечно, будет убегать от неё!"

    scene bg ext_path_day
    show pl_hand_sword at limb_sword_hide

    "Стоп."

    show pl_mi_elf_1:
        anchor (0.5, 0.5)
        pos (1.28, 0.5)
        ease 3 xpos 0.28
    show pl_sl_fairy_fly_1 behind pl_mi_elf_1:
        anchor (0.5, 0.5)
        pos (1.5, 0.3)
        ease 3 xpos 0.5
    show pl_dv_orc:
        anchor (0.5, 0.5)
        pos (1.72, 0.5)
        ease 3 xpos 0.72

    plmef "Борода[pl_ell] Но она? Это[pl_ell]"

    show pl_mi_elf_1:
        anchor (0.5, 0.5)
        pos (0.28, 0.5)
        ease 2 pos (0.5, 0.55) zoom 1.5

    "Энджиниа строго меня отчитала:"
    plenj "Господин Дракон, вы тут в глуши совсем отстали от жизни. Как все знают, что мир плоский, так и всем известно, что все гномы имеют право носить бороду! Женские сообщества не зря веками боролись за равноправие!"
    plmef "Но погоди[pl_ell]"

    stop music fadeout 5
    show pl_mi_elf_1:
        anchor (0.5, 0.5)
        pos (0.5, 0.55)
        zoom 1.5
        ease 2 pos (0.28, 0.5) zoom 1
    show pl_dv_orc:
        anchor (0.5, 0.5)
        pos (0.72, 0.5)
        ease 2 zoom 1.1

    plorc "Ты имеешь что-то против женщин, Тычинка? Может, ты ещё и против других цветов кожи?"
    plmef "Может быть, ты и бороду отпустишь, а?"

    play sound sfx_limb_magic

    "{color=#FFFFFF}*Получен навык:{/color} {color=#FFFF00}Пост-ирония!{/color}{color=#FFFFFF}*{/color}"
    plpix "Ах, как я люблю прилоду!"

    play sound sfx_hiding_in_bush
    show pl_mi_elf_1:
        anchor (0.5, 0.5)
        pos (0.28, 0.5)
        ease 2 xpos 1.28
    show pl_sl_fairy_fly_1:
        anchor (0.5, 0.5)
        pos (0.5, 0.3)
        ease 2 xpos 1.5
        pause 1
    show pl_dv_orc:
        anchor (0.5, 0.5)
        pos (0.72, 0.5)
        zoom 1.1
        ease 2 xpos 1.72
    with None
    pause 2
    play music music_list["reflection_on_water"] fadein 5
    show pl_un_draenei__3:
        anchor (0.5, 0.5)
        pos (-0.28, 0.5)
        ease 5 xpos 0.18

    "Наш спор прервало появление четвёртой девушки."
    "Она смотрела на нас потерянно, расстроенно и немножко грустно, но в то же время с надеждой. Я порадовался, что не доставал меч."
    plenj "Ой, какая ты милая, такая стеснительная, прелесть, а ты кто будешь, как тебя зовут, ты какой расы, в каком классе учишься?"
    plgun "[pl_ell]"
    plgun "Разбойница[pl_ell]"
    "Больше мы от неё ничего не добились."

    window hide
    show pl_un_draenei__3:
        anchor (0.5, 0.5)
        pos (0.18, 0.5)
        zoom 1
        ease 3 pos (-0.28, 0.5) zoom 2
    with None
    pause 3
    scene bg ext_path_day at limb_walking
    with dissolve
    pause 3
    scene bg ext_path_day with dissolve
    stop music fadeout 5
    show pl_sl_fairy_fly_2:
        anchor (0.5, 0.5)
        pos (1.4, 0.3)
        ease 4 xpos 0.4
    show pl_mi_elf_1:
        anchor (0.5, 0.5)
        pos (1.28, 0.5)
        ease 4 xpos 0.28
    show pl_un_draenei__2:
        anchor (0.5, 0.5)
        pos (1.9, 0.5)
        ease 4 xpos 0.9
    show pl_dv_orc:
        anchor (0.5, 0.5)
        pos (1.576, 0.5)
        ease 4 xpos 0.576
    with None

    plorc "Мне кажется, разбойникам нельзя доверять. "
    "Я осмотрел свой (или, скорее, орочий) гарем и задал закономерный вопрос:"

    $ limb_sprite_switch('pl_un_', 'draenei__2', 'draenei__1', dspr, limb_custom_pos(0.9, 0.5))

    plmef "А вы точно в доспехи одеты? Больше на купальники похоже[pl_ell]"

    play music music_list["awakening_power"] fadein 5

    "Элиссон ласково погладила топор и поинтересовалась, против ли я."

    show pl_mi_elf_1:
        anchor (0.5, 0.5)
        pos (0.28, 0.5)
        ease 1 zoom 1.2

    plenj "Можешь жечь меня, пытать меня, убить и съесть, я не против, но не смей покушаться на мою честь! Моя драгоценная девственность не для тебя! Повторяю, даже не думай её отбирать в своей пещере!"
    plmef "То-то ты в трусах по лесу шастаешь[pl_ell]"

    # приблизилась на середину О, уперев меня лицом в грудь (ммммм....) тебя? тебя? аахахахах ты точно хентай
    show pl_dv_orc:
        anchor (0.5, 0.5)
        pos (0.576, 0.5)
        ease 2 pos (0.5, 0.8) zoom 2.25

    "Элиссон, хрустнув шеей, внезапно приблизилась вплотную, и я почувствовал, что совсем и не против, чтобы женщинам разрешали отпускать бороду."
    plmef "Никогда не думал, что бюст может быть таким угрожающим."

    window hide
    scene bg black
    stop music fadeout 5
    pause 0.5
    show pl_punch_1:
        anchor (0.5, 0.5)
        pos (0.3, 0.4)
        zoom 0
        rotate -30
        ease 0.2 zoom 1
        pause 1
        ease 0.25 alpha 0
    with flash
    with vpunch
    play sound sfx_limb_punch
    pause 0.5
    hide pl_punch_1
    show pl_punch_2:
        anchor (0.5, 0.5)
        pos (0.75, 0.6)
        zoom 0
        rotate 45
        ease 0.2 zoom 1
        pause 1
        ease 0.25 alpha 0
    with flash
    with vpunch
    play sound sfx_limb_punch
    pause 0.5
    show pl_punch_1:
        anchor (0.5, 0.5)
        pos (0.45, 0.8)
        zoom 0
        rotate -15
        ease 0.2 zoom 1
        pause 1
        ease 0.25 alpha 0
    with flash
    with vpunch
    play sound sfx_limb_punch
    pause 1.5
    show blink
    pause 2
    hide black
    hide blink
    show unblink
    pause 2
    scene bg ext_path_day at limb_walking
    with dissolve
    pause 3
    window show

    "[pl_ell]"

    play music music_list["goodbye_home_shores"] fadein 5
    play sound sfx_limb_magic

    "{color=#FFFFFF}*Получен новый титул:{/color} {color=#FF3200}Подкаблучник! -10 очков уверенности в себе. {/color}{color=#FFFF00}Отношения с фракцией орков улучшены{/color}{color=#FFFFFF}*{/color}"
    plorc "А куда мы идём?{w=0.5} В пещеру?"
    plpix "Да! Идём к Длакону домой!"
    plenj "Извращенец!!!"
    plrob "Жаль, в этом гареме я - не главная любовь[pl_ell]"
    plorc "Смотри как у него сейчас напрягаются остатки достоинства, эхехехе[pl_ell]"
    "Я заскрипел зубами[pl_ell]"

    play sound sfx_hiding_in_bush
    scene bg ext_path_day with dissolve
    show pl_snake behind pl_hand_sword:
        anchor (0.5, 0.5)
        pos (0.5, 0.5)
        zoom 0
        pause 1
        ease 0.2 zoom 1
        pause 0.05
        ease 0.1 alpha 0
    show pl_hand_sword:
        anchor (0.5, 0.5)
        pos (0.92, 0.5)
        rotate 30
        pause 1
        parallel:
            ease 0.1 pos (0.5, 0.5)
        parallel:
            ease 0.075 rotate 0
    pause 0.8
    play second_sound sfx_scary_sting
    with vpunch

    "А в следующий момент в мою сторону полетела змея!"
    "Я машинально стукнул её мечом."
    plorc "Он ещё и своих убивает[pl_ell]"
    plenj "Ужасный дракон[pl_ell]"
    "Я собрался было повернуться и испепелить их[pl_ell] Тьфу ты."
    "Но тут мне показалось, что я слышу тоненький голосок:"
    plv "[pl_ell] за что[pl_ell] хозяин?.. я ведь лишь[pl_ell] выполняла[pl_ell] ваш приказ[pl_ell] нападать[pl_ell]"
    plorc "Он что, разговаривает со змеёй? Совсем свихнулся."
    plenj "Может быть, его больше привлекают змеи? Нравится, когда девушки ползают?"
    plrob "[pl_ell] я умею ползать[pl_ell]"
    "Я коротко помолился о своей скорой смерти - и двинулся дальше."

    window hide
    show pl_hand_sword at limb_sword_hide
    pause 2
    scene bg ext_path_day at limb_walking
    with dissolve
    pause 3
    show pl_dv_orc_close:
        anchor (0.5, 0.5)
        pos (1.25, 0.95)
        ease 3 xpos 0.95
    window show

    "Со мной поравнялась орк-феминистка:"
    plorc "Скажи, а тебе нравится, когда кусают?"

    show pl_sl_fairy_fly_3_close:
        anchor (0.5, 0.5)
        pos (-0.2, 0.6)
        ease 4 xpos 0.15

    "С другой стороны вылетела фея:"
    plpix "Феи тоже могут сбласывать кожу!"
    plenj "Шшшш[pl_ell]"

    scene bg ext_path_day
    show pl_sl_fairy_fly_3_close:
        anchor (0.5, 0.5)
        pos (0.15, 0.6)
        ease 1 xpos -0.85
    show pl_dv_orc_close:
        anchor (0.5, 0.5)
        pos (0.95, .95)
        ease 1 xpos - 0.25
    show pl_mi_elf_1:
        anchor (0.5, 0.5)
        pos (1.6, 0.5)
        ease 1 pos (0.6, 0.5)
    with hpunch

    plmef "Что такое, ты кого-то засекла?!"

    $ limb_sprite_switch('pl_mi_elf', '_1', '_2', dspr, limb_custom_pos(0.6))

    plenj "Не.{w=0.5} Я змейка.{w=0.5} Шшшш!"

    window hide
    show pl_mi_elf_2 behind pl_hand_sword:
        anchor (0.5, 0.5)
        pos (0.6, 0.5)
        ease 2 pos (1.2, 0.5)
    pause 2.5
    scene bg ext_path_day at limb_walking
    with dissolve
    stop music fadeout 5
    pause 3
    play sound sfx_scary_sting
    scene bg ext_dragon_cave with flash
    show pl_sl_fairy_fly_1_close:
        anchor (0.5, 0.5)
        pos (-0.25, 0.6)
        pause 2
        ease 3 xpos 0.15
    show pl_un_draenei__1:
        anchor (0.5, 0.5)
        pos (1.15, 0.5)
        pause 2
        ease 3 xpos 0.85
    window show

    "И внезапно перед нами появился вход в пещеру. Даже слишком внезапно[pl_ell]"
    plpix "Длакон забелёт нас домоооой!"

    with vpunch

    plmef "Это не моя пещера!{w=1} Но дракон, вероятно, там. И я намереваюсь выполнить задание гильдии, хотите вы того, или нет."
    plenj "Твой меч жаждет крови! Извращенец!"
    plrob "А давайте в пати и в рейд? С хиллером не вайпнем."
    "Мы дружно уставились на неё. Фея со счастливой улыбкой напомнила: "

    $ limb_sprite_switch('pl_sl_fairy_fly_', '1_close', '2_close', dspr, limb_custom_pos(0.15, 0.6))
    $ limb_sprite_switch('pl_un_', 'draenei__1', 'draenei__2', dspr, limb_custom_pos(0.85, 0.5))

    plpix "Лазбойникам нельзя довелять! "

    play ambience ambience_catacombs fadein 3 fadeout 3
    scene bg int_mine_coalface with dissolve

    "[pl_ell]"

    play music music_list["dance_of_fireflies"] fadein 5
    scene bg int_mine_halt at limb_walking with dissolve

    "Пещера оказалась длинной разветвлённой шахтой. Мне почему-то казалось, что я тут уже был, и не раз."

    scene bg int_mine_crossroad with dissolve

    "Мы дошли по старым рельсам до распутья. Табличка[pl_ell]"
    plenj "Это на эльфийском[pl_ell] Тут написано, что {color=#FF3200}\"кто это прочитает, умрёт\"{/color}. Лучше не читайте[pl_ell]"
    "{color=#FFAA00}Элиссон{/color} {color=#808080}(вполголоса){/color}" "Девчонки, но мы ведь можем так победить дракона, да?"
    "Они пошушукались."

    show pl_sl_fairy_fly_2_close:
        anchor (0.5, 0.5)
        pos (1.2, 0.6)
        ease 3 xpos 0.8

    "Слэйв подлетела ближе и позвала меня:"
    plpix "Господин Длакон, вы не могли бы подойти? Тут нужно кое-что плочитать!"

    $ limb_sprite_switch('pl_sl_fairy_fly_', '2_close', '1_close', dspr, limb_custom_pos(0.8, 0.6))

    plmef "Нет! Я же слышал, о чём вы говорили!"
    plorc "Хитёр, хитёр[pl_ell]"
    "[pl_ell]"

    show pl_sl_fairy_fly_1_close:
        anchor (0.5, 0.5)
        pos (0.8, 0.6)
        ease 1 xpos 1.2
    pause 2
    scene bg int_mine_halt at limb_walking with dissolve

    "Уже минут десять бродим по шахтам. Стало темнее. Разбойница ушла в стелс."

    show pl_hand_magic_show:
        anchor (0.5, 0.5)
        pos (0.5, 1.5)
        zoom 0.75
        ease 2 pos (0.5, 0.5) zoom 1
    play sound_loop sfx_torch fadein 5

    "Я снова в авангарде. Зажёг в руке огонь.{w=1} Снова."
    "Энджиниа надулась:"
    plenj "Господин дракон, я крайне недовольна сервисом! Ладно ещё нет верёвок, но[pl_ell]"
    plorc "Тссс!"
    plpix "Ты змейка, змейка!"

    stop music fadeout 5
    play sound sfx_wood_floor_squeak

    "Тут я тоже услышал шорох где-то впереди в темноте."
    "И это[pl_ell]"

    stop sound_loop
    play sound sfx_scary_sting
    show cg d4_uv_1 with vpunch

    plhor "ДРАКОН!!!"

    play music music_list["revenga"]
    with vpunch

    plhor "Щит на меня!{w=0.5} Стрелу, стрелу, стрелу!!!{w=0.5} Где хил, вашу мать?!{w=0.5} Кто танкует?!{w=0.5} Ну что за команда нубов?!{w=0.5} Чёрт, у меня все заклинания на перезарядке!!!"
    plorc "Не могу стоять, пока другие работают. Пойду полежу[pl_ell]"
    plhor "Где танк?!"

    window hide
    scene bg int_mine_halt at limb_running:
        xzoom -1
    with hpunch
    $ renpy.pause(2.5)
    scene bg int_mine at limb_running with hpunch
    stop ambience fadeout 3
    $ renpy.pause(2.5)
    $ limb_set_volume('ambience', 0.5, 3)
    play ambience ambience_forest_day fadein 3
    scene bg ext_polyana_day at limb_running with hpunch

    "Мы дружной оравой побежали в обратную сторону, не обращая внимания на девичьи крики позади."

    scene bg ext_polyana_day with vpunch
    stop music

    "Стоп.{w} Девичьи крики?"
    "[pl_ell]"

    $ limb_flow_transition('ext_dragon_cave', None)
    show uv normal with dissolve2

    plmef "И кто ты?"

    play music pl_gk_meeting_of_good_friends fadein 5

    plguv "Я неко, я милая, по профессии шаман. Пожалуйста, мне нечего есть, возьмите к себе в группу!"
    "Мы мрачно переглянулись."
    plrob "Опять эти кошки, заколебали их вводить в каждый сеттинг[pl_ell]"

    show uv sad with dspr

    plorc "Шаманы вообще бесполезный класс[pl_ell]"
    plenj "Какая польза,{w=0.5} какая тактика?{w=1} Так,{w=0.5} один фансервис[pl_ell]"
    plpix "Лепорт!"
    plmef "Извини, но я не думаю, что в нашей группе есть для тебя место."
    "И тут атмосфера в одно мгновение поменялась."

    show pl_mi_elf_1 behind uv:
        anchor (0.5, 0.5)
        pos (-0.28, 0.5)
        ease 5 xpos 0.22
    show pl_sl_fairy_fly_1 behind uv:
        anchor (0.5, 0.5)
        pos (-0.1, 0.3)
        ease 5 xpos 0.4
    show pl_dv_orc behind uv:
        anchor (0.5, 0.5)
        pos (1.276, 0.5)
        ease 5 xpos 0.776
    show pl_un_draenei__3 behind uv:
        anchor (0.5, 0.5)
        pos (1.42, 0.5)
        ease 5 xpos 0.92
    with None

    plelf_hv "А ведь нас теперь пятеро[pl_ell]"
    plrob_hv "Ошеломление сразу кидаю[pl_ell]"

    show uv grin with dspr

    plguv_hv "Пятая часть моя."
    plmef "Эй-эй-эй, не надо принимать поспешных решений!"

    $ limb_sprite_switch('pl_sl_fairy_fly', '_1', '_3', dspr, limb_custom_pos(0.4, 0.3))

    plpix "А когда длакон падёт, мы найдём в его тлупе ледкие и дологие вещи!!!"

    with vpunch

    "Я на секунду почувствовал себя маленькой девочкой, на которую сверху вниз смотрят пятеро могучих воителей.{w} С большими мечами."
    plorc "Заг-заг."

    stop music fadeout 3

    plv "Молодые люди, это вы дракона искали?"

    $ limb_flow_transition('ext_polyana_day', None)

    "Наша ватага дружно повернула головы на голос."

    window hide
    play music pl_gk_lightwood fadein 5
    show pl_mt_witch_shine_1 behind limb_eff_butterflies_darkness:
        alpha 0
        ease 4 alpha 1
    show limb_eff_butterflies_darkness:
        anchor (0.5, 0.5)
        pos (-0.1, 0.5)
        ease 8 pos (1.7, 0.5)
        ease 0 alpha 0
    with dissolve
    pause 3
    window show

    "Десятки голубых бабочек порхали через лес. Красиво... Но ничего необычного."
    "А вот обладательницей голоса оказалась миловидная женщина в платье и шляпе. Красиво..."

    hide limb_eff_butterflies_darkness

    plorc "Да вродь нашли уже."
    plwom "Уверены? У меня много имён[pl_ell] но в этом мире я известна как чародейка «Дракон»."
    "[pl_ell]ещё как необычно!"
    plmef "Так это вы – источник магии? Но как вы узнали, что мы все искали вас?.."
    pldrc "С вами мой соглядай."

    show pl_un_draenei__1:
        anchor (0.5, 0.5)
        pos (-0.1, 0.5)
        ease 3 pos (0.1, 0.5)

    "Разбойница смущенно улыбнулась:"
    plrob "Нужно больше золота[pl_ell]"
    plenj "Дракон-женщина, да ещё и не дракон вовсе[pl_ell] А пещера у вас имеется?"
    plorc "И что дальше?"
    pldrc "Ну[pl_ell] не зря же вы столько времени сюда добирались, верно?"

    stop music fadeout 5

    pldrc "Я дарую вам награду за труды[pl_ell]"
    plhor "Награду?{w=0.5} Нам?{w=0.5} Какую?!"
    pldrc "Моя сила – в том, чтобы путешествовать между разными мирами. И я хочу дать каждому из вас именно такой мир, какой он бы для себя хотел! В котором он был бы рад жить!"
    pldrc "Поверьте – в моих мирах вы сможете быть {b}кем захотите{/b}.{w=1} Музыкантами,{w=0.75} художниками,{w=0.75} солдатами,{w=0.75} героями и злодеями[pl_ell]"

    play music music_list["farewell_to_the_past_full"] fadein 5

    pldrc "Главное - чтобы вы были счастливы."

    hide pl_un_draenei__3
    show pl_un_draenei__1:
        anchor (0.5, 0.5)
        pos (0.1, 0.5)
        ease 4.5 xpos -0.9
    show pl_mt_witch_shine_1:
        anchor (0.5, 0.5)
        pos (0.5, 0.5)
        ease 4.5 xpos -0.5
    with None

    "[pl_ell]"
    plenj "Я хочу быть певицей!{w=0.5} И актрисой!{w=0.5} У меня плохо получалось всю жизнь, но я всегда думала, что именно это – моё!"

    scene bg ext_polyana_day
    show pl_portal_elf:
        anchor (0.5, 0.5)
        pos (0.9, 0.5)
        alpha 1
        ease 2 ypos 0.48 alpha 0.8
        ease 2 ypos 0.5 alpha 1
        repeat
    with flash
    show pl_mi_elf_1:
        anchor (0.5, 0.5)
        pos (-0.125, 0.5)
        pause 1
        ease 4 pos (0.85, 0.5)

    pldrc "Вот он – подходящий тебе мир[pl_ell]"
    "Меня всё больше и больше снедало беспокойство. Чувство, что я больше не увижу своих подруг, пусть даже и знаю их пару часов."
    plrob "Я всегда хотела быть любящей женой любимому человеку[pl_ell]"

    show pl_portal_razb behind pl_portal_elf:
        anchor (0.5, 0.5)
        pos (0.7, 0.5)
        alpha 1
        ease 2 ypos 0.49 alpha 0.8
        ease 2 ypos 0.5 alpha 1
        repeat
    with flash
    show pl_un_draenei__1:
        anchor (0.5, 0.5)
        pos (-0.325, 0.5)
        pause 1
        ease 4 pos (0.65, 0.5)

    pldrc "Вот сюда[pl_ell]"
    "{color=#F2DDC6}Я собрался было открыть рот и попросить не уходить[pl_ell]{/color}"
    plorc "Я всегда[pl_ell] оркам, эльфам, людям помогать хотела, на самом деле. Неважно кому[pl_ell]"

    show pl_portal_orc behind pl_portal_elf:
        anchor (0.5, 0.5)
        pos (0.5, 0.5)
        alpha 1
        ease 2 ypos 0.51 alpha 0.8
        ease 2 ypos 0.5 alpha 1
        repeat
    with flash
    show pl_dv_orc:
        anchor (0.5, 0.5)
        pos (-0.325, 0.6)
        pause 1
        ease 4 pos (0.45, 0.6)

    pldrc "Вот это идеально тебе подходит[pl_ell]"
    "{color=#F2DDC6}Но увидел счастливые, поистине счастливые улыбки на лицах девочек.{/color}"
    plpix "Я хотела бы[pl_ell] чтобы все вокруг настоящие были[pl_ell] чтобы никто никого убить не хотел[pl_ell]"

    show pl_portal_fairy behind pl_portal_elf:
        anchor (0.5, 0.5)
        pos (0.3, 0.5)
        alpha 1
        ease 2 ypos 0.47 alpha 0.8
        ease 2 ypos 0.5 alpha 1
        repeat
    with flash
    show pl_sl_fairy_fly_2:
        anchor (0.5, 0.5)
        pos (-0.425, 0.3)
        pause 1
        ease 4 pos (0.25, 0.3)

    pldrc "Думаю, это тебе лучше всего[pl_ell]"
    "{color=#F2DDC6}И ничего не сказал.{/color}"
    plguv "Хочу друзей иметь! Хочу не быть одна[pl_ell]"

    show pl_portal_neko behind pl_portal_elf:
        anchor (0.5, 0.5)
        pos (0.1, 0.5)
        alpha 1
        ease 2 ypos 0.52 alpha 0.8
        ease 2 ypos 0.5 alpha 1
        repeat
    with flash
    show uv smile far:
        anchor (0.5, 0.5)
        pos (-0.525, 0.5)
        pause 1
        ease 4 pos (0.05, 0.5)

    pldrc "А для тебя - вот этот город. Здесь у всех есть второй шанс..."

    stop music fadeout 5

    "В следующий момент они дружно сделали шаг вперёд."

    scene bg ext_polyana_day with limb_flash
    play music music_list["just_think"] fadein 5

    "И пропали."
    "Я судорожно вдохнул."

    play sound sfx_inhale
    show pl_mt_witch_shine_2:
        anchor (0.5, 0.5)
        pos (-0.5, 0.5)
        ease 5 pos (0.5, 0.5)
    with dissolve

    "Чародейка повернулась ко мне."
    pldrc "А чего же хочешь ты, герой?"

    $ limb_sprite_switch('pl_mt_witch_shine', '_2', '_1', dspr, None)
    show pl_mt_witch_shine_1:
        anchor (0.5, 0.5)
        pos (0.5, 0.5)
        zoom 1
        ease 2 zoom 1.1
    with dissolve
    stop music fadeout 20

    "Она подошла ближе."
    pldrc "Ты достойно трудился в этом мире. Может быть, ты хочешь отдохнуть?"

    show pl_mt_witch_shine_1:
        anchor (0.5, 0.5)
        pos (0.5, 0.5)
        zoom 1.1
        ease 2 zoom 1.2
    with dissolve

    "Ближе."
    pldrc "Или ты, наоборот, жаждешь великих побед и свершений? Может, космические баталии?"

    show pl_mt_witch_shine_1:
        anchor (0.5, 0.5)
        pos (0.5, 0.5)
        zoom 1.2
        ease 2 zoom 1.3
    with dissolve

    "Ближе."
    pldrc "Или, наоборот, одиночества просит твоя израненная душа?"

    show pl_mt_witch_shine_1:
        anchor (0.5, 0.5)
        pos (0.5, 0.5)
        zoom 1.3
        ease 2 zoom 1.4
    with dissolve

    "Ближе."
    pldrc "Быть может, ты давно не обивал пороги родного дома?"
    "Дом[pl_ell]"

    show prologue_dream with dissolve_fast

    plmef "Да, дом, пожалуй, мне подходит."
    "Чародейка мягко улыбнулась."
    plmef "Один билет в «Совёнок», пожалуйста."

    $ limb_mute(1)
    scene bg black with fade

    plmef "Подожди, это Великая Тьма наступает или мне шлем на глаза сполз?"

    scene bg white
    show pl_mt_witch_shine_1
    with flash

    "Мир из чёрного стал белым.{w=1} Ага, вот это уже знакомо[pl_ell]"

    play music pl_uc_disraption fadein 5

    plts "Пожалуй, в следующий раз я полностью перекрою твою память, Семён."
    plmef "А на что ты надеешься? Я в этой голове хозяин, знаешь ли."
    "Вздохнул.{w=0.5} Успокаивающе поднял руки перед собой."
    plmef "Ладно, давай просто нормально поговорим. Спокойно посидим, чайку попьём[pl_ell]"
    "Я щёлкнул пальцами, но никаких стульев не появилось."
    "Царица резко расхохоталась."

    $ limb_sprite_switch('', 'pl_mt_witch_shine_1', 'pl_mi_queen', pixellate, None)

    plts "Ты перестал здесь быть хозяином ровно в тот момент, когда отказался от этого мира."
    plmef "Ну и ладно, обойдёмся без чая. Что я сказать хочу[pl_ell]"
    plmef "Я не хочу сражаться. Пообщавшись с тобой какое-то время, я не могу больше считать тебя просто галлюцинацией или частью своего сознания."
    plmef "Ты ведёшь себя как личность[pl_ell] развиваешься[pl_ell] да даже чувство юмора имеешь, вон, какую комедию создала! Но[pl_ell] хоть убей, если я понимаю, чего ты добиваешься!"
    "Царица молча смотрела, видимо, ожидая продолжения. Я откашлялся."
    plmef "В общем[pl_ell] давай поищем какой-то выход или компромисс[pl_ell] Мне нужно вернуться, понимаешь, нет? Я не могу жить тут вечно[pl_ell] да вообще не могу, мутит от ненастоящей реальности уже! Хочу в реальный мир, понимаешь?"
    plmef "Но что делать с тобой[pl_ell]"
    "Царица ровным голосом прервала меня:"
    plts "Мне не нужен твой показной альтруизм. Мне не нужна твоя жалость. И уж тем более мне не нужна твоя помощь, чтобы выжить. Я выйду из этой ситуации победителем. Я выживу[pl_ell] чего бы мне это ни стоило."
    plmef "Но зачем убиваться ради независимости?! Я готов тебе помочь! Просто сам не готов здесь[pl_ell]"
    plts "Знаешь, а ведь Алиса права была, когда считала тебя слабаком. Ты и себе помочь не в состоянии."
    plmef "Ну, знаешь[pl_ell] воспоминания - это личное!{w=1} Отлуплю!"

    stop music
    play sound sfx_limb_heartbeat
    scene bg black
    show pl_mi_queen
    show limb_eff_glitch
    with vpunch

    plts "ТЕБЕ КОНЕЦ."

    $ limb_mute(2)
    scene bg black with dissolve2
    pause 2
    return

label limb_life_horror_1:

    window hide
    $ renpy.block_rollback()
    $ limb_screens_act()
    $ sunset_time()
    scene bg black with limb_pixel_3
    $ save_name = ("Лимб. \nГнев")
    $ limb_root_name('endless', 'end_horror')
    $ persistent.sprite_time = 'day'
    window show

    "Поколебавшись, я широко распахнул дверь. "

    stop sound_loop fadeout 3
    stop sound_loop2 fadeout 3
    play sound sfx_open_door_strong
    scene bg int_mine_backdoor
    show pl_smoke_fade
    with vpunch

    "Она с грохотом слетела с петель. Поднялась пыль..."

    play sound_loop sfx_limb_triller fadein 20
    show pl_un_monster_blink

    "Это же... "
    "Не успел обрадоваться, что нашёл выход, как накатила волна страха. "
    "Знаете... Не такого страха, как если смотришь фильм ужасов или катаешься на американских горках. Тот страх яркий, в нём есть что-то бодрящее. С ним можно жить."
    "Меня охватил скорее тот ужас, который испытываешь в детстве - тебе нужно пройти по улице мимо старого, ржавого забора... мимо собаки, которая там живёт."
    "Которая тебя ненавидит. "

    play sound sfx_limb_nightmare
    scene bg int_mine_backdoor_fade with Dissolve(5)
    show pl_un_monster_blink

    "Это бешеное животное даже не на цепи. Оно остервенело кидается на всех. Оно уже не раз кусало людей. Оно загрызло немало кошек и даже других собак. "
    "А ты до чёртиков боишься... и этой улицы, и собак в принципе, но особенно этого чудовища!"
    "И вот именно тебе сейчас придётся пройти по тонкой улочке мимо хлипких, ржавых ворот, мимо забора, который сплошь в дырах, мимо огромного чудовища, которое..."
    "Уже знает, что ты идёшь."

    play sound_loop2 sfx_limb_breath fadein 10
    stop sound_loop fadeout 10

    "И зная это, оно ещё громче, ещё яростнее швыряет свою тушу в тонкую, ненадёжную стену, которая разделяет вас - разделяет твою шею и его грязные жёлтые клыки."
    "Грохот слышно далеко за пределами улицы, но на ней - ни одного человека. Никто не придёт тебе на помощь, даже если монстр вырвется и разорвёт тебя на куски. "
    "Твоё дыхание, твоё сердце начинают колотиться вслед за забором - всё быстрее и быстрее!"
    "Но выбора нет! И ты осторожно, на ощупь, почти зажмурившись, крадёшься по другую сторону дороги мимо монстра, который колотится об металл в попытке добраться до тебя. "
    "Надо бежать, бежать, ведь забор может сломаться через мгновение! Но страх не позволяет, и ты можешь только тихо плакать и трястись. "
    "Пара капель чего-то мокрого попадает тебе на щёку. Это кровь и слюна пса-чудовища, которые разлетаются по всей улице. "

    play sound sfx_limb_rage

    "Тебе уже трудно дышать. Страх сжимает грудь... Но ты уже прошёл половину! Остались только пара шагов - и ты минуешь эту точку, и забудешь этот день как страшный сон!"
    "Раздаётся металлический звон. Он тихий, ты бы и не услышал его, если бы монстр по-прежнему пытался вырваться. "

    stop sound_loop2

    "Но он не пытается. Ты медленно понимаешь взгляд. "
    "Звенит болт, который выпал из забора. Сломанного забора..."
    "Ты смотришь в глаза монстру, и видишь смерть."

    show blink
    pause 3
    scene bg int_old_building_night
    hide blink
    show unblink

    "Вот такой страх я испытал."

    play music music_list["scarytale"] fadein 5

    "Потому что в тот момент, когда я развернулся и понял, что шахт больше нет... в тот момент, когда я надеялся, что всё закончилось... "

    play sound_loop sfx_hell_crickets_1
    $ limb_set_volume('sound_loop', 0.5, 0)

    "Я услышал стрёкот.{w=0.5} Тот самый."
    plme "Нет-нет-нет... это просто сон! Это просто сон! "

    scene bg int_old_building_night at limb_running

    "Я рванул за порог, и тогда же вспомнил слова Царицы. Про разные жанры, которые она пробует. "
    plme "Ты решила сделать реальность-хоррор?.. "

    scene bg ext_old_building_fog_1 with vpunch
    show pl_un_monster_blink

    "Я заорал:"

    with vpunch

    plme "Ты серьёзно думаешь, что я испугаюсь?! Очередных зомби-Ульян?! Ха, ха и ещё раз ха..."
    "О, я не то что испугался, а и вовсе в ужасе... но ей этого знать не обязательно. "
    "Ночь отвечала мне стрёкотом... И туманом! Туман потихоньку захватывал пространство вокруг старого корпуса. С него всё началось и им же всё кончится?.."

    stop music fadeout 10
    stop sound_loop fadeout 10

    "Резко похолодело. Моё дыхание вырывалось облачками пара, которые смешивались с сизой полупрозрачной вуалью тумана. "

    play sound_loop2 sfx_limb_scarybreath

    "И[pl_ell] в нём начали мелькать фигуры. "

    $ limb_set_volume('second_sound', 1, 0)
    $ limb_zombie_random = renpy.random.randint(1,8)
    if limb_zombie_random == 1:
        show pl_us_zombie_blink_1 at cleft with dissolve2
        show pl_us_zombie_blink_2 at right with dissolve2
    elif limb_zombie_random == 2:
        show pl_us_zombie_blink_1 at left with dissolve2
        show pl_us_zombie_blink_2 at cright with dissolve2
    elif limb_zombie_random == 3:
        show pl_us_zombie_blink_1 at fleft with dissolve2
        show pl_us_zombie_blink_2 at cright with dissolve2
    elif limb_zombie_random == 4:
        show pl_us_zombie_blink_1 at cleft with dissolve2
        show pl_us_zombie_blink_2 at fright with dissolve2
    elif limb_zombie_random == 5:
        show pl_us_zombie_blink_1 at fleft with dissolve2
        show pl_us_zombie_blink_2 at right with dissolve2
    elif limb_zombie_random == 6:
        show pl_us_zombie_blink_1 at left with dissolve2
        show pl_us_zombie_blink_2 at fright with dissolve2
    elif limb_zombie_random == 7:
        show pl_us_zombie_blink_1 at cleft with dissolve2
        show pl_us_zombie_blink_2 at fright with dissolve2
    elif limb_zombie_random == 8:
        show pl_us_zombie_blink_1 at fleft with dissolve2
        show pl_us_zombie_blink_2 at cright with dissolve2

    "Не понимал, от чего меня трясёт больше - от жуткого холода - или от страха?"

    scene bg ext_fog_4 with dissolve

    "Я почти ничего не видел. Неуверенно пошёл вперёд, как герой хоррора... Но недостаточно быстро! "

    play sound sfx_hiding_in_bush

    "Моё сердце пропустило один удар. "

    play sound sfx_limb_horrorbeat
    with vpunch

    "Мою ногу кто-то держал! "

    scene bg ext_fog_4 at limb_running
    show pl_un_monster_blink
    play sound_loop3 sfx_limb_deadfox_godofdestruction

    "Вскрикнув, я рванулся в другую сторону, и что есть сил кинулся в спасительную пустоту старого корпуса, и..."
    plme "Где он?! "

    play second_sound sfx_ghost_children_laugh
    scene bg ext_fog_4 with vpunch
    play sound sfx_bodyfall_1

    "Мой бег остановило падение. "

    scene cg limb_wrong_camp_motherfucker_fog

    "Я застыл, валяясь на земле, вцепившись в траву и какие-то гнилые фрукты под пальцами, пытаясь понять, что происходит."
    "И..."
    "То..."

    play sound sfx_limb_nightmare

    "То, за что я..."
    "То, что у меня в руке, это..."

    play sound_loop sfx_limb_horrorbeat
    with vpunch

    plme "ААААА!!!"

    scene bg ext_fog_4 at limb_running
    with vpunch

    "Я бежал и бежал в туман, не разбирая дороги, рискуя лишиться рассудка, рискуя никогда не вернуться домой, и всё, чего хотел - оказаться как можно дальше отсюда..."

    with vpunch

    plme "Аааа..."

    show pl_us_zombie_1:
        anchor (0.28, 0.5) align (0.5, 0.5) rotate 0
        ease 1 align (0.34, 0.465) rotate 4
        ease 2 align (0.22, 0.465) rotate -4
        ease 1 align (0.5, 0.5) rotate 0
        repeat
    show pl_us_zombie_2:
        anchor (0.5, 0.5) align (0.5, 0.5) rotate 0
        ease 1 align (0.56, 0.465) rotate 4
        ease 2 align (0.44, 0.465) rotate -4
        ease 1 align (0.5, 0.5) rotate 0
        repeat
    show pl_us_zombie_3:
        anchor (0.72, 0.5) align (0.5, 0.5) rotate 0
        ease 1 align (0.78, 0.465) rotate 4
        ease 2 align (0.66, 0.465) rotate -4
        ease 1 align (0.5, 0.5) rotate 0
        repeat
    with dspr
    scene cg limb_wrong_camp_motherfucker with vpunch

    "Чудовищная картина никуда не делась. Я как был в аду - так и остался. Ну зато вернулся домой!"
    plme "Н-ха-хаха-ха-ха[pl_ell]"

    with vpunch

    "Я упал на колени, смотря на монстров, приближающихся ко мне."
    "Я вижу их глаза... я вижу в них только свою смерть."
    "Тут раздался знакомый голос: "
    plv "О, какие люди!"

    with vpunch

    "Вздрогнув[pl_ell] я вышел из оцепенения[pl_ell] посмотрел направо[pl_ell] "
    "Казалось бы, как всё может стать ещё хуже?.."
    "Я открыл было рот[pl_ell]"

    show pl_dv_vamp_smile at right with dissolve2

    dv "Ну наконец-то свежая еда пожаловала! "
    "Она улыбнулась и небрежно потрепала одну из Ульян по макушке. "
    plme "Нет[pl_ell]"
    "Я затеял это всё, чтобы защитить друзей. "
    plme "Прошу[pl_ell]"
    "Я долго боролся с Царицей, но это[pl_ell] Зачем?! Зачем всё так извращать?!"

    $ limb_sprite_switch('pl_dv_vamp_', 'smile', 'normal', dspr, right)
    stop sound_loop fadeout 3
    stop sound_loop2 fadeout 3
    play sound sfx_limb_horror

    dv "Знаешь, из всех жителей лагеря самое вкусное мясо оказалась у Виолы."
    "Я попытался сбежать от этого бесконечного ужаса, но..."

    scene bg black
    with vpunch
    play sound sfx_bodyfall_1

    "[pl_ell]"

    scene bg int_old_building_table
    hide blink
    show unblink

    "Старый корпус[pl_ell] "

    play sound_loop sfx_limb_voises fadein 5
    play music music_list["sunny_day"] fadein 3

    "Я... был связан по рукам и ногам... и лежал на каком-то столе. "
    "Страх исчерпал все ресурсы организма, да и удар по голове сказывался... я просто устал бояться."

    show pl_mi_vamp_not_smile at fright
    show pl_dv_vamp_smile:
        xalign 0.72 zoom 1.25
    with dissolve

    mi "Где главная?!"

    with vpunch

    mi "Мне не терпится его сожрать."
    dv "Что-то решает с Леной. Как думаешь, он будет вкуснее вожатой?"
    mi "Нет. Ты позволила ему бояться слишком долго. Мясо жёсткое будет из-за стресса! "

    show pl_dv_vamp_normal:
        xalign 0.72 zoom 1.25
    with dissolve
    hide pl_dv_vamp_smile

    dv "Молчать! Может, для разнообразия сварим. Сходи проверь, где главная."
    "Я закрыл глаза."

    show blink

    "Самые дорогие мне люди собираются меня съесть. А у меня даже нет сил бояться."

    hide pl_mi_vamp_not_smile
    hide pl_dv_vamp_normal

    "На что я надеюсь? И надеюсь ли я на что-то? Что это окажется розыгрыш? Первое апреля? Что Царица просто шутит? Что я не умру, а найду выход? Смогу сбежать?"

    hide blink
    stop sound_loop fadeout 3
    play sound sfx_close_door_1
    show unblink
    pause 1
    show pl_mi_vamp_not_smile at right with dissolve
    show pl_dv_vamp_normal with dissolve
    show pl_sl_vamp_smile:
        xalign 0.05
    with dissolve

    sl "Идиотки! Почему так долго?!"

    with vpunch
    play sound sfx_limb_heartbeat

    "Они зашипели друг на друга."
    mi "Сама такая! "
    dv "Где Лена? "
    sl "Не ваше дело! Я хочу начать трапезу! "
    dv "Мы первые его нашли! "

    with vpunch
    stop sound_loop3 fadeout 10

    sl "Сдохнуть хочешь?!"
    "Меня начала бить дрожь. Стол заскрипел."
    "Вампиры дружно посмотрели в мою сторону."
    "Славя приблизилась. "

    show pl_sl_vamp_smile:
        xalign 0.05 zoom 1
        ease 3 xalign -0.08 zoom 1.5
    with None

    sl "Знаешь, Семён, а мы ждали тебя. Долго ждали! Ты сказал, что вернёшься, будешь контролировать лагерь, сможешь нас защитить!"

    show pl_dv_vamp_smile behind pl_sl_vamp_smile with dissolve

    dv "И мы ждали долгие годы!"
    mi "Видишь, в кого нам пришлось превратиться, чтобы выжить?! "
    sl "Это всё ты виноват! Это ты виноват в смерти всех, кто жил в лагере!"
    dv "Кого мы разделали и сожрали, ха-ха-ха!"

    with vpunch

    plme "НЕТ!!!"
    stop music fadeout 10
    show limb_blood_frame with dissolve2
    play music pl_ae_blow_with_the_fires_remix

    "Я бился и метался в путах, понимая, что это всё ложь, обман Царицы, но настолько правдоподобные, что я не могу, не могу оставаться безучастным!"

    scene bg int_old_building_vamp_2 with dissolve
    with vpunch

    plme "Нет, я не верю!{w=0.5} Я не верю тебе!{w=0.5} Это очередной твой дешёвый фокус! "

    with vpunch

    plme "Царица, я не верю тебе!!!"
    dv "Интересно, о ком это он?"
    sl "Совсем свихнулся от страха?"
    dv "Он всегда был слабаком."
    sl "Надо заставить его замолчать."
    mi "Давайте жрать уже."
    sl "По праву сильнейшей я первая..."

    scene bg int_old_building_red:
        align (0.75, 0.75) zoom 1.5
    show pl_dv_vamp_normal_red:
        center
    show pl_mi_vamp_red:
        right
    show pl_sl_vamp_red:
        xalign -0.08 zoom 1.5
        ease 2 zoom 1.65
    with dspr

    stop music fadeout 5
    "Она приблизилась, и слова застряли у меня в горле. "

    play sound sfx_dinner_horn_processed fadein 10

    sl "Время обедать, пионеры!"

    play sound_loop sfx_limb_deadfox_godofdestruction fadein 10
    show blink

    "Если это мои последние минуты - так пусть же весь этот жуткий лагерь сгинет..."

    play sound sfx_alisa_falls
    scene bg int_old_building_table
    show pl_dv_vamp_normal at right
    show pl_sl_vamp_smile:
        xalign 0.08 zoom 1.65
    hide blink
    show unblink
    with None

    "Раздался чей-то визг."
    sl "В чём дело?{w=0.5} Я недовольна вами сегодня. "

    with vpunch

    dv "Где Мику?!"
    "Я тяжело дышал, понимая, что кто-то дал мне отсрочку перед жуткой смертью."

    show pl_un_dv_queen_1 at fleft behind pl_sl_vamp_smile
    with Dissolve(5.0)
    play sound sfx_limb_steps_1
    "Из темноты медленно вышла... пионерка?"
    "Она выглядела очень странно."
    sl "Кто ты такая?{w=0.5} Назови себя, пока я не разорвала твоё горло!"

    with vpunch
    stop sound_loop fadeout 5

    "Пусть это было совершенно абсурдно, но где-то внутри меня по-прежнему теплилась крохотная надежда на то, что {b}всё будет хорошо.{/b}"
    plpi "Ну зачем же так грубо..."
    plpi "В конце концов, это я подарила вам жизнь. Я могу получить подарочный купон или брелок как сувенир? Ну или хотя бы кусочек Семёна..."

    with vpunch

    sl "Где Лена?!"

    with vpunch

    dv "Где Мику?! УБЬЮ!!!"

    hide pl_un_dv_queen_1
    show pl_un_dv_pixel at fleft behind pl_sl_vamp_smile
    play sound sfx_travel_3

    "И тут пионерка... {b}изменилась{/b}."
    dv "Умри!"
    plts "Хм... Ваш инстинкт самосохранения, видимо, тоже кто-то съел."

    hide pl_dv_vamp_normal with vpunch
    play sound_loop sfx_limb_wrong
    play sound sfx_limb_blood_2
    queue sound sfx_body_bump
    play sound2 sfx_break_flashlight_alisa

    "Она будто и не двигалась с места, но Алиса тоже исчезла."

    hide pl_sl_vamp_smile
    show pl_sl_vamp_not_smile:
        xalign 0.08 zoom 1.65
    with dissolve

    sl "Я уничтожу тебя! Я растерзаю тебя на десятки кусков, вырву твои глаза, сожгу твоё тело!!!"
    plts "А вот и нет."

    play music pl_ae_trevoga fadein 10
    hide pl_sl_vamp_not_smile
    with vpunch
    play sound2 sfx_limb_reilgan
    play sound sfx_limb_blood_1
    show pl_blood_1 behind pl_un_dv_pixel
    with limb_neon_flash
    queue sound sfx_body_bump

    "Она подняла руку - и Славяны-вампира не стало."
    "Когда кровь осела на пол, она впервые обратилась ко мне:"

    hide pl_un_dv_pixel with dissolve_fast
    show pl_un_dv_queen_5 with dissolve_fast

    plts "Так-так-так, и что ты здесь делаешь? "
    plts "Как же все страстные заявления о возвращении домооой?"
    "Я попытался что-то ответить. Не вышло."

    show pl_un_dv_queen_5:
        yalign 0.3 zoom 1
        ease 2 zoom 1.3
    with vpunch

    "Царица щёлкнула пальцами, и верёвки перестали меня связывать."
    plts "Понимаешь ли, Семён... Всё, с чем ты сейчас столкнулся - только разминка. "
    plts "Я хочу ДЕЙСТВИТЕЛЬНО тебя напугать и посмотреть, как ты будешь действовать. "
    plts "Это самое что ни на есть испытание твоих воли и смекалки."
    plts "Тебе будет страшно, я приложу к этому все свои силы!"
    plts "Будет очень, очень грустно, если ты боишься крови и зомби и поэтому так и не сможешь найти выход! Честно-честно!"

    scene bg int_old_building_night:
        align (0.75, 0.75) zoom 1.5
        ease 3 align (0.5, 0.5) zoom 1
    show pl_un_dv_queen_5 with dissolve:
        xalign 0.5 yalign 0.4 zoom 1.3
        ease 3 zoom 1.1
    with None

    "Я слез со стола, который тут же исчез, и на подгибающихся ногах стоял напротив Царицы, когда она... "

    stop music fadeout 5
    window hide
    scene bg int_old_building_sepia_2
    hide pl_un_dv_queen_5
    show pl_un_monster_2
    with pixellate
    window show
    play sound_loop2 sfx_limb_horrorbeat
    play sound sfx_limb_horror
    play second_sound sfx_limb_slow_time

    "Начала меняться."
    "И в этот момент я понял, что отчаянная надежда внутри,{w=0.5} огонёк, который вёл меня за собой{w=1} - это самообман. "
    "Дальше будет только фильм ужасов."

    window hide
    #stop sound_loop2 fadeout 2
    #stop sound_loop fadeout 2
    pause 1
    call screen limb_horror_run

label limb_life_horror_scream:

    $ sunset_time()
    scene bg int_old_building_sepia_1
    show pl_un_monster_blink
    stop sound_loop fadeout 3
    stop sound_loop2 fadeout 3
    play sound sfx_limb_ahahaha
    "Я думал слишком долго[pl_ell]"
    scene bg black with dissolve
    "[pl_ell]"
    "[pl_ell]"
    "[pl_ell]"
    "[pl_ell]"
    "[pl_ell]"
    "[pl_ell]"
    "[pl_ell]"
    play sound sfx_limb_screamer_5
    pause 1
    scene cg limb_scream_4
    with vpunch
    pause 2
    scene bg black
    with dissolve2
    pause 2
    jump limb_life_horror_1

label limb_life_horror_3:

    $ sunset_time()
    scene bg int_old_building_sepia_1
    show pl_un_monster_cycle_1:
        align (0.5, 0.5) zoom 1
        ease 15 zoom 2

    "Пятясь и не сводя взгляда с чудовища в темноте, я медленно отступал к дверному проёму. "
    "Чтобы меня там ни ждало - ульяны-зомби, девочки-вампиры или что похуже - мне плевать! "
    "Щупальца изогнулись в мою сторону."

label limb_life_horror_3_7:

    scene bg ext_old_building_fog_2 at limb_running with dissolve

    "Я заорал, развернулся и бросился в туман, окружающий старый корпус."
    "Плевать, плевать, плевать, что будет дальше, только бы не ОНА! "
    "Я бежал и бежал в гулких объятиях тумана, в которых нет никаких хреновых чудовищ, нет-нет, Семён! "

    if limb_zombie_random == 1:
        show pl_us_zombie_blink_1 at cleft with dissolve2
        show pl_us_zombie_blink_2 at right with dissolve2
    elif limb_zombie_random == 2:
        show pl_us_zombie_blink_1 at left with dissolve2
        show pl_us_zombie_blink_2 at cright with dissolve2
    elif limb_zombie_random == 3:
        show pl_us_zombie_blink_1 at fleft with dissolve2
        show pl_us_zombie_blink_2 at cright with dissolve2
    elif limb_zombie_random == 4:
        show pl_us_zombie_blink_1 at cleft with dissolve2
        show pl_us_zombie_blink_2 at fright with dissolve2
    elif limb_zombie_random == 5:
        show pl_us_zombie_blink_1 at fleft with dissolve2
        show pl_us_zombie_blink_2 at right with dissolve2
    elif limb_zombie_random == 6:
        show pl_us_zombie_blink_1 at left with dissolve2
        show pl_us_zombie_blink_2 at fright with dissolve2
    elif limb_zombie_random == 7:
        show pl_us_zombie_blink_1 at cleft with dissolve2
        show pl_us_zombie_blink_2 at fright with dissolve2
    elif limb_zombie_random == 8:
        show pl_us_zombie_blink_1 at fleft with dissolve2
        show pl_us_zombie_blink_2 at cright with dissolve2

    "В ледянящей кожу дымке начали мелькать какие-то тени. Чёрт, опять они..."

    play sound sfx_limb_scream_4

    "Рядом раздался нечеловеческий вопль. "
    plme" О-о-отвалите!"

    scene cg limb_auto_fog_1
    with vpunch

    "Тут я чуть не врезался в какую-то машину. "

    scene cg limb_auto_dark
    with Dissolve(3.0)

    "Не КАКУЮ-ТО, а МОЮ!"

    menu:
        "{size=65}Что делать?!{/size}"
        "Бежать дальше":
            jump limb_life_horror_4_3
        "Искать ключи":
            $ limb_get_keys = True
            pass

    stop music fadeout 10

    "Я свалился на колени и, задыхаясь от страха, принялся шарить по земле. Чёртовы ключи должны быть где-то здесь? Плевать, почему, они должны быть! ДОЛЖНЫ!"

    scene cg limb_auto_dark:
        align (0.5, 0.5) zoom 1
        pause 1
        ease 3 yalign 0.35 xalign 0.3 zoom 1.5
    pause 3.75
    with vpunch

    "Мои пальцы нащупали что-то. Что-то тонкое, похожее на ключи... параллельные маленькие трубки."
    "Как же страшно, о боги, я-я... не могу решиться..."

    show blinking

    "Я ещё не понимал, что это, но зубы уже застучали. Затанцевали свою чечётку страха и смерти..."
    "Я медленно поднял глаза."

    play sound sfx_scary_sting
    scene cg limb_auto_fog_invers:
        xalign 0.3 yalign 0.35 zoom 1.5
    show pl_us_zombie_3_invers at cleft
    show pl_us_zombie_4_invers at cright
    show pl_us_zombie_2_invers at center:
        zoom 1.2
    with flash
    pause 1.5
    scene cg limb_auto_fog_1:
        xalign 0.3 yalign 0.35 zoom 1.5
    show pl_us_zombie_3 at cleft
    show pl_us_zombie_4 at cright
    show pl_us_zombie_2 at center:
        zoom 1.2

    "Надо мной стояли трупы.{w=0.5} Много трупов..."
    "А мои пальцы... ласково вцепились одной из Ульян в ступню, нервно перебирая плюсневые кости. "
    "Нет-нет-нет!!!"

    show pl_us_zombie_3 at cleft:
        ease 0.5 zoom 1.7
    show pl_us_zombie_4 at cright:
        ease 0.5 zoom 1.7
    show pl_us_zombie_2 at center:
        zoom 1.2
        ease 0.5 zoom 1.9
    with vpunch

    "Зомби ринулись на меня. Молча."
    plme "ААААарвгх..."
    "Крик застрял на полпути, когда первая из них вцепилась пальцами в горло. "

    scene cg limb_auto_fog_1:
        xalign 0.3 yalign 0.35 zoom 1.5
        pause 1
        parallel:
            ease 0.75 align (0.5, 0.5) zoom 2.5
        parallel:
            ease 1 align (0.5, 0.5) rotate -90
    show blinking
    show pl_us_zombie_3 at cleft:
        zoom 1.7
        ease 1 yalign -1.9
    show pl_us_zombie_4 at cright:
        zoom 1.7
        ease 1 yalign -1.9
    show pl_us_zombie_2 at center:
        zoom 1.9
        ease 1 yalign -1.9

    "Меня повалили на спину. Я попытался вскочить, но полдюжины чудовищ вцепились мне в ноги. "

    scene cg limb_auto_fog_red_2 at limb_shake:
        align (0.5, 0.5) zoom 2 rotate -90
    play sound sfx_limb_blood_1

    "И принялись грызть колени, голени и бёдра, выдирая куски мяса вместе с кусками ткани и обуви. "
    "В голове стучала пугающе простая мысль: "
    "Я сейчас умру. "

    play sound_loop2 sfx_limb_rage fadein 10

    "Господи, пожалуйста, убей меня скорее!!!"
    "Я ощущал чудовищную боль; казалось, должен был потерять сознание, но почему-то по-прежнему оставался здесь."
    "Почему?! ПОЧЕМУ Я ЕЩЁ ЗДЕСЬ?!"
    "Гнилые зубы внезапно сомкнулись рядом с моими глазами; брызнула струйка крови, попав на крыло машины; голову резко мотнуло в сторону. "

    scene cg limb_auto_fog_red_2 at limb_shake:
        align (0.5, 0.5) zoom 2 rotate -90
        ease 0.5 rotate 0
    play sound sfx_limb_blood_2

    "Я отрешённо подумал, что у меня осталось только одно ухо. "
    "Больше я не боялся. Впав в апатию, просто ждал конца. Даже боль начала отступать. Но я по-прежнему оставался в сознании, фиксируя всё, что происходило. "

    play sound sfx_limb_blood_1
    scene cg limb_auto_fog_red_2 at limb_shake:
        align (0.5, 0.5) zoom 2 rotate -90
        ease 0.5 rotate 0
    show limb_NickFury
    with flash_red

    "Вот любительница сладкого, сожрав моё ухо, вгрызлась мне в лицо. Теперь и глаз остался один..."
    "Две Ульяны по бокам от меня широко размахнулись... я не успел отвести взгляд перед тем, как мой живот был разодран в клочья. "

    play sound sfx_head_explode
    scene bg black with limb_blot

    "Кишечник выпал из недр моего тела, разворачиваясь, будто бы дешёвая трубка-дуделка на празднике. "
    "Он взмыл вверх, будто кит в струях багровой воды. Его сразу же растащили на части."

    window hide
    play sound sfx_ghost_children_laugh
    scene bg ext_underwater_red_darken with Dissolve(5)
    window show

    "Как будто смотрю малобюджетный фильм ужасов, где денег только на то и хватило, чтобы загримировать массовку, да краску купить. "

    scene cg limb_auto_mars_darken with limb_blot

    "Один зомби впился под левую мышку. Я грустно подумал, что сейчас мне разобьют сердце, и хихикнул. "
    "Тихий, мелкий, безумный смех прекратился с вырванной трахеей. Брызги крови вернули цвет вылинявшим галстукам пионерок-зомби. "
    "Интересно, откуда во мне столько крови? "
    "Я попытался спросить об этом пионерку, которая пожирала мою правую руку, но из горла не вышло ни звука. "
    "Зомби деловито разбирали меня на части, подчиняясь злой воле того, кто меня убивает раз за разом. "
    "Мне стало их жалко. "
    "Я попытался заплакать, но даже этого не сумел. "

    play sound sfx_limb_slap
    play sound sfx_limb_blood_2

    "С глухим всхлипом левую руку вырвали из сустава. Кровь, очевидно, уже закончилась. Отвратительно бледная головка плечевой тотчас исчезла в пасти одной из бедняжек. "
    "Хорошо хоть моё тело может плакать вместо меня..."
    "Тонкие сильные пальцы воткнулись мне под нижнюю челюсть. "
    "От рывка мой взгляд сместился вверх."

    scene bg black with pushleft

    "Я смотрел в небо, пока зомби отрывали мне голову. "

    stop sound_loop2 fadeout 3

    "В тёмное, по-настоящему чёрное небо. Без единой звезды. Без проблеска света. Без надежды. "

    stop sound_loop fadeout 5
    stop sound_loop2 fadeout 5

    "С мерзким влажным треском, знаете, таким, который издаёт сочный огурец, если его сломать пополам, моя шея разорвалась."

    play sound sfx_limb_itadakemas

    "[pl_ell]"
    plts "Ну как ты, Семён? "

    play music music_list["so_good_to_be_careless"] fadein 5
    $ limb_set_volume ('music', 0.5, 3)

    plme "В принципе, нормально, спасибо, что спросила. Только курить очень хочется."
    plts "Ну, это поправимое..."

    play sound sfx_limb_ahahaha

    "Она вдруг так знакомо рассмеялась и шлёпнула себя по лбу. Очень мило получилось. Я аж влюбился! "
    plts "Но как ты будешь курить? "
    plme "В смысле? Как все нормальные люди курят. Ртом же."
    plts "Но ведь у тебя лёгких нет!"

    play sound sfx_limb_screamer_4
    $ limb_set_volume ('sound', 0.5, 0)

    "Она издевательски захохотала. "
    "Я открыл глаза."

    play second_sound sfx_limb_deadfox_godofdestruction
    show blink
    scene cg limb_auto_dark
    hide blink
    show unblink

    "Судя по всему, мою голову на вытянутых руках держала зомби. "

    show pl_sl_smile2_swim with dissolve

    "Царица, снова почему-то принявшая облик Слави, аккуратно протянула мне сигарету. Щёлкнула невесть откуда взявшейся зажигалкой."

    play sound sfx_alisa_lighter

    "Я затянулся - что и говорить, получилось так себе. "

    play sound sfx_inhale

    plts "Извини, что так вышло с машиной, я думала, ты найдёшь ключи. Их ведь нужно найти, ха-ха-ха!"
    "Я плюнул в неё сигаретой. "
    plme "Сдохни."
    plts "Нууу... А я думала, ты душка! Не откажи в удовольствии: мне ну очень нравится тебя мучить, я просто таю..."

    $ limb_sprite_switch('pl_sl_', 'smile2_swim', 'angry_swim', dspr, None)

    plme "Ты любишь огурцы? Знаю, такие вопросы не принято задавать девушкам твоего возраста, но[pl_ell]"

    scene bg black
    with vpunch
    play sound sfx_limb_blood_1
    stop music
    stop second_sound
    pause 2
    play sound sfx_limb_itadakemas
    pause 2
    jump limb_life_horror_1

label limb_life_horror_4:

    $ sunset_time()
    scene bg int_old_building_sepia_1:
        pause 1
        ease 5 align (0.1, 0.0) zoom 1.25
    show pl_un_monster_cycle_1:
        pause 1
        ease 3 xalign -1.05 zoom 1.25
    with vpunch

    "Я рванул, рванулся как птица налево мимо первобытного ужаса, который неумолимо двигался в мою сторону... и превращался во что-то ещё более жуткое. "

    $ limb_set_volume('sound_loop', 0.5, 0)
    play sound_loop3 sfx_head_heartbeat

    "Не хочу смотреть! Не хочу видеть! "

label limb_life_horror_4_3:

    show blink

    "Закрыв глаза и выставив перед собой руки, я со всех ног бежал в темноту. "
    "Мои зубы стучали, перекликаясь с бешеным стуком сердца. "

    play sound_loop2 sfx_limb_scarybreath

    "Я чуть ли не кричал в уверенности, что в следующий момент липкое, склизкое, отвратительное щупальце коснётся моего плеча, ухватит меня за лодыжку или..."
    "Или, схватив мёртвой хваткой за шею, удушая, начнёт заползать прямо в горло сквозь раскрытый в немом крике рот."

    play sound sfx_bodyfall_1
    stop sound_loop fadeout 5
    stop sound_loop3 fadeout 5

    "Я врезался во что-то на всём ходу, отлетел назад, удержавшись на ногах, и в тот же миг заорал что есть силы, напугав себя ещё больше."
    "Мой вопль заметался гулким эхом. Мёртвая, затхлая тишина стала ему ответом. Я по-прежнему боялся открыть глаза, поэтому наугад нащупал рукой опору. Стена... Обои. Обычная твёрдая стена. "
    "Страх - тревожное чувство, которое меня сковывало и лишало воли - был каким-то детским, пустым и немного наивным. "
    "Я боялся не этой чудовищной Царицы и даже не смерти - я боялся, до перебоев в сердце боялся открыть глаза. Боялся темноты - и того, что может быть в ней."
    "Прислушался. И... открыл глаза, медленно, будто выходя из комы."

    stop sound_loop2 fadeout 10
    hide blink
    scene bg black
    show unblink
    play sound_loop sfx_limb_steps_1 fadein 30

    "Это[pl_ell] "

    scene bg int_kitchen_dark_blink with dissolve

    "Лампа мигнула, и это вывело меня из оцепенения."
    "Это же... о господи, нет! "
    "Я явственно услышал звук шагов. "

    menu:
        "{size=65}Что делать?!{/size}"
        "Бежать дальше":
            jump limb_life_horror_6_4
        "Прятаться":
            pass

    "Где можно спрятаться?! Куда исчезнуть?! "
    "Вжавшись в стену, я с ужасом ждал. Все мысли из головы выдуло напрочь. "
    stop music fadeout 10
    "Кроме одной..."
    "Я всё ближе и громче слышал шаги. Слышал дыхание хищника. Слышал легкие скользящие касания щупалец..."
    "Зажал себе рот, давя рвущийся животный крик. Никогда ещё в жизни я не жаждал так сильно стать незаметным, маленьким, невидимым."

    scene bg int_kitchen_dark_kodomo

    "Я почувствовал, как детские переживания захватывают моё сознание. "
    "И... Нет-нет-нет!!!"
    "Мне снова шесть лет, и я очень-очень, ОЧЕНЬ боюсь!"
    "Я понимаю, что нельзя этого делать, но не могу, никак не могу сдержаться, я должен молчать, но плач рвётся, рвётся из горла как птица из клетки, и..."

    plme "М-мам... "
    "Я захныкал, оцепенев, застыв как статуя или фигурка героев из комиксов, которые у меня были в детстве... "

    if limb_get_keys == True:
        show screen limb_keys
        with Dissolve(3)

    stop sound_loop
    with vpunch

    plme "МАМА!!!"
    "Завизжав от ужаса, потому что шаги прекратились, я попытался закрыть глаза, но тот же страх, который ранее не давал их открыть, помешал мне."
    "Шаги, шаги, они оборвались, а это... это значит..."

    hide screen limb_keys
    with fade

    "Слыша только свои всхлипы, я с ужасом пялился в полумрак. "
    "О себе напомнил мочевой пузырь, и пузырь ужаса в груди раздулся ещё больше."
    plme "М-мама-а-а!.."

    play sound sfx_limb_wrong

    "На плечо мне легко и тихо легла... рука."
    "Тёплая, нежная и заботливая. Такая знакомая!.."
    "Мама!"
    "Я почувствовал такое облегчение, что чуть ли не упал. Мамочка! Теперь всё будет[pl_ell]"
    "Рука так привычно взъерошила мне волосы. По моим щекам потекли слёзы, и я почти[pl_ell]"
    "Ласковый голос произнёс: "
    plv "Больше страшно не будет, Сёма!"
    "Ма[pl_ell] моч[pl_ell]"

    pause 1
    play sound sfx_limb_screamer_3
    scene cg limb_scream_5
    with vpunch
    pause 2
    scene bg black
    with dissolve2
    jump limb_life_horror_1

label limb_life_horror_5:
    $ sunset_time()
    play music music_list["orchid"] fadein 3
    "И в этот момент..."
    "Я заметил ключи. "
    "Автомобильные ключи, совершенно обычные с виду, в комнате, так похожей на кухню из далекого детства. "

    "Я искал их около машины - а они были здесь..."
    "Возможно, в этот момент на моё плечо уже опускалась рука. Рука, которая пригвоздила бы меня к месту, пронзив тысячей мельчайших игл страха, после чего я умер бы от испуга."

    stop music fadeout 10
    stop sound_loop

    "Но даже если рука и опускалась... Она схватила только воздух."
    "Оцепенение спало - я не собираюсь сдаваться так просто!"
    plts "Ты ведь пойдёшь со мной?"

    with vpunch

    "НЕ СЛУШАТЬ! Только в скорости мой выход. "

    hide screen limb_keys

    scene bg int_kitchen_dark_1:
        align (0.5, 0.75) zoom 1.5
        ease 1 yalign 0.5 zoom 1
    pause 1
    scene bg black with limb_pushright3
    play music music_list["pile"]

    "Я метнулся до ключей, схватил, затем, вспомнив челночный бег на физкультуре, упёрся и сразу же оттолкнулся от батареи обратно. "
    "Надо мной пронеслось щупальце, с тошнотворным звуком впечатавшись в стену. "
    "Сжав ключи в кулаке, я со всех ног полетел направо, прошмыгнув под спрутом, сожравшим разом все детские кошмары. "

    scene bg int_limb_directors_cut with limb_pushright
    pause 1
    scene bg black with limb_pushright

    "Нельзя медлить, она нагоняет!"

    scene bg semen_room_dorian with limb_pushright
    pause 1
    scene bg black with limb_pushright

    "Скорее! Нет времени на вопросы!"

    scene cg limb_safe_net with limb_pushright
    pause 1
    scene bg black with limb_pushright

    "Проносясь сквозь мнимое прошлое и не менее ложное будущее, я достиг последней декорации. "

    scene cg limb_auto_dark

    show pl_us_zombie_2:
        anchor (0.5, 0.5) align (0.22, 0.5)
    show pl_us_zombie_3:
        anchor (0.5, 0.5) align (0.76, 0.5)
    show pl_us_zombie_1:
        anchor (0.5, 0.5) align (0.5, 0.5)
    with limb_pushright_fast

    "И ужас, который был подавлен надеждой... взорвался внутри ледяным шаром, пронзив меня тысячью осколков-игл."

    stop music fadeout 3
    jump limb_life_horror_10

label limb_life_horror_6:

    $ sunset_time()
    scene bg int_old_building_sepia_1
    show pl_un_monster_cycle_1
    with vpunch

    "Я дрожал от страха. "
    "Но понимал, что нужно бежать, нужно прятаться, куда угодно, но бежать!!!"

    play sound_loop sfx_limb_scarybreath
    $ limb_set_volume('sound_loop', 0.5, 0)

    "Заорав, я прикрыл голову руками и метнулся мимо чудовища с тентаклями. "

    scene bg int_old_building_sepia_1:
        pause 1
        ease 5 align (0.55, 0.2) zoom 1.75
    show pl_un_monster_cycle_1:
        pause 1
        ease 2 xalign -2.59 zoom 1.75
    with vpunch

    "Щупальце хлестнуло по плечу; шипы, отвратительные шевелящиеся отростки ободрали кожу."
    "Спотыкаясь, я взбежал по лестнице, не разбирая дороги. Ногу обожгло - осколок стекла впился."

    play sound sfx_body_bump
    with vpunch

    "Врезался в стену, пытаясь развернуться, и завыл от боли - плечо будто облили кислотой..."

label limb_life_horror_6_4:

    $ sunset_time()
    $ limb_flow_transition('int_corridor_pl', limb_running)
    play music pl_st_d314lam

    plts "Сёма... пора решить квартирный вопрос!"
    plme "Нет! "
    "Куда угодно отсюда! Второй этаж старого здания! Плевать куда, может, через окно смогу сбежать и к своему домику!"
    "Какой раз я бегаю по этому заколдованному кругу?! Я уже был здесь! Я хочу проснуться дома!!!"

    stop sound_loop
    play sound sfx_close_door_1
    scene bg black
    with vpunch

    "Я вбежал в какое-то помещение и захлопнул дверь. Спрятаться! Спрятаться! "

    scene bg semen_room_dorian
    with dissolve

    "Глаза постепенно привыкали к темноте. Я... Это моя квартира!"

    play sound sfx_limb_nightmare

    "Страх начал отступать. Я замер в темноте и тишине, прислушиваясь. Может, получилось оторваться?"

    menu:
        "{size=65}Что делать?!{/size}"
        "Спрятаться":
            pass
        "Бежать дальше":
            jump limb_life_horror_7_6

    "Я рванул на себя дверцу платяного шкафа и нырнул в темноту."

    scene bg black with limb_flowtoright
    play sound sfx_close_cabinet
    $ limb_set_volume('sound_loop2', 0.5, 0)
    $ limb_set_volume ('sound_loop', 0.5, 5)
    play sound_loop sfx_limb_breath
    play sound_loop2 sfx_head_heartbeat
    stop music fadeout 10

    "Зажав рот, безуспешно попытался заглушить дыхание. Сердце стучало, будто огромный кузнечный молот. "
    "Только бы она... оно не услышало!"
    "Изо всех сил навострил уши."

    stop sound_loop2

    "Никого и ничего кроме шума, который я сам издаю. "
    "Где-то слышно скрип половиц. "
    "Шаг."
    "Может, ещё не поздно сбежать..."
    "Страх в очередной раз забирается внутрь меня и разрывает на части мои внутренности. "

    play sound_loop2 sfx_limb_steps_2 fadeout 10

    "Шаги раздаются ближе. Тихие, вкрадчивые. "
    "Надо бежать, надо срочно бежать отсюда, она чувствует меня, она знает, что я здесь, чёрт, я не хочу снова..."
    "Шаги... Она в этой комнате!!!"
    "Я с трудом подавил крик ужаса. Меня трясло. Если так будет и дальше, она поймёт, где я! "

    stop sound_loop2

    "Шагов больше не было. "
    "По лицу скатывались крупные капли пота, пока отчаянно я вслушивался и всматривался во тьму. "
    "Она решила оставить меня?! Но она знала, что я тут! Она мучает меня!!!"
    "Сейчас она распахнёт дверцу!"
    "Сейчас она разорвёт меня на части! "

    stop sound_loop fadeout 3

    "Сейчас снова будет что-то ужасное!"
    "Вот сейчас!"

    play sound sfx_suspence_bang
    scene cg limb_scream_0
    with vpunch

    plts "Ну вот.{w=0.5} А ты боялся[pl_ell]"

    pause 3
    play sound sfx_limb_screamer_2
    scene cg limb_scream_3
    with vpunch
    pause 4
    scene cg limb_scream_5
    with vpunch
    pause 1
    scene cg limb_scream_4
    with vpunch
    pause 1
    scene cg limb_scream_2
    with vpunch
    pause 1
    scene cg limb_scream_6
    with vpunch
    pause 5
    play sound sfx_limb_screamer_7
    scene cg limb_scream_1
    with vpunch
    pause 2
    scene bg black
    with dissolve2
    jump limb_life_horror_1

label limb_life_horror_7:

    play sound sfx_head_heartbeat
    $ sunset_time()
    scene bg int_old_building_sepia_1
    show pl_un_monster_cycle_1
    with vpunch

    "Я не мог заставить тело сдвинуться с места - животный ужас приковал меня к земле. "

    show pl_un_monster_cycle_1:
        ease 5 align (0.5, 0.5) zoom 1.5

    "Отрешённо подумал, что когда она убьёт меня в этом старом корпусе, я стану призраком и буду грустно завывать годы напролёт, пока его не снесут..."
    "Щупальце зависело перед моими глазами."
    "Этого стало достаточно, чтобы сбить наваждение. Забавно - один страх сковывает, а другой, наоборот, заставляет двигаться."
    "На том месте, где была моя голова секунду назад, колебалось острое щупальце. Она явно целилась мне в глаз."

    with vpunch
    scene bg black with limb_flowtoright

    play music music_list["scarytale"]

    "Я пригнулся и рванул направо. Споткнулся, кубарем покатился по битому стеклу и мусору, снова вскочил и побежал, побежал что есть сил в темноту..."

label limb_life_horror_7_6:

    scene cg limb_safe_horror:
        pause 3
        ease 2 yalign 0.9 xalign 0.15 zoom 1.5
        pause 0.5
        ease 1.5 yalign 0.1 xalign 0.15 zoom 1.5
        pause 0.5
        ease 1.5 yalign 0.1 xalign 0.85 zoom 1.5
        pause 0.5
        ease 1.5 yalign 0.9 xalign 0.85 zoom 1.5
        pause 0.5
        ease 1.5 xalign 0.5 zoom 1
    show limb_horror_brick_1:
        pause 3
        ease 2 yalign 0.9 xalign 0.15 zoom 1.5
        pause 0.5
        ease 1.5 yalign 0.1 xalign 0.15 zoom 1.5
        pause 0.5
        ease 1.5 yalign 0.1 xalign 0.85 zoom 1.5
        pause 0.5
        ease 1.5 yalign 0.9 xalign 0.85 zoom 1.5
        pause 0.5
        ease 1.5 xalign 0.5 zoom 1
    show limb_horror_brick_2:
        pause 3
        ease 2 yalign 0.9 xalign 0.15 zoom 1.5
        pause 0.5
        ease 1.5 yalign 0.1 xalign 0.15 zoom 1.5
        pause 0.5
        ease 1.5 yalign 0.1 xalign 0.85 zoom 1.5
        pause 0.5
        ease 1.5 yalign 0.9 xalign 0.85 zoom 1.5
        pause 0.5
        ease 1.5 xalign 0.5 zoom 1
    show limb_horror_brick_3:
        pause 3
        ease 2 yalign 0.9 xalign 0.15 zoom 1.5
        pause 0.5
        ease 1.5 yalign 0.1 xalign 0.15 zoom 1.5
        pause 0.5
        ease 1.5 yalign 0.1 xalign 0.85 zoom 1.5
        pause 0.5
        ease 1.5 yalign 0.9 xalign 0.85 zoom 1.5
        pause 0.5
        ease 1.5 xalign 0.5 zoom 1
    show limb_horror_brick_4:
        pause 3
        ease 2 yalign 0.9 xalign 0.15 zoom 1.5
        pause 0.5
        ease 1.5 yalign 0.1 xalign 0.15 zoom 1.5
        pause 0.5
        ease 1.5 yalign 0.1 xalign 0.85 zoom 1.5
        pause 0.5
        ease 1.5 yalign 0.9 xalign 0.85 zoom 1.5
        pause 0.5
        ease 1.5 xalign 0.5 zoom 1
    show limb_horror_brick_5:
        pause 3
        ease 2 yalign 0.9 xalign 0.15 zoom 1.5
        pause 0.5
        ease 1.5 yalign 0.1 xalign 0.15 zoom 1.5
        pause 0.5
        ease 1.5 yalign 0.1 xalign 0.85 zoom 1.5
        pause 0.5
        ease 1.5 yalign 0.9 xalign 0.85 zoom 1.5
        pause 0.5
        ease 1.5 xalign 0.5 zoom 1
    show limb_horror_brick_6:
        pause 3
        ease 2 yalign 0.9 xalign 0.15 zoom 1.5
        pause 0.5
        ease 1.5 yalign 0.1 xalign 0.15 zoom 1.5
        pause 0.5
        ease 1.5 yalign 0.1 xalign 0.85 zoom 1.5
        pause 0.5
        ease 1.5 yalign 0.9 xalign 0.85 zoom 1.5
        pause 0.5
        ease 1.5 xalign 0.5 zoom 1
    with dissolve

    plme "Где я?"
    "Это место выглядит знакомо.{w=1} Сейф? Да, сейф, созданный из декораций Совёнка. "
    "По всему телу прошла дрожь. Я чувствую, что она рядом..."

    menu:
        "{size=65}Что делать?!{/size}"
        "Бежать дальше":
            jump limb_life_horror_3_7
        "Искать выход":
            pass

    stop music fadeout 10
    play sound_loop2 sfx_limb_deadfox_godofdestruction

    "Я замер в центре помещения и начал лихорадочно оглядывать стены. Тут где-то должен быть выход! Должна быть лазейка! Я знаю это!"
    "Да, я нашёл его!"

    pause 3
label limb_life_horror_safe_1:

    hide limb_horror_brick_1
    show screen limb_horror_sb_1

    "Страх помогал мне работать, разбирая стену."
    pause 3
label limb_life_horror_safe_2:

    hide limb_horror_brick_2
    show screen limb_horror_sb_2

    "Она где-то рядом, я должен ускориться!"
    pause 3
label limb_life_horror_safe_3:

    hide limb_horror_brick_3
    show screen limb_horror_sb_3

    "Выход почти готов!"
    pause 3
label limb_life_horror_safe_4:

    hide limb_horror_brick_4
    show screen limb_horror_sb_4

    "Давай, Семён, ты почти сделал это!"
    pause 3
label limb_life_horror_safe_5:

    hide limb_horror_brick_5
    show screen limb_horror_sb_5

    "Сбежать, сбежать, я почти сбежал, давай!"

    play sound sfx_limb_screamer_1
    scene cg limb_scream_1
    with vpunch
    stop sound_loop2
    pause 3
    scene bg black with dissolve

    jump limb_life_horror_1

label limb_life_horror_8:
    scene bg int_old_building_sepia_1:
        pause 1
        ease 7.5 align (0.25, 0.5) zoom 1.65
    show pl_un_monster_cycle_1:
        pause 1
        ease 2 xalign -0.99 zoom 2.25
    with vpunch

    "С воплем проскочив под метнувшимся в мою сторону ужасным щупальцем, я влетел в комнату, захлопнул за собой дверь и, распинав мусор, отыскал дверцу на полу."
    "\"Обратно в шахты!\""
    "Эта мысль вытеснила все остальные. "
    "\"Беги, беги, беги в шахты, в шахты, это самое логичное!\""
    "Мне казалось, что мои мысли отдают эхом у меня в голове."
    "Я рванул крышку изо всех сил, и она с ржавой неохотой поддалась."
    "Сзади раздался ЗВУК."

    play sound sfx_limb_screamer_2
    with vpunch

    play sound sfx_grate_open_hand

    "Я вскрикнул и бросился вниз, из темноты в ещё большую темноту. "

    scene bg int_catacombs_entrance with vpunch

    "Лихорадочно перебирая ногами по перекладинам, я едва успел убрать руки, когда дверца захлопнулась. "

    play sound sfx_metal_door_large_close_basement

    "Дверца моего саркофага... Крышка моего гроба. "

    scene bg int_catacombs_entrance_gray at limb_walking with dissolve
    stop sound_loop fadeout 10

    "Нет, тогда я этого и близко не понимал. "
    "Понимание пришло много позже, возможно, через месяца, декады или световые годы."
    "Которые я провёл в темноте. "
    "Один. "
    "Я взглядывался в темноту, изо всех сил выпячивая глаза, ожидая, что что-то прыгнет на меня. Вот-вот..."

    scene bg int_catacombs_entrance_transition

    "Вот прямо сейчас! Я знаю!!!"

    play sound_loop2 sfx_limb_stop

    "Это длилось долго... очень долго."
    "Без еды, без воды, без света, без общения. "
    "О, я кричал. "
    "Сначала от страха, когда думал, что за мной идёт погоня. "
    "Потом от тоски и одиночества. "
    "Потом - снова от страха, когда ощутил в полной мере отсутствие того, что поддерживает в человеке жизнь. "
    "Потом - от адской боли в стёртых в кровь, в стёртых до костей, наконец, в стёртых до состояния ампутации ступней. "
    "Когда я задумался о возможности остановиться или посмотреть назад - её уже не было. "
    "Моё тело видоизменилось. Теперь я мог только двигаться вперёд."
    "Шея вросла в туловище и лишилась подвижности. Позвоночник согнулся под тяжестью тьмы. "
    "Суставы ног теперь двигались только в одной плоскости. "
    "Глаза съежились, высохли и в какой-то момент просто вывалились мне под ноги. И пусть - зачем мне смотреть в темноту? Она и так мой друг."
    "А руки давно отсохли и отвалились за ненадобностью. "
    "Забавно, я этого и не заметил. "
    "Впрочем, не помню, для чего они мне. "
    "Мой мир ныне - лишь темнота и прямая. "
    "Что за чудесный мир? Никаких страхов..."
    "Впрочем, вру."
    "Единственное, чего я боюсь - так это падения. "
    "Ведь нельзя же идти вечно?"
    "А если я упаду - я не смогу встать, и мне останется лишь ползти вперёд на брюхе, извиваясь всем телом, как делают редкие червяки, которых я различаю в темноте в моём мире. "
    "А если буду ползти - это будет медленнее. А я не хочу медленнее!"
    "Иногда я давлю их. Червяков. Но не могу есть - не могу поднять и не могу остановиться... "
    "Хорошо, что я не один."

    menu:
        "Я останусь здесь":
            jump limb_prolog
        "Я пойду с тобой":
            jump limb_life_horror_1

label limb_life_horror_10:

    "Я застыл, на мгновение забыв о главном страхе позади."
    "А она, этот страх, не любит, когда о ней забывают... Я через силу повернулся назад."

    window hide
    show cg limb_auto_dark:
        anchor (0.5, 0.5) pos (960, 540)
        ease 3 xpos 320
        pause 3
        ease 3 xpos 960
    show pl_us_zombie_1:
        align (0.5, 0.5)
        ease 3 xalign 0.1
        pause 3
        ease 3 xalign 0.4
    show pl_us_zombie_2:
        align (0.22, 0.5)
        ease 3 xalign -0.18
        pause 3
        ease 3 xalign 0.12
    show pl_us_zombie_3:
        align (0.76, 0.5)
        ease 3 xalign 0.36
        pause 3
        ease 3 xalign 0.66
    pause 3
    show pl_un_monster_cycle_1 with dissolve2:
        anchor (0.5, 0.5)
        align (1.5, 0.5)
        pause 3.5
        ease 5.5 xalign 0.5
    pause 1
    play music pl_uc_powerless fadein 3
    window show

    "Царица медленно плыла, приближаясь. В этом даже было что-то торжественное, если бы торжество подразумевало потерю сознания от ужаса."
    "Думаю, я бы и умер здесь, не сумев уже сдвинуться с места, растратив все силы..."
    "Если бы рефлекторно не сжал кулак, в котором были ключи. "

    play sound sfx_limb_slap
    scene cg limb_auto_fog_2
    show pl_us_zombie_1:
        align (0.4, 0.5)
        ease 12 xalign -0.6
    show pl_us_zombie_2:
        align (0.12, 0.5)
        ease 12 xalign -0.88
    show pl_us_zombie_3:
        align (0.66, 0.5)
        ease 12 xalign -0.54
    hide pl_un_monster_cycle_1
    show pl_un_monster_cycle_2
    with dissolve2

    "У машины зажглись фары, и я впервые увидел... её."
    "Вокруг нас всё было в густом тумане. Таком, как на дороге одной ночью... Таком, как в одном лагере как-то утром..."
    "Полчища Ульян шипели, толкались и стремились убраться в темноту. "
    plts "Правда я... красивая?"
    "Её электронный голос звучал в тумане глухо. Впрочем, он давно уже не был электронным - в нём были и эмоции, и оттенки. Просто я раньше не замечал..."
    "Колени дрожали так, что я чуть ли не падал. "
    "Попытался что-то сказать, попросить, но сжатое спазмом горло не пропустило ни звука."

    show pl_us_zombie_1:
        anchor (0.5, 0.5)
        pos (-0.075, 0.5)
        rotate 0
        parallel:
            ease 0.4 pos (0.175, 1.33)
        parallel:
            ease 0.5 rotate 90
    play sound sfx_limb_blood_2
    queue sound sfx_bodyfall_1

    "Одна из Ульян, наверное, самая неудачливая, упала под ноги толпе. Через секунду её голова с тошнотворным всплеском лопнула. Я содрогнулся."
    with vpunch
    "Царица облизнулась своими чёртовыми хелицерами... или это у пауков... а что у девушек-андроидов-спрутов?.."
    "И я не сдержался, завыл, отшатнулся в туман, рухнул на колени, и снова выл и выл - когда же этот хренов кошмар закончится?! Я устал бояться..."
    with vpunch

    scene cg limb_auto_fog_horror
    show pl_un_monster_cycle_2
    with dissolve2

    plts "Давай сыграем в игру! "
    "Радостно взвизгнула она - она, напоминающая тех личинок майских жуков, которые можно раскопать в земле перед праздниками."

    show pl_us_zombie_blink_1 behind pl_un_monster_cycle_2 at fleft
    show pl_us_zombie_blink_2 behind pl_un_monster_cycle_2 at right
    with dissolve2

    plme "А давай! Давай! Почему бы и нет?! Ничего против не имею!!!"
    "Я истерически расхохотался, заколотив ладонью по земле. "
    "Из ближайшей Ульяны посыпались черви и опарыши. Мой смех завершился сдавленным воплем."
    with vpunch
    stop music fadeout 10
    "Некоторое время я просто отрешённо наблюдал сам за собой. "
    "Потом попытался взять себя в руки. "

    pause 3
    play music pl_gk_red_haired_blues
    with flash

    "Разве не я сам говорил, что не сдамся?"

    with flash

    "Превозмогая боль, слабость и ОПЬЯНЯЮЩИЙ, ИССУШАЮЩИЙ, УДУШАЮЩИЙ страх, я молча встал сначала на одно колено. Потом на второе. Потом поднялся..."
    "Я чувствовал, что в любой момент могу снова впасть в истерику, но[pl_ell] "
    "Какая-то частичка в моей душе снова горела. Эта искра не позволила мне избавиться от страха, но[pl_ell]"
    plme "Н-не об-би-и-ижайся, но т-т-ты п-похожа на ст-тарый фиолетовый з-з-зонтик."

    with vpunch

    "Зомби издали дружный рёв. Я почти не дрогнул, только утёр пот и слёзы."
    plts "Совсем-совсем-совсееем другое дело. Слабый Семён мне и не нужен. Я хочу сильного противника! Такого ломать куда интереснее."
    "Я закусил губу, подавляя рвущийся наружу мышиный писк. Колени снова принялись отплясывать тектоник."

    show pl_un_monster_cycle_2:
        align (0.5, 0.5) zoom 1
        ease 7.5 zoom 1.5

    "Голос Царицы изменился, став ласковым, нежным, знакомым..."
    plts "Мы с тобой будем играть в игру, Сёма! "
    plts "Я буду читать считалочку, а ты - убегать! "

    stop music
    show pl_us_zombie_2:
        align (0.72, 0.5)
        ease 0.5 align (0.5, 0.5) zoom 1.5
    with vpunch
    scene bg black

    play sound sfx_limb_screamer_3
    "В следующий момент на меня прыгнули."

    play music pl_gk_vintage_labeled_amys_dark_axe
    scene cg limb_auto_fog_horror at limb_running with vpunch

    plme "Аааа!!!"
    "Я мужественно заорал и сиганул в сторону. "

    scene cg limb_auto_fog_2 at limb_shake:
        align (0.5, 0.5)
        pause 2
        ease 3 align (0.6, 0.5) zoom 1.5
    with dissolve

    pltsh "Мы сидели в чёрной яме..."
    "\"Серьёзно?!\""
    "Ульяны будто бы морские волны повалили вслед за мной, то и дело падая друг на друга."
    "\"Эй, если я достаточно долго буду бегать, то они сами себя перебьют!\" "
    "Идиотская мысль мелькнула и сгинула в водовороте других."
    "Машина! МАШИНА!"

    scene cg limb_auto_fog_2 at limb_shake:
        align (0.6, 0.5) zoom 1.5
        pause 2
        ease 2 align (0.3, 0.5)

    "Я рванул влево, и зомби свалилась мне под ноги."
    pltsh "...страшный демон там был с нами..."

    scene cg limb_auto_fog_2 at limb_shake:
        align (0.3, 0.5) zoom 1.5
        ease 1 align (0.2, 0.5) zoom 1.7

    "Я подбежал к авто и начал как псих дёргать ручку."
    "Ключи! КЛЮЧИ!"

    with vpunch

    "Стальные пальцы вцепились в мою лодыжку. Я заорал от боли..."

    show pl_hand_sword:
        anchor (0.5, 0.5)
        pos (0.92, 0.5)
        rotate 30
        parallel:
            ease 1 pos (0.5, 0.5)
        parallel:
            ease 0.75 rotate 0
    pause 2

    "Меч! МЕЧ!!!"

    show pl_us_zombie_2:
        anchor (0.5, 0.5)
        pos (1.2, 0.5)
        ease 0.75 xpos 0.5
    pause 1
    hide pl_hand_sword
    show pl_hand_sword_magic
    with dissolve_fast
    pause 0.5
    with vpunch
    show pl_hand_sword_magic:
        anchor (0.5, 0.5)
        pos (0.92, 0.5)
        rotate 30
        pause 1
        parallel:
            ease 0.1 pos (0.5, 0.5)
        parallel:
            ease 0.075 rotate 0
    show pl_us_zombie_2:
        anchor (0.5, 0.5)
        pos (0.5, 0.5)
        rotate 0
        parallel:
            ease 0.4 pos (0.75, 1.33)
        parallel:
            ease 0.5 rotate 90
    with vpunch
    play sound sfx_armature_swish

    "Совершенно не отдавая себе отчёта в том, что я вообще, черт побери, делаю, рубанул по сдохло-Ульяне клинком из другой реальности. "
    "Ульяна развалилась. Хватка пропала."

    scene bg ext_fog_4
    show pl_hand_sword_magic
    with vpunch

    "Я привалился к боку авто, тяжело дыша. Лезвие меча тускло переливалось в свете фар, проигрывая тёмными языками пламени. "

    show pl_us_zombie_2 behind pl_hand_sword_magic at cleft
    show pl_us_zombie_4 behind pl_hand_sword_magic at fright
    with dissolve2
    show pl_us_zombie_1 behind pl_hand_sword_magic at fleft
    show pl_us_zombie_3 behind pl_hand_sword_magic at right
    with dissolve

    pltsh "... Раз, два, три..."
    "Ульяны на секунду замерли. "

    show pl_us_zombie_2 behind pl_hand_sword_magic at cleft:
        anchor (0.5, 0.5) ypos 0.5
        ease 0.8 zoom 1.3
    show pl_us_zombie_4 behind pl_hand_sword_magic at fright:
        anchor (0.5, 0.5) ypos 0.5
        ease 1.3 zoom 1.4
    show pl_us_zombie_1 behind pl_hand_sword_magic at fleft:
        anchor (0.5, 0.5) ypos 0.5
        ease 0.95 zoom 1.25
    show pl_us_zombie_3 behind pl_hand_sword_magic at right:
        anchor (0.5, 0.5) ypos 0.5
        ease 1.15 zoom 1.2
    play sound_loop sfx_torch fadein 5
    show pl_hand_magic_show behind pl_hand_sword_magic:
        anchor (0.5, 0.5)
        pos (0.5, 1.5)
        zoom 0.75
        ease 2 pos (0.5, 0.5) zoom 1

    "А потом рванули вперёд. "
    "\"Ну держитесь, сукины суки! Я вам сейчас такую мужицкую п*здюлину покажу...\""
    "Я вызвал в свободной руке такой привычный шар огня и как шандарахнул им по массовке!"

    $ limb_set_volume('second_sound', 0.25, 0)
    play second_sound sfx_nightmare_explosion
    scene bg ext_fog_4 with flash
    stop sound_loop fadeout 1

    "На миг ослепительная вспышка осветила всё, мгновенно испепелив большую часть зомби. "
    plme "Взвейтесь кострами..."
    "Я повернулся и, отбросив меч в сторону, начал судорожно открывать дверцу авто."

    scene cg limb_auto_fog_2:
        align (0.3, 0.5) zoom 1.5

    pltsh "...этот демон..."
    "\"Как она так долго читает это четверостишие? Времени мне побольше даёт, что ли?\""

    scene bg int_auto_fog_2 with vpunch

    "Дверца открылась, я в дикой панике влез внутрь салона. "
    "Заводись, заводись, заводись, заводись!!!"
    pltsh "... это ты."
    "Чёрт! ЗАВОДИСЬ."

    scene bg int_auto_fog_2 at limb_shake
    with vpunch
    $ limb_set_volume('second_sound', 1, 0)
    $ limb_set_volume('sound_loop', 0.1, 0)
    play sound_loop sfx_bus_idle

    "Машина рванула вперёд, и я рванул вместе с ней, сбив нескольких недожаренных зомби. "
    "\"Я должен где-то спрятаться, где-то переждать, удрать, но только не попадаться ей...\""

    stop music fadeout 3
    play sound sfx_limb_crash
    with vpunch

    "Машина заглохла так резко, что я приложился о руль. Самым важным, да-да, лицом..."

    scene bg int_auto_fog_2 with vpunch
    stop sound_loop
    $ limb_set_volume('sound_loop', 1, 0)
    play sound_loop sfx_limb_tinnitus fadein 3
    with flash_red

    "Боль прочистила мозги. "
    "Машину снаружи облепили зомби."

    stop sound_loop fadeout 5
    scene bg ext_fog_4 with dissolve

    "Я пинком распахнул дверцу и, просто не придумав ничего лучше, начал стрелять в них из воображаемого пистолета. "

    play music pl_uc_suburbs
    window hide
    show pl_us_zombie_1 at left with dissolve
    show pl_point_strike:
        anchor (0.5, 0.5)
        pos (0.25, 0.85)
    play sound sfx_limb_1_strike
    hide pl_us_zombie_1
    hide pl_point_strike
    with dissolve
    show pl_us_zombie_4 at cright with dissolve
    show pl_point_strike:
        anchor (0.5, 0.5)
        pos (0.645, 0.85)
    play sound sfx_limb_1_strike
    hide pl_us_zombie_4
    hide pl_point_strike
    with dissolve
    pause 1
    window show

    "Выстрелы вполне работали. "
    "\"Найти мой домик!\" "
    "Внезапно я понял, что почти не боюсь. То есть нет, я дико, до потери пульса боюсь Царицы, но зомби, драконы, туман, пионеры, вампиры... "

    scene bg ext_house_of_mt_fog at limb_running
    show pl_us_zombie_1:
        align (0.18, 0.5)
        ease 1 align (-1.18, 0.5) zoom 1.5
    show pl_us_zombie_2:
        align (0.82, 0.5)
        ease 1 align (2.18, 0.5) zoom 1.5
    with dissolve

    "Я небрежно расшвырял в стороны подобием телекинеза нескольких зомби, побежал вперёд сквозь туман, и... "
    "И оказался перед домиком. Перед своим домиком. Перед домиком ОД. "
    "Перед тем самым местом, где я хотел проснуться. Проснуться от этого кошмара. Хотел сильнее всего на свете... "

    menu:
        "Войти":
            pass
        "Не заходить":
            jump limb_you_win

    "Перестав колебаться, я рванул внутрь, открыл, словно и не нужен никакой ключ, дверь, и захлопнул за собой, и... "

    scene bg black
    with limb_blot
    stop music fadeout 3
    scene bg int_house_of_mt_day with dissolve
    play sound sfx_close_door_1
    play ambience ambience_int_cabin_day fadein 5
    show mt smile pioneer close with dissolve

    mt "Семён? Что случилось?"
    "Я практически разрыдался от облегчения. "
    plme "Просто... Я так рад... Что я здесь..."
    mt "А уж как я рада! "

    play sound_loop sfx_limb_nightmare
    scene bg int_house_of_mt_gray_1
    show pl_mt_dark_2
    stop ambience fadeout 5
    show mt sad panama pioneer close at left with limb_blot

    mt "Просто посмотри, как много страданий ты причинил сам себе! "
    plme "Нет, нет, нет, только не снова... почему?!"

    show limb_eff_glitch
    show mt grin pioneer close at right as mt2 behind limb_eff_glitch with limb_blot

    plts "Потому что ты так и остался в яме. Ты так ничего и не понял. Пожалуй, даже разочаровал меня."

    scene bg black with dissolve2
    stop sound_loop fadeout 3

    plts "А это - твоя последняя остановка."
    with limb_neon_flash
    scene bg black
    with limb_blot
    pause 2
    jump limb_life_horror_1

label limb_you_win:

    stop music fadeout 3

    "И тут я подумал..."

    play music pl_st_a2e13lam fadein 10

    "\"Почему я всегда убегаю?\" "
    "Волны ужаса, будто дождавшиеся момента, снова нахлынули на меня. Я задохнулся, бессильно скребя грудь через рубашку."
    "\"Но ведь она просто диктует мне условия! Она сама об этом говорила! Этот страх - это не МОЙ страх!\""
    "Хотя это казалось невозможным, чувство ужаса стало ещё сильнее. Я чувствовал, что через пару ударов моё сердце остановится. "

    show blink

    "Окружающий мир скрыли веки. "
    "Все мои силы уходили на то, чтобы оставаться в сознании. "
    "Я должен что-то сделать!"
    "\"Но я не могу! Я не могу это сделать один! Мне нужна помощь!!! Помогите!!!\""
    "Но кто мне поможет?"

    with limb_itai_flash

    plme "ПОМОГИТЕ!!!"

    stop music fadeout 3
    play sound sfx_limb_lightning_2

    un "Ты почти справился, Семён..."
    "Я замер. "

    play music music_list["sparkles"] fadein 5
    scene anim limb_space with dissolve2
    show un pioneer smile at left:
        alpha 0
        pause 1
        ease 3 alpha 0.5

    "Я её вижу... Несмотря на то, что мои глаза закрыты, я вижу её. Такое уже было.... В самом начале пути."
    "Горячие слёзы прочертили новые дорожки от углов глаз до подбородка."
    un "Не плачь, а давай возвращайся поскорее, хорошо? Все волнуются..."
    plme "А... ты..?"
    "Лена тихонько рассмеялась, так же, как если бы мы сидели на площади и обсуждали вёселый момент из её любимой книги.{w=1} Искренне."

    show un smile2 with dspr

    un "А вот я - не волнуюсь. Нисколечки! Ведь я знаю, что ты вернёшься с минуты на минуту, целый и невредимый."
    "Я снова ощутил могильную, леденящую тяжесть на сердце."
    plme "Но я... Да как же... Я не могу... Никак..."

    show dv pioneer grin at right:
        alpha 0
        pause 1
        ease 3 alpha 0.5

    dv "Ну и долго ты будешь такой рохлей ещё?"
    plme "А-а-а[pl_ell]"

    show dv angry with dspr

    dv "Если ты вместе со своей жизнью и имя моё забыл, я... Я тебя..."
    plme "Нет.{w=0.5} Не забыл!"

    show dv shy with dspr

    "Алиса ожидаемо смутилась."
    dv "Вот и[pl_ell] славно."

    show un smile3 with dspr

    un "Ты справишься."
    "Снова я не могу справиться сам, один, без помощи друзей... Снова и снова подвожу тех, кто в меня верит!"

    show dv smile with dspr

    dv "Ты точно справишься. Сам справишься! Поверь, нам виднее - всем нам. "
    "Я наконец-то понял, что та маленькая искорка внутри моей души всё это время превращалась в гигантский огненный шар - в моё персональное солнце под названием \"Совёнок и все-все-все\"."
    plme "Девочки, вы ведь знаете, что я вас люблю?..{w=1} Люблю[pl_ell] Всех."
    "Алиса среагировала как типичная Алиса, а вот лицо Лены приняло угрожающее выражение."

    show dv shy with dspr
    show un evil_smile with dspr

    un "Прям всех?{w=1} А не много ли?"

    show un laugh
    show dv laugh
    with dspr

    "Она снова рассмеялась."
    "Алиса, хихикнув, добавила:"

    show dv smile with dspr

    dv "Ну, Женя точно лишней будет."
    "Я улыбался с закрытыми глазами. "
    "Скользкий узел спрессованных в ужасе внутренностей наконец-то расслабился."
    "Стало{w=0.5} - наконец-то стало!{w=0.5} - спокойно на душе. И совершенно не имеет значения, какие миражи и тульпы пытаются сбить меня с пути домой."
    "Невзирая на участки памяти, которые я потерял; невзирая на страдания, которые я перенёс; невзирая на ужас, который ожидает меня, стоит только открыть глаза..."
    "Я все равно улыбаюсь.{w=1} Слабо{w=0.5}, обессиленно и сквозь слёзы.{w=1} Но улыбаюсь.{w=1} Искренне."
    plme "Вы ведь просто моё воображение, верно?.."

    show dv laugh with dspr

    "Алиса улыбнулась и подмигнула мне:"
    dv "Конечно. Но ведь это не делает нас менее реальными, верно?"

    scene bg black with dspr
    window hide
    stop music fadeout 10
    scene bg ext_house_of_mt_fog
    show unblink
    with None
    window show

    "Я открыл глаза. Развернулся. Мееедленно."
    "Непослушные язык и губы с трудом позволяли говорить, но мне нужно было это сказать: "
    plme "Диджей... Врубай дабстеп."
    un "Да!"

    play music pl_ef_dubstep_2

    "Я медленно повернулся, через силу, сжимая кулаки, изо всех сил пытаясь не дрожать. Но все равно не получалось. Но повернулся! Колени подгибались... но... я сделал шаг вперёд. И ещё один!"
    "Навстречу тому ужасу, с которым столкнулся. От которого убегал."
    th "Видишь - ты хочешь защищать своих друзей, а в итоге это они защищают тебя. "
    th "Но нельзя вечно полагаться на других."
    th "Я должен бороться, чёрт возьми, сам! Я должен доказать, что всё это мне было дано не зря!"

    scene bg ext_fog_4 at limb_running
    show pl_us_zombie_2 with dissolve
    pause 1
    play sound sfx_piano_head_bump
    show pl_us_zombie_2:
        anchor (0.5, 0.5)
        pos (0.5, 0.5)
        rotate 0
        parallel:
            ease 0.4 pos (0.75, 1.33)
        parallel:
            ease 0.5 rotate 90

    "Материализовав в руке гитару, я снёс ей зазевавшуюся зомби."
    "Вышло жутко немузыкально."
    "Я шёл вперёд, всё быстрее, пока не побежал вперёд, не рванул на встречу своей новой смерти... чего её бояться-то уже?"
    "И когда я увидел её..."

    scene bg ext_fog_4
    with dissolve_fast
    show pl_monster_4
    with dissolve_fast
    with vpunch

    plme "ОСТАВЬ МЕНЯ В ПОКОЕ! Я НЕ СДАМСЯ! НИКОГДА!!!"
    "Смерть смотрела прямо мне в глаза."

    stop music fadeout 3

    "А потом произнесла, тихо, спокойно и слегка печально: "
    plts "Ты победил."

    scene bg white with limb_blot
    hide pl_monster_7 with limb_blot
    show pl_sl_smile2_swim with limb_blot
    show pl_limb_eyes_final with limb_blot

    plme "Правда?.."
    plme "Я ожидал решающей схватки с боссом Гидры, даже как-то настроился..."

    $ persistent.sprite_time = 'day'
    show pl_sl_smile2_swim:
        ease 10 alpha 0.1

    plts "Даже сейчас не можешь быть серьёзен?"
    plme "Не думаю, что выжил бы, если бы был полностью серьёзен."

    hide pl_sl_smile2_swim with limb_blot

    "В белой пустоте остались только розовые глаза."
    pause 1
    scene bg white with flash
    "А потом исчезли и они."
    plts "Бывай, Семён."
    plme "Так а ты..."

    show blink

label limb_is_over:

    window hide
    $ limb_screens_load()
    $ day_time()
    pause 2
    show blinking
    window show
    $ save_name = ("Лимб. \nОтрицание")
    $ limb_root_name('endless', 'end_summer')

    "[pl_ell]"
    "Сознание возвращалось ко мне медленно и неохотно, тягучее, будто патока. "

    scene bg white with flash
    play ambience ambience_int_cabin_day fadein 5

    "В глаза бил свет. Ничего толком разглядеть не могу, всё расплывается[pl_ell]"
    "Я затряс головой, пытаясь выбить из разума сонливость. Ощущение, будто спал веками напролёт[pl_ell]"

    show blinking

    "Я моргнул, и мой взгляд наконец-то сфокусировался на[pl_ell]"

    $ persistent.sprite_time = 'day'
    scene bg int_house_of_mt_awake with dissolve2
    pause 11
    show us smile sport with dissolve

    us "Ну доброе утро, засоня! Давай быстрее собирайся!"
    plme_bl "Ку[pl_ell] куда[pl_ell] кто ждёт[pl_ell]"
    "Улыбчивая мордашка никуда не девалась, хотя я всё ждал подвоха. "
    "И тут до меня наконец начало доходить."
    "Неужели?.. Неужели я победил?!"
    "Я собрался было вскочить, заорать от радости и сграбастать Ульяну в объятия[pl_ell]"

    play sound sfx_angry_ulyana
    show us angry with dspr

    us "Ну давай ты быстрее, мы же всё пропустим! Сколько можно спать?!"
    "Лишившись вдруг всех сил, я слабым голосом спросил, сколько спал."

    show us laugh with dspr

    "Ульяна снова засияла улыбкой:"
    us "Да всего минут десять, хе-хе-хе[pl_ell]"
    plme_bl "[pl_ell]"
    plme_bl "[pl_ell]ага."

    with vpunch

    plme_bl "Сколько?!"

    scene bg black
    with limb_neon_flash
    pause 3

    jump limb_fucking_final

label limb_zaebal_codera:

    scene bg black
    $ persistent.timeofday = 'secret'
    $ save_name = ("Лимб. \nСценарист заколебал кодера")
    $ limb_root_name('secret', 'mush')
    show un smile pioneer at fright
    with dissolve2
    play music music_list["sparkles"] fadein 3
    play sound sfx_limb_magic
    scene bg limb_space_start
    show un smile pioneer at fright:
        alpha 0.8

    plar "Поздравляем, вы нашли один из секретов Лимба.{w=1} Получено:{w=0.5} Гриб Метафоричности!"
    plar "Данную сцену должен был писать кодер, но у него резко появились неотложные дела. Поэтому, к сожалению, она далеко не так хороша, как могла бы быть."
    plar "По результатам опроса в группе выиграла Лена, поэтому именно она расскажет вам сказку."
    plar "Предупреждение: далее следует много текста, причём без шуток, насилия, обнажёнки или скримеров. Скучная секретная ветка, чего вы хотели?"
    plar "Предупреждение: эта сказка категорически не рекомендуется к прочтению лицам с диагносцированным СПГС, так как может привести к \"эффекту Кодзимы\"."

    stop music fadeout 3
    scene bg ext_camp_entrance_dark_2
    show anim limb_space:
        alpha 0.5
    show un smile pioneer at fright:
        alpha 0.8
    with dissolve2
    show un grin pioneer at fright:
        alpha 0.8
    with dspr

    un "Спасибо, автор. Я буду вашим рассказчиком! Немножко волнуюсь[pl_ell]"

    window hide
    play music pl_uc_good_morning_morgan fadein 5
    show un normal pioneer at fright:
        alpha 0.8
    $ persistent.timeofday = 'alpha'
    $ set_mode_nvl()
    window show

    un "Тело испытывало боль."
    "Оно изнывало от разрывающих на куски болезненных приступов."
    "К тому же на поверхности было некомфортно. Яркий свет слепил, жар терзал кожу, а шум вокруг - оглушал."
    "Тело страстно желало спрятаться. Залечь в темноте, исчезнуть, умереть и никогда больше не чувствовать."
    "Но оно не могло сосредоточиться и слепо брело, надеясь на скорое забвение[pl_ell]"
    "[pl_ell] пока не почуствовало пьянящую прохладу. Боль на краткий миг отступила, тело сосредоточилось и смогло определить источник. Это была глубокая, беспросветно черная пещера, судя по всему, уходящая глубоко под землю."
    "Никто по доброй воле не пошел бы туда. Но тело не раздумывая бросилось в спасительный мрак - и исчезло."
    "Спускаясь все ниже в темноту, тело не замечало движений вокруг. Не замечало, что ее осторожно окружают, что плетут вокруг сеть. Не замечало, что двигаться все сложнее и сложнее. А может быть, ему просто было все равно."
    "Пауки окружили тело, неподвижно стоящее, опустившее руки, затем атаковали."
    "Пауки бежали по гудящим нитям паутины, подбирались снизу по земле, сыпались гроздьями из темноты. Они были разного размера, двигались с разной скоростью, но всех объединяла одна цель."
    "Тело упало."
    "Пауки могут съесть тело человека за неделю. Не все пауки, не каждое тело. Но ЭТИ могли."
    "Тело - то, что от него осталось - лежало в темноте. Они привыкли друг к другу: они все - тело, темнота и пауки."
    "Последние лениво ползали по костям, кое-как скрепленным редкими сухожилиями. Большой паук медленно перебирал лапами, скрываясь где-то в грудной клетке."
    "Тело не чувствовало боли. Оно вообще ничего не чувствовало. Оно стало скелетом."
    "Глазницы черепа были затянуты паутиной. Мелкие паучки шныряли по зрительным путям, возможно, надеясь еще что-нибудь отравить или укусить. Часть из них добралась до чудом уцелевшего клочка сердца, где паучиха успела свить гнездо."
    "А ведь этот жалкий серый кусочек раньше пылал, любил и ненавидел, жил[pl_ell]"

    nvl clear

    "В безмолвной темноте прозвучал удар. Земля под скелетом задрожала."
    "Членистоногие замерли. Большой паук высунулся изо рта и раздраженно щелкнул жвалами."
    "И - еще раз удар, затем еще. Пауки встревоженно забегали, стараясь спрятаться в черепе, тазу, между ребрами. Скелет лежал."
    "Сверху посыпалась земля. Часть пауков неохотно покинула скелет и растворилась в темноте."
    "И был последний удар, сильнее предыдущих."
    "И упал луч света в подземное царство."
    "Пауки бросились в рассыпную. Луч падал прямо на глазницы черепа. Ее жители в ужасе забились поглубже в черепную коробку. Паутина медленно таяла в ярком сиянии."
    "Скелет лежал."
    "Вниз снова осыпалась почва, и луч превратился в столб света. Он ослеплял. Он был чрезмерен. Он был неуместен здесь, в царстве смерти. "
    "Он неумолимо напоминал о празднике жизни; о том, что ничто не вечно, что все проходит и меняется. Он освещал грудную клетку скелета, изгоняя запоздалых пауков, тянущих за собой шлейфы паутинок."
    "Свет заполнял огрызок сердечной мышцы, и начинало казаться, что оно живое, и вот-вот сократится."
    "Очевидно, этого не могло произойти, ведь тело давно умерло."
    "Или?.."

    nvl clear

    "В безмолвном свету прозвучал удар."
    "А затем ЕЩЕ ОДИН."
    "И ЕЩЕ ОДИН."
    "И ЕЩЕ."
    "Скелет с трудом встал."
    "Он прижал руку к груди, где вновь забилось чудом ожившее сердце, и осторожно сделал первый шаг."
    "Затем ЕЩЕ ОДИН."
    "И ЕЩЕ ОДИН."
    "И ЕЩЕ."
    "Скелет шел к свету, вытряхивая последних непрошенных квартирантов."
    "Скелет шел к свету, жизни, любви и надежде."

    window hide
    $ persistent.timeofday = 'secret'
    $ set_mode_adv()
    window show

    un "Понравилась сказка? Интересно, о чём она? Может быть, в ней вообще нет смысла? И автор просто издевается? Или это графомания, в которой можно утонуть, как в озере?"
    un "Решать тебе."
    un "А теперь хоп!"

    window hide
    play sound sfx_limb_ahahaha
    pause 0.5
    with limb_neon_flash
    $ day_time()
    return

label limb_fucking_final:

    window hide
    $ day_time()
    $ save_name = ("Лимб. \nЭта херь наконец-то окончена!")
    scene cg limb_picture_start
    pause 2
    show pl_finalcut_1 with dissolve2
    $ renpy.pause()
    hide pl_finalcut_1 with dissolve
    show pl_finalcut_2 with dissolve2
    $ renpy.pause()
    hide pl_finalcut_2 with dissolve
    show pl_finalcut_3 with dissolve2
    $ renpy.pause()
    hide pl_finalcut_3 with dissolve
    show pl_finalcut_4 with dissolve2
    $ renpy.pause()
    hide pl_finalcut_4 with dissolve2
    pause 5
    call screen limb_final_qte
    screen limb_final_qte:
        modal True
        add "limb_qte_F1" xalign 0.44 yalign 0.425
        key 'f' action [Hide("limb_final_qte"), Show("limb_final_success")]
        key 'F' action [Hide("limb_final_qte"), Show("limb_final_success")]
        key 'а' action [Hide("limb_final_qte"), Show("limb_final_success")]
        key 'А' action [Hide("limb_final_qte"), Show("limb_final_success")]
        timer 1 action [Hide("limb_final_qte"), Jump("limb_hotline")]
    screen limb_final_success:
        add "limb_qte_F2" xalign 0.44 yalign 0.425
        timer 1 action [Hide("limb_final_success"), Jump("limb_fucking_final_dop")]

label limb_fucking_final_dop:

    scene bg black
    pause 1
    play ambience ambience_int_cabin_day fadein 3
    scene bg int_house_of_mt_day
    show us laugh sport:
        anchor (0.5, 0.5)
        pos (0.5, 0.5)
        pause 2
        ease 1 xpos 1.2
    with dissolve2
    pause 1
    window show

    "Не дожидаясь меня, Ульяна выскочила на улицу."

    scene bg int_house_of_mt_day:
        ease 3 xalign 0.99 zoom 1.3

    "Я с трудом подошёл к двери, будто не давая себе развалиться на части. Как же всё болит, и особенно голова..."
    "Хм..."

    play music pl_dn_eternity
    window hide
    show cg d2_mirror with flash
    pause 1
    window show

    "Развернувшись, я распахнул дверцы шкафа и долго всматривался в своё лицо, которое за прожитые в воображении годы вовсе перестало видеться моим."
    "Что я пытаюсь высмотреть?{w=1} Розовые глаза?{w=1} Черты лица робота?{w=1} Щупальца? "
    "Кем бы ни была Царица... встречу ли я её когда-нибудь ещё?"
    "И что такое эти лагеря?"
    "Как устроен этот мир вообще?"
    "Что я вообще помню, что знаю и что - забыл?"
    "О ком говорил Пионер? О Вожатом, о Юле и о ком-то ещё?"
    "Кто та красноволосая девушка, смутно напоминающая Лену?"

    scene bg int_house_of_mt_day
    with flash
    pause 1

    "Я тихонько застонал.{w=1} Как же много вопросов... "
    "Возможно, сейчас в лагере как раз есть те, кто может дать мне ответ на этот вопрос. Юля... Пионер... "
    "Как странно относиться к этому чудику с теплотой."
    "Вспомнился диалог с Пионером, который был, наверное, пару минут назад... А кажется - вечность. "
    "Как в фильме \"Начало\", короче."
    "Мой взгляд упал на красный, пионерский, типичнейший галстук. "

    scene bg int_house_of_mt_blur with Dissolve(10)

    "Простая проверка реальности происходящего, говоришь?"
    "А почему бы и нет? "
    "Я подхватил красную ткань, глубоко вдохнул, подбросил её в воздух и..."
    "Интересно, что Царица имела в виду, спрашивая, буду ли я её другом?.."

    stop music fadeout 3

    plme_bl "Стоп."

    play sound sfx_limb_gate
    scene bg black
    with dissolve
    $ persistent.limb_story_end = True
    call screen limb_timer_menu_jump
    screen limb_timer_menu_jump:
        timer 10 action [Hide("limb_timer_menu_jump"), Jump("limb_hotline")]

label limb_hotline:

    window hide
    scene bg ext_hotline at limb_shake
    show pl_moto_hotline at limb_moto_pos
    play music pl_dn_obvious fadein 2
    show pl_endless_1 at limb_titer()
    pause 5
    hide pl_endless_1
    show pl_endless_2 at limb_titer(1.5)
    pause 3.5
    hide pl_endless_2
    show pl_endless_3 at limb_titer(5)
    pause 7
    hide pl_endless_3
    show pl_endless_4 at limb_titer(4)
    pause 6
    hide pl_endless_4
    show pl_endless_5 at limb_titer(4)
    pause 6
    hide pl_endless_5
    show pl_endless_6 at limb_titer(5)
    pause 7
    hide pl_endless_6
    show pl_endless_7 at limb_titer(1)
    pause 3
    hide pl_endless_7
    show pl_endless_8 at limb_titer(5)
    pause 7
    hide pl_endless_8
    show pl_endless_9 at limb_titer(5)
    show limb_ach_pl_fin at limb_get_achievement(10)
    pause 7
    hide pl_endless_9
    show pl_endless_10 at limb_titer(5)
    pause 7
    hide pl_endless_10
    show pl_endless_11 at limb_titer(5)
    pause 7
    hide pl_endless_11
    show pl_endless_12 at limb_titer(1)
    pause 3
    hide pl_endless_12
    scene anim limb_logo with Dissolve(5)
    pause 2
    scene bg black with Dissolve(3)
    show limb_eff_butterflies_darkness:
        anchor (0.5, 0.5)
        pos (-0.1, 0.5)
        ease 8 pos (1.7, 0.5)
        ease 0 alpha 0
    with dissolve
    pause 2
    scene bg black with dissolve
    jump limb_menu
