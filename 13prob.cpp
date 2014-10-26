/*
 * 13prob.cpp
 *
 *  Created on: Sep 17, 2014
 *      Author: Brandon
 */
#include <vector>
#include <list>
#include <fstream>
#include <iostream>

using namespace std;

const int DIGIT = 50;
const int N = 100;

inline int num(char c){
   return c - '0';
}

int main(){
   vector<vector<int>*> places;
   list<int> longSum;

   for(int i=0;i<DIGIT;i++){
      places.push_back(new vector<int>);
   }

   ifstream nums("50digs.txt");
   string line;
   for (int l = 0; l < N; ++l) {
      nums >> line;
      //cout << l << ":"<< line << endl;
      for(int i=0;i<DIGIT;i++){
         (*places[i]).push_back(num(line.at(i)));
      }
   }
   nums.close();

   //getchar();

   while(!places.empty()){
      vector<int> collumn = *places.back();
      places.pop_back();

      long int sum= 0;
      while(!collumn.empty()){
         sum+=collumn.back();
         collumn.pop_back();
      }

      //add sum to list
      longSum.push_front(sum%10);
      sum = sum/10;

      vector<vector<int>*>::reverse_iterator it=places.rbegin();

      while(sum>0){
         if(it!=places.rend()){
            (*it)->push_back(sum%10);
            it++;
         }else{
            places.insert(places.begin(),new vector<int>);
            (*places.begin())->push_back(sum%10);
         }
         sum = sum/10;
      }

   }

   cout << endl << endl;
   //for(list<int>::iterator it = longSum.begin(); distance(longSum.begin(),it)<10; it++){
   for(list<int>::iterator it = longSum.begin(); it!=longSum.end(); it++){
      cout << *it;
   }
   cout << endl;


}



