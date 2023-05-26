# todo: war exhibit conversation background #149

image bg museum_war_top:
    "map-bgs/museum_war_top.png"
    zoom 1.15
    yalign 0.2

label museum_war:
    if saw.war == False:
        jump .capsulefirst
    scene bg museum_war_top
    show posty neutral

    p "_" # todo: war exhibit imagemap #150

    menu:
        "Capsule":
            jump .capsule
        "Return to the entrance.":
            jump museum_entrance

label .capsulefirst:
    scene bg museum_war
    show posty neutral
    show capsule pain
    p "_" # Capsule stops Posty at the entrance to the war exhibit, asking if she's strong and begging her to take this "heavier" off her hands. #153
    show heavier #151 
    $ saw.war = True
    $ item.heavier = True
    "You got the {b}heavier{/b}!{p}description" #152
    capsule happy "_" # capsule is thankful. Posty asks what a heavier even is, and Capsule explains what it is. It's the opposite of a lighter. Instead of adding fire to things, it removes fire from things. It's also heavy.
    jump museum_war
