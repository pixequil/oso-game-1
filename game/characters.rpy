# File for defining characters

init python:
    # stop talking code taken from outdated wiki
  
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
    xalign -0.05
    pause 0.2
    "talksprites/posty/posty_neutral_close.png"
    pause 0.2
    repeat
image posty neutral quiet:
    "talksprites/posty/posty_neutral_close.png"
    xalign -0.05

image posty happy = WhileSpeaking(
    "posty", 
    "posty happy talk", 
    "posty happy quiet"
    )
image posty happy talk:
    "talksprites/posty/posty_happy_open.png"
    xalign -0.05
    pause 0.2
    "talksprites/posty/posty_happy_close.png"
    pause 0.2
    repeat
image posty happy quiet:
    "talksprites/posty/posty_happy_close.png"
    xalign -0.05

image posty sad = WhileSpeaking(
    "posty", 
    "posty sad talk", 
    "posty sad quiet"
    )
image posty sad talk:
    "talksprites/posty/posty_sad_open.png"
    xalign -0.05
    pause 0.2
    "talksprites/posty/posty_sad_close.png"
    pause 0.2
    repeat
image posty sad quiet:
    "talksprites/posty/posty_sad_close.png"
    xalign -0.05

image posty concerned = WhileSpeaking(
    "posty", 
    "posty concerned talk", 
    "posty concerned quiet"
    )
image posty concerned talk:
    "talksprites/posty/posty_concerned_open.png"
    xalign -0.05
    pause 0.2
    "talksprites/posty/posty_concerned_close.png"
    pause 0.2
    repeat
image posty concerned quiet:
    "talksprites/posty/posty_concerned_close.png"
    xalign -0.05

image posty confused = WhileSpeaking(
    "posty", 
    "posty confused talk", 
    "posty confused quiet"
    )
image posty confused talk:
    "talksprites/posty/posty_confused_open.png"
    xalign -0.05
    pause 0.2
    "talksprites/posty/posty_confused_close.png"
    pause 0.2
    repeat
image posty confused quiet:
    "talksprites/posty/posty_confused_close.png"
    xalign -0.05

image posty zany = WhileSpeaking(
    "posty", 
    "posty zany talk", 
    "posty zany quiet"
    )
image posty zany talk:
    "talksprites/posty/posty_zany_open.png"
    xalign -0.05
    pause 0.2
    "talksprites/posty/posty_zany_close.png"
    pause 0.2
    repeat
image posty zany quiet:
    "talksprites/posty/posty_zany_close.png"
    xalign -0.05

image posty angry = WhileSpeaking(
    "posty", 
    "posty angry talk", 
    "posty angry quiet"
    )
image posty angry talk:
    "talksprites/posty/posty_angry_open.png"
    xalign -0.05
    pause 0.2
    "talksprites/posty/posty_angry_close.png"
    pause 0.2
    repeat
image posty angry quiet:
    "talksprites/posty/posty_angry_close.png"
    xalign -0.05

image posty annoyed = WhileSpeaking(
    "posty", 
    "posty annoyed talk", 
    "posty annoyed quiet"
    )
image posty annoyed talk:
    "talksprites/posty/posty_annoyed_open.png"
    xalign -0.05
    pause 0.2
    "talksprites/posty/posty_annoyed_close.png"
    pause 0.2
    repeat
image posty annoyed quiet:
    "talksprites/posty/posty_annoyed_close.png"
    xalign -0.05

image posty astonished = WhileSpeaking(
    "posty", 
    "posty astonished talk", 
    "posty astonished quiet"
    )
image posty astonished talk:
    "talksprites/posty/posty_astonished_close.png"
    xalign -0.05
    pause 0.2
    "talksprites/posty/posty_astonished_open.png"
    pause 0.2
    repeat
image posty astonished quiet:
    "talksprites/posty/posty_astonished_close.png"
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
    xalign -0.05
image posty astonished anim:
    xalign -0.05
    function anims.posty.astonished.reset

    block:
        "talksprites/posty/posty_astonished_anim_[anims.posty.astonished.frame].png"
        function anims.posty.astonished.advance
        pause anims.posty.astonished.wait
        repeat

