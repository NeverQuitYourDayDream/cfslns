// 1033A. King Escape 
// Completed in 30 ms 0 kb
// 2/27/2021

#include <iostream>
#define newl '\n'
using namespace std;

bool safe(int x1, int y1, int x2, int y2) {
    
    // Queen (x1, y1), Square (x2, y2)
    // check if square is diagonally attacked by the queen
    // in this case the slope of the line is 1 or -1
    // alternatively we can also just check if rise == run 
    
    if (x2 - x1 == y2 - y1) {
        return false;
    }
    else if (x2 - x1 == y1 - y2) {
        return false;
    }
    else if (x1 - x2 == y2 - y1) {
        return false;
    }
    else if (x1 - x2 == y1 - y2) {
        return false;
    }
    else {
        return true;
    }
}

int main() {

    int n;
    cin >> n;
    int ax, ay;
    cin >> ax >> ay;
    int bx, by;
    cin >> bx >> by;
    int cx, cy;
    cin >> cx >> cy;

    bool ok;
    
    
    // in any case the King cannot cross the files
    // and ranks attacked by the Queen
    // the board is split into 4 quadrants

    if (bx < ax && cx < ax) {
        if (by < ay && cy < ay) {
            if (safe(ax, ay, cx, cy)) {
                ok = true;
            }
        }
        else if (by > ay && cy > ay) {
            if (safe(ax, ay, cx, cy)) {
                ok = true;
            }
        }
        else {
            ok = false;
        }
    }

    else if (bx > ax && cx > ax) {
        if (by > ay && cy > ay) {
            if (safe(ax, ay, cx, cy)) {
                ok = true;
            }
        }
        else if (by < ay && cy < ay) {
            if (safe(ax, ay, cx, cy)) {
                ok = true;
            }
        }
        else {
            ok = false;
        }
    }
    else {
        ok = false;
    }
    
    // print answer
    if (ok) {
        cout << "YES" << newl;
    }
    else {
        cout << "NO" << newl;
    }

    return 0;
}
