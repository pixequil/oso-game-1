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

    show posty neutral
    show yd
    yd "Welcome to the character test room. I get to talk first."
    p "No fair!! Haha, well at least I get to stop talking when I'm not talking. Jealous?"
    yd "What are you talking about? We fixed that."
    p "Well, what if I want to have an inner monologue?"
    p quiet "{i}How's this?{/i}"

    