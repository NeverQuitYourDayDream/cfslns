// 710B. Optimal Point on a Line
// Completed in 546 ms 1200 kb

#include <iostream>
#include <algorithm>
using namespace std;
 
int main() {
    
    int n;
    cin >> n;
    
    int points[n];
    for (int i=0; i < n; i++) {
        cin >> points[i];        
    }
 
    sort(points, points+n);
  
    if (n%2 == 0) {
      cout << points[n/2 - 1] << '\n';
    }
    else {
      cout << points[n/2] << '\n';
    }
 
    return 0;
}
