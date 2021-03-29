// 1331B. Limericks
// Completed in 31 ms 0 kb

#include <iostream>
#define newl '\n'
using namespace std;
 
int main() {
    int a;
    cin >> a;
    
    for (int i = 2; i < a; i++) {
        if (a % i == 0) {
            cout << i << a/i << newl;
            return 0;
        }
    }
  
    return 0;
}
