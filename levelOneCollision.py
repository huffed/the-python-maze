coords = [
    [967, 1113, 567, 521],
    [1,2,3,4]
]

var = 0
x1 = []
x2 = []
y1 = []
y2 = []
loop = "True"

while loop == "True":
    x1.append(coords[var][0])
    x2.append(coords[var][2])
    y1.append(coords[var][1])
    y2.append(coords[var][3])
    var = var + 1
    checkIndex = var in range(-len(coords), len(coords))
    if checkIndex == False:
        loop = "False"

print(x1)
print(x2)
print(y1)
print(y2)
