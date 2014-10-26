#include <cmath>
#include <iostream>

using namespace std;

const int MAX = 4000000;  //four million
//const int MAX = 400;  //four million

int main(){
   long int a =1;
   long int b =2;
   long int fib=0;
   long int total = 2; //include the second term b;

   while(fib < MAX){
      fib = a + b;
      a = b; b = fib;
      //cout << fib << endl;
      if(fib%2==0){ total += fib;}
   }
   cout << total << endl;
}
