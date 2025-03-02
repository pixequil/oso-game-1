# throughout the game, the player can return to Toasty to receive hints. this file is jumped to when the player interacts with Toasty, and then sends the player back to mainstreet (which is where Toasty should always be accessed).
# the hints are listed in a weird, almost reverse walkthrough order here.
# since the hints are accessed via "call", they should all end with "return".

label toasty_hints:

    scene bg mainstreet
    
    if win_flag:
        show posty neutral
        show toasty smug5
        if finalehint and (nicestart > 15):
            t "Okay, okay, I get it, you love talking to me."
            t "Now go get some rest. Those park benches look like a great spot."
            return
        p "Hey Toasty, how\'s it going?"
        t "It\'s good. The weather is nicer than usual."
        p suspicious "I genuinely think that\'s the first time I\'ve managed to start a conversation with you without you insulting me almost immediately."
        if (nicestart == 0):
            t smug3 "What can I say, I\'m in a good mood right now…"
        elif (nicestart == 1):
            t smug3 "Nah, I think I did, like, once."
        else:
            t smug3 "No, I definitely have. Like [nicestart] times."
            p suspicious "You were counting?"
            t turned2 "No..."
            p "Right..."
        t smug3 "Y\'know, you aren\'t half bad."
        p "Oh? And what makes you say that?"
        t laugh "Well, you seemed pretty committed to this one delivery, you even vandalized a painting for it!"
        t "Blue Tile couldn\'t stop crying about it afterwards. I would say the entire town thinks you\'re a villain now, but no one liked that painting to begin with…"
        t enthused "Y'know, part of me kind of admires it."
        p "The delivery?"
        t annoyed "No, you idiot. Your commitment to the delivery."
        t "And also the painting vandalization, but mostly the commitment."
        p "Oh…"
        p happy "Well, I finally finished it! Got the package where it\'s meant to be. And I got a shout out from Crayon Box herself!"
        if finalehint:
            t neutral2 "What\'re you gonna do now? Head back to the dusty street corner I know you live at, and {b}{color=#FFFF00}nap{/color}{/b} while you wait for another package? Go on a nice walk {b}{color=#FFFF00}in the park{/color}{/b}? Vandalize another painting?"
        else:
            t neutral2 "What\'re you gonna do now? Head back to the dusty street corner I know you live at, and nap while you wait for another package? Go on a nice walk in the park? Vandalize another painting?"
        p "Hah… those all sound nice. I don\'t know what I\'m going to do, but at the end of the day, I\'m just glad to have that delivery over and done with."
        t smug "You do sound relieved, too bad relaxing would get you confused for a normal mailbox and you'd probably get an envelope or two thrown at you."
        p "Hehe, I\'ll just have to find somewhere a mailbox wouldn\'t be then… I\'ll see you around Toasty!"
        t enthused "See you around, get hit in the face with a package for me!"
        p annoyed "Yeah, and how about you go take a swim."
        $ finalehint = True
        $ nicestart += 1
        return

    elif party_bs:
        show posty neutral
        show toasty neutral
        show bs follow behind posty with moveinleft
        $ nicestart += 1
        bs "Hello!"
        t smug "Who is this you brought along to follow you, Posty?"
        bs "Lady, I'm gonna be the next big thing!"
        p happy "We're looking for someone who wants to promote them."
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
        p "Oof, am I glad I made Retainer happy again. I can't wait to take a nap."
        t pointandlaugh "Ohohoho, what do we have here? Thinking of turning truant for the treacherous mistress known as sleep?"
        p annoyed "Stop speaking like a Victorian; you don't appear to have anything better to do."
        t smug "I concede that I am not the shiniest appliance in this messy kitchen we call life, but I don't recall you having a keen interest in lepidopterology."
        p suspicious "Lepidoptrolowhat? Is that even a word or are you trying to get one up on me?"
        t crossedarms "Hmph: if you were even a hundredth as diligent and scholarly as me, you would've realized that lepidopterists would kill to even touch the {b}package{/b} you hold right now."
        t smug "Who knows, if you are careless enough, maybe even little old me may take a swipe at it!"
        p astonished "OH RIGHT, THE PACKAGE!!!"
        p neutral "Sorry. Been a long day."
        t enthused "Well, what are you waiting for, dummy!"
        return

    elif item.makeshift_trophy:
        show posty neutral
        show toasty smug
        t "You have a nice trophy with ya. Whatcha get it for, participation?"
        p "No, just made it myself."
        t enthused "What you going to do with it?"
        p "Dunno, probably put it on a shelf at home; pretend to be a winner and show it off."
        t smug "Well, it would severely clash with the decor, especially with the grey curtains and general lack of furniture."
        p annoyed "Rude. Also how did you know what my-"
        t crossedarms "Keep your petty questions for later! You said this thing made you feel like a winner, right?"
        p suspicious "Yeah?"
        t "Well, I think there is someone who would like that feeling, someone down on their luck..."
        t enthused "A big hulking trophy would bring their spirits right up!"
        show toasty angry
        p neutral "Who? You?"
        t smug2 "Sister, my spirits are already up watching you wander around this street."
        return

    elif item.scrapmetal:
        show posty angry
        show toasty pointandlaugh
        t "SCRAP METAL!!!"
        t "YOU SPENT ALL YOUR MONEY ON SCRAP METAL!!!"
        t "AAAAHAHAHAHAHAHA!!!"
        p "Guessing you had something to do with this?"
        t "HAHAHAHAHAHA..."
        t enthused "Aaahhh..."
        t smug "No, I didn't."
        p "Right."
        t neutral "No, really."
        p "Well, what am I supposed to do with this?"
        if whatdoilooklike:
            t annoyed "What do I look like, a {b}{color=#FFFF00}tool{/color}{/b}? Figure it out yourself!"
        else:
            t annoyed "What do I look like, a guide book? Figure it out yourself!"
        $ whatdoilooklike = True
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
        p concerned "Toasty, don't-"
        hide badpainting
        "Toasty took the {b}napkin \"painting!\"{/b}"
        p sad "That was a painting someone kindly gifted me!"
        t annoyed "What, this tatty thing? A painting?"
        t "Puhlease with the jokes."
        p annoyed "Just look at it."
        show badpainting
        t smug "You call this a painting?!"
        t "Honestly, you better not make any enemies if this counts as a gift."
        t "I almost feel sorry for you."
        p "Ha. Ha. Ha."
        t "So what landfill did you get this from?"
        p "Some poor starving artist who hadn't eaten a crumb for months. They looked absolutely disheveled."
        p "I got this avante garde piece-"
        t laugh "Nice save!"
        p "After giving them a bag of chips. You should've seen them pour out their gratitude."
        p "That is how I got this thing."
        p "Admittedly, it's not great, but it clearly meant a lot to them. They called it their \"greatest work!\""
        t neutral "Well gee, I feel bad now."
        show badpainting
        "Toasty gave back the {b}napkin \"painting!\"{/b}"
        hide badpainting
        p "You feeling sorry for someone? That's character development I thought I'd never see!"
        t laugh "Bad that you gave away a perfectly good bag of chips for this!"
        t "It would benefit everyone if you never become an art critic, because your taste is objectively HORRIBLE!"
        p angry "Wow. I am so disappointed."
        t "Now if you excuse me, I need to organize a strategy meeting ASAP."
        t turned "Alright, how to make this trash into treasure, Toastmeister?"
        if toastmeister:
            p "You still sticking with Toastmeister?"
        else:
            p annoyed quiet "..."
        t "Well, who would pay a huge, huuuge amount for worthless scribbles?"
        t "Well, it would be anyone who needed to look all snooty and fancy!"
        t "But how, Toaster the Moster? Surely their superior tastes would stall us from making millions via such low tactics?"
        t "Well, what if they want to be fooled?"
        t "If it appears sufficiently advanced and esoteric, then they can simply ramble randomly about its various \"nuances.\""
        t "As a wise guy once said, \"Eye is in the art of the beholder\" or something deep like that!"
        t "If I had an approximation of art, I would go towards the snootiest person in the area!"
        t "They wouldn't let go of an opportunity to act high and mighty over lowly plebs about the \"beauties of maximal-detrius-desalination-debris murals in an abstract and expressive makeshift canvas in the modern era,\" they would make entire reviews about it!"
        t "Before we can say \"easel\", we will be super rich beyond our wildest dreams!!"
        t "Ohohoho, can't wait to see her look when I roll past her in a flexed out car with MY NAME ON IT!"
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
        t turned2 "That\'s a real loss for you, you could\'ve gotten a drink from there! Or at least given it to someone else who deserves it."
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
        p concerned "I bonked my head on the pizza-eating painting just now."
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
        show toasty neutral2
        $ nicestart += 1
        t "Hey Posty."
        p "Remember that boring painting about the blue army and the red army in the art gallery?"
        t "From like... 5 minutes ago?"
        p "Y\'know, the one that used to be black and white and really violent?" 
        t "Yeah, what about it?"
        p "Well let's just say, I don\'t think it\'s gonna get any more visitors after... a certain \"green\" incident."
        t "You threw green paint on a rare expensive painting? Important as an item of an era's culture and an artistic depiction of old history?"
        p angry "Technically, it wasn't green {i}paint{/i}, but..."
        p "Never mind, I just realized you don't care."
        t smug "I'd be extremely offended if I wasn't excited about you being thrown in jail."
        t enthused "Is the painting that got damaged ok?"
        p "Ehhhh, if you call recolored green \"ok,\" then yeah."
        t smug2 "Might as well check it out before the curators take it down."
        p happy "Not before I get it first!"
        return
    
    elif item.battery:
        show posty happy
        show toasty neutral
        p "Duh duh dum, dum diddly dum-"
        t smug2 "Hello my most perfidious postbox."
        p annoyed "Oh no, not again. {w}{i}\(cough){/i} {w}So what do you need?"
        t crossedarms "I was just wondering what you have in your hand."
        show battery_center
        p suspicious "Just a battery."
        t angry "That's it? I thought it would be something more valuable."
        p concerned "I dunno, something intrigues me about it."
        t smug "Could it be its satisfying weight, finely crafted out of the earth's treasures of lithium and manganese?"
        t smug3 "Maybe its cold metal gives tingles as though a hidden memory is unlocked from your steely heart."
        p confused "Why are you being so fancy with the descriptions?"
        t annoyed "Shut up, I'm talking here."
        t smug5 "It must be the tasteful interspersion of Helvetica and Arial in the phrase \"PLEASE DON'T EAT, INGEST, OR SWALLOW THIS;\" gives the message some much needed depth."
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
        hide battery_center
        hide posty with moveoutleft
        t neutral "Could I have sabotaged myself again?"
        t turned2 "No! Of course not! You're too smart to do that!"
        return

    elif item.imaginary_lighter:
        show posty neutral
        show toasty annoyed
        t "What's it now, blue box?"
        p "It's Posty."
        t "Well, do I look like care?"
        t smug2 "So, what do you want?"
        p concerned "I got this… thing. It makes fire."
        p suspicious "You like fire, right?"
        t smug "Maybe I do, why?"
        t smug3 "Do you want to impress me with a gift? Even after all our petty squabbles?"
        t smug5 "Aww, Posty, you\'re warming my dear, frigid heart…"
        show toasty crossedarms
        show imaginary_lighter
        p annoyed "Whatever, Toasty. Just what do you think of this?"
        t laugh "BWA HA HA HA!"
        show posty concerned
        t smug3 "I think I underestimated your stupidity. If you tried to roast this toast with THAT, it would turn back into bread!"
        p "What? Just look-"
        t smug "There\'s nothing in your hand, you absolute bag of hammers. I don't buy it. Do you really think you can show me air and I\'ll be impressed?"
        if saw.ahiss:
            t smug2 "You just can\'t leave me alone, can you?"
            p "I was just saying hi?"
            t "You hover and hover around me, like a crusty little dog begging for scraps."
            p "I couldn't care less about you."
            t smug "How many times have you sauntered up to this corner and started shooting the breeze?"
            p "Uh…"
            t smug3 "Don\'t start counting."
            p suspicious "What's with the dog comparisons?"
            t annoyed "I can\'t stand dogs… there\'s only one animal worse than them…"
            p "Wait, you hate dogs? What's next on your list, baby bunnies?"
            t smug "Ha! That was almost funny."
            t annoyed "No, the animals I loathe most of all are cats! A nothing-special clod like you would be in good company with one of those beasts!"
            t angry "They hiss and strut and prance, going \"Mine! Mine! Mine!\""
            show posty concerned
            t angry "They act like the whole world belongs to them, but they\'re really nothing special!"
            t angry "They aren\'t even noteworthy enough to be good for nothing. At least you can try to use their pathetic little claws as a letter opener! But nothing special! Nothing cool! Just the boring, medial tasks ever devised!"
            p "Wow, harsh."
            t turned2 "I needed to blow off some steam there. Feel free to walk away from me."
            p "I will."
            return
        else:
            p "But it's not air! How come I can see it and you can't?"
            t laugh "Maybe it's imaginary. Like your brain cells."
            p concerned "That doesn't make any sense. I got it from a liar in the museum. They handed it right to me."
            t enthused "Maybe you only got it, because you believe it to be real as a physical construct."
            t "Perhaps whoever gave it to you was able to will it into existence as a contradiction to the laws of nature and science."
            p "That doesn't make any sense unless both of us were completely insane."
            t "Oh, you make this way too easy for yourself."
            t smug5 "Alright everyone, Posty's gone crazy. She's coco bananas!"
            p annoyed "Who are you talking to?"
            t "For all we know, she's probably imagining us all as humans instead of objects!"
            p concerned "Humans?"
            t smug "Oh y'know, like that cat from the museum, except more freakish."
            t turned2 "Anyway, I've got no business talking to you anymore. Shoo."
            return
    
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
        t annoyed "What the toast is a heavier?"
        p "It apparently {i}(pant){/i} sucks fire in."
        t "Really? You believe anything these days. Where'd you get this thing, the back alley? I've seen you walking around there!"
        p "I {i}(pant){/i} swear. It hurts..."
        t smug "Yadda yadda we get it, you are weak."
        t "Let me handle it."
        "Toasty took the {b}heavier!{/b}"
        hide heavier
        t angry "HOLY CRUNCH {i}(pant){/i} HOW DID {i}(pant){/i} YOU CARRY {i}(pant){/i} THIS?!"
        p astonished "I don't know?! Probably willpower or something like that."
        t "Well {i}(pant){/i} I need {i}(pant){/i} to consult someone pronto."
        t turned "Oh boy."
        t "This is a pretty awkward situation {i}(pant){/i} I have gotten myself in {i}(pant){/i} Toastmeister!"
        $ toastmeister = True
        t "Well Mailmouth did say {i}(pant){/i} this thing can suck fire up!"
        t "So we need to find {i}(pant){/i} some fire {i}(pant){/i} to suck up!"
        t "There was a {i}(pant){/i} painting {i}(pant){/i} that had {i}(pant){/i} some fire {i}(pant){/i} in the gallery."
        t "Yeah {i}(pant){/i} that'll work."
        t "Let's give this {i}(pant){/i} back and maybe we'll get it back when it's filled with fire."
        show heavier
        t annoyed "Here {i}(pant){/i} you go."
        "You have received the {b}heavier!{/b}"
        hide heavier
        t "Don't do that to me ever again."
        return

    elif bt_distracted:
        if toastybtdistracted == 0: 
            show posty astonished
            show toasty enthused
            $ nicestart += 1
            t "Woah Posty, what's the rush?"
            p "This is hard to explain, but I may have bribed a guy to make an opening for me to steal a painting by distracting another guy and I sorta just walked away."
            t neutral2 "Huh? Why?"
            p sad "I don't know, I'm scared! What if I get caught?"
            t angry "Posty, now is not the time to be getting cold feet! Seriously."
            t "You could do any number of things while they\'re distracted!"
            t "Why would you go through all this effort of smuggling soup into the museum just to do nothing? Aren\'t you going to do something with it?" 
            t "You baffle me on new levels I never thought existed. Why did you just run away?!"
            t "The painting you're stealing is unguarded! Just do whatever you want to do, stop waiting your time!"
            $ toastybtdistracted += 1
            return
        if toastybtdistracted == 1:
            show posty concerned
            show toasty angry
            t "You're still out here?"
            t "Stop talking to me and go steal that painting! You\'re wasting your time!"
            $ toastybtdistracted += 1
            return
        else:
            show posty astonished
            show toasty angry
            t "Posty, seriously, if you\'re not going to do it, I'll snatch that soup from you and steal that painting myself!"
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
        if rusty:
            t pointandlaugh "Hah! Just the thought of you getting everything {b}{color=#FFFF00}rusty{/color}{/b} makes me chuckle!"
        else:
            t pointandlaugh "Hah! Just the thought of you getting everything rusty makes me chuckle!"
        $ rusty = True
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

    elif quest.paintings and (quest.moneys == False) and (money == 4):
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

    elif quest.paintings and (quest.money_food == False):
        show posty neutral
        show toasty neutral2
        if binoc_obsessed2:
            p "Binoculars says to bonk my head into paintings."
            p angry "There is no way I'm doing that."
            t pointandlaugh "I think it would be funny!"
        else:
            $ nicestart += 1
            t "What'cha got there?"
            p "Gold spray paint."
            t smug3 "Wanting to get into mural art, Posty?"
            p concerned "No, I'm just holding onto it. I'm not sure what to do with it though."
            t enthused "Maybe you need to get some inspiration."
            p happy "Like in the art museum?"
            show posty angry
            t smug2 "I was actually thinking about you ruminating in a hole in the ground, but the museum works too."
            p "I already did that."
            t smug "Ruminated in a hole in the ground?"
            p "Got inspired in the museum. And I got reprimanded, and now I have this gold spray paint."
            t annoyed "Oh right."
            t smug3 "Well, do you feel done in the museum?"
            p suspicious "I guess there was that super sus hotdog painting..."
            show posty angry
            t pointandlaugh "Someone's hungry!!!"
            if binoc_obsessed:
                t smug2 "You and that {b}{color=#FFFF00}Binoculars{/color}{/b} guy must be obsessed with it or something!"
                $ binoc_obsessed2 = True
            else:
                t smug2 "You and that Binoculars guy must be obsessed with it or something!"
            $ binoc_obsessed = True
            p "Okay, whatever."
        return

    elif quest.paintings and quest.bs and quest.money_food:
        show posty neutral
        show toasty crossedarms
        if (moolah == False):
            $ nicestart += 1
            t "You sound like you're carrying a lot of gold! And not just that gold spray paint..."
            t enthused "Moolah!!!"
            p angry "Yeah, it's what happens when I'm nice to people. You should try it."
            t smug "Or you could try to get richer."
            p neutral "That's your first idea."
            t "Yeah."
            t smug2 "I mean, it'd be pretty easy."
            $ moolah = True
        t smug3 "You haven't noticed all the random money lying around on the ground? It's practically asking to be picked up!"
        if (money > 2):
            p "Actually, I have."
            t annoyed "Well, you missed a spot."
            if missedaspot:
                p astonished "WHERE???"
                if item.cash_main:
                    t turned "I think I saw it in the alley?"
                else:
                    t angry "LITERALLY RIGHT BEHIND YOU!!!"
                p "Oh."
            $ missedaspot = True
        p "Guess I'll have a look."
        return

    elif paintings == 3 and (quest.paintings == False):
        show posty suspicious
        show toasty angry
        $ nicestart += 1
        if (easels_bother == False):
            t "\"Make A Walkway! Take Them Away!\""
            p "Whoa, Toasty, what are you up to?"
            t crossedarms "Isn\'t it obvious?"
            t enthused "I\'m protesting." 
            extend smug5 " Because I\'m a good object."
            p "Debateable."
            p "What is this protest about?"
            t turned "The museum entrance is SWAMPED with blank easels. I want them gone! They\'re taking up precious legroom." 
            p annoyed "That\'s what this is about? Legroom? Seriously?"
            t enthused "Yep! If I yell loud enough, someone is bound to do something about those easels." 
            t angry "\"Easels Be Gone, "
            extend neutral2 "uh…"
            extend angry "Something That Rhymes With Gone!\""
            t neutral2 "What have you been doing?"
            p concerned "I've stolen three paintings in like an hour."
            t neutral "Why?"
            p "They inspired me too much. I felt like taking them for my artistic journey."
            t smug "More like a kleptomaniac journey."
            t smug "Speaking of which, I used to steal paintings all of time. Four of them actually! Just one more than you!"
            p annoyed "No, you haven't, Toasty. You're just saying that to annoy me."
            t pointandlaugh "And it's clearly working!"
            t neutral "Seriously though, those easels are bothering me."
        else:
            t neutral "Seriously though, those {b}{color=#FFFF00}easels{/color}{/b} are bothering me."
        p annoyed "The strangest things bother you, Toasty."
        t pointandlaugh "Called yourself strange! Ha!"
        $ easels_bother = True
        return

    elif paintings == 2:
        show posty neutral
        show toasty annoyed
        t "I swear Posty, wherever I go, there you are."
        p "You don't go anywhere. I've haven\'t seen you leave this corner all day."
        t "I'm busy looking busy. What have you been doing?"
        t neutral2 "Hey, where did you get those paintings?"
        p suspicious "Why do you care?"
        t smug3 "Because I remember seeing those in the museum, so I'm wondering how you got them."
        show toasty smug4
        p "Well, they are from the museum, but I got them through completely legal methods."
        t smug "Even if that's true, that's an embarrassingly low amount of paintings you have."
        p "What do you mean? I think it's an impressive feat."
        t smug2 "You should've stolen three. I\'ve stolen three paintings! Why not you?"
        if toastytwopaintings:
            p "I thought you said you stole two paintings-{nw}"
        t enthused "Everyone knows that having three paintings means you are a true art connoisseur, only two must mean you don't care about the arts."
        p "Well, how would I get another painting?"
        t neutral "The museum has three main exhibits, so you can probably get a third painting from one of the exhibits, preferably one you haven't already “legally” taken a painting from."
        t smug2 "Or you could buy online and skip the possibility of being arrested altoge-"
        p "OK thanks, see you later."
        t turned "He he he, good work Toasty. Posty's lack of patience will be her undoing."
        return

    elif paintings == 1:
        show posty annoyed
        show toasty crossedarms
        t "Well, well, well, look who decides to darken my doorstep once again."
        p "You don\'t have a door. You just stand in the street all day."
        t angry "At least I have a more interesting life than {i}you.{/i}"
        p angry "Oh yeah? Have you ever stolen a painting before?"
        t "Of— of course I have! Actually, I\'ve stolen {i}two{/i} paintings!"
        $ toastytwopaintings = True
        t annoyed "I don't do it anymore because painting stealing is lame and boring because museums are lame and boring."
        t pointandlaugh "But then again, I guess you\'d fit right in there, huh? Hahahah!"
        t "Go back to hanging around those lame and boring museum exhibits! Because you\'re lame!"
        p annoyed "And boring?"
        t angry "Ugh! I wanted to say it."
        return

    elif item.scrap_trophy:
        show posty neutral
        show toasty enthused
        show scraptrophy
        t "Your trophy sucks."
        p angry "Can you be nice, like, ever?"
        t "Seriously, who would want a trophy like that?"
        t pointandlaugh "Hah! It should be in a museum!!!"
        return
    
    elif quest.bs:
        show posty neutral
        show toasty neutral
        $ nicestart += 1
        t "You deal with that Brand Soda guy yet?"
        p "Yeah. We found some kid to be their manager, to some degree."
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
            t annoyed "Well, it was supposed to, but I reworded it in my head before saying it and..."
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
