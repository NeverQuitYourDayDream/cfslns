// 47A. Triangular Numbers
// Completed in 31 ms 0 kb

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

int main() {

    int n;
    cin >> n;

    int x = 1;
    while (x * (x+1) / 2 < n) {
        x += 1;
    }

    if (x * (x+1) / 2 <= n) { 
        cout << "YES" << newl;
    }
    else {
        cout << "NO" << newl;
    }

    return 0;
}
