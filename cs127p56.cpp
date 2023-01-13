//Name:  Lameya Mostafa
//Email: Lameya.mostafa18@myhunter.cuny.edu
//Date:  November23,2022
//This program takes two integers as bound and prints all even integers

#include <iostream>
using namespace std;

int main() {
    int x;
    int y;
    cout << "Enter start: ";
    cin>> x;
    cout<< "Enter end: ";
    cin>> y;
    for (int i=x; i<= y; i++){
        if (i%2==0){
            cout<< i <<"\n" ;
        } else {
            continue;
        }
    }


}