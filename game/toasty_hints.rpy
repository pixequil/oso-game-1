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
        bs "Hello!"
        t smug "Who is this you brought along to follow you?"
        bs "Lady, I'm gonna be the next big thing!"
        p happy "We're looking for someone who wants to advertise them."
        t annoyed "Well that surely isn't me; I don't care."
        show posty neutral
        bs "Oh..."
        t smug2 "Try talking to somebody else around here. No one loiters around Main Street unless they're trying to reach for the stars."
        bs "Oh, that sounds like a good idea!"
        t smug5 "Good idea? Aimlessly walking around and talking to strangers?"
        show toasty pointandlaugh talk
        t "Gyahahahaha! Loool!"
        p angry quiet "..."
        return

    # above this line are urgent hints, that should be prioritized
    # below this line are hints displayed in roughly reverse walkthrough order

    elif quest.retainer:
        show posty happy
        show toasty neutral
        p "Oof I glad I made Retainer happy again, I can't wait to take a nap."
        t pointandlaugh "Ohohoho what do we have here: thinking of turning truant for the treacherous mistress known as sleep?"
        p annoyed "Stop speaking like a Victorian; you don't appear to have anything better to do."
        t smug "I concede that I am not the shiniest appliance in this messy kitchen we call life, but I don't recall you having a keen interest in lepidopterology."
        p suspicious "Lepidoptrolowhat? Is that even a word or are you trying to get one up on me?"
        t crossedarms "Hmph: if you were even a hundredth as diligent and scholarly as me, you would've realized that lepidopterists would kill to even touch the {b}package{/b} you hold right now."
        t smug "Who knows, if you are careless enough, maybe even little old me may take a swipe of it!"
        return

    elif item.makeshift_trophy:
        show posty neutral
        show toasty enthused 
        t "You have a nice trophy with ya, what you going to do with it?"
        p "Dunno, probably put it on a shelf at home; pretend to be a winner and show it off."
        t smug "Well it would severely clash with the decor, especially with the grey curtains and general lack of furniture."
        p annoyed "Rude. Also how did you find my address-"
        t crossedarms "Keep your petty questions for later! You said this thing made you feel like a winner, right?"
        p suspicious "Yeah"
        t "Well I think there is someone who would like that feeling, someone down on their luck..."
        t enthused "A big hulking trophy would bring their spirits right up!"
        return
    
    elif item.notice:
        show posty concerned
        show toasty smug
        t "Posty! Is that what I think I see?"
        p "Yeah, it's a notice of reprimand from the art museum."
        t pointandlaugh "HA HA HA!"
        t smug2 "Oh, tsk tsk. Posty!"
        t smug5 "Don't you know those things are only given to the worst of people? The lowest forms of life? The raffiest of the riffraff? "
        p annoyed "I get the picture, Toasty."
        t neutral2 "I don't know how you could be so cruel..."
        t turned2 "In fact, I shouldn't even speak to scoundrelous scum such as you."
        p angry "C'mon Toasty! I need your help! What do I do with this notice?"
        t turned "Blah blah blah, I'm not listening to you..."
        t turned "Why don't you go hang out with your friends in the alley near the dumpsters?"
        t turned2 "WHERE YOU BELONG!"
        return

    elif item.napkin:
        show posty neutral
        show toasty neutral
        t "hint for if you got the napkin painting" #252
        return

    elif item.chips:
        show posty happy
        show toasty neutral     
        p "You want some Generi-Chips?"
        t pointandlaugh "Lol, no!"
        t smug "Why'd you even get those anyway? I thought you hated them!"
        p annoyed "Argh! That's exactly why I'm trying to get rid of them!"
        t smug2 "Hmph. Well, where'd you get those chips?"
        p concerned "Uh...the museum?"
        t smug3 "Have you asked somebody in the museum if they want them?"
        p "...no, I don't think so."
        t smug5 "I would say go in there and check, but to be honest, I think you're stuck with them."
        t pointandlaugh "Hah! You really are stupid, aren't you?"
        return


    elif saw.janitors and (quest.money_food == False):
        show posty neutral
        show toasty smug
        t "It\'s you, my good \'ol pal, post it note!"
        p annoyed "It\'s Posty, Toaster."
        t smug3 "Yeah I\'m just joking around! Learn to have some humor."
        p "Yeah whatever. Anyways I saw this secret room with a vending machine in it or.. whatever."
        t annoyed "You saw a vending machine and you {b}didn\'t use it?!{/b} Why not dummy!"
        p sad "Well… I thought it was some ordinary vending machine, so I didn\'t take some time to investigate it."
        t turned2 "That\'s a real loss for you, you could\'ve gotten a drink from there! Maybe if you were just tired or dehydrated.. Whatever it was!"
        p neutral "Hm.. I suppose, I\'ll get going now."
        show posty annoyed
        t pointandlaugh "Yeah whatever. Just go already and stop wasting my time!"
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
        t "hint for if you have the battery" #175
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
        p "Hey Toasty?"
        t "What?"
        p "I need some help, could you lend a hand?"
        t smug "No."
        p angry "And why not?"
        t crossedarms "Busy."
        p "Doing what?"
        t pointandlaugh "Not helping you."
        p "I will give you a papercut with one of these envelopes if you don\'t help me."
        t "HAH! I\'d like to see you try."
        show ladle_full
        p "Ok, how about I pour this miso soup on you?"
        t neutral "...Why do you just have a ladle of miso soup? Are you going to eat that or something?"
        p suspicious "No, look, I\'m only telling you this because you\'re enough of an idiot to support it, but I need to dump this on a painting, and someone is in my way."
        t enthused "Ooh~ defiling stuff? Count me in!"
        p angry "Absolutely not, you\'d just get us caught by insulting me."
        t smug2 "Touche, either way, whatcha gonna do about it?"
        p concerned "I\'m… not sure. You\'re good with these things, that\'s why I came to you."
        t enthused "Well, if someone is in your way, couldn\'t you just get them… out of your way?"
        p angry "If it was that simple, I would\'ve done it already."
        t laugh "Maybe you could just kill them and go to prison so I wouldn\'t have to talk to you again."
        p annoyed "Gee, thanks. Any ACTUAL suggestions?"
        t smug "If you aren\'t willing to do it, find someone else who is!"
        p angry "I\'M NOT GONNA KILL TH- ugh, you\'re useless."
        t laugh "Happy to be, Posty!"
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
        show toasty annoyed
        t "Um... what are you doing with that?"
        p "Doing with what?"
        show ladle_empty
        t "The ladle."
        p "Dunno. A red guy gave it to me."
        t laugh quiet "..."
        p angry "What!"
        t -quiet "It's a ladle. You fill it up with things. Are you stupid?"
        p "That was very rude."
        return

    elif quest.paintings and (quest.moneys == False) and (money == 3):
        show posty neutral
        show toasty neutral2
        t "What'cha got there?"
        p "Gold spray paint."
        t smug3 "Taking up a life of crime, Posty?"
        p concerned "No, I'm just holding onto it. I'm not sure what to do with it though."
        t crossedarms "It looks like you've got enough money to spend on a loot box from Dolly's."
        t "If you're lucky, you could get the perfect thing to spray paint."
        t "Granted, I've heard stories of people going broke from the insurance costs of a new car."
        t "Or even dying after from a box that had lethal arsenic powder inside of it."
        show posty angry
        t smug2 "Either way, I want you to know I'm happy for you."
        p annoyed "I'm very reassured."
