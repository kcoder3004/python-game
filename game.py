import random


def show_instructions():
    print("""
    Text Adventure Game
    ===================
    Commands:
      go [direction]
      get [item]
      inventory
      look
    """)


def show_status():
    print('---------------------------')
    print(f'You are in the {current_room["name"]}')
    print(current_room["description"])
    print(f'Inventory: {inventory}')
    if "item" in current_room:
        print(f'You see a {current_room["item"]}')
    print("---------------------------")


# An inventory, which is initially empty
inventory = []

# A dictionary linking a room to other rooms and items
rooms = {
    'Hall': {
        'name': 'Hall',
        'description': 'You are in the hall. There is a door to the south and east.',
        'south': 'Kitchen',
        'east': 'Dining Room',
        'item': 'key'
    },
    'Kitchen': {
        'name': 'Kitchen',
        'description': 'You are in the kitchen. There is a door to the north.',
        'north': 'Hall',
        'item': 'monster'
    },
    'Dining Room': {
        'name': 'Dining Room',
        'description': 'You are in the dining room. There is a door to the west and south.',
        'west': 'Hall',
        'south': 'Garden',
        'item': 'potion'
    },
    'Garden': {
        'name': 'Garden',
        'description': 'You are in the garden. There is a door to the north.',
        'north': 'Dining Room'
    }
}

# Start the player in the Hall
current_room = rooms['Hall']

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
        if move[1] in current_room:
            # Set the current room to the new room
            current_room = rooms[current_room[move[1]]]
        else:
            print("You can't go that way!")

    # If they type 'get' first
    if move[0] == 'get':
        # If the item is in the room
        if "item" in current_room and move[1] == current_room['item']:
            # Add the item to their inventory
            inventory.append(move[1])
            # Remove the item from the room
            del current_room['item']
            print(f'{move[1]} got!')
        else:
            print(f"Can't get {move[1]}!")

    # If they type 'inventory' first
    if move[0] == 'inventory':
        print(f'Inventory: {inventory}')

    # If they type 'look' first
    if move[0] == 'look':
        show_status()

    # Player loses if they enter a room with a monster
    if 'item' in current_room and current_room['item'] == 'monster':
        print('A monster has got you... GAME OVER!')
        break

    # Player wins if they get to the Garden with a key and a potion
    if current_room['name'] == 'Garden' and 'key' in inventory and 'potion' in inventory:
        print('You escaped the house... YOU WIN!')
        break
