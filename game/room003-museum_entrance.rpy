# todo: #25 museum entrance conversation background

label museum_entrance:
    if saw.museum == False:
        jump .first_time
    else:
        scene bg museum_entrance_top # TODO: #26 museum entrance imagemap (needs illustration)
        show posty neutral

        p "_"

        menu:
            "Check out the Blue Exhibit.":
                jump museum_blue
            "Check out the War Exhibit.":
                jump museum_war
            "Check out the Food Exhibit.":
                jump museum_food
            "Check out those easels?":
                jump .easels
            "Talk to Security Cameron again.":
                jump .cameron
            "Leave.":
                jump mainstreet

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
    p neutral quiet "..."
    p -quiet "...What?"
    cameron "Alright, you caught me. We suffered soup-related losses in a soup attack earlier today."
    p concerned "What's a soup attack?" 
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
    scene bg easels # TODO: #29 easels scene
    show posty neutral

    "There are three {b}easels{/b} here." # TODO: #30 rewrite easel narration
    p quiet "..."
    "You feel ...{w} something."
    "The germinating seeds of inspiration?"
    "Maybe you can make a work of art here, if you collect enough {color=#ffff00}inspiration{/color}."
    jump museum_entrance

label .cameron:
    scene bg museum_entrance
    show posty neutral
    show cameron
    p "_" # TODO: #31 talking to Security Cameron again
    jump museum_entrance
