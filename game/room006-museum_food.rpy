# todo: food exihibit conversation bg #190

# todo: food main exhibit painting #226

image bg museum_food_nav:
    "map-bgs/museum_food_nav.png"

image bg museum_food:
    "dbgs/museum_food_dbg.png"

image badpainting:
    "items/badpainting.jpg"
    zoom 0.1
    yalign 0.5

image painting_food floor:
    "items/Brussel_Sprouts.png"
    xalign 0.5
    yalign 1.0
    zoom 0.75

image painting_food:
    "items/Brussel_Sprouts.png"
    xalign 0.5
    yalign 0.3
    zoom 0.75

image eating:
    "items/personeatingfoodpainting.png"
    xalign 0.5
    yalign 0.4
    zoom 1.75

screen food_nav():
    viewport:
        child_size (1280,720)
        add "bg museum_food_nav"

        showif (quest.painting_food == False):
            imagebutton:
                pos (970,40)
                idle "brussels"
            imagebutton:
                pos (840,20)
                idle "nav_rm"
                hover "nav_rm p"
                action Jump("museum_food.painting")

        imagebutton:
            pos (470,50)
            idle "food_mini1"
        imagebutton:
            pos (630,55)
            idle "nbspain"
        imagebutton:
            pos (800,50)
            idle "food_mini3"
        imagebutton:
            pos (540,30)
            idle "nav_np"
            hover "nav_np p"
            action Jump("museum_food.notepad")

        imagebutton: 
            xanchor 0.5
            yanchor 0.5
            pos (270, 640)
            idle "arrow dn black"
        imagebutton: 
            xanchor 0.5
            yanchor 0.5
            pos (270, 640)
            idle "pnav dn i"
            hover "pnav dn"
            action Jump("museum_entrance")
        imagebutton: 
            xanchor 0.5
            yanchor 0.5
            pos (323, 140)
            idle "arrow up black"
        showif (food_switch == False):
            imagebutton:
                pos (260,50)
                idle "corndogpainting"
        imagebutton: 
            xanchor 0.5
            yanchor 0.5
            pos (323, 140)
            idle "pnav up i"
            hover "pnav up"
            action If(food_switch,Jump("janitors"),Notify("It doesn't even look like it's held up on the wall... Weird."))

        imagebutton:
            pos (360,320)
            idle "food_island"
        imagebutton:
            pos (400,370)
            idle "poplars"
        showif (food_switch == False):
            imagebutton: 
                xanchor 0.5
                yanchor 0.5
                pos (450, 450)
                idle "pnav up i"
                hover "pnav up"
                action Play("sound","sound/51166__rutgermuller__switch_01a.ogg"),SetVariable("food_switch",True),With(vpunch)
        showif food_switch:
            imagebutton: 
                xanchor 0.5
                yanchor 0.5
                pos (450, 450)
                idle "pnav up i"
                hover "pnav up"
                action Jump("museum_food.eating")
        imagebutton:
            pos (800,365)
            idle "food_mini2"
        imagebutton:
            pos (600,358)
            idle "marbsp"

        showif quest.painting_food:
            imagebutton:
                pos (840,470)
                idle "nav_rm"
                hover "nav_rm p"
                action Jump("museum_food.rm")
        imagebutton:
            pos (520,350)
            idle "nav_mb"
            hover "nav_mb p"
            action Jump("museum_food.marble")

        imagebutton:
            pos (560,560)
            idle "applestand"

image nav_np = Composite(
    (250,250),
    (0,0), "hitbox",
    (160,80), "minisprites/notepad (1).png",
)
image nav_np p = Composite(
    (250,250),
    (0,0), "nav_np",
    (50,70), "pnav rt"
)

image marbsp:
    "talksprites/food_big2.png"
    zoom 0.2
image nbspain:
    "talksprites/food_big3.png"
    zoom 0.2

