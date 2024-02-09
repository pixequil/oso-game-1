# todo: war exhibit conversation background #149

# todo: war main exhibit painting #225

image bg museum_war_top:
    "map-bgs/museum_war_top.png"
    zoom 1.15
    yalign 0.2

image bg museum_war:
    "dbgs/museum_war_dbg.png"
    yalign 0.2

image bg museum_war_flipped:
    "dbgs/museum_war_dbg.png"
    yalign 0.2
    xzoom -1.0

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
    scene bg museum_war_flipped
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
    scene bg museum_war_flipped
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

label .pal1:
    show posty happy
    $ saw.pal = True
    p "Greetings!"
    pal "Hello! I'm Palettette@."
    p confused "Wait, like, with the @?"
    pal "Yep. Pretty cool, huh? Didn't think you could have that in a name, did ya?"
    p neutral "I didn't."
    pal "So, what's your deal?"
    p concerned "I'm supposed to be delivering this package, but I got all sidetracked..."
    pal "Bummer! Anyway, now that I've heard about you, I get to tell you about me!"
    pal "So, I used to live in Cincinatti, you know, but since I'm an artist, haha, times got tough."
    pal "I got kicked out! How cruel is that! All because it's apparently \"against policy\" to dispose of leftover oil paints in the toilet..."
    show posty annoyed
    pal "But like, what else are toilets for, right?"
    pal "So yeah, anyway though, I had to leave Cincinatti, and I took a bus out here!"
    pal "And I was crashing at a friend's place, when I realized..."
    pal "I forgot my CD player at my old place!"
    pal "I'm so sad... that was like, my favorite thing ever. There's no better way to listen to music, you know!"
    p neutral "I didn't even think people {i}had{/i} CD players anymore."
    pal "Oh, I made my own with spare parts! I'm a real tech wiz! Couldn't you tell?"
    p neutral "Uhh..."
    pal "This thing in my hand! I made it myself! Wanna know what it does?"
    p suspicious "Sure..?"
    pal "I call it...{w} the SCANTER!{w}\nPatent pending."
    pal "It's a combination painter and scanner! Pretty cool, huh?"
    p "How do you combine a painter and a scanner? Wait, what even is a painter anyway?"
    pal "A painter paints! You don't know what a painter is?"
    pal "You're in an art gallery!"
    pal "All these paintings... look around you... made by painters!"
    p concerned "Right..."
    pal "So it's kinda like if a painter was a device instead of a living person that needs to be paid."
    pal "It can't {i}make{/i} paintings yet though. Only change the style of existing ones."
    p suspicious "So like an instagram filter?"
    pal "Sure!"
    pal "I'd show it off, but, I lost the battery. Still, pretty cool thingy for me to hold!"
    if item.battery:
        pal "... Hey wait a sec. Is that my battery? You went and found it for me?? You're so sweet!!!"
        p zany "Huh-oh yup! I totally grabbed it to give to you."
        p "Definitely not lying."
        jump .pal_battery
    else:
        p neutral "What happened to the battery?"
        pal "It rolled away!"
        p "It did?"
        pal "Yep!"
        p suspicious "Why didn't you pick it up?"
        pal "It rolled into another country."
        p astonished anim "ANOTHER COUNTRY?!!"
        show posty suspicious
        pal "According to {b}that cat over there{/b}, yeah! They won't let me have it back, because of their little plot of land!"
        pal "Actually, do you think you could bring me it? That'd be soo sweet!"
        p "Sure..."
        jump museum_war

label .pal2:
    show posty neutral
    pal "Heyy! Did you manage to get the battery?"
    if item.battery:
        p happy "Yeah! Here you go!"
        jump .pal_battery
    elif battery_asked:
        p sad "Ahiss said they won't give it to me. Something about owning the land it rests on and stuff."
        pal "Yeah, they're like that."
        p "Well... I guess I better give up..."
        pal "Oh, don't give up! I'm sure there's a way to convince them that their imaginary claim to land isn't real!"
        pal "If words won't convince them, maybe you can, like, find something to prove it? A counter-deed perhaps!"
        p suspicious "What's a counter-deed?"
        pal "It's like a deed, but on the counter! Haha, get it?"
        pal "You know, like... counters? Kitchen counters? For eating burgers on?"
        p "Other food too, I hope?"
        pal "Right, of course!"
        jump museum_war
    else:
        p "Oops, I didn't try to get it yet."
        jump museum_war

