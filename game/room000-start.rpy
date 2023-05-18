# The game starts here.

label start:

    scene bg room

    show posty happy

    p "You've created a new Ren'Py game."

    p "Once you add a story, pictures, and music, you can release it to the world!"

    menu:

        "Start the game.":
            jump firstscene
            
        "Developer testing room.":
            jump chartest

