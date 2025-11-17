# CAMPUS NAVIGATION & UTILITY PLANNER

# BUILDING DATA ADT
class Building:
    def __init__(data,BuildingID,BuildingName,LocationDetails):
        data.BuildingID=BuildingID
        data.BuildingName=BuildingName
        data.LocationDetails=LocationDetails
    def __str__(data):
        return f"{data.BuildingID} - {data.BuildingName} ({data.LocationDetails})"


# BINARY SEARCH TREE (BST)
class BSTNode:
    def __init__(node,building):
        node.building=building
        node.left=None
        node.right=None

class BST:
    def __init__(tree):
        tree.root=None
    def insert(tree,building):
        def add(node,building):
            if not node:
                return BSTNode(building)
            if building.BuildingID<node.building.BuildingID:
                node.left=add(node.left,building)
            else:
                node.right=add(node.right,building)
            return node
        tree.root=add(tree.root,building)
    def search(tree,BuildingID):
        def find(node,BuildingID):
            if not node:
                return None
            if node.building.BuildingID==BuildingID:
                return node.building
            if BuildingID<node.building.BuildingID:
                return find(node.left,BuildingID)
            return find(node.right,BuildingID)
        return find(tree.root,BuildingID)
    def inorder(tree):
        result=[]
        def go(node):
            if node:
                go(node.left)
                result.append(str(node.building))
                go(node.right)
        go(tree.root)
        return result
    def preorder(tree):
        result=[]
        def go(node):
            if node:
                result.append(str(node.building))
                go(node.left)
                go(node.right)
        go(tree.root)
        return result
    def postorder(tree):
        result=[]
        def go(node):
            if node:
                go(node.left)
                go(node.right)
                result.append(str(node.building))
        go(tree.root)
        return result
    def height(tree):
        def h(node):
            if not node:
                return 0
            return 1+max(h(node.left),h(node.right))
        return h(tree.root)


# AVL TREE
class AVLNode:
    def __init__(node,building):
        node.building=building
        node.left=None
        node.right=None
        node.height=1

class AVL:
    def __init__(tree):
        tree.root=None
    def get_height(tree,node):
        if not node:
            return 0
        return node.height
    def get_balance(tree,node):
        return tree.get_height(node.left)-tree.get_height(node.right)
    def rotate_right(tree,y):
        x=y.left
        T2=x.right
        x.right=y
        y.left=T2
        y.height=1+max(tree.get_height(y.left),tree.get_height(y.right))
        x.height=1+max(tree.get_height(x.left),tree.get_height(x.right))
        return x
    def rotate_left(tree,x):
        y=x.right
        T2=y.left
        y.left=x
        x.right=T2
        x.height=1+max(tree.get_height(x.left),tree.get_height(x.right))
        y.height=1+max(tree.get_height(y.left),tree.get_height(y.right))
        return y
    def insert(tree,building):
        def add(node,building):
            if not node:
                return AVLNode(building)
            if building.BuildingID<node.building.BuildingID:
                node.left=add(node.left,building)
            else:
                node.right=add(node.right,building)
            node.height=1+max(tree.get_height(node.left),tree.get_height(node.right))
            balance=tree.get_balance(node)
            if balance>1 and building.BuildingID<node.left.building.BuildingID:
                print("AVL rotation LL at",node.building.BuildingID)
                return tree.rotate_right(node)
            if balance<-1 and building.BuildingID>node.right.building.BuildingID:
                print("AVL rotation RR at",node.building.BuildingID)
                return tree.rotate_left(node)
            if balance>1 and building.BuildingID>node.left.building.BuildingID:
                print("AVL rotation LR at",node.building.BuildingID)
                node.left=tree.rotate_left(node.left)
                return tree.rotate_right(node)
            if balance<-1 and building.BuildingID<node.right.building.BuildingID:
                print("AVL rotation RL at",node.building.BuildingID)
                node.right=tree.rotate_right(node.right)
                return tree.rotate_left(node)
            return node
        tree.root=add(tree.root,building)
    def inorder(tree):
        result=[]
        def go(node):
            if node:
                go(node.left)
                result.append(str(node.building))
                go(node.right)
        go(tree.root)
        return result
    def height(tree):
        return tree.get_height(tree.root)


# GRAPH 
from collections import defaultdict,deque
import heapq

