from egz1btesty import runtests
from collections import deque

class Node:
  def __init__( self):
    self.left = None    # lewe poddrzewo
    self.right = None   # prawe poddrzewo
    self.parent = None       # pole do wykorzystania przez studentow
    self.color = 0

def solve( root ):

  heights = [1]
  nodes = [[]]
  queue = deque()

  queue.append( (root, 1) )

  while len(queue) > 0:

    temp, h = queue.popleft()

    if len(heights) < h + 1:
        heights.append(0)
        nodes.append([])

    #print(h, len(heights), heights)

    if temp.left != None:
      heights[h] += 1
      temp.left.parent = temp
      nodes[h].append(temp.left)
      queue.append( (temp.left, h + 1))
    
    if temp.right != None:
      heights[h] += 1
      temp.right.parent = temp
      nodes[h].append(temp.right)
      queue.append( (temp.right, h + 1))

  return heights, nodes
  
def purge( root ):

  val = 0
  queue = deque()

  queue.append(root)


  while len(queue) > 0:

    temp = queue.popleft()

    if temp.left != None:
      
      if temp.left.color == 0:
        
        val += 1
        temp.left = None
      else:
        queue.append(temp.left)

    if temp.right != None:

      if temp.right.color == 0:
        val += 1
        temp.right = None
      else:
        queue.append(temp.right)

  return val

def wideentall( T ):

  heights, nodes = solve( T )

  #print(heights)
  #print(nodes)
  

  endi = 0

  for i in range(len(heights)):

    if heights[i] >= heights[endi]:
      endi = i

  queue = deque()
  for i in range(len(nodes[endi])):
    nodes[endi][i].color = 1
    queue.append(nodes[endi][i])

  while len(queue) > 0:

    temp = queue.popleft()

    if temp.parent != None:
      temp.parent.color = 1
      queue.append(temp.parent)

  #for i in range(len(nodes)):
  #  for j in range(len(nodes[i])):
  #    print(i, nodes[i][j].color)
  
  res = purge( T )

  #print(res)

  return res


A = Node()
B = Node()
C = Node()
A.left = B
A.right = C
D = Node()
E = Node()
B.left = D
B.right = E
F = Node()
E.right = F
G = Node()
F.right = G

wideentall( A )

#runtests( wideentall, all_tests = False )