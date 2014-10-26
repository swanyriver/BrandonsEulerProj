/*
 * prob5.cpp
 *
 *  Created on: Sep 10, 2014
 *      Author: Brandon
 */

#include <iostream>

using namespace std;

const int MAX = 20;

bool divisible(long int num, int divisor=2){
   if(divisor==MAX){
      return num%divisor == 0;
   }else{
      return (num%divisor == 0) && divisible(num, ++divisor);
   }
}

int main(){
   long int a=2520;
   while(!divisible(a)){
      a+=20;
   }
   cout << endl << a << endl;
}


