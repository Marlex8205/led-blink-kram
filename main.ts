basic.forever(function on_forever() {
    basic.showString("Shalom")
    basic.pause(1000)
    basic.clearScreen()
    basic.pause(1000)
})
input.onButtonPressed(Button.A, function on_button_pressed_a() {
    basic.showString("Tut Tut")
})
input.onButtonPressed(Button.B, function on_button_pressed_b() {
    basic.showString("67")
})
