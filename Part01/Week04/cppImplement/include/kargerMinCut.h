#ifndef KARGERMINCUT_H
#define KARGERMINCUT_H

#include<vector>
#include<random>
#include<stdexcept>
#include<iostream>

class Graph {
    public:
        Graph() = default;
        // Graph(Graph& g);
        void addEdge(int u, int v);
        void addNode();
        int kargerMinCut();
        void contrast();
    private:
        std::vector<std::vector<size_t>> graph;
        int binarySearch(size_t u);
};
#endif