#239 generi-chips

image bg janitors_top:
    "map-bgs/janitors_top.png"
    zoom 1.15
    yalign 0.2

image bg janitors:
    "dbgs/janitors_dbg.png"

transform lookatvend:
    xzoom -1.0
    xalign 0.6
    yalign 1.0

transform getvend:
    xzoom -1.0
    xalign 0.4
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
    p "_" # posty decides to get something from the vending machine.
    show posty at getvend
    show posty at lookatvend
    show generichips
    $ item.chips = True
    "You got the {b}Generi-Chips{/b}!" #240 describe
    hide generichips 
    p "_" # posty says she hates them! so she won't eat them.
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
