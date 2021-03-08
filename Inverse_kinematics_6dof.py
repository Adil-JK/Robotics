import numpy as np

# Length of the links (in mm)
a1 = 200.0
a2 = 200.0
a3 = 200.0

# Coordinates of end-effector in mm
x = float(input("Enter x coordinate: "))
y = float(input("Enter y coordinate: "))
z = float(input("Enter z coordinate: "))

if x>=198.9 and y>=347.0 and z>=205.4:
    print("\nThe coordinates are out of reach for this robot!")
else:
    pass

    # For Theta 1 (T1)
    if x==0 and y==0:
        T1=0
    else:
        T1 = np.arctan(y/x)

    # For Theta 2 (T2)
    r1 = np.sqrt(x**2 + y**2)
    r2 = z - a1
    r3 = np.sqrt(r1**2 + r2**2)
    phi2 = np.arcsin(r2/r3)
    # For phi1, using law of cosines
    phi1 = np.arccos((a2**2+r3**2-a3**2)/(2*a2*r3))
    T2 = phi2 - phi1

    # For Theta 3
    # From law of cosines
    phi3 = np.arccos((a2**2+a3**2-r3**2)/(2*a2*a3))
    T3 = np.pi - phi3

    # Rotational matrix from frame 0 to frame 3
    R0_3 = np.array([[-np.cos(T1)*np.cos(T2)*np.sin(T3)-np.cos(T1)*np.sin(T2)*np.cos(T3), np.sin(T1), np.cos(T1)*np.cos(T2)*np.cos(T3)-np.cos(T1)*np.sin(T2)*np.sin(T3)],
                     [-np.sin(T1)*np.cos(T2)*np.sin(T3)-np.sin(T1)*np.sin(T2)*np.cos(T3), -np.cos(T1), np.sin(T1)*np.cos(T2)*np.cos(T3)-np.sin(T1)*np.sin(T2)*np.sin(T3)],
                     [-np.sin(T2)*np.sin(T3)+np.cos(T2)*np.cos(T3), 0, np.sin(T2)*np.cos(T3)+np.cos(T2)*np.sin(T3)]])

    print("\nR0_3 = ", R0_3)

    # Inverse of R0_3 matrix
    inv_R0_3 = np.linalg.inv(R0_3)

    print("\ninv_R0_3 = ", inv_R0_3)

    # Position of our end effector
    R0_6 = np.array([[-1.0, 0.0, 0.0],
                      [0.0, -1.0, 0.0],
                      [0.0, 0.0, 1.0]])

    # Rotational matrix from frame 3 to frame 6
    R3_6 = np.dot(inv_R0_3, R0_6)

    print("\nR3_6 = ", R3_6)

    T5 = np.arccos(R3_6[2][1])

    T6 = np.arccos(R3_6[2][0]/-np.sin(T5))

    T4 = np.arccos(R3_6[0][1] / np.sin(T5))

    R3_6_Check = np.array([[np.cos(T4)*np.cos(T5)*np.cos(T6)-np.sin(T4)*np.sin(T6), np.cos(T4)*np.sin(T5), np.cos(T4)*np.cos(T5)*np.sin(T6)+np.sin(T4)*np.cos(T6)],
                     [np.sin(T4)*np.cos(T5)*np.cos(T6)+np.cos(T4)*np.sin(T6), np.sin(T4)*np.sin(T5), np.sin(T4)*np.cos(T5)*np.sin(T6)-np.cos(T4)*np.cos(T6)],
                     [-np.sin(T5)*np.cos(T6), np.cos(T5), -np.sin(T5)*np.sin(T6)]])

    print("\nR3_6_Check = ", R3_6_Check)

    # Angles in degrees
    T1 = (T1 * 180.0) / np.pi
    T2 = (T2 * 180.0) / np.pi
    T3 = (T3 * 180.0) / np.pi
    T4 = (T4 * 180.0) / np.pi
    T5 = (T5 * 180.0) / np.pi
    T6 = (T6 * 180.0) / np.pi

    print("\nT1(deg): ", T1)
    print("T2(deg): ", T2)
    print("T3(deg): ", T3)
    print("T4(deg): ", T4)
    print("T5(deg): ", T5)
    print("T6(deg): ", T6)