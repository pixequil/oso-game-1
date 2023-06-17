image bg alley_top:
    "map-bgs/alley_top.png"
    zoom 1.8
    yalign 0.2

image bg alley:
    "dbgs/alley_dbg.png"

label alley:
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
    elif saw.tag:
        jump .tag2
    else:
        jump .tag1



label .stick:
    scene bg alley
    show posty neutral
    show stickshift
    stick "_" #259 stickshift conversation
    jump alley