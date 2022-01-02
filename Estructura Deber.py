
class Ejercicios:
    def EjercicioTipos_de_datos_y_acciones_elementales_1(self):
        print(type("Hola Mundo"))
        print(type("Verdadero"))
        print(type(""))
        print(type("1"))
        print(type("c"))
        print(type("256"))
        print(type("8>19"))

    def EjercicioTipos_de_datos_y_acciones_elementales_2(self):
        resultado = (5 + 3 * 2) + 9 > 3 * 5 * 14 % 3
        print(resultado)
        print(type(resultado))
        resultado = 2 * (4 - 10 + 8) / 2 * 36 * (1 / 2)
        print(resultado)
        print(type(resultado))
        resultado = 260 / 12 + 54 % 3 - 85 % 7
        print(resultado)
        print(type(resultado))
        resultado = (48 < 2 * 3) or (2 * 7 < 12)
        print(resultado)
        print(type(resultado))
        resultado = ((8 > 2) or (932 < 23)) and 4 == 2
        print(resultado)
        print(type(resultado))

    def EjercicioTipos_de_datos_y_acciones_elementales_4(self):
        #Dados dos (2) números calcule la suma, resta, multiplicación, división y módulo.
        x = int(input("ingrese el primer numero: "))
        y = int(input("ingrese el segundo numero: "))

        suma = x + y
        resta = x - y
        multiplicacion = x * y
        division = x / y
        modulo = x % y
        print("La suma da como resultado {}, la resta da como resultado {}, la multiplicación da como resultado {}, la división como resultado {} y por ultimo el módulo da como resultado {}.".format(suma, resta, multiplicacion, division,
                                                                                                           modulo))

    def EjercicioTipos_de_datos_y_acciones_elementales_5(self):
        #Dados tres (3) números, Hacer una aplicación que calcule la resolvente.
        a = int(input("ingrese el primer numero: "))
        b = int(input("ingrese el segundo numero: "))
        c = int(input("ingrese el tercer numero: "))

        resolvente1 = (-b + (((b ** 2) - (4 * a * c)) ** (0.5))) / (2 * a)
        resolvente2 = (-b - (((b ** 2) - (4 * a * c)) ** (0.5))) / (2 * a)

        print("Da como resultado :{} y {}".format(resolvente1, resolvente2))

    def EjercicioTipos_de_datos_y_acciones_elementales_6(self):
        #Dados dos (2) lados de un triángulo en cm, calcular la hipotenusa del mismo
        CO = int(input("Ingrese el primer cateto en cm: "))
        CA = int(input("Ingrese el segundo cateto en cm: "))

        hipotenusa = (((CO ** 2) + (CA ** 2)) ** (0.5))

        print("Su hipotenusa es: ", hipotenusa)

    def EjercicioTipos_de_datos_y_acciones_elementales_7(self):
        #Dado un (1) número, imprimir 0 si es par y 1 si es impar.
        x = int(input("Ingrese un número: "))
        resultado = x % 2

        if resultado == 0:
            print("0")
        else:
            print("1")

    def EjercicioTipos_de_datos_y_acciones_elementales_9(self):
        #Dado un (1) número binario de cuatro (4) dígitos imprimir su bit da paridad. El bit de paridad es 1 si el número de bits 1 es impar y 0 en caso contrario.
        numero = input("Ingrese su numero binario de 4 dígitos: ")
        digito = int(numero[0]) + int(numero[1]) + int(numero[2]) + int(numero[3])

        bit_de_paridad = digito % 2
        if  bit_de_paridad == 0:
            numero = numero + " bit de paridad 0"
        else:
            numero = numero + " bit de paridad 1"
        print( numero)


    def EjercicioTipos_de_datos_y_acciones_elementales_10(self):
        #Dado un (1) número binario de cuatro (4) dígitos imprimir su valor
        x = input("Ingrese su numero binario de cuatro dígitos: ")
        print(x)
        y = ((2 * (int(x[0]))) ** 3) + ((2 * (int(x[1]))) ** 2) + ((2 * (int(x[2]))) ** 1) + ((2 * (int(x[3]))) ** 0)
        print("Su valor es", y)

    def EjercicioTipos_de_datos_y_acciones_elementales_11(self):
        #Dado un (1) número de cuatro (4) dígitos imprimirlo por separado en unidades,
        #decenas, centenas y unidades de mil.
        numero = input("Ingrese su numero binario de cuatro dígitos: ")
        print("Unidades: ", (numero[3]))
        print("Decenas: ", (numero[2]))
        print("Centenas: ", (numero[1]))
        print("Unidades de mil: ", (numero[0]))

    def EjercicioEstructuras_De_Control_de_Flujo_de_Datos_1(self):
        #Todos los años que se dividen exactamente entre 400, o que son divisibles
        #exactamente entre 4 y no son divisibles exactamente entre 100 son años  bisiestos. Usando estas premisas crea un algoritmo que lea una fecha como un número
        #entero con el formato ddmmaaaa, y luego extraiga el año de la fecha indicando si
        #el mismo es un año bisiesto o no.
        x = int(input("Ingrese su fecha en (ddmmaaaa): "))
        y = str(x)
        z = int(y[4] + y[5] + y[6] + y[7])
        AB = [(z % 400), (z % 4), (z % 100)]

        res = False
        if AB[1] == 0 and not (AB[2] == 0):
            res = True

        if AB[0] == 0 or res:
            print("Es un año bisiesto")
        else:
            print("No es un año bisiesto")

    def EjercicioEstructuras_De_Control_de_Flujo_de_Datos_2(self):
        #Dado un número entero cuya cantidad de dígitos es igual a 5, determine si es capicúa.
        #Nota: un número capicúa es aquel que se lee igual hacia adelante que hacia atrás
        x = int(input("Ingrese un número de 5 dígitos: "))
        y = str(x)
        if y[0] == y[4] and y[1] == y[3]:
            print("Es un numero capicúa.")
        else:
            print("No es un numero capicúa")

    def EjercicioEstructuras_De_Control_de_Flujo_de_Datos_3(self):
        #Cree un algoritmo que tome por entrada las horas y minutos de un día y dé como
        #resultado su equivalente en segundos.
        horas = int(input("Ingrese las horas: "))
        minutos = int(input("Ingrese los minutos: "))
        print("Su resultado es: ", ((horas * 3600) + (minutos * 60)),"segundos")

    def EjercicioEstructuras_De_Control_de_Flujo_de_Datos_4(self):
        #Para un valor entero positivo que representa una cantidad en segundos, indicar su equivalente en minutos, horas y días.
        x = int(input("Ingrese su valor en (segundos): "))
        while x <= 0:
            x = int(input("Es necesario que ingrese un valor positivo en (segundos): "))

        y = [(x / 60), (x / 3600), (x / 86400)]

        print("La equivalente en minutos es {}, en horas {} y en días {}.".format(y[0], y[1], y[2]))

    def EjercicioEstructuras_De_Control_de_Flujo_de_Datos_5(self):
        #Dados tres números enteros positivos A, B y C, determine ¿cuál de ellos es elmayor? y ¿cuál es el segundo mayor?
        n = [0] * 3
        Posicion = ["primer", "segundo", "tercer"]
        c = 0
        while c <= 2:
            n[c] = int(input("Ingrese su " + Posicion[c] + " número: "))
            c = c + 1
        if n[0] > n[1] and n[0] > n[2]:
            p = n[0]
            if n[1] > n[2]:
                s = n[1]
            else:
                s = n[2]
        else:
            if n[1] > n[0] and n[1] > n[2]:
                p = n[1]
                if n[0] > n[2]:
                    s = n[0]
                else:
                    s = n[2]
            else:
                p = n[2]
                if n[0] > n[1]:
                    s = n[0]
                else:
                    s = n[1]
        print("El valor mayor es {} y el segundo valor mayor es {}.".format(p, s))

    def EjercicioEstructuras_De_Control_de_Flujo_de_Datos_6(self):
        #En un estacionamiento el monto a pagar se calcula multiplicando el número de horas que permaneció el automóvil dentro del estacionamiento por Bs. 4 y se
        #incrementa esta cantidad en Bs. 2,50 por cada media hora adicional. Ahora se desea que usted elabore un algoritmo que a partir de la hora de entrada
        #y la hora de salida de un vehículo (las mismas corresponden a un mismo día) calcule el monto a pagar por el dueño del vehículo.
        #La entrada vendrá dada por dos enteros positivos el primero representa las horas y el segundo los minutos, además por último se debe leer un carácter (A o P) que
        #indica si la hora es AM o PM.
        t_dos = [0] * 2
        t_uno = [0, 0, "", 0, 0, ""]
        PBs = ["La hora de entrada", "Los minutos excedentes de entrada", 2, "la hora de salida", "Los minutos excedentes de salida", 5]
        c = 0
        for i in PBs:
            if (c != 2 or c != 5):
                if (i != 2 and i != 5):
                    t_uno[c] = int(input("Ingrese {}: ".format(i)))
                c += 1
            if c == 2 or c == 5:
                hi = input("La hora que ingresó es am o pm? ")
                t_uno[(PBs[c])] = hi

        t_dos[0] = (t_uno[0] * 3600) + (t_uno[1] * 60)
        t_dos[1] = (t_uno[3] * 3600) + (t_uno[4] * 60)

        if t_uno[2] == t_uno[5]:
            Hp = t_dos[1] - t_dos[0]
        else:
            Hp = (43200 - t_dos[0]) + t_dos[1]

        t_dos[0] = (Hp - (Hp % 3600)) / 3600
        t_dos[1] = (Hp % 3600) / 60
        print(t_dos)
        Monto_a_pagar = t_dos[0] * 4

        if t_dos[1] >= 30:
            Monto_a_pagar = Monto_a_pagar + 2.50
        print("El dueño del vehículo pagará Bs. ", Monto_a_pagar)

    def EjercicioEstructuras_De_Control_de_Flujo_de_Datos_7(self):
