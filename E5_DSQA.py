#  Cálculo del salario mensual con descuentos
# Ejercicio 5
# Diego Quisque

# Creacion de Datos
salario_diario = 500
dias_trabajados = 22

# Cálculo del salario bruto
salario_bruto = salario_diario * dias_trabajados

# Creacion del Descuentos
descuento_seguro = salario_bruto * 0.10
descuento_ahorro = salario_bruto * 0.05

# Calculo del Salario neto
salario_neto = salario_bruto - (descuento_seguro + descuento_ahorro)

# Muestro el resultado de lo anteriormente calculado
print("Salario bruto:", salario_bruto)
print("Descuento por seguro:", descuento_seguro)
print("Descuento por ahorro:", descuento_ahorro)
print("Salario neto:", salario_neto)