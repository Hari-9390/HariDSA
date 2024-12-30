class Graph:
    def __init__(self):
        self.adj_list={}

    def add_edge(self,node1,node2):
        if node1 not in self.adj_list:
            self.adj_list[node1]=[]
        if node2 not in self.adj_list:
            self.adj_list[node2]=[]
        self.adj_list[node1].append(node2)
        self.adj_list[node2].append(node1)

    def bfs(self,start_node,visited=None):
        if visited is None:
        visited=set()
        dfs
        queue=[start_node]
        bfs_order=[]

        while queue:
            node=queue.pop(0)
            if node not in visited:
                visited.add(node)
                bfs_order.append(node)

                for neighbour in self.adj_list[node]:
                    if neighbour not in visited:
                        queue.append(neighbour)


        return bfs_order
    def display(self):
        for node,neighbours in self.adj_list.items():
            print(f"{node} {','.join(map(str,neighbours))}")

g=Graph()

num_edges=int(input())
for _ in range(num_edges):
    node1=int(input("Enter node1"))
    node2=int(input("Enter node2"))
    g.add_edge(node1,node2)
g.display()

start_node=int(input())
bfs_result=g.bfs(start_node)
print(bfs_result)
