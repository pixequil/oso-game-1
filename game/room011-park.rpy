image bg park_top:
    "map-bgs/park_top.png"
    zoom 1.3
    yalign 0.2

image bg park:
    "dbgs/park_dbg.jpg"

label park:
    $ last.mainx = 0.45
    scene bg park_top
    show posty neutral
    p "_" #285 park imagemap

    menu:
        "Automotone":
            jump .auto
        "Retainer" if win_flag:
            jump .retainer
        "Take a break on one of the benches.":
            jump .bench
        "Back to main street.":
            jump mainstreet

label .auto:
    scene bg park
    show posty neutral
    show auto bothered
    auto "_" #286 talking to automatone. A businessman taking a break in the park, because all the construction on main street has made trying to get to work into a futile act. He mentions that things were already complicated with Blob not there to help the company, and this is another problem on top.
    p "_"
    auto sad "_"
    jump park

label .retainer:
    scene bg park
    show posty neutral
    show retainer happy
    retainer "_" #287 retainer's feeling better after what happened at the dome just now.
    jump park

label .bench:
    if win_flag:
        jump .win
    else:
        scene bg park
        show posty neutral
        p "{i}..Maybe I could take a small break on the bench?{/i}"
        p angry "{i}No! I wont until I deliver this package!{/i}"
        p happy "{i}But boy am I looking forward to it!{/i}"
        jump park

label .win:
        scene bg park
        show posty neutral
        "It had been a long and busy day."
        p happy "It sure was!"
        "What was supposed to be a simple delivery of some butterflies became a hectic blur of tasks, people and talking as she met with a wide variety of people throughout the city."
        "Some people lived lives that were beyond her comprehension; artists, connoisseurs, wannabe marketers, lords even!"
        p astonished "I didn't even know they were still around!"
        "Well, 'lords'."
        "As the weight of sleep gradually settled, she felt a sense of satisfaction."
        "Another job well done!"
        p happy "zzzzzz"
    menu:
        "End the game?"

        "Yes, I'm finished.":
            show win_art #289
            jump credits
        "No, not yet.":
            jump park
