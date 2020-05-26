from machine import Pin, PWM


def mapper(value):
    mappedValue = ((value - 0) / (255 - 0)) * (1025 - 0) + 0
    return mappedValue


class RGBLED:
    def __init__(self, redPin, greenPin, bluePin):  # constructor, defaults pins to off
        self.redPin = PWM(Pin(redPin), duty=0)
        self.greenPin = PWM(Pin(greenPin), duty=0)
        self.bluePin = PWM(Pin(bluePin), duty=0)

    def turnOn(self):  # turn all pins on (WHITE)
        self.redPin.duty(255)
        self.greenPin.duty(255)
        self.bluePin.duty(255)

    def turnOff(self):  # turn all pins off (OFF)
        self.redPin.duty(0)
        self.greenPin.duty(0)
        self.bluePin.duty(0)



    def color(self, red, green, blue):  # method to select rgb value to display.
        #code to map 0-255 to 0-1025:

        self.redPin.duty(red)
        self.greenPin.duty(green)
        self.bluePin.duty(blue)


