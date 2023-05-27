# throughout the game, the player can return to Toasty to receive hints. this file is jumped to when the player interacts with Toasty, and then sends the player back to mainstreet (which is where Toasty should always be accessed).
# the hints are listed in a weird, almost reverse walkthrough order here.
# since the hints are accessed via "call", they should all end with "return".

label toasty_hints:

    scene bg mainstreet
    show posty neutral
    show toasty neutral
    
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

    elif item.battery:
        show posty neutral
        show toasty neutral
        t "hint for if you have the battery" #175
        return

    elif item.imaginary_lighter:
        show posty neutral
        show toasty neutral
        t "hint for if you have the imaginary lighter" #163
        return
    
    elif item.heavier:
        show posty neutral
        show toasty neutral
        t "hint for if you have the heavier" #162
        return

    elif bt_distracted:
        show posty neutral
        show toasty neutral
        t "hint for if blue tile is distracted and you can finally take the painting" #120
        return

    elif miso_blocked and (quest.painting_blue == False):
        show posty neutral
        show toasty neutral
        t "hint for if blue tile doesn't let you spill soup on the painting" #117
        return

    elif item.ladle_full:
        t smug2 "Oh, so you decided to use that ladle on something, hmm?"
        t laugh "What are you going to do with that soup, anyway? Start a food fight?"
        t pointandlaugh "Hah! Just the thought of you getting everything rusty makes me chuckle!"
        t neutral quiet "..."
        t enthused "Actually, if you are, can I join?"
        p neutral "Uh, I'm not planning any fights, sorry."
        t annoyed "Ugh, {i}lame{/i}."
        return

    elif item.ladle_empty:
        t "hint for if you have empty ladle" # todo: #52 empty ladle hint (use it on miso soup)
        return

    elif paintings == 1:
        show posty neutral
        show toasty neutral
        t "hint for if you've taken one painting" #154
        return
    
    elif quest.bs:
        t "hint for if you finished Brand Soda quest" # TODO: #18 hint for after brand soda quest (go in the museum)
        return

    elif saw.retainerblock:
        t "hint for after you try to deliver the butterflies" # todo: #19 blocked by retainer hint (idk look around and talk to people or something)
        return

    elif item.butterfly_package:
        t "hint for if you just started the game" # TODO: #6 game start hint (try delivering the butterflies)
        return

    else:
        t "I don't have any hints for you, sorry. You should never see this dialogue."
        p confused "Wuh oh."
        return