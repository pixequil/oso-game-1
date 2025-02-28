image bg mainstreet_top:
    "map-bgs/mainstreet_top.png"

image bg mainstreet:
    "dbgs/mainstreet_dialogue_bg.png"

image butterfly_package:
    "items/butterfly_package.png"
    zoom 0.5
    truecenter

image ladle_full:
    "items/ladle_full.png"
    xalign 0.5
    yalign 0.5
    zoom 0.6

image scraptrophy:
    "items/scraptrophy.png"
    xalign 0.5
    yalign 0.5
    zoom 5.0
    rotate 45


image scrapmetal:
    "items/scrapmetal.png"
    zoom 1.3

default party_leave = "\"Ah sorry, we can't leave this place; 95% of the town has a restraining order against me for my promotional activities.\""
default last.mainx = 0.0
default last.mainy = 0.0

screen mainstreet_nav():
    viewport:
        child_size (3000, 720) # without redundifying the size here, ren'py will not allow scrolling
        edgescroll (300, 2000) # (bounds, speed) these are good values for horizontal scrolling, but this may need to be reduced for rooms with vertical scrolling.
        arrowkeys True
        xinitial last.mainx
        yinitial last.mainy
        add "bg mainstreet_top"

        # textbutton "Show Hitboxes":
        #     action ToggleVariable("devmode",True,False)

        # arrows
        imagebutton: # park arrow
            xanchor 0.5 # these make it so the xpos ypos are the center of the arrow
            yanchor 0.5
            xpos 1406
            ypos 640
            idle "arrow dn"
        imagebutton: # park arrow posty
            xanchor 0.5 # these make it so the xpos ypos are the center of the arrow
            yanchor 0.5
            xpos 1406
            ypos 640
            idle "pnav dn i"
            hover "pnav dn"
            action If(party_bs,Notify(party_leave),Jump("park"))
        imagebutton: # alley arrow
            xanchor 0.5 # these make it so the xpos ypos are the center of the arrow
            yanchor 0.5
            xpos 1739
            ypos 80
            idle "arrow up"
        imagebutton: # alley arrow posty
            xanchor 0.5 # these make it so the xpos ypos are the center of the arrow
            yanchor 0.5
            xpos 1739
            ypos 80
            idle "pnav up i"
            hover "pnav up"
            action If(party_bs,Notify(party_leave),MouseMove(640,480)),If(party_bs,Notify(party_leave),Jump("alley"))
        imagebutton: # dome arrow
            xanchor 0.5 # these make it so the xpos ypos are the center of the arrow
            yanchor 0.5
            xpos 2920
            ypos 320
            idle "arrow rt"
        imagebutton: # dome arrow posty
            xanchor 0.5 # these make it so the xpos ypos are the center of the arrow
            yanchor 0.5
            xpos 2920
            ypos 350
            idle "pnav rt i"
            hover "pnav rt"
            action If(party_bs,Notify(party_leave),Jump("dome"))

        # doors
        imagebutton: # museum door
            xanchor 0.5 # these make it so the xpos ypos are the center
            yanchor 0.5
            xpos 1320
            ypos 198
            idle "pnav up i"
            hover "pnav up"
            action If(party_bs,Notify(party_leave),Jump("mainstreet.go_museum"))
        imagebutton: # music door
            xanchor 0.5 # these make it so the xpos ypos are the center
            yanchor 0.5
            xpos 932
            ypos 203
            idle "pnav up i"
            hover "pnav up"
            action If(party_bs,Notify(party_leave),MouseMove(681, 612)),If(party_bs,Notify(party_leave),Jump("musicstore"))

        # people
        showif (party_bs == False) and (quest.bs == False): # bs alone
            imagebutton:
                xanchor 0.5 # these make it so the xpos ypos are the center
                yanchor 0.5
                xpos 2456
                ypos 300
                idle "nav_bs"
                hover "nav_bs p"
                action Jump("mainstreet.brandsoda")
        imagebutton: # yd
            xpos 1021
            ypos 139
            idle "nav_yd"
            hover "nav_yd p"
            action Jump("mainstreet.yd")
        imagebutton: # toasty
            xpos 535
            ypos 170
            idle "nav_t"
            hover "nav_t p"
            action Jump("mainstreet.toasty")
        imagebutton: # btnet
            xpos 480
            ypos 430
            idle "nav_bt"
            hover "nav_bt p"
            action Jump("mainstreet.btnet")
        imagebutton: # dolly
            xpos 2500
            ypos 30
            idle "nav_dolly"
            hover "nav_dolly p"
            action Jump("dolly")
        imagebutton: # miso
            xpos 1410
            ypos 119
            idle "nav_miso"
            hover "nav_miso p"
            action Jump("mainstreet.miso")
        imagebutton: # tooly
            xpos 1919
            ypos 177
            idle "nav_tooly"
            hover "nav_tooly p"
            action Jump("mainstreet.tooly")
        imagebutton: # tb
            xpos 130
            ypos 110
            idle "nav_tb"
            hover "nav_tb p"
            action Jump("mainstreet.tb")
        showif (item.cash_main == False):
            imagebutton: #main cash
                xpos 132
                ypos 480
                idle "nav_maincash"
                hover "nav_maincash p"
                action Jump("mainstreet.cash")

