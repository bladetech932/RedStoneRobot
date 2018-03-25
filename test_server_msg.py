import msgpack
import socket
import Adafruit_PCA9685 as pca

pwm = pca.PCA9685()
pwm.set_pwm_freq(60)
FL_channel = 0
FR_channel = 1
BL_channel = 2
BR_channel = 3

port = 55555
s = socket.socket()
s.bind(('', port))
s.listen(1)
print("waiting for connection...")
conn, addr = s.accept()
# print("connected to: ", addr)


while True:

    packed = conn.recv(1024)

    data = msgpack.unpackb(packed)

    FL_motor = ((-data[0][1] + data[0][0]) * -2 + 420)
    FR_motor = ((-data[0][1] - data[0][0]) * 2 + 420)
    BL_motor = ((-data[0][1] - data[0][0]) * -2 + 420)
    BR_motor = ((-data[0][1] + data[0][0]) * 2 + 420)
    print("FL:", FL_motor, " FR:", FR_motor, " BL:", BL_motor, " BR:", BR_motor)

    pwm.set_pwm(FL_channel, 0, FL_motor)
    pwm.set_pwm(FR_channel, 0, FR_motor)
    pwm.set_pwm(BL_channel, 0, BL_motor)
    pwm.set_pwm(BR_channel, 0, BR_motor)
conn.close()
s.close()
