import Complex
import re
import os

def testString():
    s1='hello'
    print('{0} with length {1:2d}'.format(s1[1:2],len(s1)))

def testList():
    cubes = [1, 8, 27, 65, 125]
    cubes[3] = 4**3
    cubes.append(216)
    cubes.insert(0, 0)
    print(cubes)
    cubes[2:4] = []
    for w in cubes:
        print(w, end=',')
        
    print()
    del cubes[-1]
    print([x for x in cubes if x >= 64])
    for i,v in enumerate(cubes):
        print(i,v)
        
    print([(x, y) for x in [1,2,3] for y in [3,1,4] if x != y])

def testMap():
    mymap={"a":1,"b":2}
    print(mymap)
    for k,v in mymap.items():
        print(k,v)
    
    if(mymap["a"] and mymap["b"]):
        print("well")
        
    
def testFile():
    with open('test.txt', 'r') as f:
        for line in f:
            print(line, end='')
    
def testClass():
    obj = Complex.Complex(1)
    obj.dog = -1
    print(obj.add(2)+obj.dog)

def testRegex():
    print(re.findall(r'\bf[a-z]*', 'which foot or hand fell fastest'))
    print(re.sub(r'(\b[a-z]+) \1', r'\1', 'cat in the the hat'))
    print(re.split(r'\s+', 'I got the best deals  anywhere!'))
    print(re.findall(r'[\w\-\']+', 'which foot or hand\'s fell fas-test'))
    
def filesRename(dirPath):
    for file in os.listdir(dirPath):
        os.rename(dirPath+file, dirPath+file[-6:-4]+'. '+file[:-7]+'.mp4')

# testString()
# testList()
# testMap()
# testFile()
# testClass()
# testRegex()
# filesRename('D:/TDDOWNLOAD/runaway/')