from webweb import Web

web = Web(
    adjacency=[
        [1,1]
    ],
    display={
        "metadata": {
            "Ward": {"values": list([i+1 for i in range(10)])}
        },
        "nodes": {
            1: {
                "name": "Djinni of Steam",
                "Ward": "1",
            },

        },
    },
)
if __name__ == "__main__":
    web.display.colorBy = "Ward"
    web.display.charge = 100
    web.display.linkStrength = 0.2
    web.display.linkLength = 30

    web.show()
