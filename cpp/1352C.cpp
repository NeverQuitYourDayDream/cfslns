// 1352C. K-th not divisible by N
// Completed in 31 ms 0 kb

#include <iostream>
#define ll long long

using namespace std;

int main() {

    int t;
    cin >> t;
    while (t--) {
    
        ll n, k;
        cin >> n >> k;
        
        // c represents the amount we shift our answer forward
        // skip c numbers since those will be divisible by n
        // k-th positive integer plus c will be the answer
        
        // c is (k-1) divided by (n-1) rounded down (floor)
        ll c = (k-1) / (n-1);
        cout << k + c << '\n';
    }
    return 0;
}
