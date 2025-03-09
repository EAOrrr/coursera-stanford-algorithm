#include <fstream>
#include <algorithm>
#include <vector>
#include <cmath>

using std::pair;    using std::vector;

vector<pair<double, double>> readfile(const std::string& filename, int* np) {
    std::ifstream input(filename);
    int n;
    input >> n;
    *np = n;
    vector<pair<double, double>> cities(n);
    // double vx[n], vy[n];
    for(int i = 0; i < n; i++) {
        int idx;
        input >> idx >> cities[i].first >> cities[i].second;
    }
    return cities;
    // double** distances = new double*[n];
    // for (int i = 0; i < n; i++) {
    //     distances[i] = new double[n];
    // }
    // for (int i = 0; i < n; i++) {
    //     for (int j = 0; j < n; j++) {
    //         if (i == j) distances[i][j] = INFINITY;
    //         else {
    //             distances[i][j] = std::pow((vx[i] - vx[j]), 2)
    //          + std::pow((vy[i]-vy[j]), 2);
    //         }
    //     }
    // }
    // return distances;
}

double get_distance(const vector<pair<double, double>>& cities, int i, int j) {
    return std::pow((cities[i].first - cities[j].first), 2)
             + std::pow((cities[i].second - cities[j].second), 2);
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

double find_min(int visiting, bool* visited, vector<pair<double, double>> cities, int n) {
    double min_dist = INFINITY;
    int to_visit = -1;
    for (int city = 0; city < n; city++) {
        double distance = get_distance(cities, visiting, city);
        if (!visited[city] &&  distance < min_dist) {
            min_dist = distance;
            to_visit = city;
         }
    }
    return to_visit;
}

double tsp_nearest_neighbor_heuristic(int n, vector<pair<double, double>> cities) {
    double dist = 0;
    int visiting = 0, visited_cnt = 1;
    // vector<bool> visited(n, false);
    bool visited[n];
    for (int i = 0; i < n; i++) {
        visited[i] = false;
    }
    visited[visiting] = true;

    while (visited_cnt != n) {
        int next_to_visit = find_min(visiting, visited, cities, n);
        dist += std::sqrt(get_distance(cities, visiting, next_to_visit));
        visited_cnt += 1;
        visited[next_to_visit] = true;
        visiting = next_to_visit;
    }

    dist += std::sqrt(get_distance(cities, visiting, 0));
    return dist;
}

int main() {
    int n;
    auto cities = readfile("/mnt/e/practice/h_programming_basis/Standford_Algorithm/Part04/Week03/nn.txt", &n);
    // auto cities = readfile("/mnt/e/practice/h_programming_basis/Standford_Algorithm/Part04/Week03/cpp_impl/test.txt", &n);
    
    printf("hello\n");
    double result = tsp_nearest_neighbor_heuristic(n, cities);
    printf("%f\n", result);
    // for (int i = 0; i < n; i++) {
    //     delete[] distances[i];
    // }
    // delete[] distances;
    return 0;
}