//============================================================================
// Name        : xordecrypt.cpp
// Author      : 
// Version     :
// Copyright   : Your copyright notice
// Description : Hello World in C++, Ansi-style
//============================================================================

#include <iostream>
#include "hashMap.h"
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include "hashMap.h"
#include "dictionary.h"
#include "cipher.h"

using namespace std;

const int NUMCHARS = 1201;
const int PADDED = 64*14;

/*
void decrypt(char* in, char* out, char* key){

    char lkey[64];
    char onek;
    for(char* x=0;x<64;onek=key[(++x)%3]) lkey[x]=onek;

    long long int* esi= in;
    long long int* edi= out;

    for(int i=0;i<PADDED;i+=64){
        *edi = *esi^lkey;
        edi+=64;
        esi+=64;
    }

    *(out+NUMCHARS)=0;

}
*/

void decrypt(char* in, char* out, char* key){

    char onek;
    for(int x=0;x<NUMCHARS;onek=key[(++x)%3]){
       *out=(*in)^onek;
       ++in;
       ++out;
    }
    *out=0;
}

int main() {

    hashMap* myDict = createDict();

    char* test = (char*) malloc(PADDED);
    for(char* i=test; i<test+PADDED; i+=16){
        strcpy(i,"hello Brandon :)");
    }
    *(test+NUMCHARS)=0;

    char* out = (char*) malloc(PADDED);

    printf("%s\n",test);
    decrypt(test,out,"abc");
    printf("%s\n",out);

    decrypt(out,out,"abc");
    printf("%s\n",out);


	return 0;
}
