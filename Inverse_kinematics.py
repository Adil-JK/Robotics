import numpy as np

# Desired position of the end effector
x = 20.0
y = 0.0
z = 10.0

# Length of the links
a1 = 10.0
a2 = 10.0
a3 = 10.0

# Theta 1
T1 = np.arctan(y/x)

# Theta 2
r1 = np.sqrt((z-a1)**2 + x**2)
phi2 = np.arccos((a2**2+r1**2-a3**2)/(2*a2*r1))
T2 = np.arctan((z-a1)/x) - phi2

# Theta 3
phi3 = np.arccos((a2**2+a3**2-r1**2)/(2*a2*a3))
T3 = 180.0 - phi3

print(T1)
print(T2)
print(T3)