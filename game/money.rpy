
image cash_payment:
    "items/cash_payment.png"

image cash_loot:
    "items/cash_loot.png"
    zoom 0.5
image cash_loot_nav:
    "cash_loot"
    zoom 0.5

image cash_total = Composite(
    (400,200),
    (0,0), "cash_brandsoda",
    (400-260,50), "cash_bust",
    (150+20,100), "cash_alley",
    (60+20,120), "cash_main",
)

image cash_brandsoda = ConditionSwitch(
    "quest.bs == True", "cash_payment",
    "quest.bs == False", "hitboxf"
)
image cash_bust = ConditionSwitch(
    "quest.money_food == True", "cash_payment",
    "quest.money_food == False", "hitboxf"
)
image cash_main = ConditionSwitch(
    "item.cash_main == True", "cash_loot",
    "item.cash_main == False", "hitboxf"
)
image cash_alley = ConditionSwitch(
    "item.cash_alley == True", "cash_loot",
    "item.cash_alley == False", "hitboxf"
)

screen moneytest_buttons:
    vbox:
        textbutton "Brand Soda":
            action ToggleVariable("quest.bs")
        textbutton "Marble Bust":
            action ToggleVariable("quest.money_food")
        textbutton "Main Street":
            action ToggleVariable("item.cash_main")
        textbutton "Alley":
            action ToggleVariable("item.cash_alley")

label moneytest:
    scene bg room
    stop music

    "money test!"
    show cash_payment at truecenter
    "payment"
    hide cash_payment
    show cash_loot at truecenter
    "loot"
    hide cash_loot
    show screen moneytest_buttons
    show cash_brandsoda at truecenter
    show cash_bust at left
    show cash_main at right
    show cash_alley at topright
    "separately"
    hide cash_brandsoda
    hide cash_bust
    hide cash_main
    hide cash_alley
    show cash_total at truecenter
    "total"

    return


label money_get:
    "..."
    show cash_total at truecenter
    if money == 0:
        "A player should never see this text."
    elif money == 1:
        "You now have {b}some money{/b}!"
    elif money == 2:
        "You now have {b}some more money{/b}!"
    elif money == 3:
        "You now have {b}a lot of money{/b}!"
    elif money == 4:
        "You now have {b}{color=#ffff00}all of the money in the area{/color}{/b}!"
    if saw.dolly:
        "Nice! You needed this for that lootbox!"
    hide cash_total
    return

label dolly:
    $ last.mainx = 1.0
    scene bg mainstreet
    show dolly
    if party_bs:
        jump .dbs
    elif quest.moneys:
        jump .dlast
    elif saw.dolly == False:
        jump .dfirst
    else:
        jump .drepeat

label .dbs:
    show posty neutral
    p neutral "I don't think this'll work, but let's try it anyway."
    show bs follow behind posty with moveinleft
    bs "Heyyyyyyy Dolly! What do you say about-"
    dolly "No."
    p sad "Just no?"
    dolly "This dork's already tried to market himself to me as the mascot for my stand."
    dolly "Monthly sales went down 85%% because of him."
    bs "Come on, give me another chance!"
    dolly "Nothing doing. Find some other sucker to market you."
    jump mainstreet

label .dfirst:
    show posty suspicious
    p suspicious "What's this?"
    dolly "Ah! About time you made it to my stand!"
    dolly "I am Dolly, the sole proprietor of this fine establishment."
    dolly "How's the delivery going, Posty?"
    p happy "It's going fine I suppo-"
    p astonished "Wait a minute, how do you know my name?"
    dolly "I have connections, darling."
    p confused "Wha-"
    dolly "But anyway, what brings you here today?"
    p neutral "I guess I'm just browsing." 
    dolly "In that case, allow me to offer you something truly exsquisite."
    show lootbox at truecenter with moveinbottom
    dolly "Behold, a one-of-a-kind, very special, very rare ''loot box.''"
    p suspicious "What's in it?"
    dolly "Who can say?"
    dolly "Perhaps it's filled with wonderful riches to make you exceptionally wealthy!" 
    dolly "Or it could be filled with an everyday household object."
    dolly "It's all chance, honey! Buy one today and you can win practically anything."
    p happy "Alright, you've convinced me! How much?"
    show posty astonished before
    dolly "{b}{color=#ffff00}All of the money in the area{/color}{/b}."
    p astonished anim "WHAT?!"
    dolly "Well, all of the real money. I think I saw some fake money recently; don't waste my time with it."
    dolly "But don't you want it?"
    p sad "Yeah..."
    $ saw.dolly = True
    jump .money_check

label .drepeat:
    show posty neutral
    p "Hi, Dolly!"
    dolly "Ah, Posty! Rich yet?"
    show lootbox at truecenter with moveinbottom
    dolly "The random loot box is calling your name! Don't you want it?"
    p sad "Yeah..."
    jump .money_check

label .dlast:
    show posty annoyed
    show dolly
    p "You ripped me off! I thought I was getting something valuable!"
    dolly "You did! You got a loot box! It's not my fault it had a common item in it."
    dolly "You want to buy another one?"
    p "No."
    dolly "Are you sure? 99\% of gamblers quit before they win big."
    p "I can live with that."
    jump mainstreet