#El IMC resulta de la división de la masa del individuo (en kilogramos) entre el
# cuadrado de la estatura (en metros). El índice de masa corporal es un indicador
# del peso de una persona en relación con su altura.
# Clasificación del IMC de acuerdo con la OMS de la ONU:
# a. Menor a 16: Criterio de ingreso.
# b. 16 a 16.9: infra peso.
# c. 17 a 18.4: bajo peso.
# d. 18.5 a 24.9: peso normal.
# e. 25 a 29.9: sobrepeso.
# f. 30 a 34.9: obesidad pre-mórbida.
# g. 40 a 45: obesidad mórbida.
# h. Mayor a 45: obesidad híper-mórbida.
# Dado el peso de una persona en libras (1 libra = 0,453592 Kg) y su estatura en
# centímetros, calcule su IMC e indique como salida el peso en kilogramos, el valor
# de IMC de la persona y la categoría en la cual fue clasificado.

        Clasificacion = ["no cumple con el Criterio de ingreso", "tiene infra peso", "tiene bajo peso", "tiene peso normal",
              "tiene sobrepeso", "tiene obesidad pre-mórbida", "tiene obesidad mórbida", "tiene obesidad híper-mórbida"]
        Mi = int(input("Ingrese su peso en libras: "))
        estatura = float(input("Ingrese su estatura en centímetros: "))

        IMC = (Mi * 0.453592) / ((estatura * 0.01) ** 2)

        if IMC > 45:
            i = Clasificacion[7]
        elif IMC > 40:
            i = Clasificacion[6]
        elif IMC > 30:
            i = Clasificacion[5]
        elif IMC > 25:
            i = Clasificacion[4]
        elif IMC > 18.5:
            i = Clasificacion[3]
        elif IMC > 17:
            i = Clasificacion[2]
        elif IMC > 16:
            i = Clasificacion[1]
        else:
            i = Clasificacion[0]

        print(
            "Su peso en kilogramos es {} y por lo consiguiente su IMC es de {} que quiere decir que {}.".format((Mi * 0.453592), IMC,
                                                                                                  i))

    def EjercicioEstructuras_De_Control_de_Flujo_de_Datos_8(self):
        #Escriba un algoritmo que reciba una fecha (día y mes) correspondiente al año
