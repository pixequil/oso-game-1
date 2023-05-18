# The game starts here.

label start:

    # setting all the flags to false (is there really no better way to do this?) (prepared to sound stupid)
    $ win_flag = False
    $ item_butterfly_package = False
    $ party_bs = False

    scene bg room

    show posty happy

    p "You've created a new Ren'Py game."

    p "Once you add a story, pictures, and music, you can release it to the world!"

    menu:

        "Start the game.":
            jump firstscene
            
        "Developer testing room.":
            jump chartest

