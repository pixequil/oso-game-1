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

    elif item.ladle_full:
        t "hint for if you have full ladle" # todo: #51 full ladle hint (further rust the bars)

    elif item.ladle_empty:
        t "hint for if you have empty ladle" # todo: #52 empty ladle hint (use it on miso soup)
        return
    
    elif quest.bs:
        t "hint for if you finished Brand Soda quest" # TODO: #18 hint for after brand soda quest (go in the museum)
        return

    elif saw.retainerblock:
        show toasty neutral
        p concerned "Hey Toasty."
        t smug "Hey loser."
        t smug2 "Looks like you met Retainer." 
        t smug3 "Let me guess, was he bitter and in denial?"
        p "Pretty much..."
        t laugh "HA! Good thing I'm not wasting my time over there!"
        t crossedarms "I'm hanging out here, where all the action is!"
        t enthused "Music, art, local businesses, it all just...makes me feel alive!"
        t smug "And then I look at your face."
        show toasty pointandlaugh talk
        p annoyed "Thanks, I guess."
        return

    elif item.butterfly_package:
        t "hint for before you try to deliever the butterfly package to Crayon Box" # todo #6 
        return

    else:
        t "I don't have any hints for you, sorry. You should never see this dialogue."
        p confused "Wuh oh."
        return