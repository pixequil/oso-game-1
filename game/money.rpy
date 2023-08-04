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
        show cash_bundle_1
        "You now have {b}some money{/b}!"
        hide cash_bundle_1
        return
    elif money == 2:
        show cash_bundle_2
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
    show bs follow behind posty
    p "_" #todo: #111 Dolly quickly rejects Brand Soda, saying they've already spoken.
    jump mainstreet

label .dfirst:
    show posty neutral
    p "meeting dolly first time" # TODO: #35 initial dolly conversation; transition seamlessly into money checking tree. Dolly is a Shifty businesswoman with a shoddily built storefront lining the street, and whatever she offers to sell you a “loot box” full of what can surely be wonderful riches, provided you can give her "a lot of money".
    jump .money_check

label .drepeat:
    show posty neutral
    p "revisiting dolly" # TODO: #36 repeat dolly conversation; transition seamlessly into money checking tree
    jump .money_check

label .money_check:
    if money == 0:
        if item.red_cash:
            show redcash
            p "i have red cash" # TODO: #37 Posty offers the red cash since she lacks real money
            jump mainstreet
        else:
            p "i have nothing" # todo: #38 posty has no money
            jump mainstreet
    elif money == 1:
        show cash_bundle_1
        p "i have some money" # todo: #39 posty has "some" money. this is not enough money for Dolly; Dolly wants "a lot of" money.
        jump mainstreet
    elif money == 2: #250
        show cash_bundle_2
        p "i have a lot of money" #  posty has "a lot of" money
        dolly "_" # dolly thinks this is sufficient for the loot box, although she pretends briefly that it's not, to mess with Posty. 
        "{b}{color=#e3d3ab}Dolly{/color}{/b} took all your {b}money{/b}!"
        if item.red_cash:
            "... except the worthless {b}{color=#ff0000}red cash{/color}{/b}."
        dolly "_" # "much appreciated!"
        p "_" # "... so, the loot box?"
        dolly "_" # "right!"
        show lootbox #266
        "..." #268 insert gratuitous lootbox opening animation, reminiscent of predatory gacha games
        hide lootbox
        show scrapmetal #269
        $ item.scrapmetal = True
        $ quest.moneys = True
        "You got some {b}scrap metal{/b} from the loot box!" #270
        p "_" # this disappoints and upsets posty, but Dolly will offer no refunds.
        jump mainstreet

