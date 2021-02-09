// 1372A. Omkar and Completion 
// Completed in 31 ms 0 kb

#include <iostream>

using namespace std;

int main() {
    
    int t;
    cin >> t;
    
    while (t--) {
        int n;
        cin >> n;
        
        // the easiest "complete" array is just n 1s.         
        for (int i = 0; i < n; i++) {
            cout << "1";
        }
        cout << '\n';
    }
    return 0;
}
