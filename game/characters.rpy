# File for defining characters

# stop talking code

# TODO: #1 implement automatic mouth animation stopping when they are not talking

define p = Character("Posty", who_color="#5282f1", image="posty")

image posty neutral:
    "talksprites/posty/posty_neutral_open.png"
    zoom 2.2
    xalign -0.05
    pause 0.2
    "talksprites/posty/posty_neutral_close.png"
    pause 0.2
    repeat

define yd = Character("Yellow Diamond", who_color="#ffff00", image="yd")

image yd:
    "talksprites/yd_open.png"
    zoom 1.2
    xalign 1.0
    yalign 0.0
    pause 0.2
    "talksprites/yd_close.png"
    pause 0.2
    repeat

# Non-canonical scene for testing stuff. Players should never see this in the final game.

label chartest:

    scene bg room with fade

    show posty neutral
    show yd
    p "Welcome to the character test room."
    yd "I don't feel very welcome tbh!"

    