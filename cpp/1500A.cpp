// 1500A. Going Home
// Completed in 592 ms 58700 kb
// 03/27/2021
#include <iostream>
#define newl '\n'
using namespace std;

int main() {
    int n;
    cin >> n;
    
    int nums[5000000], x[5000000], y[5000000];
    for (int i = 0; i < n; i++) {
        cin >> nums[i];
    }
    
    for (int i = 1; i <= n; i++) {
        for (int j = i+1; j <= n; j++) {
            int s = nums[i] + nums[j];
            
            if (x[s]) {
                if(i != x[s] && i != y[s] && j != x[s] && j != y[s]) {
                    cout << "YES" << newl;
                    cout << i << " ";
                    cout << j << " ";
                    cout << x[s] << " ";
                    cout << y[s] << newl;
                    return 0;
                }
            }
            x[s] = i;
            y[s] = j;
        }
    }
    cout << "NO" << newl;
    return 0;
}
