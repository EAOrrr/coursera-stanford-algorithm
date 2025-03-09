#ifndef GRAPH_H
#define GRAPH_H
#include<vector>
#include<algorithm>
class Graph {
    public:
        Graph(size_t n);
        void addEdge(int u, int v);
        std::vector<int> reverseTopologicalSort();
        void dfsReverseTopo(int i, std::vector<bool>& visited,
            std::vector<int>& ordering, int& order);
        std::vector<int> scc();
        void dfsSCC(int x, std::vector<bool>& visited, int scc_id, std::vector<int>& scc_id_vec);
    private:
        std::vector<std::vector<int>> inAdj;
        std::vector<std::vector<int>> outAdj;
        size_t size;
};

#endif