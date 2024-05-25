import numpy as np

def forward_euler(f, t_s, x , h_s, amod):
    """
        Inputs 
            f: A function representing the RHS of the DEQ (dx/dt = f(t,x))
            t_s: A vector of points in time at which numerical solutions 
                will be approximated
            x:  The numerical approximated solution data to the DEQ, f
            h_s: The Step size in seconds

        Returns:
            t_s: A vector of points in time at which numerical solutions 
                will be approximated
            x:  The numerical approximated solution data to the DEQ, f
    """
    # Forward Euler numerical integration
    for i in range(1, len(t_s)):
        x[:,i] = x[:,i-1] + h_s * f(t_s[i-1], x[:,i-1], amod)

    return t_s, x
        
