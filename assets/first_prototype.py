print("Bienvenido a Maquina Zen.")
userName = input("Para iniciar ingresa tu nombre: ")
print("Bienvenido", userName)
print("Si estás acá es porque estás buscando respuestas que solo tú podrás responder. De todas maneras, \nTODO es solo un truco y este simple programa de computadora te permitirá entender aquello.")
print("---------------------------------------------------------------------------\n---------------------------------------------------------------------------")
print("Nuestros servidores disponen han logrado encontrar 3 registros de Maestros 'Zen' \n¿Con cual de ellos quisieras hablar?")
print("Dogen > > > ")
print("Bodhidharma > > >")
print("Milarepa > > >")
dogenSalute = "saludos"
userPath = input("Quiero hablar con:")
if userPath == "Dogen":
    print("El maestro Dogen ha ingresado a la sala de chat.")
    for i in dogenSalute:
        print(i)
    for i in userName:
        print(i)
    print("Dogen dice:", userName + ",", "si eres incapaz de encontrar la verdad justo donde estás, ¿donde más esperas encontrarla?")
    responseDogen = input("¿Que respondes?")
    print("Dogen dice: ")
