#239 generi-chips

image bg janitors_top:
    "map-bgs/janitors_top.png"
    zoom 1.15
    yalign 0.2

image bg janitors:
    "dbgs/janitors_dbg.png"

image generichips:
    "items/generi-chips.png"
    xalign 0.1
    yalign 0.5
    zoom 0.8

transform lookatvend:
    xzoom -1.0
    xalign 0.6
    yalign 1.0

transform getvend:
    xzoom -1.0
    xalign 0.2
    yalign 1.0


label janitors:
    if saw.janitors == False:
        jump .sb1
    scene bg janitors_top
    show posty neutral
    p "_" #235 todo: janitors imagemap

    menu:
        "Squirt Bottle":
            jump .sb2
        "Vending machine":
            jump .vend
        "Get outta here":
            jump museum_food

label .vend:
    scene bg janitors
    show posty neutral at lookatvend
    p happy "Ooo a vending machine!"
    show sb with moveinright
    sb "Hey! Uh don't use that."
    p suspicious "Why? You said I could do anything."
    sb "Well- Not this."
    p neutral "What if I were to,"
    extend " say, I don't know..."
    extend happy " rat you out?"
    sb "NO!! Uhm- ugh!"
    sb "...Fine."
    p "Yay!"
    show posty at getvend with move
    show posty at lookatvend with move
    show generichips
    $ item.chips = True
    "You got the {b}Generi-Chips{/b}!" 
    "Generi-Chips: it has some nutrients."
    hide generichips
    p annoyed "Eww really? Generi-Chips??"
    sb "It's better than nothing!"
    p "Whatever, I'm keeping them in case I need it."
    jump janitors


label .sb1:
    scene bg janitors
    show posty neutral
    show sb
    $ saw.janitors = True
    sb "_" #236 Squirt Bottle confronts you about how you got in here
    p "_"
    jump janitors

label .sb2:
    scene bg janitors
    show posty neutral
    show sb
    sb "_" #237 repeat conversation with Squirt Bottle
    jump janitors
