import numpy as np

# Desired position of the end effector
x = 20.0
y = 0.0
z = 10.0

# Length of the links
a1 = 10.0
a2 = 10.0
a3 = 10.0

# For Theta 1 (T1)
if x==0 and y==0:
    T1=0
else:
    T1 = np.arctan(y/x)
    T1 = (T1*180.0)/np.pi

# For Theta 2 (T2)
r1 = np.sqrt(x**2 + y**2)
r2 = z - a1
phi2 = np.arctan(r2/r1)

# phi2 in degrees
phi2 = (phi2*180.0)/np.pi
r3 = np.sqrt(r1**2 + r2**2)

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

print("T1: ", T1)
print("T2: ", T2)
print("T3: ", T3)
