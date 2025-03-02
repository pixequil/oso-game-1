# todo: #32 blue exhibit conversation background

# #113
# todo: image museum_blue_p_rusty
# todo: image museum_blue_p_opened
# todo: image museum_blue_p_missing


image bg blue_red:
    "dbgs/blue_red.png"

image bg blue_talk:
    "dbgs/blue_rusty.png"
image bg blue_talk rusted:
    "dbgs/blue_rusted.png"
image bg blue_talk taken:
    "dbgs/blue_taken.png"

image bg museum_blue_top:
    "map-bgs/museum_blue_top_default.png"

image bg museum_blue_top stolen:
    "map-bgs/museum_blue_top_nopainting.png"

image redcash:
    "items/redcash.png"
    xalign 0.5
    yalign 0.5
    zoom 3.0

image painting_blue:
    "items/blue_exhibit_main_painting.png"
    truecenter
    zoom 0.5

image ladle_empty:
    "items/ladle_empty.png"
    xalign 0.5
    yalign 0.5
    zoom 0.6

image ladle_full:
    "items/ladle_full.png"
    xalign 0.4
    yalign 0.5
    zoom 0.6

image rusty_gate:
    "items/rusty_gate.png"
    xalign 0.75
    yalign 0.6
    zoom 1.25

image rusty_gate_broken:
    "items/rusty_gate_broken.png"
    xalign 0.75
    yalign 0.6
    zoom 1.25

screen blue_nav:
    viewport:
        child_size (1280,720)

        showif quest.painting_blue == False:
            add "museum_blue_top_default"
        showif quest.painting_blue:
            add "museum_blue_top_nopainting"

        imagebutton: 
            xanchor 0.5
            yanchor 0.5
            pos (1200, 580)
            idle "arrow rt black"
        imagebutton: 
            xanchor 0.5
            yanchor 0.5
            pos (1200, 550)
            idle "pnav rt i"
            hover "pnav rt"
            action Jump("museum_entrance")

        imagebutton: # redtile
            pos (645, 450)
            idle "nav_redtile"
            hover "nav_redtile p"
            action Jump("museum_blue.rt")
        
        imagebutton:
            pos (520,40)
            idle "nav_main"
            hover "nav_main p"
            action Jump("museum_blue.painting")

        showif saw.rcash == False:
            imagebutton:
                pos (200, 540)
                idle "nav_rcash"
                hover "nav_rcash p"
                action Jump("museum_blue.redcash")

image nav_rcash = Composite(
    (150,150),
    (0,0), "hitbox",
    (50,50), "rcash_tiny",
)
image rcash_tiny:
    "items/redcash.png"
image nav_rcash p = Composite(
    (280,280),
    (0,0), "nav_rcash",
    (80,0), "pnav lt"
)
image nav_main = Composite(
    (280,280),
    (0,0), "hitbox",
    (160,40), "bluetile_tiny",
)
image nav_main p = Composite(
    (280,280),
    (0,0), "nav_main",
    (80,0), "pnav up"
)
image bluetile_tiny = ConditionSwitch(
    "quest.painting_blue == True","bluetile_scared",
    "bt_distracted == True","nothing",
    "True","bluetile_giddy"
)
image bluetile_giddy:
    "minisprites/bluetile_giddy.png"
    zoom 0.03
image bluetile_angry:
    "minisprites/bluetile_angry.png"
    zoom 0.8
image bluetile_scared:
    "minisprites/bluetile_scared.png"
    # zoom 0.03

image nav_redtile = Composite(
    (280,280),
    (0,0), "hitbox",
    (160,40), "redtile_tiny",
    (40,40), "bluetile_tiny2"
)
image nav_redtile p = Composite(
    (280,280),
    (0,0), "nav_redtile",
    (100,0), "pnav up"
)
image redtile_tiny:
    "minisprites/redtile.png"
    zoom 0.13
image bluetile_tiny2 = ConditionSwitch(
    "bt_distracted == True","bluetile_angry",
    "True","nothing"
)

label museum_blue:
    play music "sound/music/TheSeanimator22 - Dinner at 7pm.ogg" if_changed
    # if saw.blue == False:
    #     jump .redcash
    # else:
    $ renpy.choice_for_skipping()
    $ renpy.save_persistent()
    call screen blue_nav

# label museum_blue:
#     if saw.blue == False:
#         jump .redcash
#     else:
#         scene bg museum_blue_top # TODO: #33 blue exhibit imagemap (needs illustration)
#         show posty neutral

#         p "_"

