
image inventory:
    "inventory.png"

screen inventory_screen:
    add "inventory"

    imagebutton:
        idle "inventory"
        action NullAction()

    showif item.butterfly_package:
        imagebutton:
            idle "butterfly_package"
            xalign 0.5
            yalign 1.3
            action Notify("Butterfly package, addressed to Crayon Box, at the dome west of here.")

    showif (item.painting_blue) and (quest.paintings == False):
        imagebutton:
            idle "inv blue"
            xalign 0.05
            yalign 0.75
            action Notify("From the Blue Exhibit. Makes me feel inspired!")
        
    showif item.red_cash:
        imagebutton:
            idle "inv redcash"
            xalign 0.05
            yalign 0.95
            action Notify("Red cash. Fake money I found in the Blue Exhibit.")

    showif item.ladle_empty:
        imagebutton:
            idle "inv ladle empty"
            xalign 0.05
            yalign 0.65
            action Notify("The ladle Red Tile used to splash miso soup on the blue painting!")

    showif item.ladle_full:
        imagebutton:
            idle "inv ladle full"
            xalign 0.05
            yalign 0.65
            action Notify("I filled it with miso soup! Why did I do that?!")

    showif (item.painting_war) and (quest.paintings == False):
        imagebutton:
            idle "inv war"
            xalign 0.1
            yalign 0.3
            action Notify("From the War Exhibit. Makes me feel inspired!")

    showif item.battery:
        imagebutton:
            idle "battery_center"
            xalign 0.1
            yalign 0.3
            action Notify("A battery I got from Ahiss's territory!")

    showif item.imaginary_lighter:
        imagebutton:
            idle "imaginary_lighter"
            xalign 0.1
            yalign 0.2
            action Notify("Imaginary lighter. Can be used to imaginary burn things.")

    showif item.heavier:
        imagebutton:
            idle "heavier"
            xalign 0.1
            yalign 0.2
            action Notify("Heavier. Opposite of a lighter. Removes fire.")

    showif (item.painting_food) and (quest.paintings == False):
        imagebutton:
            idle "inv food"
            xalign 0.24
            yalign 0.75
            action Notify("From the Food Exhibit. Makes me feel inspired!")

    showif item.notice:
        imagebutton:
            idle "notice"
            xalign 0.2
            yalign 0.5
            action Notify("Notice of reprimand. I feel so counterculture for having this!")

    showif item.spraypaint:
        imagebutton:
            idle "spraypaint"
            xalign 0.2
            yalign 0.5
            action Notify("Gold spray paint! I could make something look premium with this!")

    showif item.chips:
        imagebutton:
            idle "generichips"
            xalign 0.9
            yalign 0.15
            action Notify("Generi-Chips. I don't like these.")

    showif item.napkin:
        imagebutton:
            idle "inv badpainting"
            xalign 0.95
            yalign 0.2
            action Notify("A horrible \"painting\" drawn on a napkin. Uninspiring.")

    showif (money > 0) and (quest.moneys == False):
        imagebutton:
            xalign 0.5
            yalign 0.3
            idle "cash_total"
            action If((money < 4),Notify("Money I got somehow."),Notify("All of the money in the area."))

    showif party_bs:
        imagebutton:
            idle "inv bs"
            xalign 1.0
            yalign 1.0
            action Notify("My friend Brand Soda. Looking for a job.")

    showif item.scrapmetal:
        imagebutton:
            xalign 0.5
            yalign 0.25
            idle "scrapmetal"
            action Notify("Scrap metal. Raw material I don't know what to do with.")

    showif item.scrap_trophy:
        imagebutton:
            idle "inv trophy scrap"
            xalign 0.5
            yalign 0.3
            action Notify("A trophy. It's uninspired. Could use a little something.")

    showif item.makeshift_trophy:
        imagebutton:
            idle "inv trophy makeshift"
            xalign 0.5
            yalign 0.3
            action Notify("Makeshift trophy! Sure to make anyone's day!")

    imagebutton:
        xalign 1.0
        yalign 0.0
        idle "inv1"
        hover "inv2"
        action Hide("inventory_screen")

image inv blue:
    "painting_blue"
    zoom 0.5

image inv war:
    "war_painting_green"
    zoom 1.7

image inv food:
    "painting_food"
    zoom 0.4


image inv trophy scrap:
    "items/scraptrophy.png"
    zoom 4.5
image inv trophy makeshift:
    "items/makeshift_trophy.png"
    zoom 4.5

image inv bs:
    "talksprites/brandsoda_close.png"
    zoom 0.8

image inv redcash:
    "redcash"
    zoom 0.8

image inv ladle empty:
    "ladle_empty"
    zoom 0.5

image inv ladle full:
    "ladle_full"
    zoom 0.5

image inv badpainting:
    "badpainting"
    zoom 0.9
