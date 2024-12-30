class DirectGraph:
    def __init__(self):
        self.adjacent_list={}

    def add_vertex(self,vertex):
        if vertex not in self.adjacent_list:
            self.adjacent_list[vertex]=[]

    def add_edge(self,from_vertex,to_vertex):
        if from_vertex not in self.adjacent_list:
            self.add_vertex(from_vertex)
        if to_vertex not in self.adjacent_list:
            self.add_vertex(to_vertex)
        self.adjacent_list[from_vertex].append(to_vertex)

    def display(self):
        for vertex,edges in self.adjacent_list.items():
            print(f"{vertex} : {','.join(edges) if edges else 'No edged'}")


dg = DirectGraph()
dg.add_vertex('A')
dg.add_vertex('B')
dg.add_vertex('C')
dg.add_vertex('D')



dg.add_edge('A','1')
dg.display()


    
