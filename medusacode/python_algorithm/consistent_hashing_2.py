#!/usr/bin/env python
# coding:utf-8


import consistent_hash

print '>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>'
nodes = range(10)
print nodes

ch = consistent_hash.ConsistentHash(nodes)
# print ch

ns = []
for key in range(20):
    ns.append(ch.get_node(str(key)))
print ns
print '>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>'
ch.add_nodes(range(10, 15, 1))

ns = []
for key in range(20):
    ns.append(ch.get_node(str(key)))
print ns
print '>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>'

# >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
# [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
# [8, 0, 0, 3, 7, 0, 0, 6, 2, 9, 6, 6, 5, 2, 7, 3, 0, 2, 5, 3]
# >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
# [8, 12, 0, 12, 7, 0, 0, 6, 2, 9, 6, 12, 5, 12, 7, 3, 10, 14, 10, 3]
# >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
