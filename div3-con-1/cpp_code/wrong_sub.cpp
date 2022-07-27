#include <bits/stdc++.h>
using namespace std;
    
int main() {
    // solution comes here
    int num, n;
    cin >> num >> n;

    while (n > 0){
        if (num % 10 == 0){
            num /= 10;
        }else{
            num--;
        }
        n--;
    }
    cout << num << '\n';
}
