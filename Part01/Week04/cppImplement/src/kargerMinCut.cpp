#include"kargerMinCut.h"

// Graph::Graph(Graph& g) {
    
// }

void Graph::addNode() {
    graph.push_back({});
}

void Graph::addEdge(int u, int v) {
    graph[u].push_back(v);
}

int Graph::kargerMinCut() {
    while (graph.size() > 2) {
        contrast();
    }
    return graph[0].size()-1;
}


void Graph::contrast() {
    static std::random_device r;
    static std::default_random_engine e(r());
    // static int cnt = 0;
    size_t v0Idx = std::uniform_int_distribution<int>(0, graph.size() - 1)(e); 
    size_t v0 = graph[v0Idx][0];
    size_t v1 = graph[v0Idx][std::uniform_int_distribution<int>(1, graph[v0Idx].size() - 1)(e)];       // v2.id
    size_t v1Idx = binarySearch(v1);
    // std::cout << cnt <<  ": " << v0 << " " << v1 << std::endl;
    // cnt++;
    // merge and remove self-loop
    std::vector<size_t> adj{v0};
    for (auto p = graph[v0Idx].begin() + 1; p < graph[v0Idx].end(); p++) {
        if (*p != v1 && *p != v0) adj.push_back(*p);
    }
    for (auto p = graph[v1Idx].begin() + 1; p < graph[v1Idx].end(); p++) {
        if (*p != v0 && *p != v1) adj.push_back(*p);
    }
    graph[v0Idx] = adj;
    for (size_t i = 0; i < graph.size(); i++) {
        if (i != v0Idx) {
            for (size_t j = 1; j < graph[i].size(); j++) {
                if (graph[i][j] == v1) graph[i][j] = v0;
            }
        }
    }
    graph.erase(graph.begin() + v1Idx);
}

int Graph::binarySearch(size_t u) {
    int start = 0, end = graph.size() - 1;
    while (start <= end) {
        int mid = start + (end-start) / 2;
        if (graph[mid][0] == u) return mid;
        else if (graph[mid][0] < u) start = mid+1;
        else end = mid-1;
    }
    // if (graph[end][0] == u) return end;
    throw std::runtime_error("index invalid: " + std::to_string(u));
}