# 2014 e imprima por pantalla el número de días que han pasado desde el 1 de
# Enero de 2014 hasta la fecha dada.
        m = {"ENERO": 31, "FEBRERO": 59, "MARZO": 90, "ABRIL": 120, "MAYO": 151, "JUNIO": 181, "JULIO": 212, "AGOSTO": 243, "SEPTIEMBRE": 273, "OCTUBRE": 304, "NOVIEMBRE": 334, "DICIEMBRE": 365}
        fd = int(input("Ingrese el día: "))
        fm = input("Ingrese el mes: ").upper()
        for i in m:
            if i == fm:
                print("Han pasado {} días.".format(((m[i]) + fd)))

    def EjercicioEstructuras_De_Control_de_Flujo_de_Datos_9(self):
        #Solicitar un número entre el 1 y el 12 e imprimir el mes correspondiente a dicho número.

        mes = {"Enero": 1, "Febrero": 2, "Marzo": 3, "Abril": 4, "Mayo": 5, "Junio": 6, "Julio": 7, "Agosto": 8,
              "Septiembre": 9, "Octubre": 10, "Noviembre": 11, "Diciembre": 12}
        n = int(input("Ingrese un número del 1 al 12: "))
        for i in mes:
            if n == mes[i]:
                print("El mes que eligio es ", i)
    def EjercicioEstructuras_De_Control_de_Flujo_de_Datos_10(self):
