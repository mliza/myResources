/*
    Date:   10/26/2023
    Author: Martin E. Liza
    File:   navigation.cpp
    Def:

    Author		Date		Revision
    ----------------------------------------------------
    Martin E. Liza	10/26/2023	Initial version.
*/
#include "tools.hpp"
#include <utility>

// Default Constructor
Tools::Tools()
{

}

// Constructor
Tools::Tools(int n) : n(n)
{

}

// Destructor
Tools::~Tools()
{

}

// Copy constructor
Tools::Tools(const Tools& other)
{
    *this = other;
}

// Move constructor
Tools::Tools(Tools&& other)
{

}

// Copy assignment operator
Tools& Tools::operator=(const Tools& other)
{
    this->x = other.x;
    return *this;
}

// Mover assignment operator
Tools& Tools::operator=(Tools&& other)
{
    this->x = std::move(other.x); 
    return *this;
}

// Some other operator
void Tools::set_n(int n)
{
    this->n = n;
}

// Getter
int Tools::get_n() const
{
    return this->n;
}

// Overload for std::cout
std::ostream& operator<<(std::ostream& os, const Tools& t) {
    return os << t.n;
}

// Static variable
int Tools::x = 5;

// Static function
void Tools::print_x()
{
    std::cout << "Tools::x = " << Tools::x << '\n';
}
