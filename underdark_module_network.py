from webweb import Web

web = Web(
    adjacency=[[0, 1], [1, 2]],
    display={
        'nodes' : {
            0 : {
                'name' : 'Kua Toa Village',
                'Zone' : 'Twilight',
            },
            1 : {
                'name' : 'The Great Sharay',
                'Zone' : 'Gloom',
            },
            2 : {
                'name' : 'Skeletal Fisherman',
                'Zone' : 'Dusk',
            },
            3 : {
                'name' : 'Enchanted Forest',
                'Zone' : 'Twilight',
            },
        },
    },
)

web.show()