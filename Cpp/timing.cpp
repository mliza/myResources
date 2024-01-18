/*
    Date:   01/08/2024
    Author: Martin E. Liza
    File:   timing.cpp
    Def:

    Author          Date        Revision
    ----------------------------------------------------
    Martin E. Liza  01/08/2024  Initial version.
*/

#include <chrono>
#include <iostream>

class Timer
{
public:
    Timer()
    {
        m_StartTimePoint = std::chrono::high_resolution_clock::now();
    }

    ~Timer()
    {
        Stop();
    }

    void Stop()
    {
        std::chrono::time_point< std::chrono::high_resolution_clock> endTimePoint = std::chrono::high_resolution_clock::now();
        double start = std::chrono::time_point_cast<std::chrono::nanoseconds>(m_StartTimePoint).time_since_epoch().count();
        double end = std::chrono::time_point_cast<std::chrono::nanoseconds>(endTimePoint).time_since_epoch().count();
        double duration_ns = end - start;
        double duration_us = duration_ns * 1/1000;
        std::cout << duration_ns << "[ns] (" << duration_us << "[us])\n";
    }

private:
    std::chrono::time_point< std::chrono::high_resolution_clock> m_StartTimePoint;
};
