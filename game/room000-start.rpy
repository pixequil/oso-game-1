# The game starts here.

image bg room:
    "bgs/room.png"


label start:

# default text speed is broken in this prerelease version, so this is my hackjob
    if not persistent.cps:
        $ preferences.text_cps = 120
        $ persistent.cps = True
        $ renpy.save_persistent()

    jump firstscene

    # scene bg room
    # show posty sad
    # p "This game is currently in development, so it's missing much of its dialogue."
    # p happy "Technically, it's possible to complete it, though!"

    # menu:

    #     "Start the game.":
    #         jump firstscene
            
    #     "Developer testing room.":
    #         jump chartest

