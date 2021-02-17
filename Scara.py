import numpy as np

# Length of the links (in mm)
a1 = 200.0
a2 = 200.0
a3 = 200.0
a4 = 150.0

# Coordinates of end-effector in mm
x = float(input("Enter x coordinate: "))
y = float(input("Enter y coordinate: "))
z = float(input("Enter z coordinate: "))

# Here the end effector is taken as cylindrical tool piece (Dimensions are in mm)
r = float(input("Enter the radius of the end effector: "))
s = float(input("Enter the arc length/ sweep distance of the end effector: "))

if x==0 and y==0:
    print("You have entered wrong coordinates")
else:
    pass

    # For Theta 1 (T1)
    phi1 = np.arctan(y/x)
    r1 = np.sqrt(x**2 + y**2)
    phi2 = np.arccos((a2**2+r1**2-a3**2)/(2*a2*r1))
    T1 = phi1 - phi2
    # Theta 1 in degrees
    T1 = (T1*180.0)/np.pi

    # For Theta 2 (T2)
    phi3 = np.arccos((a2**2+a3**2-r1**2)/(2*a2*a3))
    # phi3 in degrees
    phi3 = (phi3 * 180.0) / np.pi
    T2 = 180.0 - phi3

    # For d3
    d3 = a1 - a4 - z

    # For Theta 4 (T4)
    T4 = (s/r)
    T4 = (T4*180.0)/np.pi

    # Angles in degrees
    print("\nT1(deg): ", T1)
    print("T2(deg): ", T2)
    print("d3(mm): ", d3)
    print("T4(deg): ", T4)

