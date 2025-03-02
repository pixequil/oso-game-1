# todo: war exhibit conversation background #149

# todo: war main exhibit painting #225

image bg museum_war_top:
    "map-bgs/museum_war_nav.png"

image bg museum_war:
    "dbgs/museum_war_dbg.png"
    yalign 0.2

image tapestry:
    "talksprites/tapestry.png"
    xalign 0.8
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
    yalign 0.3

image burger out:
    "items/big_fire_painting_2.png"
    xalign 0.45
    yalign 0.3

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
    yalign 0.25
    zoom 1.5

image deed:
    "items/imaginary_deed.png"
    xalign 0.6
    yalign 0.5
    zoom 1.5
    alpha 0.5

image painting_war:
    "items/war_Exhibit_photo_original.png"
    xalign 0.5
    yalign 0.3
    zoom 0.4

image painting_war green:
    "items/war_Exhibit_photo_green.png"
    xalign 0.5
    yalign 0.3
    zoom 0.4

image painting_war red:
    "items/war_Exhibit_photo_red.png"
    xalign 0.5
    yalign 0.3
    zoom 0.4
    
image painting_war blue:
    "items/war_Exhibit_photo_blue.png"
    xalign 0.5
    yalign 0.3
    zoom 0.4

screen war_nav():
    viewport:
        child_size (1280,720)

        add "bg museum_war_top"



        imagebutton:
            pos (550,10)
            idle "war_painting_tiny"
        showif scanter_green == False:
            imagebutton:
                pos (510,0)
                idle "nav_controversy"
                hover "nav_controversy p"
                action Jump("museum_war.painting1")

        showif scanter_green and (quest.painting_war == False):
            imagebutton:
                pos (510,0)
                idle "nav_warting"
                hover "nav_warting p"
                action Jump("museum_war.painting2")

        imagebutton:
            pos (210,0)
            idle "champurrlain_tiny"
        imagebutton:
            pos (200,130)
            idle "dotted line"
        showif deed_burned == False:
            imagebutton:
                pos (200,110)
                idle "battery"
        imagebutton:
            pos (190,0)
            idle "nav_ahiss"
            hover "nav_ahiss p"
            action Jump("museum_war.ahiss")

        imagebutton:
            pos (870,40)
            idle "nav_pal"
            hover "nav_pal p"
            action Jump("museum_war.pal")

        imagebutton:
            pos (340,320)
            idle "war_island"
        showif burger_extinguish == False:
            imagebutton:
                pos (550,380)
                idle "burger_fire"
        showif burger_extinguish:
            imagebutton:
                pos (550,380)
                idle "burger_out"

        showif scanter_green:
            imagebutton:
                pos (760,380)
                idle "nav_controversy"
                hover "nav_controversy p"
                action Jump("museum_war.glasses2")

        imagebutton:
            pos (470,350)
            idle "nav_buff"
            hover "nav_buff p"
            action Jump("museum_war.buff")

        imagebutton:
            pos (190,410)
            idle "nav_capsule"
            hover "nav_capsule p"
            action Jump("museum_war.capsule")

        imagebutton: 
            xanchor 0.5
            yanchor 0.5
            pos (1011, 640)
            idle "arrow dn"
        imagebutton: 
            xanchor 0.5
            yanchor 0.5
            pos (1011, 640)
            idle "pnav dn i"
            hover "pnav dn"
            action Jump("museum_entrance")

image nav_capsule = Composite(
    (250,250),
    (0,0), "hitbox",
    (40,120), "minisprites/capsule.png",
)
image nav_capsule p = Composite(
    (250,250),
    (0,0), "nav_capsule",
    (30,70), "pnav lt"
)

image nav_warting = Composite(
    (250,250),
    (0,0), "hitbox",
)
image nav_warting p = Composite(
    (250,250),
    (0,0), "nav_warting",
    (60,20), "pnav up"
)

