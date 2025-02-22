image bg dome_top:
    "map-bgs/dome_top.png"

image bg dome:
    "dbgs/Dome_dialogue_bg.png"

default domedoor_text = "Seems like the door is locked now."

screen dome_nav():
    viewport:
        child_size (1280,720)
        add "bg dome_top"

        # textbutton "Show Hitboxes":
        #     action ToggleVariable("devmode",True,False)

        # arrow
        imagebutton: # main street arrow
            xanchor 0.5 
            yanchor 0.5
            xpos 75
            ypos 530
            idle "arrow lt"
        imagebutton: # main street arrow posty
            xanchor 0.5 
            yanchor 0.5
            xpos 75
            ypos 530-20
            idle "pnav lt i"
            hover "pnav lt"
            action MouseMove(960,360),Jump("mainstreet") # mouse move is to prevent main street from automatically scrolliong. feels weird maybe?
        
        # people
        showif (win_flag == False) and quest.retainer:
            imagebutton: # cb
                pos (860, 378)
                idle "nav_cb"
                hover "nav_cb p"
                action Jump("dome.cb")
        showif (quest.retainer == False):
            imagebutton: # cb blocked
                pos (860, 378)
                idle "nav_cb"
        showif (quest.retainer == False):
            imagebutton: # retainer
                pos (750, 400)
                idle "nav_ret"
                hover "nav_ret p"
                action Jump("dome.retainer")
        imagebutton: # sweets
            pos (275, 272)
            idle "nav_sweets"
            hover "nav_sweets p"
            action Jump("dome.sweets")
        showif (win_flag == True):
            imagebutton: # trying to enter the dome now that cb is gone
                pos (860, 378)
                idle "nav_domedoor"
                hover "nav_domedoor p"
                action Notify(domedoor_text)
                
image nav_sweets = Composite(
    (240,280),
    (0,0), "hitbox",
    (150,40), "minisprites/bonbon.png",
    (30,30), "minisprites/sourgummy.png"
)
image nav_sweets p = Composite(
    (240,280),
    (0,0), "nav_sweets",
    (60,20), "pnav up"
)

image nav_ret = Composite(
    (220,160),
    (0,0), "hitbox",
    (100,20), "minisprites/retainersad.png"
)
image nav_ret p = Composite(
    (220,160),
    (0,0), "nav_ret",
    (0,30), "pnav rt"
)

image nav_cb = Composite(
    (240,280),
    (0,0), "hitbox",
    (70,0), "minisprites/crayonbox.png"
)
image nav_cb p = Composite(
    (240,280),
    (0,0), "nav_cb",
    (40,20), "pnav up"
)
image nav_domedoor = Composite(
    (240,280),
    (0,0), "hitbox",
)
image nav_domedoor p = Composite(
    (240,280),
    (0,0), "nav_domedoor",
    (40,20), "pnav rt"
)



label dome:
    $ renpy.choice_for_skipping()
    $ last.mainx = 1.0
    if win_flag:
        if renpy.music.get_playing() != "sound/music/Nyakiye - 111.ogg":
            play music "sound/music/Nyakiye - 111 intro.ogg" if_changed
            queue music "sound/music/Nyakiye - 111.ogg"
    else:
        play music "sound/music/plebkingdom - Break.ogg" if_changed
    call screen dome_nav

# label dome_fallback:
#     $ last.mainx = 1.0
#     scene bg dome_top
#     show posty neutral

#     p "_" # TODO: #20 dome imagemap

#     menu:
#         "Talk to Crayon Box" if item.butterfly_package:
#             jump .cb
#         "Talk to Retainer" if (quest.retainer == False):
#             jump .retainer
#         "Talk to Bon-Bon & Sour Gummy":
#             jump .sweets
#         "Leave.":
#             jump mainstreet

label .cb:
    if quest.retainer:
        jump .cb_give
    else:
        "PLAYER SHOULD NEVER SEE THIS TEXT. REPORT TO SATOMI IMMEDIATELY."
        $ saw.retainerblock = True
        jump dome

