function out = DiffusionEquation1D() 

%Constants + Boundary Conditions 
L = 0.1; %wall thickness, [m]
T0 = 0; %Initial wall temperature [C] (B.C) 
Tsur1 = 40; %surface temperature at surface 1 [C]
Tsur2 = 20; %surface temperature at surface 2 [C]
alpha = 0.0001; %thermal diffusivity [m^2/s]

%Nodes 
n = 10; %number of nodes
dx = L/n; %node thickness [m] 
tFinal = 60; %simulation time [s] 
dt = 0.1; %fixed time step [s]

%Set up parameters
x = (dx/2):dx:(L-dx/2); %Node distances [m]
T = ones(n,1)*T0; %initial nodal temperature vector [C] 
dTdt = zeros(n,1); %initialize derivative of temperature for each node 
t = 0:dt:tFinal; %Simulation Time [s]

for j = 1:length(t) %step through time 
 	for i = 2:n-1 %step through nodes  
		dTdt(i) = alpha*(-(T(i)-T(i-1))/dx^2 + (T(i+1)-T(i))/dx^2); 
    end
 	dTdt(1) = alpha*(-((T(1)-Tsur1))/dx^2 + (T(2)-T(1))/dx^2); 
    dTdt(n) = alpha*(-(T(n)-T(n-1))/dx^2 + (Tsur2-T(n))/dx^2);
    T = T + dTdt * dt; 
	figure(1) 
	plot(x,T, 'Linewidth',3) 
	axis([0 L 0 50])
	xlabel('Distance [m]')
	ylabel('Temperature [\circ C]')
%	pause(0.6) 
	grid on
end	
end
