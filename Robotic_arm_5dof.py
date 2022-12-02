import numpy as np
import time
import serial
import sys

# Length of the links (in mm)
a1 = 120.0
a2 = 200.0
a3 = 200.0
a4 = 45.0
a5 = 15.0
a6 = 120.0

# Home position coordinates of the robotic arm

x0 = 200.0
y0 = 0
z0 = 150.0

# Values for radius and sweep distance/ arc length of the rotary part of joint 4 at home position (in mm)
rpr_0 = 17.0
sd_0 = 0.0

# Values for vertical and horizontal distances of the end-effector servomotor of joint 5 at home position (in mm)
v0 = 0
h0 = 15.0

# Coordinates of the final position where the end-effector has to move (in mm)

x5 = 200.0
y5 = 200.0
z5 = 180.0

# Values for radius and sweep distance/ arc length of the rotary part of joint 4 at final position (in mm)
rpr_5 = 17.0
sd_5 = 26.5

# Values for vertical and horizontal distances covered by the end-effector servomotor of joint 5 at final position (in mm)
v5 = 17.0
h5 = 15.0

port = input("Enter the connected arduino port number: ")
ser = serial.Serial(port.upper(), 9600, timeout = 1)

Counter = 1
while True:

    print("Cycle", Counter)
    # For Theta 1 of home position (T1_0)
    T1_0 = np.arctan(y0 / x0)
    T1_0 = (T1_0 * 180.0) / np.pi

    # For Theta 2 of home position (T2_0)
    r1_0 = np.sqrt(x0 ** 2 + y0 ** 2)
    r2_0 = z0 - a1
    r3_0 = np.sqrt(r1_0 ** 2 + r2_0 ** 2)

    phi2_0 = np.arcsin(r2_0 / r3_0)

    # phi2_0 in degrees
    phi2_0 = (phi2_0 * 180.0) / np.pi

    # For phi1_0, using law of cosines
    phi1_0 = np.arccos((a2 ** 2 + r3_0 ** 2 - a3 ** 2) / (2 * a2 * r3_0))

    # phi1_0 in degrees
    phi1_0 = (phi1_0 * 180.0) / np.pi
    T2_0 = phi2_0 - phi1_0

    # For Theta 3 of home position (T3_0)
    # From law of cosines
    phi3_0 = np.arccos((a2 ** 2 + a3 ** 2 - r3_0 ** 2) / (2 * a2 * a3))

    # phi3_0 in degrees
    phi3_0 = (phi3_0 * 180.0) / np.pi
    T3_0 = 180.0 - phi3_0

    # For Theta 4 of home position (T4_0)
    T4_0 = (sd_0 / rpr_0)
    T4_0 = (T4_0 * 180.0) / np.pi

    # For Theta 5 of home position (T5_0)
    T5_0 = np.arctan(v0 / h0)
    T5_0 = (T5_0 * 180.0) / np.pi

    print("Setting at home position: T1_0:{0}, T2_0:{1},  T3_0:{2},  T4_0:{3},  T5_0:{4},  \n".format(T1_0, T2_0, T3_0, T4_0, T5_0))
    ser.write(b"{0},{1},{2},{3},{4}".format(T1_0, T2_0 * (-1), T3_0, T4_0, T5_0));

    time.sleep(1.5)

    # For Theta 1 of final position (T1)
    T1 = np.arctan(y5 / x5)
    T1 = (T1 * 180.0) / np.pi

    # Limitation for coordinates of joint 1
    if T1 <= 0 or T1 >= 90.0:
        sys.exit("The coordinates you entered are out of reach for joint 1")

    # For Theta 2 of final position (T2)
    r1 = np.sqrt(x5 ** 2 + y5 ** 2)
    r2 = z5 - a1
    r3 = np.sqrt(r1 ** 2 + r2 ** 2)
    phi2 = np.arcsin(r2 / r3)

    # phi2 in degrees
    phi2 = (phi2 * 180.0) / np.pi

    # For phi1, using law of cosines
    phi1 = np.arccos((a2 ** 2 + r3 ** 2 - a3 ** 2) / (2 * a2 * r3))

    # phi1 in degrees
    phi1 = (phi1 * 180.0) / np.pi
    T2 = phi2 - phi1

    # Limitation for coordinates of joint 2
    if T2 <= -180.0 or T2 >= 0.0:
        sys.exit("The coordinates you entered are out of reach for joint 2")

    # For Theta 3 of final position (T3)
    # From law of cosines
    phi3 = np.arccos((a2 ** 2 + a3 ** 2 - r3 ** 2) / (2 * a2 * a3))

    # phi3 in degrees
    phi3 = (phi3 * 180.0) / np.pi
    T3 = 180.0 - phi3

    # Limitation for coordinates of joint 3
    if T3 <= 40.0 or T3 >= 180.0:
        sys.exit("The coordinates you entered are out of reach for joint 3")

    # For Theta 4 of final position (T4)
    T4 = (sd_5 / rpr_5)
    T4 = (T4 * 180.0) / np.pi

    # Limitation for coordinates of joint 4
    if T4 <= 0.0 or T4 >= 180.0:
        sys.exit("The coordinates you entered are out of reach for joint 4")

    # For Theta 5 of final position (T5)
    T5 = np.arctan(v5 / h5)
    T5 = (T5 * 180.0) / np.pi

    # Limitation for coordinates of joint 5
    if T5 <= 0.0 or T5 >= 50.0:
        sys.exit("The coordinates you entered are out of reach for joint 5")

    print("Moving to final position: T1:{0},  T2:{1},  T3:{2},  T4:{3},  T5:{4},  \n".format(T1, T2, T3, T4, T5))
    ser.write(b"{0},{1},{2},{3},{4}".format(T1, T2 * (-1), T3, T4, T5));

    time.sleep(1.5)

    print("Returning to home position: T1_0:{0},  T2_0:{1},  T3_0:{2},  T4_0:{3},  T5_0:{4},  \n".format(T1_0, T2_0, T3_0, T4_0, T5_0))
    ser.write(b"{0},{1},{2},{3},{4}".format(T1_0, T2_0 * (-1), T3_0, T4_0, T5_0));

    time.sleep(1.5)

    Counter += 1

    # The robotic arm will continuosly move between the given coordinates until the user stops the program to halt the while loop