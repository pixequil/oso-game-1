label dome:
    scene bg dome with fade
    show posty neutral

    p "_" # TODO: #20 dome imagemap

    menu:
        "Talk to Crayon Box":
            jump .cb
        "Talk to Retainer":
            jump .retainer
        "Talk to Bon-Bon & Sour Gummy":
            jump .sweets
        "Leave.":
            jump mainstreet

label .cb:
    if quest_retainer:
        jump .cb_talk
    else:
        "Seems like {b}{color=#fc809d}Retainer{/color}{/b} is in the way..."
        $ saw_retainerblock = True
        jump dome

label .retainer:
    if item_makeshift_trophy:
        jump .retainer_give
    else:
        scene bg dome
        show posty neutral
        show retainer sad
        p "_" # TODO: #21 retainer is sad he got eliminated
        retainer "_"
        jump dome