#En un almacén se hace un 20% de descuento a los clientes cuya compra supere
# los Bs 1000, se desea que realice un algoritmo el cual tome por entrada el monto a
# pagar por el cliente y arroje como salida el monto aplicando el descuento de ser
# necesario.
        cantidad = float(input("Ingrese el valor a pagar en el almacen: "))
        if cantidad > 1000:
            total_a_pagar = cantidad * 0.80
            print("SU total a pagar con el descuento de la tienda es de : Bs", total_a_pagar)
        else:
            print("Su total o monto a pagar es de: Bs", cantidad)
         # Otra forma de desarrollarlo
        # cantidad = int(input("Ingrese el valor  a pagar: "))
        # total_a_pagar = cantidad
        # if cantidad > 1000:
        #     total_a_pagar = total_a_pagar - (cantidad * 0.2)
        # print("Su total o monto a pagar es Bs ", total_a_pagar)


    def EjercicioEstructuras_Iterativas_1(self):
        #Dado un número entero N, calcular e informar al usuario cuántos dígitos tiene dicho número.
        N = int(input("Ingrese su numero: "))
        N = str(N)
        print("{} tiene {} dígitos".format(N, len(N)))

    def EjercicioEstructuras_Iterativas_2(self):
        #Dado un número, determine si es capicúa. Nota: un número capicúa es aquel que se lee igual hacia adelante que hacia atrás.
        numeroc = int(input("Ingrese su número: "))
        t = True
        ctdi = 0
        numeroc = str(numeroc)
        ctdf = len(str(numeroc)) - 1
        while t:
            if ctdf - ctdi == 1 or ctdf - ctdi == 2:
                t = False
            if numeroc[ctdi] == numeroc[ctdf]:
                det = True
            else:
                det = False
            ctdi += 1
            ctdf -= 1
        if det:
            print("Es un número capicúa.")
        else:
            print("No es un número capicúa.")

    def EjercicioEstructuras_Iterativas_3(self):
        # Dado un número N determinar si es un número primo.
        # Nota: Un número primo es aquel que solo es divisible por 1(uno) y por el mismo.

        numero = int(input("Ingrese un número: "))
        x = "no es primo"
        if numero % 2 != 0:
            x = "es primo"
        print("El número ingresado", x)

    def EjercicioEstructuras_Iterativas_4(self):
        #Construya un programa que dado un valor entero N, haga el cálculo de la función factorial utilizando estructuras iterativas.
        numerof = int(input("Ingrese número factorial "))
        ra = 1
        for i in range(1, numerof + 1, 1):
            ra = i * ra
        print(ra)

    def EjercicioEstructuras_Iterativas_5(self):
        #Dado un número entero N que representa una contraseña y asumiendo que una
# contraseña debe tener al menos 10 dígitos para ser segura, determine si la
# contraseña ingresada por el usuario es correcta, de no serlo debe pedirla
# nuevamente hasta que tenga los 10 (diez) dígitos solicitados y al ser correcta
# mostrar un mensaje de éxito al usuario, por salida estándar.

        C = 0
        r = True
        while r:
            if len((str(C))) < 10:
                C = int(input("Ingrese la contraseña: "))
                if len((str(C))) == 10:
                    r = False
        print("la contraseña fue exitosamente ingresada")

    def EjercicioEstructuras_Iterativas_6(self):
        #Dada una secuencia de números terminada en cero (0), elaborar un algoritmo que
# informe al usuario qué valor tiene el número mayor y qué valor tiene el número
# menor, sin contar el cero (0).
        x = 1
        Ct = -1
        y = []
        vmayor = 0
        vmenor = vmayor
        while y != 0:
            x = int(input("Ingrese un número: "))
            y.append(x)
            Ct += 1
            if Ct == 1:
                if x > vmayor:
                    vmenor = vmayor
                    vmayor = x
                else:
                    vmenor = x
            elif Ct == 0:
                vmayor = y[0]

            if Ct >= 1:
                if x != 0:
                    if x > vmayor:
                        vmayor = x
                    if x < vmenor:
                        vmenor = x
                else:
                    break

        print("El número mayor es {} y el número menor es {}.".format(vmayor, vmenor))

    def EjercicioEstructuras_Iterativas_7(self):
        #Se tiene una secuencia de enteros terminada en cero, que corresponde a la edad,