image nav_mb = Composite(
    (250,250),
    (0,0), "hitbox",
    (160,80), "minisprites/fffffffffffmarble_final.png",
)
image nav_mb p = Composite(
    (250,250),
    (0,0), "nav_mb",
    (50,70), "pnav rt"
)

image nav_rm = Composite(
    (250,250),
    (0,0), "hitbox",
    (160,80), "rmm",
)
image nav_rm p = Composite(
    (250,250),
    (0,0), "nav_rm",
    (50,70), "pnav rt"
)
image rmm:
    "minisprites/ripped_mitten_alpha.png"
    zoom 0.7

image applestand = Composite(
    (300,300),
    (0,46),"map-bgs/applestand.png",
    (4,0),"items/OSO_stone_apple_prop.png"
)

image brussels:
    "items/Brussel_Sprouts.png"
    zoom 0.15
image poplars:
    "items/personeatingfoodpainting.png"
    zoom 0.5
image corndogpainting:
    "items/corndogpainting.png"
    zoom 1.5
image food_island:
    "map-bgs/museum_food_top_island.png"

image food_big1:
    "talksprites/food_big1.png"
    xalign 0.5
    yalign 0.3
image food_big2:
    "talksprites/food_big2.png"
    xalign 0.5
    yalign 0.3
image food_big3:
    "talksprites/food_big3.png"
    xalign 0.5
    yalign 0.3


label museum_food:
    $ renpy.choice_for_skipping()
    call screen food_nav

# label museum_food:
#     scene bg museum_food_top
#     show posty neutral

#     p "_" # todo: food exhibit imagemap #224

#     menu:
#         "Ripped Mitten & Unappetizing painting" if (quest.painting_food == False):
#             jump .painting
#         "Ripped Mitten" if quest.painting_food:
#             jump .rm
#         "Notepad":
#             jump .notepad
#         "Marble Bust":
#             jump .marble
#         "Corndog painting" if (food_switch == False):
#             jump .corndog
#         "Hidden passageway" if food_switch:
#             jump janitors
#         "Eating painting":
#             jump .eating
#         "Go back to the entrance.":
#             jump museum_entrance

label .marble:
    scene bg museum_food
    show food_big2
    show marble
    if quest.money_food:
        jump .marble3
    elif saw.marble:
        jump .marble2
    else:
        jump .marble1
    
    label .marble1:
    show posty neutral
    $ saw.marble = True
    marble "As an art critic and collector, I am severely disappointed with these so-called \"artworks\"! Everything here is so bland."
    p suspicious "..Okaay? Who are you?"
    marble "I am Marble Bust. My personal collection of fine art is one of the most respected in the art world! My name means something in this town!"
    marble "And as I said, this entire exhibit is lacking when it comes to wowing me! In fact, this entire museum has been rather upsetting. Nothing in here would fit for my collection!"
    if item.napkin:
        jump .marble_napkin
    else:
        p neutral "I don't know. I saw this one piece that-{nw}"
        marble "You clearly don't understand true art! Leave at once while I search for {b}the ultimate work of art{/b}!"
        jump museum_food

label .marble2:
    show posty neutral
    if item.napkin:
        jump .marble_napkin
    else:
        marble "Did you not hear me? Get out! I am trying to find {b}the ultimate work of art{/b}!"
    jump museum_food

label .marble_napkin: 
    marble "Hold on. What is that you're holding?"
    p "This?"
    show badpainting
    marble "Why... This is the greatest artwork I have ever seen! I simply must have it for my collection!! I will pay handsomely!"
    p suspicious "{i}Really??{/i}"
    p happy "Oh, I'm not sure! I don't want to give away this wonderful piece of art, but alright!"
    "You handed over the {b}priceless, one-of-a-kind highbrow painting{/b}!"
    $ item.napkin = False
    hide badpainting
    $ money += 2
    $ quest.money_food = True
    show cash_bundle_2 at truecenter
    $ renpy.transition(irisout, layer="master") #prevents interruption of the text window
    "{b}{color=#bdbb9a}Marble Bust{/color}{/b} gave you {b}some money{/b}!"
    hide cash_bundle_2
    call money_get
    p "Farewell!"
    jump museum_food

