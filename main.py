def on_button_pressed_a():
    serial.write_string("A=1,")
    basic.show_string("A=1")
input.on_button_pressed(Button.A, on_button_pressed_a)

def on_button_pressed_b():
    serial.write_string("B=1,")
    basic.show_string("B=1")
input.on_button_pressed(Button.B, on_button_pressed_b)

def on_forever():
    serial.write_string("T=" + str(input.temperature()) + ",")
    serial.write_string("L=" + str(input.light_level()) + ",")
    basic.show_string("TL")
    basic.pause(10000)
basic.forever(on_forever)
