image bg alley_top:
    "map-bgs/alley_top.png"
    zoom 1.8
    yalign 0.2

image bg alley:
    "dbgs/alley_dbg.png"

label alley:
    $ last.mainx = 0.65
    scene bg alley_top
    show posty neutral
    p "_" #258 alley imagemap

    menu:
        "Tag":
            jump .tag
        "Stick Shift":
            jump .stick
        "Get outta here":
            jump mainstreet

label .tag:
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
    "You got the {b}glittery gold spray paint{/b}!" #261
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
    p "So uh.. Have you been up to anything new lately?"
    tag "Kind of.. I\'ve been experimenting with new colors lately, It\'s quite fun! You should try it some time with me."
    p "Sure! I\'d be down to do so."
    tag "I need to get more spray paint cans.. My old ones are running out of ink!"
    p happy "I can help you get some!"
    tag "Really?! I\'m happy you're able to get me some more supplies!"
    p "No problem, I\'m always willing to help out someone like you!"
    p "Who\'s your inspiration to do graffiti art?"
    tag "Oh! There\'s this guy named Graffiti, and he\'s so cool! He can shapeshift into letters and objects, he can even make objects and all that stuff! I look up to him a lot."
    p "That\'s great! I\'m sure he\'d be proud of the kind of art you\'d make."
    tag "Heh, thanks Posty."
    p "Of course! You guys would be a great duo together!"
    jump alley

label .stick:
    scene bg alley
    show posty neutral
    show stickshift
    stick "_" #259 stickshift conversation
    jump alley