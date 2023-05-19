# todo: #25 museum entrance conversation background

label museum_entrance:
    if saw_museum == False:
        jump .first_time
    else:
        scene bg museum_entrance_top # TODO: #26 museum entrance imagemap (needs illustration)
        show posty neutral

label .first_time:
    scene bg museum_entrance
    show posty neutral
    show cameron # TODO: #27 Security Cameron talksprite
    p "_" # TODO: #28 Security Cameron welcomes Posty to the museum when she first arrives. He talks about an incident where some Miso Soup character spilled some Miso Soup in one of the gates in the Blue Exhibit, just barely missing a painting. Says the Miso Soup character swears they wear a Plastic Wrap when in the museum but he knows they took the wrap off to commit this crime.
    cameron "_"
    $ saw_museum = True
    jump museum_entrance