init python:
    def is_popped_True(t, st, at):
        global is_popped
        global animation_frame_toasty
        if not ('is_popped' in globals()):
            is_popped = True
        if is_popped != True:
            is_popped = True
            animation_frame_toasty = 1
        else:
            animation_frame_toasty = 0

    def is_popped_False(t, st, at):
        global is_popped
        global animation_frame_toasty
        if not ('is_popped' in globals()):
            is_popped = False
        if is_popped != False:
            is_popped = False
            animation_frame_toasty = 1
        else:
            animation_frame_toasty = 0

    def next_frame_toasty(t, st, at):
        global animation_frame_toasty
        if animation_frame_toasty < 5 and animation_frame_toasty > 0:
            animation_frame_toasty += 1
        else:
            animation_frame_toasty = 0

    def clear_toasty_transition():
        if ('is_popped' in globals()):
            global is_popped
            del is_popped

define t = Character("Toasty",
    callback=speaker("toasty"), 
    image="toasty", 
    who_color="#c8a28b"
    )

image toasty neutral = WhileSpeaking(
    "toasty", 
    "toasty neutral talk",
    "toasty neutral quiet"
    )
image toasty neutral talk:
    xalign 1.0
    function is_popped_False
    parallel:
        pause 0.04
        function next_frame_toasty
        repeat
    parallel:
        block:
            "talksprites/toasty/toasty_neutral_close_[animation_frame_toasty].png"
            pause 0.04
            repeat 5
        block:
            "talksprites/toasty/toasty_neutral_open_[animation_frame_toasty].png"
            pause 0.04
            repeat 5
        repeat
image toasty neutral quiet:
    xalign 1.0
    function is_popped_False
    block:
        "talksprites/toasty/toasty_neutral_close_[animation_frame_toasty].png"
        pause 0.04
        function next_frame_toasty
        repeat 6

image toasty neutral2 = WhileSpeaking(
    "toasty", 
    "toasty neutral2 talk",
    "toasty neutral2 quiet"
    )
image toasty neutral2 talk:
    xalign 1.0
    function is_popped_False
    parallel:
        pause 0.04
        function next_frame_toasty
        repeat
    parallel:
        block:
            "talksprites/toasty/toasty_neutral2_close2_[animation_frame_toasty].png"
            pause 0.04
            repeat 5
        block:
            "talksprites/toasty/toasty_neutral2_open_[animation_frame_toasty].png"
            pause 0.04
            repeat 5
        repeat
image toasty neutral2 quiet:
    xalign 1.0
    function is_popped_False
    block:
        "talksprites/toasty/toasty_neutral2_close_[animation_frame_toasty].png"
        pause 0.04
        function next_frame_toasty
        repeat 6

image toasty smug = WhileSpeaking(
    "toasty", 
    "toasty smug talk", 
    "toasty smug quiet"
    )
image toasty smug talk:
    xalign 1.0
    function is_popped_True
    parallel:
        pause 0.04
        function next_frame_toasty
        repeat
    parallel:
        block:
            "talksprites/toasty/toasty_smug_close_[animation_frame_toasty].png"
            pause 0.04
            repeat 5
        block:
            "talksprites/toasty/toasty_smug_open_[animation_frame_toasty].png"
            pause 0.04
            repeat 5
        repeat
image toasty smug quiet:
    xalign 1.0
    function is_popped_True
    block:
        "talksprites/toasty/toasty_smug_close_[animation_frame_toasty].png"
        pause 0.04
        function next_frame_toasty
        repeat 6

image toasty smug2 = WhileSpeaking(
    "toasty", 
    "toasty smug2 talk", 
    "toasty smug2 quiet"
    )
image toasty smug2 talk:
    xalign 1.0
    function is_popped_True
    parallel:
        pause 0.04
        function next_frame_toasty
        repeat
    parallel:
        block:
            "talksprites/toasty/toasty_smug2_close_[animation_frame_toasty].png"
            pause 0.04
            repeat 5
        block:
            "talksprites/toasty/toasty_smug2_open_[animation_frame_toasty].png"
            pause 0.04
            repeat 5
        repeat
