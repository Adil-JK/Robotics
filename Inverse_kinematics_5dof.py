import numpy as np
import serial
import sys

# Length of the links (in mm)
a1 = 120
a2 = 200
a3 = 200

# Coordinates of end-effector in mm
x = float(input("Enter x coordinate: "))
y = float(input("Enter y coordinate: "))
z = float(input("Enter z coordinate: "))

# Values for radius and sweep distance of rotary part at joint 4 (Dimensions are in mm)
rp1 = float(input("Enter the radius of rotary part at joint 4: "))
sd1 = float(input("Enter the arc length/ sweep distance of rotary part at joint 4: "))

# Values for vertical and horizontal distances of end-effector at joint 5 (Dimensions are in mm)
v = float(input("Enter the vertical distance of the end-effector:  "))
h = float(input("Enter the horizontal distance of the end-effector: "))

port = input("Enter the connected arduino port number: ")
ser = serial.Serial(port.upper(), 9600, timeout = 1)

if x == 0 and y == 0:
    sys.exit("You have entered wrong coordinates")
else:
    # For Theta 1 (T1)
    if x == 0 and y == 0:
        T1 = 0
    else:
        T1 = np.arctan(y / x)
        T1 = (T1 * 180) / np.pi

        # Limitation for coordinates of joint 1
        if T1 <= 0 or T1 >= 180:
            sys.exit("The coordinates you entered are out of reach for joint 1")

    # For Theta 2 (T2)
    r1 = np.sqrt(x ** 2 + y ** 2)
    r2 = z - a1
    r3 = np.sqrt(r1 ** 2 + r2 ** 2)
    phi2 = np.arcsin(r2 / r3)

    # phi2 in degrees
    phi2 = (phi2 * 180) / np.pi

    # For phi1, using law of cosines
    phi1 = np.arccos((a2 ** 2 + r3 ** 2 - a3 ** 2) / (2 * a2 * r3))

    # phi1 in degrees
    phi1 = (phi1 * 180) / np.pi
    T2 = phi2 - phi1

    # Limitation for coordinates of joint 2
    if T2 <= 0 or (T2 * 1) >= 180:
        sys.exit("The coordinates you entered are out of reach for joint 2")

    # For Theta 3
    # From law of cosines
    phi3 = np.arccos((a2 ** 2 + a3 ** 2 - r3 ** 2) / (2 * a2 * a3))

    # phi3 in degrees
    phi3 = (phi3 * 180) / np.pi
    T3 = 180 - phi3

    # Limitation for coordinates of joint 3
    if T3 <= 0 or T3 >= 135:
        sys.exit("The coordinates you entered are out of reach for joint 3")

    # For Theta 4 (T4)
    T4 = (sd1 / rp1)
    T4 = (T4 * 180) / np.pi

    # Limitation for coordinates of joint 4
    if T4 <= 0 or T4 >= 180:
        sys.exit("The coordinates you entered are out of reach for joint 4")

    # For Theta 5 (T5)
    T5 = np.arctan(v / h)
    T5 = (T5 * 180) / np.pi

    # Limitation for coordinates of joint 5
    if T5 <= 0 or T5 >= 50:
        sys.exit("The coordinates you entered are out of reach for joint 5")

print("Angles: T1:{0} T2:{1} T3:{2} T4:{3} T5:{4}".format(T1, T2, T3, T4, T5))
ser.write(b"{0},{1},{2},{3},{4}".format(T1, T2, T3, T4, T5));
ser.close()
