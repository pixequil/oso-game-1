# todo: war exhibit conversation background #149

# todo: war main exhibit painting #225

image bg museum_war_top:
    "map-bgs/museum_war_top.png"
    zoom 1.15
    yalign 0.2

image bg museum_war:
    "dbgs/museum_war_dbg.png"
    yalign 0.2

image heavier:
    "items/Heavier.png"
    truecenter
    zoom 2.5

image burger fire:
    "items/big_fire_painting_1.png"
    xalign 0.45
    yalign 0.5

image burger out:
    "items/big_fire_painting_2.png"
    xalign 0.45
    yalign 0.5

image imaginary_lighter:
    "items/Imaginary_Lighter.png"
    truecenter
    zoom 2.0

image battery_center:
    "items/batteries.png"
    truecenter
    zoom 1.5

image battery_floor:
    "items/batteries.png"
    yalign 1.0
    zoom 1.5

image champurrlain:
    "items/Champurrlain_painting.png"
    xalign 0.44
    yalign 0.3
    zoom 1.5

image deed:
    "items/imaginary_deed.png"
    xalign 0.44
    yalign 0.5
    zoom 1.5

image painting_war:
    "items/war_Exhibit_photo_original.png"
    truecenter
    zoom 0.4

image painting_war green:
    "items/war_Exhibit_photo_green.png"
    truecenter
    zoom 0.4


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
        "Main Exhibit\nRose-Colored Glasses & Blue-Colored Glasses" if scanter_green == False:
            jump .painting1
        "Main Exhibit" if (scanter_green == True) and (quest.painting_war == False):
            jump .painting2
        "Rose-Colored Glasses & Blue-Colored Glasses" if scanter_green:
            jump .glasses2
        "Return to the entrance.":
            jump museum_entrance

label .painting1:
    scene bg museum_war
    show painting_war
    show rcg
    show bcg
    if saw.glasses:
        show posty neutral
        "The two still seemed to be fighting."
        jump museum_war
    else:
        show posty neutral
        p "uh excu-"
        rcg "This art piece clearly shows the victory of the Redoinks!!"
        bcg "No{w} - The positioning obviously implies the victory of the Blouououous."
        bcg "They are so wounded and depressed, having to fight in a war n' all, yknow?"
        rcg "What do you mean!?! The determination in their eyes say it all! You always see the gloomy parts of EVERYTHING!"
        bcg "You always see the hopeful parts, even when it isn't intended!"
        p "{i}They look busy. I should probably leave.{/i}"
        $ saw.glasses = True
        jump museum_war

label .painting2:
    scene bg museum_war
    show painting_war green
    show posty neutral
    p "_" #211 posty beholds the painting and decides to take it since no one's around to block it.
    hide painting_war green # !! HIDING AND SHOWING THE PAINTING MOVES IT TO THE FRONT LAYER. changing its location should imply to the player that it is being 'taken'. this will probably make more sense once there are backgrounds, as the paintings will then feel more integrated.
    show painting_war green at center 
    "You got an {b}art piece{/b}!" #212 describe war painting
    $ item.painting_war = True
    $ quest.painting_war = True
    $ paintings += 1
    hide painting_war
    p "_" # posty decides to quickly leave.
    jump museum_war

label .glasses2:
    scene bg museum_war
    show rcg
    show bcg
    show posty happy
    p "Sooo what are you discussing?"
    rcg "Oh perfect timing! I was just about to explain to this glaucous grumblewort about how the Reddoinki Renaissance is not only findable with enough determination,{nw}" 
    rcg "but its various progenitors are actually hidden away behind one of the paintings no doubt with new pieces just to be appreciated!{nw}"
    bcg "What a hopelessly naive statement to make, especially regarding the well documented disappearances of all 14 Great Doinkers in the Crimison Expedition of 1923!{nw}"
    bcg "Honestly art hasn't progressed a single inch since those geniuses and their Blouououousian compatriots left this mortal plane...{nw}"
    show posty concerned
    bcg "Just a single one of their pieces makes this entire gallery frankly feel like a frivolous box of toys!{nw}"
    bcg "I don't know why artists today don't give up at the mere thought of them.{nw}"
    rcg "Woah woah that is extremely short sighted even for you!{nw}"
    show posty confused
    rcg "All we have to do to bring back those beautiful days is free those artists from their schlocky cells!{nw}"
    rcg "I swear I heard a couple of noises from that misnomer of a painting at night...{nw}"
    rcg "Crisis of the Populars? An ill befitting name for an ill befitting piece!{nw}"
    rcg "It must be hiding something valuable, like a Doinker at work!{nw}"
    bcg "Now now, you have been watching one too many of those speculative fictions!{nw}"
    bcg "Not every gallery will have globe spanning schemes, sometimes it is just a pile of sad attempts.{nw}"
    rcg "Ohohoho I would loveeee to elucidate you over a couple cakes; maybe it would be nice to have something sweet for once-{nw}"
    bcg "And while we at it, I would like to bring you back to reality with something nonfiction-{nw}"
    rcg "Are you implying that I am delusional?!{nw}"
    bcg "I will never ever stoop as low as to even hint at your ability to read a lot into research.{nw}"
    rcg "Well at least I am able to think outside the constraints of your inability to have fun.{nw}"
    bcg "What is the point of having fun if it results in misinforming people like our observer here!{nw}"
    p "Woah woah I am not getting involved with this!"
    jump museum_war

