init -1 python hide:

    if persistent.choices == None:
        persistent.choices = []

    persistent.hentai = False

    config.default_afm_time = 0

    config.default_afm_enable = None

    config_session = False





    _preferences.self_voicing = False




    config.developer = False

    want_label_select = False

    config.skip_indicator = False

    config.screen_width = 1920
    config.screen_height = 1080

    if not persistent._use_custom_menu:
        config.window_title = u"Бесконечное лето"
        config.name = "Everlasting Summer"
        config.version = "1.2"
    else:
        config.window_title = u"Бесконечное лето: Endless Horizons"
        config.name = "Everlasting Summer: EH"
        config.version = "0.9"




    import os
    os.environ['SDL_VIDEO_CENTERED'] = '1'

    config.window_icon = "images/misc/icon.png"
    config.windows_icon = "images/misc/icon.png"

    config.default_fullscreen = True

    config.has_autosave = True

    config.gl_resize = True

    config.default_text_cps = 50

    # config.mouse = { }
    # config.mouse["default"] = [
    #     ("images/misc/mouse/1.png",  0, 0)

    #     ]

    _game_menu_screen = "game_menu_selector"

    config.layers = ['underlay', 'master','mapoverlay', 'widgetoverlay', 'transient','screens','overlay']

    #config.main_menu_music = "sound/music/blow_with_the_fires.ogg"

    theme.roundrect(
        widget = "#003c78",
        widget_hover = "#0050a0",
        widget_text = "#c8ffff",
        widget_selected = "#ffffc8",
        disabled = "#404040",
        disabled_text = "#c8c8c8",
        label = "#ffffff",
        frame = "#6496c8",
        rounded_window = False,
        mm_root = "main_menu",
        gm_root = "#dcebff",
        less_rounded = True,       
        )


    config.has_sound = True
    config.has_music = True
    config.has_voice = True

    config.rollback_length = 1000
    config.hard_rollback_limit = 1000







    config.enter_transition = Dissolve(.25)
    config.exit_transition = Dissolve(.25)
    config.intra_transition = Dissolve(.25)
    config.main_game_transition = Dissolve(.25)
    config.game_main_transition = Dissolve(.25)
    config.end_splash_transition = Dissolve(.25)
    config.end_game_transition = fade
    config.after_load_transition = dissolve
    config.window_show_transition = Dissolve(.25)
    config.window_hide_transition = Dissolve(.25)

    config.quit_action = ui.gamemenus("_confirm_quit")

    def new_screenshot_callback(fn):
        renpy.notify(__("Saved screenshot as " + fn.rsplit("\\",1)[1]))

    config.screenshot_callback = new_screenshot_callback

init python: ## СБОРКА
    build.directory_name = "Everlasting_Summer-EH_0.9"
    build.executable_name = "Everlasting_Summer-EH"
    build.include_update = False
    build.classify('**debug.rpy**', None)
    build.classify('**hentai.rpy**', None)
    build.classify('**hentai.rpyc**', None)
    build.classify('**dev-mode.rpy**', None)
    build.classify('**dev-mode.rpyc**', None)
    build.classify('**~', None)
    build.classify('**.bak', None)
    build.classify('**.rpy', None)
    build.classify('**.bat', None)
    build.classify('**.txt', None)
    build.classify('**.bak', None)
    build.classify('**.rpy#', None)
    build.classify('**.log', None)
    build.classify('**/.**', None)
    build.classify('**/#**', None)
    build.classify('**/thumbs.db', None)
    build.classify('game/**.png', 'archive')
    build.classify('game/**.jpg', 'archive')
    build.classify('game/**.ogg', 'archive')
    build.classify('game/**.wav', 'archive')
    build.classify('game/**.mp3', 'archive')
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
