# File for defining characters

init python: # stop talking code taken from outdated wiki
  
    # This is set to the name of the character that is speaking, or
    # None if no character is currently speaking.
    speaking = None
  
    # This returns speaking if the character is speaking, and done if the
    # character is not.
    def while_speaking(name, speak_d, done_d, st, at):
        if speaking == name:
            return speak_d, .1
        else:
            return done_d, None
  
    # Curried form of the above.
    curried_while_speaking = renpy.curry(while_speaking)
  
    # Displays speaking when the named character is speaking, and done otherwise.
    def WhileSpeaking(name, speaking_d, done_d=Null()):
        return DynamicDisplayable(curried_while_speaking(name, speaking_d, done_d))
  
    # This callback maintains the speaking variable.
    def speaker_callback(name, event, **kwargs):
        global speaking
       
        if event == "show":
            speaking = name
        # elif event == "slow_done":
        #     speaking = None
        elif event == "end":
            speaking = None
  
    # Curried form of the same.
    speaker = renpy.curry(speaker_callback)

### CHARACTERS ###

define p = Character("Posty", 
    callback=speaker("posty"), 
    image="posty", 
    who_color="#5581c1"
    )

image posty neutral = WhileSpeaking(
    "posty", 
    "posty neutral talk", 
    "posty neutral quiet"
    )
image posty neutral talk:
    "talksprites/posty/posty_neutral_open.png"
    zoom 2.2
    xalign -0.05
    pause 0.2
    "talksprites/posty/posty_neutral_close.png"
    pause 0.2
    repeat
image posty neutral quiet:
    "talksprites/posty/posty_neutral_close.png"
    zoom 2.2
    xalign -0.05

image posty happy = WhileSpeaking(
    "posty", 
    "posty happy talk", 
    "posty happy quiet"
    )
image posty happy talk:
    "talksprites/posty/posty_happy_open.png"
    zoom 2.2
    xalign -0.05
    pause 0.2
    "talksprites/posty/posty_happy_close.png"
    pause 0.2
    repeat
image posty happy quiet:
    "talksprites/posty/posty_happy_close.png"
    zoom 2.2
    xalign -0.05

image posty sad = WhileSpeaking(
    "posty", 
    "posty sad talk", 
    "posty sad quiet"
    )
image posty sad talk:
    "talksprites/posty/posty_sad_open.png"
    zoom 2.2
    xalign -0.05
    pause 0.2
    "talksprites/posty/posty_sad_close.png"
    pause 0.2
    repeat
image posty sad quiet:
    "talksprites/posty/posty_sad_close.png"
    zoom 2.2
    xalign -0.05

image posty concerned = WhileSpeaking(
    "posty", 
    "posty concerned talk", 
    "posty concerned quiet"
    )
image posty concerned talk:
    "talksprites/posty/posty_concerned_open.png"
    zoom 2.2
    xalign -0.05
    pause 0.2
    "talksprites/posty/posty_concerned_close.png"
    pause 0.2
    repeat
image posty concerned quiet:
    "talksprites/posty/posty_concerned_close.png"
    zoom 2.2
    xalign -0.05

image posty confused = WhileSpeaking(
    "posty", 
    "posty confused talk", 
    "posty confused quiet"
    )
image posty confused talk:
    "talksprites/posty/posty_confused_open.png"
    zoom 2.2
    xalign -0.05
    pause 0.2
    "talksprites/posty/posty_confused_close.png"
    pause 0.2
    repeat
image posty confused quiet:
    "talksprites/posty/posty_confused_close.png"
    zoom 2.2
    xalign -0.05

image posty zany = WhileSpeaking(
    "posty", 
    "posty zany talk", 
    "posty zany quiet"
    )
image posty zany talk:
    "talksprites/posty/posty_zany_open.png"
    zoom 2.2
    xalign -0.05
    pause 0.2
    "talksprites/posty/posty_zany_close.png"
    pause 0.2
    repeat
image posty zany quiet:
    "talksprites/posty/posty_zany_close.png"
    zoom 2.2
    xalign -0.05

image posty angry = WhileSpeaking(
    "posty", 
    "posty angry talk", 
    "posty angry quiet"
    )
image posty angry talk:
    "talksprites/posty/posty_angry_open.png"
    zoom 2.2
    xalign -0.05
    pause 0.2
    "talksprites/posty/posty_angry_close.png"
    pause 0.2
    repeat
image posty angry quiet:
    "talksprites/posty/posty_angry_close.png"
    zoom 2.2
    xalign -0.05

image posty annoyed = WhileSpeaking(
    "posty", 
    "posty annoyed talk", 
    "posty annoyed quiet"
    )
image posty annoyed talk:
    "talksprites/posty/posty_annoyed_open.png"
    zoom 2.2
    xalign -0.05
    pause 0.2
    "talksprites/posty/posty_annoyed_close.png"
    pause 0.2
    repeat
image posty annoyed quiet:
    "talksprites/posty/posty_annoyed_close.png"
    zoom 2.2
    xalign -0.05

image posty astonished = WhileSpeaking(
    "posty", 
    "posty astonished talk", 
    "posty astonished quiet"
    )
