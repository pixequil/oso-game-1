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

label .tag2: #263
    show posty neutral
    tag "_" # tag sees your notice of reprimand and therefore thinks you're extremely cool, considering you to be a kindred spirit. they give you a can of gold spray paint.
    show spraypaint at truecenter #260
    $ item.notice = False
    $ item.spraypaint = True
    $ tag_trade = True
    "You got the {b}glittery gold spray paint{/b}!" #261
    hide spraypaint
    if item.scrap_trophy:
        call trophy
        tag "_" # tag comments on your use of the spray paint
        jump alley
    else:
        p "_" # some kind of thank-you
        jump alley

label .tag3:
    show posty neutral
    tag "_" #264 revisiting tag after receiving the spray paint. don't mention what the spray paint may or may not have been used for.
    jump alley

label .stick:
    scene bg alley
    show posty neutral
    show stickshift
    stick "_" #259 stickshift conversation
    jump alley