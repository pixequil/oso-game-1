image bg dome_top:
    "bgs/dome_top.png"
    zoom 1.5
    yalign 0.2

image bg dome:
    "dbgs/Dome_dialogue_bg.png"

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
        bonbon "What's the point in the dome? It sucks and needs to be destroyed."
        sgummy "How can you hate the dome. Look at how I can see my reflection, its round shape, and its durability. I wish that was me."
        bonbon "What!? Do you want to be a dome?"
        sgummy "Yes! Being a dome means I\'ll have everything ever wanted!"
        bonbon "You don\'t make any sense. You can\'t become a dome."
        sgummy "Why not?"
        bonbon "If you did then that means I\'ll have to destroy you too!"
        sgummy "You wouldn\'t because nothing would hurt me!"
        bonbon "I can!"
        sgummy "Yeah right!"
        jump dome
