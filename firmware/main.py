from kmk.kmk_keyboard import KMKKeyboard
from kmk.scanners import MatrixScanner
from kmk.keys import KC

keyboard = KMKKeyboard()

# Define row and column pins
keyboard.row_pins = (keyboard.io.D0, keyboard.io.D1, keyboard.io.D2, keyboard.io.D3,
                     keyboard.io.D4, keyboard.io.D5, keyboard.io.D6, keyboard.io.D7)

keyboard.col_pins = (keyboard.io.D9, keyboard.io.D8, keyboard.io.D10, keyboard.io.D16,
                     keyboard.io.D14, keyboard.io.D15, keyboard.io.D18, keyboard.io.D19,
                     keyboard.io.D20, keyboard.io.D21)

keyboard.diode_orientation = MatrixScanner.DIODE_COL2ROW

# Define keymap layout (80 keys)
keyboard.keymap = [
    [
        KC.ESC,    KC.F1,   KC.F2,   KC.F3,   KC.F4,   KC.F5,   KC.F6,   KC.F7,   KC.F8,   KC.F9,
        KC.GRAVE,  KC.N1,   KC.N2,   KC.N3,   KC.N4,   KC.N5,   KC.N6,   KC.N7,   KC.N8,   KC.N9,
        KC.TAB,    KC.Q,    KC.W,    KC.E,    KC.R,    KC.T,    KC.Y,    KC.U,    KC.I,    KC.O,
        KC.CAPS,   KC.A,    KC.S,    KC.D,    KC.F,    KC.G,    KC.H,    KC.J,    KC.K,    KC.L,
        KC.LSFT,   KC.Z,    KC.X,    KC.C,    KC.V,    KC.B,    KC.N,    KC.M,    KC.COMM, KC.DOT,
        KC.LCTL,   KC.FN0,  KC.LALT, KC.SPC,  KC.EQL,  KC.BSPC, KC.ENT,  KC.DEL,  KC.RBRC, KC.BSLS,
        KC.RALT,   KC.FN1,  KC.RCTL, KC.LEFT, KC.DOWN, KC.RIGHT, KC.F12, KC.DEL,  KC.COLN, KC.QUOT,
        KC.UP,     KC.INS,  KC.SLSH, KC.RSFT, KC.P,    KC.LBRC, KC.N0,   KC.MINS, KC.F10,  KC.F11
    ]
]