#         menu:
#             "Main Exhibit & Blue Tile" if (bt_distracted == False):
#                 jump .painting
#             "Red Tile" if (bt_distracted == False):
#                 jump .rt
#             "Main Exhibit" if bt_distracted:
#                 jump .painting
#             "Red Tile & Blue Tile" if bt_distracted:
#                 jump .rt
#             "Return to the entrance.":
#                 jump museum_entrance

label .redcash:
    scene bg blue_red
    show posty astonished
    show redcash
    p suspicious "Huh, what's this red thing doing here?" 
    p happy "Oh well. Yoink."
    $ saw.rcash = True
    $ item.red_cash = True
    "You got the {b}{color=#de474e}red cash{/color}{/b}!{p}It\'s money but it\'s red."
    p neutral "... This isn't real money."
    if saw.dolly:
        p "Dolly definitely won't take this."
        p suspicious "Who even {i}would{/i} take this?"
    else:
        p suspicious "Who walks around with fake money?"

    jump museum_blue
        
label .rt:
    scene bg blue_red
    show redtile

    if quest.painting_blue:
        show posty neutral
        redtile "How it'd go?"
        p happy "Perfect! I missed the painting and completely melted the fence."
        redtile "That sounds like you failed."
        p "Well actually, you know how Blue Tile is always obsessed with the blue exhibit?"
        redtile "Uh huh."
        p "And how he goes absolutely ballistic if you even touch them wrong?"
        redtile "Yeah, what about it?"
        p happy "I got one of them."
        $ renpy.transition(hpunch, layer="master")
        redtile "WHAT?!"
        p "I have one of the blue paintings."
        redtile "Y- you have one of them?! One of the things that gets Bluey in a twist?"
        p suspicious "Why did you think I paid you to argue with the guy? I ain't exactly invisible, so I needed a distraction."
        redtile "I thought you were going to splash the paintings a bit or flip them upside down, not straight up rob the place!"
        p happy "As Piquante once said: good artists copy, great artists steal!"
        redtile "He didn't mean {i}literally{/i} stealing anything! It was a metaphor for making your ideas your own-"
        p "Yeah yeah, \"the opposite of a fait accompli is to make.\" I got it!"
        redtile "You're a criminal, Posty! But so am I. I'm sure we can agree not to rat each other out?"
        p "Oh totally!"
        redtile "Great. Thanks again by the way!"
        redtile "Y'know, for helping me with my revenge."
        p "Enjoy the cash!"
        jump museum_blue

    if saw.redtile == False:
        show posty neutral
        $ saw.redtile = True
        redtile "What do you want from me? I was just about to make a remark about the incessant use of blue in this exhibit."
        p "Well-"
        redtile "Let me guess. You are confused about my very presence in this area."
        if saw.bluetile == True:
            p concerned "Yeah, but I assumed you were friends with Blue Tile and you went to check out the exhibit together."
        else:
            p concerned "Yeah, but I assumed you were friends with that guy over there and you went to check out the exhibit together."
        redtile "Uggh, not even close. Blue dragged me out here so he couldn't ramble on about this dumb, irritating, meaningless color to himself."
        redtile "As for the exhibit, if you knew anything about its long and complex history, you would know it represents the death of free artistic expression and pandering to the masses."
        p confused "What?"
        redtile "Let me tell you a story."
        redtile "Long before its desecration, this gallery was once known for its wide array of red and vermillion."
        redtile "For miles and miles, you could see the culmination of hours poured into the worship of the most delectable primary color."
        redtile "For instance, there was a nice piece which depicted a glorious autumn scene in dabs of scarlet and crimson dancing among the cerise earth."
        redtile "Another piece was a striking self portait, heightened by the calculated use of fire engine red alongside carmine, creating a beautiful abstraction."
        redtile "It was the height of art!"
        redtile "You want to know what happened to such a veritable storage of culture?"
        redtile "It was dumped into some dusty archive for some crackpot \"blue period.\""
        redtile "Countless examplars of colour use, condemned to permanent darkness because uncultured swinish rubes, who couldn't tell the difference between garnet and salmon pink, ate up this garish mess."
        redtile "I mean, it absolutely claws at my cultural soul to watch Blue Tile rave up and down about this every single day."
        redtile "Do you know how much of my life seeps away every time I hear that idiot acting like these paintings have the slightest etch of artistic integrity in them? It hurts!"
        redtile "So, I began scheming a way to get back at the blue gallery: what if the exhibit were to have an...accident?"
        redtile "Lets say, one of the vistors {i}accidentally{/i} spilled something over the art pieces? That would be a tragic thing to happen..."
        p suspicious "So you attempted to spill something on the art?"
        redtile "Well...there was maybe a little accident."
        redtile "A tiny scoop of miso soup for the starving art...pieces."
        redtile "Promise you'll keep this next part a secret?"
        p suspicious "OK..."
        redtile "It was me. I brought some miso soup from home and tried to throw it on the art when Blue wasn't looking."
        redtile "Besides, it wasn't like I was defacing them!"
        redtile "You could think of it as an improvement, like those art restorers who repaint pieces back to new."
        redtile "Anyway, all the soup did was rust the gates, which was really the only redeeming quality about this exhibit."
        redtile "I'm sure the security guard has it out for me though. Someone else took the blame, but I still have the evidence on me."
        redtile "I need to get rid of it before he sees it, but I can't risk drawing attention to myself."
        redtile "Actually, here! You take it!"
        $ item.ladle_empty = True
        show ladle_empty
        show posty concerned
        "You got the {b}ladle{/b}!{p}You feel guilty just carrying it..."
        p "What do I do with it?"
        redtile "I would extremely appreciate it if you get that ladle as far away from here as you can."
        redtile "Think of it as a token of red appreciation and blue disdain, if you will."
        p "OK, well, talk to you later."
        jump museum_blue

    elif item.ladle_empty:
        show posty neutral
        p "Hey, Red Tile."
        redtile "Just call me Red. Have you gotten rid of that ladle yet?"
        p "No, but I should be able to keep it a secret as long as I've got it hidden."
        redtile "Ok, well be careful. I don't want the security guard or Blue figuring out I tried to vandalize this painting."
        redtile "Even though it deserves it. It's a mockery to the medium itself!"
        redtile "Even a small trace of dark red would create a more appealing contrast than just light blue and dark blue."
        p "You know, if I wanted to, I could do what you did again and take the painting for myself."
        p astonished "I really want that painting. It sings to me..."
        redtile "You're not saying you're gonna risk your own life to deface an art piece, are you?"
        p "No..."
        p "And on that note, I need to go."
        jump museum_blue

    elif bt_distracted:
        show posty neutral
        show bluetile scared behind redtile:
            xzoom -1.0
            xpos 0.75
        bluetile "How could you say such a thing?!"
        extend annoyed " Your mere presence ruins the beauty of this exhibit!"
        redtile "Can't you see how horrible this is? The blue is just sooo outdated! Doesn't even look good."
        bluetile scared "Take that back! Please take that back!"
        redtile "{i}Posty, what are you doing here?! Go do your thing! I can only argue so much!{/i}"
        jump museum_blue

    elif item.ladle_full and miso_blocked:
        show posty neutral
        show redtile 
        if saw.rdeal:
            redtile "Well? Where's my compensation?"
        else:
            p "Hey Red, mind if I ask you a favour!"
            redtile "Sure, whatcha want me to do?"
            p concerned "I attempted to \"add\" some colour to the exhibition, but Blue Tile stopped me."
            redtile "Ah of course, Blue would never let his precious little pieces get harmed."
            p suspicious "Well, I noticed that he gets really passionate when it comes to blue stuff, so I was hoping you could distract him with a couple remarks about the color blue for me."
            redtile "No way."
            p astonished "Come on, you can get revenge for the red exhibit! Just some small talk!"
            redtile "When it comes to Blue, there is never just small talk."
            redtile "That guy can be so hung up on that, it's annoying."
            redtile "One more hour of him talking and I am going to lose it!"
            redtile "Besides, I've risked too much as is."
            p concerned "What would it take?"
            redtile "Maybe some cash. If I have to deal with him, at least I should be fairly compensated for my sacrifice."
        label .rt_money:
            menu:
                "Offer cash." if (money > 0) and (quest.moneys == False):
                    show cash_total at truecenter
                    show posty concerned
                    p "Will this do?"
                    redtile "You would need to offer me way more money than that. You got anything else?"
                    p "Let me check. Sorry, I've never bribed anybody before."
                    hide cash_total
                    jump .rt_money
                "Offer red cash." if item.red_cash:
                    show redcash
                    show posty concerned
                    p "I have this red bill I found on the floor."
                    redtile "Hey! I must've dropped this on the way in!"
                    redtile "This is worth more to me than any plain old dollar bill!"
                    redtile "Thanks, Posty! You got yourself a deal. Gimme a second to get started!"
                    redtile "Hey, Bluey!"
                    hide redtile with moveoutright
                    "Red Tile draws Blue Tile's attention away from the painting and asks him about his favorite shades of blue. They look absolutely bored."
                    "Now's your chance to use that soup and get that painting!"
                    $ item.red_cash = False
                    $ bt_distracted = True
                    jump museum_blue
                "Never mind." if (item.red_cash == False):
                    $ saw.rdeal = True
                    jump museum_blue

    elif item.ladle_full:
        show posty astonished
        show redtile
        redtile "What are you still doing with that ladle, Posty?"
        p "I filled it with miso soup again!"
        redtile "What? What happened to \"get it as far away from here as you can?\""
        p "It's complicated! Look, you have to take this ladle back!"
        show ladle_full
        p "You need to splash the soup on the painting! You have to do it for me!"
        redtile "Posty, I gotta go on living!"
        p "Just throw it! Throw it when no one's looking!"
        redtile "You throw it when no one's looking!"
        p "I can't! I'm not sneaky! They'll send me to jail and I can't afford bail on a mailbox salary! Please, you gotta do it for me, I'm begging you!"
        redtile "Nothing doing! I can't be seen with the ladle! I'm trying to lay low! It has to be you!"
        p concerned "OK, I guess I'll do it myself."
        p angry "But if I get arrested for this..."
        extend "I'll be really upset with you."
        hide ladle_full
        jump museum_blue


