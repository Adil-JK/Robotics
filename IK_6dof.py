import numpy as np

# Length of the links (in mm)
a1 = 200.0
a2 = 200.0
a3 = 200.0

# Coordinates of end-effector in mm
x = float(input("Enter x coordinate: "))
y = float(input("Enter y coordinate: "))
z = float(input("Enter z coordinate: "))

# Values for radius and sweep distance of bracket at joint 4 (Dimensions are in mm)
r1 = float(input("Enter the radius of bracket at joint 4: "))
s1 = float(input("Enter the arc length/ sweep distance of bracket at joint 4: "))

# Values for radius and sweep distance of rotary part at joint 5 (Dimensions are in mm)
r2 = float(input("Enter the radius of rotary part at joint 5: "))
s2 = float(input("Enter the arc length/ sweep distance of rotary part at joint 5: "))

# Values for radius and sweep distance of end-effector at joint 6 (Dimensions are in mm)
r3 = float(input("Enter the radius of end-effector at joint 6: "))
s3 = float(input("Enter the arc length/ sweep distance of end-effector at joint 6: "))

if x==0 and y==0:
    print("You have entered wrong coordinates")
else:
    pass


    # For Theta 1 (T1)
    if x==0 and y==0:
        T1=0
    else:
        T1 = np.arctan(y/x)
        T1 = (T1*180.0)/np.pi

        # Limitation for coordinates of joint 1
        if T1<=-180.0 or T1>=180.0:
            print("The coordinates you entered are out of reach for joint 1")
        else:
            print("\nT1(deg): ", T1)

    # For Theta 2 (T2)
    r1 = np.sqrt(x**2 + y**2)
    r2 = z - a1
    r3 = np.sqrt(r1**2 + r2**2)
    phi2 = np.arcsin(r2/r3)

    # phi2 in degrees
    phi2 = (phi2*180.0)/np.pi

    # For phi1, using law of cosines
    phi1 = np.arccos((a2**2+r3**2-a3**2)/(2*a2*r3))

    # phi1 in degrees
    phi1 = (phi1*180.0)/np.pi
    T2 = phi2 - phi1

    # Limitation for coordinates of joint 2
    if T2 <= -35.0 or T2 >= 130.0:
        print("The coordinates you entered are out of reach for joint 2")
    else:
        print("T2(deg): ", T2)

    # For Theta 3
    # From law of cosines
    phi3 = np.arccos((a2**2+a3**2-r3**2)/(2*a2*a3))

    # phi3 in degrees
    phi3 = (phi3*180.0)/np.pi
    T3 = 180.0 - phi3

    # Limitation for coordinates of joint 3
    if T3 <= -100.0 or T3 >= 80.0:
        print("The coordinates you entered are out of reach for joint 3")
    else:
        print("T3(deg): ", T3)

    # For Theta 4 (T4)
    T4 = (s1 / r1)
    T4 = (T4 * 180.0) / np.pi

    # Limitation for coordinates of joint 4
    if T4 <= -270.0 or T4 >= 270.0:
        print("The coordinates you entered are out of reach for joint 4")
    else:
        print("T4(deg): ", T4)

    # For Theta 5 (T5)
    T5 = (s2 / r2)
    T5 = (T5 * 180.0) / np.pi

    # Limitation for coordinates of joint 5
    if T5 <= -180.0 or T5 >= 180.0:
        print("The coordinates you entered are out of reach for joint 5")
    else:
        print("T5(deg): ", T5)

    # For Theta 6 (T6)
    T6 = (s2 / r2)
    T6 = (T6 * 180.0) / np.pi

    # Limitation for coordinates of joint 6
    if T6 <= -270.0 or T6 >= 270.0:
        print("The coordinates you entered are out of reach for joint 6")
    else:
        print("T6(deg): ", T6)
