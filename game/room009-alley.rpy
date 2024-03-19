image bg alley_top:
    "map-bgs/alley_top.png"

image bg alley:
    "dbgs/alley_dbg.png"

default last.alleyy = 1.0

screen alley_nav:
    viewport:
        child_size (1280,1200)
        edgescroll (150, 2000)
        add "bg alley_top"
        yinitial last.alleyy

        # textbutton "Show Hitboxes":
        #     action ToggleVariable("devmode",True,False)

        imagebutton:
            xanchor 0.5 
            yanchor 0.5
            xpos 635
            ypos 1100
            idle "arrow dn"
        imagebutton:
            xanchor 0.5
            yanchor 0.5
            xpos 635
            ypos 1100
            idle "pnav dn i"
            hover "pnav dn"
            action Jump("mainstreet")

        imagebutton: # stick
            pos (700, 600)
            idle "nav_stick"
            hover "nav_stick p"
            action Jump("alley.stick")

        imagebutton: # tag
            pos (400, 400)
            idle "nav_tag"
            hover "nav_tag p"
            action Jump("alley.tag")

image nav_tag = Composite(
    (240,280),
    (0,0), "hitbox",
    (100,0), "minisprites/Tag_overworld.png"
)
image nav_tag p = Composite(
    (240,280),
    (0,0), "nav_tag",
    (120,20), "pnav up"
)

image nav_stick = Composite(
    (220,160),
    (0,0), "hitbox",
    (100,0), "minisprites/stick_shift.png"
)
image nav_stick p = Composite(
    (220,160),
    (0,0), "nav_stick",
    (0,10), "pnav rt"
)

label alley:
    $ renpy.choice_for_skipping()
    $ last.mainx = 0.65
    play music "sound/music/REZURRECTA - ZAKU.ogg" if_changed
    call screen alley_nav


# label alley:
#     $ last.mainx = 0.65
#     scene bg alley_top
#     show posty neutral
#     p "_" #258 alley imagemap

#     menu:
#         "Tag":
#             jump .tag
#         "Stick Shift":
#             jump .stick
#         "Get outta here":
#             jump mainstreet

label .tag:
    $ last.alleyy = 0.2
    scene bg alley
    show tag
    if tag_trade:
        jump .tag3
    elif item.notice:
        jump .tag2
    else:
        jump .tag1

label .tag1:
    show posty neutral
    tag "Ey, wassup?"
    p "The sky."
    p astonished "Oh, I mean..."
    p happy "Sup! Name's Posty."
    tag "What's a gal like you doing in this shady back alley?"
    p suspicious "I'm not quite sure myself. One minute, I was delievering a package and the next minute, I'm back here."
    p neutral "What do you guys do for fun back here?"
    tag "We rebel against the art establishment and all it stands for."
    p "What's there to rebel about it? I'm not much of an artist so I'm a little out of the loop."
    tag "Here, lemme lay somethin' down for ya, ya know that \"art\" museum, right?" #262 tag explains their deal
    p "Uh, yeah...? What about it?"
    show posty astonished
    tag "WHAT ABOUT IT?! WHAT DO YOU MEAN WHAT ABOUT IT?!??!"
    p anim "...!"
    tag "Ahem. Sorry 'bout that, heh, got a bit carried away... it's just, sigh, that institution! It's more like a regime in there!"
    tag "Stupid oldheads, talkin' 'bout what is and isn't art! They won't accept me n' my free spirit! Jus' they wait 'til they see my new magnum opus!"
    p neutral -anim "Oh? What is it?"
    tag "Heh, let's jus' say it requires a TON of special Glittery Gold Spray Paint! Hopefully that'll get my name out there. Who knows, maybe I'll even meet my idol, Graffiti!"
    tag "He's the coolest! He can shapeshift into letters and objects, he can even make his own tools and all that stuff! I look up to him a lot."
    p happy "That's great!"
    p neutral "Oh, well, er, I gotta go. I wish you good luck on your... endeavors." 
    tag "Thanks, babe. 'Preciate it!"
    jump alley

label .tag2:
    show posty neutral
    tag "Hey."
    p "Hi."
    tag "What\'s..."
    tag "...Woah, is that a notice of reprimand?!"
    tag "Dude! That\'s so cool! That must mean you\'re a renegade rebel just like me!" 
    p "I wouldn\'t say that exactly—"
    tag "Sticking it to the man, showing the world who\'s boss, being an incendiary, fighting for the little guy, all that jazz! It\'s you and me against the world, buddy!"
    tag "I\'m definitely not lonely or anything!"
    p confused "Uh..."
    tag "Anyway!!! All rabble-rousers like us gotta have something. You know what that is?"
    p concerned quiet "{i}Please don\'t give me a knife, Toasty won\'t let me live it down{/i}"
    tag "Spray paint!"
    p neutral "Oh."
    p happy "Oh!"
    tag "You gotta leave your mark somehow, you know?"
    show spraypaint at truecenter
    $ item.notice = False
    $ item.spraypaint = True
    $ tag_trade = True
    "You got the {b}glittery gold spray paint{/b}! {w}If you want to make something desirable, try spraying it with glittery gold!"
    hide spraypaint
    if item.scrap_trophy:
        call trophy
        tag "Oh, hey, cool."
        tag "I was expecting something more like tagging \"DARN THE MAN, SAVE THE EMPIRE\" but you know. A trophy is cool too."
        jump alley
    else:
        p happy "Thanks, Tag!" 
        tag "See ya later, firebrand."
        jump alley

label .tag3:
    show posty neutral
    p "So uh... have you been up to anything new lately?"
    tag "I\'ve been experimenting with new colors lately. It\'s pretty fun! You should try it some time with me."
    p happy "Sure! I\'d be down."
    tag "I need to get more spray paint cans. My old ones are running dry!"
    p "I can help you get some!"
    tag "Really?! That means a lot to me that you're able to get me some more supplies!"
    p "No problem, I\'m always willing to help out a fellow artist like yourself!"
    p "I\'m sure Graffiti \'d be proud of the kind of art you make."
    tag "Heh, thanks Posty."
    p "Of course! You guys would be a great duo together!"
    jump alley

label .stick:
    $ last.alleyy = 0.6
    scene bg alley
    show posty neutral
    show stickshift
    p "Hey... whatcha doing?"
    stick "Just working on a piece of graffiti."
    p suspicious "...That\'s it?"
    stick "That\'s it."
    p "You don\'t have like, some thing I have to fetch for you, or some goal I have to complete for you so you can give me some item to help me on my journey?"
    stick "Nah."
    stick "Just making some art. No goal in mind."
    stick "I\'m just doing it to do it. I\'m gonna finish this piece, not tell anyone about it, and I\'ll go about my regular life ‘til I get the urge to do it again."
    stick "It\'s just for me. It\'s fun."
    p neutral "...Huh."
    p "...Well, I\'ll let you get back to it, I guess."
    stick "Good luck on your journey!"
    p "You too!"
    stick "Be good, stranger."
    jump alley