class Graph:
    def __init__(g):
        g.adj_list=defaultdict(list)
        g.nodes=[]
    def add_edge(g,u,v,w):
        g.adj_list[u].append((v,w))
        g.adj_list[v].append((u,w))
        if u not in g.nodes:
            g.nodes.append(u)
        if v not in g.nodes:
            g.nodes.append(v)
    def adjacency_matrix(g):
        size=len(g.nodes)
        matrix=[[0]*size for _ in range(size)]
        for i,u in enumerate(g.nodes):
            for v,w in g.adj_list[u]:
                j=g.nodes.index(v)
                matrix[i][j]=w
        return matrix
    def BFS(g,start):
        visited=set()
        q=deque([start])
        order=[]
        while q:
            node=q.popleft()
            if node not in visited:
                visited.add(node)
                order.append(node)
                for v,_ in g.adj_list[node]:
                    q.append(v)
        return order
    def DFS(g,start):
        visited=set()
        order=[]
        def go(node):
            if node not in visited:
                visited.add(node)
                order.append(node)
                for v,_ in g.adj_list[node]:
                    go(v)
        go(start)
        return order
    def dijkstra(g,start):
        dist={node:float("inf") for node in g.nodes}
        dist[start]=0
        pq=[(0,start)]
        while pq:
            d,u=heapq.heappop(pq)
            if d>dist[u]:
                continue
            for v,w in g.adj_list[u]:
                nd=d+w
                if nd<dist[v]:
                    dist[v]=nd
                    heapq.heappush(pq,(dist[v],v))
        return dist
    def kruskal(g):
        edges=[]
        for u in g.nodes:
            for v,w in g.adj_list[u]:
                edges.append((w,u,v))
        edges.sort()
        parent={node:node for node in g.nodes}
        def find(x):
            while parent[x]!=x:
                x=parent[x]
            return x
        mst=[]
        for w,u,v in edges:
            pu=find(u)
            pv=find(v)
            if pu!=pv:
                mst.append((u,v,w))
                parent[pu]=pv
        return mst


# EXPRESSION TREE 
class ExprNode:
    def __init__(node,val):
        node.val=val
        node.left=None
        node.right=None

class ExpressionTree:
    def buildExpressionTree(tree,postfix):
        stack=[]
        for ch in postfix:
            node=ExprNode(ch)
            if ch in "+-*/":
                node.right=stack.pop()
                node.left=stack.pop()
            stack.append(node)
        return stack.pop()
    def evaluateExpression(tree,node):
        if node.val.isdigit():
            return int(node.val)
        L=tree.evaluateExpression(node.left)
        R=tree.evaluateExpression(node.right)
        if node.val=="+":
            return L+R
        if node.val=="-":
            return L-R
        if node.val=="*":
            return L*R
        if node.val=="/":
            return L//R


#MAIN
def insertBuilding(BuildingTree,BuildingID,BuildingName,LocationDetails):
    b=Building(BuildingID,BuildingName,LocationDetails)
    BuildingTree.insert(b)

def traverseBuildings(BuildingTree,mode="inorder"):
    if mode=="inorder":
        return BuildingTree.inorder()
    if mode=="preorder":
        return BuildingTree.preorder()
    if mode=="postorder":
        return BuildingTree.postorder()
    return []

def addBuildingRecord(BuildingTree,BuildingID,BuildingName,LocationDetails):
    insertBuilding(BuildingTree,BuildingID,BuildingName,LocationDetails)

def listCampusLocations(BuildingTree):
    return traverseBuildings(BuildingTree,"inorder")

def constructCampusGraph(CampusGraph,edges):
    for u,v,w in edges:
        CampusGraph.add_edge(u,v,w)

def findOptimalPath(CampusGraph,start):
    return CampusGraph.dijkstra(start)

def planUtilityLayout(CampusGraph):
    return CampusGraph.kruskal()


if __name__=="__main__":
    b1=Building(10,"Admin Block","Main Office")
    b2=Building(5,"Library","Central Library")
    b3=Building(20,"Hostel","Student Housing")
    b4=Building(15,"CSE Block","Computer Science Department")

    print("\nBST (BuildingTree using BST)")
    bst=BST()
    addBuildingRecord(bst,b1.BuildingID,b1.BuildingName,b1.LocationDetails)
    addBuildingRecord(bst,b2.BuildingID,b2.BuildingName,b2.LocationDetails)
    addBuildingRecord(bst,b3.BuildingID,b3.BuildingName,b3.LocationDetails)
    addBuildingRecord(bst,b4.BuildingID,b4.BuildingName,b4.LocationDetails)
    print("Inorder:",listCampusLocations(bst))
    print("Preorder:",traverseBuildings(bst,"preorder"))
    print("Postorder:",traverseBuildings(bst,"postorder"))
    print("BST Height:",bst.height())

    print("\nAVL (BuildingTree using AVL)")
    avl=AVL()
    avl.insert(b1)
    avl.insert(b2)
    avl.insert(b3)
    avl.insert(b4)
    print("AVL inorder:",avl.inorder())
    print("AVL Height:",avl.height())
    print("Compare Heights -> BST:",bst.height(),"AVL:",avl.height())

    print("\nCampusGraph")
    g=Graph()
    constructCampusGraph(g,[
        ("Admin","Library",4),
        ("Library","Hostel",6),
        ("Admin","Hostel",8),
        ("Admin","CSE",3),
        ("CSE","Library",2)
    ])
    print("Adjacency List:",g.adj_list)
    print("Adjacency Matrix:",g.adjacency_matrix())
    print("BFS from Admin:",g.BFS("Admin"))
    print("DFS from Admin:",g.DFS("Admin"))
    print("Dijkstra from Admin:",findOptimalPath(g,"Admin"))
    print("Kruskal MST (planUtilityLayout):",planUtilityLayout(g))

    print("\nExpressionTree for energy bill")
    et=ExpressionTree()
    root=et.buildExpressionTree("23*54*+")
    print("Energy Bill (evaluateExpression):",et.evaluateExpression(root))
