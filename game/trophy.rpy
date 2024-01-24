image makeshift_trophy:
    "items/makeshift_trophy.png"
    xalign 0.5
    yalign 0.5
    zoom 5.0
    rotate 45

label trophy:
    show spraypaint at truecenter
    p "Oh! Like this?" #280 "oh, i know what to use this for!"
    tooly "Perfect!"
    show scraptrophy
    #279 add a quick animation for using the spray paint on the trophy. just moving them around and making the screen flash should be sufficient
    hide spraypaint
    hide scraptrophy
    show makeshift_trophy
    "You used the {b}glittery gold spray paint{/b} on the {b}scrap trophy{/b}, making it into a {b}makeshift trophy{/b}!"
    $ item.spraypaint = False
    $ item.scrap_trophy = False
    $ item.makeshift_trophy = True
    hide makeshift_trophy
    return
    