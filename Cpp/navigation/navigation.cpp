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

void Navigation::ECEF2LLA(std::vector<double> vectorPosECEF, 
                          std::vector<double> &vecPosLLA)
{
    double eccentricity = sqrt( 1 - 
                    pow(mMinorEarthRadius / mMajorEarthRadius, 2) );
}