label .pal:
    scene bg museum_war
    show palettette
    if scanter_green:
        jump .pal3
    elif saw.pal:
        jump .pal2
    else:
        jump .pal1

label .pal1: #205
    show posty neutral
    pal "_" # palettette introduces herself, explaining her backstory and discussing the scanter and offering to demonstrate.
    p "_"
    if item.battery:
        pal "_" # palettette asks like "wait, is that MY battery? you got it for me?" or something
        p "_" # posty acts like she totally grabbed the battery out of wanting to give it to palettette even though this is a lie
        jump .pal_battery
    else:
        $ saw.pal = True
        pal "_" # palettette explains that her battery rolled into ahiss's territory and asks posty to get it back
        jump museum_war

label .pal2: #206
    show posty neutral
    pal "_" # palettette asks if you managed to get the battery
    if item.battery:
        p "_" # posty presents the battery
        jump .pal_battery
    elif battery_asked:
        p "_" # posty explains that ahiss won't hand it over, and there can be an ensuing conversation, potentially offering a hint.
        jump museum_war
    else:
        p "_" # posty says that she hasnt asked yet. there can be a brief interaction here
        jump museum_war

label .pal_battery: #207
    show battery_center
    "You handed over the {b}battery{/b}!"
    $ item.battery = False
    hide battery
    pal "_" # now that she has the battery, palettette demonstrates it on the painting near the glasses.
    scene bg museum_war
    show painting_war # war painting and a green-filtered version of it
    show bcg at right
    show rcg at left
    with pushleft
    bcg "_" # bcg and rcg continue arguing
    rcg "_"
    show painting_war green with vpunch
    ""
    $ scanter_green = True
    bcg "_" # bcg and rcg lose interest in the painting and leave
    rcg "_"
    hide rcg with moveoutright
    bcg "_" # bcg parting remark maybe?
    hide bcg with moveoutright
    scene bg museum_war
    show palettette
    show posty neutral
    with pushright
    pal "_" # palettette talks about how cool the scanter is or something
    p quiet "_" # posty silently thinks to herself that she really really wants that painting.
    p -quiet "_" # posty says goodbye to palettette
    jump museum_war

label .pal3:
    show posty neutral
    p "_" #208 revisiting palettette. avoid mentioning whether posty took the painting.
    pal "_"
    jump museum_war

label .ahiss:
    scene bg museum_war
    show champurrlain #166
    if deed_burned:
        jump .ahiss3
    show battery_floor #168
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
        hide battery_floor
        show battery_center
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
    capsule "Hey! You there, do you mind helping me out with a favor?"
    p "Huh?"
    capsule "I need your help to carry this heavy item off of my hands!"
    p happy "Oh sure! No problem!"
    show capsule happy
    show heavier 
    $ saw.war = True
    $ item.heavier = True
    "You got the {b}heavier{/b}!{p}This thing can remove a lot of fire from an area. It just requires a bit of elbow grease to get it working." 
    hide heavier
    p concerned "Oh wow! This sure is heavy... what even is this?"
    capsule "It's the opposite of a lighter. Instead of adding fire to things, it removes fire from things. It's also heavy."
    p confused quiet "..."
    jump museum_war

label .capsule:
    scene bg museum_war
    show posty neutral
    show capsule happy
    p "_" # Capsule re-explains what the heavier does, in case you forgot. #155 
    jump museum_war
    
