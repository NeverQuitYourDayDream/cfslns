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
    
    int t;
    cin >> t;
    while (t--) {
        
        int n;
        cin >> n;
        
        int ans = 0;
        int levels[n];
        
        for (int i = 0; i < n; i++) {
            cin >> levels[i];
        }
        
        sort(levels, levels + n);

        for (int i = 0; i < n; i++) {
            if (levels[i] != levels[0]) {
                ans++;
            }
        }
        cout << ans << newl;
    }
    return 0;
}
