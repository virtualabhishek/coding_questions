class UnionFind:
    def __init__(self,size):
        self.root = [i for i in range(size)]

    # union takes O(N) everytime
    # def find(self, x):
    #     return self.root[x]
    #
    # def union(self, x, y):
    #     rootX = self.find(x)
    #     rootY = self.find(y)
    #     if rootX != rootY:
    #         for i in range(len(self.root)):
    #             if(self.root[i] == rootY):
    #                 self.root[i] = rootX
    #     return

    # takes less than 0(N) time if find is fast
    # def find(self, x):
    #     while(x != self.root[x]):
    #         x = self.root[x]
    #     return self.root[x]
    #
    # def union(self, x, y):
    #     rootX = self.find(x)
    #     rootY = self.find(y)
    #     if rootX != rootY:
    #         self.root[rootY] = rootX
    #     return

    # Optimized path
    def find(self, x):
        if(x == self.root[x]):
            return x
        self.root[x] = self.find(self.root[x])
        return self.root[x]

    def union(self, x, y):
        rootX = self.find(x)
        rootY = self.find(y)
        if rootX != rootY:
            self.root[rootY] = rootX
        return

    def isConnected(self, x, y):
        return self.find(x) == self.find(y)

if __name__ == "__main__":
    ob = UnionFind(10)
    ob.union(1,2)
    ob.union(1,3)
    ob.union(3,4)
    ob.union(5,6)
    print(ob.isConnected(1,4))
    print(ob.isConnected(1,6))


