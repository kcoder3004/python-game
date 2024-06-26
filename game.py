import random

def show_instructions():
    print("""
    Text Adventure Game
    ===================
    Commands:
      go [direction]
      get [item]
    """)

def show_status():
    print('---------------------------')
    print(f'You are in the {current_room}')
    print(f'Inventory: {inventory}')
    if "item" in rooms[current_room]:
        print(f'You see a {rooms[current_room]["item"]}')
    print("---------------------------")

# An inventory, which is initially empty
inventory = []

# A dictionary linking a room to other rooms
rooms = {
    'Hall': {
        'south': 'Kitchen',
        'east': 'Dining Room',
        'item': 'key'
    },
    'Kitchen': {
        'north': 'Hall',
        'item': 'monster'
    },
    'Dining Room': {
        'west': 'Hall',
        'south': 'Garden',
        'item': 'potion'
    },
    'Garden': {
        'north': 'Dining Room'
    }
}

# Start the player in the Hall
current_room = 'Hall'

show_instructions()

# Loop infinitely
while True:
    show_status()
    
    # Get the player's next 'move'
    move = ''
    while move == '':
        move = input('>')
    
    # Split the input into an action and a direction/item
    move = move.lower().split()
    
    # If they type 'go' first
    if move[0] == 'go':
        # Check that they are allowed wherever they want to go
        if move[1] in rooms[current_room]:
            # Set the current room to the new room
            current_room = rooms[current_room][move[1]]
        else:
            print("You can't go that way!")
    
    # If they type 'get' first
    if move[0] == 'get':
        # If the item is in the room
        if "item" in rooms[current_room] and move[1] == rooms[current_room]['item']:
            # Add the item to their inventory
            inventory.append(move[1])
            # Remove the item from the room
            del rooms[current_room]['item']
            print(f'{move[1]} got!')
        else:
            print(f"Can't get {move[1]}!")
    
    # Player loses if they enter a room with a monster
    if 'item' in rooms[current_room] and rooms[current_room]['item'] == 'monster':
        print('A monster has got you... GAME OVER!')
        break
    
    # Player wins if they get to the Garden with a key and a potion
    if current_room == 'Garden' and 'key' in inventory and 'potion' in inventory:
        print('You escaped the house... YOU WIN!')
        break
