/*
    Date:   10/26/2023
    Author: Martin E. Liza
    File:   navigation.cpp
    Def:

    Author		Date		Revision
    ----------------------------------------------------
    Martin E. Liza	10/26/2023	Initial version.
*/

#pragma once
#include <iostream>
#include <cmath>
#include <vector>


class Navigation
{
    public: 
        Navigation( ); //Constructor 
        void ECEF2LLA(std::vector<double> vectPosECEF, 
                      std::vector<double> &vecPosLLA);

    private:
        const double mMinorEarthRadius = 6356752.3;
        const double mMajorEarthRadius = 6378137.0;


};
