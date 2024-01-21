# todo: #25 museum entrance conversation background

image bg museum_entrance_top:
    "map-bgs/museum_entrance_top.png"
    zoom 1.15
    yalign 0.2

image bg museum_entrance:
    "dbgs/museum_entrance_dbg.png"
    xzoom -1.0

image notice:
    "items/notice.png"
    truecenter
    zoom 0.5

transform posteaselpos:
    xalign 0.5
    yalign 1.0

label museum_entrance:
    if saw.museum == False:
        jump .first_time
    else:
        scene bg museum_entrance_top # TODO: #26 museum entrance imagemap
        show posty neutral

        p "_"

        menu:
            "Check out the Blue Exhibit.":
                jump museum_blue
            "Check out the War Exhibit.":
                jump museum_war
            "Check out the Food Exhibit.":
                jump museum_food
            "Check out those easels?" if (paintings != 3):
                jump .easels
            "Easels:\nUse the three paintings as {color=#ffff00}{i}inspiration{/i}{/color}." if (paintings == 3) and (quest.paintings == False):
                jump .inspiration
            "Talk to Security Cameron again.":
                jump .cameron
            "Leave.":
                jump mainstreet

label .inspiration:
    scene bg museum_entrance
    show posty neutral at posteaselpos
    p "_" # posty feels a rush of inspiration, due to the three stolen paintings in her possession!
    if item.napkin:
        show badpainting
        p "_" # ... and not this one, which isn't even a painting.
        hide badpainting
        p "_" # but yeah!
    scene bg painting_combined # 253
    "You ride the blast of creativity and combine your inspirations into a {b}new work of art{/b}!"
    $ quest.paintings = True
    scene bg museum_entrance
    show painting_combined
    show posty neutral
    show cameron
    cameron "_" # cameron is really mad, as he's finally noticed that you've been stealing paintings and have now irreparably combined them into this 'mess'
    p "_" # posty asks if she's going to be kicked out
    cameron "_" # reluctantly, cameron explains that he's already kicked someone out today, so he can't do it again. but he can confiscate the damaged art...
    hide painting_combined
    "{b}{color=#bdbfe2}Security Cameron{/color}{/b} took the {b}art piece{/b} from you!"
    cameron "_" # ...and write you a notice of reprimand!
    show notice #255
    "You received the {b}notice of reprimand{/b}!" # describe #256
    hide notice
    $ item.notice = True
    cameron "_" # he grumbles something like "enjoy the exhibitions"
    p "_" # parting remark
    jump museum_entrance

label .first_time:
    scene bg museum_entrance
    show posty neutral
    show cameron
    p "Well, this place is cute. Maybe I can—"
    cameron "Welcome to the Art Museum!" 
    p happy "—Oh! Thanks!"
    cameron "The name's Security Cameron. Nice to meet you."
    p "I'm Posty. Nice to meet you too!" 
    cameron "Feel free to peruse one of our many current exhibits, all of which are free of soup because no soup incidents or attacks occur here on my watch!" 
    p suspicious quiet "..."
    p -quiet "...What?"
    cameron "Alright, you caught me. We suffered soup-related losses in a soup attack earlier today."
    p concerned "... What's a soup attack?" 
    cameron "Some shady good-for-nothing Miso Soup character spilled some of their contents on the gate in the Blue Exhibit. If they had splashed two inches to the left, one of our paintings would've been a goner."
    cameron "This kid swears they wear a Plastic Wrap when they're in the museum, but I know the truth. They removed the wrap. They're a no-good vandal."
    cameron "I swear on my life as this fair museum's Head Security Guard, I will bring justice to that Miso Soup fiend."
    p "...How do you know they took off the wrap?"
    cameron "Because there was once no soup in the exhibit, and then there was. What else could have happened?"
    cameron "Also I'm never wrong."
    cameron "Also I'm really cool and everyone loves me."
    p neutral quiet "..."
    cameron "Anyway."
    cameron "Enjoy your time at the museum. Have a souptacular— I mean spectacular day. Ugh!!!" 
    p -quiet "...See ya."
    $ saw.museum = True
    jump museum_entrance

label .easels:
    scene bg museum_entrance
    show posty neutral at posteaselpos
    p "Hmmm...a few blank easels. Must be for on-site painters."
    p astonished "Woah! What the?"
    p astonished "I feel... {w}something."
    p concerned "Could this be..."
    p astonished "THE GERMINATING SEEDS OF INSPIRATION!?"
    p astonished "I have to create something!"
    p suspicious "But what?"
    "Maybe you should take a walk around the museum. You know, for {color=#ffff00}inspiration.{/color}"
    p happy "Good idea disembodied voice!"
    jump museum_entrance

label .cameron:
    scene bg museum_entrance
    show cameron
    if quest.paintings:
        show posty neutral
        p "_" # talking to security cameron after receiving the note of reprimand
        jump museum_entrance
    
    elif item.ladle_full:
        show posty neutral quiet
        p "{i}I should probably avoid {b}Security Cameron{/b} if I have this ladle. Don't want him to think I would spill the soup on a painting!{/i}" # this text will be a notification in the final version of this room's nav screen
        jump museum_entrance

    elif quest.painting_blue:
        show posty neutral
        p "_" #128 talking to security cameron after splashing soup on the painting
        jump museum_entrance
        
    else:
        show posty neutral
        p "Hey man."
        cameron "Hey."
        cameron "..."
        cameron "Did you need something?"
        p "Oh. No. Just… checking in. Seeing what's up."
        cameron "'What's up'? My blood pressures what's up!"
        cameron "Just kidding I don't think I have that."
        p "..."
        p "Right."
        cameron "Just come back to me if something broth-ers you. I mean bothers you."
        cameron "Bye."
        p "Bye."
        jump museum_entrance
