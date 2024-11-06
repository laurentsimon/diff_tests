

def numerial_derivative1(f, x, epsilon=1e-5):
    delta_f = f(x+epsilon) - f(x)
    return delta_f / epsilon

def numerial_derivative2(f, x, epsilon=1e-5):
    f1_xpe = numerial_derivative1(f, x+epsilon, epsilon)
    f1_x = numerial_derivative1(f, x, epsilon)
    return (f1_xpe - f1_x) / epsilon

x_points = [1, 10, 50, 75, 100]

for x in x_points:
    f = lambda x:x**10
    f_1 = lambda x:10*(x**9)
    f_2 = lambda x:90*(x**8)
    
    v_1 = numerial_derivative1(f, x)
    v_2 = numerial_derivative2(f, x)

    print()
    print(f_1(x), v_1)
    print(f_2(x), v_2)
    #print(f2_derivative(x), f_1**2)