image nav_maincash = Composite(
    (150,150),
    (0,0), "hitbox",
    (50,50), "cash_loot_nav",
)
image nav_maincash p = Composite(
    (150,150),
    (0,0), "nav_maincash",
    (80,0), "pnav lt"
)

image nav_tb = Composite(
    (200,280),
    (0,0), "hitbox",
    (45,20), "minisprites/ticketbooth.png"
)
image nav_tb p = Composite(
    (200,280),
    (0,0), "nav_tb",
    (45,20), "pnav up"
)

image nav_tooly = Composite(
    (240,280),
    (0,0), "hitbox",
    (45,00), "minisprites/Tooly_OSO.png"
)
image nav_tooly p = Composite(
    (240,280),
    (0,0), "nav_tooly",
    (45,0), "pnav up"
)

image nav_miso = Composite(
    (260,210),
    (0,0), "hitbox",
    (40,60), "nav_miso base"
)
image nav_miso base:
    "minisprites/miso_soup_big_minisprite.png"
    xanchor 0.0
    yanchor 0.0
    zoom 0.3
image nav_miso p = Composite(
    (260,210),
    (0,0), "nav_miso",
    (75,40), "pnav lt"
)

image nav_dolly = Composite(
    (240,280),
    (0,0), "hitbox",
    (55,00), "minisprites/dolly.png"
)
image nav_dolly p = Composite(
    (240,280),
    (0,0), "nav_dolly",
    (45,0), "pnav up"
)

image nav_bt = Composite(
    (240,200),
    (0,0), "hitbox",
    (130,30), "minisprites/ButterflyNet_overworld.png"
)
image nav_bt p = Composite(
    (240,200),
    (0,0), "nav_bt",
    (15,45), "pnav rt"
)

image nav_t = Composite(
    (220,160),
    (0,0), "hitbox",
    (100,20), "minisprites/toasty.png"
)
image nav_t p = Composite(
    (220,160),
    (0,0), "nav_t",
    (0,0), "pnav rt"
)

image nav_yd = ConditionSwitch(
    "quest.bs == False","nav_yd lonely",
    "quest.bs == True","nav_yd friend"
)
image nav_yd p = Composite(
    (200,200),
    (0,0), "nav_yd",
    (30,0), "pnav up"
)
image nav_yd lonely = Composite(
    (200,200),
    (0,0), "hitbox",
    (0,0), "nav_yd base"
)
image nav_yd friend = Composite(
    (200,200),
    (0,0), "nav_yd lonely",
    (100,15), "nav_bs base"
)
image nav_yd base:
    "minisprites/yellowdiamond0001.png"
    xzoom -1.0

image nav_bs = Composite(
    (200,200),
    (0,0), "hitbox",
    (90,40), "nav_bs base"
)
image nav_bs base:
    "minisprites/Brand_Soda.png"
    xanchor 0.0
    yanchor 0.0
    zoom 0.75
image nav_bs p = Composite(
    (200,200),
    (0,0), "nav_bs",
    (-20,20), "pnav rt"
)