label .marble3:
    show posty neutral
    p "What are you going to do with your painting?"
    marble "I will hang it up proudly in my home proudly!"
    marble "The craft! The mediums! The deeper themes! You must tell me how you created this piece!"
    p "Oh, it's a complex forgotten art. You wouldn't get it. I'm sorry, but I'm busy right now."
    marble "Thank you for this masterpiece!"
    jump museum_food

label .notepad:
    scene bg museum_food
    show food_big3
    show notepad
    if gave_chips:
        jump .notepad3
    elif saw.notepad:
        jump .notepad2
    else:
        jump .notepad1

label .notepad1:
    show posty concerned
    $ saw.notepad = True
    p "Oh my, are you alright?"
    notepad "Can't you tell?! I am at rock bottom here."
    notepad "I have turned my whole life upside down for the chance of exhibitions and now I can't even afford a bite to eat!!"
    notepad "Many times I pleaded and begged the curators to buy my life's work, many times they rejected me..."
    p sad "Man that sucks."
    notepad "Not even half of it. I reduced my prices all the way down to $2 for everything I ever made."
    notepad "You know what they said? No!"
    notepad "I am at my wits end: starving in the middle of the food exhibit."
    notepad "I should've stayed back home, then I wouldn't have ended up here."
    notepad "Time after time I put so much heart into this, only to be thrown out like a stray cup."
    notepad "I don't know why I bother."
    if item.chips:
        jump .notepad_chips
    else:
        notepad "Hey gal, you have any food?"
        p concerned "Sorry, I don't have a crumb on me."
        notepad "If you find some, please give it to me! I can hear my stomach rumbles from here!"
        p "Will do, will do."
        jump museum_food

label .notepad2:
    show posty neutral
    notepad "Oh hey, it's you again! Do you have any food on you now?"
    if item.chips:
        jump .notepad_chips
    else:
        p "Sorry, I still got nothing."
        notepad "Oh well. Let me know if you find any. I would appreciate it!"
        jump museum_food

label .notepad_chips:
        p "It isn't much, but I got a bunch of chips if you wan-"
        notepad "OOOHH PLEASE GIVE IT TO ME THANK YOU SO MUCH!!!"
        p "You need it more than I do."
        show generichips at truecenter
        "You handed over the {b}Generi-Chips{/b}!"
        $ item.chips = False
        $ gave_chips = True
        hide generichips
        notepad "This tastes soooo amazing!"
        notepad "First meal in a week, you are my shining saviour!"
        p happy "Glad to be of help!"
        notepad "For assisting me in my direst hour, you shall have my greatest work."
        notepad "It distills my essence into a small package you can carry around as a reminder."
        p astonished "Aw shucks, that is too much!"
        show badpainting
        "You got the {b}napkin \"painting\"{/b}!{w} If this was in the eye of the beholder, then they would go blind. It's not even painted."
        $ item.napkin = True
        hide badpainting
        p confused "Oohhheheh it looks... avant garde."
        notepad "This is for feeding me, only the best!"
        p happy "Hehe no biggie!"
        p suspicious quiet "{i}Did they pick up some trash to fool me? Why would anyone even consider this?{/i}"
        p neutral quiet "{i}Eh whatever, it's free.{/i}"
        p concerned "Ahahaha ohh I am soo sorry, I have a meeting in 30 minutes!"
        p concerned "I can't hang around any longer sadly..."
        notepad "It is a shame I can't see your enjoyment for any longer."
        p happy "See you around I guess!"
        jump museum_food
