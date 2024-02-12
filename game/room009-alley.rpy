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

        textbutton "Show Hitboxes":
            action ToggleVariable("devmode",True,False)

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
    $ last.mainx = 0.65
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
    tag "_" #262 tag explains their deal
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
    tag "I\'ve been experimenting with new colors lately, It\'s pretty fun! You should try it some time with me."
    p happy "Sure! I\'d be down."
    tag "I need to get more spray paint cans. My old ones are running dry!"
    p "I can help you get some!"
    tag "Really?! That means a lot to me that you're able to get me some more supplies!"
    p "No problem, I\'m always willing to help out a fellow artist like yourself!"
    p "Who\'s your inspiration to do graffiti art?"
    tag "Oh! There\'s this guy named Graffiti, and he\'s so cool! He can shapeshift into letters and objects, he can even make his own tools and all that stuff! I look up to him a lot."
    p "That\'s great! I\'m sure he\'d be proud of the kind of art you\'d make."
    tag "Heh, thanks Posty."
    p "Of course! You guys would be a great duo together!"
    jump alley

label .stick:
    $ last.alleyy = 0.6
    scene bg alley
    show posty neutral
    show stickshift
    stick "_" #259 stickshift conversation
    jump alley