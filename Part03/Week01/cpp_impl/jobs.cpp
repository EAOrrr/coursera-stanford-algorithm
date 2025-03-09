#include<iostream>
#include<fstream>
#include<vector>
#include<algorithm>
#include<stdexcept>

using std::cout;    using std::endl;
using std::vector;  

struct Job {
    int weight;
    int length;
};

vector<Job> readJobs() {
    // std::ifstream input("/mnt/e/practice/h_programming_basis/Standford_Algorithm/Part03/Week01/smalltest.txt");
    std::ifstream input("/mnt/e/practice/h_programming_basis/Standford_Algorithm/Part03/Week01/jobs.txt");
    if (!input.is_open()) throw std::runtime_error("cannot open file");
    int n;
    input >> n;
    vector<Job> result;
    while (n--) {
        int w, l;
        input >> w >> l;
        result.push_back({w, l});
    }
    return result;
}

long long falseSchedule(vector<Job>& jobs) {
    std::sort(jobs.begin(), jobs.end(), 
        [](Job j1, Job j2) {
            return (j1.weight - j1.length > j2.weight - j2.length) || 
                (j1.weight-j1.length == j2.weight - j2.length && j1.weight > j2.weight);
        });
    long long  result = 0;
    int completeTime = 0;
    int cnt = 0;
    for (auto& job: jobs) {
        
        completeTime += job.length;
        result += completeTime * job.weight;
    }
    return result;
}

long long trueSchedule(vector<Job>& jobs) {
    std::sort(jobs.begin(), jobs.end(), 
        [](Job j1, Job j2) {
            return ((double)j1.weight/j1.length > (double)j2.weight/j2.length);
        });
    long long  result = 0;
    int completeTime = 0;
    int cnt = 0;
    for (auto& job: jobs) {
        completeTime += job.length;
        result += completeTime * job.weight;
    }
    return result;
}

int main() {
    vector<Job> jobs = readJobs();
    cout << falseSchedule(jobs) << endl;
    cout << trueSchedule(jobs) << endl;

}