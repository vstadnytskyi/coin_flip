##http://www.python-course.eu/graphs_python.php This is a nice place to learn about graphs, how to use and how to code them.
##

from random import randint
import numpy as np
import matplotlib.pyplot as plt
import time 
from math import factorial as fc

class coin_flip_graph(object):
    def __init__(self):
        self.graph = {}
        self.graph[''] = ["h","t"]
    def add_level(self):
        for i in self.graph.keys():
            for j in self.graph[i]:
                self.graph[j] = [j  + 'h' , j  + 't'] 
        return
    def h_or_t(self, lst):
        res = 0
        for i in lst:
            if i == 'h':
                res = res + 1
        return res
    def max_branch(self):
        max_len = 0
        for i in self.graph.keys():
            if len(i)>max_len:
                max_len = len(i)  
        return max_len
    def delete_smaller_branches(self):
        for i in self.graph.keys():
            if len(i) < self.max_branch():
                del self.graph[i]
    def sum_of_leaves(self):
        res = []
        for i in self.graph.keys():
            if len(i) == self.max_branch():
                res.append(self.h_or_t(i))
        return res        
    def find_k(self,n):
        res = 0    
        for i in self.sum_of_leaves():
            if i == n:
                res = res +1
        return res
def analytical_solution(tosses,k_heads):
    n = tosses
    k = k_heads
    return (fc(n)/(fc(k)*fc(n-k)))*((0.5)**k)*(1-0.5)**(n-k)

    #request input: how many times to toss the coin

#reques input: how many total heads is expected after n tosses
k_heads = 1
tosses = 0

if k_heads >= tosses:
    tosses = int(float(raw_input("how many time to toss (n):")))  
    k_heads =   int(float(raw_input("how many heads (k) in (n) tosses: "))) 
coin_flip = coin_flip_graph()
t_start = time.time()
for i in range(tosses):
    coin_flip.add_level()
    coin_flip.delete_smaller_branches() #<- this will erase branches smaller than the largest one. 
print 'time for computing ',time.time() - t_start, 'seconds'
#print coin_flip._sum_of_leaves()
print 'total sum of all leaves', len(coin_flip.sum_of_leaves())
print 'how many leaves have k =',k_heads,'heads =', coin_flip.find_k(3)
print 'probability of (k)',k_heads,' heads in (n)' ,tosses, 'tosses, computational', float(coin_flip.find_k(k_heads))/float(len(coin_flip.sum_of_leaves()))
print 'probability of ',k_heads,' heads in',tosses, 'tosses, analytical', analytical_solution(tosses,k_heads)  
print 'the length of the dictionary', len(coin_flip.graph)      