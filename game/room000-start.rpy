# The game starts here.

image bg room:
    "bgs/room.png"

label start:

    scene bg room

    show posty happy

    p "Hello."

    p "This is a story of determination, focus and a lot of shenanigans"

    p happy "I hope you enjoy this venture from the OSO team!"

    menu:

        "Start the game.":
            jump firstscene
            
        "Developer testing room.":
            jump chartest

