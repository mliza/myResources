#include <iostream>

size_t intPow(size_t base, size_t exponent)
{
    if (exponent == 0 || base == 1)
    {
        return 1;
    }

    if (exponent == 1)
    {
        return base;
    }

    size_t map = intPow(base, exponent >> 1);

    return exponent & 1 ? base * map * map : map * map;
}

int main()
{
    std::cout << "iPow 2,5: " << intPow(2,5) << std::endl;
    std::cout << "iPow 2,4: " << intPow(2,4) << std::endl;
    return 0;
}