image nav_buff = Composite(
    (250,250),
    (0,0), "hitbox",
    (140,90), "minisprites/buff.png",
)
image nav_buff p = Composite(
    (250,250),
    (0,0), "nav_buff",
    (40,40), "pnav up"
)

image nav_controversy = Composite(
    (250,250),
    (0,0), "hitbox",
    (30,80), "nav_rcg",
    (140,80), "nav_bcg"
)
image nav_controversy p = Composite(
    (250,250),
    (0,0), "nav_controversy",
    (60,20), "pnav up"
)

image nav_rcg:
    "minisprites/rose-colored-glasses-angry-sprite.png"
image nav_bcg:
    "minisprites/bcg.png"
    xzoom -0.7
    yzoom 0.7

image nav_pal = Composite(
    (250,250),
    (0,0), "hitbox",
    (100,40), "minisprites/palettette.png",
)
image nav_pal p = Composite(
    (250,250),
    (0,0), "nav_pal",
    (0,20), "pnav rt"
)
image war_painting_tiny = ConditionSwitch(
    "quest.painting_war == True","nothing",
    "scanter_green == True","war_painting_green",
    "True","war_painting_original"
)
image war_painting_original:
    "items/war_Exhibit_photo_original.png"
    zoom 0.1
image war_painting_green:
    "items/war_Exhibit_photo_green.png"
    zoom 0.1
image nav_ahiss = Composite(
    (250,250),
    (0,0), "hitbox",
    (70,40), "minisprites/ahiss_the_Cat_over.png",
)
image nav_ahiss p = Composite(
    (250,250),
    (0,0), "nav_ahiss",
    (50,40), "pnav up"
)

image champurrlain_tiny:
    "items/Champurrlain_painting.png"
    zoom 0.35
image war_island:
    "map-bgs/museum_war_top_island.png"


label museum_war:
    if renpy.music.get_playing() != "sound/music/Gavimator - the jungle.ogg":
        play music "sound/music/Gavimator - the jungle intro.ogg" if_changed
        queue music "sound/music/Gavimator - the jungle.ogg"
    $ renpy.choice_for_skipping()
    $ renpy.save_persistent()
    call screen war_nav

# label museum_war:
#     if saw.war == False:
#         jump .capsulefirst
#     scene bg museum_war_top
#     show posty neutral

#     p "_" # todo: war exhibit imagemap #150 #169

#     menu:
#         "Capsule":
#             jump .capsule
#         "Buff":
#             jump .buff
#         "Ahiss the Cat":
#             jump .ahiss
#         "Palettette@":
#             jump .pal
#         "Main Exhibit\nRose-Colored Glasses & Blue-Colored Glasses" if scanter_green == False:
#             jump .painting1
#         "Main Exhibit" if (scanter_green == True) and (quest.painting_war == False):
#             jump .painting2
#         "Rose-Colored Glasses & Blue-Colored Glasses" if scanter_green:
#             jump .glasses2
#         "Return to the entrance.":
#             jump museum_entrance

label .painting1:
    scene bg museum_war_flipped
    show painting_war
    show rcg
    show bcg
    if saw.glasses:
        show posty neutral
        "The two still seem to be fighting."
        show rcg:
            xzoom -1.0
            xpos 0.6
        rcg "Is there something you need? We're in the middle of an important discussion."
        bcg "Why don't we ask her?"
        rcg "Good idea!"
        show rcg with move:
            xpos 0.8
        rcg "Tell us? Does this painting show the victory of the Redoinks or the Blouououous?"
        p concerned "It's in black and white. I can't tell which army is which."
        rcg "You can figure it out through the context clues hidden in the painting!"
        bcg "Expressions, tints and shades, knowledge of basic history!"
        p "Um, I don't know. Sorry. I'm not qualified to interpret art."
        bcg "Then please let us continue our debate without you."
        jump museum_war
    else:
        show posty neutral
        p "Uh excu-{nw}"
        rcg "This art piece clearly shows the victory of the Redoinks!"
        bcg "No.{w} The positioning obviously implies the victory of the Blouououous."
        bcg "They are so wounded and depressed, having to fight in a war n' all, yknow?"
        rcg "What do you mean!?! The determination in their eyes say it all! You always see the gloomy parts of EVERYTHING!"
        bcg "You always see the hopeful parts, even when it isn't intended!"
        p quiet "{i}They look busy. I should probably leave.{/i}"
        $ saw.glasses = True
        jump museum_war

