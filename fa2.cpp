#include<stdio.h>
#include<string.h>
#include<stdlib.h>
#include<stdio.h>
#define noc 256

int calcState(char *pattern, int patternl, int state, int x)
{

if (state < patternl && x == pattern[state])
return state+1;
// prefix finding
int nextState, i;
for (nextState = state; nextState > 0; nextState--)
{
if(pattern[nextState-1] == x)
{
for(i = 0; i < nextState-1; i++)
{
if (pattern[i] != pattern[state-nextState+1+i])
break;
}
if (i == nextState-1)
return nextState;
}
}

return 0;
}


void constrTFrfa(char *pattern, int patternl, int TF[][noc])
{
int state, x;
for (state = 0; state <= patternl; ++state)
for (x = 0; x < noc; ++x)
TF[state][x] = calcState(pattern, patternl, state, x);
}

//display pattern in text
void search(char *pattern, char *skepText)
{
int patternl = strlen(pattern);
int skepTextl = strlen(skepText);

int TF[patternl+1][NO_OF_CHARS];

constrTFrfa(pattern,patternl, TF);

// text processing over the algo
int i, state=0;
for (i = 0; i < skepTextl; i++)
{
state = TF[state][skepText[i]];
if (state == patternl)
{
printf ("\n Pattern found at index %d", i-patternl+1);
}
}
}

// main
int main()
{
char *skepText = "cococcccoocodeplagcococo";
char *pattern = "codeplag";
search(pattern, skepText);
return 0;
}

