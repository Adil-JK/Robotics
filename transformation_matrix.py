import numpy as np

# Theta in degrees
T1 = 0
T2 = 0
T3 = 0

# Theta in radians
T1 = (T1/180.0)*np.pi
T2 = (T1/180.0)*np.pi
T3 = (T1/180.0)*np.pi

# Length of the links
a1 = 10
a2 = 10
a3 = 10

# Rotational matrices

R0_1 = np.array([[np.cos(T1), 0, -np.sin(T1)], [np.sin(T1), 0, np.cos(T1)], [0, 1, 0]])
R1_2 = np.array([[np.cos(T2), -np.sin(T2), 0], [np.sin(T2), np.cos(T2), 0], [0, 0, 1]])
R2_3 = np.array([[np.cos(T3), -np.sin(T3), 0], [np.sin(T3), np.cos(T3), 0], [0, 0, 1]])

R0_2 = np.dot(R0_1, R1_2)
R0_3 = np.dot(R0_2, R2_3)

# Displacement vectors

d0_1 = np.array([[0], [0], [a1]])
d1_2 = np.array([[a2*np.cos(T2)], [a2*np.sin(T2)], [0]])
d2_3 = np.array([[a3*np.cos(T3)], [a3*np.sin(T3)], [0]])

# Transformation matrices

T0_1 = np.concatenate((R0_1, d0_1), 1)
T0_1 = np.concatenate((T0_1,[[0,0,0,1]]), 0)

T1_2 = np.concatenate((R1_2, d1_2), 1)
T1_2 = np.concatenate((T1_2,[[0,0,0,1]]), 0)

T2_3 = np.concatenate((R2_3, d2_3), 1)
T2_3 = np.concatenate((T2_3,[[0,0,0,1]]), 0)

T0_2 = np.dot(T0_1, T1_2)
T0_3 = np.dot(T0_2, T2_3)

print("Transformation matrix from frame 0 to frame 3")
print(T0_3)