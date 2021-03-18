// 560A. Currency System in Geraldion
// Completed in 31 ms 0 kb
// 03/17/2021

#include <iostream>
#include <vector>
#include <algorithm>
#include <cmath>
#define ll long long
#define newl '\n'

using namespace std;

int main() {
    int n;
    cin >> n;
    
    // if 1 in the banknotes, 
    // then any number can be 
    // made using 1s
    
    // if 1 not in banknotes,
    // then 1 is the minimum
    // number that cannot be 
    // made (return ans = 1)
    
    while (n--) {
        int x;
        cin >> x;
        if (x == 1) {
            // if x == 1 cout -1
            // exit immediately
            cout << -1 << newl;
            return 0;
        }
    }
    
    cout << 1 << newl;
    return 0;
}
