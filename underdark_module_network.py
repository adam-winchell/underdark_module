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
        [34, 36],
        [34, 37],
        [35, 36],
        [17, 29],
        [17, 8],
        [24, 19],
        [38, 35],
        [38, 4],
        [39, 28],
        [39,38],
        [40,28],
        [40, 10],
        [13, 36],
        [27,12],
        [7,32],
        [3,32],
        [19,4],
        [41, 2],
        [42,35],
        [42,10],
        [43,5],
        [43,44],
        [45, 3],
        [45,46],
        [46, 4],
        [10,47],
        [53,54],
        [55,28],
        [55, 21]
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
                "name": "Depths of the Mind",
                "Zone": "Void",
            },
            5: {
                "name": "The Final Gauntlet",
                "Zone": "Void",
            },
            6: {
                "name": "Fzbl",
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
                "Zone": "Gloom",
            },
            12: {
                "name": "Dungeon of the Smiling One",
                "Zone": "Shadow",
            },
            13: {
                "name": "The Rot",
                "Zone": "Dusk",
            },
            14: {
                "name": "The Pit",
                "Zone": "Twilight",
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
                "Zone": "Void",
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
                "Zone": "Gloom",
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
                "name": "The Broken Mountains",
                "Zone": "Gloom",
            },
            29: {
                "name": "Yuan-ti Ruins",
                "Zone": "Gloom",
            },
            30: {
                "name": "Th'lxi the Scourge",
                "Zone": "Twilight",
            },
            31: {
                "name": "Ghost of a Drow Samurai",
                "Zone": "Twilight",
            },
            32: {
                "name": "The Valley of Spirits",
                "Zone": "Dusk",
            },
            33: {
                "name": "Ruins of YYY",
                "Zone": "Gloom",
            },
            34: {
                "name": "Stalking Nothic",
                "Zone": "Twilight",
            },
            35: {
                "name": "Orcus Stuff",
                "Zone": "Void",
            },
            36: {
                "name": "Shrine of Orcus",
                "Zone": "Shadow",
            },
            37: {
                "name": "Mystery of the Tanaruks",
                "Zone": "Dusk",
            },
            38: {
                "name": "Great Wyrm Shadow Dragon",
                "Zone": "Void",
            },
            39: {
                "name": "Waking Up",
                "Zone": "Shadow",
            },
            40: {
                "name": "Drow Hamlet",
                "Zone": "Dusk",
            },
            41: {
                "name": "Bottomless Valley",
                "Zone": "Gloom",
            },
            42: {
                "name": "The Words of Orcus",
                "Zone": "Dusk",
            },
            43: {
                "name": "Purple Worm Nest",
                "Zone": "Gloom",
            },
            44: {
                "name": "Purple Worm Crossing",
                "Zone": "Dusk",
            },
            45: {
                "name": "Colony of Myconids",
                "Zone": "Twilight",
            },
            46: {
                "name": "Death of a Colony",
                "Zone": "Dusk",
            },
            47: {
                "name": "Migrant Caravan",
                "Zone": "Dusk",
            },
            48: {
                "name": "The Banished One",
                "Zone": "Shadow",
            },
            49: {
                "name": "Void Oblex",
                "Zone": "Void",
            },
            50: {
                "name": "Temple of Demogorgon",
                "Zone": "Shadow",
            },
            51: {
                "name": "Inverted Pyramid",
                "Zone": "Shadow",
            },
            52: {
                "name": "Hierophant of Annihilation",
                "Zone": "Shadow",
            },
            53: {
                "name": "Charon's New Deal",
                "Zone": "Void",
            },
            54: {
                "name": "Ocean of Anguish",
                "Zone": "Void",
            },
            55: {
                "name": "Nightmare of Reality",
                "Zone": "Dusk",
            },
            56: {
                "name": "Wraith Hunters",
                "Zone": "Dusk",
            },
            57: {
                "name": "Gar'god's Libray",
                "Zone": "Shadow",
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
