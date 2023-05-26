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
        "Buff":
            jump .buff
        "Return to the entrance.":
            jump museum_entrance

label .buff:
    if burger_extinguish == True:
        jump .buff2
    scene bg museum_war
    show burger fire # full-size fire burger painting (and fire-free version) #156
    show posty neutral
    show buff
    p "_" # Posty talks to Buff. #160
    buff "_" # Loves history. Tells you all about history and the paintings and people in the room. Doesn't actually know anythving about history but Posty doesn't either so it's hard to call them out on it.
    "_" #157 describe the burger painting. There's a painting of the Hideous Burger Fire on the eastern wall, with the fire described as wanting to jump out of the page!
    buff "__" # buff makes up some kind of fact about the painting.
    p "_" # posty thinks to use the heavier on the painting, removing the fire.
    show burger out
    $ item.heavier = False
    $ burger_extinguish = True
    p "__" # posty prods buff for another fact about the painting, that is now changed.
    buff "_" # buff makes up a new fact that contradicts the previous fact.
    p "_" # posty calls them out on the contradiction, causing them to give posty an imaginary lighter.
    show imaginary_lighter #158
    $ item.imaginary_lighter = True
    "You got the {b}imaginary lighter{/b}!{p}description" #159 the imaginary lighter can be used to add fire to imaginary things.
    hide imaginary_lighter
    p "_" # posty is confused.
    buff "_" # buff explains that imaginary things are a contradictory science, so they gave Posty a con-science lighter to make their conscience lighter after saying a contradiction outing themself as a liar. this all sounds very made-up, but, that's the nature of imaginary things.
    jump museum_war

label .buff2:
    scene bg museum_war
    show burger out
    show posty neutral
    show buff
    p "_" # revisiting buff and the fire-free burger painting #161
    jump museum_war

label .capsulefirst:
    scene bg museum_war
    show posty neutral
    show capsule pain
    p "_" # Capsule stops Posty at the entrance to the war exhibit, asking if she's strong and begging her to take this "heavier" off her hands. #153
    show heavier #151 
    $ saw.war = True
    $ item.heavier = True
    "You got the {b}heavier{/b}!{p}description" #152
    hide heavier
    capsule happy "_" # capsule is thankful. Posty asks what a heavier even is, and Capsule explains what it is. It's the opposite of a lighter. Instead of adding fire to things, it removes fire from things. It's also heavy.
    jump museum_war

label .capsule:
    scene bg museum_war
    show posty neutral
    show capsule happy
    p "_" # Capsule re-explains what the heavier does, in case you forgot. #155 
    jump museum_war
    