image toasty smug2 quiet:
    xalign 1.0
    function is_popped_True
    block:
        "talksprites/toasty/toasty_smug2_close_[animation_frame_toasty].png"
        pause 0.04
        function next_frame_toasty
        repeat 6

image toasty smug3 = WhileSpeaking(
    "toasty", 
    "toasty smug3 talk", 
    "toasty smug3 quiet"
    )
image toasty smug3 talk:
    xalign 1.0
    function is_popped_True
    parallel:
        pause 0.04
        function next_frame_toasty
        repeat
    parallel:
        block:
            "talksprites/toasty/toasty_smug3_close_[animation_frame_toasty].png"
            pause 0.04
            repeat 5
        block:
            "talksprites/toasty/toasty_smug3_open_[animation_frame_toasty].png"
            pause 0.04
            repeat 5
        repeat
image toasty smug3 quiet:
    xalign 1.0
    function is_popped_True
    block:
        "talksprites/toasty/toasty_smug3_close_[animation_frame_toasty].png"
        pause 0.04
        function next_frame_toasty
        repeat 6

image toasty smug4:
    xalign 1.0
    function is_popped_True
    block:
        "talksprites/toasty/toasty_smug4_[animation_frame_toasty].png"
        pause 0.04
        function next_frame_toasty
        repeat 6

image toasty smug5 = WhileSpeaking(
    "toasty", 
    "toasty smug5 talk", 
    "toasty smug5 quiet"
    )
image toasty smug5 talk:
    xalign 1.0
    function is_popped_True
    parallel:
        pause 0.04
        function next_frame_toasty
        repeat
    parallel:
        block:
            "talksprites/toasty/toasty_smug5_close_[animation_frame_toasty].png"
            pause 0.04
            repeat 5
        block:
            "talksprites/toasty/toasty_smug5_open_[animation_frame_toasty].png"
            pause 0.04
            repeat 5
        repeat
image toasty smug5 quiet:
    xalign 1.0
    function is_popped_True
    block:
        "talksprites/toasty/toasty_smug5_close_[animation_frame_toasty].png"
        pause 0.04
        function next_frame_toasty
        repeat 6

image toasty angry = WhileSpeaking(
    "toasty", 
    "toasty angry talk", 
    "toasty angry quiet"
    )
image toasty angry talk:
    xalign 1.0
    function is_popped_False
    parallel:
        pause 0.04
        function next_frame_toasty
        repeat
    parallel:
        block:
            "talksprites/toasty/toasty_angry_close2_[animation_frame_toasty].png"
            pause 0.04
            repeat 5
        block:
            "talksprites/toasty/toasty_angry_open_[animation_frame_toasty].png"
            pause 0.04
            repeat 5
        repeat
image toasty angry quiet:
    xalign 1.0
    function is_popped_False
    block:
        "talksprites/toasty/toasty_angry_close_[animation_frame_toasty].png"
        pause 0.04
        function next_frame_toasty
        repeat 6

image toasty annoyed = WhileSpeaking(
    "toasty", 
    "toasty annoyed talk", 
    "toasty annoyed quiet"
    )
image toasty annoyed talk:
    xalign 1.0
    function is_popped_False
    parallel:
        pause 0.04
        function next_frame_toasty
        repeat
    parallel:
        block:
            "talksprites/toasty/toasty_annoyed_close_[animation_frame_toasty].png"
            pause 0.04
            repeat 5
        block:
            "talksprites/toasty/toasty_annoyed_open_[animation_frame_toasty].png"
            pause 0.04
            repeat 5
        repeat
image toasty annoyed quiet:
    xalign 1.0
    function is_popped_False
    block:
        "talksprites/toasty/toasty_annoyed_close_[animation_frame_toasty].png"
        pause 0.04
        function next_frame_toasty
        repeat 6

image toasty crossedarms = WhileSpeaking(
    "toasty", 
    "toasty crossedarms talk", 
    "toasty crossedarms quiet"
    )