label firstscene:

    scene black
    stop music fadeout 1.0
    p "..."
    p "And this is going to..."
    
    show bg mainstreet
    play music "sound/music/REZURRECTA - ASTRUM_DEUS_P1.ogg"
    $ renpy.transition(dissolve, layer="master") #prevents interruption of the text window
    show posty neutral
    show btnet 

    extend " {b}{color=#c0d4e7}Crayon Box{/color}{/b}, at {i}1189 Brick Ave{/i}, right?"
    btnet "That's right!"
    p quiet "Okay, that's..."
    show posty astonished before
    extend " ..!"
    p astonished anim "THAT'S THE OSO DOME!!!"
    btnet "Yeah, it's my biggest job yet!"
    p -anim "And you want ME to deliver it??"
    btnet "Of course! I can always trust you for a swift and intact delivery, Posty."
    p happy "I'll take care of it right away! Consider it express with no extra charge!"

    show butterfly_package
    "Received the {b}Butterfly Package{/b}!{p}There is something fluttering inside..."
    $ item.butterfly_package = True
    hide butterfly_package

    btnet "Best of luck!"
    p "Thanks! Not that I'll need it, since it's just a short walk east of here."
    btnet "I'll leave you to it then."
    hide btnet with moveoutright
    p quiet "..."
    p astonished "Wow..! I get to deliver to the OSO Dome!"
    p "I bet {b}{color=#c0d4e7}Crayon Box{/color}{/b} is gonna use this in a challenge or something!"

    show toasty turned2
    $ renpy.transition(moveinbottom, layer="master") #prevents interruption of the text window
    p "I can't believe I get to be involved in Open Source Objects!!!"
    t "La la la, just minding my own business..." 
    t annoyed "Oh. {i}You're{/i} here. Didn't see ya."
    p neutral "Hi Toasty."
    t smug "Guess you got another job, huh."
    p "You were listening?"
    t smug2 "For that stoopid show, what was it?{w}\nOpen Source{w=0.4} Items{w=0.4} or whatever."
    t smug5 "Well, I don't even care!"
    p "K."
    t pointandlaugh "I bet you'll trip and fall on your way there!"
    p "I have to go deliver this now. See you later, Toasty."
    t laugh "Hah, well, don't come crying to me if you need help with anything!"

    hide toasty with moveoutright

    p "Welp. Better get going!"

label mainstreet:
    $ renpy.choice_for_skipping()
    $ last.alleyy = 1.0
    play music "sound/music/REZURRECTA - ASTRUM_DEUS_P1.ogg" if_changed
    call screen mainstreet_nav

label .go_museum:
    $ last.mainx = 0.4
    jump museum_entrance

# label .mainstreet_fallback:

#     scene bg mainstreet_top with fade
#     show posty neutral

#     p "__" # TODO: #9 replace this choice tree with an imagemap that scrolls

#     menu:
#         "Talk to someone.":
#             jump .talk
#         "Go somewhere.":
#             if party_bs:
#                 show bs follow behind posty
#                 bs "_" #TODO: #11 thing for Brand Soda to say to prevent you from leaving main street
#                 jump mainstreet
#             else:
#                 jump .go
# label .talk:

#     menu:
#         "B.T. Net":
#             jump .btnet 
#         "Dolly":
#             jump dolly # in money.rpy
#         "Miso Soup":
#             jump .miso
#         "Brand Soda" if (party_bs == False) and (quest.bs == False):
#             jump .brandsoda
#         "Toasty":
#             call toasty_hints
#             jump mainstreet
#         "Tooly":
#             jump .tooly 
#         "Yellow Diamond" if quest.bs == False:
#             jump .yd
#         "Yellow Diamond & Brand Soda" if quest.bs:
#             jump .yd
#         "Ticket Booth":
#             jump .tb       
# label .go:

#     menu:
#         "Music Store":
#             jump musicstore 
#         "Art Museum":
#             jump museum_entrance 
#         "Shady Back Alley":
#             jump alley 
#         "Park":
#             jump park 
#         "The Dome":
#             jump dome

label .toasty:
    $ last.mainx = 0.0
    call toasty_hints
    jump mainstreet

label .cash:
    $ last.mainx = 0.0
    scene bg mainstreet
    show posty happy
    show cash_loot at truecenter
    p "Oh look, there's money!"
    if saw.dolly:
        p "Better grab it!"
    else:
        p "Wonder what it's doing here! Oh well, I'll just take it."
    hide cash_loot
    $ money += 1
    $ item.cash_main = True
    call money_get
    if party_bs:
        show bs follow behind posty with moveinleft
        bs "Oh hey, what did you find?"
        p "Don't worry about it!"
        bs "Uhh... okay!"
    jump mainstreet

