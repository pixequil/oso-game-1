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
    auto "Oh god oh god oh god how can I explain this?!" 
    p "Oh what seems to be the issue sir?"
    auto "My business is trying to make a contract and I am unable to make it-"
    p concerned "On time?"
    auto sad "At all!"
    auto bothered "Apparently there are a lot of orange cones everywhere in main street, major construction works."
    auto "I don't know why NOW of all times they strike at once, but now I am in a major predicament."
    p concerned "Woah you must be some really important person if you stressing like that!"
    auto sad "I wish, I just own a small legal services firm in the cheapest part of the city: that contract is all I'd got!"
    auto bothered "I have to act all like Mr Community Service for stir fry and pennies and prevent half of my clients from practically signing their confessions and handcuffing themselves."
    auto sad "The other week I had to save this doofus from hard labour-"
    p astonished "HARD LABOUR?!"
    auto "A small technicality in the city's Charter of Rights and Liberties, grants the council the right to force people into doing everyone's work for them in case of an 'unforgivable crime'."
    p "I didn't know they had such laws in the books."
    auto "Yeah that was the first time I seen that loophole, had to dig up old paperwork to prove that section hadn't been in force since this city was just a swamp."
    auto bothered "Didn't help the case when the frustrating fizz-in-the-brain attempted to bribe the judge with 'endorsement coupons' and a signature in return for clemency."
    p suspicious "Those antics sound awfully similar to a certain guy I know in Mainstreet..." 
    p concerned "Seems like you have a lot on your plate."
    auto "And to top it all off, I have only three other guys to help me: Mop currently sick with the flu, Playing Cards is desperately keeping the client happy and Mr Blob just decided to up and leave!"
    p astonished "Wait... you know Blob?"
    auto "Yeah, he was supposed to do all the background stuff: sorting through paperwork, answering calls and all that."
    auto "Really good at that too, although he had... certain quirks."
    p suspicious "Quirks?"
    auto "Well for one, he was unusually rigid in the work ethic department."
    auto "Every day he would clock in on the dot, clock out on the dot."
    auto "Even when we were flooded with late paperwork, he would leave on the hour without a care."
    auto "Now he straight up gone without even a letter!"
    auto sad "Since then, business has been hectic to say the least."
    auto "I wish he would come back..."
    "{i}ring ring..!{/i}" #390
    auto bothered "Oh it is Playing Cards! Hopefully she can pull this through."
    auto "...hello"
    auto "...mhm"
    auto "..."
    auto sad "...oh."
    auto "I see."
    auto "............"
    auto "Thanks, see you soon."
    p concerned "Did you keep it?"
    auto "..."
    auto "We lost the deal."
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
