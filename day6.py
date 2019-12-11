#!/usr/bin/python3

from io import StringIO
from typing import Dict, io

test_input = '''COM)B
B)C
C)D
D)E
E)F
B)G
G)H
D)I
E)J
J)K
K)L
K)YOU
I)SAN'''

class Node:
    def __init__(self, name, path='', orbits=0):
        self._name = name
        self._path = path
        self._orbits = orbits
        self._next_node = None

    def add_next_node(self, node):
        self._next_node = node

    def __str__(self) -> str:
        return 'Node {}; Next -> {}'.format(self._name, self._next_node)

    def __repr__(self) -> str:
        return '<Node: {} {} {}>'.format(self._name, self._path, self._orbits)


nodes = {}

def transform_input(file: io) -> Dict:
    tmp = {}
    for line in file.readlines():
        root, leaf = line.strip().split(')')
        if root not in tmp:
            tmp[root] = []
        tmp[root].append(leaf)
    return tmp
    # return  dict(*[line.split(')') for line in file.readlines())
    # return [k for line in file.readlines() for k in line.split(')')]

Nodes = []

def calc(nodes, root_node, path='', orbits=0):
    Nodes.append(Node(root_node, path, orbits))
    children = nodes.get(root_node)
    if children:
        for child in nodes[root_node]:
            calc(nodes, child, path+'|'+root_node, orbits+1)

# def parse_input(file: io) -> Generator:
#     for line in file.readlines():
#         root, leaf = line.split(')')
#         if root not in nodes:
#             nodes[root] = Node(root)
#         nodes[root].add_next_node(Node(leaf))


def main():
    # tmp = transform_input(StringIO(test_input))
    tmp = transform_input(open('day6.in', 'r'))
    # print(tmp)
    calc(tmp, 'COM', orbits=0)
    print(sum(i._orbits for i in Nodes))
    you_san = [set(n._path.split('|')) for n in Nodes if n._name in ['SAN', 'YOU']]
    # print(you_san)
    print(you_san[0] - you_san[1])
    print(len(you_san[0] - you_san[1])+1)
    


if __name__ == '__main__':
    main()