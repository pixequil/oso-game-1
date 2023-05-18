# throughout the game, the player can return to Yellow Diamond to receive hints. this file is jumped to when the player interacts with Yellow Diamond, and then sends the player back to mainstreet (which is where Yellow Diamond should always be accessed).
# the hints are listed in reverse walkthrough order here.
# since the hints are accessed via "call", they should all end with "return".

label yd_hints:

    scene bg mainstreet
    show posty neutral
    show yd
    
    if win_flag:

        yd "you won; no need to have a hint" # yd explains you dont need hints because you won. or something. replace later
        return

    elif item_butterfly_package:

        yd "hint for if you just started the game" # TODO: #6 game start hint
        return

    else:

        yd "I don't have any hints for you, sorry. You should never see this dialogue."
        p confused "Wuh oh."
        return