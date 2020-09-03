# structure defining the rooms in the game. Try adding more rooms to the game!
rooms = {
    "Stimson Tavern": 
    {
        "description": 
        [
            "You're in a cozy tavern in the small town of Stimson. You take advantage of the",
            "quiet atmosphere and get warmed by an open fire."
        ],
        "exits": 
        {
            "outside": "Outside Stimson Tavern"
        },
    },
    "Outside Stimson Tavern": 
    {
        "description": 
        [
            "You're standing outside Stimson Tavern. You enjoy the small, covered patio in",
            "front of the tavern and breathe in the cool, fresh air."
        ],
        "exits": 
        {
            "inside": "Stimson Tavern",
            "path": "Stimson Tavern Path"
        },
    },
    "Stimson Tavern Path": 
    {
        "description": 
        [
            "The path in front of Stimson Tavern is worn and weathered. There is a sign that",
            "reads, 'North: Stepford <-> South: Merthrop'"
        ],
        "exits": 
        {
            "tavern": "Outside Stimson Tavern",
            "north": "Stimson Tavern Path North",
            "south": "Stimson Tavern Path South"
        },
    },
    "Stimson Tavern Path North": 
    {
        "description": 
        [
            "You are on a dirt path leading north from Stimson Tavern. In front of you lies",
            "a small stream that is just big enough that it gives you hesitation jumping",
            "over it."
        ],
        "exits": 
        {
            "south": "Stimson Tavern Path"
        },
    },
    "Stimson Tavern Path South": 
    {
        "description": 
        [
            "You are on a dirt path leading south from Stimson Tavern. The path leads to a",
            "dense forest that is dimly lit. You are on guard as you reach the forest's",
            "edge."
        ],
        "exits": 
        {
            "north": "Stimson Tavern Path"
        },
    }
}
