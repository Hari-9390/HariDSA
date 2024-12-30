class DirectGraph:
    def __init__(self,num_vert):
        self.num_vert=num_vert
        self.adj_matrix=[[0 for _ in range(num_vert)]for _ in range(num_vert)]
        self.vertex_join={}
        self.index_join={}
        self.current_index=0

    def add_vertex(self,vertex):
        if vertex not in self.vertex_join:
            self.vertex_join[vertex]=self.current_index
            self.index_join[self.current_index]=vertex
            self.current_index+=1

    def add_edge(self,from_vertex,to_vertex):
        if (from_vertex in self.vertex_join) and (to_vertex in self.vertex_join):
            from_index = self.vertex_join[from_vertex]
            to_index = self.vertex_join[to_vertex]
            self.adj_matrix[from_index][to_index]=1
        else:
            print(f"Error: One or both vertices '{from_vertex}' and '{to_vertex} doesn't exist'")

    def display(self):
        first='  '+'  '.join(self.vertex_join.keys())
        print(first)
        for i,r in enumerate(self.adj_matrix):
            row_dis=' '.join(map(str,r))
            print(f"{self.index_join[i]} {row_dis}")

n=5

dg=DirectGraph(n)
dg.add_vertex("1")
dg.add_vertex("2")
dg.add_vertex("3")
dg.add_vertex("4")
dg.add_vertex("5")
dg.add_edge("1","2")
dg.add_edge("1","3")
dg.add_edge("1","4")
dg.add_edge("2","5")
dg.add_edge("5","4")
dg.add_edge("4","3")
dg.add_edge("3","2")
dg.display()
