import Complex
import re
import os
import shutil


def test_string():
    s1 = 'hello'
    print('{0} with length {1:2d}'.format(s1[1:2], len(s1)))


def test_list():
    cubes = [1, 8, 27, 65, 125]
    cubes[3] = 4 ** 3
    cubes.append(216)
    cubes.insert(0, 0)
    print(cubes)
    cubes[2:4] = []
    for w in cubes:
        print(w, end=',')

    print()
    del cubes[-1]
    print([x for x in cubes if x >= 64])
    for i, v in enumerate(cubes):
        print(i, v)

    print([(x, y) for x in [1, 2, 3] for y in [3, 1, 4] if x != y])


def test_map():
    my_map = {"a": 1, "b": 2}
    print(my_map)
    for k, v in my_map.items():
        print(k, v)

    if my_map["a"] and my_map["b"]:
        print("well")


def test_file():
    with open('test.txt', 'r') as f:
        for line in f:
            print(line, end='')


def test_class():
    obj = Complex.Complex(1)
    obj.dog = -1
    print(obj.add(2) + obj.dog)


def test_regex():
    print(re.findall(r'\bf[a-z]*', 'which foot or hand fell fastest'))
    print(re.sub(r'(\b[a-z]+) \1', r'\1', 'cat in the the hat'))
    print(re.split(r'\s+', 'I got the best deals  anywhere!'))
    print(re.findall(r'[\w\-\']+', 'which foot or hand\'s fell fas-test'))


def rename_files(dir):
    for file in os.listdir(dir):
        os.rename(dir + file, dir + file[-6:-4] + '. ' + file[:-7] + '.mp4')


def move_files(dir):
    for root, dirs, files in os.walk(dir):
        if root == dir:
            continue
        print(root, dirs, files)
        for i, file in enumerate(files):
            pos = root.rfind('/')
            new_file = dir + root[pos + 1:] + ('' if len(files) == 1 else str(i + 1)) + file[file.rfind('.'):]
            print('mv {0} to {1}'.format(root + '/' + file, new_file))
            shutil.move(root + '/' + file, new_file)
        print('delete dir ', root)
        os.rmdir(root)

# test_string()
# test_list()
# test_map()
# test_file()
# test_class()
# test_regex()
# rename_files('D:/TDDOWNLOAD/runaway/')
# move_files('D:/movie/test/')