label .painting2:
    scene bg museum_war_flipped
    show painting_war green
    show posty happy
    p "This painting looks so cool! Maybe nobody will notice if I..." 
    hide painting_war green # !! HIDING AND SHOWING THE PAINTING MOVES IT TO THE FRONT LAYER. changing its location should imply to the player that it is being 'taken'. this will probably make more sense once there are backgrounds, as the paintings will then feel more integrated.
    show painting_war green at center 
    "You got an {b}art piece{/b}! {w}\nThis painting looked a lot more meaningful and violent when it was in black and white. Now it just looks green. And violent."
    extend " It gives you a feeling of {color=#ffff00}{i}inspiration{/i}{/color}!"
    $ item.painting_war = True
    $ quest.painting_war = True
    $ paintings += 1
    hide painting_war
    p "{i}cough{/i} Oh no, where'd the painting go? I guess there's nothing to see here anymore, everyone!"
    hide posty with moveoutright
    jump museum_war

label .glasses2:
    scene bg museum_war
    show tapestry
    show rcg
    show bcg
    show posty happy
    p "Sooo what are you discussing?"
    rcg "Oh perfect timing! I was just about to explain to this glaucous grumblewort about how the Reddoinki Renaissance is not only findable with enough determination,{nw}" 
    rcg "but its various progenitors are actually hidden away behind one of the paintings, no doubt with new pieces just to be appreciated!{nw}"
    bcg "What a hopelessly naive statement to make, especially regarding the well documented disappearances of all 14 Great Doinkers in the Crimison Expedition of 1923!{nw}"
    bcg "Honestly art hasn't progressed a single inch since those geniuses and their Blouououousian compatriots left this mortal plane...{nw}"
    show posty concerned
    bcg "Just a single one of their pieces makes this entire gallery frankly feel like a frivolous box of toys!{nw}"
    bcg "I don't know why artists today don't give up at the mere thought of them.{nw}"
    rcg "Woah woah that is extremely short sighted, even for you!{nw}"
    show posty confused
    rcg "All we have to do to bring back those beautiful days is free those artists from their schlocky cells!{nw}"
    rcg "I swear I heard a couple of noises from that misnomer of a painting at night...{nw}"
    rcg "Crisis of the Populars? An ill befitting name for an ill befitting piece!{nw}"
    rcg "It must be hiding something valuable, like a Doinker at work!{nw}"
    bcg "Now now, you have been watching one too many of those speculative fictions!{nw}"
    bcg "Not every gallery will have globe spanning schemes, sometimes it is just a pile of sad attempts.{nw}"
    rcg "Ohohoho I would loveeee to elucidate you over a couple cakes; maybe it would be nice to have something sweet for once-{nw}"
    bcg "And while we're at it, I would like to bring you back to reality with something nonfiction-{nw}"
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
    hide battery_center
    pal "Alrighty! Now it's time to show off the scanter!"
    show posty neutral
    pal "There, that black and white painting looks like the perfect target!"
    pal "Let me aim it like soo..."
    p happy "I can't wait to see it in action!"
label .nogood2:
    pal "What color should I change it to?"
    menu:
        "Red!":
            jump .red
        "Blue!":
            jump .blue
        "Green!":
            jump .green
