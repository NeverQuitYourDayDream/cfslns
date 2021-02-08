// 869B. The Eternal Immortality
// Completed in 31 ms 0 kb

#include<iostream>
 
using namespace std;
 
typedef long long ll;
 
int main() {
    
    ll a, b;
    cin >> a >> b;
    
    if (b - a > 9) {
        cout << 0;
    }
    else {
        ll ld = 1;
        ll i;
        for (i = a + 1; i <= b; i++) {
            ld = (ld * (i % 10)) % 10;
            if (ld == 0) {
                break;
            }
        }
        
        cout << ld << '\n';
    }
    
    return 0;
} 
