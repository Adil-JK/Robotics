import numpy as np

# Theta in degrees
T1 = 0
T2 = 0
T3 = 0

# Theta in radians
T1 = (T1/180.0)*np.pi
T2 = (T2/180.0)*np.pi
T3 = (T3/180.0)*np.pi

# Alpha in degrees
A1 = 90
A2 = 0
A3 = 0

# Alpha in radians
A1 = (A1/180.0)*np.pi
A2 = (A2/180.0)*np.pi
A3 = (A3/180.0)*np.pi

# Length of the links
a1 = 10
a2 = 10
a3 = 10

# D-H(Denavit-Hartenberg) parameters table
dh = np.array([[T1,A1,0,a1], [T2,A2,a2,0], [T3,A3,a3,0]])

# Transformation matrix from frame 0 to frame 1
T0_1 = np.array([[np.cos(dh[0][0]), -np.sin(dh[0][0])*np.cos(dh[0][1]), np.sin(dh[0][0])*np.sin(dh[0][1]), dh[0][2]*np.cos(dh[0][0])],
        [np.sin(dh[0][0]), np.cos(dh[0][0])*np.cos(dh[0][1]), -np.cos(dh[0][0])*np.sin(dh[0][1]), dh[0][2]*np.sin(dh[0][0])],
        [0, np.sin(dh[0][1]), np.cos(dh[0][1]), dh[0][3]],
        [0, 0, 0, 1]])

print("Transformation matrix from frame 0 to frame 1")
print(T0_1)

# Transformation matrix from frame 1 to frame 2
T1_2 = np.array([[np.cos(dh[1][0]), -np.sin(dh[1][0])*np.cos(dh[1][1]), np.sin(dh[1][0])*np.sin(dh[1][1]), dh[1][2]*np.cos(dh[1][0])],
        [np.sin(dh[1][0]), np.cos(dh[1][0])*np.cos(dh[1][1]), -np.cos(dh[1][0])*np.sin(dh[1][1]), dh[1][2]*np.sin(dh[1][0])],
        [0, np.sin(dh[1][1]), np.cos(dh[1][1]), dh[1][3]],
        [0, 0, 0, 1]])

print("\nTransformation matrix from frame 1 to frame 2")
print(T1_2)

# Transformation matrix from frame 2 to frame 3
T2_3 = np.array([[np.cos(dh[2][0]), -np.sin(dh[2][0])*np.cos(dh[2][1]), np.sin(dh[2][0])*np.sin(dh[2][1]), dh[2][2]*np.cos(dh[2][0])],
        [np.sin(dh[2][0]), np.cos(dh[2][0])*np.cos(dh[2][1]), -np.cos(dh[2][0])*np.sin(dh[2][1]), dh[2][2]*np.sin(dh[2][0])],
        [0, np.sin(dh[2][1]), np.cos(dh[2][1]), dh[2][3]],
        [0, 0, 0, 1]])

print("\nTransformation matrix from frame 2 to frame 3")
print(T2_3)

T0_2 = np.dot(T0_1, T1_2)
T0_3 = np.dot(T0_2, T2_3)

print("\nTransformation matrix from frame 0 to frame 3")
print(T0_3)