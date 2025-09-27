"""Calculadora muy sencilla en español.

Soporta: sumar, restar, multiplicar, dividir y potencia.
Ejecuta el programa y sigue las instrucciones en pantalla.
"""

def pedir_numero(prompt):
	while True:
		val = input(prompt)
		try:
			return float(val)
		except ValueError:
			print("Entrada no válida. Por favor, introduce un número.")


def mostrar_menu():
	print("\n--- Calculadora sencilla ---")
	print("Operaciones disponibles:")
	print("  1) sumar (+)")
	print("  2) restar (-)")
	print("  3) multiplicar (*)")
	print("  4) dividir (/)")
	print("  5) potencia (a^b)")
	print("  6) salir")


def main():
	while True:
		mostrar_menu()
		opcion = input("Elige una operación (1-6) o escribe el símbolo (+ - * / ^) : ").strip()

		if opcion in ("6", "salir", "exit"):
			print("Adiós.")
			break

		# Map symbols to choices
		simbolos = {"+": "1", "-": "2", "*": "3", "/": "4", "^": "5", "**": "5"}
		if opcion in simbolos:
			opcion = simbolos[opcion]

		if opcion not in ("1", "2", "3", "4", "5"):
			print("Opción no válida. Intenta de nuevo.")
			continue

		a = pedir_numero("Introduce el primer número: ")
		b = pedir_numero("Introduce el segundo número: ")

		if opcion == "1":
			resultado = a + b
			op_text = "+"
		elif opcion == "2":
			resultado = a - b
			op_text = "-"
		elif opcion == "3":
			resultado = a * b
			op_text = "*"
		elif opcion == "4":
			op_text = "/"
			if b == 0:
				print("Error: división por cero no permitida.")
				continue
			resultado = a / b
		elif opcion == "5":
			resultado = a ** b
			op_text = "^"

		print(f"Resultado: {a} {op_text} {b} = {resultado}")


if __name__ == "__main__":
	main()
