#include "Reihe.h"

Reihe::Reihe(Widerstand* r1, Widerstand* r2) 
    : Widerstand(r1->getValue() + r2->getValue())
{
}