move_list = {
    'test move' : {
        'Power' : 999,
        'Accuracy': 100,
        'Name': 'Testing',
        'Type': 'Physical'
    },
    
    'Poly Tackle' : {
        'Power': 35,
        'Accuracy': 90,
        'Name': 'Poly Tackle',
        'Type': 'Physical'
    },
    'Square Fury': {
        'Chance': 10,
        'Power': 35,
        'Accuracy': 90,
        'Name': 'Square Fury',
        'Type': 'Physical'

    },
    'Polyscare': {
        'Debuff': 1.1,
        'Name': 'Polyscare',
        'Type': 'Status'
    },
    'Ridicule': {
        'Attack Buff Increase': 1.1,
        'Defense Debuff Decrease': 1.1,
        'Name': 'Ridicule',
        'Type': 'Status'
    },
    
    
    }


moves = {
    'move 1' : move_list['Poly Tackle'],
    'move 2' : move_list['Square Fury'],
    'move 3' : move_list['Polyscare'],
    'move 4' : move_list['Ridicule']
}

move_options = ['Poly Tackle', 'Square Fury', 'Polyscare', 'Ridicule']