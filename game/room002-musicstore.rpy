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
    $ jukesong = "None"
    play music "sound/music/LuckyLootCrate - purple precipitation.ogg" if_changed
label .exitjb:
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
        neon "Whether you're looking for slick tunes to veg out to or just wanna appreciate the history of your favourite artists, I know the A-Zs of it."
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
    p neutral "You wouldn't happen to know how to deliver a package safely, would you?"
    sheet "Nope."
    p "Yeah, that checks."
    sheet "To be honest, there's not much to do here other than listen to music."
    sheet "Unless you wanted to take a break and listen to music, you should probably finish delivering your package or something."
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
        jb "If you have a song you dream of hearing but don't have the equipment, just give me the name and I'll play it in crisp detail!"
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
    jb "I can swap out the music in this store with any other track from this game!"
    p confused "The music in this what?"
    jb "The music in this store."
    p neutral "Oh OK. Sorry for mishearing you."
    jb "That's OK, I get that all the time."
    jump .jb

label .tunes:
    $ renpy.choice_for_skipping()
#    stop music fadeout 1.0
    call screen tunezzz
    jump .jb

screen tunezzz:
    viewport:
        child_size (1280,720)
        add "jukebg"
        add "jukebars"
        use juke_vbox
        
image jukebg:
    "images/jukebox_bg.png"
image jukebars:
    "images/jukebox_stripes.png"
    huepulse

screen juke_vbox:

    vbox:
        style "juke_vbox_style"

        textbutton "{b}A Jar of Copper Salts{/b} - {i}citb{/i}":
            action Play("music","sound/music/A Jar of Copper Salts - citb.ogg")
        textbutton "{b}REZURRECTA{/b} - {i}ASTRUM DEUS P1{/i}":
            action Play("music","sound/music/REZURRECTA - ASTRUM_DEUS_P1.ogg")
        textbutton "{b}LuckyLootCrate{/b} - {i}purple precipitation{/i}":
            action Play("music","sound/music/LuckyLootCrate - purple precipitation.ogg")
        textbutton "{b}PlugBoy{/b} - {i}paths{/i}":
            action Play("music","sound/music/PlugBoy - paths.ogg")
        textbutton "{b}TheSeanimator22{/b} - {i}Dinner at 7pm{/i}":
            action Play("music","sound/music/TheSeanimator22 - Dinner at 7pm.ogg")
        textbutton "{b}Gavimator{/b} - {i}the jungle{/i}":
            action Play("music","sound/music/Gavimator - the jungle.ogg"),Play("music","sound/music/Gavimator - the jungle intro.ogg"),Queue("music","sound/music/Gavimator - the jungle.ogg")
            # first, plays the main song
            # second, plays the song's intro, immediately cancelling the main song.
            # as a result, the player does not hear the main song.
            # however, the main song then gets queued, to play after the intro.
            # so, why play the main song first and immediately skip it?
            # the textbutton is programmed by the engine to display as active if its action condition is true.
            # this includes a played song, but not a queued song.
            # so, really, this is just so the button doesn't dismiss itself once the intro finishes playing.
            # took me a good hour to figure out this simple solution, but it's so much better than my first attempt
            # (which involved two new variables and a dummy button that replaced the existing button)
            # (bleh!)
            # anyway, that fix wasn't just spaghetti, it was also LESS FUNCTIONAL
            # because it subtly took away your ability to restart a song, for ONLY THAT SONG
        textbutton "{b}KrystalGhostz{/b} - {i}Breakfast Beat{/i}":
            action Play("music","sound/music/KrystalGhostz - Breakfast Beat.ogg")
        textbutton "{b}hewd{/b} - {i}For the Cake{/i}":
            action Play("music","sound/music/hewd - For the Cake.ogg")
        textbutton "{b}REZURRECTA{/b} - {i}ZAKU{/i}":
            action Play("music","sound/music/REZURRECTA - ZAKU.ogg")
        textbutton "{b}plebkingdom{/b} - {i}Break{/i}":
            action Play("music","sound/music/plebkingdom - Break.ogg")
        textbutton "{b}Nyakiye{/b} - {i}111{/i}":
            action Play("music","sound/music/Nyakiye - 111.ogg"),Play("music","sound/music/Nyakiye - 111 intro.ogg"),Queue("music","sound/music/Nyakiye - 111.ogg")
        textbutton "{b}LuckyLootCrate{/b} - {i}patience{/i}":
            action Play("music","sound/music/LuckyLootCrate - patience.ogg")
        textbutton "{b}tetroid{/b} - {i}Outro{/i}":
            action Play("music","sound/music/tetroid - Outro quieter.ogg")
        textbutton "{b}mintykiwi{/b} - {i}cdafafad{/i} {size=-5}(bonus track){/size}":
            action Play("music","sound/music/mintykiwi - cdafafadRemake.ogg")

        

style juke_vbox_style:
    xalign 0.5
    yalign 0.4

transform huepulse:
    matrixcolor HueMatrix(360) * BrightnessMatrix(0.0)
    easeout_cubic 1.5 matrixcolor HueMatrix(180) * BrightnessMatrix(0.4)
    easein_cubic 1.5 matrixcolor HueMatrix(0) * BrightnessMatrix(0.0)
    repeat
