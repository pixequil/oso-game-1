image cash_bundle_1:
    "items/cash_bundle.png"
    xalign 0.5
    yalign 0.55
    zoom 4.0

label money_get:
    if money == 0:
        "A player should never see this text."
    elif money == 1:
        show cash_bundle_1
        "You now have {b}some money{/b}!"
        hide cash_bundle_1
        return

