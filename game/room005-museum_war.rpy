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

    p "_" # todo: war exhibit imagemap #150 #169

    menu:
        "Capsule":
            jump .capsule
        "Buff":
            jump .buff
        "Ahiss the Cat":
            jump .ahiss
        "Palettette@":
            jump .pal
        "Main Exhibit\nRose-Colored Glasses & Blue-Colored Glasses":
            jump .painting
        "Return to the entrance.":
            jump museum_entrance

label .ahiss:
    scene bg museum_war
    show champurrlain #166
    if deed_burned:
        jump .ahiss3
    show battery floor #168
    show ahiss
    if saw.ahiss == False:
        $ saw.ahiss = True
        jump .ahiss1
    elif saw.ahiss:
        jump .ahiss2
    "if you're seeing this, there's a problem"

label .ahiss1:
    show posty neutral with moveinleft
    p "_" # posty steps into ahiss's space for the first time #171
    show deed #170
    $ renpy.transition(hpunch, layer="master") #prevents interruption of the text window
    ahiss "_" # ahiss interrupts her and tells her to back up, claiming that they own this plot of land and showing the imaginary deed.
    show posty quiet:
        xalign -0.3
    $ renpy.transition(move, layer="master") #prevents interruption of the text window
    p "..!" # posty backs off.
    ahiss "_" # ahiss explains more about themself. make sure the last line of the interaction is ahiss, so it transitions into the next block correctly.
    show posty -quiet
    jump .ahiss_deed

label .ahiss2:
    show posty neutral with moveinleft
    p "_" # posty steps into ahiss's space again #172
    show deed 
    $ renpy.transition(hpunch, layer="master") #prevents interruption of the text window
    ahiss "_" # ahiss interrupts her and reminds her to back up
    show posty:
        xalign -0.3
    $ renpy.transition(move, layer="master") #prevents interruption of the text window
    p "_" # posty backs off and apologizes. it might be sarcastic if you want.
    ahiss "_" # ahiss chastises posty for forgetting. make sure the last line of the interaction is ahiss, so it transitions into the next block correctly.
    jump .ahiss_deed

label .ahiss_deed: #173
    if item.imaginary_lighter == False:
        if saw.pal:
            p "_" # posty asks if she can at least have that battery
            ahiss "_" # ahiss is like no way
            $ battery_asked = True
        p "_" # posty is like "well i'll leave you be then" or something
        jump museum_war
    else:
        p quiet "{i}_{/i}" # posty thinks to use the imaginary lighter on the deed.
        show posty:
            xalign -0.05
        $ renpy.transition(move, layer="master") #prevents interruption of the text window
        ahiss "_" # ahiss says something as posty approaches to incinerate the deed
        hide deed
        $ renpy.transition(irisout, layer="master") #prevents interruption of the text window
        "You {b}imaginary burned{/b} the {b}imaginary deed{/b}!"
        $ deed_burned = True
        $ item.imaginary_lighter = False
        if saw.pal:
            p "_" # posty takes the battery since it belongs to palettette.
        else:
            p "_" # posty notices the battery on the ground and takes it now that she's close to it, on impulse.
        show battery center
        "You got the {b}battery{/b}!"
        $ item.battery = True
        hide battery
        if battery_asked:
            ahiss "_" # "i hope you're happy" or something
            p "_"
            ahiss "_" # ahiss finds a way to be smug about this situation in the end.
        else:
            ahiss "_" # "that's what you wanted!??" or something
            if saw.pal:
                p "_" # posty tells the truth: yes
            else:
                p "_" # posty tells the truth: no
            ahiss "_" # ahiss finds a way to be smug about this situation in the end.
        jump museum_war

label .ahiss3:
    show ahiss
    show posty neutral with moveinleft
    p "_" # revisiting ahiss after burning their deed and taking the battery #174
    jump museum_war

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
    