label .pal_battery:
    show battery_center
    "You handed over the {b}battery{/b}!"
    $ item.battery = False
    hide battery
    pal "Alrighty! Now it's time to show off the scanter!"
    pal "Let me aim it like soo..."
    p happy "I can't wait to see it in action!"
    scene bg museum_war_flipped
    show painting_war # war painting and a green-filtered version of it
    show bcg at right
    show rcg at left
    with pushleft
    bcg "...quit being so naive! The Redoinks are clearly fleeing in mass disarray!"
    rcg "Well, that is what a military novice like yourself would say! I see the Blouououous using their cowardly retreat tactic."
    bcg "A military novice would be able to properly identify the state of the battle! Does that triumphant victory really look like \"cowardly retreat\" to you?"
    show painting_war green with vpunch
    ""
    $ scanter_green = True
    bcg "... On the other hand, perhaps it's a depiction of the internal conflicts within the tragic nation of the Greeners."
    rcg "To think they'd have the gall to display such a controversial piece."
    rcg "Let's get out of here!"
    hide rcg with moveoutright
    bcg "Dreadful."
    hide bcg with moveoutright
    scene bg museum_war
    show palettette
    show posty astonished
    with pushright
    pal "Holy moly it works!"
    p quiet "{i}Oh my god I really want that painting, it would be such a vibe...{/i}"
    p happy "Glad to see it works! I gotta go quick now..."
    pal "See ya around and thanks for the battery!"
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
    p happy "Ooh you seem to know a lot about art!"
    buff "Why thank you! I am a fanatic when it comes to these things!"
    buff "The food exhibit in particular is one of the oldest collection of pre OSO artwork in the world, some of them dating back thousands of years!"
    p astonished "Thousands of years?!"
    buff "Indeed. Take this firey masterpiece here!"
    "_" #157 describe the burger painting. There's a painting of the Hideous Burger Fire on the eastern wall, with the fire described as wanting to jump out of the page!
    buff "This painting shows the very last moments of the artist who had painted it."
    buff "If you listen closely, you can hear faint crackling and screams..."
    p concerned "..."
    buff "As though he is still burning alive in that August evening..."
    p suspicious "(I may not know what watercolor is, but they are bluffing!)"
    p "(Maybe I should try out this heavier thing, just in case...)"
    show burger out
    $ item.heavier = False
    $ burger_extinguish = True
    p happy "Wow you have a lot of knowledge about this exhibit!"
    p "Tell me more about this Abandoned in the Grill piece."
    buff "Why.. er certainly"
    buff "It is a misconception that this particular piece is called Abandoned in the Grill because the artist died in a fire..."
    p suspicious "Oh?"
    buff "Yeah yeah err it was because..."
    p "Yes?"
    buff "The artist was being torn from limb to limb by a... burger that became alive!"
    buff "Yeahh yeah yea..."
    p "But I just remember you telling me with absolute certainty you can hear faint crackling if you listen closely enough!"
    buff "Ahhhuhuhuh... it was thematic!"
    p annoyed "You are pulling my flap."
    buff "You finally caught me..."
    show imaginary_lighter #158
    $ item.imaginary_lighter = True
    "You got the {b}imaginary lighter{/b}!{p}description" #159 the imaginary lighter can be used to add fire to imaginary things.
    hide imaginary_lighter
    p confused "Huh?"
    buff "The imaginary and illusory don\'t follow our rules as much as they evade them."
    buff "To make a lie requires the liar to know what looks true."
    buff "You have caught me in a contradiction of my own making, you know this contradictory science like the back of your hand!"
    buff "Making your conscience lighter in the end of it..."
    buff "Con-science lighter, contradictory science lighter..."
    p annoyed "I see"
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
    
