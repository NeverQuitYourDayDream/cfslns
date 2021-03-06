// 1088A. Ehab and another construction problem
// Completed in 31 ms 0 kb
// 3/6/2021

#include <iostream>
#define ll long long
#define newl '\n'
using namespace std;

void solve() {
    int x;
    cin >> x;
    for (int a = 1; a <= x; a++) {
        for (int b = 1; b <= x; b++) {
            if (b%a == 0 && a*b > x && a/b < x){
                cout << b << " " << a << newl;
                return;
            }
        }
    }
    cout << "-1" << newl;
}
 
int main() {
    solve();
    return 0;
}
