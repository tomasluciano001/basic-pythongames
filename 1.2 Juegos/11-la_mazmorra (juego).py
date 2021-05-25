import random

print("Juego de la mazmorra \n"
      "-------------------- \n"
      "\n"
      "Vos y tu compañero de celda acaban de escapar de la prisión, burlaron a los guardias \n"
      "y se dirigen hacia el exterior. Entran en una mazmorra controlada por guardias con armadura \n"
      "y uno de sus guardia ataca a tu compañero pero te escondés. Se lo llevan pero vos pasas desapercibido entre las sombras \n"
      "El guardia se retira, es tu posibilidad de escapar. ¿Hacia dónde te dirigís? \n"
      "\n"
      "A la izquierda hay una puerta semiabierta. A la derecha una escotilla en el suelo \n")

opcion = input ("OPCION A: Puerta semiabierta | OPCION B: Escotilla \n")

if opcion == "A":
    print("Entrás en la puerta semiabierta y otro guardia te descubre. ¿Qué hacés?")
    opcion = input("OPCION A: Te hacés el muerto | OPCION B: Salís corriendo hacia la siguiente puerta \n")

    if opcion == "A":
        print("El guardia se da cuenta que no estás muerto y te encierran en una celda de máxima seguridad. \nFIN.")
    elif opcion == "B":
        print("Después de esa puerta encontrás una rana mutante que te regala un puñal casero hecho de madera. ¿Lo acepás?")
        opcion = input("OPCION A: Sí | OPCION B: No \n")
        if opcion == "A":
            print("Agarrás el puñal y avanzas, hay dos pasillos circulares, no ves el final de ninguno. \n"
                  "Hay uno a la derecha y otro a la izquierda. ¿Cuál elegís?")
            opcion = input("OPCION A: Izquierda | OPCION B: Derecha \n")
            if opcion == "A":
                print("La habitación se hace cada vez más oscura, ves tan poco que caes en un agujero con pinchos y moris de forma dolorosa.\nFIN")
            elif opcion == "B":
                print("Encontrás la salida, en la puerta hay estacionado un carruaje de lujo, te subís y escapás hacia tu libertad \nFIN :)")
        elif opcion == "B":
            print("La rana te devora y te morís en seguida, su veneno hace efecto casi de manera instantánea \nFIN")


elif opcion == "B":
    print("Caes en una zona inundada, el agua te llega hasta las rodillas, avanzás durante media hora y finalmente \n"
          "llegás a una zona abierta seca y con luz, parecen unas alcantarillas \n\n"
          "Encontrás un palo largo, es robusto... podría servir en el futuro, quién sabe ¿Lo levantás?")
    opcion = input("OPCION A: Sí | OPCION B: No \n")

    palo_inventario = False

    if opcion == "A":
        print("Agarraste el palo \n")
        palo_inventario = True
    elif opcion == "B":
        print("No lo agarrás \n")
    else:
        print("No elegiste nada, así que te morís por indeciso :( \n FIN")
        exit()

    numero_random_rata = random.randint(1, 100)
    print("Seguís avanzando, encontrás una rata de 2 metros y te pregunta: ¿Cuánto es 13 * {}?".format (numero_random_rata))
    opcion = int(input("¿Cuál es el resultado?"))

    if opcion == 13 * numero_random_rata:
        print("La rata te asesina en el acto, resulta que odia a la gente que es más inteligente que ella \nFIN")
    else:
        print("La rata abre una puerta delante tuyo, parece un pasillo que lleva hasta la salida. \n"
              "Lo recorrés, llegás al final y el túnel se derrumba atrás tuyo, no parece haber salida \n"
              "salvo una boca de alcantarilla en el techo, pero está lejos de tu alcance ¿Qué hacés? \n")

        opcion = input("OPCION A: Esperás a que alguien te rescate | OPCION B: Intentás salir \n")

        if opcion == "A":
            print("Un montón de ratas aparecen y te devoran vivo, morís. \nFIN")
        elif opcion == "B" and palo_inventario:
            print("Usás el palo que agarraste antes para impulsarte, lográs trepar y salir de ahí. \n"
                  "En la puerta hay estacionado un carruaje de lujo, te subís y escapás hacia tu libertad \nFIN :)")
        else:
            print("No tenés con que subir, si tan solo tuvieras un palo... Pero no lo tenés \n"
                  "Así que te quedás atrapado.  \n\nPasado un rato aparecen un montón de ratas hambrientas que te devoran vivo. \nFIN")
else:
    print("No elegiste ninguna opción válida")
    exit()