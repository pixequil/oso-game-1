

label firstscene:

    scene bg mainstreet

    show posty neutral
    show btnet

    p "_" # TODO: #7 conversation where BT Net gives Posty the butterflies
    btnet "_"

    show item butterfly_package # TODO: needs image!
    "Received the {b}Butterfly Package{/b}!"
    $ item_butterfly_package_flag = True
    hide item butterfly_package

    btnet "_" # parting remarks
    hide btnet with moveoutright
    p "_" # internal monologue

    show yd with moveintop
    yd "_" # TODO: #8 conversation where Yellow Diamond implies you can use them for hints
    p "_"

    hide yd with moveouttop

    p "_" # parting remarks?

label mainstreet:

    p "__" # TODO: #9 replace this choice tree with an imagemap that scrolls

    menu:
        "Talk to someone.":
            jump .talk
        "Go somewhere.":
            jump .go

label .talk:

    menu:
        "B.T. Net":
            jump .btnet
        "Dolly":
            jump .dolly
        "Miso Soup":
            jump .miso
        "Brand Soda":
            jump .brandsoda
        "Toasty":
            jump .toasty
        "Tooly":
            jump .tooly
        "Yellow Diamond":
            call yd_hints
            jump mainstreet
        

label .go:

    menu:
        "Music Store":
            jump musicstore
        "Art Museum":
            jump museum_entrance
        "Shady Back Alley":
            jump alley
        "Park":
            jump park
        "The Dome":
            jump dome
