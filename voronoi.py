import matplotlib.pyplot as plt
import numpy as np
from scipy.spatial import Delaunay

s = """10 13
0 229 188
1 81 291
2 302 69
3 186 219
4 201 314
5 131 273
6 161 353
7 278 282
8 256 289
9 78 35
9 1 5
1 5 6
5 9 6
9 6 3
6 3 4
3 4 0
3 9 0
4 0 8
4 6 8
0 8 7
6 8 7
7 0 2
9 0 2"""
s = s.split("\n")
n = int(s[0].split(" ")[0])
s = s[1:]

points = []
for i in range(n):
    points.append(list(map(int, s[i].split()[1:])))

s = s[n:]
triangles = []

for line in s:
    triangles.append(list(map(int, line.split())))

points = np.array(points)

plt.triplot(points[:, 0], points[:, 1], triangles)
plt.plot(points[:, 0], points[:, 1], 'o')
plt.show()

tri = Delaunay(points)

plt.triplot(points[:, 0], points[:, 1], tri.simplices)
plt.plot(points[:, 0], points[:, 1], 'o')
plt.show()
