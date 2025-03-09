#include"graph.h"
#include<iostream>

Graph::Graph(size_t n):inAdj(n), outAdj(n), size(n){}

void Graph::addEdge(int u, int v) {
    // std::cout << size << ' ' << u << ' ' << v << std::endl;
    outAdj[u].push_back(v);
    inAdj[v].push_back(u);
}

std::vector<int> Graph::reverseTopologicalSort() {
    std::vector<bool> visited(size, false);
    std::vector<int> ordering(size);
    int order = size-1;
    for (size_t i = 0; i < size; i++) {
        if (!visited[i]) {
            dfsReverseTopo(i, visited, ordering, order);
        }
    }
    return ordering;
}

void Graph::dfsReverseTopo(int i, std::vector<bool>& visited, 
    std::vector<int>& ordering, int& order) {
    visited[i] = true;
    for (int x: inAdj[i]) {
        if (!visited[x]) {
            dfsReverseTopo(x, visited, ordering, order);
        }
    }
    ordering[order--] = i;
}

void Graph::dfsSCC(int x, std::vector<bool>& visited,
                    int scc_id, std::vector<int>& scc_id_vec) {
    int nodes = 0;
    visited[x] = true;
    scc_id_vec[x] = scc_id;
    for (auto v: outAdj[x]) {
        if (!visited[v]) {
            dfsSCC(v, visited, scc_id, scc_id_vec);
        }
    }
}

std::vector<int> Graph::scc() {
    auto order = reverseTopologicalSort();
    std::vector<bool> visited(size, false);
    std::vector<int> result;
    std::vector<int> scc_id_vec(size);
    int scc_id = 0;
    for (int v: order) {
        if (!visited[v]) {
            dfsSCC(v, visited, scc_id, scc_id_vec);
            scc_id += 1;
        }
    }
    // std::cout << scc_id << ' ' << size << std::endl;
    return scc_id_vec;
}