image toasty crossedarms talk:
    xalign 1.0
    function is_popped_False
    parallel:
        pause 0.04
        function next_frame_toasty
        repeat
    parallel:
        block:
            "talksprites/toasty/toasty_crossedarms_close_[animation_frame_toasty].png"
            pause 0.04
            repeat 5
        block:
            "talksprites/toasty/toasty_crossedarms_open_[animation_frame_toasty].png"
            pause 0.04
            repeat 5
        repeat
image toasty crossedarms quiet:
    xalign 1.0
    function is_popped_False
    block:
        "talksprites/toasty/toasty_crossedarms_close_[animation_frame_toasty].png"
        pause 0.04
        function next_frame_toasty
        repeat 6

image toasty enthused = WhileSpeaking(
    "toasty", 
    "toasty enthused talk", 
    "toasty enthused quiet"
    )
image toasty enthused talk:
    xalign 1.0
    function is_popped_False
    parallel:
        pause 0.04
        function next_frame_toasty
        repeat
    parallel:
        block:
            "talksprites/toasty/toasty_enthused_close_[animation_frame_toasty].png"
            pause 0.04
            repeat 5
        block:
            "talksprites/toasty/toasty_enthused_open_[animation_frame_toasty].png"
            pause 0.04
            repeat 5
        repeat
image toasty enthused quiet:
    xalign 1.0
    function is_popped_False
    block:
        "talksprites/toasty/toasty_enthused_close_[animation_frame_toasty].png"
        pause 0.04
        function next_frame_toasty
        repeat 6

image toasty laugh = WhileSpeaking(
    "toasty", 
    "toasty laugh talk", 
    "toasty laugh quiet"
    )
image toasty laugh talk:
    xalign 1.0
    function is_popped_False
    parallel:
        pause 0.04
        function next_frame_toasty
        repeat
    parallel:
        block:
            "talksprites/toasty/toasty_laugh_close_[animation_frame_toasty].png"
            pause 0.04
            repeat 5
        block:
            "talksprites/toasty/toasty_laugh_open_[animation_frame_toasty].png"
            pause 0.04
            repeat 5
        repeat
image toasty laugh quiet:
    xalign 1.0
    function is_popped_False
    block:
        "talksprites/toasty/toasty_laugh_close_[animation_frame_toasty].png"
        pause 0.04
        function next_frame_toasty
        repeat 6

image toasty pointandlaugh = WhileSpeaking(
    "toasty", 
    "toasty pointandlaugh talk", 
    "toasty pointandlaugh quiet"
    )
image toasty pointandlaugh talk:
    xalign 1.0
    function is_popped_False
    parallel:
        pause 0.04
        function next_frame_toasty
        repeat
    parallel:
        block:
            "talksprites/toasty/toasty_pointandlaugh_close_[animation_frame_toasty].png"
            pause 0.04
            repeat 5
        block:
            "talksprites/toasty/toasty_pointandlaugh_open_[animation_frame_toasty].png"
            pause 0.04
            repeat 5
        repeat
image toasty pointandlaugh quiet:
    xalign 1.0
    function is_popped_False
    block:
        "talksprites/toasty/toasty_pointandlaugh_close_[animation_frame_toasty].png"
        pause 0.04
        function next_frame_toasty
        repeat 6

image toasty turned = WhileSpeaking(
    "toasty", 
    "toasty turned talk", 
    "toasty turned quiet"
    )
image toasty turned talk:
    xalign 1.0
    function is_popped_False
    parallel:
        pause 0.04
        function next_frame_toasty
        repeat
    parallel:
        block:
            "talksprites/toasty/toasty_turned_close_[animation_frame_toasty].png"
            pause 0.04
            repeat 5
        block:
            "talksprites/toasty/toasty_turned_open_[animation_frame_toasty].png"
            pause 0.04
            repeat 5
        repeat
image toasty turned quiet:
    xalign 1.0
    function is_popped_False
    block:
        "talksprites/toasty/toasty_turned_close_[animation_frame_toasty].png"
        pause 0.04
        function next_frame_toasty
        repeat 6

image toasty turned2 = WhileSpeaking(
    "toasty", 
    "toasty turned2 talk", 
    "toasty turned2 quiet"
    )
