#include<iostream>
using namespace std;

int gcd(int a, int b){
    if (b == 0) return a;
    int aPrime =  a % b;
    return gcd(b, aPrime);
}

int main(){
    int d = gcd(357,234);
    cout << d << '\n';
    return 0;
}