#include <assert.h>
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include "hashMap.h"
#include "dictionary.h"

/*
 the getWord function takes a FILE pointer and returns you a string which was
 the next word in the in the file. words are defined (by this function) to be
 characters or numbers seperated by periods, spaces, or newlines.
 
 when there are no more words in the input file this function will return NULL.
 
 this function will malloc some memory for the char* it returns. it is your job
 to free this memory when you no longer need it.
 */
char* getWord(FILE *file);


/*
 Load the contents of file into hashmap ht
 */
void loadDictionary(FILE* file, struct hashMap* ht);



int isWord(hashMap* ht,char* word){
    return containsKey(ht,word);
}

hashMap *createDict() {
  struct hashMap* hashTable;
  int tableSize = 1000;
  hashTable = createMap(tableSize);
  
  FILE* dictionary;
  
  loadDictionary(dictionary,hashTable);
  
  return hashTable;
}

void loadDictionary(FILE* file, struct hashMap* ht)
{
    file = fopen("dictionary.txt","r");

    char* nextWord;
    while(( nextWord = getWord( file ))){
        insertMap(ht, nextWord, 0);
    }
}

char* getWord(FILE *file)
{
	int length = 0;
	int maxLength = 16;
	char character;
    
	char* word = (char*)malloc(sizeof(char) * maxLength);
	assert(word != NULL);
    
	while( (character = fgetc(file)) != EOF)
	{
		if((length+1) > maxLength)
		{
			maxLength *= 2;
			word = (char*)realloc(word, maxLength);
		}
		if((character >= '0' && character <= '9') || /*is a number*/
		   (character >= 'A' && character <= 'Z') || /*or an uppercase letter*/
		   (character >= 'a' && character <= 'z') || /*or a lowercase letter*/
		   (character == 39)) /*or is an apostrophy*/
		{
			word[length] = character;
			length++;
		}
		else if(length > 0)
			break;
	}
    
	if(length == 0)
	{
		free(word);
		return NULL;
	}
	word[length] = '\0';
	return word;
}
