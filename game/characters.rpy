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

define p = Character(
    "Posty", 
    callback=speaker("posty"), 
    image="posty", 
    who_color="#5282f1"
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
    "talksprites/posty/posty_astonished_open.png"
    zoom 2.2
    xalign -0.05
    pause 0.2
    "talksprites/posty/posty_astonished_close.png"
    pause 0.2
    repeat
image posty astonished quiet:
    "talksprites/posty/posty_astonished_close.png"
    zoom 2.2
    xalign -0.05

init python: # code taken from https://essrenpytutorials.page/animating-an-image-in-renpy-automatically/
    def next_frame(t, st, at):
        global animation_frame
        if animation_frame < 18: # todo: #3 change frame amount from being hardcoded, to instead be a variable you can pass to the function
            animation_frame += 1
        # else:
        #     animation_frame = 1

image posty astonished anim:
    zoom 2.2
    xalign -0.05
    "talksprites/posty/posty_astonished_anim_[animation_frame].png"
    pause 0.04
    function next_frame
    repeat



define yd = Character(
    "Yellow Diamond", 
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


# Non-canonical scene for testing stuff. Players should never see this in the final game.

label chartest:

    scene bg room with fade
    $animation_frame = 1

    show posty neutral
    show yd
    yd "Welcome to the character test room. I get to talk first."
    p "No fair!! Haha, well at least I get to stop talking when I'm not talking. Jealous?"
    yd "What are you talking about? We fixed that."
    p "Well, what if I want to have an inner monologue?"
    p quiet "{i}How's this?{/i}"
    yd "I heard that"
    p astonished quiet "..."
    p astonished anim "..!"
    p -anim "How..?!"
    yd "Dunno."

    