label .painting:
    if saw.bluetile == False:
        scene bg blue_talk
        show posty neutral
        show bluetile giddy
        $ saw.bluetile = True
        bluetile "Hello!!! Another lover of this exhibit! Yay!!!"
        bluetile "I'm Blue Tile! My friends call me Blue! That's my friend Red Tile! Who are you?"
        p "Name's Posty. What's going on?"
        bluetile "This is the new blue exhibit they curated just a few days ago! This is one of the happiest days of my life!"
        bluetile "This artwork in particular really speaks to me! It's a portrait of Crayon Box, the host of that Open Source Objects show in the dome! Does it speak to you too?"
        p "Oh no, I'm just looking aro-"
        p astonished anim "!"
        "As soon as you glance at the painting Blue Tile refered to, you are suddenly captured with the feeling of {color=#ffff00}{i}inspiration{/i}{/color}."
        p astonished -anim "...Woahh..."
        bluetile "You said it!!! This entire exhibition makes me feel things like astonishment, awe, and glory!"
        bluetile "Ever since these beautiful masterpieces fell from the clear skies, I've always had to watch out for jealous vandals whom I won't name-"
        extend annoyed " {i}coughs{/i} Red Tile {i}coughs{/i}"
        bluetile "...who have a vendetta against this exquisite cultural array due to it being \"the wrong colour\"."
        p "Uh huh..."
        extend quiet "{i} If only those bars weren't in the way...{/i}"
        bluetile giddy "Personally, I don't have a particular favorite colour, I like all the colours of the rainbow: Blue, Zaffre, Periwinkle, Azure, Denim, Glaucous and Eclipse!"
        bluetile annoyed "But that doesn't mean I shun other colours like \"Paint the Whole Gallery Red\" Tile,"
        extend giddy " I just like these pieces because of the message and the meaning behind every stroke and every frame..."
        p talk "Yeah yeah..."
        extend quiet "{i} How would I even carry it?{/i}"
        bluetile giddy "I am so glad we can come to such total agreement about these pieces, not just because of colours. "
        extend annoyed "LIKE SOMEONE WHO I HAVE THE GRACE TO NOT NAME AND SHAME!"
        if item.ladle_full:
            p astonished "SCREW IT! I HAVE TO SET IT FREE!"
            jump .painting_ladle_blocked
        else:
            bluetile scared "Are you doing OK?"
            show posty neutral
            p "Huh- Oh! I'm sorry! I think I dozed off there."
            bluetile giddy "Oh, that's alright! I get it! I sometimes feel that way when I stand here for too long too!"
            p "I should probably go. Cya!"
            jump museum_blue

    elif quest.painting_blue:
        scene bg blue_talk taken
        show posty concerned
        show bluetile scared
        bluetile "AUGH!! Where could it have gone?? Who could have taken it?!?"
        p "What's wrong? Feeling blue?"
        bluetile "It's the painting of Crayon Box! It's gone!"
        p sad "Oh whaaat? Noooooo! You know where it went?"
        bluetile "I WOULDN'T BE LOOKING AROUND FOR IT IF I KNEW, POSTY!"
        p concerned "Calm down, blue dude! Think about where you last saw it and work backwards from there."
        p "That's what I do when I lose my valuable possessions."
        bluetile annoyed "Ooohh, it's that maroon loser who took my precious painting. That cultural ignoramus was never open to anything that didn't rhyme with zred or mrimson!"
        bluetile  "I was always accommodating to their wishes and desires! I was even considering going to a red exhibit down the street to even it out!"
        bluetile "But that scarlet boor just went and declared war on me! That won't stand on my watch."
        "{i}Gosh, he's angry! You almost feel bad. {/i}"
        extend "{i}Almost.{/i}"
        p talk "Um, good luck with your search."
        jump museum_blue

    elif saw.bluetile and (item.ladle_full == False):
        scene bg blue_talk
        show posty happy
        show bluetile giddy
        p "Hey again, Blue!"
        bluetile "Hi Posty!"
        show posty concerned
        "You look away from the painting. You don't want to be caught in a trance again. You can sense the {color=#ffff00}{i}inspiration{/i}{/color} emanating from the framed piece."
        "You can almost hear it begging you to release it from its caged shackles."
        p "So what's so great about this exhibit?"
        bluetile "Isn't it obvious?"
        p suspicious "Well like, is it the imagery and subject matter people make with the color blue?"
        p "I mean, with this piece, Crayon Box is something of a pop art icon nowadays."
        bluetile "Oh, of course! What people create with the lightest tints of cyan and an analogous color palette is incredible!"
        bluetile annoyed "My friend Red likes to think that all I am is a numbnuts obsessed with the color blue, like I'm its number one fan and sworn protector."
        p "Aren't you though?"
        bluetile giddy "Well yeah!"
        bluetile "But what they don't know is that I wouldn't be if everything blue wasn't so pretty!"
        p "OK."
        p "Well, talk to you later."
        bluetile giddy "Bye Posty! Come by again!"
        jump museum_blue

    elif item.ladle_full:
        jump .painting_ladle