image posty astonished talk:
    "talksprites/posty/posty_astonished_close.png"
    zoom 2.2
    xalign -0.05
    pause 0.2
    "talksprites/posty/posty_astonished_open.png"
    pause 0.2
    repeat
image posty astonished quiet:
    "talksprites/posty/posty_astonished_close.png"
    zoom 2.2
    xalign -0.05

init python:
    class FBFAnimation():
        """Represent a frame-by-frame animation, which only plays once."""

        def __init__(self, num_frames, framerate):
            self.num_frames = num_frames
            self.wait = 1 / framerate

            self.reset()

        def reset(self, *args): # We don't care about the arguments
            self.frame = 1

        def advance(self, *args): # Same with here
            if self.num_frames != self.frame:
                self.frame += 1

define anims.posty.astonished = FBFAnimation(18, 24)

image posty astonished before:
    "talksprites/posty/posty_astonished_anim_1.png"
    zoom 2.2
    xalign -0.05
image posty astonished anim:
    zoom 2.2
    xalign -0.05
    function anims.posty.astonished.reset

    block:
        "talksprites/posty/posty_astonished_anim_[anims.posty.astonished.frame].png"
        function anims.posty.astonished.advance
        pause anims.posty.astonished.wait
        repeat



define t = Character("Toasty",  # TODO: #14 toasty sprites (she needs plenty)
    callback=speaker("toasty"), 
    image="toasty", 
    who_color="#c8a28b"
    )





define yd = Character("Yellow Diamond", 
    callback=speaker("yd"), 
    image="yd", 
    who_color="#ffff00"
    )

image yd = WhileSpeaking(
    "yd", 
    "yd talk", 
    "yd quiet"
    )
image yd talk:
    "talksprites/yd_open.png"
    zoom 1.2
    xalign 1.0
    yalign 0.0
    pause 0.2
    "talksprites/yd_close.png"
    pause 0.2
    repeat
image yd quiet:
    "talksprites/yd_close.png"
    zoom 1.2
    xalign 1.0
    yalign 0.0


define btnet = Character("B.T. Net", 
    image="btnet", 
    who_color="#ff8aa7"
    )

image btnet:
    "talksprites/btnet.png"
    zoom 1.4
    xalign 1.0


define bs = Character("Brand Soda", 
    callback=speaker("bs"), 
    image="bs", 
    who_color="#df7dff"
    )

image bs = WhileSpeaking(
    "bs", 
    "bs talk", 
    "bs quiet"
    )
image bs talk:
    "talksprites/brandsoda_open.png"
    zoom 1.2
    xalign 1.0
    pause 0.2
    "talksprites/brandsoda_close.png"
    pause 0.2
    repeat
image bs quiet:
    "talksprites/brandsoda_close.png"
    zoom 1.2
    xalign 1.0

image bs follow = WhileSpeaking(
    "bs", 
    "bs follow talk", 
    "bs follow quiet"
    )
image bs follow talk:
    "talksprites/brandsoda_open.png"
    xzoom -1.0
    zoom 1.2
    xalign 0.35
    pause 0.2
    "talksprites/brandsoda_close.png"
    pause 0.2
    repeat
image bs follow quiet:
    "talksprites/brandsoda_close.png"
    xzoom -1.0
    zoom 1.2
    xalign 0.35


define bonbon = Character("Bon-Bon", 
    callback=speaker("bonbon"), 
    image="bonbon", 
    who_color="#65a9d2"
    )

image bonbon = WhileSpeaking(
    "bonbon", 
    "bonbon talk", 
    "bonbon quiet"
    )
image bonbon talk:
    "talksprites/bonbon_open.png"
    zoom 1.2
    xalign 1.1
    pause 0.2
    "talksprites/bonbon_close.png"
    pause 0.2
    repeat
image bonbon quiet:
    "talksprites/bonbon_close.png"
    zoom 1.2
    xalign 1.1


define sgummy = Character("Sour Gummy", 
    callback=speaker("sgummy"), 
    image="sgummy", 
    who_color="#fd85ed"
    )

image sgummy = WhileSpeaking(
    "sgummy", 
    "sgummy talk", 
    "sgummy quiet"
    )
image sgummy talk:
    "talksprites/sourgummy_open.png"
    zoom 1.2
    xzoom -1.0
    xalign 0.75
    pause 0.2
    "talksprites/sourgummy_close.png"
    pause 0.2
    repeat
image sgummy quiet:
    "talksprites/sourgummy_close.png"
    zoom 1.2
    xzoom -1.0
    xalign 0.75


define retainer = Character("Retainer", 
    callback=speaker("retainer"), 
    image="retainer", 
    who_color="#fc809d"
    )

image retainer sad = WhileSpeaking(
    "retainer", 
    "retainer sad talk", 
    "retainer sad quiet"
    )
image retainer sad talk:
    "talksprites/retainer_sad_open.png"
    zoom 1.2
    xzoom -1.0
    xalign 1.0
    pause 0.2
    "talksprites/retainer_sad_close.png"
    pause 0.2
    repeat
