#include<fstream>
#include<sstream>
#include<iostream>
#include<vector>
#include<random>
#include"kargerMinCut.h"
using std::endl;    using std::cout;
using std::getline; using std::vector;

Graph buildGraph(std::string filename) {
    std::ifstream input(filename);
    if (!input.is_open()) throw std::runtime_error("fail to open " + filename);
    Graph g;
    std::string line;
    while (std::getline(input, line)) {
        std::istringstream iss(line);
        int u;
        int v;
        iss >> u;
        g.addNode();
        g.addEdge(u-1, u-1);
        while (iss >> v) {
            g.addEdge(u-1, v-1);
        }
    }
    return g;
}
int main() {
    auto g = buildGraph("/mnt/e/practice/h_programming_basis/Standford_Algorithm/Part01/Week04/cppImplement/input.txt");
    // cout << g.kargerMinCut();
    int min = INT32_MAX;
    for (int i = 0; i < 100000; i++) {
        Graph gg = g;
        int cnt = gg.kargerMinCut();
        if (cnt < min) min = cnt;
        // cout << cnt << endl;
    }
    cout << min << endl;
    return 0;
}