image toasty turned2 talk:
    xalign 1.0
    function is_popped_False
    parallel:
        pause 0.04
        function next_frame_toasty
        repeat
    parallel:
        block:
            "talksprites/toasty/toasty_turned2_close_[animation_frame_toasty].png"
            pause 0.04
            repeat 5
        block:
            "talksprites/toasty/toasty_turned2_open_[animation_frame_toasty].png"
            pause 0.04
            repeat 5
        repeat
image toasty turned2 quiet:
    xalign 1.0
    function is_popped_False
    block:
        "talksprites/toasty/toasty_turned2_close_[animation_frame_toasty].png"
        pause 0.04
        function next_frame_toasty
        repeat 6




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
#    zoom 0.9
    xalign 1.0
    pause 0.2
    "talksprites/brandsoda_close.png"
    pause 0.2
    repeat
image bs quiet:
    "talksprites/brandsoda_close.png"
#    zoom 0.9
    xalign 1.0

image bs follow = WhileSpeaking(
    "bs", 
    "bs follow talk", 
    "bs follow quiet"
    )
image bs follow talk:
    "talksprites/brandsoda_open.png"
    xzoom -1.0
#    zoom 0.9
    xalign 0.35
    pause 0.2
    "talksprites/brandsoda_close.png"
    pause 0.2
    repeat
image bs follow quiet:
    "talksprites/brandsoda_close.png"
    xzoom -1.0
#    zoom 0.9
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

image cameron = WhileSpeaking(
    "cameron",
    "cameron talk",
    "cameron quiet"
)

image cameron quiet:
    "talksprites/security_cameron.png"
    zoom 0.45
    xcenter 0.8

image cameron talk:
    "talksprites/security_cameron.png"
    xzoom 0.45
    yzoom 0.45
    xcenter 0.8

    block:
        parallel:
            easein_elastic 0.4 xzoom (0.45 + 0.02)
        parallel:
            easein_elastic 0.4 yzoom (0.45 - 0.02)

        pause 0.05


        parallel:
            easein_elastic 0.4 xzoom (0.45 - 0.02)
        parallel:
            easein_elastic 0.4 yzoom (0.45 + 0.02)

        pause 0.05

        repeat

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
        "Toasty sprites.":
            jump .toasty
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
    hide bs
    show cameron
    cameron "Hello, I'm Security Camera, but they call me Security Cameron."
    p neutral "Hello, Security Cameron."

label .toasty:

    hide yd
    $ clear_toasty_transition()
    show toasty neutral
    t "I'm toasty and this is my neutral expression."
    t smug "When I have a smug expression my toast pops."
    p "ok"
    t smug2 "This is another one."
    show toasty neutral
    p "What happens if you shift expressions when you're not saying anything?"
    show toasty smug4
    p "Does it still animate?"
    show toasty neutral
    p "Looks like it does."
    t smug2 "Leaving"
    hide toasty
    p quiet "..."
    $ clear_toasty_transition()
    show toasty enthused
    t "and coming back with my toast in a different state doesn't play the animation."
    t annoyed "Well, actually the state of my toast isn't automatically thrown out when I'm hidden, so by default it does still play."
    t neutral2 "You have to put \"$ clear_toasty_transition()\" before showing me in order to prevent the transition."
    t neutral "Going from not smug to smug with a hide in between"
    hide toasty
    p quiet "..."
    $ clear_toasty_transition()
    show toasty smug5
    t "Can also be made to not play the animation."
    p neutral "So, what different expressions you have?"
    t neutral "Well there's neutral,"
    t neutral2 "the other neutral (neutral2),"
    t smug "smug,"
    t smug2 "smug explainy (smug2),"
    t smug3 "a secret third smug expression (smug3),"
    t smug4 "{i}this one which doesn't have lip sync (smug4),{/i}"
    t smug5 "smug with my eyes closed (smug5),"
    t annoyed "this sort of annoyed bashful expression (annoyed),"
    t laugh "laughing I guess? (laugh),"
    t enthused "enthused,"
    t pointandlaugh "pointing and laughing (pointandlaugh),"
    t turned "looking in the other direction (turned),"
    t turned2 "pretending I'm not paying attention (turned2),"
    t angry "angry,"
    t crossedarms "and then this one where I'm crossing my arms (crossedarms)."

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


    