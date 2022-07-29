#include<iostream>
using namespace std;

int main(){
    int n;
    cin >> n;
    long long total = 0;
    total = (1 + n) * (n / 2.0);

    int temp;
    for (int i = 0; i < n-1; i++){
        cin >> temp;
        total -= temp;
    }
    cout << total << '\n';
    return 0;
}