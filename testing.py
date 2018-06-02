__author__ = 'Dennis Qiu'
from binarySearchTree import BinarySearchTree
from AVLtree import AVLTree
import time
import sys
import math

predicted_times = {}
d_sizes = [100, 1000, 10000,20000]
tree_dic = open('tree.txt', 'w', encoding='utf-8')

def dictionary(dic_file):
    """
    Reads in dictionary.txt.
    :param dic_file: dictionary.txt file
    :return: list of words in dictionary.txt
    """
    dic_list = []
    with open(dic_file, 'r', encoding='UTF-8') as words:
        for line in words.readlines():
            dic = line.strip()
            dic = dic.lower()
            dic_list.append(dic)
    return dic_list

def O_logn_time(time1, size2, size1=d_sizes[0]):
    """

    :param time1:
    :param size2:
    :param size1:
    :return: O logn time
    """
    return time1 * math.log(size2) / math.log(size1)

def O_n_time(time1, size2, size1=d_sizes[0]):
    """

    :param time1:
    :param size2:
    :param size1:
    :return:
    """
    return time1 * size2 / size1

def predict_bigO_time(cur_size, cur_time, next_size):
    """
    calculate the expected times for next size with different complexity performances
    based on current time measured for current size
        O(N2)
        O(N)
        O(NlogN)
        O(logN)
    :param cur_size:
    :param cur_time:
    :param next_size:
    :return: None
    """
    t_n2 = cur_time * next_size * next_size / cur_size / cur_size
    t_n = cur_time * next_size / cur_size
    t_nlogn = cur_time * next_size * math.log(next_size) / cur_size / math.log(cur_size)
    t_logn = cur_time * math.log(next_size) / math.log(cur_size)
    print('Based on time measured for current size {}: {:5f} seconds, for next size {}:\n\
           \tcurrent  : {:5f}\n\
           \tO(logN)  : {:5f}\n\
           \tO(N)     : {:5f}\n\
           \tO(NlogN) : {:5f}\n\
           \tO(N2)    : {:5f}\n'.format(cur_size, cur_time, next_size, cur_time, t_logn, t_n, t_nlogn, t_n2))

def search_time(dic, d, Tree, orderedList=False):
    """
    Measures the time it takes to search word in the given list
    :param dic: the word (value of the node) to be searched
    :param d: the word list, it can be random or ordered list
    :param Tree: a tree object (can be BinarySearchTree or AVLTree)
    :param orderedList: a flag to indicate whether wList is an ordered list or not, by default is not
    :return: measured time from start to finish
    """
    size = len(d)
    if Tree == "AVLTree":
        tree = AVLTree()
    elif Tree == "BinarySearchTree":
        tree = BinarySearchTree()
    else:
        print("Unsupported tree type: {}".format(Tree))
        return 0
    if orderedList:
        list_str = 'ordered list'
    else:
        list_str = 'random list'

    try:
        for i in range(size):
            tree[i] = d[i]
    except RecursionError as e:
        print('Exception caught while building the {} with size {}: {}'.format(Tree, size, e))
        tree_dic.write('Error in building {},  size {:5d}, {}, word: "{}"\n'.format(Tree, size, list_str, dic))
        return 0
    print('{}, height of tree: {}, size of tree: {}'.format(Tree, tree.height(tree.root), len(tree)))

    tree.set_balanceFactor()
    start = time.clock()
    try:
        if orderedList:
            dKey = tree.search_ordered_list(dic)
        else:
            dKey = tree.search_random_list(dic)
        if dKey:
            print('yes, {} is in tree, found at key {}'.format(dic, dKey))
        else:
            print("no, {} is not found in tree".format(dic))
    except RecursionError as e:
        print('Exception caught during search with size {}: {}'.format(size, e))
        tree_dic.write('Error during search {}, size {:5d}, {}, word: "{}"\n'.format(Tree, size, list_str, dic))
        return 0
    stop = time.clock()
    d_time = stop - start
    print('Searching for word "{}" in size {} tree took {:5f} seconds'.format(dic, size, d_time))

    if dKey:
        word_str = 'word in tree'
    else:
        word_str = 'word not in tree'
    tree_dic.write('\nSearch time: {:5f} seconds \n{}: size {}\n{}, word: "{}"\n'.format(d_time, list_str, size, word_str, dic))

    sizes = d_sizes
    this_size = sizes.index(size)
    if this_size < len(sizes) - 1:
        nextSize = sizes[this_size + 1]
        predict_bigO_time(size, d_time, nextSize)
    return d_time

