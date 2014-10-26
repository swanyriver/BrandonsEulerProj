#include <iostream>
#include <string>
#include <cstdlib>
#include <sstream>

using namespace std;

const int SEED = 999;

bool isPalindrome(string str){
   while(!str.empty()){
      if(str.back() != str.front()){
         return false;
      }else{
         str.erase(0,1);
         if(!str.empty()) str.pop_back();
      }
   }
   return true;
}

bool isPalindrome(int num){
   ostringstream ss;
   ss << num;
   return isPalindrome(ss.str());
}

///Recursive problem takes two numbers 999 and 999
/// a * b
/// a-- b--
/// a * b++ while b<=999

int main(){

   /*cout << "12321 isPal:" << isPalindrome(12321) <<endl;
   cout << "1231 isPal:" << isPalindrome(1231) << endl;
   cout << "1221 isPal:" << isPalindrome(1221) << endl;
   exit(0);
*/
   int product;
   int largestPalin =0;
   int a = SEED;
   int b = SEED;
   do{
      if(b!=SEED+1){
         product = a*b;
      }else{
         a--;
         b=a;
         product = a*b;
      }

      //cout << " a:" << a << " b:" << b << " product:" << product << endl;
      b++;
      //getchar();
      //if(a%10==0)getchar();
      if(isPalindrome(product) && product > largestPalin)
         largestPalin = product;
   }while(a!=0);

   //b--;
   //cout << a << '/'  << b << endl << product << endl;
   cout << endl << largestPalin << endl;

}
