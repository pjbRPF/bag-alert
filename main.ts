input.onGesture(Gesture.Shake, function () {
    basic.clearScreen()
    pin = []
    alarm = 1
    radio.sendNumber(1)
})
input.onLogoEvent(TouchButtonEvent.Pressed, function () {
    if (input.buttonIsPressed(Button.A)) {
        pin.push(1)
        basic.showString("1")
        basic.pause(100)
        basic.clearScreen()
    }
    if (input.buttonIsPressed(Button.B)) {
        pin.push(0)
        basic.showString("0")
        basic.pause(100)
        basic.clearScreen()
    }
    if (pin.length == 6) {
        pinCheck = true
        for (let index = 0; index <= 5; index++) {
            if (code[index] != pin[index]) {
                pinCheck = false
            }
        }
        if (pinCheck == true) {
            basic.showIcon(IconNames.Yes)
            music.stopAllSounds()
            alarm = 0
            radio.sendNumber(0)
        } else {
            basic.showIcon(IconNames.No)
            pin = []
        }
    }
})
let pinCheck = false
let alarm = 0
let pin: number[] = []
let code: number[] = []
radio.setGroup(42)
code = [
1,
1,
1,
0,
0,
0
]
pin = []
basic.forever(function () {
    if (alarm == 1) {
        music.playSoundEffect(music.createSoundEffect(WaveShape.Triangle, 5000, 228, 255, 255, 2000, SoundExpressionEffect.Vibrato, InterpolationCurve.Logarithmic), SoundExpressionPlayMode.InBackground)
    }
})
