//Name:  Lameya Mostafa
//Email: Lameya.mostafa18@myhunter.cuny.edu
//Date:  December 4,2022
//This program prints academic standing based on credits

#include <iostream>
using namespace std;
int main(){
    int x;
    cout<< "Enter number of credit hours taken: ";
    cin>> x;
    if (x <28){
        cout<< "freshman";
    } else{
        if (x==28 & x< 61){
            cout<<"sophomore";
        } else{
            if (61==x & x<94){
                cout<< "junior";
            } else{
                cout<< "senior";
            }
        }
    }
    return 0;
}
