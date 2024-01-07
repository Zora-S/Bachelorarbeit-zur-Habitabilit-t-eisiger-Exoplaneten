import math
from scipy.constants import G
from scipy.constants import Stefan_Boltzmann as sigma

def layers(R_p, dW, R_stern, T_stern, M_stern, A_B, e, a_p, k_2, Q):
    x_u = R_p
    x_o = R_p + dW

    #Naturkonstanten
    rho_w = 997 #mittlere Dichte von Wasser in kg/m^3
    rho_e = 910 #mittlere Dichte von Eis in kg/m^3
    l_W = 0.5562 #Wärmeleitfähigkeit des Wassers
    l_E = 2.33 #Wärmeleitfähigkeit des Eises

    #Berechenete Eigenschaften des Planeten
    A = 4*math.pi*x_u**2 #Oberfläche des festen Kerns in Quadratmetern
    
    #Berechnung von Leistung und Temperatur
    mean_motion = math.sqrt(G*M_stern/(a_p**3))
    E_tidal = 21/2*k_2/Q*G*M_stern**2*R_p**5*mean_motion*e**2/a_p**6
    h_s = sigma*R_stern**2*T_stern**4/a_p**2
    E_stern = h_s*math.pi*R_p**2*(1-A_B)
    T_o = ((E_stern+E_tidal)/(4*math.pi*sigma*R_p**2))**(1/4) #Berechnung der oberen Temperatur
    T_m = 273.15 #mittlere Temperatur wird auf den Gefrierpunkt gesetzt
    #print(((E_stern+E_tidal)/(4*math.pi*sigma*R_p**2))**(1/4))

    #Berechnung der Schichtdicke
    x_m = x_o - (l_E*A) * (T_m-T_o)/(E_tidal)
    
    T_u = T_m + E_tidal/(l_W*A) * (x_m-x_u)

    if x_m-x_u < 0:
        x_o = x_u+dW
        x_m = x_u
    elif x_o-x_m < 0:
        x_m = x_u+dW
        x_o = x_m

    return x_o-x_u, x_o-x_m, x_m-x_u