#rotational


from sympy import * 

omega2 = omega1 + alpha * t
theta = omega1 * t + .5 * alpha * t**2
theta = omega * t
omega2**2 = omega1**2 + 2 * alpha * theta
omega = diff(theta,t)
alpha = diff(omega,t)
omega = integrate(alpha,t)
theta = integrate(omega,t)