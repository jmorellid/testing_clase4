# language: es

Característica: Feaures que deben cumplir las listas según los requisitos establecidos por el cliente
	En una lista vacía hay cero elementos
	Al agregar un elemento a una lista vacía hay un elemento
	En una lista vacía no hay ninguna clave
	Se puede recuperar un elemento de una lista no vacía a partir de su clave
	Cuando se agrega un elemento a una lista no vacía con calve existente la lista actualiza el valor correspondiente
	Cuando se agrega un elemento a una lista vacía la lista de calves está ordenada


Escenario: Comportamiento esperado lista vacia
	Dado que tengo una lista
	Cuando esta vacía
	Entonces la lista no debe tener claves ni elementos


Escenario: Cantidad de elementos y claves consistentes respecto a la cantidad de pares agregados
	Dado que tengo una lista
	Cuando agrego los pares
		| clave       | elemento  |
		| abeja       |  timba    |
		| campo       |  pasto    |
		| toldo       |  verde    |

	Entonces la lista debe tener "3" elementos
	Y la lista debe tener "3" claves


Escenario: Actualización de elementos cuya clave ya existía 
	Dado que tengo una lista
	Cuando agrego los pares
		| clave       | elemento  |
		| abeja       |  timba    |
		| campo       |  pasto    |
		| campo       |  verde    |

	Entonces el elemento asociado a "campo" debe ser "verde"


Escenario: Recuperar un elemento de una lista no vacía a partir de su clave
	Dado que tengo una lista
	Cuando agrego los pares
		| clave       | elemento  |
		| abeja       |  timba    |
		| campo       |  pasto    |
		| campo       |  verde    |
		| comida      | risotto   |
	Entonces el elemento asociado a "campo" debe ser "verde"
		Y el elemento asociado a "abeja" debe ser "timba"
		Y el elemento asociado a "comida" debe ser "risotto"


Escenario: Cuando se agrega un elemento a una lista vacía la lista de calves está ordenada
	Dado que tengo una lista
	Cuando agrego los pares
		| clave       | elemento  |
		| zebra       |  ensalada |
		| abeja       |  timba    |
		| campo       |  pasto    |
		| campo       |  verde    |
		| comida      | risotto   |
	Entonces la lista de claves estará ordenada según la siguiente lista
	    | clave       |
		| abeja       |
		| campo       |
		| comida      |
		| zebra       |


Escenario: Retornar mensaje de error cuando se desea eliminar un elemento inexistente
	Dado que tengo una lista
	Cuando agrego los pares
		| clave       | elemento  |
		| abeja       |  timba    |
		| campo       |  pasto    |
		| campo       |  verde    |
		| comida      | risotto   |
		Y se desea eliminar el elemento "auricular"
	Entonces debe arrojar el error ValueError con el mensaje "No encontró la clave!"