label .tb:
    $ last.mainx = 0.0
    scene bg mainstreet
    if party_bs:
        show posty neutral
        show tb shy
        show bs follow behind posty with moveinleft 
        bs "Yooooooo, what up!"
        tb shy "Ummmmm...hi..."
        tb shy "I'm sorry, I don't do well in mobs."
        bs "Well thankfully for you, I do! I can market the whole theater for you and bring thousands of people over here to watch your movies!"
        tb shy "Thousands of people? Gathering in front of me? All at once?"
        tb shy "Um, I'm not interested, sorry!"
        bs "Oh, well screw you then."
        jump mainstreet
    if saw.tb:
        show posty neutral
        show tb neutral
        p "Hi again!"
        tb "Oh, hello!"
        tb "Heh heh..."
        tb shy "Sorry, I'm a little shy..."
        p "Isn't working in front of a movie theater a strange career choice for you then?"
        tb "I don't know...it pays well."
        tb neutral "Though what I really want to do is work on Broadway."
        p happy "Good luck with that!"
        jump mainstreet
    else:
        show posty neutral
        show tb shy
        p "Hi!"
        tb "H-hi!"
        tb "What movie are y-you interested in seeing?"
        p "Oh, no movies for now. I'm delivering something important for work."
        tb "Ok! Come again!"
        $ saw.tb = True
        jump mainstreet


label .brandsoda:

    $ last.mainx = 1.0
    scene bg mainstreet
    show posty neutral
    show bs behind posty
    if that_dork:
        p quiet "{i}It's that dork Dolly was talking about... act natural.{/i}"
        p astonished quiet "{i}WAIT, THIS IS MY FRIEND BRAND SODA!{/i}"
    bs "Yo, Posty! How\'s my favorite mailbox?"
    show posty astonished -quiet
    p "Oh, hi Brand Soda. I'm busy with delivering an important package right now."
    bs "Dope. Who\'s it for?"
    p happy "The OSO Dome."
    bs "WOAH! That...is...big! Something like that is bound to draw a lot of attention…"
    bs "Do you have any idea how overwhelming that could be?"
    p concerned "It kinda slipped past me..."
    p "Hey, speaking of attention, how's that gig at the comedy club?"
    bs "They banned me after one act! Can you believe it? Called me a hack fraud."
    bs "ME! THE NEXT BIG THING!"
    p "What did you do to get banned?"
    bs "I called the audience freaks and geeks for about ten minutes."
    bs "The whole street banned me actually."
    bs "Even if I took one step on the pavement there, they'd call the police on me for trespassing."
    bs "And other streets caught wind and now I can't promote myself anywhere else other than here."
    p concerned "Dang...that sucks dude."
    bs "If I had a marketing agent or something, I could get enough attention on me to get back into those venues..."
    bs "Hey, I have an idea! What if you took me around town and we can find someone to do some marketing for me?"
    p "Oh, I don't know...I've got a lot on my plate right n-"

    show bs follow with move:
        xalign 0.35
    
    bs "Nope, it's already decided. I'm here now!"

    $ party_bs = True
    "{b}{color=#df7dff}Brand Soda{/color}{/b} joined your party!"

    p neutral "Alright, I guess."
    bs "Sweet! Let's get us some marketing!"

    jump mainstreet

label .yd_quals:
    yd "Number 1: They should have a lot of charisma."
    yd "Not too dry or trying too hard to be cool. Just enough to make me laugh!"
    yd "Number B: They should have a lot of bouis-ness experience. Flying can be pretty technical for people to understand!"
    yd "And Number C: They should like nachos."
    yd "I really like nachos."
    yd "But I haven't found anyone yet!"
    return

label .yd:
    $ last.mainx = 0.25
    scene bg mainstreet
    show posty neutral
    show yd
    if party_bs:
        jump .yd_bs_money
    elif quest.bs:
        jump .yd_bs_happy
    elif saw.yd:
        yd "Hiiiiiiii!"
        p neutral "Hi again. Hey, what are your qualifications for a best friend to promote your flying lessons again?"
        yd "Huh? Oh yeah! Uhhhhhhh..."
        call .yd_quals
        p neutral "Don't worry, I'm still looking for someone! You'll be the first to know!"
        jump mainstreet    
    else:
        yd "Hiiiiiiii!"
        p suspicious "Uhh...hi."
        yd "Can we be best friends?"
        p neutral "I don't know, kid. I'm too busy."
        yd "That's OK!"
        p "Where are your parents?"
        yd "Is that a type of vegetable?"
        p "Never mind."
        p "What are you doing out by yourself?"
        yd "I'm an entrée-prenur!"
        p suspicious "For what?"
        yd "Flying lessons for people who don't know how to fly! It'll be the best thing ever!"
        yd "But I need a best fwiend to help me out with the buies-ness!"
        p "You mean business?"
        yd "No, buies-ness! It's French!"
        yd "But I won't just take anybody to be my best friend! I have very special spec-sip-uh-kay-shuns!"
        call .yd_quals
        p neutral "Well, if I find anyone to help your business take off, I'll let you know."
        yd "Hehehe, flying pun! Thanks, mail girl!"
        $ saw.yd = True

        jump mainstreet

