image cash_bundle_1:
    "items/cash_bundle.png"
    xalign 0.5
    yalign 0.55
    zoom 4.0

# todo: cash bundle 2 #249

label money_get:
    if money == 0:
        "A player should never see this text."
    elif money == 1:
        show cash_bundle_1 at truecenter
        "You now have {b}some money{/b}!"
        hide cash_bundle_1
        return
    elif money == 2:
        show cash_bundle_2 at truecenter
        "You now have {b}a lot of money{/b}!"
        hide cash_bundle_2
        return

label dolly:
    $ last.mainx = 1.0
    scene bg mainstreet
    show dolly
    if party_bs:
        jump .dbs
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
    # TODO: #35
    #initial dolly conversation; 
    #transition seamlessly into money checking tree. 
    #Dolly is a Shifty businesswoman with a shoddy street storefront 
    #and whatever she offers to sell you a “loot box”
    #full of what can surely be wonderful riches, 
    #provided you can give her "a lot of money".
    p suspicious "What's this?"
    dolly "Ah! About time you made it to my stand!"
    dolly "I am Dolly, the sole proprietor of this fine establishment."
    dolly "How's the delivery going, Posty?"
    p happy "It's going fine I suppo-"
    p astonished "Wait a minute, how do you know my name?"
    dolly "I have connections to your higher-ups, darling."
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
    dolly "How much do you have?"
    $ saw.dolly = True
    jump .money_check

label .drepeat:
    show posty neutral
    p "Hi, Dolly!"
    dolly "Ah, Posty! Rich yet?" # TODO: #36 repeat dolly conversation; transition seamlessly into money checking tree
    show lootbox at truecenter with moveinbottom
    dolly "The random loot box is calling your name!"
    p "Well..."
    jump .money_check

label .money_check:
    if money == 0:
        if item.red_cash:
            show redcash
            p happy "I have some red cash if that will work."
            dolly "Oooh, sorry. There's no market anymore in red dollars."
            show posty concerned
            dolly "How about some real money?"# TODO: #37 Posty offers the red cash since she lacks real money
            p concerned "Sorry, I got nothing."
            dolly "Come back when you have actual cash, Posty."
            hide lootbox
            jump mainstreet
        else:
            p concerned "I'm afraid I don't have any money."
            p concerned "Can we barter?"
            dolly "No."
            dolly "Come back when you have a penny to your name, Posty." # todo: #38 posty has no 
            hide lootbox
            jump mainstreet
    elif money == 1:
        show cash_bundle_1 at truecenter
        p happy "I have some money. Is this enough for anything?" # todo: #39 posty has "some" money. 
        dolly "Only my pocket lint."
        dolly "I want A LOT of money, Posty. Double what you have now."
        p happy "Ok, I'll be back later." #this is not enough money for Dolly; Dolly wants "a lot of" money.
        jump mainstreet
    elif money == 2: #250
        show cash_bundle_2 at truecenter
        p happy "I've got plenty of money. Here you go." #  posty has "a lot of" money
        dolly "Hmmm, sorry. You're still short."
        p astonished "What?!?"
        dolly "Haha, I'm just screwing with you. Of course you have enough." # dolly thinks this is sufficient for the loot box, although she pretends briefly that it's not, to mess with Posty. 
        show posty angry
        hide cash_bundle_2
        "{b}{color=#e3d3ab}Dolly{/color}{/b} took all your {b}money{/b}!"
        if item.red_cash:
            "... except the worthless {b}{color=#ff0000}red cash{/color}{/b}."
        dolly "Your patronage is appreciated." # "much appreciated!"
        p suspicious "So, the loot box!" # "... so, the loot box?"
        dolly "Oh yes, of course!"
        dolly "Let's see what you've won!" # "right!"
        show lootbox at truecenter #266
        "..." #268 insert gratuitous lootbox opening animation, reminiscent of predatory gacha games
        hide lootbox
        show scrapmetal at truecenter #269
        $ item.scrapmetal = True
        $ quest.moneys = True
        "You got some {b}scrap metal{/b} from the loot box!" #270
        p annoyed "Oh. Wow."
        dolly "Thank you! Come again! No refunds!" # this disappoints and upsets posty, but Dolly will offer no refunds.
        jump mainstreet

