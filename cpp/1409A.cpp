// 1409A. Yet Another Two Integers Problem
// Completed in 140 ms 0 kb
// 3/1/2021

#include <iostream>
#define ll long long
#define newl '\n'
using namespace std;

int solve(ll a, ll b) {

    if (a == b) {
        return 0;
    }
    
    if (a > b) {
        return (a - b - 1) / 10 + 1;
    }
    else {
        return (b - a - 1) / 10 + 1;
    }
}

int main() {

    int t;
    cin >> t;
    while (t--) {
        ll a, b;
        cin >> a >> b;
        cout << solve(a, b) << newl;
    }

    return 0;
}
