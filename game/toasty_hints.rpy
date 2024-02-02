# throughout the game, the player can return to Toasty to receive hints. this file is jumped to when the player interacts with Toasty, and then sends the player back to mainstreet (which is where Toasty should always be accessed).
# the hints are listed in a weird, almost reverse walkthrough order here.
# since the hints are accessed via "call", they should all end with "return".

label toasty_hints:

    scene bg mainstreet
    
    if win_flag:
        show posty neutral
        show toasty neutral
        t "you won; no need to have a hint" # they have some kind of conversation about how posty actually managed to deliver the package, and how it was quite difficult. posty muses that she could use a nap in the park
        return

    elif party_bs:
        show posty neutral
        show toasty neutral
        show bs follow behind posty with moveinleft
        bs "_"
        t "hint for if Brand Soda is following you" # TODO: #13 brand soda hint (talk to yd or "someone who wants to advertise")
        return

    # above this line are urgent hints, that should be prioritized
    # below this line are hints displayed in roughly reverse walkthrough order

    elif quest.retainer:
        show posty neutral
        show toasty neutral
        t "hint for if you made retainer leave but didnt talk to crayon box" #292
        return

    elif item.makeshift_trophy:
        show posty neutral
        show toasty neutral
        t "hint for if you have the makeshift trophy (give it to retainer)" #281
        return
    
    elif item.notice:
        show posty neutral
        show toasty neutral
        t "hint for if you got the notice of reprimand" #257
        return

    elif item.napkin:
        show posty neutral
        show toasty neutral
        t "hint for if you got the napkin painting" #252
        return

    elif item.chips:
        show posty neutral
        show toasty neutral
        t "hint for if you got the chips" #242
        return


    elif saw.janitors and (quest.money_food == False):
        show posty neutral
        show toasty neutral
        t "hint for if you went in the janitors closet but didnt get chips" #241
        return

    elif food_switch and (quest.money_food == False) and (saw.janitors == False):
        show posty neutral
        show toasty neutral
        t "hint for if you opened the janitors closet but didnt go in" #234
        return

    elif scanter_green and (quest.painting_war == False):
        show posty neutral
        show toasty neutral
        t "hint for if Palettette has turned the painting green" #222
        return
    
    elif item.battery:
        show posty neutral
        show toasty neutral
        p happy "Duh duh dum, dum diddly dum-"
        t enthused "Hello my most perfidious postbox."
        p annoyed "not again {i}coughs{/i} so what you need?"
        t crossedarms "I was just wondering what you have in your hand?"
        p suspicious "Just a battery."
        t angry "That's it? I thought it would be something more valuable."
        p concerned "I dunno, something intrigues me about it."
        t smug "Could it be its satisfying weight, finely crafted out of the earth's treasures?"
        t "Maybe its cold metal gives tingles as though a hidden memory is unlocked from your steely heart."
        p confused "Why you being so fancy with the descriptions?"
        t enthused "Oh! I can put my curiosities to rest-"
        p happy "Ahh you are finally giving me peace."
        t smug "It must be the tasteful interspersion of Helvetica and Arial in 'PLEASE DON'T EAT OR CONSUME THIS'; gives the message some much needed depth."
        p concerned "you reading too much into this."
        t pointandlaugh "How did such a nitwit like you get so tasteful?"
        p annoyed "..."
        t neutral"..."
        t "Joking, joking."
        t "Besides, why are you looking at it like that?"
        p concerned "I dont know. I thought a good walk could help me with that."
        t smug "Wellll-"
        p confused "Well?"
        t neutral "Give me a second, I have a call."
        t turned "Looks like my cuboid companion has made a major misstep: wasting valuable energy on idle walking!"
        p confused "...wait what?"
        t "I know the quality of art has declined rapidly in the last decade of so but I dont recall being a battery exhibit back there."
        t "Think Toast, who would lose such an item there?"
        t "Maybe an artist, too engrossed in their crafts, dropped it behind..."
        t "Yess you are such a genius Toastmeister, I will win this challenge in no time!"
        p annoyed "really Toastmeister?"
        t "All we have to do is make sure our friend doesn't eavesdrop and we golden!"
        t "Err..hope to see you bye!"
        t neutral "So whatcha going to do with the battery?"
        return

    elif item.imaginary_lighter:
        show posty neutral
        show toasty neutral
        t "hint for if you have the imaginary lighter" #163
        return
    
    elif item.heavier:
        show posty neutral
        show toasty neutral
        t "hint for if you have the heavier" #162
        return

    elif bt_distracted:
        show posty neutral
        show toasty neutral
        t "hint for if blue tile is distracted and you can finally take the painting" #120
        return

    elif miso_blocked and (quest.painting_blue == False):
        show posty neutral
        show toasty neutral
        t "hint for if blue tile doesn't let you spill soup on the painting" #117
        return

    elif item.ladle_full:
        show posty neutral
        show toasty smug2
        t "Oh, so you decided to use that ladle on something, hmm?"
        t laugh "What are you going to do with that soup, anyway? Start a food fight?"
        t pointandlaugh "Hah! Just the thought of you getting everything rusty makes me chuckle!"
        t neutral quiet "..."
        t enthused "Actually, if you are, can I join?"
        p neutral "Uh, I'm not planning any fights, sorry."
        t annoyed "Ugh, {i}lame{/i}."
        return

    elif item.ladle_empty:
        show posty neutral
        show toasty neutral
        t "hint for if you have empty ladle" # todo: #52 empty ladle hint (use it on miso soup)
        return

    elif quest.paintings and (quest.moneys == False) and (money == 2):
        show posty neutral
        show toasty neutral
        t "hint for if you have the spray paint but nothing to decorate with it (see dolly)" #265
        return

    elif quest.paintings and (quest.bs == False):
        show posty neutral
        show toasty neutral
        t "hint for if you have the spray paint but nothing to decorate with it (talk to bs)" #265
        return

    elif quest.paintings and (money == 1):
        show posty neutral
        show toasty neutral
        t "hint for if you have the spray paint but nothing to decorate with it (do food exhibit quest)" #265
        return

    elif paintings == 3 and (quest.paintings == False):
        show posty neutral
        show toasty neutral
        t "hint for if you've taken three paintings (assemble them)" #229
        return

    elif paintings == 2:
        show posty neutral
        show toasty neutral
        t "hint for if you've taken two paintings" #221
        return

    elif paintings == 1:
        show posty neutral
        show toasty neutral
        t "hint for if you've taken one painting" #154
        return
    
    elif quest.bs:
        show posty neutral
        show toasty neutral
        t "hint for if you finished Brand Soda quest" # TODO: #18 hint for after brand soda quest (go in the museum)
        return

    elif saw.retainerblock:
        show posty concerned
        show toasty neutral
        p concerned "Hey Toasty."
        t smug "Hey loser."
        t smug2 "Looks like you met Retainer." 
        t smug3 "Let me guess, was he bitter and in denial?"
        p "Pretty much..."
        t laugh "HA! Good thing I'm not wasting my time over there!"
        t crossedarms "I'm hanging out here, where all the action is!"
        t enthused "Music, art, local businesses, it all just...makes me feel alive!"
        t smug "And then I look at your face."
        show toasty pointandlaugh talk
        p annoyed "Thanks, I guess."
        return

    elif item.butterfly_package:
        show posty neutral
        show toasty neutral
        t "hint for if you just started the game" # TODO: #6 game start hint (try delivering the butterflies)
        return

    else:
        show posty neutral
        show toasty neutral
        t "I don't have any hints for you, sorry. You should never see this dialogue."
        p confused "Wuh oh."
        return
