image bg mainstreet_top:
    "bgs/mainstreet_top.png"

label firstscene:

    scene bg mainstreet # TODO: #23 main street conversation bg

    show posty neutral
    show btnet

    p "_" # TODO: #7 conversation where BT Net gives Posty the butterflies
    btnet "_"

    show item butterfly_package # TODO: #10 needs image!
    "Received the {b}Butterfly Package{/b}!"
    $ item_butterfly_package = True
    hide item butterfly_package

    btnet "_" # parting remarks
    hide btnet with moveoutright
    p "_" # internal monologue

    show toasty neutral with moveinbottom
    t "_" # TODO: #8 conversation where Toasty implies you can use her for hints
    p "_"

    hide toasty with moveoutright

    p "_" # parting remarks?

label mainstreet:

    scene bg mainstreet_top with fade
    show posty neutral

    p "__" # TODO: #9 replace this choice tree with an imagemap that scrolls

    menu:
        "Talk to someone.":
            jump .talk
        "Go somewhere.":
            if party_bs:
                show bs follow behind posty
                bs "_" #TODO: #11 thing for Brand Soda to say to prevent you from leaving main street
                jump mainstreet
            else:
                jump .go

label .talk:

    menu:
        "B.T. Net":
            jump .btnet #
        "Dolly":
            jump dolly # in money.rpy
        "Miso Soup":
            jump .miso
        "Brand Soda" if (party_bs == False) and (quest_bs == False):
            jump .brandsoda
        "Toasty":
            call toasty_hints
            jump mainstreet
        "Tooly":
            jump .tooly #
        "Yellow Diamond" if quest_bs == False:
            jump .yd
        "Yellow Diamond & Brand Soda" if quest_bs:
            jump .yd
        

label .go:

    menu:
        "Music Store":
            jump musicstore #
        "Art Museum":
            jump museum_entrance #
        "Shady Back Alley":
            jump alley #
        "Park":
            jump park #
        "The Dome":
            jump dome

label .brandsoda:

    scene bg mainstreet
    show posty neutral
    show bs behind posty

    p "_" # TODO: #12 conversation where Brand Soda decides to follow you
    bs "_"

    show bs follow with move:
        xalign 0.35
    
    bs "__"
    $ party_bs = True
    "{b}{color=#df7dff}Brand Soda{/color}{/b} joined your party!"

    p "_"

    jump mainstreet

label .yd:
    scene bg mainstreet
    show posty neutral
    show yd
    if party_bs:
        jump .yd_bs_money
    elif quest_bs:
        jump .yd_bs_happy
    else:
        p "_" # TODO: #15 conversation where yd implies they want to get into advertising
        yd "_"

        jump mainstreet

label .yd_bs_money:
    show bs follow behind posty
    p "_" # TODO: #16 conversation where posty convinces yd to support Brand Soda. Brand Soda, grateful, gives Posty some money as thanks.
    yd "_"
    bs "_"

    show bs with move:
        xalign 0.65
    $ party_bs = False
    "{b}{color=#df7dff}Brand Soda{/color}{/b} left your party!"

    bs "_"

    $ money += 1
    $ quest_bs = True
    show cash_bundle_1
    $ renpy.transition(irisout, layer="master")
    "{b}{color=#df7dff}Brand Soda{/color}{/b} gave you {b}some money{/b}!"
    hide cash_bundle_1
    call money_get

    bs "_"
    jump mainstreet

label .yd_bs_happy:
    show bs behind yd:
        xalign 0.65
        yalign 1.0
    p "_" # TODO: #17 conversation with the now-satisfied yd and bs
    yd "_"
    bs "_"
    jump mainstreet

label .miso:
    scene bg mainstreet
    show posty neutral
    show miso # TODO: #45 Miso Soup talksprite

    if (item_ladle_empty == False) and (miso_took == False):
        p "_" # TODO: #46 miso soup conversation before youve taken any soup
        miso "_"
        jump mainstreet
    
    elif item_ladle_empty and (miso_took == False):
        p "_" # TODO: #47 you take soup from Miso Soup 
        miso "_"
        $ item_ladle_empty = False
        $ item_ladle_full = True
        $ miso_took = True
        show ladle_full
        "You filled the {b}ladle{/b} with {b}miso soup{/b}!" # TODO: #48 describe soup-filled ladle
        miso "_"
        jump mainstreet

    elif miso_took and (quest_painting_blue == False):
        p "_" #TODO: #49 miso soup conversation after you've taken soup
        miso "_"
        jump mainstreet

    elif miso_took and quest_painting_blue:
        p "_" # todo: #50 miso soup conversation after splashing miso soup on painting
        miso "_"
        jump mainstreet

    else:
        p "Players should not see this text."



