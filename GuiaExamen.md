## Problema 1.
Dada una matriz cuadrada N x N calcular la diferencia absoluta de las sumas a lo largo de las diagonales.
Entrada:
```
3
11 2 4   
4 5 6   
10 8 -12   
```
Salida

```
15
```
## Problema 2.
El encargado de una libreria quiere hacer un programa que calcule el costo de la multa que debe pagar una persona si regresa el libro despues de la fecha de entrega.
* Si el libro es regresado el dia indicado el cargo es igual a 0
* Si el libro es regresado en el mismo mes entonces el cargo se calcula por: cargo = 15*Numero de dias tarde.
* Si el libro no es regresado el mismo mes pero es en el mismo año entonces se calcula como: Cargo = 500xNumero de meses
* Si el libro no es regresado en el mismo año entonces se calcula como 1000

### Entrada
Se deben introducir los dias de entrega en formato D M Y en la primera linea se introduce la fecha actual y en la segunda linea el dia esperado  de entrega

```
9 6 2015
6 6 2015
```

### Restricciones.

$$1 \leq D \leq 31$$
$$ 1 \leq M \leq 12 $$
1 \leq Y \leq 3000 $$

### Salida

Para la entrada sería 45
A partir de 3 dias seria 15 x 3 = 45
