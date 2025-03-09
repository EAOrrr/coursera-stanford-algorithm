#include"cluster.h"
#include<iostream>

UF::UF(size_t n):parent(n), rank(n) {
    for (size_t i = 0; i < n; i++) {
        parent[i] = i;
    }
}

void UF::union_(size_t u, size_t v) {
    size_t u_p = find(u), v_p = find(v);
    if (u_p == v_p) return;
    if (rank[u_p] < rank[v_p]) {
        parent[u_p] = v_p;
    }
    else if (rank[u_p] > rank[v_p]) {
        parent[v_p] = u_p;
    }
    else {
        parent[u_p] = v_p;
        rank[v_p]++;
    } 
}

size_t UF::find(size_t x) {
    while (x != parent[x]) {
        parent[x] = parent[parent[x]];
        x = parent[x];
    }
    return x;
}

int cluster(const std::string& filename) {
    std::ifstream input(filename);
    if (!input.is_open()) throw std::runtime_error("cannot open file " + filename);
    size_t n, b;
    input >> n >> b;
    size_t k = n;

    std::vector<std::vector<bool>> nodes;
    UF uf(n);

    for (size_t i = 0; i < n; i++) {
        std::vector<bool> bits(b);
        for (size_t j = 0; j < b; j++) {
            int b;
            input >> b;
            bits[j] = (bool) b;
        }
        for (size_t j = 0; j < nodes.size(); j++) {
            // std::cout << (uf.find(j) != uf.find(nodes.size())) << " " <<  hammingDist(nodes[j], bits) << std::endl;
            if (uf.find(j) != uf.find(nodes.size()) && hammingDist(nodes[j], bits) < 3) {
                uf.union_(j, nodes.size());
                k--;
            }
        }
        nodes.push_back(bits);  
    }
    return k;
}

int hammingDist(const std::vector<bool>& v, const std::vector<bool>& u) {
    int result = 0;
    for (size_t i = 0; i < v.size(); i++) {
        result += (int) (v[i] ^ u[i]);
    }
    return result;
}