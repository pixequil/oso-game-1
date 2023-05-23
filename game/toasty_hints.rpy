# throughout the game, the player can return to Toasty to receive hints. this file is jumped to when the player interacts with Toasty, and then sends the player back to mainstreet (which is where Toasty should always be accessed).
# the hints are listed in a weird, almost reverse walkthrough order here.
# since the hints are accessed via "call", they should all end with "return".

label toasty_hints:

    scene bg mainstreet
    show posty neutral
    show toasty neutral at right
    
    if win_flag:
        t "you won; no need to have a hint" # toasty explains you dont need hints because you won. or something. replace later
        return

    elif party_bs:
        show bs follow behind posty with moveinleft
        bs "_"
        t "hint for if Brand Soda is following you" # TODO: #13 brand soda hint (talk to yd or "someone who wants to advertise")
        return

    # above this line are urgent hints, that should be prioritized
    # below this line are hints displayed in roughly reverse walkthrough order

    elif item.ladle_full:
        t "hint for if you have full ladle" # todo: #51 full ladle hint (further rust the bars)

    elif item.ladle_empty:
        t "hint for if you have empty ladle" # todo: #52 empty ladle hint (use it on miso soup)
        return
    
    elif quest.bs:
        t "hint for if you finished Brand Soda quest" # TODO: #18 hint for after brand soda quest (go in the museum)
        return

    elif saw.retainerblock:
        p "Hey Toasty."
        t "Hey loser."
        p "I just tried to deliever my package of butterflies to Crayon Box and this guy who just got eliminated is blocking the walkway."
        t "Oh yeah, Retainer. Kind of a wimp."
        t "He's the type of guy who wants instant gratification. Like a medal or trophy or something."
        t "But I wish good luck on anyone trying to find something for him."
        p "Awwww, thanks Toasty!"
        t  "Oh, in that case, I don't wish you any good luck at all." # todo: #19 blocked by retainer hint (idk look around and talk to people or something)
        return

    elif item.butterfly_package:
        t "hint for if you just started the game" # TODO: #6 game start hint (try delivering the butterflies)
        return

    else:
        t "I don't have any hints for you, sorry. You should never see this dialogue."
        p confused "Wuh oh."
        return