class SocialNetwork:
    def __init__(self):
        self.graph={}
    def add_node(self,node):
        if node not in self.graph:
            self.graph[node] = []
    def add_edge(self,node1,node2):
        if node1 in self.graph and node2 in self.graph:
            self.graph[node1].append(node2)
            self.graph[node2].append(node1)


    def __str__(self):
        return str(self.graph)
def main():
    n=int(input())
    social_network=SocialNetwork()
    for _ in range(n):
        operation=input().strip().split()
        command=operation[0]
        if command=="AddNode":
            node=int(operation[1])
            social_network.add_node(node)
        elif command=="AddEdge":
            node1=int(operation[1])
            node2=int(operation[2])
            social_network.add_edge(node1,node2)
    print(social_network)

if __name__ == "__main__":
    main()

