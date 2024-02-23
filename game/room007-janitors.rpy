#239 generi-chips

image bg janitors_top:
    "map-bgs/janitors_top.png"

image bg janitors:
    "dbgs/janitors_dbg.png"

image generichips:
    "items/generi-chips.png"
    xalign 0.1
    yalign 0.5
    zoom 0.8

transform lookatvend:
    xzoom -1.0
    xalign 0.6
    yalign 1.0

transform getvend:
    xzoom -1.0
    xalign 0.2
    yalign 1.0

transform flip: 
    xzoom -1.0

screen janitor_nav():
    viewport:
        child_size (1280,720)
        add "bg janitors_top"

        imagebutton: 
            xanchor 0.5
            yanchor 0.5
            pos (323, 600)
            idle "arrow dn"
        imagebutton: 
            xanchor 0.5
            yanchor 0.5
            pos (323, 600)
            idle "pnav dn i"
            hover "pnav dn"
            action Jump("museum_food")

        imagebutton:
            pos (250,200)
            idle "nav_spray"
            hover "nav_spray p"
            action Jump("janitors.sb2")
        imagebutton: 
            xanchor 0.5
            yanchor 0.5
            pos (230, 150)
            idle "pnav up i"
            hover "pnav up"
            action Jump("janitors.vend")

image nav_spray = Composite(
    (250,250),
    (0,0), "hitbox",
    (110,0), "minisprites/squirtbottle.png",
)
image nav_spray p = Composite(
    (250,250),
    (0,0), "nav_spray",
    (60,30), "pnav up"
)

label janitors:
    if saw.janitors == False:
        jump .sb1
    $ renpy.choice_for_skipping()
    call screen janitor_nav

# label janitors:
#     if saw.janitors == False:
#         jump .sb1
#     scene bg janitors_top
#     show posty neutral
#     p "_" #235 todo: janitors imagemap

#     menu:
#         "Squirt Bottle":
#             jump .sb2
#         "Vending machine":
#             jump .vend
#         "Get outta here":
#             jump museum_food

label .vend:
    scene bg janitors
    show posty happy at lookatvend
    if vendingmachine_used == True:
        p "I really don't need any more food."
        show sb with moveinright
        sb "You better not take any more food!"
        p annoyed "I heard you the first time, dude. You don't need to remind me."
        p "At this rate, I may rat you out anyway."
        sb "Ugghh!"
        hide sb with moveoutright
        p happy "Tee hee!"
    else:
        p "Ooo a vending machine!"
        show sb with moveinright
        sb "Hey! Uh, don't use that."
        p suspicious "Why? You said I could do anything."
        sb "Well- Not this."
        sb "I need this food more than you do."
        p neutral "What if I were to,"
        extend " say, I don't know..."
        extend happy " rat you out?"
        sb "NO!! Uhm- ugh!"
        sb "...fine."
        p "Yay!"
        show posty at getvend with move
        show posty at lookatvend with move
        show generichips
        $ item.chips = True
        "You got the {b}Generi-Chips{/b}!" 
        "Generi-Chips: it has some nutrients."
        hide generichips
        p annoyed "Eww really? Generi-Chips??"
        sb "It's better than nothing!"
        p "Whatever, I'm keeping them in case I need it."
        $ vendingmachine_used = True
    jump janitors


label .sb1:
    scene bg janitors
    show posty neutral
    show sb:
        flip
        right
    $ saw.janitors = True
    p suspicious quiet "{i}What\'s this place?{/i}"
    p neutral "...heya."
    hide sb
    show sb # resets sb so hes facing the correct way
    $ renpy.transition(hpunch, layer="master")
    sb "AHGDHSXJS- How d'ya get here!?"
    p "Umm I don't know... Errrrm nice chairs?"
    sb "You don't get to complement my chairs unless I invite you in. And I don't recall sending invitations."
    p "Errrrrrr.."
    sb "{i}sighh{/i}  Fine! You can stay here."
    sb "Not because I am happy to do so, but because you would be too much of a pain to evict."
    sb "You can do whatever you want, but don't tell anyone about this."
    p happy "Not a single word will come out about this, sir!"
    sb quiet "..."
    sb -quiet "Don't be so formal, just call me Squeezy."
    sb "Do whatever, I guess."
    jump janitors

label .sb2:
    scene bg janitors
    show posty neutral
    show sb
    p "So, what is this place?"
    sb "Well, if you must know, I've been the janitor for about twenty years. I know this building like the back of my hand."
    sb "This job can be really hard sometimes, so I spent some time expanding this old janitor's closet my own personal paradise."
    sb " I can relax here whenever I want to! I even pushed in a vending machine for free food!"
    sb "As long as I hide a painting behind the passageway, no one notices or cares."
    p "So you engineered that switch with the placard?"
    sb "Yep. It's amazing what you can learn on the internet these days."
    p happy "That's really cool, dude!"
    sb "Hey, what's your deal anyway?"
    p concerned "Oh, I've been trying to deliver this package!"
    sb "Wow, that's such a surprise. I'm truly in awe. I could've never possibly foreseen this judging by the kind of object you are."
    p happy "Thank you!"
    p neutral "Anyway, uh, it's taking a lot longer than I thought it would..."
    p "But that's just the way things go sometimes, right?"
    sb "I wouldn't know."
    p "I should probably tell you what I'm delivering."
    sb "You don't have to."
    p happy "But I wanna!"
    p "You ever have something that's so cool that you just {i}have{i} to tell somebody else?"
    p "Like, a revelation so big you just can't keep yourself contained?"
    sb "Hey, speaking of which, you better not have forgotten about our deal!"
    p suspicious "Deal?"
    sb "Don't tell anyone about this secret room!"
    p concerned "I'm kidding! Of course I didn't forget!"
    p "...Probably."
    sb "Probably?!?"
    jump janitors

