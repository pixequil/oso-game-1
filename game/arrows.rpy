image arrow:
    "arrow.png"

image arrow half:
    "arrow"
    alpha 0.4

transform invis:
    alpha 0.0

transform dn:
    rotate 180

transform rt:
    rotate 90

transform lt:
    rotate 270

transform black:
    matrixcolor TintMatrix("000")

image pnav up:
    "minisprites/pnav up.png"
    pause 0.1
    ypos 4
    pause 0.1
    ypos 0
    repeat
image pnav rt:
    "minisprites/pnav rt.png"
    pause 0.1
    ypos 4
    pause 0.1
    ypos 0
    repeat
image pnav:
    "minisprites/pnav dn.png"
    pause 0.1
    ypos 4
    pause 0.1
    ypos 0
    repeat
image pnav lt:
    "minisprites/pnav rt.png"
    xzoom -1.0
    pause 0.1
    ypos 4
    pause 0.1
    ypos 0
    repeat

