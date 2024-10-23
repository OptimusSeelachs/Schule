#pragma once

#include "Widerstand.h"

class Parallel : public Widerstand
{
    public:
        Parallel(){};
        Parallel(Widerstand* r1, Widerstand* r2);
};