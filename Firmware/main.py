# You import all the IOs of your board
import board

# These are imports from the kmk library
from kmk.kmk_keyboard import KMKKeyboard
from kmk.scanners.keypad import KeysScanner
from kmk.keys import KC
from kmk.modules.macros import Press, Release, Tap, Macros
from kmk.modules.encoder import EncoderHandler
from kmk.extensions.rgb import RGB

# This is the main instance of your keyboard
keyboard = KMKKeyboard()

# Add the macro extension
macros = Macros()
keyboard.modules.append(macros)

# Rotary Encoder implementation
encoder_handler = EncoderHandler()
keyboard.modules.append(encoder_handler)

encoder_handler.pins = ((board.A0, board.A1),)  # A0 = GPIO28, A1 = GPIO29
encoder_handler.map = [((KC.VOLD, KC.VOLU),)]   # Rotate left/right

# LED implementation
rgb_ext = RGB(pixel_pin=board.D5, num_pixels=2)
keyboard.extensions.append(rgb_ext)

# Define your pins here!
PINS = [board.D1, board.D2, board.D6, board.D7, board.D11, board.D10, board.D9, board.D8]
# Encoder button
PINS.append(board.A2)

# Tell kmk we are not using a key matrix
keyboard.matrix = KeysScanner(
    pins=PINS,
    value_when_pressed=False,
)

# Here you define the buttons corresponding to the pins
# Look here for keycodes: https://github.com/KMKfw/kmk_firmware/blob/main/docs/en/keycodes.md
# And here for macros: https://github.com/KMKfw/kmk_firmware/blob/main/docs/en/macros.md
keyboard.keymap = [
    [
        KC.Macro(Press(KC.LCTL), Tap(KC.C), Release(KC.LCTL)),
	KC.Macro(Press(KC.LCTL), Tap(KC.V), Release(KC.LCTL)),
        KC.DELETE,
	KC.TAB,
	KC.LGUI
        KC.MACRO("Hello world!"),
        KC.Macro(Press(KC.LCTRL), PRESS(KC.LALT), PRESS(KC.DELETE), RELEASE(KC.LCTRL), RELEASE(KC.LALT), RELEASE(KC.DELETE)),
        KC.ENTER,
    ]
]

# Start kmk!
if __name__ == '__main__':
    keyboard.go()