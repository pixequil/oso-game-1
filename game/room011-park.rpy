image bg park_top:
    "map-bgs/park_top.png"

image bg park:
    "dbgs/park_dbg.jpg"

transform flip: 
    xzoom -1.0

screen park_nav:
    viewport:
        child_size (1280,720)
        add "park_top"

        imagebutton: 
            xanchor 0.5
            yanchor 0.5
            xpos 658
            ypos 80
            idle "arrow up black"
        imagebutton: 
            xanchor 0.5
            yanchor 0.5
            xpos 658
            ypos 80
            idle "pnav up i"
            hover "pnav up"
            action Jump("mainstreet")

        imagebutton: # auto
            pos (300, 30)
            idle "nav_auto"
            hover "nav_auto p"
            action Jump("park.auto")
        showif quest.retainer and (saw.retainerpark == False):
            imagebutton:
                pos (700,500)
                idle "nav_retp"
                hover "nav_retp p"
                action Jump("park.retainer")
        imagebutton: # bench left
            pos (86, 300)
            idle "nav_bench"
            hover "nav_bench pl"
            action Jump("park.bench")
        imagebutton: # bench right
            pos (965, 213)
            idle "nav_bench"
            hover "nav_bench pr"
            action Jump("park.bench")

image nav_bench = Composite(
    (250,250),
    (0,0), "hitbox",
)
image nav_bench pl = Composite(
    (250,250),
    (0,0), "nav_bench",
    (0,20), "pnav rt"
)
image nav_bench pr = Composite(
    (250,250),
    (0,0), "nav_bench",
    (80,20), "pnav lt"
)

image nav_retp = Composite(
    (240,280),
    (0,0), "hitbox",
    (220-98,20), "minisprites/retainerhappy.png"
)
image nav_retp p = Composite(
    (240,280),
    (0,0), "nav_retp",
    (0,0), "pnav rt"
)

image nav_auto = Composite(
    (240,280),
    (0,0), "hitbox",
    (0,0), "minisprites/automatone.png"
)
image nav_auto p = Composite(
    (240,280),
    (0,0), "nav_auto",
    (20,40), "pnav lt"
)


label park:
    $ renpy.choice_for_skipping()
    $ last.mainx = 0.45
    play music "sound/music/LuckyLootCrate - patience.ogg" if_changed
    call screen park_nav

# label park:
#     $ last.mainx = 0.45
#     scene bg park_top
#     show posty neutral
#     p "_" #285 park imagemap

#     menu:
#         "Automotone":
#             jump .auto
#         "Retainer" if win_flag:
#             jump .retainer
#         "Take a break on one of the benches.":
#             jump .bench
#         "Back to main street.":
#             jump mainstreet

label .auto:
    scene bg park
    show posty neutral
    show auto bothered
    auto "Oh god oh man oh god oh man how can I explain this?!" 
    p "Oh, what seems to be the issue, sir?"
    auto "My business is trying to make a contract and I am unable to make it-"
    p concerned "On time?"
    auto sad "At all!"
    auto bothered "Apparently there's major construction work being done everywhere on Main Street! My way to work is blocked off by orange cones!"
    auto "I don't know why NOW of all times they shut down every road at once, but now I am in a major predicament."
    p concerned "Woah, you must be some really important person if you're stressing like that!"
    auto sad "I wish! I just own a small legal services firm in the cheapest part of the city; that contract is all I've got!"
    auto bothered "I have to act all \"Mr. Community Service\" to prevent half of my clients from practically signing their confessions and handcuffing themselves."
    auto sad "The other week, I had to save this doofus from hard labour-"
    p astonished "HARD LABOUR?!"
    auto bothered "A small technicality in the city's Charter of Rights and Liberties grants the council the right to force people into doing everyone's work for them in case of an \"unforgivable crime.\""
    p "I didn't know they had such laws."
    auto "Yeah, that was the first time I'd seen that loophole. I had to dig up old paperwork to prove that that section hadn't been enforced since this city was a swamp."
    auto sad "Of course it didn't help the case when my frustrating fizz-in-the-brain client attempted to bribe the judge with \"endorsement coupons\" and an \"autograph\" in return for clemency."
    p suspicious "Those antics sound awfully similar to a guy I know..." 
    p concerned "Seems like you have a lot on your plate."
    auto "And to top it all off, the only other three guys I have to help me are busy. Mop is sick with the flu, Playing Cards is desperately keeping her client happy, and Blob up and left!"
    p astonished "Wait... you know Blob? Like, OSO Blob?"
    auto bothered "Yeah, they were supposed to do all the background stuff: sorting through paperwork, answering calls, all that."
    auto "Really good at that too, although they had... certain quirks."
    p suspicious "Quirks?"
    auto "Well for one, they were unusually rigid in the work ethic department."
    auto "Every day, they would clock in on the dot, clock out on the dot."
    auto "Even when we were flooded with late paperwork, they would leave on the hour without a care."
    auto sad "Now, they straight up vanish and go on this reality show without even a letter!"
    auto  "Since then, business has been hectic to say the least."
    auto "I wish they would come back..."
    play audio "sound/ringring.wav"
    "{i}ring ring..!{/i}" #390
    auto bothered "Oh! It's Playing Cards! Hopefully she can pull this through. Excuse me."
    show auto:
        flip
    auto "...hello"
    auto "...mhm"
    auto "..."
    auto sad "...oh."
    auto "I see."
    auto "............"
    auto "Thanks, see you soon."
    show auto
    auto "..."
    p concerned "Well? Did you keep it?"
    auto "We lost the deal."
    jump park

label .retainer:
    scene bg park
    show posty neutral
    show retainer happy behind posty
    p "Oh hi again!"
    retainer "Hello! What are you doing here?"
    p happy "Just relaxing. "
    extend astonished "Never knew it would take all day to deliver one package!"
    show posty happy
    retainer "Heh. I was heading home, but decided to come here."
    retainer "Y'know, to get some fresh air!"
    "...."
    show posty neutral
    retainer "Hey uh... Thanks again for the trophy! "
    extend "It isn't as good as winning, but I'm happy that someone cares about me..."
    p happy "No problem man! Glad you're feeling better!"
    p happy "Well, I better get going. I think I'm going to take a nap."
    retainer "It was nice meeting you! Goodbye!"
    p "You too, bye!"
    $ saw.retainerpark = True
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