label .painting_ladle:
    if bt_distracted:
        scene bg blue_talk
        show posty concerned
        show ladle_full
        p concerned "Alrighty, here it goes!"
        hide ladle_full
        show bg blue_talk rusted
        "You repeat Red Tile's crime, splashing more miso soup on the painting!"
        p angry "Drat, I missed! Curse you, weak arms!"
        p annoyed "All I hit was this gate that has rusted open-"
        p astonished quiet "!!"
        p happy "I just got an idea..."
        show bg blue_talk taken
        show painting_blue
        "You got an {b}art piece{/b}!{p}Whether you love it or hate it, there is no denying that it makes great use of the azure colour."
        extend " You now feel some {color=#ffff00}{i}inspiration{/i}{/color}!"
        hide painting_blue
        p happy "Ohohoho, I'm closer to true creativity!"
        p astonished "Uh oh, here comes Blue!"
        hide posty with moveoutleft
        show bluetile annoyed with moveinright
        $ renpy.transition(moveinleft, layer="master") #prevents interruption of the text window
        $ item.ladle_full = False
        $ item.painting_blue = True
        $ quest.painting_blue = True
        $ bt_distracted = False
        $ paintings += 1
        bluetile annoyed "I swear I have never seen a more unqualified person in my life; they can't appreciate the subtle nuances-"
        bluetile annoyed quiet "..."
        bluetile scared "Where did the painting go?"
        bluetile scared "This exhibit has been... vandalized!"
        bluetile scared "My favorite piece, gone!"
        bluetile scared "Who did this?!"
        bluetile scared "Who dared to lay their fingertips on this masterpiece?!"
        bluetile scared "I'll find that thief and stuff them with so much legalese, they will be speaking it!"
        bluetile scared "DO YOU KNOW WHO I AM?!"
        bluetile scared "I HAVE A WHOLE BOOK OF LAWYERS READY TO LITIGATE YOUR EXISTENCE, CAN YOU HEAR ME?!"
        bluetile annoyed "I swear if that piece doesn't come back here within thirty minutes, I'll send the dogs out."
        bluetile annoyed "Aaaaaaaaaaaaaarggh!"
        jump museum_blue

    else:
        jump .painting_ladle_blocked

label .painting_ladle_blocked:
    scene bg blue_talk
    show posty concerned
    show bluetile scared
    $ miso_blocked = True
    "You attempt to repeat Red Tile's crime, unsheathing the ladle filled with miso soup and preparing to toss it at the painting bars."
    p concerned "Alrighty, here it goes!"
    bluetile "HEY!! What do you think you're doing?!"
    p quiet "... "
    extend neutral "Nothing."
    bluetile annoyed "Liar! I will not let you do {i}anything{/i} to ruin this glorious painting!"
    bluetile "This is everything I live for! And you are not gonna take it away so easily!!"
    bluetile "So scram, you vandal!"
    jump museum_blue


