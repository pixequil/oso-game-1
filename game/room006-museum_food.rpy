# todo: food exihibit conversation bg #190

# todo: food main exhibit painting #226

image bg museum_food_top:
    "map-bgs/museum_food_top.png"
    zoom 1.15
    yalign 0.2

label museum_food:
    if saw.food == False:
        jump .painting
    scene bg museum_food_top
    show posty neutral

    p "_" # todo: food exhibit imagemap #224

label .painting: #228
    scene bg museum_food
    show painting_food
    show posty neutral
    show rm
    rm "_" # something about the painting before walking away
    hide rm with moveoutright
    p "_" # posty beholds the main painting in the food exhibit and feels a compulsion to collect it.
    show painting_food at center
    "You got an {b}art piece{/b}!" #227 describe food painting
    $ item.painting_food = True
    $ quest.painting_food = True
    $ paintings += 1
    $ saw.food = True
    hide painting_food
    if paintings == 1:
        p "this was the first painting (replace this text)" # posty says something and decides to look around the rest of the exhibit
    else:
        p "that was easy (replace this text)" # posty remarks that it was easy to take this painting, if this isn't her first painting.
    jump museum_food

