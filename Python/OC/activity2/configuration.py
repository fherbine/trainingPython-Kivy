MAPS_PATH='cartes'
PORT=25000
STATIC_ELEMENTS={'O': 'WallElement', '.': 'DoorElement', ' ': 'EmptyElement'}
AVAILABLE_COMMANDS={
    'O': 'move_left',
    'E': 'move_right',
    'N': 'move_up',
    'S': 'move_down',
    'M': 'make_wall',
    'P': 'make_door',
    'Q': '%QUIT%',
}
