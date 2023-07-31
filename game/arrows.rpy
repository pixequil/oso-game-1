image arrow up:
    "arrow.png"
    alpha 0.4

image arrow dn:
    "arrow up"
    rotate 180

image arrow rt:
    "arrow up"
    rotate 90

image arrow lt:
    "arrow up"
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
image pnav dn:
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
image pnav i:
    "minisprites/pnav dn.png"
    alpha 0.0

