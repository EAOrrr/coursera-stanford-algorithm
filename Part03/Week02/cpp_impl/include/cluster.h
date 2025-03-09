#ifndef CLUSTER_H
#define CLUSTER_H

#include<vector>
#include<fstream>
#include<stdexcept>

class UF {
    public:
        UF(size_t n);
        void union_(size_t u, size_t v);
        size_t find(size_t x);
    private:
        std::vector<size_t> parent;
        std::vector<size_t> rank;
};

int cluster(const std::string& filename);
int hammingDist(const std::vector<bool>& v, const std::vector<bool>& u);
#endif