label .nogood:
    scene bg museum_war
    show palettette
    show posty annoyed
    with pushleft
    pal "Look at it go! My invention is incredible!"
    p annoyed quiet "{i}Well... those two are still arguing. Just differently. I wonder if there's something I can do to make them stop!{/i}"
    pal "Want me to do it again?"
    p happy "Sure!"
    pal "Okay, first, I'll revert the changes..."
    show palettette with vpunch
    pal "Kabam!"
    p "Incredible!"
    jump .nogood2
label .blue:
    scene bg museum_war_flipped
    show painting_war
    show bcg at right
    show rcg at left
    with pushright
    rcg "The redoinks, you can recognize them just from their chivalrous adamance."
    bcg "From here, it looks like spineless timidity."
    rcg "Well, they don't have spines, but that's no sign of a lack of courage! See, this one-"
    bcg "That's a Blouououou. Not a Redoink. You can tell because she's chasing off that piteous Redoink over-"
    show painting_war blue with vpunch
    ""
    rcg "I beg your pardon?"
    rcg "That's a Blouououou. He's blue."
    bcg "The valorous heroes are blue as well! It's the victory of the Blouououous, without a doubt!"
    rcg "Victory over who, exactly? Not over the Redoinks, they're not depicted."
    bcg "The Redoinks would never appear in such a victorious painting, having no record of victory whatsoever!"
    rcg "You- this is heresy, look..."
    jump .nogood
label .red:
    scene bg museum_war_flipped
    show painting_war
    show bcg at right
    show rcg at left
    with pushright
    bcg "And I insist, it this is very clearly the victory of the Blouououous!"
    rcg "No, no, amateur mistake, I've been telling you! That one, right there, is a fleeing Blouououou. You can tell, by examining his-"
    show painting_war red with vpunch
    ""
    bcg "You were saying?"
    rcg "I- oh, I concede, I had misread the face of this fleeing soldier, it's... it's actually..."
    bcg "Hah! You were wrong! it's the victory of the Blouououous!"
    rcg "I see no Blouououous here."
    bcg "A-"
    bcg "But, but you see..."
    jump .nogood
label .green:
    scene bg museum_war_flipped
    show painting_war
    show bcg at right
    show rcg at left
    with pushright
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
    with pushleft
    p quiet "{i}Oh my post office I really want that painting, it would be such a vibe...{/i}"
    p happy "Glad to see it works! I gotta go quick now..."
    pal "See ya around and thanks for the battery!"
    jump museum_war

label .pal3:
    show posty neutral
    pal "Hey Posty! What's up? You want to see how the scanter works again?"
    p "Nah, I'm good."
    pal "Well, that's a relief, because I don't have any paintings to use it on anymore."
    pal "Don't worry though! Once I get this thing finished, it won't need pre-made paintings to do it\'s job."
    p "A device that can make images on its own..."
    p concerned "For some reason, the idea of that scares me."
    pal "Nah, don't fret it. It's a one-of-a-kind device. You don't need to worry about it being misused!"
    p happy "That's good to hear. Talk to you later."
    jump museum_war

label .ahiss:
    scene bg museum_war
    show champurrlain
    if deed_burned:
        jump .ahiss3
    show battery_floor
    show ahiss
    if saw.ahiss == False:
        $ saw.ahiss = True
        jump .ahiss1
    elif saw.ahiss:
        jump .ahiss2
    "if you're seeing this, there's a problem"

