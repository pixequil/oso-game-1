image bg music_top:
    "map-bgs/music_top.png"

image bg music:
    "dbgs/music_store_dbg.png"

screen music_nav:
    viewport:
        child_size (1280,720)
        add "music_top"

        imagebutton:
            xanchor 0.5 
            yanchor 0.5
            xpos 679
            ypos 650
            idle "arrow dn black"
        imagebutton:
            xanchor 0.5
            yanchor 0.5
            xpos 679
            ypos 650
            idle "pnav dn i"
            hover "pnav dn"
            action Jump("mainstreet")

        imagebutton: # jb
            pos (920, 0)
            idle "nav_jb"
            hover "nav_jb p"
            action Jump("musicstore.jb")

        imagebutton: # nl
            pos (320, 50)
            idle "nav_nl"
            hover "nav_nl p"
            action Jump("musicstore.nl")

        imagebutton: # sheet
            pos (800,350)
            idle "nav_sheet"
            hover "nav_sheet p"
            action Jump("musicstore.sheet")



image nav_sheet = Composite(
    (250,250),
    (0,0), "hitbox",
    (150,20), "minisprites/sheet_ow_sprite.png",
)
image nav_sheet p = Composite(
    (375,250),
    (0,0), "nav_sheet",
    (50,30), "pnav rt"
)

image nav_nl = Composite(
    (375,250),
    (0,0), "hitbox",
    (150,20), "minisprites/neonlights_ow_sprite.png",
    (0,80), "map-bgs/musicstoreforeground.png"
)
image nav_nl p = Composite(
    (375,250),
    (0,0), "nav_nl",
    (150,30), "pnav up"
)


image nav_jb = Composite(
    (250,250),
    (0,0), "hitbox",
)
image nav_jb p = Composite(
    (250,250),
    (0,0), "nav_jb",
    (40,30), "pnav up"
)

label musicstore:
    $ renpy.choice_for_skipping()
    $ last.mainx = 0.15
    play music "sound/music/LuckyLootCrate - purple precipitation.ogg" if_changed
    call screen music_nav

# label musicstore:
#     $ last.mainx = 0.15
#     scene bg music_top
#     show posty neutral
#     p "_" #294 music store imagemap

#     menu:
#         "Neon Lights":
#             jump .nl
#         "Sheet":
#             jump .sheet
#         "Jukebox":
#             jump .jb
#         "Leave.":
#             jump mainstreet

label .nl:
    scene bg music
    show neon
    if (saw.nl == False):
        show posty neutral
        neon "Heya homegirl, welcome to the Music Store: the home of all things music!"
        neon "I am Neon Lights, the resident expert for all things tubular!"
        neon "Whether you looking for slick tunes to veg out to or just wanna appreciate the history of your favourite artists, I know the A-Zs of it."
        neon "All I need is a record and a player and I'm set for life!"
        neon "Hopefully you will find it as stellar as I do: it wouldn't hurt to find a fellow aficionado to talk with!"
        neon "What can I help you find?"
        $ saw.nl = True
    else:
        show posty neutral
        neon "Hi again! What do you need?"
    p "Nothing at the moment."
    neon "Ok..."
    neon "Nothing. Of course. Just like I do every day I stand in front of this stupid stand for 8 stupid hours talking to these stupid-"
    p concerned "Excuse me?"
    neon "...I said as long as you're still browsing, you can talk to Jukebox in the corner and play some music."
    neon "Maybe you'll like one of them enough to purchase one."
    p happy "Sounds cool. I'll be sure to check it out."
    jump musicstore

label .sheet:
    scene bg music
    show sheet
    if (saw.sheet == False):
        show posty neutral
        sheet "Hi, welcome to the Music Store, the home for all things audio related."
        sheet "My name is Music Sheet, Sheet for short."
        sheet "Not to brag, but I know every note, rest and staff of music here!"
        sheet "Whether you are confused by semidemihemiquavers or looking for recommendations that will take you way back to your childhood, I am the guy for you!"
        sheet "Hopefully I'll see you more frequently around here; Neon gets a bit cranky doing nothing after a while."
        sheet "So anyway, what can I do for you?"
        $ saw.sheet = True
    else:
        show posty neutral
        sheet "Nice to see ya again! How may I help you?"
        p quiet "Asking again probably wouldn't hurt."
    p neutral "You wouldn't happen to know how to deliever a package safely, would you?"
    sheet "Nope."
    p "Yeah, that checks."
    sheet "To be honest, there's not much to do here other than listen to music."
    sheet "Unless you wanted to take a break and listen to music, you should probably finish delievering your package or something."
    p annoyed "OK mom."
    jump musicstore

label .jb:
    scene bg music
    show jb
    show posty happy
    if (saw.jb == False):
        jb "Sup, I'm Jukebox (Juke for short)."
        p "Hello, Jukebox! I'm Posty!"
        jb "Hey Posty, how's it going?"
        p "I'm doing well, but I've been contemplating what song could be my favorite."
        jb "Well lucky for you, I'm the go-to for any and all music, from vinyls to digital!"
        jb "If you have a record you dream playing but you don't have the equipment, just give it to me and hear it in crisp detail!"
        jb "I even have some tracks of my own that you could listen to!"
        jb "Let's hear them all and you can pick a favorite later."
        p "Great idea."
        $ saw.jb = True
    else:
        jb "Let's listen to some music!"   
    menu:
        "Talk to Jukebox.":
            jump .talk
        "Play some tunes!":
            jump .tunes
        "Bye!":
            jump musicstore

label .talk:
    show posty neutral
    p "What is it you do again?"
    jb "I can play any music you give me!"
    jb "Whether it's the music in this game or some original music of my own, I can play it and swap out the music in this store!"
    show posty confused
    jb "I even have some remixed OSO tracks!"
    p confused "The music in this what?"
    jb "The music in this store."
    p neutral "Oh OK. Sorry for mishearing you."
    jb "That's OK, I get that all the time."
    jump .jb

label .tunes:
    "This feature is not yet available." #298 jukebox music player
    jump .jb