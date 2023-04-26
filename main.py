def on_gesture_shake():
    global pin, alarm
    basic.clear_screen()
    pin = []
    alarm = 1
input.on_gesture(Gesture.SHAKE, on_gesture_shake)

def on_logo_pressed():
    global pinCheck, alarm, pin
    if input.button_is_pressed(Button.A):
        pin.append(1)
        basic.show_string("1")
        basic.pause(100)
        basic.clear_screen()
    if input.button_is_pressed(Button.B):
        pin.append(0)
        basic.show_string("0")
        basic.pause(100)
        basic.clear_screen()
    if len(pin) == 6:
        pinCheck = True
        for index in range(6):
            if code[index] != pin[index]:
                pinCheck = False
        if pinCheck == True:
            basic.show_icon(IconNames.YES)
            music.stop_all_sounds()
            alarm = 0
        else:
            basic.show_icon(IconNames.NO)
            pin = []
input.on_logo_event(TouchButtonEvent.PRESSED, on_logo_pressed)

pinCheck = False
alarm = 0
pin: List[number] = []
code: List[number] = []
code = [1, 1, 1, 0, 0, 0]
pin = []

def on_forever():
    if alarm == 1:
        music.play_sound_effect(music.create_sound_effect(WaveShape.TRIANGLE,
                5000,
                228,
                255,
                255,
                2000,
                SoundExpressionEffect.VIBRATO,
                InterpolationCurve.LOGARITHMIC),
            SoundExpressionPlayMode.IN_BACKGROUND)
basic.forever(on_forever)
