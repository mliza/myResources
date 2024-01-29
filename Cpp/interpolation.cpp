#include <iostream>
#include <iomanip>

/*
   y = y0 + (x - x0) * (y1 - y0) / (x1 - x0)
*/

// Explicit
double linear_interp1(double x0, double x1, double y0, double y1, double x)
{
    double dx = (x - x0) / (x1 - x0);
    return y0 * (1 - dx) + y1 * dx;
}

// Implicit
double linear_interp2(double x0, double x1, double y0, double y1, double x)
{
    double m = (y1 - y0) / (x1 - x0);
    return y0 + m * (x - x0);
}


int main()
{

    // Parameters
    uint32_t vect_size = 9000 ;
    double x0 = 0.0;
    double x1 = 10.0;
    double y0_1 = 378989.0;
    double y0_2 = 378989.0; 
    double y1 = 378989.0;
    double time_vect[vect_size] = {0.0};
    double y0_inter1_vect[vect_size] = {0.0}; 
    double y0_inter2_vect[vect_size] = {0.0}; 
    double eps = 0.001;
    int max_err_indx = -1;
    double val_interp1 = 0.0;
    double val_interp2 = 0.0;
    
    // Initialize needed variables
    time_vect[0] = eps;

    for (uint32_t i = 0; i < vect_size; ++i)
    {
        time_vect[i] = time_vect[0] + i * eps;
        y0_inter1_vect[i] = linear_interp1(x0, x1, y0_1, y1, time_vect[i]);
        y0_inter2_vect[i] = linear_interp2(x0, x1, y0_2, y1, time_vect[i]);

        // Move initial variables to next time steps
        y0_1 = y0_inter1_vect[i]; 
        y0_2 = y0_inter2_vect[i]; 
        x0 = time_vect[i];

        if (y0_1 != y0_2)
        {
            int max_err_indx = i;
            int time_max = x0;
            val_interp1 = y0_1; 
            val_interp2 = y0_2; 
        }

    }
    std::cout << std::fixed << std::setprecision(15) << "linear_interp1, linear_interp2, diff: " << val_interp1 << ", " << val_interp2<< ", " <<  val_interp1 - val_interp2 << std::endl;

    return 0;
}
