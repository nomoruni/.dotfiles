from libqtile.config import Group, Match

# groups = []

group_names = ["1", "2", "3", "4", "5", "6", "7", "8", "9"]
group_labels = [" ", " ", " ", " ", " ", "󰿎 ", " ", " ", " "]
# group_layouts = ["monadtall", "monadtall", "monadtall", "monadtall", "monadtall", "monadtall",]


# for i in range(len(group_names)):
#     groups.append(
#         Group(
#             name=group_names[i],
#             label=group_labels[i],
#         ))

groups = [
        Group(
        name = group_names[0],
        label = group_labels[0],
        # matches=[Match(wm_class=["Firefox"])]
    ),
        Group(
        name = group_names[1],
        label = group_labels[1],
        # matches=[Match(wm_class=["Firefox"])]
    ),
        Group(
        name = group_names[2],
        label = group_labels[2],
        matches=[
            Match(wm_class="Navigator")
        ]
    ),
        Group(
        name = group_names[3],
        label = group_labels[3],
        matches=[
            Match(wm_class="Code")
        ]
    ),
        Group(
        name = group_names[4],
        label = group_labels[4],
        matches=[Match(wm_class=["libreoffice"])]
    ),
        Group(
        name = group_names[5],
        label = group_labels[5],
        matches=[
            Match(wm_class="vlc")
        ]
    ),
        Group(
        name = group_names[6],
        label = group_labels[6],
        matches=[
            Match(wm_class="Inkscape"),
            Match(wm_class="Gimp")
        ]
    ),
        Group(
        name = group_names[7],
        label = group_labels[7],
        matches=[
            Match(wm_class="VirtualBox Manager")
        ]
    ),
        Group(
        name = group_names[8],
        label = group_labels[8],
        matches=[Match(wm_class=["Windscribe"])]
    ),
]
