

notas1=[f"Lengua = 5 , Matematica = 8 , Cs Sociales = 7 , Cs Naturales = 8"]
alumno1={"nombre":"Juan","apellido": "Fernandez","DNI":"51872145","FDN":"22/09/2011","tutor":"Pablo Fernandez","notas":notas1,"faltas":2, "amonestaciones":0}

notas2=[f"Lengua = 9 , Matematica = 6 , Cs Sociales = 6 , Cs Naturales = 7"]
alumno2={"nombre":"Geronimo","apellido": "Ortega","DNI":"51679203","FDN":"17/01/2011","tutor":"Lucio Ortega","notas":notas2,"faltas":2, "amonestaciones":0}

notas3=[f"Lengua = 8 , Matematica = 7 , Cs Sociales = 7 , Cs Naturales = 9"]
alumno3={"nombre":"Juan","apellido": "Gutierrez","DNI":"51964311","FDN":"11/04/2011","tutor":"Liliana Gutierrez","notas":notas3,"faltas":2, "amonestaciones":1}



Alumnos=[alumno1,alumno2,alumno3]

def mostrar(alumno1,alumno2,alumno3):
    print(alumno1)
    print(alumno2)
    print(alumno3)

def modify(alumno1,alumno2,alumno3):
    i=input("que alumno desea modificar? Alumno 1, 2 o 3?: ")
    if i == 1:
        cambio=input("que desea cambiar: ")
        if cambio=="nombre":
            nombreNuevo=input("ingrese el nombre del alumno: ")
            alumno1["nombre"]=nombreNuevo
        
        if cambio=="apellido":
            ApellidoNuevo=input("ingrese el apellido nuevo: ")
            alumno1["apellido"]=ApellidoNuevo

        if cambio=="DNI" or "dni":
            NuevoDni=input("ingrese el nuevo DNI: ")
            alumno1["DNI"]=NuevoDni
        
        if cambio=="FDN" or "fecha de nacimiento":
            NuevaFdn=input("ingrese la fecha de nacimiento: ")
            alumno1["FDN"]=NuevaFdn

        if cambio=="tutor":
            NuevoTutor=input("ingrese el nuevo tutor: ")
            alumno1 ["tutor"]=NuevoTutor

        if cambio=="notas":
            NuevasNotas=input("ingrese las notas del alumno: ")
            alumno1["notas"]=NuevasNotas
        
        if cambio=="faltas":
            NumFaltas=input("ingrese la cantidad defaltas del alumno")
            alumno1["faltas"]=NumFaltas

        if cambio=="amonestaciones":
            NumAmonsetaciones=input("ingrese el numero de amonestaciones: ")
            alumno1["amonestaciones"]=NumAmonsetaciones

    if i == 2:
        cambio=input("que desea cambiar: ")
        if cambio=="nombre":
            nombreNuevo=input("ingrese el nombre del alumno: ")
            alumno2["nombre"]=nombreNuevo
        
        if cambio=="apellido":
            ApellidoNuevo=input("ingrese el apellido nuevo: ")
            alumno2["apellido"]=ApellidoNuevo

        if cambio=="DNI" or "dni":
            NuevoDni=input("ingrese el nuevo DNI: ")
            alumno2["DNI"]=NuevoDni
        
        if cambio=="FDN" or "fecha de nacimiento":
            NuevaFdn=input("ingrese la fecha de nacimiento: ")
            alumno2["FDN"]=NuevaFdn

        if cambio=="tutor":
            NuevoTutor=input("ingrese el nuevo tutor: ")
            alumno2 ["tutor"]=NuevoTutor

        if cambio=="notas":
            NuevasNotas=input("ingrese las notas del alumno: ")
            alumno2["notas"]=NuevasNotas
        
        if cambio=="faltas":
            NumFaltas=input("ingrese la cantidad defaltas del alumno")
            alumno2["faltas"]=NumFaltas

        if cambio=="amonestaciones":
            NumAmonsetaciones=input("ingrese el numero de amonestaciones: ")
            alumno2["amonestaciones"]=NumAmonsetaciones

    if i == 3:
        cambio=input("que desea cambiar: ")
        if cambio=="nombre":
            nombreNuevo=input("ingrese el nombre del alumno: ")
            alumno3["nombre"]=nombreNuevo
        
        if cambio=="apellido":
            ApellidoNuevo=input("ingrese el apellido nuevo: ")
            alumno3["apellido"]=ApellidoNuevo

        if cambio=="DNI" or "dni":
            NuevoDni=input("ingrese el nuevo DNI: ")
            alumno3["DNI"]=NuevoDni
        
        if cambio=="FDN" or "fecha de nacimiento":
            NuevaFdn=input("ingrese la fecha de nacimiento: ")
            alumno3["FDN"]=NuevaFdn

        if cambio=="tutor":
            NuevoTutor=input("ingrese el nuevo tutor: ")
            alumno3 ["tutor"]=NuevoTutor

        if cambio=="notas":
            NuevasNotas=input("ingrese las notas del alumno: ")
            alumno3["notas"]=NuevasNotas
        
        if cambio=="faltas":
            NumFaltas=input("ingrese la cantidad defaltas del alumno")
            alumno3["faltas"]=NumFaltas

        if cambio=="amonestaciones":
            NumAmonsetaciones=input("ingrese el numero de amonestaciones: ")
            alumno3["amonestaciones"]=NumAmonsetaciones


def agregar(Alumnos):
    print(Alumnos)
    nombre4=input("ingrese el nombre del alumno nuevo: ")
    apellido4=input("ingrese su apellido: ")
    FDN4=input("ingrese su fecha de nacimiento: ")
    DNI4=input("ingrese su DNI: ")
    Tutor4=input("ingrese el nombre y apellido de su tutor: ")
    NumFaltas4=0
    NumAmones4=0

    Alumno4={"nombre":nombre4,"apellido": apellido4,"DNI":DNI4,"FDN":FDN4,"tutor":Tutor4,"faltas":NumFaltas4, "amonestaciones":NumAmones4}

    Alumnos.append(Alumno4)
    print(Alumnos)
    print("¡Se ha añadido con exito!")

def remove(Alumnos):
    Remove="Ingrese el numero de alumno que desea borrar: "

    if Remove==1:
        Alumnos.remove(0)
        print(Alumnos)
        print("¡Se ha borrado con exito!")

    if Remove==2:
        Alumnos.remove(1)
        print(Alumnos)
        print("¡Se ha borrado con exito!")
        
    if Remove==3:
        Alumnos.remove(2)
        print(Alumnos)
        print("¡Se ha borrado con exito!")


a=input("que desea realizar?: ")

if a=="mostrar los datos de los alumnos" or "mostrar" or "mostrar alumnos" or "alumnos" or "show":

    mostrar()

if a=="modificar" or "modify" or "editar" or "modificar un alumno":

    modify()

if a=="agregar" or "add" or "append" or "añadir":

    agregar()

if a=="borrar" or "delete" or "destroy" or "remove" or "eliminar" :

    remove()

else:
    al=input("si necesitas ayuda usa /help para ver tus opciones: ")
    if al=="/help":
        print("Para mostrat los datos de algun alumno: - mostrar los datos de los alumnos - mostrar - show - alumnos ")
        print("Para modificar algun alumno: - modificar - modify - editar - modificar a un alumno ")
        print("Para agregar a un alumno: - agregar - add - append - añadir")
        print("Para borrar la informacion de un alumno: - borrar - delete - destroy - remove - eliminar")




    






    