label .ahiss1:
    show posty neutral with moveinleft
    if saw.pal:
        p happy "Aha! There\'s the batteries."
    show posty astonished
    $ renpy.transition(hpunch, layer="master") #prevents interruption of the text window
    ahiss "HALT! State your business immediately. I will not tolerate intruders upon my land."
    show posty quiet:
        xalign -0.3
    $ renpy.transition(move, layer="master") #prevents interruption of the text window
    p -quiet "Woah! I don\'t want any trouble. I\'m just…"
    p suspicious "Hang on, your land?"
    show deed #170
    ahiss "The deed\'s right here, darling. This kingdom belongs to me. See it for yourself."
    p neutral "I can\'t see it."
    ahiss "Huh? Well, IGNORANCE OF THE LAW IS NO EXCUSE! LEAVE AT ONCE!"
    p astonished "AGH! Will do…"
    ahiss "To yield even one morsel of this land\'s bounty to you, that would be an insult to the great Champurrlain and the flag they fought for."
    p neutral "Hm? Who\'s Champurrlain?"
    ahiss "Hmph, I suppose people do come to this museum to educate themselves… "
    hide deed
    ahiss "Very well then. Champurrlain is none other than the cat you see in the painting before you, whom I happen to be a direct descendant of. "
    p astonished "Really? I would\'ve never guessed. "
    ahiss "Yes, yesss! A legendary war hero of unmatched brilliance. They practically invented the element of surprise. "
    p annoyed "The element of surprise, you say…"
    ahiss "What a battle it was, indeed. From the moment that Champurrlain\'s troops rode their invisible horses into battle, victory was imminent. "
    ahiss "They readied their imperceptible cannons, cleverly struck down the opposition with a barrage of undetectable cannonballs, and planted their flag to claim the land. "
    ahiss "That flag...nothing brings a tear to the eye quite like its majestic, ultraviolet hue."
    jump .ahiss_deed

label .ahiss2:
    show posty neutral with moveinleft
    ahiss "Didn't I say to leave?!?"
    show deed 
    $ renpy.transition(hpunch, layer="master")
    ahiss "I mustn't explain what I\'ve already told you about what this deed entails! Now go!"
    show posty:
        xalign -0.3
    $ renpy.transition(move, layer="master")
    p concerned "Oh, uh, Sorry. I forgot I'm not supposed to be back here. I just wanted to revisit and see what you were doing…"
    ahiss "Well I\'m doing nothing now that you're here! If you forget and revisit again, you will suffer the consequences! Now get going and don't come back!"
    jump .ahiss_deed

label .ahiss_deed:
    if item.imaginary_lighter == False:
        if saw.pal:
            p sad "Well... anyway."
            p "Do you think I could have that battery on the ground?"
            ahiss "Absolutely not!"
            show deed
            ahiss "As this deed clearly specifies, any property, including items that may or may not \"accidentally fall\" within our borders, as private property belonging to this land's owner, namely me."
            p angry "What deed? You must be imagining it out of thin air."
            p astonished "Oh."
            ahiss "It's still a valid piece of documentation that certifies me as owner of this land."
            p neutral "I guess."
            $ battery_asked = True
        p "Well, I'll leave you be, then."
        jump museum_war
    else:
        p neutral quiet "{i}Maybe I can use my {b}imaginary lighter{/b} on the imaginary deed!{/i}"
        show posty:
            xalign -0.05
        $ renpy.transition(move, layer="master") #prevents interruption of the text window
        ahiss "Are your ears clogged with fur? Or do you not even have ears at all? I said to stay out of my property!"
        show deed
        ahiss "This deed decrees you as a dastardly invader of this land!"
        hide deed
        $ renpy.transition(irisout, layer="master") #prevents interruption of the text window
        "You {b}imaginary burned{/b} the {b}imaginary deed{/b}!"
        $ deed_burned = True
        $ item.imaginary_lighter = False
        if saw.pal:
            p happy "I'll take this, since it belongs to Palettette@!"
        else:
            p neutral "Oh, look, a battery. Yoink!"
        hide battery_floor
        show battery_center
        "You got the {b}battery{/b}!{w} \nA giant D battery meant to run large electrical devices."
        $ item.battery = True
        hide battery_center
        if battery_asked:
            ahiss "Grr... hiss... I hope you're happy. You've destroyed my family legacy!"
            p annoyed "Well, you wouldn't give me the battery."
            ahiss "You'd incinerate my intergenerational fortune, just like that?"
            ahiss "You could've gone to a corner store, you freak!"
        else:
            ahiss "Th- THAT'S ALL YOU WANTED?!!"
            if saw.pal:
                p "Pretty much."
                ahiss "Ugh, the... the nerve..."
            else:
                p "No, I just kinda saw it and I was like \"I may as well take it.\""
                p happy "You never know when you'll need stuff like this, right?"
                ahiss "Tch... well, thanks for clearing out the trash laying around."
                ahiss "Yes, yes. You, cleaning trash. It suits you! Ohohoho!~"
        ahiss "... Maybe this is good for me in the end."
        ahiss "After all, maintaining our land here was starting to get boring."
        ahiss "Now maybe I can go explore new avenues!"
        ahiss "Literally."
        jump museum_war