# peso y estatura de una muestra de hombres y mujeres mayores de 18 años. Con
# base en dicha secuencia se desea realizar un estudio a fin de conocer:
#  Edad promedio de todas las personas en la muestra.
#  Peso promedio de todas las personas en la muestra.
#  Estatura promedio de todas las personas en la muestra.
#  Cuántas personas hay con edad entre los 18 y 25 años.
#  Cuántas personas son mayores a 36 años.
#  Cuál es el promedio de peso de las personas con edades entre 18 y 35
# años.

        x = 0
        P = ["La edad", "El peso", "La estatura"]
        M= [36, 81, 102, 60, 19, 22, 61, 60, 19, 42, 85, 113, 71, 93, 35, 65, 46, 72, 52, 98, 104, 23, 37, 143,
              25, 56, 73, 28, 99, 105, 21, 52, 132, 46, 57, 60, 27, 80, 93, 102, 51, 121, 76, 57, 18, 26, 77, 101,
              28, 63, 100, 74, 93, 107, 38, 26, 113, 25, 47, 144, 33, 93, 109, 69, 64, 109, 45, 58, 66, 55, 44, 132,
              30, 68, 120, 63, 79, 107, 75, 20, 118, 94, 44, 160, 19, 69, 80, 57, 66, 140, 32, 88, 79, 54, 33, 122, 0]
        Pe = [0, 0, 0, 0]
        AC = [0, 0, 0]
        Ct = 0
        while x < 3:
            AC[x] = AC[x] + M[Ct]

            if M[Ct] == M[96] or M[Ct] == M[95] or M[Ct] == M[94]:
                x += 1
                Ct = 0
                Ct += x
            else:
                if x == 0:
                    if M[Ct] > 18 and M[Ct] < 25:
                        Pe[0] += 1
                        Pe[3] += M[Ct + 1]
                elif M[Ct] > 36:
                    Pe[1] += 1
                Ct += 3
        for i in P:
            Ct += 1
            print("{} promedio de todas las personas en la muestra es {}".format(i, round(((AC[Ct - 4]) / 32))))

        print("Hay {} personas con edad entre los 18 y 35 años con un peso promedio de {}".format(Pe[0], round(
            (Pe[3] / Pe[0]))))
        print("Hay {} personas mayores a 36 años".format(Pe[1]))

    def EjercicioEstructuras_Iterativas_8(self):
        #Construye un algoritmo que calcule e imprima la tabla de multiplicar, desde la tabla
# del 1 hasta la del 10
        for i in range(1, 11, 1):
            for j in range(1, 13, 1):
                print("{} * {} = {}".format(i, j, (i * j)))
            print("*" * 34)

    def EjercicioEstructuras_Iterativas_9(self):
        #Escribir un algoritmo que muestre todas las fichas de dominó, sin repetir.
        x = 0
        ctr = 0
        for i in range(0, 7, 1):
            for j in range(i, 7, 1):
                print(i, " ", j)

    def EjercicioEstructuras_Iterativas_10(self):
        #Dados N número positivos (N>1) calcular el promedio de esta serie. Considere que
# la serie termina al leer un 0.
        N = 1
        T = 0
        ctr = 0
        x = ["Ingrese", "Número incorrecto, ingrese"]
        y = 0
        while N != 0:
            N = int(input(x[y] + " un número positivo: "))
            if N > 1:
                y = 0
                T += N
                ctr += 1
            else:
                y = 1
        print("Su promedio de la serie es: ", (T / (ctr)))

    def EjercicioProcedimientos_1(self):
        #Construya una función que solicite edades al usuario y determine el promedio de
