//Name:  Lameya Mostafa
//Email: Lameya.mostafa18@myhunter.cuny.edu
//Date:  December 12,2022
//This program prints two's compliment


#include <iostream>
using namespace std;

int main(){
    cout<< "Enter an integer between [-128,127]";
    int n;
    cin>> n; 
    int num = n; 
    string result ="";
    int rem;
    if (num <0) {
        num= -num-1;    
    } 
    int size = 8 ;
    int len = result.length() ;
    for (int i = 0; i < size - len; i++) {
        result = "0" + result;
    }

    for(int i = result.length()-1; i <result.length(); i--){
        rem = num % 2;
        result.replace(i,1,to_string(rem));
        num /= 2;
    }


    if (n < 0) {
        for (int i = 0; i < 8; i++) {
            if (result[i] == '0') {
                result[i] = '1' ;
            }
            else {
                result[i] = '0' ;
            }
        }
    }

    cout << "binary string: " ;
    cout << result ;


}


