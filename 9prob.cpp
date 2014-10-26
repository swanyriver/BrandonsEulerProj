/*
 * 9prob.cpp
 *
 *  Created on: Sep 17, 2014
 *      Author: Brandon
 */

#include <iostream>
#include <string>
#include <cmath>

using namespace std;

const int SUM = 1000;

bool isSquare(int num){
   double sq = sqrt(num);
   return sq == floor(sq);
}



int main(){
   int a=0;
   int b, c;

   while(a<SUM){
      a++;
      cout << a << ",";
      cout.flush();
      b=a+1;
      while(b < (SUM-a)/2){
         c = SUM - a - b;
         //if(isSquare(c) && a*a + b*b == c){
         if(a*a + b*b == c*c){
            cout << endl << a << "^2 + " << b << "^2 = " << c*c << "(" << c << ")";
            cout << endl << "product " << a*b*c<< endl;
            exit(1);
         }
         b++;
      }
   }
}


