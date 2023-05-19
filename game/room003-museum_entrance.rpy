# todo: #25 museum entrance conversation background

label museum_entrance:
    if saw_museum == False:
        jump .first_time
    else:
        scene bg museum_entrance_top # TODO: #26 museum entrance imagemap (needs illustration)
        show posty neutral

        p "_"

        menu:
            "Check out the Blue Exhibit.":
                jump museum_blue
            "Check out the War Exhibit.":
                jump museum_war
            "Check out the Food Exhibit.":
                jump museum_food
            "Check out those easels?":
                jump .easels
            "Talk to Security Cameron again.":
                jump .cameron
            "Leave.":
                jump mainstreet

label .first_time:
    scene bg museum_entrance
    show posty neutral
    show cameron # TODO: #27 Security Cameron talksprite
    p "_" # TODO: #28 Security Cameron welcomes Posty to the museum when she first arrives. He talks about an incident where some Miso Soup character spilled some Miso Soup in one of the gates in the Blue Exhibit, just barely missing a painting. Says the Miso Soup character swears they wear a Plastic Wrap when in the museum but he knows they took the wrap off to commit this crime.
    cameron "_"
    $ saw_museum = True
    jump museum_entrance

label .easels:
    scene bg easels # TODO: #29 easels scene
    show posty neutral

    "There are three {b}easels{/b} here." # TODO: #30 rewrite easel narration
    p quiet "..."
    "You feel ...{w} something."
    "The germinating seeds of inspiration?"
    "Maybe you can make a work of art here, if you collect enough {color=#ffff00}inspiration{/color}."
    jump museum_entrance