label .yd_bs_money:
    show bs follow behind posty with moveinleft
    yd "Hi Maily!"
    p "Posty."
    yd "Hi Posty!"
    p happy "Say, I have this friend, Brand Soda, you might be interested in!"
    bs "Hello strange child! Are you in need of a comedian, spokesperson, or hypeman?"
    yd "No!"
    bs "Oh ok then."
    yd "I just need a best friend to promote my flying lessons start-up! But I haven't found anyone yet! I'm sad!"
    bs "PR work, huh?"
    p happy "It's your angle, man! Go for it!"
    bs "Say, um, diamondy boy, what would this \"best friend\" need to do?"
    yd "I need them to market my business oppurtunity! They would be the face of the company while I do all the important stuff!"
    yd "They need to be very charismatic! Are you charismatic?"
    bs "I have tons of charisma coming out of my butt!"
    yd "HAHAHA! You're funny!"
    yd "Are you smart at buahs-ness?"
    bs "Oh totally! I have experience all over the city!"
    bs "In fact, the city thinks I'm too forward thinking."
    bs "So now, I'm stuck on this street without a single penny or crumb to my name..."
    yd "Oh no!"
    bs "Yes, it's quite tragic..."
    bs "But you know, now I have all the time in the world and am completely available except on Tuesdays!"
    bs "Say, is it possible that this gig could be popular?"
    yd "Exactly! I am very confident it could go national!"
    bs "National marketing...wow..."
    p "Oh yeah, trust me! This yellow guy's a real visionary!"
    bs "Oh sign me up! I am totally in on this!"
    yd "Yay!"
    yd "Oh, one more thing! Very important!"
    yd "Do you like nachos?"
    bs "Pffftt...I'm a nachoholic!"
    bs "I eat them all the time!"
    yd "Wowzers! Me too!"
    yd "Is this the beginning of a beautiful friendship?"
    bs "Oh, more than that! We became best buds!"
    yd "YAYYYYYY!"

    show bs with move:
        xalign 0.65
    $ party_bs = False
    "{b}{color=#df7dff}Brand Soda{/color}{/b} left your party!"

    bs "Posty! Thanks to you, I'm employed! I can't thank you enough!"
    bs "Just to show you I'm not the heartless celebrity that everyone thinks I am, here's a bonus for helping me find a marketing agent and my way back into the spotlight!"

    $ money += 1
    $ quest.bs = True
    show cash_brandsoda at truecenter
    $ renpy.transition(irisout, layer="master") #prevents interruption of the text window
    "{b}{color=#df7dff}Brand Soda{/color}{/b} gave you {b}some money{/b}!"
    hide cash_brandsoda
    call money_get

    p happy "Wow, thanks Brand Soda!"
    bs "I'll never forget you!"
    bs "So kid, what is this \"business oppurtunity\" you were starting again?"
    jump mainstreet

label .yd_bs_happy:
    show posty happy
    show bs behind yd:
        xalign 0.65
        yalign 1.0
    yd "Hi Posty!"
    bs "Sup Posty, me and Yellow Diamond here are just working out the kinks of our business."
    p happy "Well, I'll leave you to it!"
    bs "So Yellow Diamond, how do we teach people with legs to fly?"
    bs "Doesn't that sound impossible?"
    yd "It's easy! You have to believe in it really hard!"
    bs "I can't help but feel I've been duped..."
    jump mainstreet

label .misoproblems:
    miso "I just got banned from the musuem!"
    miso "The security guard in there said I spilled my soup on one of the security gates and almost ruined one of the paintings!"
    miso "But I didn't do it! I always bring plastic wrap to protect the soup from spilling! Honest!"
    miso "I tried telling him I didn't do it, but he wrote me a notice of reprimand anyway and kicked me out! That guy is so strict!"
    miso "And it gets worse!"
    miso "My parents are really big art connoisseurs! If they find out that I could've destroyed something priceless, they might kick me out of their fortune!"
    p "I'm sorry, there's nothing I can really do to help right now."
    return

