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
  
    # Create a channel for speaking sounds
    renpy.music.register_channel("speak", tight=True, file_prefix="sound/voices/")

    # This callback maintains the speaking variable.
    def speaker_callback(name, event, sound_file="snd-txt1.mp3", interact=True, **kwargs):
        global speaking
        
        # Responsible for talking animations
        if event == "show":
            speaking = name
        # elif event == "slow_done":
        #     speaking = None
        elif event == "end":
            speaking = None

        # Do a boopy voice
        if not interact:
            return

        if event == "show_done":
            renpy.sound.play(sound_file, loop=True, channel="speak")
        elif event == "slow_done":
            renpy.sound.stop(channel="speak", fadeout=0.05)
  
    # Curried form of the same.
    speaker = renpy.curry(speaker_callback)

# Animation system
init python:
    class FBFAnimation():
        """Represent a frame-by-frame animation."""

        def __init__(self, num_frames, framerate, *, reset_after=False, reset_frame=1):
            self.num_frames = num_frames
            self.wait = 1 / framerate
            self.reset_frame = reset_frame
            self.reset_after = reset_after

            self.reset()

        def reset(self, *args): # We don't care about the arguments
            self.frame = self.reset_frame

        def advance(self, *args): # Same with here
            if self.frame < self.num_frames and self.frame > 0:
                self.frame += 1
            elif self.reset_after:
                self.reset()

### CHARACTERS ###

