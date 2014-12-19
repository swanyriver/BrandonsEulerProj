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

void getKey(int i, char* key){
    key[0]= i%26+'a';
    key[1]= (i%(26*26))/26 +'a';
    key[2]= i/(26*26)+'a';
}

int score(char* text, hashMap* dict){
    int result = 0;
    char* finger = text;
    char* fileEnd = text+NUMCHARS;
    while(finger<fileEnd){
        char* wordEnd=finger;
        while(*wordEnd!=' ' && wordEnd<fileEnd)++wordEnd;
        *wordEnd=0;
        if(isWord(dict,finger)) ++result;
        finger = wordEnd+1;
    }
    return result;
}

int main() {

    char* out = (char*) malloc(NUMCHARS+1);

    /*hashMap* myDict = createDict();



    char key[4];
    key[3]=0;
    int BestWordMatch = 0;
    char bestKey[3];

    for(int i = 0; i<(26*26*26); ++i){

        getKey(i,key);
        //printf("%s  %d\n",key, key[1]);

        decrypt(cipherText,out,key);

        int wordMatch = score(out,myDict);
        if (wordMatch>BestWordMatch){
            BestWordMatch = wordMatch;
            for(int i=0;i<3;++i) bestKey[i]=key[i];
        }

    }

    decrypt(cipherText,out,bestKey);

    printf("result: (matched words:%d) \n\n%s\n\n",BestWordMatch,out);
    printf("key was: %s",bestKey);

    printf("first:%c,%d", *out);
*/
    decrypt(cipherText,out,"god");
    out[0] = out[0]^'g';  //for some reason first one is missed
    printf("\n\n\n%s",out);

    char* finger = out;
    int sum = 0;
    while(*finger){
        sum+=*finger;
        finger++;
    }

    printf("\n\nsum is%d\n\n",sum);


	return 0;
}
