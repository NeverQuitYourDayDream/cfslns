// 1436B. Prime Square
// Completed in 30 ms 0 kb
// 03/15/2021

#include <iostream>
#include <vector>
#include <algorithm>
#include <cmath>
#define ll long long
#define newl '\n'

using namespace std;

int main() {
    int t;
    cin >> t;
    while (t--) {
        int n;
        cin >> n;

        for (int i = 0; i < n; i++) {
            for (int j = 0; j < n; j++) {
                if (i == j || (i+1) % n == j) {
                    cout << 1 << " ";
                }
                else {
                    cout << 0 << " ";
                }
            }
            cout << newl;
        }
    
    }
    return 0;
}
