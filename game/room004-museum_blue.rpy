# todo: #32 blue exhibit conversation background

# #113
# todo: image museum_blue_p_rusty
# todo: image museum_blue_p_opened
# todo: image museum_blue_p_missing

image redcash:
    "items/redcash.png"
    xalign 0.5
    yalign 0.5
    zoom 3.0

label museum_blue:
    if saw.blue == False:
        jump .redcash
    else:
        scene bg museum_blue_top # TODO: #33 blue exhibit imagemap (needs illustration)
        show posty neutral

        p "_"

        menu:
            "Talk to Blue Tile":
                jump .bt
            "Talk to Red Tile":
                jump .rt
            "Return to the entrance.":
                jump museum_entrance

label .redcash:
    scene bg museum_blue
    show posty neutral
    p "_" # TODO: #34 Posty finds Red Cash on the floor upon entering the blue room.    
    
    show redcash
    $ saw.blue = True
    $ item.red_cash = True
    "You got the {b}{color=#de474e}red cash{/color}{/b}!{p}It\'s money but it\'s red."
    jump museum_blue
        
label .rt:
    scene bg museum_blue
    show redtile

    if saw.redtile == False:
        show posty neutral
        $ saw.redtile = True
        p "_" # TODO: #40 first Red Tile conversation. Red Tile is A grumpy character that absolutely hates this exhibit, and is mostly here out of spite. They have previously thrown some Miso Soup at one of the paintings, leaving its gate rusted, but managed to avoid the blame for it. Regardless, they’re not trying to draw too much attention to themselves. They also have some choice words about Blue Tile.
        redtile "_" # Red Tile gives you the soup ladle, They’re very interested in getting rid of the incriminating evidence.
        $ item.ladle_empty = True
        show ladle_empty # TODO: #41 ladle, empty and filled with soup versions
        "You got the {b}ladle{/b}!{p}You feel guilty just carrying it..."
        redtile "_"
        jump museum_blue

    elif item.ladle_empty:
        show posty neutral
        p "_" # todo: #44 short conversation with red tile
        jump museum_blue

label .bt:
    if saw.bluetile == False:
        show bg museum_blue_p_rusty
        show posty neutral
        $ saw.bluetile = True
        p "_" #114 Blue Tile explains their whole deal, while Posty is captured by the compulsion to take the painting
        jump museum_blue

