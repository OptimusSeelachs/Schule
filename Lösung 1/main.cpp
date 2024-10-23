
#include "Widerstand.h"
#include "Reihe.h"
#include "Parallel.h"

#include <iostream>

using namespace std;

int main()
{
    float r1 = 3;
    float r2 = 4;
    float r3 = 5;
    
    Widerstand* pRges =
        new Parallel(
            new Reihe(
                new Widerstand(r1), 
                new Widerstand(r2)
            ),
            new Widerstand(r3)
        );

    cout << "Rges = " << pRges->getValue();
}