#hint:if you have spray paint but nothing to decorate(see dolly) #265
        return

    elif quest.paintings and (quest.bs == False):
        show posty neutral
        show toasty neutral2
        t "What'cha got there?"
        p "Gold spray paint."
        t smug3 "Turning into an graffiti artist, Posty?"
        p concerned "No, I'm just holding onto it. I'm not sure what to do with it though."
        t smug2 "You could get ideas from people on the street. That soda can guy's always in need for a commission."
        t laugh "They're so self-absorbed that you'd never run out of work!"
        t laugh "Hope you like drawing a soda can for the rest of your life!"
#hint:if you have spray paint but nothing to decorate(talk to bs)" #265
        return

    elif quest.paintings and (money == 1):
        show posty neutral
        show toasty neutral2
        t "What'cha got there?"
        p "Gold spray paint."
        t smug3 "Wanting to get into mural art, Posty?"
        p concerned "No, I'm just holding onto it. I'm not sure what to do with it though."
        t enthused "Maybe you need to get some inspiration."
        p happy "Like in the art museum?"
        show posty angry
        t smug2 "I was actually thinking about you ruminating in a hole in the ground, but that works too."
#hint:if you have the spray paint but nothing to decorate with it (do food exhibit quest)" #265
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
        t "You deal with that Brand Soda guy yet?"
        p "Yeah. Yellow Diamond's gonna be their manager, to some degree."
        t "Oh good. Now what?"
        p "I'm not sure. I got some money out of it."
        t smug2 "Try spending it all in one place."
        p annoyed "Very funny."
        t "Ok, seriously though, try going somewhere else. You spent so much time wandering around the street with Brand Soda."
        t "Maybe you should go to that art museum. It sounds interesting!"
        t "You could make the next big painting and get a fat paycheck from it!"
        t "Then you could spend your money at two places!"
        t pointandlaugh "And be twice as broke!"

        return

    elif saw.retainerblock:
        show posty concerned
        show toasty neutral
        p concerned "Hey Toasty."
        t smug "Hey loser."
        t smug2 "Looks like you met Retainer."
        p "Wait, how did you-{nw}"
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
        if saw.lost:
            show toasty angry
            t "I SAID GO!!!"
            p confused "SORRY!"
        else:
            show toasty turned2
            $ saw.lost = True
            t "You again? That was fast."
            p "I guess I got turned around?"
            t smug "You know, I'd tell you to get lost, but..."
            show toasty pointandlaugh
            extend "\nit looks like you don't know how!"
            t smug3 "Look. Around here, we have a mantra:\n\"When in doubt, look around!\""
            p suspicious "I don't think that rhymes."
            t annoyed "Well, it was supposed to, but I reworded it in my head before saying it, so now it doesn't."
            t "WHATEVER!"
            t crossedarms "Basically, if you keep trying random stuff, something's bound to work."
            p neutral "Okay."
            t annoyed "So... go do it already."
            p sad "Oh, right."
        return

    else:
        show posty neutral
        show toasty neutral
        t "I don't have any hints for you, sorry. You should never see this dialogue."
        p confused "Wuh oh."
        return
