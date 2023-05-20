# todo: #32 blue exhibit conversation background

image redcash:
    "items/redcash.png"
    xalign 0.5
    yalign 0.5
    zoom 3.0

label museum_blue:
    if saw_blue == False:
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
    $ saw_blue = True
    $ item_red_cash = True
    "You got the {b}{color=#de474e}red cash{/color}{/b}!" # todo: #42 describe red cash
    jump museum_blue
        
label .rt:
    scene bg museum_blue
    show posty neutral
    show redtile
    
    if saw_redtile == False:
        $ saw_redtile = True
        p "_" # TODO: #40 first Red Tile conversation. Red Tile is A grumpy character that absolutely hates this exhibit, and is mostly here out of spite. They have previously thrown some Miso Soup at one of the paintings, leaving its gate rusted, but managed to avoid the blame for it. Regardless, they’re not trying to draw too much attention to themselves. They also have some choice words about Blue Tile.
        rt "_" # Red Tile gives you the soup ladle, They’re very interested in getting rid of the incriminating evidence.
        $ item_ladle_empty = True
        show ladle_empty # TODO: #41 ladle, empty and filled with soup versions
        "You got the {b}ladle{/b}!" # todo: #43 describe ladle
        rt "_"
        jump museum_blue

    elif item_ladle_empty and (item_painting_blue == False):
        p "_" # todo: #44 short conversation with red tile
        jump museum_blue