label .cb_give:
    scene bg dome
    show posty happy
    show cb
    show butterfly_package
    p "Phew! Here you go ma'am!"
    cb "Thank you so much!"
    play music "sound/music/Nyakiye - 111 intro.ogg" fadeout 0.5
    queue music "sound/music/Nyakiye - 111.ogg"
    "You handed over the {b}Butterfly Package{/b}!"
    $ item.butterfly_package = False
    $ win_flag = True
    hide butterfly_package
    cb "Just in time! I'll need to go now."
    hide cb with moveoutright
    show posty astonished before
    cb "Gather 'round, contestants! The fourth challenge is about to start!"
    cb "I had the contents of today's challenge"
    show posty astonished anim
    cb "I had the contents of today's challenge{fast} {i}specially{/i}{w=0.3} delivered!"
    p astonished "Oh my god!! Crayon Box is talking about {i}ME{/i}?!? This is a dream come true!!"
    "{i}You successfully finished your work for today!{/i}"
    p happy "Gosh!! I'm so tired from that! Perhaps some new scenery would help..."
    jump dome

label .retainer:
    if item.makeshift_trophy:
        jump .retainer_give 
    elif saw.retainerblock:
        scene bg dome
        show posty concerned
        show retainer crying with hpunch
        retainer "AHHHHHHHHH!"
        p "Never mind."
        jump dome
    else:
        scene bg dome
        show posty neutral
        show retainer sad
        $ saw.retainerblock = True
        p "What's wrong?"
        retainer "Sigh, things haven't been going well."
        retainer "Got eliminated from this show after only a couple of challenges, which was way earlier than expected."
        p "Ah shame, it happens sometimes."
        show retainer crying with hpunch
        retainer "It was supposed to be my breakthrough moment! When I started making friends and doing more in my life!"
        retainer "Instead I ended up here, without accolades to show for it!"
        retainer "I don't understand why I did this in the first place, no one cared I was gone!"
        p concerned quiet "..."
        p -quiet "May I get past you?"
        retainer "AHHHHHHHHH!"
        p "Never mind."
        jump dome

label .retainer_give:
    scene bg dome
    show posty astonished
    show retainer sad behind posty
    p "Hey...Retainer, is it?" 
    retainer "{i}sniff sniff{/i} Yeah, that's me."
    p happy "I have a gift for you!"
    retainer "Oh! Really?"
    p neutral "Lemme just..."
    show makeshift_trophy
    "You handed over the {b}makeshift trophy{/b} to Retainer!"
    p happy "Tadaaaaa!"
    $ item.makeshift_trophy = False
    $ quest.retainer = True
    retainer "Oh my jawline! That's for me?!"
    p "Yep! Think of it as a, uhh...a participation trophy!"
    p quiet "{i}...please tell me he'll bite the bait.{/i}"
    retainer "I..."
    show retainer happy with hpunch
    retainer "I love it! {w}I knew Crayon Box appreciated my presence! Oh, I gotta put this on my shelf!"
    hide makeshift_trophy
    p -quiet "I'm sure she was thinking of you!"
    p quiet "{i}One man's trash...{/i}"
    retainer "And she even put a label on it!"
    p astonished -quiet "E-Eh? She did?"
    retainer "Right here! She said I'm...\"top-grade steel\"! Crayon Box must think I showed off my greatest strengths."
    p concerned "Ah, hehe...I'm sure she did!"
    retainer "There's something else here, too..."
    retainer sad "...\"100\% recyclable\"?"
    p "Uhhhhh..."
    p happy "...i-it probably means she thinks you're so versatile that you could be a contestant in just about any other show without changing anything at all!"
    p quiet "{i}...woof, that was a horrible bluff. He wouldn't believe that in a million years!{/i}"
    retainer quiet "..."
    retainer happy -quiet "...hey, you're right! I bet I could be a knockout. I'm perfect already!"
    retainer "That settles it! Next time I see Crayon Box, I'll give her so much thanks for this trophy that she won't even know what hit her!"
    p "{i}Uh oh, if he realizes Crayon Box is right over there, this could get bad...{/i}"
    p -quiet "Hold on! Don't you wanna bring this home with you first? Make sure it doesn't get damaged and all?"
    retainer "Oh! Of course! This is my proudest achievement yet! I'm not gonna let anything happen to it!"
    p quiet "{i}I'm sure with the passage of time, this situation's gonna seem funnier than it is pathetic and kinda sad...{/i}"
    retainer "I gotta get this back home! Thanks a heap, Posty. If you see Crayon Box, tell her I said thanks for the trophy!"
    p -quiet "Later, Retainer!"
    hide retainer with moveoutleft
    "{b}{color=#fc809d}Retainer{/color}{/b} got out of the way!"
    if saw.retainerblock:
        p "Whew! I thought he'd never leave!"
    else:
        p concerned "Pretty lucky of me to have that fake trophy, if I do say so myself!"
    jump dome

