#pragma once

#include "Widerstand.h"

class Reihe : public Widerstand
{
    public:
        Reihe(){};
        Reihe(Widerstand* r1, Widerstand* r2);
};