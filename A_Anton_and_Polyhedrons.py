n=int(input())
count=0
hmap={"Tetrahedron":4,
      "Cube":6,
      "Octahedron":8,
      "Dodecahedron":12,
      "Icosahedron":20   }

for i in range(n):
    s=input()

    count+=hmap[s]

print(count)