define p = Character("Posty", 
    callback=speaker("posty", sound_file="undertalevoicetest_posty_2_fix.wav"),
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
    "talksprites/posty/posty_neutral.png"
    pause 0.2
    repeat
image posty neutral quiet:
    "talksprites/posty/posty_neutral.png"
    xalign -0.05

    block:
        "talksprites/posty/posty_neutral.png"
        pause 2.0
        "talksprites/posty/posty_neutral_blink.png"
        pause 0.125
        repeat

image posty happy = WhileSpeaking(
    "posty", 
    "posty happy talk", 
    "posty happy quiet"
    )
image posty happy talk:
    "talksprites/posty/posty_happy_open.png"
    xalign -0.05
    pause 0.2
    "talksprites/posty/posty_happy.png"
    pause 0.2
    repeat
image posty happy quiet:
    "talksprites/posty/posty_happy.png"
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
    "talksprites/posty/posty_sad.png"
    pause 0.2
    repeat
image posty sad quiet:
    "talksprites/posty/posty_sad.png"
    xalign -0.05

    block:
        "talksprites/posty/posty_sad.png"
        pause 2.0
        "talksprites/posty/posty_sad_blink.png"
        pause 0.125
        repeat

image posty concerned = WhileSpeaking(
    "posty", 
    "posty concerned talk", 
    "posty concerned quiet"
    )
image posty concerned talk:
    "talksprites/posty/posty_concerned_open.png"
    xalign -0.05
    pause 0.2
    "talksprites/posty/posty_concerned.png"
    pause 0.2
    repeat
image posty concerned quiet:
    "talksprites/posty/posty_concerned.png"
    xalign -0.05

    block:
        "talksprites/posty/posty_concerned.png"
        pause 2.0
        "talksprites/posty/posty_concerned_blink.png"
        pause 0.125
        repeat

image posty confused = WhileSpeaking(
    "posty", 
    "posty confused talk", 
    "posty confused quiet"
    )
image posty confused talk:
    "talksprites/posty/posty_confused_open.png"
    xalign -0.05
    pause 0.2
    "talksprites/posty/posty_confused.png"
    pause 0.2
    repeat
image posty confused quiet:
    "talksprites/posty/posty_confused.png"
    xalign -0.05

    block:
        "talksprites/posty/posty_confused.png"
        pause 2.0
        "talksprites/posty/posty_confused_blink.png"
        pause 0.125
        repeat

image posty zany = WhileSpeaking(
    "posty", 
    "posty zany talk", 
    "posty zany quiet"
    )
image posty zany talk:
    "talksprites/posty/posty_zany_open.png"
    xalign -0.05
    pause 0.2
    "talksprites/posty/posty_zany.png"
    pause 0.2
    repeat
image posty zany quiet:
    "talksprites/posty/posty_zany.png"
    xalign -0.05

define anims.posty.angry = FBFAnimation(22, 24)

image posty angry = WhileSpeaking(
    "posty", 
    "posty angry talk", 
    "posty angry quiet"
    )
image posty angry talk:
    "talksprites/posty/posty_angry_open.png"
    xalign -0.05
    pause 0.2
    "talksprites/posty/posty_angry.png"
    pause 0.2
    repeat
image posty angry quiet:
    "talksprites/posty/posty_angry.png"
    xalign -0.05

    block:
        "talksprites/posty/posty_angry.png"
        pause 2.0
        "talksprites/posty/posty_angry_blink.png"
        pause 0.125
        "talksprites/posty/posty_angry.png"
        pause 2.0

        block:
            function anims.posty.angry.reset
            block:
                "talksprites/posty/posty_angry_anim_[anims.posty.angry.frame].png"
                function anims.posty.angry.advance
                pause anims.posty.angry.wait
                repeat anims.posty.angry.num_frames

            repeat 2

        repeat

image posty annoyed = WhileSpeaking(
    "posty", 
    "posty annoyed talk", 
    "posty annoyed quiet"
    )
image posty annoyed talk:
    "talksprites/posty/posty_annoyed_open.png"
    xalign -0.05
    pause 0.2
    "talksprites/posty/posty_annoyed.png"
    pause 0.2
    repeat
image posty annoyed quiet:
    "talksprites/posty/posty_annoyed.png"
    xalign -0.05

    block:
        "talksprites/posty/posty_annoyed.png"
        pause 2.0
        "talksprites/posty/posty_annoyed_blink.png"
        pause 0.125
        repeat

image posty astonished = WhileSpeaking(
    "posty", 
    "posty astonished talk", 
    "posty astonished quiet"
    )
image posty astonished talk:
    "talksprites/posty/posty_astonished.png"
    xalign -0.05
    pause 0.2
    "talksprites/posty/posty_astonished_open.png"
    pause 0.2
    repeat
image posty astonished quiet:
    "talksprites/posty/posty_astonished.png"
    xalign -0.05

    block:
        "talksprites/posty/posty_astonished.png"
        pause 2.0
        "talksprites/posty/posty_astonished_blink.png"
        pause 0.125
        repeat

image posty suspicious = WhileSpeaking(
    "posty", 
    "posty suspicious talk", 
    "posty suspicious quiet"
    )
image posty suspicious talk:
    "talksprites/posty/posty_suspicious.png"
    xalign -0.05
    pause 0.2
    "talksprites/posty/posty_suspicious_open.png"
    pause 0.2
    repeat
image posty suspicious quiet:
    "talksprites/posty/posty_suspicious.png"
    xalign -0.05

    block:
        "talksprites/posty/posty_suspicious.png"
        pause 2.0
        "talksprites/posty/posty_suspicious_blink.png"
        pause 0.125
        repeat

define anims.posty.astonished = FBFAnimation(17, 24)

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
    class ToastyStates():
        def __init__(self):
            self.is_popped = False
            self.unset = True
            self.mouth_state = "close"

        def unpop(self, *args):
            self.set_popped_state(False)

        def pop(self, *args):
            self.set_popped_state(True)

        def set_popped_state(self, new_state):
            self.mouth_state = "close"
            if self.unset:
                self.is_popped = new_state
                self.unset = False

            if self.is_popped != new_state:
                self.is_popped = new_state
                anims.toasty.toast.frame = 1
            else:
                anims.toasty.toast.frame = 0

        def toggle_mouth(self, *args):
            if self.mouth_state == "close":
                self.mouth_state = "open"
            else:
                self.mouth_state = "close"

        def no_anim(self, *args):
            self.unset = True

define anims.toasty.toast = FBFAnimation(5, 25, reset_after=True, reset_frame=0)

define states.toasty = ToastyStates()

define t = Character("Toasty",
    callback=speaker("toasty"), 
    image="toasty", 
    who_color="#d64d66"
    )

image toasty neutral = WhileSpeaking(
    "toasty", 
    "toasty neutral talk",
    "toasty neutral quiet"
    )
image toasty neutral talk:
    xalign 1.0
    function states.toasty.unpop
    parallel:
        "talksprites/toasty/toasty_neutral_[states.toasty.mouth_state]_[anims.toasty.toast.frame].png"
        pause 0.04
        function anims.toasty.toast.advance
        repeat
    parallel:
        pause 0.2
        function states.toasty.toggle_mouth
        repeat
image toasty neutral quiet:
    xalign 1.0
    function states.toasty.unpop
    block:
        "talksprites/toasty/toasty_neutral_close_[anims.toasty.toast.frame].png"
        pause 0.04
        function anims.toasty.toast.advance
        repeat 6

image toasty smug = WhileSpeaking(
    "toasty", 
    "toasty smug talk", 
    "toasty smug quiet"
    )
image toasty smug talk:
    xalign 1.0
    function states.toasty.pop
    parallel:
        "talksprites/toasty/toasty_smug_[states.toasty.mouth_state]_[anims.toasty.toast.frame].png"
        pause 0.04
        function anims.toasty.toast.advance
        repeat
    parallel:
        pause 0.2
        function states.toasty.toggle_mouth
        repeat
image toasty smug quiet:
    xalign 1.0
    function states.toasty.pop
    block:
        "talksprites/toasty/toasty_smug_close_[anims.toasty.toast.frame].png"
        pause 0.04
        function anims.toasty.toast.advance
        repeat 6

image toasty smug2 = WhileSpeaking(
    "toasty", 
    "toasty smug2 talk", 
    "toasty smug2 quiet"
    )
image toasty smug2 talk:
    xalign 1.0
    function states.toasty.pop
    parallel:
        "talksprites/toasty/toasty_smug2_[states.toasty.mouth_state]_[anims.toasty.toast.frame].png"
        pause 0.04
        function anims.toasty.toast.advance
        repeat
    parallel:
        pause 0.2
        function states.toasty.toggle_mouth
        repeat
image toasty smug2 quiet:
    xalign 1.0
    function states.toasty.pop
    block:
        "talksprites/toasty/toasty_smug2_close_[anims.toasty.toast.frame].png"
        pause 0.04
        function anims.toasty.toast.advance
        repeat 6

image toasty neutral2 = WhileSpeaking(
    "toasty", 
    "toasty neutral2 talk",
    "toasty neutral2 quiet"
    )
image toasty neutral2 talk:
    xalign 1.0
    function states.toasty.unpop
    parallel:
        "talksprites/toasty/toasty_neutral2_[states.toasty.mouth_state]_[anims.toasty.toast.frame].png"
        pause 0.04
        function anims.toasty.toast.advance
        repeat
    parallel:
        pause 0.2
        function states.toasty.toggle_mouth
        repeat
image toasty neutral2 quiet:
    xalign 1.0
    function states.toasty.unpop
    block:
        "talksprites/toasty/toasty_neutral2_close2_[anims.toasty.toast.frame].png"
        pause 0.04
        function anims.toasty.toast.advance
        repeat 6

image toasty smug3 = WhileSpeaking(
    "toasty", 
    "toasty smug3 talk", 
    "toasty smug3 quiet"
    )
image toasty smug3 talk:
    xalign 1.0
    function states.toasty.pop
    parallel:
        "talksprites/toasty/toasty_smug3_[states.toasty.mouth_state]_[anims.toasty.toast.frame].png"
        pause 0.04
        function anims.toasty.toast.advance
        repeat
    parallel:
        pause 0.2
        function states.toasty.toggle_mouth
        repeat
image toasty smug3 quiet:
    xalign 1.0
    function states.toasty.pop
    block:
        "talksprites/toasty/toasty_smug3_close_[anims.toasty.toast.frame].png"
        pause 0.04
        function anims.toasty.toast.advance
        repeat 6

image toasty smug4:
    xalign 1.0
    function states.toasty.pop
    block:
        "talksprites/toasty/toasty_smug4_[anims.toasty.toast.frame].png"
        pause 0.04
        function anims.toasty.toast.advance
        repeat 6

image toasty smug5 = WhileSpeaking(
    "toasty", 
    "toasty smug5 talk", 
    "toasty smug5 quiet"
    )
image toasty smug5 talk:
    xalign 1.0
    function states.toasty.pop
    parallel:
        "talksprites/toasty/toasty_smug5_[states.toasty.mouth_state]_[anims.toasty.toast.frame].png"
        pause 0.04
        function anims.toasty.toast.advance
        repeat
    parallel:
        pause 0.2
        function states.toasty.toggle_mouth
        repeat
image toasty smug5 quiet:
    xalign 1.0
    function states.toasty.pop
    block:
        "talksprites/toasty/toasty_smug5_close_[anims.toasty.toast.frame].png"
        pause 0.04
        function anims.toasty.toast.advance
        repeat 6

image toasty angry = WhileSpeaking(
    "toasty", 
    "toasty angry talk", 
    "toasty angry quiet"
    )
image toasty angry talk:
    xalign 1.0
    function states.toasty.unpop
    parallel:
        "talksprites/toasty/toasty_angry_[states.toasty.mouth_state]_[anims.toasty.toast.frame].png"
        pause 0.04
        function anims.toasty.toast.advance
        repeat
    parallel:
        pause 0.2
        function states.toasty.toggle_mouth
        repeat
image toasty angry quiet:
    xalign 1.0
    function states.toasty.unpop
    block:
        "talksprites/toasty/toasty_angry_close2_[anims.toasty.toast.frame].png"
        pause 0.04
        function anims.toasty.toast.advance
        repeat 6

image toasty annoyed = WhileSpeaking(
    "toasty", 
    "toasty annoyed talk", 
    "toasty annoyed quiet"
    )
image toasty annoyed talk:
    xalign 1.0
    function states.toasty.unpop
    parallel:
        "talksprites/toasty/toasty_annoyed_[states.toasty.mouth_state]_[anims.toasty.toast.frame].png"
        pause 0.04
        function anims.toasty.toast.advance
        repeat
    parallel:
        pause 0.2
        function states.toasty.toggle_mouth
        repeat
image toasty annoyed quiet:
    xalign 1.0
    function states.toasty.unpop
    block:
        "talksprites/toasty/toasty_annoyed_close_[anims.toasty.toast.frame].png"
        pause 0.04
        function anims.toasty.toast.advance
        repeat 6

image toasty crossedarms = WhileSpeaking(
    "toasty", 
    "toasty crossedarms talk", 
    "toasty crossedarms quiet"
    )
image toasty crossedarms talk:
    xalign 1.0
    function states.toasty.unpop
    parallel:
        "talksprites/toasty/toasty_crossedarms_[states.toasty.mouth_state]_[anims.toasty.toast.frame].png"
        pause 0.04
        function anims.toasty.toast.advance
        repeat
    parallel:
        pause 0.2
        function states.toasty.toggle_mouth
        repeat
image toasty crossedarms quiet:
    xalign 1.0
    function states.toasty.unpop
    block:
        "talksprites/toasty/toasty_crossedarms_close_[anims.toasty.toast.frame].png"
        pause 0.04
        function anims.toasty.toast.advance
        repeat 6

image toasty enthused = WhileSpeaking(
    "toasty", 
    "toasty enthused talk", 
    "toasty enthused quiet"
    )
image toasty enthused talk:
    xalign 1.0
    function states.toasty.unpop
    parallel:
        "talksprites/toasty/toasty_enthused_[states.toasty.mouth_state]_[anims.toasty.toast.frame].png"
        pause 0.04
        function anims.toasty.toast.advance
        repeat
    parallel:
        pause 0.2
        function states.toasty.toggle_mouth
        repeat
image toasty enthused quiet:
    xalign 1.0
    function states.toasty.unpop
    block:
        "talksprites/toasty/toasty_enthused_close_[anims.toasty.toast.frame].png"
        pause 0.04
        function anims.toasty.toast.advance
        repeat 6

image toasty laugh = WhileSpeaking(
    "toasty", 
    "toasty laugh talk", 
    "toasty laugh quiet"
    )
image toasty laugh talk:
    xalign 1.0
    function states.toasty.unpop
    parallel:
        "talksprites/toasty/toasty_laugh_[states.toasty.mouth_state]_[anims.toasty.toast.frame].png"
        pause 0.04
        function anims.toasty.toast.advance
        repeat
    parallel:
        pause 0.2
        function states.toasty.toggle_mouth
        repeat
image toasty laugh quiet:
    xalign 1.0
    function states.toasty.unpop
    block:
        "talksprites/toasty/toasty_laugh_close_[anims.toasty.toast.frame].png"
        pause 0.04
        function anims.toasty.toast.advance
        repeat 6

image toasty pointandlaugh = WhileSpeaking(
    "toasty", 
    "toasty pointandlaugh talk", 
    "toasty pointandlaugh quiet"
    )
image toasty pointandlaugh talk:
    xalign 1.0
    function states.toasty.unpop
    parallel:
        "talksprites/toasty/toasty_pointandlaugh_[states.toasty.mouth_state]_[anims.toasty.toast.frame].png"
        pause 0.04
        function anims.toasty.toast.advance
        repeat
    parallel:
        pause 0.2
        function states.toasty.toggle_mouth
        repeat
image toasty pointandlaugh quiet:
    xalign 1.0
    function states.toasty.unpop
    block:
        "talksprites/toasty/toasty_pointandlaugh_close_[anims.toasty.toast.frame].png"
        pause 0.04
        function anims.toasty.toast.advance
        repeat 6

image toasty turned = WhileSpeaking(
    "toasty", 
    "toasty turned talk", 
    "toasty turned quiet"
    )
image toasty turned talk:
    xalign 1.0
    function states.toasty.unpop
    parallel:
        "talksprites/toasty/toasty_turned_[states.toasty.mouth_state]_[anims.toasty.toast.frame].png"
        pause 0.04
        function anims.toasty.toast.advance
        repeat
    parallel:
        pause 0.2
        function states.toasty.toggle_mouth
        repeat
image toasty turned quiet:
    xalign 1.0
    function states.toasty.unpop
    block:
        "talksprites/toasty/toasty_turned_close_[anims.toasty.toast.frame].png"
        pause 0.04
        function anims.toasty.toast.advance
        repeat 6

image toasty turned2 = WhileSpeaking(
    "toasty", 
    "toasty turned2 talk", 
    "toasty turned2 quiet"
    )
image toasty turned2 talk:
    xalign 1.0
    function states.toasty.unpop
    parallel:
        "talksprites/toasty/toasty_turned2_[states.toasty.mouth_state]_[anims.toasty.toast.frame].png"
        pause 0.04
        function anims.toasty.toast.advance
        repeat
    parallel:
        pause 0.2
        function states.toasty.toggle_mouth
        repeat
image toasty turned2 quiet:
    xalign 1.0
    function states.toasty.unpop
    block:
        "talksprites/toasty/toasty_turned2_close_[anims.toasty.toast.frame].png"
        pause 0.04
        function anims.toasty.toast.advance
        repeat 6




define yd = Character("Yellow Diamond", 
    callback=speaker("yd", sound_file="yd_voice.wav"), 
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
    callback=speaker("btnet"),
    image="btnet", 
    who_color="#ff8aa7"
    )

image btnet = WhileSpeaking(
    "btnet",
    "btnet talk",
    "btnet quiet"
    )

image btnet quiet:
    "talksprites/btnet.png"
    zoom 1.4
    xalign 0.825 yalign 1.01
    xanchor 0.5 yanchor 1.0
    rotate_pad True
    transform_anchor True

image btnet talk:
    "talksprites/btnet.png"
    zoom 1.4
    xalign 0.825 yalign 1.01 # Is here to make sure the rotation doesn't cause missing pixels on the bottom
    xanchor 0.5 yanchor 1.0
    rotate_pad True
    transform_anchor True

    block:
        ease 1.25 rotate -2
        ease 1.25 rotate  2
        repeat


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
    xalign 1.0
    pause 0.2
    "talksprites/brandsoda_close.png"
    pause 0.2
    repeat
image bs quiet:
    "talksprites/brandsoda_close.png"
    xalign 1.0

image bs follow = WhileSpeaking(
    "bs", 
    "bs follow talk", 
    "bs follow quiet"
    )
image bs follow talk:
    "talksprites/brandsoda_open.png"
    xzoom -1.0
    xalign 0.35
    pause 0.2
    "talksprites/brandsoda_close.png"
    pause 0.2
    repeat
image bs follow quiet:
    "talksprites/brandsoda_close.png"
    xzoom -1.0
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
    xalign 0.75
    yalign 1.25
    pause 0.2
    "talksprites/sourgummy_close.png"
    pause 0.2
    repeat
image sgummy quiet:
    "talksprites/sourgummy_close.png"
    zoom 1.2
    xalign 0.75
    yalign 1.25


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
    xalign 1.0
    pause 0.2
    "talksprites/retainer_sad_close.png"
    pause 0.2
    repeat
image retainer sad quiet:
    "talksprites/retainer_sad_close.png"
    zoom 1.2
    xalign 1.0

image retainer happy = WhileSpeaking(
    "retainer", 
    "retainer happy talk", 
    "retainer happy quiet"
    )
image retainer happy talk:
    "talksprites/retainer_happy_open.png"
    zoom 1.2
    xalign 1.0
    pause 0.2
    "talksprites/retainer_happy_close.png"
    pause 0.2
    repeat
image retainer happy quiet:
    "talksprites/retainer_happy_close.png"
    zoom 1.2
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
    who_color="#bdbfe2"
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

define bluetile = Character("Blue Tile", 
    callback=speaker("bluetile"), 
    image="bluetile", 
    who_color="#2469ff"
    )

image bluetile annoyed = WhileSpeaking(
    "bluetile", 
    "bluetile annoyed talk", 
    "bluetile annoyed quiet"
    )
image bluetile annoyed talk:
    "talksprites/bluetile_annoyed_open.png"
    zoom 1.3
    xzoom -1.0
    xalign 1.05
    yalign 2.0
    pause 0.2
    "talksprites/bluetile_annoyed_close.png"
    pause 0.2
    repeat
image bluetile annoyed quiet:
    "talksprites/bluetile_annoyed_close.png"
    zoom 1.3
    xzoom -1.0
    xalign 1.05
    yalign 2.0

image bluetile giddy = WhileSpeaking(
    "bluetile", 
    "bluetile giddy talk", 
    "bluetile giddy quiet"
    )
image bluetile giddy talk:
    "talksprites/bluetile_giddy_open.png"
    zoom 1.3
    xzoom -1.0
    xalign 1.05
    yalign 2.0
    pause 0.2
    "talksprites/bluetile_giddy_close.png"
    pause 0.2
    repeat
image bluetile giddy quiet:
    "talksprites/bluetile_giddy_close.png"
    zoom 1.3
    xzoom -1.0
    xalign 1.05
    yalign 2.0

image bluetile scared = WhileSpeaking(
    "bluetile", 
    "bluetile scared talk", 
    "bluetile scared quiet"
    )
image bluetile scared talk:
    "talksprites/bluetile_scared_open.png"
    zoom 1.3
    xzoom -1.0
    xalign 1.05
    yalign 2.0
    pause 0.2
    "talksprites/bluetile_scared_close.png"
    pause 0.2
    repeat
image bluetile scared quiet:
    "talksprites/bluetile_scared_close.png"
    zoom 1.3
    xzoom -1.0
    xalign 1.05
    yalign 2.0


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


define capsule = Character("Capsule", 
    callback=speaker("capsule"), 
    image="capsule", 
    who_color="#fb9609"
    )

image capsule pain = WhileSpeaking(
    "capsule", 
    "capsule pain talk", 
    "capsule pain quiet"
    )
image capsule pain talk:
    "talksprites/capsule_pain_open.png"
    xzoom -1.0
    xalign 1.0
    pause 0.2
    "talksprites/capsule_pain_close.png"
    pause 0.2
    repeat
image capsule pain quiet:
    "talksprites/capsule_pain_close.png"
    xzoom -1.0
    xalign 1.0

image capsule happy = WhileSpeaking(
    "capsule", 
    "capsule happy talk", 
    "capsule happy quiet"
    )
image capsule happy talk:
    "talksprites/capsule_happy_open.png"
    xzoom -1.0
    xalign 1.0
    pause 0.2
    "talksprites/capsule_happy_close.png"
    pause 0.2
    repeat
image capsule happy quiet:
    "talksprites/capsule_happy_close.png"
    xzoom -1.0
    xalign 1.0


define buff = Character("Buff", 
    callback=speaker("buff"), 
    image="buff", 
    who_color="#b5bed6"
    )

image buff = WhileSpeaking(
    "buff", 
    "buff talk", 
    "buff quiet"
    )
image buff talk:
    "talksprites/buff_open.png"
    zoom 1.6
    xalign 1.03
    pause 0.2
    "talksprites/buff_close.png"
    pause 0.2
    repeat
image buff quiet:
    "talksprites/buff_close.png"
    zoom 1.6
    xalign 1.03


define ahiss = Character("Ahiss the Cat", 
    callback=speaker("ahiss"), 
    image="ahiss", 
    who_color="#f19c79"
    )

image ahiss = WhileSpeaking(
    "ahiss", 
    "ahiss talk", 
    "ahiss quiet"
    )
image ahiss talk:
    "talksprites/ahiss_open.png"
    zoom 1.5
    xalign 1.0
    xzoom -1.0
    pause 0.2
    "talksprites/ahiss_close.png"
    pause 0.2
    repeat
image ahiss quiet:
    "talksprites/ahiss_close.png"
    zoom 1.5
    xalign 1.0
    xzoom -1.0


define palettette = Character("Palettette@", 
    callback=speaker("palettette"), 
    image="palettette", 
    who_color="#d68c7b"
    )

image palettette = WhileSpeaking(
    "palettette", 
    "palettette talk", 
    "palettette quiet"
    )
image palettette talk:
    "talksprites/palettette_open.png"
    zoom 1.5
    xalign 1.0
    pause 0.2
    "talksprites/palettette_close.png"
    pause 0.2
    repeat
image palettette quiet:
    "talksprites/palettette_close.png"
    zoom 1.5
    xalign 1.0


define rcg = Character("Rose-Colored Glasses", 
    callback=speaker("rcg"), 
    image="rcg", 
    who_color="#ff80a6"
    )

image rcg = WhileSpeaking(
    "rcg", 
    "rcg talk", 
    "rcg quiet"
    )
image rcg talk:
    "talksprites/rcg_open.png"
    zoom 1.5
    xalign 0.6
    xzoom -1.0
    pause 0.2
    "talksprites/rcg_close.png"
    pause 0.2
    repeat
image rcg quiet:
    "talksprites/rcg_close.png"
    zoom 1.5
    xalign 0.6
    xzoom -1.0


define bcg = Character("Blue-Colored Glasses", 
    callback=speaker("bcg"), 
    image="bcg", 
    who_color="#aed6e3"
    )

image bcg = WhileSpeaking(
    "bcg", 
    "bcg talk", 
    "bcg quiet"
    )
image bcg talk:
    "talksprites/bcg_open.png"
    zoom 1.0
    xalign 1.06
    yalign 1.15
    pause 0.2
    "talksprites/bcg_close.png"
    pause 0.2
    repeat
image bcg quiet:
    "talksprites/bcg_close.png"
    zoom 1.0
    xalign 1.06
    yalign 1.15

define miso = Character("Miso Soup",
    callback=speaker("miso"), 
    image="miso", 
    who_color="#ab9d67"
    )

define notepad = Character("Notepad",
    callback=speaker("notepad"), 
    image="notepad", 
    who_color="#eff5f9"
    )

image notepad = WhileSpeaking(
    "notepad", 
    "notepad talk", 
    "notepad quiet"
    )
image notepad talk:
    "talksprites/notepad_open.png"
    zoom 1.6
    xzoom -1.0
    xalign 1.1
    pause 0.2
    "talksprites/notepad_close.png"
    pause 0.2
    repeat
image notepad quiet:
    "talksprites/notepad_close.png"
    zoom 1.6
    xzoom -1.0
    xalign 1.1



define tag = Character("Tag",
    callback=speaker("tag"), 
    image="tag", 
    who_color="#ebeaef"
    )

image tag = WhileSpeaking(
    "tag", 
    "tag talk", 
    "tag quiet"
    )
image tag talk:
    "talksprites/tag_open.png"
    zoom 1.4
    xzoom 1.0
    xalign 1.0
    pause 0.2
    "talksprites/tag_close.png"
    pause 0.2
    repeat
image tag quiet:
    "talksprites/tag_close.png"
    zoom 1.4
    xzoom 1.0
    xalign 1.0



define stickshift = Character("Stick Shift",
    callback=speaker("stickshift"), 
    image="stickshift", 
    who_color="#434343"
    )

image stickshift = WhileSpeaking(
    "stickshift", 
    "stickshift talk", 
    "stickshift quiet"
    )
image stickshift talk:
    "talksprites/stickshift_open.png"
    zoom 1.3
    xzoom 1.0
    xalign 1.0
    pause 0.2
    "talksprites/stickshift_close.png"
    pause 0.2
    repeat
image stickshift quiet:
    "talksprites/stickshift_close.png"
    zoom 1.3
    xzoom 1.0
    xalign 1.0



define auto = Character("Automotone",
    callback=speaker("auto"), 
    image="auto", 
    who_color="#00DAFF"
    )

image auto bothered= WhileSpeaking(
    "auto", 
    "auto bothered talk", 
    "auto bothered quiet",
    )
image auto bothered talk:
    "talksprites/automotone_bothered_open.png"
    zoom 1.3
    xzoom -1.0
    xalign 1.0
    pause 0.2
    "talksprites/automotone_bothered_close.png"
    pause 0.2
    repeat
image auto bothered quiet:
    "talksprites/automotone_bothered_close.png"
    zoom 1.3
    xzoom -1.0
    xalign 1.0


image auto sad= WhileSpeaking(
    "auto",
    "auto sad talk", 
    "auto sad quiet"
)
image auto sad talk:
    "talksprites/automotone_sad_open.png"
    zoom 1.3
    xzoom -1.0
    xalign 1.0
    pause 0.2
    "talksprites/automotone_sad_close.png"
    pause 0.2
    repeat
image auto sad quiet:
    "talksprites/automotone_sad_close.png"
    zoom 1.3
    xzoom -1.0
    xalign 1.0



define tb = Character("Ticket Booth",
    callback=speaker("tb"), 
    image="tb", 
    who_color="#5D3266"
    )

image tb neutral= WhileSpeaking(
    "tb", 
    "tb neutral talk", 
    "tb neutral quiet"
    )
image tb neutral talk:
    "talksprites/ticketbooth_normal_open.png"
    zoom 1.5
    xzoom 1.0
    xalign 1.0
    pause 0.2
    "talksprites/ticketbooth_normal_close.png"
    pause 0.2
    repeat
image tb neutral quiet:
    "talksprites/ticketbooth_normal_close.png"
    zoom 1.5
    xzoom 1.0
    xalign 1.0


image tb shy= WhileSpeaking(
    "tb",
    "tb shy talk", 
    "tb shy quiet"
)
image tb shy talk:
    "talksprites/ticketbooth_shy_open.png"
    zoom 1.5
    xzoom 1.0
    xalign 1.0
    pause 0.2
    "talksprites/ticketbooth_shy_close.png"
    pause 0.2
    repeat
image tb shy quiet:
    "talksprites/ticketbooth_shy_close.png"
    zoom 1.5
    xzoom 1.0
    xalign 1.0



define sb = Character("Squirt Bottle",
    callback=speaker("sb"), 
    image="sb", 
    who_color="#eb4034"
    )

image sb = WhileSpeaking(
    "sb", 
    "sb talk", 
    "sb quiet"
    )
image sb talk:
    "talksprites/squirtbottle_open.png"
    zoom 1.4
    xzoom 1.0
    xalign 1.0
    pause 0.2
    "talksprites/squirtbottle_close.png"
    pause 0.2
    repeat
image sb quiet:
    "talksprites/squirtbottle_close.png"
    zoom 1.4
    xzoom 1.0
    xalign 1.0



define marble = Character("Marble Bust",
    callback=speaker("marble"), 
    image="marble", 
    who_color="#bdbb9a"
    )

image marble = WhileSpeaking(
    "marble", 
    "marble talk", 
    "marble quiet"
    )
image marble talk:
    "talksprites/marblebust_open.png"
    zoom 1.3
    xzoom 1.0
    xalign 1.0
    pause 0.2
    "talksprites/marblebust_close.png"
    pause 0.2
    repeat
image marble quiet:
    "talksprites/marblebust_close.png"
    zoom 1.3
    xzoom 1.0
    xalign 1.0



define cb = Character("Crayon Box",
    callback=speaker("cb"), 
    image="cb", 
    who_color="#AED6E3"
    )

image cb = WhileSpeaking(
    "cb", 
    "cb talk", 
    "cb quiet"
    )
image cb talk:
    "talksprites/crayon_box_open.png"
    zoom 1.5
    xzoom -1.0
    xalign 1.0
    pause 0.2
    "talksprites/crayon_box_close.png"
    pause 0.2
    repeat
image cb quiet:
    "talksprites/crayon_box_close.png"
    zoom 1.5
    xzoom -1.0
    xalign 1.0
    
define tooly = Character("Tooly",
    callback=speaker("tooly"),
    image="tooly",
    who_color="9e4234"
    )

image tooly = WhileSpeaking(
    "tooly",
    "tooly talk",
    "tooly quiet"
    )
image tooly talk:
    "talksprites/tooly_open.png"
    zoom 1.2
    xzoom 1.0
    xalign 1.1
    pause 0.2
    "talksprites/tooly_close.png"
    pause 0.2
    repeat
image tooly quiet:
    "talksprites/tooly_close.png"
    zoom 1.2
    xzoom 1.0
    xalign 1.1



define rm = Character("Ripped Mitten",
    callback=speaker("rm"), 
    image="rm", 
    who_color="#63DEC2"
    )

image rm = WhileSpeaking(
    "rm", 
    "rm talk", 
    "rm quiet"
    )
image rm talk:
    "talksprites/ripped_mitten_open.png"
    zoom 1.2
    xzoom -1.0
    xalign 1.0
    pause 0.2
    "talksprites/ripped_mitten_close.png"
    pause 0.2
    repeat
image rm quiet:
    "talksprites/ripped_mitten_idle.png"
    zoom 1.2
    xzoom -1.0
    xalign 1.0

define jb = Character("Jukebox",
    callback=speaker("jb"), 
    image="jb", 
    who_color="#482C40"
    )

image jb = WhileSpeaking(
    "jb", 
    "jb talk", 
    "jb quiet"
    )
image jb talk:
    "talksprites/jukebox_open.png"
    zoom 1.3
    xzoom 1.0
    xalign 1.0
    pause 0.2
    "talksprites/jukebox_close.png"
    pause 0.2
    repeat
image jb quiet:
    "talksprites/jukebox_close.png"
    zoom 1.3
    xzoom 1.0
    xalign 1.0

    

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
        "End the game please.":
            return

label .other:

    p "Other people!"
    yd "K, well I'm Yellow Diamond. You already knew that part."
    yd "Time to take my leave!"
    hide yd
    show btnet
    btnet "Hi, I'm B.T. Net!"
    p "Hello, B.T. Net!"
    hide btnet
    show rcg
    show bcg
    rcg "Hello there, I'm Rose-Colored Glasses!"
    bcg "And I'm Blue-Colored Glasses."
    hide rcg
    hide bcg
    show palettette
    palettette "Howdy, it's me, Palettette@!"
    p "Hi hello how are you"
    hide palettette
    show ahiss
    ahiss "Good afternoon, darling. My name is Ahiss the Cat."
    ahiss "Hiss!"
    p "ok"
    hide ahiss
    show buff
    buff "I'm buff. I mean, I'm Buff."
    hide buff
    show capsule happy
    capsule "Hello! It's me, Capsule. I'm feeling happy."
    capsule pain "Ah! I'm in pain!"
    p "Pain from what?"
    capsule "Existential dread."
    capsule happy "Just kidding!"
    hide capsule
    show bluetile giddy
    bluetile "Heyyyyy, it's me Blue Tile! I have three sets of sprites!"
    bluetile annoyed "Grr... (annoyed)"
    bluetile giddy "Yay though! (giddy)"
    bluetile scared "Aah! (scared)"
    p "Ok."
    hide bluetile
    show dolly
    p "Hi Dolly. This is what you look like when you're not speaking. Also I just wanna test where the text wraps just out of curiosity."
    dolly "That's right. And this is what I look like when I {i}am{/i} speaking."
    p "Damn!"
    dolly "And also..."
    dolly "I can program your whole game and make the art for you for only fifty easy payments of $999.99."
    dolly "That means you pay me $999.99 fifty seperate times."
    p annoyed "I can tell you're really invested in helping me..."
    dolly "shhhhhhhh don't worry about it"
    hide dolly
    show posty neutral
    show redtile
    redtile "Hi I'm Red Tile."
    p "sup"
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
    hide cameron
    show notepad
    notepad "Hey, I'm Notepad."
    hide notepad
    show tag
    tag "Sup. it's me, tag. i'm cool, i guess."
    p "How come you didn't capitalize your i's?"
    tag "it's subversive."
    hide tag
    show stickshift
    stickshift "Hi, my name is Stick Shift."
    hide stickshift
    show auto bothered
    auto bothered "Huh? Oh, I'm Automotone."
    auto sad "The artist made extra assets for me and now I'm sad."
    auto sad "They put in too much hard work for an NPC."
    p "I wouldn't worry about it."
    p zany "JUST LOOK AT ME!"
    auto sad "I can't be beared to look. :("
    hide auto sad
    show posty neutral
    show tb neutral
    tb neutral "Hello! I'm Ticket Booth."
    tb neutral "I also have extra assets!"
    tb neutral "I have these neutral talking sprites!"
    tb shy "And I have shy talking sprites..."
    tb shy "More sprites are helpful, right?"
    p "Yeah, I guess so."
    hide tb
    show sb
    sb "What do you want? I'm busy!"
    p "Sorry, Squirt Bottle."
    hide sb
    show marble
    marble "My name is Marble Bust, and I'm personally starting to doubt that one person seriously drew all these assets."
    hide marble
    show cb
    cb "Heya, kiddo! It's me Crayon Box, host of Open Source Objects!"
    hide cb
    show rm
    rm "Oh hi, I'm Ripped Mitten."
    p "What's wrong with your camera?"
    rm "I don't know."
    hide rm
    show jb
    jb "Yooooooo! It's me, Jukebox!"
    jb "I have all the latest hits like Last Night, Someone you Loved, and Darude Sandstorm!"
    p "Ew. No."
    p "What even is a darude?"
    jb "It's a way of life."
    hide jb
    show tooly
    tooly "Hey there pal! My name's Tooly!"
    p "Hi Tooly! /pos"
    tooly "Ewwww, get out of here with your modern slang."
    hide toooly
    jump chartest

label .toasty:

    hide yd
    $ states.toasty.no_anim()
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
    $ states.toasty.no_anim()
    show toasty enthused
    t "and coming back with my toast in a different state doesn't play the animation."
    t annoyed "Well, actually the state of my toast isn't automatically thrown out when I'm hidden, so by default it does still play."
    t neutral2 "You have to put \"$ states.toasty.no_anim()\" before showing me in order to prevent the transition."
    t neutral "Going from not smug to smug with a hide in between"
    hide toasty
    p quiet "..."
    $ states.toasty.no_anim()
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
    hide toasty
    jump chartest

label .posty:

    p "Meee!!!"
    yd "Cool, you can at least talk."
    p "By the way, my expressions have an idle blink animation, except for happy and zany."
    yd "Now that's some attention to detail, if I do say so myself!"
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
    yd quiet "..."
    p sad "Sad."
    yd quiet "..."
    p angry "Angry..! Note how there's an idle animation!"
    yd quiet "..."
    p annoyed "Annoyed."
    yd quiet "..."
    p astonished "Astonished, if you remember."
    p astonished anim "And astonished comes with an animation, too."
    p confused "Confused?"
    yd quiet "..."
    p concerned "Concerned..."
    yd quiet "..."
    p neutral quiet "..."
    p suspicious "... suspicious..."
    yd "Suspicious indeed."
    p zany "ZANY!!1"
    yd "What was that last one?"
    p "USE THIS ONE SPARINGLY!!!!11"
    jump chartest
