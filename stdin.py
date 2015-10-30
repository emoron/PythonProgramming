# Numero de casos a leer de STDIN como un entero
numofCases = input()
i = 0
while i < numofCases:
    numofNumbers = input()
 
    # raw_input() acepta una entrada como: 1 2 22 232 12 as a string
    # input() puede aceptar solo una entrada
    # raw_input().strip().split(" ") genera una lista con numeros como cadenas.
    # map(int,xxxx) regresa xxxx and convierte esta lista de cadenas a enteros.
    b = map(int, raw_input().strip().split(" "))
 
    print maxProfit(b)
     
    i += 1
