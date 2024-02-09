image bg dome_top:
    "map-bgs/dome_top.png"
    zoom 1.5
    yalign 0.2

image bg dome:
    "dbgs/Dome_dialogue_bg.png"

label dome:
    $ last.mainx = 1.0
    scene bg dome_top with fade
    show posty neutral

    p "_" # TODO: #20 dome imagemap

    menu:
        "Talk to Crayon Box" if item.butterfly_package:
            jump .cb
        "Talk to Retainer" if (quest.retainer == False):
            jump .retainer
        "Talk to Bon-Bon & Sour Gummy":
            jump .sweets
        "Leave.":
            jump mainstreet

label .cb:
    if quest.retainer:
        jump .cb_give
    else:
        "Seems like {b}{color=#fc809d}Retainer{/color}{/b} is in the way..."
        $ saw.retainerblock = True
        jump dome

label .cb_give:
    scene bg dome
    show posty neutral
    show cb
    p happy "Phew! Here you go ma'am!"
    cb "Thank you so much!"
    show butterfly_package
    "You handed over the {b}Butterfly Package{/b}!"
    $ item.butterfly_package = False
    $ win_flag = True
    hide butterfly_package
    cb "Just in time! I'll need to go now."
    hide cb with moveoutright
    show posty astonished before
    cb "Gather 'round, contestants! The fourth challenge is about to start!"
    cb "I had the contents of today's challenge"
    show posty astonished anim
    cb "I had the contents of today's challenge{fast} {i}specially{/i}{w=0.3} delivered!"
    p astonished "Oh my god!! Crayon Box is talking about {i}ME{/i}?!? This is a dream come true!!"
    "You successfully finished your work for today!"
    p happy "Gosh!! I'm so tired from that! Perhaps some new scenery would help..."
    jump dome

label .retainer:
    if item.makeshift_trophy:
        jump .retainer_give 
    else:
        scene bg dome
        show posty neutral
        show retainer sad
        p "What's wrong?"
        retainer "Sigh, things hadn't been going well."
        retainer "Got eliminated from this show after only a couple of challenges, which was way earlier than expected."
        p "Ah shame, it happens sometimes."
        retainer "It was supposed to be my breakthrough moment! When I start making friends and doing more in my life."
        retainer "Instead I ended up here, without accolades to show for it."
        retainer "I don't understand why I did this in the first place, no one cared I was gone."
        p "..."
        p "May I get past you?"
        retainer "..."
        p "Never mind."
        jump dome

label .retainer_give: #282
    scene bg dome
    show posty neutral
    show retainer sad behind posty
    p "_" 
    retainer "_" # retainer is still sad. write the conversation assuming it's possible posty has or hasnt talked to retainer before.
    p "_" # posty has an idea of what to give him though!'
    show retainer happy
    show makeshift_trophy
    "You handed over the {b}makeshift trophy{/b}!"
    $ item.makeshift_trophy = False
    $ quest.retainer = True
    hide makeshift_trophy
    retainer "_" # retainer accepts it and becomes happy! also, he decides it's time to finally go home.
    hide retainer with moveoutleft
    "{b}{color=#fc809d}Retainer{/color}{/b} got out of the way!"
    if saw.retainerblock:
        p "_" # "finally!"
    else:
        p "_" # "good thing i had that with me!"
    jump dome

label .sweets:
    scene bg dome
    show bonbon
    show sgummy behind bonbon
    if quest.retainer:
        show posty neutral
        bonbon "_" #283 bonbon and sour gummy saw you give retainer that trophy
        sgummy "_"
        jump dome
    else:
        show posty neutral
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
