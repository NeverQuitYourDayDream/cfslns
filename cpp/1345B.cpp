// 1345B. Card Constructions
// Completed in 265 ms 0 kb

#include <iostream>
using namespace std;

int cards(int h) {

    // derived formula for number of cards per height:
    // each layer adds 2*(i) + (i-1) = 3*i - 1 cards,
    // to find the amount of cards for a pyramid with 
    // height h, simply sum the card count of all pyramids 
    // above it (1, 2, 3, ... h)

    int res = 0;
    for (int i = 1; i <= h; i++) {
        res += 3*i - 1;
    }
    return res;
}

int solve(int n) {

    int pyramids = 0;
    int i = 0;
    while (n > 0) {

        // minimum number of cards to make a pyramid is 2
        if (n < 2) {
            break;
        }   
    
        // if cards(i) <= n, include it in the pyramid count
        if (cards(i) <= n && cards(i+1) > n) {
            n -= cards(i);
            pyramids++;
            // reset i to 1 - restart the search process
            i = 1;
        }
        else {
            // cannot make a pyramid, or i is too small
            // in this case increment i 
            i++;
        }

    }
    return pyramids;
}

int main() {

    int t;
    cin >> t;
    while (t--) {
        int n;
        cin >> n;
        cout << solve(n) << '\n';
    }
  
    return 0;
}