# las edades mayores a 18 años. El usuario indicará cuando desea dejar de
# suministrar datos de entrada. En la Acción Principal se informará el promedio
# calculado.
        Datos = input("Desea ingresar datos? sí (y) o no (n) ")
        if Datos.lower() == "y":
            print("Si desea dejar de ingresar datos, ingrese una 'x'")
            promedio = Ejercicios()
            prom = promedio.SoliUser(Datos)
            if prom != 0:
                print("El promedio de las edades mayores a 18 años es de: ", prom)
            elif prom == 0:
                print("No existen edades mayores a 18 años.")
            else:
                print("Como no ha dado valores, no hay promedio.")
        else:
            print("No ingresó edades!")

    def SoliUser(self, x):
        le = []
        while x.lower() != "x":
            y = input("Ingrese edad: ")
            if y == "x":
                x = "x"
            elif y != "x" and int(y) <= 0:
                print("Ingrese un valor acorde, o ingrese 'x' para dejar de ingrear datos.")
            elif int(y) > 18:
                le.append(int(y))
        if len(le) > 0:
            print(le)
            Pr = (sum(le)) / len(le)
        else:
            Pr = 0

        return Pr

    def EjercicioProcedimientos_2(self):
        #Construya una función “Eleva” Que reciba como parámetros una base y un exponente y retorne al algoritmo principal el resultado de elevar un numero al otro.
        x = int(input("Ingrese la base: "))
        y = int(input("Ingrese su exponente: "))
        expo = Ejercicios()
        ex = expo.Eleva(x, y)
        print("El resultado de elevar {} a la {} es {}".format(x, y, ex))

    def Eleva(self, base, ex):
        resultado = base ** ex
        return resultado

    def EjercicioProcedimientos_3(self):
       #Escriba una función que calcule el perímetro del pentágono (siendo el perímetro la suma de los lados del polígono)
        lado = int(input("Ingrese el lado del polígono: "))
        perimetro = Ejercicios()
        pe = perimetro.PerPenta(lado)
        print("El perímetro del pentágono es: {}".format(pe))

    def PerPenta(self, lado):
        resultado = lado * 5
        return resultado

    def EjercicioProcedimientos_4(self):
        #En una empresa pagan según las horas trabajadas y una tarifa fija por hora. Si la
# cantidad de horas trabajadas en una semana es mayor a 40, la tarifa se
# incrementa en un 35% para las horas extras. Escribe una acción principal que
# solicite la identificación de 5 empleados, el monto cancelado por hora, y la
# cantidad de horas trabajadas por cada uno, llame a acciones/funciones que
# calculen el salario semanal por horas trabajadas (<=40) y los ingresos por
# concepto de horas extras, y finalmente informe los resultados en la acción
# principal.

        ID = {}
        accionp = Ejercicios()
        while len(ID) <= 4:
            x = input("Ingrese su identificación(nombre): ")
            ID[x] = int(input("Ingrese horas trabajadas{}: ".format(x)))
        monto_h = int(input("Ingrese el monto por hora: "))

        Ss = accionp.CalSalSem(ID, monto_h)
        for i in Ss:
            print(i, "cobrará", Ss[i][1])

    def CalSalSem(self, x, re):
        CacP = Ejercicios()
        for i in x:
            if x[i] <= 40:
                x[i] = [x[i], (x[i] * re)]
            else:
                x[i] = [x[i], (40 * re)]
                x[i][1] = CacP.CalIngHExt(x[i], re)
        print("*" * 20)
        return x

    def CalIngHExt(self, K, ET):
        extras = K[1] + ((K[0] - 40) * (ET + (ET * 0.35)))
        return extras

    def EjercicioProcedimientos_5(self):
        #Escriba una acción (MillasAKilometros) que convierta una distancia en millas a
# kilómetros (1milla = 1.60935km). Esta acción recibirá como parámetros: el nombre
# de la ciudad origen, el nombre de la ciudad destino y la distancia en millas entre
# ellas y debe retornar la distancia entre las ciudades en kilómetros.
# Desarrolle además una acción principal en donde utilice a la acción
# MillasAKilometros para convertir e informar la distancia en kilómetros entre 4 pares
# de ciudades suministradas por el usuario.
# Entrada:
# Cuidad A
# Ciudad B
# 332
# Salida:
# Entre la Ciudad A y la Ciudad B hay 534.30 Km.

        Cal = Ejercicios()
        DP = ["primer", "segundo", "tercer", "cuarto"]
        ctr = 0
        while ctr < 5:
            CA = input("Ingrese el {} par de Ciudad:\n1. ".format(DP[ctr]))
            CB = input("2. ")
            D = int(input("Ingrese la distancia entre la ciudad {} y {}: ".format(CA, CB)))
            CMK = Cal.Calmikm(CA, CB, D)
            print("Entre la ciudad de {} y la de {} hay {} Km".format(CA, CB, round(CMK, 2)))
            ctr += 1

    def Calmikm(self, a, b, c):
        KMC = 1.60935
        resultado = c * KMC
        return resultado

Resolucion_de_ejercicio = Ejercicios()
Resolucion_de_ejercicio.EjercicioEstructuras_Iterativas_7()
