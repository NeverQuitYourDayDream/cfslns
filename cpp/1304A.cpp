/*
 * 1304A. Two Rabbits
 *
 * Completed in 31 ms 0 kb
 */

#include <iostream>
 
using namespace std;
 
int main() {
 
    int t;
    cin >> t;
    while (t --) {
        int x, y, a, b;
        cin >> x >> y >> a >> b;
        int dxy = y - x;
        
        if (dxy % (a + b) == 0) {
            cout << dxy / (a + b) << endl;
        } 
        else {
            cout << -1 << endl;
        }
    }
 
    return 0;
}
