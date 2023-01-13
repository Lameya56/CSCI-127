//Name:  Lameya Mostafa
//Email: Lameya.mostafa18@myhunter.cuny.edu
//Date:  December 12,2022
//This program converts Celsius to Farenheit

#include <iostream>
using namespace std;
#include <iostream>
using namespace std;

int main() {
    cout << "Input your annual budget: " ;
    double budget ;
    cin >> budget ;
    cout << "Input your month expense: " ;
    double expense;
    cin >> expense ;
    double inflation = expense*1.15;
    for (int i = 1; i < 13; i++) {
        if (i > 6){
            budget = budget - inflation ;
            printf("%5d\t%7.2f\t%27.2f\n", i, inflation, budget);
        }
        else {
            budget = budget - expense ;
            printf("%5d\t%7.2f\t%27.2f\n", i, expense, budget);
        }

    }
    if (budget < 0){
        cout << "need higher budget" ;
    }

}