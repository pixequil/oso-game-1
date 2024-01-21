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

image painting_food_floor:
    "items/Brussel_Sprouts.png"
    xalign 0.5
    yalign 1.0
    zoom 0.75

image painting_food:
    "items/Brussel_Sprouts.png"
    truecenter
    zoom 0.75

image eating:
    "items/personeatingfoodpainting.png"
    truecenter
    zoom 1.75

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

label .marble:
    scene bg museum_food
    show marble
    if quest.money_food:
        jump .marble3
    elif saw.marble:
        jump .marble2
    else:
        jump .marble1

label .marble1: #248
    show posty neutral
    $ saw.marble = True
    marble "_" # Marble Bust explains her deal. A very discerning and respected (if a bit eccentric) art critic and collector (and a connoisseur of the arts). She is disappointed with all the artwork not only in this exhibition but also in the entire museum - nothing there seems fit for her personal collection.
    p "_" # posty is like ok
    if item.napkin:
        jump .marble_napkin
    else:
        marble "_" # marble bust tells posty to leave her alone while she searches for the ultimate work of art
        jump museum_food

label .marble2: #248
    show posty neutral
    if item.napkin:
        jump .marble_napkin
    else:
        marble "_" # marble bust reminds posty to leave her alone while she searches for the ultimate work of art
        jump museum_food

label .marble_napkin: 
    marble "_" # marble bust stops posty, asking what she's holding.
    p "_" # "this?"
    show badpainting
    marble "_" # marble bust thinks this is the highest form of art. simply must have it for her collection. offers to pay handsomely.
    p "_" #posty pretends to not want to hand it over, but agrees to.
    "You handed over the {b}priceless, one-of-a-kind highbrow painting{/b}!"
    $ item.napkin = False
    hide badpainting
    $ money += 2
    $ quest.money_food = True
    show cash_bundle_2 at truecenter
    $ renpy.transition(irisout, layer="master") #prevents interruption of the text window
    "{b}{color=#bdbb9a}Marble Bust{/color}{/b} gave you {b}some money{/b}!"
    hide cash_bundle_2
    call money_get
    p "_" # some kind of parting remark
    jump museum_food

label .marble3: #251
    show posty neutral
    marble "_" # revisiting marble bust
    jump museum_food

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
    show generichips at truecenter
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
    show painting_food_floor
    show posty neutral
    show rm
    p "_" # posty arrives, having felt drawn to this painting inexplicably
    rm "_" # Ripped Mitten says a veiled complaint about the painting, like it doesn't belong here, and how nobody would miss it. then they leave.
    hide rm with moveoutright
    p "_" # posty beholds the main painting in the food exhibit and feels a compulsion to collect it.
    hide painting_food_floor
    show painting_food
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

