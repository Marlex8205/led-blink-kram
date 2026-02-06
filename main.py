def on_forever():
    basic.show_string("Shalom")
    basic.pause(1000)
    basic.clear_screen()
    basic.pause(1000)

basic.forever(on_forever)

def on_button_pressed_a():
    basic.show_string("Tut Tut")

input.on_button_pressed(Button.A, on_button_pressed_a)

def on_button_pressed_b():
    basic.show_string("67")

input.on_button_pressed(Button.B, on_button_pressed_b)
