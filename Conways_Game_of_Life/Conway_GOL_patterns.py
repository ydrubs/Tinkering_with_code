"""Patters for initial seeding of the cells in Conways Game of Life.
Source code credit: https://github.com/marcpaulo15/game_of_life/blob/main/seed_patterns.yml"""

def glider():
    injection_array = [  # Glider  [Spaceships, moves diagonally]
         [0, 1, 0],
         [0, 0, 1],
         [1, 1, 1],
    ]
    return injection_array

def penta():
    injection_array = [  # Penta-decathlon  [Oscillator, period 15]
         [1, 1, 1],
         [1, 0, 1],
         [1, 1, 1],
         [1, 1, 1],
         [1, 1, 1],
         [1, 1, 1],
         [1, 0, 1],
         [1, 1, 1],
    ]
    return injection_array

def diehard():
    injection_array = [  # Diehard  [disappears after 130 generations]
        [0, 0, 0, 0, 0, 0, 0, 1, 0],
        [0, 1, 1, 0, 0, 0, 0, 0, 0],
        [0, 0,1, 0, 0, 0, 1, 1, 1]
    ]
    return injection_array

def heavy_sapceship():
    injection_array = [  # Heavy-weight spaceship  [Spaceship, moves horizontally]
            [0, 1, 1, 1, 1, 0, 0],
            [1, 1, 1, 1, 1, 1, 0],
            [1, 1, 1, 1, 0, 1, 1],
            [0, 0, 0, 0, 1, 1, 0],
        ]
    return injection_array

def minimal():
    injection_array = [  # Minimal pattern (just 10 living cells) that exhibits infinite growth
            [0, 0, 0, 0, 0, 0, 1, 0],
            [0, 0, 0, 0, 1, 0, 1, 1],
            [0, 0, 0, 0, 1, 0, 1, 0],
            [0, 0, 0, 0, 1, 0, 0, 0],
            [0, 0, 1, 0, 0, 0, 0, 0],
            [1, 0, 1, 0, 0, 0, 0, 0],
        ]
    return injection_array

def beautiful():
    injection_array = [  # Beautiful pattern [eventually stabilized in different shapes]
        [1, 1, 1],
        [0, 0, 1],
        [1, 0, 1],
        [1, 1, 0],
        [0, 0, 0],
        [1, 1, 0],
        [1, 0, 1],
        [0, 0, 1],
        [1, 1, 1],
    ]
    return injection_array

def three_by_three():
    injection_array = [  # Two 3x3 squares  [Oscillator, period 8]
            [1, 1, 1, 0, 0, 0],
            [1, 1, 1, 0, 0, 0],
            [1, 1, 1, 0, 0, 0],
            [0, 0, 0, 1, 1, 1],
            [0, 0, 0, 1, 1, 1],
            [0, 0, 0, 1, 1, 1]
        ]
    return injection_array

def beautiful2():
    injection_array = [  # Beautiful pattern that creates different forms of life
            [1, 0, 1, 0, 0, 0, 1, 0, 1],
            [1, 0, 1, 1, 0, 1, 1, 0, 1],
            [0, 1, 1, 0, 1, 0, 1, 1, 0],
            [0, 0, 0, 1, 0, 1, 0, 0, 0],
            [0, 0, 0, 1, 1, 1, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0],
            [1, 0, 0, 0, 0, 0, 0, 0, 1],
            [1, 0, 0, 0, 0, 0, 0, 0, 1],
            [1, 0, 0, 0, 0, 0, 0, 0, 1],
        ]
    return injection_array

def inf_loop():
    injection_arrey = [  # Infinite Loop [Oscillator]
            [1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 1, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 1, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 1, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 1, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1],
        ]
    return injection_arrey