def main():
    sys.setrecursionlimit(5000)

    rand_dic = dictionary('./dictionary.txt')
    sort_dic = sorted(rand_dic)

    rdic1 = rand_dic[:100]
    sdic1 = sort_dic[:100]

    r = rdic1[36]
    s = sdic1[36]
    not_dic = 'dark'

    tree_dic.write('BinarySearchTree')
    print('SEARCHING WORD IN TREE WITH RANDOM LIST')
    ordered_list = False
    with open("./InRandomTree.csv", "w", encoding='utf-8') as t:
        t.write('size, BST, AVLT, O-logN, O-n\n')
        for i in d_sizes:
            rdic = list(rand_dic[:i])
            bst = search_time(r, rdic, "BinarySearchTree", ordered_list)
            avlt = search_time(r, rdic, "AVLTree", ordered_list)
            if i == 100:
                base_t = avlt
                t_logn = base_t
                t_n = base_t
            else:
                t_logn = O_logn_time(base_t, i)
                t_n = O_n_time(base_t, i)
            t.write("{:5d}, {:6f}, {:6f}, {:6f}, {:6f}\n".format(i, bst, avlt, t_logn, t_n))
            print('\t')

    print('SEARCHING WORD NOT IN TREE WITH RANDOM LIST')
    with open("./NotInRandomTree.csv", "w", encoding='utf-8') as t:
        t.write('size, BST, AVLT, O-logN, O-n\n')
        for i in d_sizes:
            rdic = list(rand_dic[:i])
            bst = search_time(not_dic, rdic, "BinarySearchTree", ordered_list)
            avlt = search_time(not_dic, rdic, "AVLTree", ordered_list)
            if i == 100:
                base_t = avlt
                t_logn = base_t
                t_n = base_t
            else:
                t_logn = O_logn_time(base_t, i)
                t_n = O_n_time(base_t, i)
            t.write("{:5d}, {:6f}, {:6f}, {:6f}, {:6f}\n".format(i, bst, avlt, t_logn, t_n))
            print('\t')

    print('SEARCHING WORD IN TREE WITH ORDERED LIST')
    ordered_list = True
    with open("./InOrderedTree.csv", "w", encoding='utf-8') as t:
        t.write('size, BST, AVLT, O-logN, O-n\n')
        for i in d_sizes:
            sdic = list(sort_dic[:i])
            bst = search_time(s, sdic, "BinarySearchTree", ordered_list)
            avlt = search_time(s, sdic, "AVLTree", ordered_list)
            if i == 100:
                base_t = avlt
                t_logn = base_t
                t_n = base_t
            else:
                t_logn = O_logn_time(base_t, i)
                t_n = O_n_time(base_t, i)
            t.write("{:5d}, {:6f}, {:6f}, {:6f}, {:6f}\n".format(i, bst, avlt, t_logn, t_n))
            print('\t')

    print('SEARCHING WORD NOT IN TREE WITH ORDERED LIST')
    with open("./NotInOrderedTree.csv", "w", encoding='utf-8') as t:
        t.write('size, BST, AVLT, O-logN, O-n\n')
        for i in d_sizes:
            sdic = list(sort_dic[:i])
            bst = search_time(not_dic, sdic, "BinarySearchTree", ordered_list)
            avlt = search_time(not_dic, sdic, "AVLTree", ordered_list)
            if i == 100:
                base_t = avlt
                t_logn = base_t
                t_n = base_t
            else:
                t_logn = O_logn_time(base_t, i)
                t_n = O_n_time(base_t, i)
            t.write("{:5d}, {:6f}, {:6f}, {:6f}, {:6f}\n".format(i, bst, avlt, t_logn, t_n))
            print('\t')
    tree_dic.close()
if __name__ == '__main__':
    main()