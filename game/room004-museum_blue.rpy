# todo: blue exhibit conversation background

label museum_blue:
    if item_red_cash == False:
        jump .redcash
    else:
        scene bg museum_blue_top # TODO: blue exhibit imagemap (needs illustration)
        show posty neutral

        p "_"

        menu:
            "Talk to Blue Tile":
                jump .bt
            "Talk to Red Tile":
                jump .rt

label .redcash:
    scene bg museum_blue
    show posty neutral
    p "_" # TODO: Posty finds Red Cash on the floor upon entering the blue room.    
    
    show redcash at truecenter:
        zoom 3.0
    $ item_red_cash = True
    "You got the {b}{color=#de474e}red cash{/color}{/b}!"
    jump museum_blue
        