label .money_check:
    if money == 0:
        if item.red_cash:
            show redcash
            hide lootbox
            p happy "I have some red cash if that will work."
            dolly "Oooh, sorry. There's no market anymore in red dollars."
            show posty concerned
            dolly "How about some real money?"
            p "Oh, right, I forgot."
            p "Sorry, I got nothing."
            dolly "Come back when you have actual cash, Posty."
            hide lootbox
            jump mainstreet
        else:
            p concerned "But I'm afraid I don't have any money."
            p concerned "Can we barter?"
            dolly "No."
            dolly "Come back when you have a penny to your name, Posty."
            hide lootbox
            jump mainstreet
    elif money == 1:
        show cash_total at truecenter
        hide lootbox
        p happy "I have some money. Is this enough for anything?"
        dolly "Only my pocket lint."
        p astonished "ONLY POCKET LINT?!"
        p "THIS IS SO MUCH!!!"
        dolly "I want {b}{color=#ffff00}all of the money in the area{/color}{/b}, Posty. More than double what you have now."
        p happy "Ok, I'll be back later."
        jump mainstreet
    elif money == 2:
        show cash_total at truecenter
        hide lootbox
        p happy "I have some money. Is this enough for anything?" 
        dolly "I want {b}{color=#ffff00}all of the money in the area{/color}{/b}, Posty. This is, like, half that."
        p happy "Ok, I'll be back later."
        jump mainstreet
    elif money == 3:
        show cash_total at truecenter
        hide lootbox
        p happy "I have all this money! Is this enough for anything?"
        dolly "Wow, this is a lot of money!"
        show posty astonished before
        dolly "But it's not {b}{color=#ffff00}all of the money in the area{/color}{/b}."
        p astonished anim "HOW?!"
        dolly "I can smell it... there's still something left, and it's close by..."
        if quest.bs == False:
            dolly "OH! So, so, sooo close by. I think that purple guy next to me has it!"
            p suspicious "You... want me to rob that guy?"
            dolly "Heavens no, but there must be some way to get that dork's life savings."
            $ that_dork = True
            p annoyed quiet "..."
        elif quest.money_food == False:
            dolly "Oh, it's wafting out from the food exhibit."
            p suspicious "Not the smell of food?"
            dolly "No, I've spent my whole life eating food, so I'm desensitized to it."
            p annoyed "Is that how that works?"
        elif item.cash_main == False:
            dolly "I think it must be somewhere on this very street!"
            p suspicious "Like, on the ground?"
            dolly "Yes, just like in the alleyway!"
            p "Wait, you saw me get that? Why are you making me collect this stuff for you? Get it yourself!"
            dolly "You sure? You won't get my lootbox if I'm the one who has to get up and go grab it."
            p "Sure I will, I can just reach behind your stand while you're gone."
            dolly "And that's why I'm staying here."
            p annoyed "Touche."
        elif item.cash_alley == False:
            dolly "Might be coming from that alley over there..."
            p suspicious "So you want me to go in there and rob someone?"
            dolly "Heavens no! It's probably just laying around on the ground!"
            p annoyed "Well, I guess it wouldn't be the first time."
        jump mainstreet
    elif money == 4:
        show cash_total at truecenter
        p happy "I've got all the money! Here you go."
        dolly "Hmmm, sorry. You're still short."
        p astonished "What?!?"
        dolly "Haha, I'm just screwing with you. Of course you have enough."
        show posty angry
        hide cash_total
        "{b}{color=#e3d3ab}Dolly{/color}{/b} took all your {b}money{/b}!"
        if item.red_cash:
            "... except the worthless {b}{color=#ff0000}red cash{/color}{/b}."
        dolly "Your patronage is appreciated." 
        p suspicious "So, the loot box!"
        dolly "Oh yes, of course!"
        stop music fadeout 0.5
        dolly "Let's see what you've won!"
        show lootbox burst
        play audio "sound/330563__andre_onate__kotsuzumi-roll-at-126.ogg"
        "{w=0.9}{nw}"
        play sound "sound/423518__neospica__loot-box-open.ogg"
        show glowyglow behind lootbox
        show confetti behind glowyglow
        show brightscreen
        $ item.scrapmetal = True
        $ quest.moneys = True
        "You got some {b}scrap metal{/b} from the loot box!"
        play music "sound/music/REZURRECTA - ASTRUM_DEUS_P1.ogg" fadein 1.0
        extend "\n{i}To the average person, this may be just a bunch of metal shapes, but for a skilled worker (or for whoever is willing to pay, really), it is a canvas ready to be molded into glorious masterpieces!{/i}"
        p annoyed "Oh. Wow."
        dolly "Thank you! Come again! No refunds!"
        jump mainstreet
    
image lootbox:
    "items/lootbox.png"
    truecenter

image lootbox burst:
    "lootbox"
    ease_cubic 0.1 zoom 0.9 rotate -2
    easeout_back 0.5 zoom 0.2 rotate -120
    easeout_quint 0.5 zoom 10 rotate -500
    "items/scrapmetal.png"
    easein_elastic 1.0 zoom 1.0 rotate 0

image confetti:
    "items/confetti.jpg"
    truecenter
    zoom 0.05
    additive 1.0
    easein_cubic 3.0 zoom 0.3 alpha 0.0

image glowyglow:
    "items/glow.png"
    truecenter
    additive 1.0
    zoom 0.1
    easein_quint 3.0 zoom 1.5 alpha 0.0

image brightscreen:
    "items/white.png"
    additive 1.0
    alpha 0.4
    linear 0.5 alpha 0.0
