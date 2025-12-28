import board

from kmk.kmk_keyboard import KMKKeyboard
from kmk.scanners import DiodeOrientation
from kmk.scanners.keypad import MatrixScanner
from kmk.keys import KC
from kmk.modules.encoder import EncoderHandler
from kmk.modules.macros import Macros
from kmk.extensions.rgb import RGB

keyboard = KMKKeyboard()

keyboard.matrix = MatrixScanner(
    cols=[board.GP0, board.GP1, board.GP2, board.GP3],
    rows=[board.GP4, board.GP6, board.GP7],
    diode_orientation=DiodeOrientation.COL2ROW,
)

encoder = EncoderHandler()
encoder.pins = [(board.GP26, board.GP27)]
keyboard.modules.append(encoder)

keyboard.modules.append(Macros())

rgb = RGB(
    pixel_pin=board.GP29,
    num_pixels=1,
    val_limit=40,
)

keyboard.extensions.append(rgb)

keyboard.after_init = lambda kb: kb.extensions[0].set_rgb((255, 255, 255))

keyboard.keymap = [
    [
        KC.O, KC.P, KC.Q, KC.R,
        KC.S, KC.T, KC.U, KC.V,
        KC.W, KC.X, KC.Y, KC.Z,
        KC.ENTER,
    ]
]

keyboard.matrix.key_count = 13

keyboard.coord_mapping = [
    0, 1, 2, 3,
    4, 5, 6, 7,
    8, 9, 10, 11,
    12,
]

encoder.map = [(KC.VOLU, KC.VOLD)]

if __name__ == "__main__":
    keyboard.go()
