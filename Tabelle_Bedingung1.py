#Dieses Programm soll überprüfen, welche der bekannten Planeten weit genug von ihrem Mutterstern entfernt sind,
#um eine Oberflächentemperatur von weniger als 273,15K zu haben
import csv
import math

#Erstelle Hilfslisten, in denen die jeweiligen Parameter der Planeten gespeichert werden
R_stern = []   #Radius des Sterns
T_stern = []   #Temperatur des Sterns
a = []         #mittlerer Abstand zwischen Stern und Planet
a_calc = []    #berechneter Mindestabstand
vergleich = [] #Hilfsliste um a und a_calc zu vergleichen

#die Daten werden aus der csv-Datei in die entsprechenden Listen übertragen
with open('Exoplaneten_mit_Daten_zu_Sternradius_und_-temperatur.csv') as tabelle_csv:
    tabelle = csv.reader(tabelle_csv, delimiter=',')
    
    zeilennummer = 0
    
    for row in tabelle:
        if zeilennummer == 0:
            zeilennummer += 1
        else: 
            R_stern.append(float(row[47]))
            T_stern.append(float(row[43]))
            a.append(float(row[15])*1.496*10**11)
            zeilennummer += 1

#der benötigte Abstand für jedes System wird berechnet und in einer weitere Liste gespeichert
for i in range(0,len(R_stern)):
    a_calc.append(math.sqrt(1-0.9)*(T_stern[i]/273.15)**2*R_stern[i]*696340000/2)
     
print(len(a))
print(len(a_calc)) 

#a und a_calc werden verglichen
for i in range(0,len(a)):
    if a[i] > a_calc[i]:
        vergleich.append(1)
    else:
        vergleich.append(0)
        
print(vergleich)

#Hilfsliste um eine neues csv-Datei zu erstellen
neue_tabelle = []

#Alle Zeilen der alten Tabelle, in denen der mittlere Abstand groß genug ist, werden in eine neue Tabelle übertragen
with open('Exoplaneten_mit_Daten_zu_Sternradius_und_-temperatur.csv') as tabelle_csv:
    tabelle = csv.reader(tabelle_csv, delimiter=',')
    
    zeilennummer = 0
    
    for row in tabelle:
        if zeilennummer == 0:
            neue_tabelle.append(row)
        else:
            if vergleich[zeilennummer-1]==1:
                neue_tabelle.append(row)
        zeilennummer += 1
        
with open('Albedo_0,9.csv','w') as tabelle2_csv:
    tabelle2 = csv.writer(tabelle2_csv, delimiter=',')
    
    for i in range(0,len(neue_tabelle)):
        tabelle2.writerow(neue_tabelle[i])
        
print(len(neue_tabelle))
    