label .ahiss3:
    show ahiss
    show posty neutral with moveinleft
    p "Hello, excuse me? Ahiss?"
    ahiss "...Do I know you?"
    p suspicious "I'm Posty?"
    p "I may have.. uh.. burnt your royal deed and stole a battery or something off your land."
    ahiss "Hm? Ah yes. I remember vividly now. You\'re that peasant that RUINED MY LIFE!"
    ahiss "The pain and suffering you've done to our people. Me!"
    p annoyed "Okay."
    ahiss "I hope that silly trinket was worth the devastation you wreacked upon me."
    ahiss "Ohhh, but prepare yourself soon for my glorious return!"
    ahiss "For I shall arise as the rightful heir, throwing away those unnatural chains upon my destiny and seize what is MY DIVINE RIGHT-{nw}"
    p "Really, I didn't think it was that big of a-{nw}"
    ahiss "That is enough out of you, thank you!"
    ahiss "Leave and never come back! I don't want to see your face ever again!"
    p "I was just going to say-{nw}"
    ahiss "I'm giving you one last chance before I call my royal guards to deal with you."
    p "I don't see any royal guards."
    ahiss "..."
    show posty astonished with hpunch
    ahiss "GET OUT! GO AWAY!"
    p happy "And a good day to you too, regent, or should I say, fellow citizen!" 
    hide posty with moveoutleft
    ahiss "My honour and lands shall be back in my hands soon; I just need to rally the troops again like the good old days..."
    ahiss "You shall rue the day you crossed my path, glorified breadbox!" 
    jump museum_war

label .buffsaw:
    scene bg museum_war
    show burger fire
    show posty neutral
    show buff
    jump .buffsawin # spaghetti! smelly!

label .buff:
    if burger_extinguish == True:
        jump .buff2
    elif saw.buff == True:
        jump .buffsaw
    scene bg museum_war
    show burger fire
    show posty happy
    show buff
    $ saw.buff = True
    p "Ooh, hello! You look like you know a lot about art!"
    buff "Why thank you! I am a fanatic when it comes to these things!"
    buff "The war exhibit in particular is one of the oldest collections of pre-OSO artwork in the world, some of them dating back thousands of years!"
    p astonished "Thousands of years?!"
    buff "Indeed. Take this firey masterpiece here! {i}\"Abandoned In The Grill.\"{/i}"
    "{i}It's a painting of a truly ugly burger on fire. The fire seems very realistic, being the only good thing about the painting.{/i}"
    buff "This watercolor painting shows the very last moments of the artist who had painted it."
    buff "If you listen closely, you can hear faint crackling and screams..."
    p concerned quiet "..."