label .miso:
    $ last.mainx = 0.5
    scene bg mainstreet
    show miso

    if party_bs:
        show posty happy
        show bs follow behind posty with moveinleft
        p "This guy seems like they'd be willing to invest in you."
        bs "Ehhhhh...I don't know..."
        bs "I've heard of this guy's parents. They're elitist art snobs."
        bs "If I wanna be the next big thing and appeal to everyone, I can't just go to these big shots first."
        bs "What if they don't like me and tell their rich friends how much I suck?"
        bs "Let's pick someone less risky around here."
        p neutral "OK..."
        miso "What are you guys talking about?"
        p confused " AHHHH! Nothing!"
        jump mainstreet
    
    elif (item.ladle_empty == False) and (miso_took == False):
        if saw.miso:
            show posty concerned
            p "Still worried about, uhh, all that?"
            miso "Yes! Didn't you pay attention?"
            call .misoproblems
            miso "Don't remind me..."
        else:
            show posty neutral
            $ saw.miso = True
            p "Hello!"
            miso " {i}Ohhh, my family is gonna kill me... {/i}"
            p concerned "Is there a problem?"
            miso "Huh? Oh hi, didn't see you there!"
            call .misoproblems
            p "If I can find a way to make it up, I'll let you know."
            miso "Thanks for trying, I guess."
        jump mainstreet

    elif item.ladle_empty and (miso_took == False):
        show posty sad
        p sad "I'm so sorry for this." 
        miso "What are you talking ab-"
        $ item.ladle_empty = False
        $ item.ladle_full = True
        $ miso_took = True
        show ladle_full
        "You filled the {b}ladle{/b} with {b}miso soup{/b}!"
        "Filled with miso soup, miserable to clean up properly. Perfect sabotage."
        miso "My soup!"
        jump mainstreet

    elif miso_took and (quest.painting_blue == False):
        show posty sad
        p "Again, I'm so sorry for taking some of your soup."
        miso "What did you even do that for?"
        p concerned "I need it for something. It's kind of hard to explain right now."
        p "I'll make it up to you when I finish what I have to do!"
        miso "I sure hope so! This has been the weirdest day ever!"
        jump mainstreet

    elif miso_took and quest.painting_blue:
        show posty sad
        p "Hey, Miso Soup. I'm back."
        miso "Oh no, it's you again! What more could go wrong today?"
        p  "I know I messed up before, taking your soup and all."
        p "But I want to make it up to you somehow."
        miso "Make it up? How can you possibly do that?"
        p "I have just the thing! It's something really special to me."
        ""
        p "My gratitude."
        miso "What. How is that going to-"
        p happy "Thanks for understanding! And thanks again for some of your soup!"
        hide posty with moveoutleft
        miso "Well, that was odd."
        jump mainstreet

    else:
        show posty neutral
        p "Players should not see this text."

label .btnet:
    $ last.mainx = 0.0
    scene bg mainstreet
    show btnet
        
    if party_bs:
        show posty happy
        show bs follow behind posty with moveinleft
        bs "Hello kind sir! I'm ready to sign any brand deals, contracts, or ambassadorships you put in front of me at a moment's notice!"
        btnet "Pardon?"
        p happy "We're looking for someone to market them."
        btnet "Aside from maybe a job at the museum, I'm afraid there's nothing I can do."
        p happy "Maybe you could give an object-on-the-street interview about them?"
        bs "Yeah, old man, give your honest thoughts!"
        btnet "Ummmmmm..."
        btnet "They make bad first impressions, expect rewards too quickly, have delusions of grandeur..."
        btnet "Smell flat..."
        bs "We're leaving."
        p happy "Talk to you later, boss!"
        jump mainstreet

    elif item.butterfly_package:
        show posty happy
        p happy "Hello again!"
        btnet "How's your progress on the delivery?"
        p happy "I ran into a few slip-ups, but I think I can handle it!"
        btnet "If it ever gets too difficult, I can always pass it on to someone else, like your friend Toasty or-"
        p astonished "No, it's ok! I've got it!"
        p happy "I'll let you know when it's delivered!"
        btnet "Ok, good luck Posty!"
        jump mainstreet

    else:
        show posty happy
        p happy "I delivered the package! Crayon Box was impressed with the butterflies!"
        btnet "Excellent work, Posty! I knew you could do it!"
        p happy "Do you need me to deliver any other packages today?"
        btnet "Nah. I don't want to overwork you, especially after this important order for OSO!"
        btnet "Go take a nap! You've earned it!"
        p happy "Thanks B.T.! Talk to you later!"
        jump mainstreet

