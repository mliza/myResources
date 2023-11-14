/*
    Date:   10/26/2023
    Author: Martin E. Liza
    File:   navigation.cpp
    Def:

    Author		Date		Revision
    ----------------------------------------------------
    Martin E. Liza	10/26/2023	Initial version.
*/
#include "navigation.hpp"

void Navigation::ECE2LLLA(std::vector<double> vectorPosECEF, 
                          std::vector<double> &vecPosLLA);
{
    double eccentricity = sqrt( 1 - 
                    pow(mMinorEarthRadius / mMajorEarthRadius, 2) );
}

main()
{
    std::vector<double> posECEF = {5344444, 2112, 122}; 
    std::vector<double> posLLA{ }; 
    ECE2LLLA(posECEF, &posLLA);

    return 0;
};
