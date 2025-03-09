#include<fstream>
#include<vector>
#include<iostream>

#include"graph.h"

int offset(int u, int size) {
    if (u > 0) {
        return u - 1;
    }
    else {
        return size - u - 1;
    }
}

Graph readfile(const std::string& filename, int* n) {
    std::ifstream input(filename);
    int m, size;
    input >> m;
    size = m*2;
    Graph g(size);
    *n = m;
    for (int i = 0; i < m; i++) {
        int u, v;
        input >> u >> v;
        g.addEdge(offset(-u, m), offset(v, m));
        g.addEdge(offset(-v, m), offset(u, m));
    }
    return g;
}
int inverse_offset(int offset_u, int size) {
    if (offset_u < size) {
        return offset_u + 1;
    }
    return size - offset_u - 1;
}

bool satisfiable(const std::string& filename) {
    int n;
    Graph g = readfile(filename, &n);
    auto scc_id_vec = g.scc();
    for (int i = 1; i <= n; i++) {
        if(scc_id_vec[offset(i, n)] == scc_id_vec[offset(-i, n)]) {
            return false;
        }
    }
    return true;
}

int main() {
    for (int i = 1; i <= 6; i++) {
        std::string filename = "/mnt/e/practice/h_programming_basis/Standford_Algorithm/Part04/Week04/2sat" + std::to_string(i) + ".txt";
        std::cout << satisfiable(filename) << std::endl;
    }
    // std::cout << satisfiable("/mnt/e/practice/h_programming_basis/Standford_Algorithm/Part04/Week04/test.txt") << std::endl;
}