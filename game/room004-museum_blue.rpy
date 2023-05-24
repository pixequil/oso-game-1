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
            "Main Exhibit & Blue Tile" if (bt_distracted == False):
                jump .painting
            "Red Tile" if (bt_distracted == False):
                jump .rt
            "Main Exhibit" if bt_distracted:
                jump .painting
            "Red Tile & Blue Tile" if bt_distracted:
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

    if quest.painting_blue:
        show posty neutral
        p "_" #126 red tile after you steal the painting
        jump museum_blue

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

    elif item.ladle_full and miso_blocked:
        show posty neutral
        $ bt_distracted = True
        $ item.red_cash = False
        p "_" #118 red tile offers to distract blue tile in exchange for the red cash (and because they want that painting harmed)
        jump museum_blue

    elif bt_distracted:
        show posty neutral
        show bluetile scared
        p "_" #119 red tile urges you to quickly do what you need to do, while continuing to distract blue tile
        jump museum_blue


label .painting:
    if saw.bluetile == False:
        show bg museum_blue_p_rusty
        show posty neutral
        show bluetile giddy
        $ saw.bluetile = True
        p "_" #114 Blue Tile explains their whole deal, while Posty is captured by the compulsion to take the painting
        if item.ladle_full:
            jump .painting_ladle_blocked
        else:
            p "_" # posty says bye
            jump museum_blue

    elif quest.painting_blue:
        show bg museum_blue_p_missing
        show posty neutral
        show bluetile scared
        p "_" # blue tile after the painting is stolen (still doesn't know posty did it)
        jump museum_blue

    elif saw.bluetile and (item.ladle_full == False):
        show bg museum_blue_p_rusty
        show posty neutral
        show bluetile giddy
        p "_" #123 revisiting blue tile casually before anything happens
        jump museum_blue

    elif item.ladle_full:
        jump .painting_ladle

label .painting_ladle:
    if bt_distracted:
        show bg museum_blue_p_rusty
        show posty neutral
        p "_" #121 scene where posty, alone, splashes miso soup on the painting and takes the painting on impulse now that the bars are rusted away. blue tile shows up, too late, and is upset about it.
        "You repeat Red Tile's crime, splashing more miso soup on the painting!"
        show bg museum_blue_p_opened
        p "__" # posty takes the painting.
        show bg museum_blue_p_missing
        show painting_blue #122 blue exhibit main painting on display
        "You got an {b}art piece{/b}!" #127 describe blue painting
        $ item.ladle_full = False
        $ item.painting_blue = True
        $ quest.painting_blue = True
        $ bt_distracted = False
        $ paintings += 1
        hide painting_blue
        show bluetile scared behind posty
        $ renpy.transition(moveinleft, layer="master") #prevents interruption of the text window
        bluetile "_" # blue tile freaks out
        p "_" # posty decides to quickly leave.

    else:
        jump .painting_ladle_blocked

label .painting_ladle_blocked:
    show bg museum_blue_p_rusty
    show posty neutral
    show bluetile scared
    $ miso_blocked = True
    "You attempt to repeat Red Tile's crime, splashing more miso soup on the painting."
    p "_" #116 blue tile stops you from splashing miso soup on the painting when you try to.
    jump museum_blue


