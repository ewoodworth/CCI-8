# Recursive fibionacci generator. Turns out the runtime will be about 2^n. Ew, gross.
def fib(i):
    if i == 0:
        return 0
    elif i == 1:
        return 1
    else:
        return fib(i-1) + fib(i-2)

#print fib(22)

#from https://ujihisa.blogspot.com/2010/11/memoized-recursive-fibonacci-in-python.html
#Create a list to cache values
__fib_cache = {}
def fib_dirty_cache(n):
    if n in __fib_cache:
        return __fib_cache[n]
    else:
        __fib_cache[n] = n if n < 2 else fib_dirty_cache(n-2) + fib_dirty_cache(n-1)
        return __fib_cache[n]

# print fib_dirty_cache(300)

# An even more professional and attractive variation would create and use a decorator 
def memoize(f):
    cache = {}
    def decorated_function(*args):
        if args in cache:
            return cache[args]
        else:
            cache[args] = f(*args)
            return cache[args]
    return decorated_function

@memoize
def fib_memoed(n):
    return n if n < 2 else fib_memoed(n-2) + fib_memoed(n-1)

# print fib_memoed(300)

#and then if you really want to show off
def memoize_awesome(f):
    cache = {}
    return lambda *args: cache[args] if args in cache else cache.update({args: f(*args)}) or cache[args]

@memoize_awesome
def fib_memoed_awesome(n):
    return n if n < 2 else fib_memoed_awesome(n-2) + fib_memoed_awesome(n-1)

# print fib_memoed_awesome(300)

#A child is running up a staircase with n steps and can hop either 1 step, 2 steps or 3 steps at a time. How many possible ways can the child run up the steps?

def stair_ways(n):
    if n < 0:
        return 0
    elif n == 0:
        return 1
    else:
        return stair_ways(n-1) + stair_ways(n-2) + stair_ways(n-3)

# print stair_ways(9)
#Notice how long that takes? Memoization to the rescue. Save your patience, conserve your runtime

@memoize_awesome
def stair_ways_memoized(n):
    if n < 0:
        return 0
    elif n == 0:
        return 1
    else:
        return stair_ways_memoized(n-1) + stair_ways_memoized(n-2) + stair_ways_memoized(n-3)

# print stair_ways_memoized(9)

#Robot at the upper left corner of a grid with r rows and c columns. Traverse the grid to the bottom right avoiding specific squares that are off limits

# https://www.cs.bu.edu/teaching/alg/maze/  Good general thoughts on algorithm development
# http://www.laurentluce.com/posts/solving-mazes-using-python-simple-recursivity-and-a-search/ 

grid = [[0, 0, 0, 0, 0, 1],
        [1, 1, 0, 0, 0, 1],
        [0, 0, 0, 1, 0, 0],
        [0, 1, 1, 0, 0, 1],
        [0, 1, 0, 0, 1, 0],
        [0, 1, 0, 0, 0, 2]]

def maze_run(r, c):
    if grid[r][c] == 2:
        print 'found at %d,%d' % (r, c)
        return True
    elif grid[r][c] == 1:
        print 'wall at %d,%d' % (r, c)
        return False
    elif grid[r][c] == 3:
        print 'visited at %d, %d' % (r, c)
        return False

    print 'visiting %d %d' % (r,c)
    grid[r][c] = 3                              #mark as visited save work

    if ((r < len(grid)-1 and maze_run(r+1,c))       
        or (c>0 and maze_run(r,c-1))
        or (r > 0 and maze_run(r-1, c))
        or (c < len(grid)-1 and maze_run(r, c+1))):
        return True
    return False

# maze_run(0,0)

#a magic index in an array exists where A[i] == i Given a sorted array of distinct integers find a magic index, if it exists in A Even if values are not distinct.

A1 = [-40, -20, -1, 1, 2, 3, 5, 7, 9, 12, 13]
A2 = [-10, -5, 2, 2, 2, 3, 4, 7, 9, 12, 13]

def find_the_magic_bs(A):
    return _find_the_magic_bs(A, 0, len(A)-1)

def _find_the_magic_bs(A, start, end):
    if end < start:
        return -1
    mid = (end + start)/2
    if A[mid] == mid:
        return mid
    elif A[mid] > mid:
        return _find_the_magic_bs(A, start, mid-1)
    else:
        return _find_the_magic_bs(A, mid+1, end)

# print find_the_magic_bs(A1)

def find_the_magic(A):
    return _find_the_magic(A, 0, len(A)-1)

def _find_the_magic(A, start, end):
    if end < start:
        return -1
    mid_index = (start + end)/2
    mid_value = A[mid_index]
    if mid_value == mid_index:
        print mid_index
    
    left_index = min(mid_index - 1, mid_value)
    left = _find_the_magic(A, start, left_index)
    if left >= 0:
        return left

    right_index = max(mid_index + 1, mid_value)
    right = _find_the_magic(A, right_index, end)

    return right

# find_the_magic(A2)

#return all subsets of a set
def subsets(l):
    if l == []:
        return [[]]

    x = subsets(l[1:])

    return x + [[l[0]] + y for y in x]

# print (subsets([1, 2, 3]))

#Write a recursive function to multiply two positive integers without using the * operator
def multiply(a, b):
    bigger = max([a, b])
    smaller = min([a, b])
    return _multiply(smaller, bigger)

def _multiply(smaller, bigger):
    if smaller == 0:
        return 0
    elif smaller == 1:
        return bigger

    s = smaller >> 1
    half_prod = _multiply(s, bigger)

    if smaller % 2 == 0:
       return half_prod + half_prod
    else:
        return half_prod + half_prod + bigger

# print multiply(4, 5)  

#tower of hanoi https://interactivepython.org/runestone/static/pythonds/Recursion/TowerofHanoi.html  Total cut and paste, but there's no better way than this to get there

def moveTower(height,fromPole, toPole, withPole):
    if height >= 1:
        moveTower(height-1,fromPole,withPole,toPole)
        moveDisk(fromPole,toPole)
        moveTower(height-1,withPole,toPole,fromPole)

def moveDisk(fp,tp):
    print("moving disk from",fp,"to",tp)

# moveTower(3,"A","B","C")


# Write a method to compose all permutations of a string with no duplicates Pretty much like subsets but string methods or use ennumerate and then it's alsmost identical. See also http://www.jeremy-boyd.com/2010/10/18/compute-all-permutations-of-a-string-in-python/ for fun horrible solution at bottom of page

from itertools import permutations
def permutate(s):
    all_combos = []
    word_list = ["".join(item) for item in _permutate(s)]
    unique_substrings = list(set(word_list))
    for u_string in unique_substrings:
        combos = [''.join(p) for p in permutations(u_string)]
        all_combos += combos
    unique_permutations = list(set(all_combos))
    return unique_permutations

def _permutate(s):
    l = enumerate(s)
    letter_list = [c for i , c in l]
    if letter_list == []:
        return [[]]
    x = _permutate(letter_list[1:])

    return x + [[letter_list[0]] + y for y in x]

print sorted(permutate("onion"))

#Print all valid combinations of n pairs of parenthesis.
# () n=1
# ()() (()) n=2
# ()()() ((())) (())() ((())) ()(())   n=3
#'new' set goes inside, in front or after
def paren(left, right=None):
    if right is None:
        right = left  # allows calls with one argument

    if left == right == 0: # base case
        yield ""

    else:
        if left > 0:
            for p in paren(left-1, right): # first recursion
                yield "("+p

        if right > left:
            for p in paren(left, right-1): # second recursion
                yield ")"+p

print paren(3)