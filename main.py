import sys, os
from filecmp import cmp

def find_identical_pairs(dir1 : str, dir2 : str):
    for file1 in os.listdir(dir1):
        first_fullpath = dir1 + '/' + file1
        for file2 in os.listdir(dir2):
            second_fullpath = dir2 + '/' + file2
            if cmp(first_fullpath, second_fullpath):
                print(first_fullpath + ' - ' + second_fullpath)

def calculate_similarity_procent(firstpath, secondpath):
    file1, file2 = open(firstpath), open(secondpath)
    text1, text2 = file1.read(), file2.read()
    d1, d2 = {i: text1.count(i) for i in text1}, {j: text2.count(j) for j in text2}
    file1.close()
    file2.close()
    error = 0
    if len(text1) >= len(text2):
        for key in d1:
            error += abs(d1[key] - d2.get(key, 0))
        return 100 * (1 - error / len(text1))

    for key in d2:
        error += abs(d1.get(key, 0) - d2[key])
    return 100 * (1 - error / len(text2))

def looks_pretty_same(dir1: str, dir2: str, similarity_procent: int):
    for file1 in os.listdir(dir1):
        first_fullpath = dir1 + '/' + file1
        for file2 in os.listdir(dir2):
            second_fullpath = dir2 + '/' + file2
            proc = calculate_similarity_procent(first_fullpath, second_fullpath)
            if proc >= similarity_procent:
                print(first_fullpath + ' - ' + second_fullpath + ' ' + str(proc))

def exists_in_first_not_in_second(dir1: str, dir2: str, similarity_procent: int):
    for file1 in os.listdir(dir1):
        first_fullpath = dir1 + '/' + file1
        for file2 in os.listdir(dir2):
            second_fullpath = dir2 + '/' + file2
            if calculate_similarity_procent(first_fullpath, second_fullpath) >= similarity_procent:
                print(first_fullpath)
                break

def exists_in_second_not_in_first(dir1: str, dir2: str):
    exists_in_first_not_in_second(dir2, dir1)




first_dir, second_dir = input(), input()
similarity_procent = int(input())

find_identical_pairs(first_dir, second_dir)
looks_pretty_same(first_dir, second_dir)
exists_in_first_not_in_second(first_dir, second_dir)
exists_in_second_not_in_first(first_dir, second_dir)