image retainer sad quiet:
    "talksprites/retainer_sad_close.png"
    zoom 1.2
    xzoom -1.0
    xalign 1.0

image retainer happy = WhileSpeaking(
    "retainer", 
    "retainer happy talk", 
    "retainer happy quiet"
    )
image retainer happy talk:
    "talksprites/retainer_happy_open.png"
    zoom 1.2
    xzoom -1.0
    xalign 1.0
    pause 0.2
    "talksprites/retainer_happy_close.png"
    pause 0.2
    repeat
image retainer happy quiet:
    "talksprites/retainer_happy_close.png"
    zoom 1.2
    xzoom -1.0
    xalign 1.0

image retainer crying = WhileSpeaking(
    "retainer", 
    "retainer crying talk", 
    "retainer crying quiet"
    )
image retainer crying talk:
    "talksprites/retainer_crying.png"
    zoom 1.2
    xzoom -1.0
    xalign 1.0
    yalign 1.05
    pause 0.2
    "talksprites/retainer_crying.png"
    yalign 1.0
    pause 0.2
    repeat
image retainer crying quiet:
    "talksprites/retainer_crying.png"
    zoom 1.2
    xzoom -1.0
    xalign 1.0


define cameron = Character("Security Cameron",
    callback=speaker("cameron"), 
    image="cameron", 
    who_color="#b7aea8"
    )


define redtile = Character("Red Tile", 
    callback=speaker("redtile"), 
    image="redtile", 
    who_color="#ff0000"
    )

image redtile = WhileSpeaking(
    "redtile", 
    "redtile talk", 
    "redtile quiet"
    )
image redtile talk:
    "talksprites/redtile_open.png"
    zoom 1.2
    xalign 1.0
    yalign 1.7
    pause 0.2
    "talksprites/redtile_close.png"
    pause 0.2
    repeat
image redtile quiet:
    "talksprites/redtile_close.png"
    zoom 1.2
    xalign 1.0
    yalign 1.7


define dolly = Character("Dolly", 
    callback=speaker("dolly"), 
    image="dolly", 
    who_color="#e3d3ab"
    )

image dolly = WhileSpeaking(
    "dolly", 
    "dolly talk", 
    "dolly quiet"
    )
image dolly talk:
    "talksprites/dolly_open.png"
    zoom 2.0
    xzoom -1.0
    xalign 1.3
    pause 0.2
    "talksprites/dolly_close.png"
    pause 0.2
    repeat
image dolly quiet:
    "talksprites/dolly_idle.png"
    zoom 2.0
    xzoom -1.0
    xalign 1.3


define miso = Character("Miso Soup",
    callback=speaker("miso"), 
    image="miso", 
    who_color="#ab9d67"
    )



# Non-canonical scene for testing stuff. Players should never see this in the final game.

label chartest:

    scene bg room with fade

    show posty neutral
    show yd
    yd "Welcome to the character test room. Pick a thing to test."

    menu:
        "Posty sprites.":
            jump .posty
        "Other characters.":
            jump .other

label .other:

    p "Other people!"
    yd "K, well I'm Yellow Diamond. You already knew that part."
    yd "Time to take my leave!"
    hide yd
    show btnet
    btnet "Hi, I'm B.T. Net!"
    hide btnet
    show dolly
    p "Hi Dolly. This is what you look like when you're not speaking. Also I just wanna test where the text wraps just out of curiosity."
    dolly "That's right. And this is what I look like when I {i}am{/i} speaking."
    p "Damn!"
    hide dolly
    show redtile
    redtile "Hi I'm Red Tile."
    hide redtile
    show retainer sad
    retainer "I'm Retainer, and I'm sad."
    retainer happy "Now I'm happy!"
    show retainer crying with hpunch
    retainer "Now I'm crying!!!"
    hide retainer
    show bonbon
    show sgummy behind bonbon
    bonbon "I'm Bon-Bon!"
    sgummy "And I'm Sour Gummy."
    hide bonbon
    hide sgummy
    show bs behind posty
    bs "Hi, I'm Brand Soda!"
#    show bs follow
    show bs follow with move:
        xalign 0.35
    bs "And now I'm next to you!"
    p astonished "Aaah!"
#    show bs -follow
    show bs with move:
        xalign 1.0
    bs "Okay I stopped being next to you."
    p neutral "Good."

label .posty:

    p "Meee!!!"
    yd "Cool, you can at least talk."
    p "Well, what if I want to have an inner monologue?"
    p quiet "{i}How's this?{/i}"
    yd "I heard that"
    p astonished before "..."
    p astonished anim "..!"
    p -anim "How..?!"
    yd "Dunno."
    p neutral "Well, never mind that. {w} Let's demonstrate my different expressions, yeah?"
    yd "Sounds like a plan!"
    p "So, this one's called neutral."
    p happy "Happy!"
    p sad "Sad."
    p angry "Angry..!"
    p annoyed "Annoyed."
    p astonished "Astonished, if you remember."
    p astonished anim "And astonished comes with an animation, too."
    p confused "Confused?"
    p concerned "Concerned..."
    p zany "ZANY!!1"
    yd "What was that last one?"
    p "USE THIS ONE SPARINGLY!!!!11"


    