label .buffsawin: # for jumping to the middle of the conversation!
    buff "As though he is still burning alive on that August evening..."
    p suspicious "{i}I may not know what watercolor is, but they are bluffing!{/i}"
    if (item.heavier == False):
        p "{i}But it's not like I can do anything about this bluffing buff.{/i}"
        jump museum_war
    p "{i}Maybe I should try out this heavier thing, just in case...{/i}"
    play sound "sound/shoop.wav"
    show burger out
    $ item.heavier = False
    $ burger_extinguish = True
    "You used the {b}Heavier{/b} to un-light the painting on fire!"
    p happy -quiet "Wow, you have a lot of knowledge about this exhibit!"
    p "Tell me more about this Abandoned in the Grill piece."
    buff "Why.. er... certainly!"
    buff "It is a misconception that this particular piece is called Abandoned in the Grill because the artist died in a fire..."
    p suspicious "Oh?"
    buff "Yeah yeah, err, it was because..."
    p "Yes?"
    buff "The artist was being torn from limb to limb by a... burger that became alive!"
    buff "Yeahh yeah yea..."
    p "But I just remember you telling me with absolute certainty you can hear faint crackling if you listen closely enough!"
    buff "Ahhhuhuhuh... it was thematic!"
    p annoyed "You are pulling my flap."
    buff "You finally caught me..."
    show imaginary_lighter #158
    $ item.imaginary_lighter = True
    "You got the {b}imaginary lighter{/b}!"
    extend "\nBe careful so as to not burn your imaginary friends. Though if you have imaginary enemies, use this to set them and any of their imaginary things on fire! Go ham!"
    hide imaginary_lighter
    p confused "Huh?"
    buff "The imaginary and illusory don\'t follow our rules as much as they evade them."
    buff "To make a lie requires the liar to know what looks true."
    buff "You have caught me in a contradiction of my own making. You know this contradictory science like the back of your hand!"
    buff "Making your conscience lighter in the end of it..."
    buff "Con-science lighter, contradictory science lighter..."
    p annoyed "I get it."
    jump museum_war


label .buff2:
    scene bg museum_war
    show burger out
    show posty neutral
    show buff
    buff "Wait. You want more history?"
    buff "Even after catching me in my previous blunder? "
    buff "No. I know your tricks."
    buff "As the great Applexander Hamilton once said, {i}\"Fool me once, you\'re to blame. Fool me twice, it\'s a jester\'s game.\" {/i}"
    p quiet ". . ."
    p suspicious -quiet "What?"
    buff "I may have been outsmarted once, but I\'m smart enough to know that my efforts will be futile when it comes to you."
    jump museum_war

label .capsulefirst:
    scene bg museum_war
    show whatever painting at truecenter
    show posty neutral 
    show capsule pain
    capsule "Hey! You there, do you mind helping me out with a favor?"
    p "Huh?"
    capsule "I need your help to carry this heavy item off my hands!"
    p happy "Oh sure! No problem!"
    show capsule happy
    show heavier 
    $ saw.capsule = True
    $ item.heavier = True
    "You got the {b}heavier{/b}!{p}This thing can remove a lot of fire from an area. It just requires a bit of elbow grease to get it working." 
    hide heavier
    p concerned "Oh wow! This sure is heavy... what even is this?"
    capsule "It's the opposite of a lighter. Instead of adding fire to things, it removes fire from things. It's also heavy."
    p confused quiet "..."
    jump museum_war

label .capsule:
    if (saw.capsule == False):
        jump .capsulefirst
    scene bg museum_war
    show whatever painting at truecenter
    show posty neutral
    show capsule happy
    if item.heavier:
        p confused "Hey! Uh... can you explain what the heavier does again?"
        capsule "I'd be happy to!"
        show heavier
        capsule "Unlike a lighter, it removes fire! No need for water or fire extinguishers here!"
        p happy "Well, thanks for explaining it again."
        capsule "No problem!" 
    else:
        p "You never told me it could put out fires on paintings."
        capsule "Oh right, I forgot to tell you about that part. To be honest, I don\'t know how that even happens myself."
        capsule "Gotta love how things work, right?"
        p "Yeah, I guess I do."
        capsule "Just don\'t cause any mayhem with that thing!"
        p happy "Alrighty!"
        capsule "If anybody saw what you did to the painting, you\'d be in trouble."
        p concerned "Oh shoot... They won\'t notice, right?"
        capsule "Ehhhh... sure."
    jump museum_war
    
