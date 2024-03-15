# throughout the game, the player can return to Toasty to receive hints. this file is jumped to when the player interacts with Toasty, and then sends the player back to mainstreet (which is where Toasty should always be accessed).
# the hints are listed in a weird, almost reverse walkthrough order here.
# since the hints are accessed via "call", they should all end with "return".

label toasty_hints:

    scene bg mainstreet
    
    if win_flag:
        show posty neutral
        show toasty smug5
        p "Hey Toasty, how\'s it going?"
        t "It\'s good. The weather is nicer than usual."
        p suspicious "I genuinely think that\'s the first time I\'ve managed to start a conversation with you without you insulting me almost immediately."
        t smug3 "What can I say, I\'m in a good mood right now…"
        t "Y\'know, you aren\'t half bad."
        p "Oh? And what makes you say that?"
        t laugh "Well, you seemed pretty committed to this one delivery, you even vandalized a painting for it!"
        t "Blue Tile couldn\'t stop crying about it afterwards. I would say the entire town thinks you\'re a villain now, but no one liked that painting to begin with…"
        t enthused "Y'know, part of me kind of admires it."
        p "The delivery?"
        t annoyed "No, you idiot. Your commitment to the delivery."
        t "And also the painting vandalization, but mostly the commitment."
        p "Oh…"
        p happy "Well, I finally finished it! Got the package where it\'s meant to be. And I got a shout out from Crayon Box herself!"
        t neutral2 "What\'re you gonna do now? Head back to the dusty street corner I know you live at, and nap while you wait for another package? Go on a nice walk in the park? Vandalize another painting?"
        p "Hah… those all sound nice. I don\'t know what I\'m going to do, but at the end of the day, I\'m just glad to have that delivery over and done with."
        t smug "You do sound relieved, too bad relaxing would get you confused for a normal mailbox and you'd probably get an envelope or two thrown at you."
        p "Hehe, I\'ll just have to find somewhere a mailbox wouldn\'t be then… I\'ll see you around Toasty!"
        t enthused "See you around, get hit in the face with a package for me!"
        p annoyed "Yeah, and how about you go take a swim."
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
        show badpainting
        p "Hey Toasty, check this out!"
        t pointandlaugh "A napkin? How considerate!"
        t "I just had a good chocolate donut!"
        p concerned "Toasty don't-"
        hide badpainting
        "Toasty took the {b}napkin \"painting\"{/b}!"
        p sad "That was a painting someone kindly given me!"
        t annoyed "What, this tatty thing; a painting?"
        t "Puhlease with the jokes."
        p annoyed "Just look at it."
        show badpainting
        t smug "You call this a painting?!"
        t "Honestly you better not make any enemies if this counts as a gift."
        t "I almost feel sorry for you."
        p "Ha. Ha. Ha."
        t "So what landfill did you get this from?"
        p "Some poor starving artist who hadn't eaten a crumb for months. They looked absolutely disheveled."
        p "I got this avante garde piece-"
        t laugh "Nice save!"
        p "After giving them a bag of chips, you should've seen them pour out their gratitude."
        p "This is how I got this thing."
        t neutral "Damn, I feel bad now-"
        show badpainting
        "Toasty gave back the {b}napkin \"painting\"{/b}!"
        hide badpainting
        p "You feeling sorry for someone? That's character development I thought I'd never see!"
        t laugh "Bad that you gave away a perfectly good bag of chips for this!"
        t "It would benefit everyone if you never become an art critic, because your taste is objectively HORRIBLE!"
        p angry "Wow. I am so disappointed."
        t "Now if you excuse me, I need to organize a strategy meeting ASAP."
        t turned "Alright, how to make this trash into treasure, Meisteroony?"
        p annoyed quiet "..."
        t "Well, who would pay a huge, huuuge amount for worthless scribbles?"
        t "Well it would be anyone who needed to look all snooty and fancy!"
        t "But how, Toaster the Moster? Surely their superior tastes would stall us from making millions via such low tactics?"
        t "Well what if they want to be fooled?"
        t "If it appears sufficiently advanced and esoteric, then they can simply ramble randomly about its various \"nuances.\""
        t "As a wise guy once said, eye is in the art of the beholder or something deep like that!"
        t "If I had an approximation of art, I would go towards the snootiest person in the area!"
        t "They wouldn't let go of an opportunity to act high and mighty over lowly plebs about the \"beauties of maximal-detrius-desalination-debris murals in an abstract and expressive makeshift canvas in the modern era\", they would make entire reviews about it!"
        t "Before we can say \"easel\", we will be super rich beyond our wildest dreams!!"
        t "Ohohoho can't wait to see her look when I roll past her in a flexed out car with MY NAME ON IT!"
        t "Ahhhhh, it would be a beautiful plan! Watching the blue block sadly walk around from the comfort of my sofa."
        t "Now to get that napkin back and fufill all my dreams..."
        t smug2 "I would looove to eat another waffle with triple syrup, but I have no napkin."
        t "Can I borrow yours?"
        p neutral -quiet "No."
        t angry "DAMNIT THIS PLAN WAS SUPPOSED TO BE FOOLPROOF!"
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
        t "It\'s you, my good \'ol pal, post-it note!"
        p annoyed "It\'s Posty, Toaster."
        t smug3 "Yeah I\'m just joking around! Learn to have some humor."
        t angry "Wait, did you seriously call me Toaster?"
        p "Yeah whatever. Anyways, I saw this secret room with a vending machine in it or... whatever."
        t annoyed "You saw a vending machine and you {b}didn\'t use it?!{/b} Why not dummy!?"
        p sad "Well… I thought it was some ordinary vending machine, so I didn\'t take some time to investigate it."
        t turned2 "That\'s a real loss for you, you could\'ve gotten a drink from there! Or at least give it to someone else who deserves it."
        p neutral "Hm... I suppose. I\'ll get going now."
        show posty annoyed
        t pointandlaugh "Yeah whatever. Just go already and stop wasting my time!"
        p "Uggh, no drink for you then."
        return

    elif food_switch and (quest.money_food == False) and (saw.janitors == False):
        show posty zany
        show toasty smug2
        p "Woaaaah I think I am seeing stars!"
        t "What is up..."
        t neutral "Girl, are you alright?"
        p concerned "I bonked my head on the plaque next to the pizza-eating painting just now."
        p sad "It hurts."
        t "Darn..."
        t pointandlaugh "Looks like I have an advantage against my hated blue rival!"
        t smug "Excuse me, I need to do another planning session in secret!"
        show toasty turned
        p angry quiet "..."
        t turned "What up Toastmeister!"
        if toastmeister:
            p -quiet "You still sticking with Toastmeister?"
        t "The blue buffoon doesn't understand the significance of that painting!"
        t "And no, we aren't just talking about its culinary delights!"
        p -quiet "Ha ha ha. You know I can hear you-"
        t "If my detective skills are correct (and I have no reason to doubt my glorious abilities), she must have revealed a secret passageway!"
        t "And without realizing, too!"
        t turned2 "Ahh, elementary my pop up Watson!"
        t turned "To think she'd find a secret passage and just walk right past it!"
        t turned2 "Well, if I was there, I surely wouldn't have made such a grave error."
        t turned "Genius! You deserve a raise for such logic."
        t turned2 "Oh, I don't deserve such praise, I need to at least thank my mother."
        t "Now, lets keep it away from prying ears!"
        t smug3 "Soooooo, how is the weather, my courier countercompanion?"
        p "I'm walking away."
        return

    elif scanter_green and (quest.painting_war == False):
        show posty neutral
        show toasty neutral
        t "hint for if Palettette has turned the painting green" #222
        return
    
    elif item.battery:
        show posty happy
        show toasty neutral
        p "Duh duh dum, dum diddly dum-"
        t smug2 "Hello my most perfidious postbox."
        p annoyed "Oh no, not again. {w}{i}\[cough]{/i} {w}So what do you need?"
        t crossedarms "I was just wondering what you have in your hand."
        show battery_center
        p suspicious "Just a battery."
        t angry "That's it? I thought it would be something more valuable."
        p concerned "I dunno, something intrigues me about it."
        t smug "Could it be its satisfying weight, finely crafted out of the earth's treasures of lithium and manganese?"
        t smug3 "Maybe its cold metal gives tingles as though a hidden memory is unlocked from your steely heart."
        p confused "Why are you being so fancy with the descriptions?"
        t annoyed "Shut up, I'm talking here."
        t smug5 "It must be the tasteful interspersion of Helvetica and Arial in the phrase \"PLEASE DON'T EAT, INGEST, OR SWALLOW THIS\"; gives the message some much needed depth."
        p concerned "You're reading too much into this."
        t pointandlaugh "How else could such a nitwit like you get so tasteful?"
        p annoyed quiet "..."
        t neutral quiet "..."
        t -quiet "Joking, joking."
        t "Besides, why'd you come to me about it?"
        p concerned -quiet "I don't know. I thought a good walk could help me decide what to do with it."
        t smug "Wellll-"
        p suspicious "Well?"
        t neutral"Give me a second, I have a call."
        t turned "Looks like my cuboid companion has made a major misstep: wasting valuable energy on idle walking!"
        p confused "...wait what?"
        t "I know the quality of art has declined rapidly in the last decade or so, but I don't recall there being a battery exhibit inside."
        t "Think Toasty, who would lose such an item there?"
        t "Maybe an artist too engrossed in their crafts dropped it..."
        t "Yes! You are such a genius, Toastmeister!"
        p annoyed "Really? Toastmeister?"
        $ toastmeister = True
        t "All we have to do is make sure our friend doesn't eavesdrop and we're golden!"
        t enthused "So whatcha going to do with the battery?"
        hide posty with moveoutleft
        hide battery_center
        t neutral "Could I have sabotaged myself again?"
        t turned2 "No! Of course not! You're too smart to do that!"
        return

    elif item.imaginary_lighter:
        if saw.ahiss:
            show posty neutral
            show toasty neutral
            t "hint for if you have the imaginary lighter" #163
            return
        else:
            show posty neutral
            show toasty neutral
            t annoyed "what's it now... blue box"
            p annoyed "it's posty..."
            t angry "well do i look i care?"
            t annoyed "so what do you want?"
            p "somehow i got this"
            t annoyed "uhh"
            t laugh "i think may have underestimated your stupidity"
            p concerned "uhh it's an imaginary lighter"
            t annoyed "well your brain is as non-existent"
            t smug "like that cat from the museum"
            t turned2 "anyway shoo."

    
    elif item.heavier:
        show toasty crossedarms
        show posty concerned
        t "What's up-"
        p "So. Heavy."
        p sad "{i}(cough cough){/i}"
        t neutral "Posty, are you alright?"
        t neutral2 "Not that I care or anything, but you collapsing in front of me would be really weird."
        show heavier
        p "I have been carrying this heavier."
        t annoyed "What the hell is a heavier?"
        p "It apparently {i}(pant){/i} sucks fire in."
        t "Really? You believe anything these days. Where'd you get this crap, the back alley? I've seen you walking around there!"
        p "I {i}(pant){/i} swear. It hurts..."
        t smug "Yadda yadda we get it, you are weak."
        t "Let me handle it."
        "Toasty took the {b}heavier!{/b}"
        hide heavier
        t angry "HOLY CRAP {i}(pant){/i} HOW DID {i}(pant){/i} YOU CARRY {i}(pant){/i} THIS?!"
        p astonished "I don't know?! Probably willpower or something like that."
        t "Well {i}(pant){/i} I need {i}(pant){/i} to consult someone pronto."
        t turned "Oh boy."
        t "This is a pretty awkward situation {i}(pant){/i} I have gotten myself in {i}(pant){/i} ToastMaestro!"
        t "Well Mailmouth did say {i}(pant){/i} this thing can suck fire up!"
        t "So we need to find {i}(pant){/i} some fire {i}(pant){/i} to suck up!"
        t "There was a {i}(pant){/i} painting {i}(pant){/i} that has {i}(pant){/i} some fire {i}(pant){/i} in the gallery."
        t "Yeah {i}(pant){/i} that'll work."
        t "Let's give this {i}(pant){/i} back and maybe we'll get it back when it's filled with fire."
        show heavier
        t annoyed "Here {i}(pant){/i} you go."
        "You have received the {b}heavier!{/b}"
        hide heavier
        t "Don't do that to me ever again."
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
        show posty annoyed
        show toasty crossedarms
        t "Well, well, well, look who decides to darken my doorstep once again."
        p "You don\'t have a door. You just stand in the street all day."
        t angry "At least I have a more interesting life than {i}you.{/i}"
        p angry "Oh yeah? Have you ever stolen a painting before?"
        t "Of— of course I have! Actually, I\'ve stolen {i}two{/i} paintings!"
        t annoyed "Besides, painting stealing is lame and boring because museums are lame and boring."
        t pointandlaugh "But then again, I guess you\'d fit right in there, huh? Hahahah!"
        t "Go back to hanging around those lame and boring museum exhibits! Because you\'re lame!"
        p annoyed "And boring?"
        t angry "Ugh! I wanted to say it."
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
