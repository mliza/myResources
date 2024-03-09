/*
    Date:   10/26/2023
    Author: Martin E. Liza
    File:   main.cpp
    Def:

    Author		Date		Revision
    ----------------------------------------------------
    Martin E. Liza	10/26/2023	Initial version.
*/

#include "navigation.hpp"

int main()
{
    Navigation nav;
    std::vector<double> posECEF = {5344444.0, 2112.0, 122.0}; 
    std::vector<double> posLLA= {0.0, 0.0, 0.0}; 
    nav.ECEF2LLA(posECEF, posLLA);

    return 0;
};