label .notepad3:
    show posty concerned
    notepad "Oh, hey! Hey! Over here, yeah! If you have any more chips or anything, I can give you another masterpiece!"
    p quiet "{i}Erm, I think I\'ll pass on another of what this guy considers a \"masterpiece\"...{/i}"
    p -quiet "Uh...I don\'t have anymore food on me, sorry."
    notepad "Hmph. And here I thought you had true aesthetic instincts, but I guess you\'re just another pedestrian in denial. Sigh…"
    p "Hey, I said sorry!"
    jump museum_food

label .painting:
    scene bg museum_food
    show painting_food
    show posty neutral
    show rm
    p "Um, hi there!"
    rm "Oh hello! I'm currently looking at..."
    extend " whatever this is."
    rm "This {i}thing{/i} feels so out of place here... Honestly, they could've used a better painting."
    p happy "I'm sure someone would want it!"
    rm "Doubt it."
    hide rm with moveoutright
    show posty astonished
    "The odd painting suddenly and inexplicably calls out to you. You are filled with {color=#ffff00}{i}inspiration{/i}{/color}."
    p astonished quiet "{i}...I need it.{/i}"
    p happy quiet "{i}It's not like it'll be missed anyway!{/i}"
    hide painting_food
    show painting_food floor
    "You got an {b}art piece{/b}! A strange painting depicting... brussel sprouts?"
    $ item.painting_food = True
    $ quest.painting_food = True
    $ paintings += 1
    hide painting_food
    if paintings == 1:
        p happy "Hehheheehehe! Oh I want to find more!"
    else:
        p happy "That was easy! I'm not complaining though!"
    jump museum_food

label .rm:
    scene bg museum_food
    show food_big1
    show posty neutral
    show rm
    rm "Oh hey, what's up?"
    p "Nothing much, how about you?"
    rm "Eh, it could be better. I wanted to get a picture in front of a painting, but I think something's wrong with my camera."
    rm "All my photos are just a black screen! I'm not sure what to do."
    p concerned "Aw man!"
    p suspicious "You sure you don't have your lens cap on the lens?"
    rm "I hope not! Ha! That would be too easy to fix! I'm sure I'll figure it out eventually though."
    jump museum_food

# label .corndog:
#     scene bg museum_food
#     show corndog
#     show posty happy
#     p "Ooooh corndog!"
#     p suspicious "I don't see why it has to take up this much space. Guess it seems tasty?"
#     p "It doesn't even look like it's held up on the wall... Weird."
#     p "Oh well, time to look elsewhere."
#     jump museum_food

label .eating: #233
    scene bg museum_food
    show eating
    # if food_switch == False:
    #     show posty suspicious
    #     p suspicious "Huh what is that doing there? Among all the food based pieces, it doesn't look that appetizing to look at someone eating."
    #     "The title of the painting is \"{i}Crisis of the Poplar Trees{/i}\". The rest of the text is too small to read at this distance." 
    #     p "The only thing true about the title is that guy is clearly having a crisis about something!"
    #     p "If I didn't know any better, I would've thought he was having some pizza psychosis..."
    #     label .eating_decide:
    #     menu:
    #         "Read more of the placard?"

    #         "Yes.":
    #             "You try to read more of the placard, but bonk your face on it by mistake!"
    #             #389 play a sound here! like a click!!!
    #             # and then a scene of the corndog painting disappearing, revealing the secret passageway.
    #             $ food_switch = True
    #             p confused "Well, that was weird. Wonder what that sound was!"
    #             jump museum_food
    #         "No.":
    #             p "_" # posty decides she is uninterested in reading more of the placard. she starts to walk away, but returns to the placard, still curious.
    #             jump .eating_decide
    # else:
    show posty suspicious
    p "Huh what is that doing there? Among all the food based pieces, it doesn't look that appetizing to look at someone eating."
    "The placard reads: \"{i}Crisis of the Poplar Trees{/i}\"."
    p "The only thing true about the title is that guy is clearly having a crisis about something!"
    p "If I didn't know any better, I would've thought he was having some pizza psychosis..."
    jump museum_food

