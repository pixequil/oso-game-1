image bg mainstreet_top:
    "bgs/mainstreet_top.png"

image butterfly_package:
    "items/butterfly_package.png"
    zoom 0.5
    truecenter

image ladle_full:
    "items/ladle_full.png"
    xalign 0.5
    yalign 0.5
    zoom 0.6

label firstscene:

    scene black
    ""
    p "And this is going to..."
    
    show bg mainstreet # TODO: #23 main street conversation bg
    $ renpy.transition(dissolve, layer="master")
    show posty neutral
    show btnet 

    extend " {b}{color=#c0d4e7}Crayon Box{/color}{/b}, at {i}1189 Brick Ave{/i}, right?"
    btnet "That's right!"
    p quiet "Okay, that's..."
    show posty astonished before
    extend " ..!"
    p astonished anim "THAT'S THE OSO DOME!!!"
    btnet "Yeah, it's my biggest job yet!"
    p -anim "And you want ME to deliver it??"
    btnet "Of course! I can always trust you for a swift and intact delivery, Posty."
    p happy "I'll take care of it right away! I have no other deliveries today, so, consider it express with no extra charge!"

    show butterfly_package
    "Received the {b}Butterfly Package{/b}!{p}There is something fluttering inside..!"
    $ item.butterfly_package = True
    hide butterfly_package

    btnet "Best of luck!"
    p "Thanks! Not that I'll need it, since it's just a short walk west of here."
    btnet "I'll leave you to it then."
    hide btnet with moveoutright
    p quiet "..."
    p astonished "Wow..! I get to deliver to the OSO Dome!"
    p "I bet {b}{color=#c0d4e7}Crayon Box{/color}{/b} is gonna use this in a challenge or something!"

    show toasty turned2
    $ renpy.transition(moveinbottom, layer="master")
    p "I can't believe I get to be involved in Open Source Objects!!!"
    t "La la la, just minding my own business..." 
    t annoyed "Oh. {i}You're{/i} here. Didn't see ya."
    p neutral "Hi Toasty."
    t smug "Guess you got another job, huh."
    p "You were listening?"
    t smug2 "For that stoopid show, what was it?{w}\nOpen Source{w=0.4} Items{w=0.4} or whatever."
    t smug5 "Well, I don't even care!"
    p "K."
    t pointandlaugh "I bet you'll trip and fall on your way there!"
    p "I have to go deliver this now. See you later Toasty."
    t laugh "Hah, well, don't come crying to me if you need help with anything!"

    hide toasty with moveoutright

    p "Welp. Better get going!"

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
            jump .btnet 
        "Dolly":
            jump dolly # in money.rpy
        "Miso Soup":
            jump .miso
        "Brand Soda" if (party_bs == False) and (quest.bs == False):
            jump .brandsoda
        "Toasty":
            call toasty_hints
            jump mainstreet
        "Tooly":
            jump .tooly #
        "Yellow Diamond" if quest.bs == False:
            jump .yd
        "Yellow Diamond & Brand Soda" if quest.bs:
            jump .yd
        

label .go:

    menu:
        "Music Store":
            jump musicstore #
        "Art Museum":
            jump museum_entrance 
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

    p "Oh, hey Brand Soda."
    bs "Hey Posty."
    bs "Say, I have a favor to ask you..."
    bs "You see, I wish to be the next big thing around these parts..."
    bs "You know, reach for the stars!"
    p "I see. And how do you want me to help?"
    bs "Well, I was wondering if you could take me around the town for some marketing!"
    p "Hmm, well, I have a package to deliver, but..."
    p happy "Sure! I don't see why not.."

    show bs follow with move:
        xalign 0.35
    
    bs "Sweet, thanks!"
    $ party_bs = True
    "{b}{color=#df7dff}Brand Soda{/color}{/b} joined your party!"

    bs "Also, I forgot to mention this..."
    bs "But I am, like, banned from every street and establishment in this town."
    bs "Hope that's not a problem!"
    p astonished quiet "..."
    p confused "Uh, of course not!"

    jump mainstreet

label .yd:
    scene bg mainstreet
    show posty neutral
    show yd
    if party_bs:
        jump .yd_bs_money
    elif quest.bs:
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
    $ quest.bs = True
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
    show miso # TODO: #45 Miso Soup talksprite

    if party_bs:
        show posty neutral
        show bs follow behind posty
        p "_" # todo: #110 should be short! Brand Soda does not want to Miso for whatever reason. (this prevents there from needing to be 3 unique conversations)
        jump mainstreet
    
    elif (item.ladle_empty == False) and (miso_took == False):
        show posty neutral
        p "_" # TODO: #46 miso soup conversation before youve taken any soup
        miso "_"
        jump mainstreet
    
    elif item.ladle_empty and (miso_took == False):
        show posty neutral
        p "_" # TODO: #47 you take soup from Miso Soup 
        miso "_"
        $ item.ladle_empty = False
        $ item.ladle_full = True
        $ miso_took = True
        show ladle_full
        "You filled the {b}ladle{/b} with {b}miso soup{/b}!" # TODO: #48 describe soup-filled ladle
        miso "_"
        jump mainstreet

    elif miso_took and (quest_painting_blue == False):
        show posty neutral
        p "_" #TODO: #49 miso soup conversation after you've taken soup
        miso "_"
        jump mainstreet

    elif miso_took and quest_painting_blue:
        show posty neutral
        p "_" # todo: #50 miso soup conversation after splashing miso soup on painting
        miso "_"
        jump mainstreet

    else:
        show posty neutral
        p "Players should not see this text."

label .btnet:
    scene bg mainstreet
    show btnet
        
    if party_bs:
        show posty neutral
        show bs follow behind posty
        p "_" # todo: #109 

        jump mainstreet

    elif item.butterfly_package:
        show posty neutral
        p "_" # TODO: #53 talking to B.T. Net (does not progress the plot)
        btnet "_"

        jump mainstreet

    else:
        show posty neutral
        p "_" # TODO: #54 talking to B.T. Net after a successful delivery! (game is in win state)
        btnet "_"

        jump mainstreet

label .tooly:
    "this scene is not available yet." # when implemeting Tooly, remember to leave room for Brand Soda interactions.