label .tooly:
    $ last.mainx = 0.83
    scene bg mainstreet
    show tooly

    if party_bs:
        show posty neutral
        show bs follow behind posty with moveinleft
        bs "Excuse me miss! Would you like to-"
        tooly "I don't deal with these newfangled social experiments! Beat it!"
        jump mainstreet

    if trophy_crafted:
        jump .tooly3
    elif saw.tooly:
        jump .tooly2
    else:
        jump .tooly1

label .tooly1:
    show posty happy
    tooly "Howdy stranger! The name's Tooly! Welcome to my shop!"
    p happy "Hello! I never noticed this place before!" 
    tooly "I just opened it!" 
    p happy "Neat! What do you do here?"
    tooly "Oh, I store nukes!"
    show posty concerned
    tooly "We have weapons of mass destruction of all shapes and sizes."
    tooly "We actually have a few deactiviated ones. Don't touch them, they're sensitive."
    p concerned "Uhhhhhhh..." 
    tooly "Hahaha! I'm just messing with you!" 
    tooly "This is a metalworking shop. Been working professionally for the past twenty years!" 
    tooly "I've got plenty of experience so if you wanted anything special crafted, I can do it pretty easily!"
    p happy "Cool!"
    tooly "Unfortunately, I can't sell you any raw materials today, since I'm fresh out."
    if money == 0:
        p concerned "That's okay, I'm kinda broke."
    p concerned "What if I brought you raw materials myself?" 
    tooly "Hmmmm..."
    tooly "You seem like a nice enough girl, so tell you what!"
    tooly "Just for being my first customer of the day, if you personally bring me the raw materials to craft anything, I'll do your first job completely free!"
    p happy "Awesome!"
    $ saw.tooly = True
    if item.scrapmetal:
        jump .tooly_scrap
    else:
        p "See you later, Tooly!"
        tooly "Later, gator."
        jump mainstreet

label .tooly2:
    show posty happy
    p "Hey Tooly!"
    tooly "Hey customer!"
    p "Can you remind me of our deal again?"
    tooly "Wasn't expecting you to forget so easily, but..."
    tooly "Just for being my first customer of the day, if you personally bring me the raw materials to craft anything, I'll do your first job completely free!"
    p "Awesome!"
    if item.scrapmetal:
        jump .tooly_scrap
    else:
        p "See you later, Tooly!"
        tooly "Later, gator."
        jump mainstreet

label .tooly_scrap: #
    show posty happy
    show scrapmetal at truecenter
    p "Will this work as raw materials?"
    tooly "Looks great! Hand it over!"
    "You handed over the {b}scrap metal{/b}!"
    $ item.scrapmetal = False
    hide scrapmetal
    p "Can you craft this into a trophy please?"
    tooly "Sounds good! I know exactly what to how it! Can I get the name for this project?"
    p "Posty."
    tooly "Alright, Posty! Give me one minute!"
    $ trophy_crafted = True
    show scraptrophy
    "Tooly crafted a {b}scrap trophy{/b}!"
    $ item.scrap_trophy = True
    hide scraptrophy
    p "Wow, it looks like a real trophy!"
    tooly "Yeah, the craftsmanship is good...but I don't know."
    tooly "It's missing something. It needs the perfect finishing touch."
    if item.spraypaint:
        call trophy
        tooly "Now that's a gold trophy!"
        tooly "You might be able to trick somebody into thinking this is real gold!"
        jump mainstreet
    else:
        p "This looks perfect! Thank you so much!"
        tooly "Hehe! Any time Posty."
        tooly "Catch you later!"
        jump mainstreet

label .tooly3:
    show posty happy
    p "Hey Tooly! How's business?"
    tooly "Deader than disco."
    tooly "Hey, what are you using that epic trophy for anyway?"
    p neutral "You're better off not knowing."
    tooly "Hmmm... sounds illegal."
    p astonished "..!"
    tooly "I'm going to have to report this as a concerned citizen."
    tooly "PFFFT! Nah!"
    p neutral "..."
    tooly "Catch you later, Posty!"
    jump mainstreet

