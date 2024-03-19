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

class Tools 
{
    public: 
        // Default constructor  
        Tools();

        // Constructor
        Tools(int n);

        // Destructor
        ~Tools();

        // Copy constructor
        Tools(const Tools& other);

        // Move constructor
        Tools(Tools&& other);

        // Copy assignment operator
        Tools& operator = (const Tools& other);

        // Move assignment operator
        Tools& operator = (Tools&& other);

        // Some other operator
        int operator() () const;

        // Setter
        void set_n(int n);

        // Getter
        int get_n() const;

        // Overload for std::cout
        friend std::ostream& operator<<(std::ostream& os, const Tools& t);

        // Static variable
        static int x;

        // Static function
        static void print_x();

    private:
        int n;
};
