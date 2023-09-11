travel = [ 
    {   
        "state": "up", 
        "cities": ["agra","mathura","kashi"],
        "cost": 50000
    },
    {
        "state":"maha", 
        "cities": ["mumbai","nashik","pune"],
        "cost": 60000 
    },
    {
        "state": "guj", 
        "cities": ["ahmedabad","surat","kachh"], 
        "cost": 70000
    }
]

def add(state,city,cost):
    travel.append({"state": state, 
        "cities": city,
        "cost": cost})

add("hp", 
    ["manali","shimla","kasol"],
    40000)

print(travel[3])