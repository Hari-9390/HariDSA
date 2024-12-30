class graph:
    def __init__(self):
        self.adj_list={}

    def add_edge(self,node1,node2):
        if node1 not in self.adj_list:
            self.adj_list[node1]=[]
        if node2 not in self.adj_list:
            self.adj_list[node2]=[]

        self.adj_list[node1].append(node2)
        self.adj_list[node2].append(node1)

    def dfs(self,st_node,visit=None):
        if visit is None:
            visit=set()
        visit.add(st_node)
        dfs_ord=[st_node]
        for nei in self.adj_list[st_node]:
            if nei not in visit:
                dfs_ord+=self.dfs(nei,visit)

        return dfs_ord

    def display(self):
        for node,nei in self.adj_list.items():
            print(f"{node} -> {','.join(map(str,nei))}")

q=graph()
num_edge=int(input("enter the number of edges"))
for _ in range(num_edge):
    node1=int(input("enter node1"))
    node2=int(input("enter node2"))
    q.add_edge(node1,node2)
q.display()
st_node=int(input("enetr the start node"))
dfs_res=q.dfs(st_node)
print(dfs_res)
