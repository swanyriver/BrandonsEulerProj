/*
 * 7prob.cpp
 *
 *  Created on: Sep 17, 2014
 *      Author: Brandon
 */


#include <iostream>
#include <string>
#include <cmath>
#include <iterator>
#include <list>

using namespace std;

const int Nth = 10001;

bool isPrime(long int num, list<long int> &primes){
   int max = ceil(sqrt(num));

   for(list<long int>::const_iterator it = primes.begin(); *it<=max && it!=primes.end(); it++){
      if(num%*it==0) return false;
   }
   return true;
}

int main(){
   list<long int> primes;
   primes.push_back(2);

   while(primes.size()!=Nth){
      int a = primes.back() +1;
      while(!isPrime(a,primes)){
         a++;
      }
      primes.push_back(a);
      cout << primes.size() << ":" << primes.back() << endl;
      //getchar();
   }

}



