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
    p "Excuse me?"
    neon "...I said as long as you're still browsing, you can talk to Jukebox in the corner and play some music."
    neon "Maybe you'll like one of them enough to purchase one."
    p "Sounds cool. I'll be sure to check it out."
    jump musicstore

label .sheet:
    show bg music
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
        p "Asking again probably wouldn't hurt."
    p "You wouldn't happen to know how to deliever a package safely, would you?"
    sheet "Nope."
    p "Yeah, that checks."
    sheet "To be honest, there's not much to do here other than listen to music."
    sheet "Unless you wanted to take a break and listen to music, you should probably finish delievering your package or something."
    p annoyed "OK mom."
    jump musicstore

label .jb:
    scene bg music
    show jb
    show posty neutral
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
    jb "Whether its the music in this game or some original music of my own, I can play it and swap out the music in this store!"
    show posty confused
    jb "I even have some remixed OSO tracks!"
    p confused "The music in this what?"
    jb "The music in this store."
    p neutral"Oh OK. Sorry for mishearing you."
    jb "That's OK, I get that all the time."
    jump .jb

label .tunes:
    "This feature is not yet available." #298 jukebox music player
    jump .jb