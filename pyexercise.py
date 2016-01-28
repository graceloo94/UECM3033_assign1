import sympy as sy
import numpy as np

def fun_1( your_id ):
    ans = hex(your_id)
    return ans

def my_integral():
    x = sy.Symbol('x')
    ans = sy.integrate(sy.ln(x)**2, (x,0,1))
    return ans

def my_solution():
    A = np.array(  [[1,1,1,2,1,2,3,1,2,1],
                    [3,4,2,5,2,2,3,2,3,2],
                    [5,6,3,8,2,2,5,5,4,4],
                    [7,8,4,11,3,2,6,1,5,5],
                    [9,10,5,14,4,3,8,2,8,3],
                    [11,12,6,15,5,3,7,5,2,4],
                    [13,14,7,14,5,3,2,3,1,2],
                    [15,16,8,11,1,5,1,4,3,1],
                    [17,18,9,10,1,5,1,2,5,2],
                    [19,20,10,8,1,5,3,1,6,2]] )
    b = np.array([176,286,462,502,624,606,456,452,486,518])
    x = np.linalg.solve(A,b) # Solve Ax = b
    return x


if __name__ == '__main__':
    your_id = 1205887
    print('Hexadecimal representation of %d is %s'%( your_id, fun_1( your_id) ))
    print('Integral = ', my_integral())
    print('Solution = ', my_solution())
