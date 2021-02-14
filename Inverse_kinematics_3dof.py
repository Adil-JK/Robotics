import numpy as np

# Length of the links (in mm)
a1 = 200.0
a2 = 200.0
a3 = 200.0

# Coordinates of end-effector (in mm)
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
        T1 = (T1*180.0)/np.pi

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


    # For Theta 3
    # From law of cosines
    phi3 = np.arccos((a2**2+a3**2-r3**2)/(2*a2*a3))

    # phi3 in degrees
    phi3 = (phi3*180.0)/np.pi
    T3 = 180.0 - phi3

    # Angles in degrees
    print("\nT1(deg): ", T1)
    print("T2(deg): ", T2)
    print("T3(deg): ", T3)
