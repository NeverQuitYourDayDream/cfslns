// 6A. Triangle
// Completed in 62 ms 0 kb

#include <iostream>
#include <vector>
#include <algorithm>
#include <cmath>
#include <queue>
#include <set>
#include <map>
#include <iomanip>
#define INF 2147483647;
#define LINF 9223372036854775807;
#define pii pair<int, int>
#define ll long long
#define pb push_back
#define newl '\n'
using namespace std;

void (solve(int segments[])) {

    if (segments[0]+segments[1] > segments[2] || segments[1]+segments[2] > segments[3]) {
        cout << "TRIANGLE" << newl;
    }
    else if (segments[0]+segments[1] == segments[2] || segments[1]+segments[2] == segments[3]) {
        cout << "SEGMENT" << newl;
    }
    else {
        cout << "IMPOSSIBLE" << newl;
    }
}

int main() {
    
    int segments[4];
    for (int i=0; i < 4; i++) {
        cin >> segments[i];
    }
    sort(segments, segments + 4);
    
    solve(segments); 
    return 0;
}
