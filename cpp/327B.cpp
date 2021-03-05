// 327B. Hungry Sequence
// Completed in 92 ms 0 kb
// 3/4/2021

#include <iostream>
#define ll long long
#define newl '\n'
using namespace std;

int main() {
    
    // one possible solution is printing out the first n primes
    // however this may be too slow for some test cases
    // another solution is to take advantage of the fact that
    // the largest possible test is n = 100,000
    // if we start printing consecutive numbers from 10^5 to 
    // 2 x 10^5, we will return a valid answer, since there's 10^5
    // numbers between 10^5 and 2 x 10^5
  
    int n;
    cin >> n;
    
    for (int i = 0; i < n; i++) {
        cout << 100000 + i << " ";
    }
    
    return 0;
}