label .sweets:
    scene bg dome
    show bonbon
    show sgummy behind bonbon:
        xzoom -1.0
        xalign 0.7
    if quest.retainer:
        show posty neutral
        bonbon "That was so sweet of her! Don't you agree?"
        sgummy "No way, she was clearly trying to ward the poor guy away from the dome for her selfish plan to talk to the host."
        bonbon "But you have to admit! The retainer guy seemed genuinely happy! I hope he's back home safe and sound and away from… that."
        sgummy "...Bon Bon, we're not having another conversation about how much you-{nw}"
        bonbon "I have no idea why those poor people would sign up to be locked in that thing! And competing against each other too! That's barbaric!"
        sgummy "Yea, I guess I can, uh, agree, I don't trust those host guys at all, but I gotta give them some... {i}cough{/i}... credit, the dome is cool."
        bonbon "It just IRRITATES me. I can't even water my plants in peace without looking at that thing! Trapping them from real grass!"
        sgummy "How do you know, huh? It's definitely real grass, Bon Bon. I would know since I look at it daily. That doesn't look like plastic grass to me."
        bonbon "Well… it's still inhumane! I've seen how eliminated contestants walk out when they've been \"eliminated\". They clearly don't want to stay there for any longer!"
        bonbon "I-... I might be going on too much, I'm sorry, but that dome just needs to go!"
        sgummy "I have to admit another thing, the dome's structure is actually done very well. They definitely didn't mix their centimeters and millimeters, and the glass is durable." 
        sgummy "I have got to meet the crew who created this beautiful structure… not that I like what it's being used for."
        bonbon "It sure does look pretty... like a siren luring its victims!"
        sgummy "I just really find the structure... unique yet simple. Durable and big! It's all I ever want to be!"
        bonbon "So you still want to be the dome, huh?"
        sgummy "UH- I wouldn't word it like that, sounds wrong. You know what, yea, I do want to be a dome. A dome with such a strong and big structure."
        bonbon quiet "..."
        bonbon -quiet "If that's what my good friend wants! Then I can't help but support it!"
        sgummy "Really?"
        bonbon "Of course! I'll supply the dynamite!"
        sgummy "You can't build a dome with dynamite, silly."
        bonbon "Oh, who said I'd be building anything?"
        jump dome
    else:
        show posty neutral
        bonbon "What's the point of the dome? It sucks and needs to be destroyed."
        sgummy "How can you hate the dome. Look at how I can see my reflection, its round shape, and its durability. I wish that was me."
        bonbon "What!? Do you want to be a dome?"
        sgummy "Yes! Being a dome means I\'ll have everything I\'ve ever wanted!"
        bonbon "You don\'t make any sense. You can\'t become a dome."
        sgummy "Why not?"
        bonbon "If you did then that means I\'ll have to destroy you too!"
        sgummy "You wouldn\'t because nothing could hurt me!"
        bonbon "I can!"
        sgummy "Yeah right!"
        jump dome
