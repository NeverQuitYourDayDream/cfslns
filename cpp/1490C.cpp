// 1490C. Sum of Cubes
// Completed in 109 ms 0 kb

#include <iostream>
#include <vector>
#include <algorithm>
#include <cmath>
#include <set>
#include <unordered_set>
#include <string>
#include <map>
#include <iomanip>
#define ll long long
#define newl '\n'
using namespace std;

void solve() {
    
    ll x;
    cin >> x;
    
    for (ll i = 1; i*i*i < x; i++) {
        ll a = x - i*i*i;
        ll l = 0;
        ll r = 10000;
        
        while (l < r-1) {
            
            // modified binary search to find cube
            ll mid = (r+l) / 2;
            if (mid*mid*mid >= a) {
                r = mid;
            }
            else {
                l = mid;
            }
        }
        // if final value of r has r*r*r == a, cout << "YES"
        // otherwise continue onto next i
        if (r*r*r == a) {
            cout << "YES" << newl;
            return;
        }
    }
    // cout << "NO" if no cube is found
    cout << "NO" << newl;
}

int main() {
    
    int t;
    cin >> t;
    while (t--) {
        solve();
    }
    
    return 0;
}
