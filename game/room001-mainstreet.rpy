label firstscene:

    scene bg mainstreet
    show posty neutral

    p "_"

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
            jump yd_hints
        

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
