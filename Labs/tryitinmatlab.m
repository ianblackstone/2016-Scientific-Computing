function f = tryitinmatlab(t,u)

M = 1477;
h = 6.77E11;

f = [u(3); u(4); -M/u(1)^2 + h^2 / u(1)^3 - 3*M*h^2 / u(1)^4 ; h/u(1)^2 ];

end

% b = 200;
% t = linspace(0,b);

% u0 = [4.7607E10,0,0,1.22];

% % Run the 113 ODE solver.
% opt = odeset('RelTol',10e-6);
% [t5,u5] = ode113(@tryitinmatlab,3*t,u0,opt);
% figure
% plot()
% title('Graph of satelite position using ODE113 solver')
% ylabel('y position')
% xlabel('x position')