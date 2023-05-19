# throughout the game, the player can return to Toasty to receive hints. this file is jumped to when the player interacts with Toasty, and then sends the player back to mainstreet (which is where Toasty should always be accessed).
# the hints are listed in reverse walkthrough order here.
# since the hints are accessed via "call", they should all end with "return".

label toasty_hints:

    scene bg mainstreet
    show posty neutral
    show toasty neutral at right
    
    if win_flag:
        t "you won; no need to have a hint" # toasty explains you dont need hints because you won. or something. replace later
        return

    elif quest_bs:
        t "hint for if you finished Brand Soda quest" # TODO: #18 hint for after brand soda quest

    elif party_bs:
        show bs follow behind posty with moveinleft
        bs "_"
        t "hint for if Brand Soda is following you" # TODO: #13 brand soda hint

    elif item_butterfly_package:
        t "hint for if you just started the game" # TODO: #6 game start hint
        return

    else:
        t "I don't have any hints for you, sorry. You should never see this dialogue."
        p confused "Wuh oh."
        return