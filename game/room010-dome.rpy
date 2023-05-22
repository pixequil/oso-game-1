image bg dome_top:
    "bgs/dome_top.png"
    zoom 1.5
    yalign 0.2

# TODO: #24 dome conversation bg

label dome:
    scene bg dome_top with fade
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
    if quest.retainer:
        jump .cb_talk #
    else:
        "Seems like {b}{color=#fc809d}Retainer{/color}{/b} is in the way..."
        $ saw.retainerblock = True
        jump dome

label .retainer:
    if item.makeshift_trophy:
        jump .retainer_give #
    else:
        scene bg dome
        show posty neutral
        show retainer sad
        p "_" # TODO: #21 retainer is sad he got eliminated
        retainer "_"
        jump dome

label .sweets:
    if quest.retainer:
        jump .sweets_sawthat #
    else:
        scene bg dome
        show posty neutral
        show bonbon
        show sgummy behind bonbon
        p "_" # TODO: #22 bonbon and sour gummy conversation about dome
        bonbon "_"
        sgummy "_"
        jump dome
