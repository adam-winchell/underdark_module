from webweb import Web

web = Web(
    adjacency=[
        [0, 1],
        [1, 2],
        [0, 4],
        [1, 5],
        [5, 6],
        [6, 7],
        [8, 9],
        [8, 10],
        [11, 12],
        [11, 4],
        [12, 4],
        [14, 15],
        [15, 5],
        [16, 15],
        [16, 17],
        [18, 19],
        [19, 20],
        [20, 21],
        [22, 4],
        [22, 19],
        [21, 19],
        [21, 23],
        [24, 4],
        [24, 25],
        [26, 27],
        [26, 28],
        [29, 23],
        [21, 29],
        [30, 2],
        [30, 5],
        [31, 10],
        [31, 32],
        [31, 33],
        [27, 4],
        [34, 20],
        [34, 35],
        [34, 36],
        [34, 37],
        [35, 36],
        [17, 29],
        [17, 8],
        [24, 19],
        [38, 35],
        [38, 4],
    ],
    display={
        "metadata": {
            "Zone": {"values": ["Twilight", "Dusk", "Gloom", "Shadow", "Void"]}
        },
        "nodes": {
            0: {
                "name": "Kua Toa Village",
                "Zone": "Twilight",
            },
            1: {
                "name": "The Great Sharay",
                "Zone": "Gloom",
            },
            2: {
                "name": "Skeletal Fisherman",
                "Zone": "Dusk",
            },
            3: {
                "name": "Enchanted Forest",
                "Zone": "Twilight",
            },
            4: {
                "name": "Elder Brain",
                "Zone": "Gloom",
            },
            5: {
                "name": "The Final Gauntlet",
                "Zone": "Gloom",
            },
            6: {
                "name": "Umbral Gauntlet 2",
                "Zone": "Gloom",
            },
            7: {
                "name": "Sword Wraith Warrior",
                "Zone": "Twilight",
            },
            8: {
                "name": "Roper Cavern",
                "Zone": "Gloom",
            },
            9: {
                "name": "The Mephitic Swamp",
                "Zone": "Shadow",
            },
            10: {
                "name": "The Court of Graz'zt",
                "Zone": "Dusk",
            },
            11: {
                "name": "The Mindflayer Outpost",
                "Zone": "Dusk",
            },
            12: {
                "name": "Dungeon of the Smiling One",
                "Zone": "Void",
            },
            13: {
                "name": "The Rot",
                "Zone": "Dusk",
            },
            14: {
                "name": "The Pit",
                "Zone": "Gloom",
            },
            15: {
                "name": "The Guild of Gloom",
                "Zone": "Gloom",
            },
            16: {
                "name": "Cave Spring",
                "Zone": "Dusk",
            },
            17: {
                "name": "Final Betrayal",
                "Zone": "Void",
            },
            18: {
                "name": "Oblex Party",
                "Zone": "Dusk",
            },
            19: {
                "name": "Juiblex's Plans",
                "Zone": "Dusk",
            },
            20: {
                "name": "Sulfurous Invasion",
                "Zone": "Twilight",
            },
            21: {
                "name": "Gnomish Village",
                "Zone": "Dusk",
            },
            22: {
                "name": "Baby Oblex",
                "Zone": "Twilight",
            },
            23: {
                "name": "Naga Hostages",
                "Zone": "Dusk",
            },
            24: {
                "name": "Behomoth Ooze",
                "Zone": "Twilight",
            },
            25: {
                "name": "Master of Golems",
                "Zone": "Twilight",
            },
            26: {
                "name": "Lost Goblins",
                "Zone": "Twilight",
            },
            27: {
                "name": "Tadpoles on the Mind",
                "Zone": "Dusk",
            },
            28: {
                "name": "The Broken Mountain",
                "Zone": "Dusk",
            },
            29: {
                "name": "Yuan-ti Ruins",
                "Zone": "Dusk",
            },
            30: {
                "name": "Umbral Gauntlet 3",
                "Zone": "Gloom",
            },
            31: {
                "name": "Ghost of a Drow Samurai",
                "Zone": "Twilight",
            },
            32: {
                "name": "The Valley of Spirits",
                "Zone": "Gloom",
            },
            33: {
                "name": "Ruins of XXX",
                "Zone": "Gloom",
            },
            34: {
                "name": "Stalking Nothic",
                "Zone": "Twilight",
            },
            35: {
                "name": "Orcus Stuff",
                "Zone": "Twilight",
            },
            36: {
                "name": "Shrine of Orcus",
                "Zone": "Twilight",
            },
            37: {
                "name": "Mystery of the Tanaruks",
                "Zone": "Twilight",
            },
            38: {
                "name": "Great Wyrm Shadow Dragon",
                "Zone": "Twilight",
            },
        },
    },
)
if __name__ == "__main__":
    web.display.colorBy = "Zone"
    web.display.charge = 300
    web.display.showNodeNames = True
    web.display.linkStrength = 0.2
    web.display.linkLength = 30

    web.show()
