#239 generi-chips

image bg janitors_top:
    "map-bgs/janitors_top.png"
    zoom 1.15
    yalign 0.2

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


label janitors:
    if saw.janitors == False:
        jump .sb1
    scene bg janitors_top
    show posty neutral
    p "_" #235 todo: janitors imagemap

    menu:
        "Squirt Bottle":
            jump .sb2
        "Vending machine":
            jump .vend
        "Get outta here":
            jump museum_food

label .vend:
    scene bg janitors
    show posty neutral at lookatvend
    p happy "Ooo a vending machine!"
    show sb with moveinright
    sb "Hey! Uh don't use that."
    p suspicious "Why? You said I could do anything."
    sb "Well- Not this."
    p neutral "What if I were to,"
    extend " say, I don't know..."
    extend happy " rat you out?"
    sb "NO!! Uhm- ugh!"
    sb "...Fine."
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
    sb "{i}sighh{/i}  Fine! you can stay here."
    sb "Not because I am happy to do so, but because you would be too much of a pain to evict."
    sb "Don't tell anyone about this."
    p happy "Not a single word will come out about this sir!"
    sb quiet "..."
    sb -quiet "Don't be so formal, just call me Squeezy."
    sb "Do whatever, I guess."
    jump janitors

label .sb2:
    scene bg janitors
    show posty neutral
    show sb
    sb "Hey, what's your deal anyway?"
    p concerned "Oh, I've been trying to deliver this package!"
    sb "Wow, that's such a surprise. I'm truly in awe. I could've never possibly foreseen this."
    p happy "Thank you!"
    p neutral "Anyway, uh, it's taking a lot longer than I thought it would.."
    p "But that's just the way things go sometimes, right?"
    sb "I wouldn't know."
    p "I should probably tell you what I'm delivering."
    sb "You don't have to."
    p happy "But I wanna!"
    p "You ever have something that's so cool that you just {i}have{i} to tell somebody else?"
    p "Like, a revelation so big you just can't keep yourself contained?"
    sb "Hey, you better not have forgotten about our deal!"
    p suspicious "Deal?"
    sb "DUDE!"
    p concerned "I'm kidding!"
    p "..Probably."
    sb "Probably?!?"
    jump janitors

