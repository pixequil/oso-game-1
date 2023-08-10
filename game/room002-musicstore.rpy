image bg music_top:
    "map-bgs/music_top.png"
    zoom 1.3
    yalign 0.2

image bg music:
    "dbgs/music_store_dbg.png"

label musicstore:
    $ last.mainx = 0.15
    scene bg music_top
    show posty neutral
    p "_" #294 music store imagemap

    menu:
        "Neon Lights":
            jump .nl
        "Sheet":
            jump .sheet
        "Jukebox":
            jump .jb
        "Leave.":
            jump mainstreet

label .nl:
    show bg music
    show neon
    if (saw.nl == False):
        show posty neutral
        neon "Welcome to the music store!" #305 neon lights first conversation
        $ saw.nl = True
    else:
        show posty neutral
        neon "Oh hi again." #306 neon lights repeat greeting
    p "__" #307 neon lights conversation
    jump musicstore

label .sheet:
    show bg music
    show sheet
    if (saw.sheet == False):
        show posty neutral
        sheet "Welcome to the music store!" #309 sheet first conversation
        $ saw.sheet = True
    else:
        show posty neutral
        sheet "Oh hi again." #310 sheet repeat greeting
    p "__" #311 sheet conversation
    jump musicstore

label .jb:
    scene bg music
    show jb
    if (saw.jb == False):
        show posty neutral
        jb "_" #296 jukebox first conversation
        $ saw.jb = True
    else:
        show posty neutral
        jb "_" #295 quick greeting
    menu:
        "Talk to Jukebox.":
            jump .talk
        "Play some tunes!":
            jump .tunes
        "Bye!":
            jump musicstore

label .talk:
    p "_" #297 jukebox second conversation
    jump .jb

label .tunes:
    "This feature is not yet available." #298 jukebox music player
    jump .jb