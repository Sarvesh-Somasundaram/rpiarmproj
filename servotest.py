from adafruit_servokit import ServoKit
kit = ServoKit(channels=16)


kit.servo[0].angle = 180

kit.servo[0].angle = 0

kit.servo[0].angle = 180

kit.servo[0].actuation_range = 160

kit.servo[0].angle = 60

kit.servo[0].angle = 160

kit.servo[0].set_pulse_width_range(1000, 2000)


