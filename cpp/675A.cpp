// 675A. Infinite Sequences 
// Completed in 577 ms 0 kb
// 2/27/2021

#include <iostream>
#include <vector>
#include <algorithm>
#include <cmath>
#include <queue>
#include <set>
#include <map>
#include <iomanip>
#define INF 2147483647
#define LINF 9223372036854775807
#define pii pair<int, int>
#define ll long long
#define pb push_back
#define newl '\n'
using namespace std;

void solve() {
    int a, b, c;
    cin >> a >> b >> c;
    
    if (c == 0) {
        if (a != b) {
            cout << "NO" << newl;
            return;
        }
        else {
            cout << "YES" << newl;
            return;
        }
    }
    else if (c > 0) {
        for (int i = a; i <= b; i += c) {
            if (i == b) {
                cout << "YES" << newl;
                return;
            }
        }
    }
    else {
        for (int i = a; i >= b; i += c) {
            if (i == b) {
                cout << "YES" << newl;
                return;
            }
        }
    }

    cout << "NO" << newl;
}

int main() {
    solve();  
    return 0;
}
