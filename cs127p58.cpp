//Name:  Lameya Mostafa
//Email: Lameya.mostafa18@myhunter.cuny.edu
//Date:  December 4,2022
//This program prints a triangle

#include <iostream>
using namespace std;
 int main(){
    int x;
    char y;
    cout<< "Enter an int: ";
    cin>> x;
    cout<< "Enter a symbol other than space: ";
    cin>> y;
    for (int i=1; i<=x; i++){
        for (int j=1;j<=i;++j){
            cout<< y ; 
        }
        cout<< "\n";
    }
    return 0;

 }