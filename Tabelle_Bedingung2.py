#In diesem Programm wird bestimmt welche der zuvor sortierten Planeten nah genug an ihrem Mutterstern sind,
# um die Oberflächentemperatur mittels Gezeitenheizung über 273,15K zu heben
import csv
import math

#Planetenabhängige Größen
R_stern = []   #Radius des Sterns
T_stern = []   #Temperatur des Sterns
M_stern = []   #Masse des Sterns
a = []         #mittlerer Abstand zwischen Planet und Stern
R_planet = []  #Radius des Planeten
e = []         #Exzentrizität der Bahn
T_planet = []  #Berechnete Temperatur des Planeten
n = []         #mittlere Bewegung des Sterns
E_tidal = []   #Heizleistung durch Gezeitenheizung
h_s = []       #Hilfsgröße
E_stern = []   #Heizleistung durch Strahlung
vergleich = []

#konstanten
k_2 = 0.3               #Lovesche Zahl, als Referenz wird hier der Wert der Erde verwendet
Q = 100                 #Dissipationsfaktor
G = 6.6743*10**(-11)    #Gravitationskonstante
sigma = 5.6704*10**(-8) #Stefan-Boltzmann-Konstante

#die benötigten Größen werden aus einer csv-Datei eingelesen und ins SI.System umgerechnet
with open('Albedo_0,6.csv') as tabelle_csv:
    tabelle = csv.reader(tabelle_csv, delimiter=',')
    
    zeilennummer = 0
    
    for row in tabelle:
        if zeilennummer == 0:
            zeilennummer += 1
        else: 
            R_stern.append(float(row[47])*6.96342*10**8) 
            T_stern.append(float(row[43]))
            M_stern.append(float(row[51])*1.989*10**30)
            a.append(float(row[15])*1.496*10**11)
            R_planet.append(float(row[19])*6370000)
            e.append(float((row[28])))
            zeilennummer += 1


#Berechnung der Größen
for i in range(0,len(R_stern)):
    n.append(math.sqrt(G*M_stern[i]/(a[i]**3)))
    
for i in range(0,len(R_stern)):
    E_tidal.append(21/2*k_2/Q*G*M_stern[i]**2*R_planet[i]**5*n[i]*e[i]**2/a[i]**6)
    
for i in range(0,len(R_stern)):
    h_s.append(sigma*R_stern[i]**2*T_stern[i]**4/a[i]**2)
    
for i in range(0,len(R_stern)):
    E_stern.append(h_s[i]*math.pi*R_planet[i]**2*(1-0.6))
    
for i in range(0,len(R_stern)):
    T_planet.append(((E_tidal[i])/(4*math.pi*sigma*R_planet[i]**2))**(1/4))
                   
#Test, ob die Oberflächentemperatur groß genug ist
for i in range(0,len(T_planet)):
    if T_planet[i] > 273.15:
        vergleich.append(1)
    else:
        vergleich.append(0)
        
print(vergleich)

#eine neue Tabelle mit den Planeten, die genug geheizt werden, wird erstelltneue_tabelle = []
with open('Albedo_0,9.csv') as tabelle_csv:
    tabelle = csv.reader(tabelle_csv, delimiter=',')
    
    zeilennummer = 0
    
    for row in tabelle:
        if zeilennummer == 0:
            neue_tabelle.append(row)
        else:
            if vergleich[zeilennummer-1]==1:
                neue_tabelle.append(row)
        zeilennummer += 1
        
with open('Ergebnis 0,9.csv','w') as tabelle2_csv:
    tabelle2 = csv.writer(tabelle2_csv, delimiter=',')
    
    for i in range(0,len(neue_tabelle)):
        tabelle2.writerow(neue_tabelle[i])
        
print(len(neue_tabelle))
    


    
