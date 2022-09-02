input.onButtonPressed(Button.A, function () {
    serial.writeString("A=1,")
    basic.showString("A=1")
})
input.onButtonPressed(Button.B, function () {
    serial.writeString("B=1,")
    basic.showString("B=1")
})
basic.forever(function () {
    serial.writeString("T=" + input.temperature() + ",")
    serial.writeString("L=" + input.lightLevel() + ",")
    basic.showString("TL")
    basic.pause(5000)
})
