import modi
from time import sleep

# f"Pitch: {gyro.pitch:<10}"
# f"Roll: {gyro.roll:<10}"
# f"Yaw: {gyro.yaw:<10}"
# f"Vel x: {gyro.angular_vel_x:<10}"
# f"Vel y: {gyro.angular_vel_y:<10}"
# f"Vel z: {gyro.angular_vel_z:<10}"
# f"Acc x: {gyro.acceleration_x:<10}"
# f"Acc y: {gyro.acceleration_y:<10}"
# f"Acc z: {gyro.acceleration_z:<10}"


def check_vel(gyro):
    vel_x = gyro.angular_vel_x
    vel_y = gyro.angular_vel_y
    vel_z = gyro.angular_vel_z

    if abs(vel_z) > 40:
        return True

    return False


def check_pitch(gyro):
    pitch = gyro.pitch

    if pitch < -90:
        return True

    return False


bundle = modi.MODI()
gyro = bundle.gyros[0]
speaker = bundle.speakers[0]


speaker.tune = 3591, 50
speaker.frequency = 1975
speaker.volume = 0


count = 0

while True:

    if check_vel(gyro) == True:
        count += 1
        speaker.volume = 100
        sleep(2)

    if check_pitch(gyro) == True:
        count += 1
        speaker.volume = 100
        sleep(2)

    speaker.volume = 0
    print(f"you are sleep! count = {count}", end="\r")

    sleep(0.01)

