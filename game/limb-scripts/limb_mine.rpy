init python:
    limb_mine_map = {
                    "1":{
                        "1":["3","2"],
                        "2":["3","2"],
                        "3":["3","2"]
                        },
                    "2":{
                        "1":["4","13"],
                        "4":["13","1"],
                        "13":["1","4"]
                        },
                    "3":{
                        "1":["halt","5"],
                        "5":["1","halt"],
                        "halt":["5","1"]
                        },
                    "4":{
                        "2":["5","6"],
                        "5":["6","2"],
                        "6":["2","5"]
                        },
                    "5":{
                        "3":["7","4"],
                        "4":["3","7"],
                        "7":["4","3"]
                        },
                    "6":{
                        "4":["9","12"],
                        "9":["12","4"],
                        "12":["4","9"]
                        },
                    "7":{
                        "5":["10","8"],
                        "8":["5","10"],
                        "10":["8","5"]
                        },
                    "8":{
                        "7":["10","9"],
                        "9":["7","10"],
                        "10":["9","7"]
                        },
                    "9":{
                        "8":["11","6"],
                        "6":["8","11"],
                        "11":["6","8"]
                        },
                    "10":{
                        "7":["halt","8"],
                        "8":["7","halt"],
                        "halt":["8","7"]
                        },
                    "11":{
                        "9":["exit","12"],
                        "12":["9","exit"]
                        },
                    "12":{
                        "13":["6","11"],
                        "6":["11","13"],
                        "11":["13","6"]
                        },
                    "13":{
                        "2":["12","coalface"],
                        "12":["coalface","2"],
                        "coalface":["2","12"]
                        }
            }

    def limb_mine_eval(direction):

        global point
        global previous_point
        global halt_visited
        global coalface_visited
        global back_to_start
        global mine_route
        global first_turn

        if direction == "left":
            old_point = point

            point = limb_mine_map[point][previous_point][0]
            previous_point = old_point
        elif direction == "right":
            old_point = point

            point = limb_mine_map[point][previous_point][1]
            previous_point = old_point

        if point == "exit":
            renpy.jump("limb_mine_exit")
        elif point == "coalface":
            point = "13"
            previous_point = "coalface"
            renpy.jump("limb_mine_coalface")
        elif point == "halt":
            if previous_point == "10":
                point = "3"
                previous_point = "halt"
                renpy.jump("limb_mine_halt")
            elif previous_point == "3":
                point = "10"
                previous_point = "halt"
                renpy.jump("limb_mine_halt")
        elif back_to_start and point == "1":
            renpy.jump("limb_mine_return_to_start")
        else:
            back_to_start = True
            renpy.jump("limb_mine_crossroad")

label limb_mine:

    $ point = "1"
    $ previous_point = "1"
    $ halt_visited = False
    $ coalface_visited = False
    $ back_to_start = False
    $ first_turn = True

    show screen limb_mine_timer
    screen limb_mine_timer:
        modal False
        timer 60 action Jump("limb_mine_loss")

    jump limb_mine_crossroad

label limb_mine_crossroad:

    $ persistent.sprite_time = "night"
    scene bg int_mine_crossroad
    with fade

    if not first_turn:
        "И куда теперь?"

    menu:
        "Налево":
            $ first_turn = False
            $ limb_mine_eval("left")
        "Направо":
            $ first_turn = False
            $ limb_mine_eval("right")

label limb_mine_return_to_start:

    $ persistent.sprite_time = "night"
    scene bg int_mine_crossroad
    with fade

    window show
    "Я вернулся к чёртовому началу!"
    window hide

    menu:
        "Налево":
            $ limb_mine_eval("left")
        "Направо":
            $ limb_mine_eval("right")

label limb_mine_coalface:

    $ persistent.sprite_time = "night"
    scene bg int_mine_coalface
    with fade
    window show

    if coalface_visited:
        window show
        "Как выбраться?{w=1} Куда бежать?! "
        window hide
        jump limb_mine_crossroad

    "Я забежал в тупик, чёрт!"
    window hide

    $ coalface_visited = True
    jump limb_mine_crossroad

label limb_mine_halt:

    $ persistent.sprite_time = "night"
    scene bg int_mine_halt
    with fade

    if halt_visited:
        window show
        "Здесь я уже был."
        window hide
        jump limb_mine_crossroad

    window show
    plme "Проклятье!"
    "Я метался как испуганный кролик."
    window hide

    $ halt_visited = True

    jump limb_mine_crossroad

label limb_mine_loss:

    $ _window_hide(vpunch)
    $ renpy.pause()
    $ LRed_text = 'НЕЕЕЕТ!!!'

    show LNOOO LRed_text:
        zoom 1 align (0.5, 0.5)
        ease 0.5 zoom 1.2
        ease 0.5 zoom 1
        repeat
    with flash
    play sound sfx_scary_sting

    $ renpy.pause()

    scene bg black with limb_pixel_2
    jump limb_prolog
