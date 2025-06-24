import board
from kmk.kmk_keyboard import KMKKeyboard
from kmk.scanners import DiodeOrientation
from kmk.keys import KC

keyboard = KMKKeyboard()

# Row GPIOs (Row 0–7)
keyboard.row_pins = [
    board.GP1,  # Row 0
    board.GP0,  # Row 1
    board.GP2,  # Row 2
    board.GP3,  # Row 3
    board.GP4,  # Row 4
    board.GP5,  # Row 5
    board.GP6,  # Row 6
    board.GP7,  # Row 7
]

# Column GPIOs (Col 0–9)
keyboard.col_pins = [
    board.GP8,   # Col 0
    board.GP9,   # Col 1
    board.GP10,  # Col 2
    board.GP16,  # Col 3
    board.GP14,  # Col 4
    board.GP15,  # Col 5
    board.GP18,  # Col 6
    board.GP19,  # Col 7
    board.GP20,  # Col 8
    board.GP21,  # Col 9
]

keyboard.diode_orientation = DiodeOrientation.COL2ROW

# Keymap (8 rows × 10 columns)
keyboard.keymap = [
    [KC.ESC,  KC.F1,  KC.F2,  KC.F3,  KC.F4,   KC.F5,   KC.F6,   KC.F7,   KC.F8,   KC.F9],    
    [KC.GRV,  KC.N1,  KC.N2,  KC.N3,  KC.N4,   KC.N5,   KC.N6,   KC.N7,   KC.N8,   KC.N9],    
    [KC.TAB,  KC.Q,   KC.W,   KC.E,   KC.R,    KC.T,    KC.Y,    KC.U,    KC.I,    KC.O],     
    [KC.CAPS, KC.A,   KC.S,   KC.D,   KC.F,    KC.G,    KC.H,    KC.J,    KC.K,    KC.L],     
    [KC.LSFT, KC.Z,   KC.X,   KC.C,   KC.V,    KC.B,    KC.N,    KC.M,    KC.COMM, KC.DOT],   
    [KC.LCTL, KC.LGUI,KC.LALT,KC.SPC, KC.RALT, KC.FN0,  KC.RCTL, KC.LEFT, KC.DOWN, KC.RIGHT],
    [KC.NO,   KC.NO,  KC.NO,  KC.NO,  KC.NO,   KC.NO,   KC.NO,   KC.NO,   KC.NO,   KC.NO],    
    [KC.NO,   KC.NO,  KC.NO,  KC.NO,  KC.NO,   KC.NO,   KC.NO,   KC.NO,   KC.NO,   KC.NO],    
]

if __name__ == '__main__':
    keyboard.go()
