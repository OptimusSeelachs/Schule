#include "Parallel.h"

Parallel::Parallel(Widerstand* r1, Widerstand* r2)
    : Widerstand((r1->getValue()*r2->getValue())/(r1->getValue()+r2->getValue()))
{
/*
    float val1 = r1->getValue();
    float val2 = r2->getValue();

    setValue((val1*val2)/(val1+val2));
*/
}