#Cajero automático

lista_nombres = ["Sofi�a", "Mateo", "Isabella", "Lucas", "Valentina", "Alejandro", "Emma", 
                 "Santiago", "Martina", "Sebastian", "Camila", "Nicolas", "Valeria", "Gabriel", 
                 "Antonella", "Daniel", "Lucía", "Andrés", "Renata", "Adrián", "Sara", "Diego", 
                 "Julieta", "Joaqui�n", "Paula", "Leonardo", "Victoria", "Benjamín", "María", "Samuel", 
                 "Amelia", "David", "Elena", "Maximiliano", "Montserrat", "Ángel", "Regina", "Tomás", 
                 "Jimena", "Cristobal", "Fernanda", "Bruno", "Ana", "Ricardo", "Ximena", "Gael", "Andrea", 
                 "Mati�as", "Carolina", "Thiago", "Daniela", "Emilio", "Alicia", "Jerónimo", "Natalia", 
                 "Dylan", "Claudia", "Iker", "Patricia", "Ivan", "Alejandra", "Alan", "Laura", "Franco", 
                 "Gabriela", "Jesus", "Mariana", "Rodrigo", "Lorena", "Martín", "Melissa", "Juan", "Paola", 
                 "Carlos", "Diana", "Pedro", "Carmen", "Miguel", "Rosa", "Jorge", "Gloria", "Luis", "Silvia", 
                 "Antonio", "Isabel", "Jose", "Esther", "Manuel", "Beatriz", "Francisco", "Raquel", "Javier", 
                 "Susana", "Raúl", "Pilar", "Alberto", "Eva", "Enrique", "Dolores", "Sergio", "Mercedes", 
                 "Oscar", "Cristina", "Julio", "Rosario"]

dict_users ={i: np.random.randint(10000, 500000) for i in lista_nombres}

str_nombre = ''

for enu, i_name in enumerate(lista_nombres):
    str_nombre = str_nombre + f"\n {enu}" + i_name

while True:
    seleccion = int(input(f" Usted quien es?: {str_nombre} \n105: SALIR\n"))
    seleccion_cliente = lista_nombres[seleccion]
    
    if seleccion in range(len(lista_nombres)):
        while True:
            operaciones = int(input("Que quiere hacer? Ver\n1: Retirar\n2: Consignar\n3: SALIR\n"))
            
            saldo_cuenta_usuario = dict_users[seleccion_cliente]
            
            #Ver
            if operaciones == 0:
                print(saldo_cuenta_usuario)
            #Retirar
            elif operaciones == 1:
                valor_retiro = int(input("Cuanto quiere retirar?: "))
                if valor_retiro <= saldo_cuenta_usuario:
                    print("Retiro Exitoso")
                    dict_users[seleccion_cliente] = saldo_cuenta_usuario - valor_retiro
                    print("Su saldo es: ", dict_users[seleccion_cliente])
        
            #consignar
            elif operaciones == 2:
                valor_consignar = int(input("¿Cuanto quiere consignar?: "))
                dict_users[seleccion_cliente] = saldo_cuenta_usuario + valor_consignar
                
            else:
                break
            
    elif seleccion == 105:
            break 
    else:
            print("Error: no selecciono una opci�n v�lida")