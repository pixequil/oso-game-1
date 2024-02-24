image arrow up:
    "arrow.png"
    alpha 0.2

image arrow dn:
    "arrow up"
    rotate 180

image arrow rt:
    "arrow up"
    rotate 90

image arrow lt:
    "arrow up"
    rotate 270

image arrow up black:
    "arrow.png"
    alpha 0.2
    black

image arrow dn black:
    "arrow.png"
    rotate 180
    alpha 0.2
    black

image arrow lt black:
    "arrow.png"
    rotate 270
    alpha 0.2
    black

image arrow rt black:
    "arrow.png"
    rotate 90
    alpha 0.2
    black

transform black:
    matrixcolor TintMatrix("000")

image pnav up = ConditionSwitch(
    "party_bs == False","pnav up base",
    "party_bs == True","pnav up bs"
)
image pnav rt = ConditionSwitch(
    "party_bs == False","pnav rt base",
    "party_bs == True","pnav rt bs"
)
image pnav dn = ConditionSwitch(
    "party_bs == False","pnav dn base",
    "party_bs == True","pnav dn bs"
)
image pnav lt = ConditionSwitch(
    "party_bs == False","pnav lt base",
    "party_bs == True","pnav lt bs"
)

image pnav up base:
    "minisprites/pnav up.png"
    hop
image pnav rt base:
    "minisprites/pnav rt.png"
    hop
image pnav dn base:
    "minisprites/pnav dn.png"
    hop
image pnav lt base:
    "minisprites/pnav rt.png"
    xzoom -1.0
    hop

image pnav up i:
    "pnav up"
    alpha 0.0
image pnav rt i:
    "pnav rt"
    alpha 0.0
image pnav dn i:
    "pnav dn"
    alpha 0.0
image pnav lt i:
    "pnav lt"
    alpha 0.0

image bsnav:
    "minisprites/Brand_Soda.png"
    zoom 0.75
    pause 0.05
    yoffset -4
    pause 0.1
    yoffset 0
    pause 0.05
    repeat

image bsnav f:
    "bsnav"
    xzoom -1.0

image pnav up bs = Composite(
    (120, 212),
    (0, 0), "pnav up base",
    (60, 100), "bsnav"
)
image pnav rt bs = Composite(
    (176, 152),
    (0, 0), "pnav rt base",
    (0, 50), "bsnav f"
)
image pnav dn bs = Composite(
    (120, 212),
    (80, 0), "bsnav",
    (0, 0), "pnav dn base"
)
image pnav lt bs = Composite(
    (176, 152),
    (0, 0), "pnav lt base",
    (120, 40), "bsnav"
)


transform hop:
    pause 0.1
    yoffset 4
    pause 0.1
    yoffset 0
    repeat

image hitbox = ConditionSwitch(
    "devmode == False","hitboxf",
    "devmode == True","hitboxt"
)
image hitboxt = Solid("#ff00003c")
image hitboxf = Solid("#ff000000")
