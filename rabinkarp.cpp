#include <iostream>
#include <stdio.h>
#include <string.h>
#include <stdlib.h>
using namespace std;
#define d 256
// find substring
void search(char *pattern, char *skepText, int q)
{
    int patternl = strlen(pattern);
    int skepTextl = strlen(skepText);
    int i, j;
    int p = 0;
    int t = 0;
    int h = 1;
    for (i = 0; i < patternl - 1; i++)
        h = (h * d) % q;
    for (i = 0; i < patternl; i++)
    {
        p = (d *p + pattern[i]) % q;
        t = (d * t + skepText[i]) % q;
    }
    for (i = 0; i <= skepTextl - patternl; i++)
    {
        if (p == t)
        {
            for (j = 0; j < patternl; j++)
            {
                if (skepText[i + j] != pattern[j])
                    break;
            }
            if (j == patternl)
            {
                cout<<"Pattern found at index: "<<i<<endl;
            }
        }
        if (i < skepTextl - patternl)
        {
            t = (d * (t - skepText[i] * h) + skepText[i + patternl]) % q;
            if (t < 0)
              t = (t + q);
        }
    }
}


int main()
{
    char *skepText = "lacodeplagfalalolaolaolalocodeplagwgerhfbfvgsrg";
    char *pattern = "codeplag";
    int q = 101;
    search(pattern, skepText, q);
    return 0;
}
