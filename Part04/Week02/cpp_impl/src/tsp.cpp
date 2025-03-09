#include<fstream>
#include<cstdint>
#include<cmath>
#include<cstring>

using std::string;  

float ** readfile(string filename, uint32_t* np) {
    std::ifstream input(filename);
    uint32_t n;
    input >> n;
    *np = n;

    float vx[n];
    float vy[n];
    for(uint32_t i = 0; i < n; i++) {
        input >> vx[i] >> vy[i];
    }
    float** dist = new float*[n];
    for (uint32_t i = 0; i < n; i++) {
        dist[i] = new float[n];
    }
    for (uint32_t i = 0; i < n; i++) {
        for (uint32_t j = 0; j < n; j++) {
            float square = (vx[i] - vx[j]) * (vx[i] - vx[j]) + (vy[i] - vy[j]) * (vy[i] - vy[j]);
            dist[i][j] = sqrtf32(square);
        }
    }
    return dist;
}

unsigned next_set_of_n_elements(unsigned x) 
  {
     unsigned smallest, ripple, new_smallest, ones;
   
     if (x == 0) return 0;
     smallest     = (x & -x);
     ripple       = x + smallest;
     new_smallest = (ripple & -ripple);
     ones         = ((new_smallest/smallest) >> 1) - 1;
     return ripple | ones;
}
float min(float x, float y) {
    return x < y? x: y;
}

float tsp(uint32_t n, float** dist) {
    uint32_t only_one = 1 << (n - 1);
    uint32_t maxones = 1 << n;
    float **dpp;
    
    dpp = new float*[n];
    
    for (uint32_t i = 0; i < n; i++) {
        dpp[i] = new float[maxones];
        for (uint32_t s = 0; s < maxones; s++) {
            dpp[i][s] = INFINITY;
        }
    }
    dpp[n - 1][only_one] = 0;

    for(uint32_t m = 0; m < n - 1; m++) {
        for (uint32_t s = only_one | (((1 << (m+1)) - 1)); s < maxones; s = next_set_of_n_elements(s)) {
            for(uint32_t j = 0; j < n; j++) {
                uint32_t with_j = 1 << j;
                if ((s & with_j) != 0) {
                    for(uint32_t k = 0; k < n; k++) {
                        uint32_t with_k = 1 << k;
                        if (((s & with_k) != 0) && k != j) {
                            dpp[j][s] = min(dpp[j][s], dpp[k][s & (~with_j)] + dist[j][k]);
                        }
                    }
                }
            }
        }
    }

    float result = INFINITY;
    // printf("%f\n", result);
    for (uint32_t j = 0; j < n - 1; j++) {
        result = min(result, dpp[j][(1 << n) - 1] + dist[j][n-1]);
    }
    for (uint32_t i = 0; i < n; i++) {
        delete[] dpp[i];
    }
    delete[] dpp;
    return result;
}
int main() {
    uint32_t n;
    float** dist;
    dist = readfile("/mnt/e/practice/h_programming_basis/Standford_Algorithm/Part04/Week02/tsp.txt", &n);
    printf("%f\n", tsp(n, dist));
    for (uint32_t i = 0; i < n; i++) {
        delete[] dist[i];
    }
    delete[] dist;
    return 0;
}