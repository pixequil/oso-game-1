# File for defining characters

define p = Character("Posty", who_color="#5282f1", image="posty")

image posty neutral:
    "talksprites/posty/posty_neutral_open.png"
    zoom 2.2
    xalign -0.05
    pause 0.2
    "talksprites/posty/posty_neutral_close.png"
    pause 0.2
    repeat

# Non-canonical scene for testing stuff. Players should never see this in the final game.

label chartest:

    scene bg room with fade

    show posty neutral
    p "Welcome to the character test room."