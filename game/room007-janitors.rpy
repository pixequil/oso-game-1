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

label .vend: #243
    scene bg janitors
    show posty neutral at lookatvend
    p "_" # posty looks at the vending machine
    show sb with moveinright
    sb "_" # Squirt Bottle comes over and confronts posty about the vending machine
    p "_" # posty explains that she wants a snack
    sb "_" # Squirt Bottle refuses to let her get a snack
    p "_" # posty threatens to rat out squirt bottle if she doesn't get a snack
    sb "_" # squirt bottle reluctantly agrees. interaction doesn't need to be this exact amount of lines
    show posty at getvend with move
    show posty at lookatvend with move
    show generichips
    $ item.chips = True
    "You got the {b}Generi-Chips{/b}!" 
    "Generi-Chips: it has some nutrients."
    hide generichips 
    p "_" # posty expresses disgust for this brand of chips, but is fine with keeping them in case she needs them for something
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
