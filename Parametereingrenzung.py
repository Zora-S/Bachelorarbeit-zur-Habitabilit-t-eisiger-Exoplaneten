import math
import matplotlib.pyplot as plt

#Naturkonstanten
G = 6.6743*10**(-11)
sigma = 5.6704*10**(-8)
l_W = 0.5562
l_E = 2.33
str_1 = 'Boah irgendwas ist hier falsch. Habe auch keinen Bock mehr. Verdammte Kacke'

#als konstant angenommen
T_M = 273.15

#freie Parameter 
R_stern = 0.6*6.96342*10**8 # *6.96342*10**8 weil sonnenradius in m
T_stern = 2500 #in K
M_stern = 0.6*1.898*10**27 # *1.989*10**30 weil sonnenmasse in kg
R_planet = 12*10**6 #2000km bis 12000km in metern
M_planet = 5513*4/3*math.pi*R_planet**3 #Masse des Planeten ausgerechnet über die dichte, erddichte als referenzwert 
A_B = 0.9 #0.1 bis 0.9
e = 0.9 #0.1 bis 0.9

k_2 = 1 #0.01 bis 1, 0.3 bei der erde
Q = 1 #1 bis 10**6


#zu berechnende Größen
a = math.sqrt(1-A_B)*(T_stern/273.15)**2*R_stern/2 #hier ist Bedingung 1 enthalten

def func(a, G, sigma, l_W, l_E, T_M, R_stern, T_stern, M_stern, R_planet, M_planet, A_B, e, k_2, Q):
    n = math.sqrt(G*M_stern/(a**3))
    E_tidal = 21/2*k_2/Q*G*M_stern**2*R_planet**5*n*e**2/a**6
    h_s = sigma*R_stern**2*T_stern**4/a**2
    E_stern = h_s*math.pi*R_planet**2*(1-A_B)
    T_o = (E_stern/(4*math.pi*sigma*R_planet**2))**(1/4)
    T_u = ((E_tidal)/(4*math.pi*sigma*R_planet**2))**(1/4)


    x_M = (T_u-T_M)/l_W
    x_o = (T_M-T_o)/l_E
    print(T_u)
    print(a)
    print('Wasserschicht', x_M)
    print('Eisschicht', x_o)
    return x_o, x_M

x1 = []
x2 = []
'''
for i in range(len(a)):
    res = func(a, G, sigma, l_W, l_E, T_M, R_stern, T_stern, M_stern, R_planet, M_planet, A_B, e[i], k_2, Q)
    x1.append(res[0])
    x2.append(res[1])

if T_u>273.15:
    print('yay')
else:
    print(str_1)
'''    
func(a, G, sigma, l_W, l_E, T_M, R_stern, T_stern, M_stern, R_planet, M_planet, A_B, e, k_2, Q)