# todo: food exihibit conversation bg #190

# todo: food main exhibit painting #226

image bg museum_food_top:
    "map-bgs/museum_food_top.png"
    zoom 1.15
    yalign 0.2

image badpainting:
    "items/badpainting.jpg"
    zoom 0.1
    yalign 0.5

label museum_food:
    scene bg museum_food_top
    show posty neutral

    p "_" # todo: food exhibit imagemap #224

    menu:
        "Ripped Mitten & Unappetizing painting" if (quest.painting_food == False):
            jump .painting
        "Ripped Mitten" if quest.painting_food:
            jump .rm
        "Notepad":
            jump .notepad
        "Marble Bust":
            jump .marble
        "Corndog painting" if (food_switch == False):
            jump .corndog
        "Hidden passageway" if food_switch:
            jump janitors
        "Eating painting":
            jump .eating
        "Go back to the entrance.":
            jump museum_entrance

label .notepad:
    scene bg museum_food
    show notepad
    if gave_chips:
        jump .notepad3
    elif saw.notepad:
        jump .notepad2
    else:
        jump .notepad1

label .notepad1: #244
    show posty neutral
    $ saw.notepad = True
    notepad "_" # notepad explains their whole deal. A starving artist (emphasis on “starving”)/doodler who has had no luck in convincing any curators to buy their art for any price. They’re extremely upset and hungry, and will trade their art for food at this point.
    if item.chips:
        jump .notepad_chips
    else:
        p "_" # posty apologizes, not having any food for them.
        notepad "_" # notepad tells her to let them know if they find any for them
        jump museum_food

label .notepad2: #244
    show posty neutral
    notepad "_" # notepad asks posty if she has any food for them now.
    if item.chips:
        jump .notepad_chips
    else:
        p "_" # posty apologizes, as she still doesn't.
        notepad "_" # notepad reminds her to let them know if they find any for them
        jump museum_food

label .notepad_chips: #246
    p "_" # posty does indeed have some chips for notepad!
    show generichips
    "You handed over the {b}Generi-Chips{/b}!"
    $ item.chips = False
    $ gave_chips = True
    hide generichips
    notepad "_" # notepad is grateful, and gives you a piece of their art in return
    show badpainting
    "You got the {b}napkin \"painting\"{/b}!" #245 describe napkin painting
    $ item.napkin = True
    hide badpainting
    p "_" # posty pretends to think it's cool and makes up an excuse to stop talking to notepad.
    jump museum_food

label .notepad3: #247
    show posty neutral
    notepad "_" # revisiting notepad
    jump museum_food

label .painting: #228
    scene bg museum_food
    show painting_food
    show posty neutral
    show rm
    p "_" # posty arrives, having felt drawn to this painting inexplicably
    rm "_" # Ripped Mitten says a veiled complaint about the painting, like it doesn't belong here, and how nobody would miss it. then they leave.
    hide rm with moveoutright
    p "_" # posty beholds the main painting in the food exhibit and feels a compulsion to collect it.
    show painting_food at center
    "You got an {b}art piece{/b}!" #227 describe food painting
    $ item.painting_food = True
    $ quest.painting_food = True
    $ paintings += 1
    hide painting_food
    if paintings == 1:
        p "this was the first painting (replace this text)" # posty says something and decides to look around the rest of the exhibit
    else:
        p "that was easy (replace this text)" # posty remarks that it was easy to take this painting, if this isn't her first painting.
    jump museum_food

label .rm:
    scene bg museum_food
    show posty neutral
    show rm
    rm "_" #230 speaking to ripped mitten a second time, briefly
    jump museum_food

label .corndog:
    scene bg museum_food
    show corndog
    show posty neutral
    p "_" #231 posty observes the corndog painting. it doesnt really call out to her, but it sure is huge. it doesn't seem to be supported by anything, just leaning on the wall. posty decides to look at the other paintings.
    jump museum_food

label .eating: #233
    scene bg museum_food
    show eating
    show posty neutral
    if food_switch == False:
        p "_" # posty observes that the painting doesn't really belong here. these are paintings of food, not paintings of eating. she takes a look at the painting's placard, curious why it was included.
        "The title of the painting is \"{i}Crisis of the Poplar Trees{/i}\". The rest of the text is too small to read at this distance." 
        p "_" # posty remarks that that's hardly a fitting name for this painting either, and it sure as hell isnt fitting for a painting in the food exhibit.
        label .eating_decide:
        menu:
            "Read more of the placard?"

            "Yes.":
                "You try to read more of the placard, but bonk your face on it by mistake!"
                # play a sound here! like a click!!!
                # and then a scene of the corndog painting disappearing, revealing the secret passageway.
                $ food_switch = True
                p "_" # something like "well that was weird. better back off"
                jump museum_food
            "No.":
                p "_" # posty decides she is uninterested in reading more of the placard. she starts to walk away, but returns to the placard, still curious.
                jump .eating_decide
    else:
        p "_" # posty returns to actually read the placard this time.
        "The placard reads: \"{i}(something){/i}\". Weird!" # placard full text.
        p "_" # some kind of remark
        jump museum_food

