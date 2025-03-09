#include <fstream>
#include <algorithm>
#include <vector>
#include <cmath>

using std::pair;    using std::vector;

double** readfile(const std::string& filename, int* np) {
    std::ifstream input(filename);
    int n;
    input >> n;
    *np = n;
    double vx[n], vy[n];
    for(int i = 0; i < n; i++) {
        int idx;
        input >> idx >> vx[i] >> vy[i];
    }

    double** distances = new double*[n];
    for (int i = 0; i < n; i++) {
        distances[i] = new double[n];
    }
    for (int i = 0; i < n; i++) {
        for (int j = 0; j < n; j++) {
            if (i == j) distances[i][j] = INFINITY;
            else {
                distances[i][j] = std::pow((vx[i] - vx[j]), 2)
             + std::pow((vy[i]-vy[j]), 2);
            }
        }
    }
    return distances;
}

double** get_squared_distances(const vector<pair<double, double>>& cities) {
    int n = cities.size();
    double** distances = new double*[n];
    for (int i = 0; i < n; i++) {
        distances[i] = new double[n];
    }
    for (int i = 0; i < n; i++) {
        for (int j = 0; j < n; j++) {
            if (i == j) distances[i][j] = INFINITY;
            else {
                distances[i][j] = std::pow((cities[i].first - cities[j].first), 2)
             + std::pow((cities[i].second - cities[j].second), 2);
            }
        }
    }
    return distances;
}

double find_min(int visiting, bool* visited, double** distances, int n) {
    double min_dist = INFINITY;
    int to_visit = -1;
    for (int city = 0; city < n; city++) {
         if (!visited[city] && distances[visiting][city] < min_dist) {
            min_dist = distances[visiting][city];
            to_visit = city;
         }
    }
    return to_visit;
}

double tsp_nearest_neighbor_heuristic(int n, double** distances) {
    double dist = 0;
    int visiting = 0, visited_cnt = 1;
    // vector<bool> visited(n, false);
    bool visited[n];
    for (int i = 0; i < n; i++) {
        visited[i] = false;
    }
    visited[visiting] = true;

    while (visited_cnt != n) {
        int next_to_visit = find_min(visiting, visited, distances, n);
        dist += std::sqrt(distances[visiting][next_to_visit]);
        visited_cnt += 1;
        visited[next_to_visit] = true;
        visiting = next_to_visit;
    }

    dist += std::sqrt(distances[0][visiting]);
    return dist;
}

int main() {
    int n;
    auto distances = readfile("/mnt/e/practice/h_programming_basis/Standford_Algorithm/Part04/Week03/nn.txt", &n);
    // auto distances = readfile("/mnt/e/practice/h_programming_basis/Standford_Algorithm/Part04/Week03/cpp_impl/test.txt", &n);
    
    printf("hello\n");
    double result = tsp_nearest_neighbor_heuristic(n, distances);
    printf("%f\n", result);
    for (int i = 0; i < n; i++) {
        delete[] distances[i];
    }
    delete[] distances;
    return 0;
}