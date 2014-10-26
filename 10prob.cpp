/*
 * 10prob.cpp
 *
 *  Created on: Sep 17, 2014
 *      Author: Brandon
 */
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

const int Nth = 2*pow(10,6);

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

   while(primes.back()<Nth){
      int a = primes.back() +1;
      while(!isPrime(a,primes)){
         a++;
      }
      primes.push_back(a);
      cout << primes.size() << ":" << primes.back() << endl;
      //getchar();
   }
   primes.pop_back();

   size_t sum=0;

   for(list<long int>::const_iterator it = primes.begin(); it!=primes.end(); it++){
      sum += *it;
   }
   cout << endl << endl << sum << endl;

}







