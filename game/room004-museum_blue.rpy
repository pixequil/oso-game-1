# todo: #32 blue exhibit conversation background

# #113
# todo: image museum_blue_p_rusty
# todo: image museum_blue_p_opened
# todo: image museum_blue_p_missing

image bg museum_blue_top:
    "map-bgs/museum_blue_top_default.png"
    zoom 1.0

image redcash:
    "items/redcash.png"
    xalign 0.5
    yalign 0.5
    zoom 3.0

image cash_bundle_1:
    "items/cash_bundle_1.png"
    truecenter
    zoom 1.5

image painting_blue:
    "items/blue_exhibit_main_painting.png"
    truecenter
    zoom 0.5

image ladle_empty:
    "items/ladle_empty.png"
    xalign 0.5
    yalign 0.5
    zoom 0.6

image ladle_full:
    "items/ladle_full.png"
    xalign 0.4
    yalign 0.5
    zoom 0.6

image rusty_gate:
    "items/rusty_gate.png"
    xalign 0.75
    yalign 0.6
    zoom 1.25

image rusty_gate_broken:
    "items/rusty_gate_broken.png"
    xalign 0.75
    yalign 0.6
    zoom 1.25

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

    elif bt_distracted:
        show posty neutral
        show bluetile scared behind redtile:
            xzoom -1.0
            xpos 0.75
        p "_" #119 red tile urges you to quickly do what you need to do, while continuing to distract blue tile
        jump museum_blue

    elif item.ladle_full and miso_blocked:
        show posty neutral
        show redtile 
        p "Hey Red, mind if I ask you a favour!" #118
        redtile "Sure, whatcha want me to do?"
        p concerned "I attempted to 'add' some colour to the exhibition, but Bluey here stopped me."
        redtile "Ah of course, Blue would never let his precious little pieces get harmed."
        p suspicious "Well, I noticed that the guy gets really passionate when it comes to blue stuff, so I was hoping you could distract him with a couple of remarks."
        redtile "No way."
        p astonished "Come on, you can get revenge for the Red Exhibit, just some small talk!"
        redtile "When it comes to the colour blue, it is never small talk."
        redtile "That guy can be so hung up on that it is annoying."
        redtile "One more hour of him whining and I am leaving."
        p concerned "What would it take?"
        redtile "Maybe some cash... If I have to deal with him, atleast I should be fairly compensated for my sacrifice."
        label .rt_money:
            menu:
                "Offer cash." if (money > 0) and (quest.moneys == False):
                    show cash_bundle_1
                    p "_" # red tile refuses the regular cash.
                    hide cash_bundle_1
                    jump .rt_money
                "Offer red cash.":
                    show redcash
                    p "_" # red tile takes the red cash.
                    $ item.red_cash = False
                    $ bt_distracted = True
                    jump museum_blue

    elif item.ladle_full:
        show posty neutral
        p "_" #130 red tile refuses to use the ladle a second time, urging posty to do it
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
        show posty concerned
        show bluetile scared
        p "What is wrong, feeling blue?"
        bluetile scared "It's the painting, it is gone!"
        p sad "Oh whaat nooo, you know where it went?"
        bluetile "God dammit no! I WOULDN'T BE LOOKING AROUND FOR IT IF I HAD IT!"
        p confused "Damn calm down dude, think where you last seen it and work backwards from there."
        p "That is what I do when I lose my extremely valuable possessions."
        bluetile annoyed "Ooohh it is that maroon loser who took my precious painting : that cultural ignoramus was never open to anything that didn't rhyme with zred or mrimson!"
        p concerned "language"
        bluetile annoyed "I was always accommodating to his wishes and desires about the place; hell I was considering adding a red piece to even it out."
        bluetile "But the scarlet boor just went and declared war on me! That won't stand on my watch."
        p "anyway good luck with the painting"
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
        show ladle_full
        p concerned "Aighty, here it goes!" #121
        hide ladle_full
        show bg museum_blue_p_opened
        "You repeat Red Tile's crime, splashing more miso soup on the painting!"
        p angry "Drat, I missed."
        p annoyed "All I hit was this gate that has rusted open-"
        p astonished quiet "!!"
        p happy "I just got an idea.."
        show bg museum_blue_p_missing
        show painting_blue #122
        "You got an {b}art piece{/b}!{p}Whether you love it or hate it, there is no denying that it makes great use of the azure colour." #127
        hide painting_blue
        p happy "Ohohoho I can't wait to see Bluey's face!"
        hide posty with moveoutleft
        show bluetile behind posty
        $ renpy.transition(moveinleft, layer="master") #prevents interruption of the text window
        $ item.ladle_full = False
        $ item.painting_blue = True
        $ quest.painting_blue = True
        $ bt_distracted = False
        $ paintings += 1
        bluetile annoyed "I swear I have never seen a more unqualified person in my life; he can't appreciate their subtle nuances-"
        bluetile annoyed quiet "..."
        bluetile scared "Where did the painting go?"
        bluetile scared "This exhibit has been... vandalized"
        bluetile scared "My piece, gone."
        bluetile annoyed "Who did this?"
        bluetile annoyed "Who dared to lay their fingertips on this masterpiece??"
        bluetile annoyed "I'll find that thief and stuff them with so much legalese they will be speaking it."
        bluetile annoyed "DO YOU KNOW WHO I AM?!"
        bluetile annoyed "I HAVE A WHOLE BOOK OF LAWYERS READY TO LITIGATE YOUR EXISTENCE, CAN YOU HEAR ME?!"
        bluetile annoyed "I swear if that piece doesn't comeback here with thirty minutes I'll send the dogs out."
        bluetile annoyed "Aaaaaaaaaaaaaarggh"
        jump museum_blue

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


