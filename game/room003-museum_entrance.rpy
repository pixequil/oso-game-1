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
    p "_" # TODO: #28 Security Cameron welcomes Posty to the museum when she first arrives
    cameron "_"
    jump museum_entrance



