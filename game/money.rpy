image cash_bundle_1:
    "items/cash_bundle.png"
    xalign 0.5
    yalign 0.55
    zoom 4.0

label money_get:
    if money == 0:
        "A player should never see this text."
    elif money == 1:
        show cash_bundle_1
        "You now have {b}some money{/b}!"
        hide cash_bundle_1
        return

label dolly:
    scene bg mainstreet
    show posty neutral
    show dolly
    if dolly_first == False:
        jump .dfirst
    else:
        jump .drepeat

label .dfirst:
    p "meeting dolly first time" # TODO: #35 initial dolly conversation; transition seamlessly into money checking tree
    jump .money_check

label .drepeat:
    p "revisiting dolly" # TODO: #36 repeat dolly conversation; transition seamlessly into money checking tree
    jump .money_check

label .money_check:
    if money == 0:
        if item_red_cash:
            p "i have red cash" # TODO: #37 Posty offers the red cash since she lacks real money
            jump mainstreet
        else:
            p "i have nothing" # todo: #38 posty has no money
            jump mainstreet
    elif money == 1:
        p "i have some money" # todo: #39 posty has "some" money
        jump mainstreet

