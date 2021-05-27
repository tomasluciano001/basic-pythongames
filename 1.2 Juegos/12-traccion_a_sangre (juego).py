import random

numero_random = random.randint(1,100)

cars = False
metal = False

print("\nTracción a sangre \n"
      "------------------- \n\n"
      "Fuiste a hacer un trabajo de reparación de computadoras a un barrio peligroso. \n"
      "Al salir de la casa de tu cliente, un grupo de personas te quieren robar pero saliste corriendo y \n"
      "lograste perderlos por poco tiempo. \n\n"
      "Ahora te están buscando y tenés que salir del barrio lo más rápido posible. ¿Cómo vas a salir? \n")

opcion = input("OPCION A: Te arriesgás a sacar el celular y llamás a tu amigo que vivió ahí para que te venga a buscar \n"
      "OPCION B: Intentar buscar la salida por tu cuenta\n")

if opcion == "A":
      print("Tu amigo va para allá en seguida, te dice que vuelvas a la casa del cliente para que estén más seguros")
      opcion = input("OPCION A: Ignorar su consejo \n"
                     "OPCION B: Volver sabiendo que los ladrones te están buscando \n")

      if opcion == "A":
            print("Caminás sin rumbo un buen rato hasta que los ladrones te encuentran \n" 
                  "y te matan para sacarte la plata que cobraste. FIN \n")
            exit()

      elif opcion == "B":
            print("Volvés a la casa del cliente y afortunadamente los ladrones ya se habían ido del lugar. \n"
                  "Tu cliente te deja entrar después de explicarle la situación. \n\n"
                  "Pasado un rato tu amigo te avisa que ya está cerca y que vayas saliendo, pero \n"
                  "te das cuenta que no vino en auto como pensabas sino que fue caminando. ¿Qué hacés?\n")

            opcion = input("OPCION A: Lo seguís igual porque ya conoce el barrio \n"
                           "OPCION B: Le decís que es un boludo y te vas solo \n")

            if opcion == "A":
                  print("Te lleva por unos pasillos re turbios dentro del barrio \n\n"
                        "Llegado el momento, se encuentran con una valla bastante alta y te dice que la saltes. \n"
                        "Del otro lado hay una plaza tranquila, no te va a pasar nada, te dice \n\n"
                        "Al saltarla ves que hay una feria y tienen algunos juegos donde se sortean premios.\n")

                  opcion = input("OPCION A: Jugar \n"
                                 "OPCION B: No jugar \n")

                  if opcion == "A":
                        print("Te sumás y el chico que atiende el juego te dice que si superás el siguiente reto mental \n"
                              "te ganás un juguete de Cars. \n")

                        print("¿Cuánto es 3 * {}? ".format(numero_random))
                        opcion = int(input("¿Cuál es el resultado? \n"))

                        if opcion == 3 * numero_random:
                              print("¡¡¡GANASTE!!! \n"
                                    "*Se añadió Mate a tu inventario* \n")
                              cars = True
                              print("De repente ves que un nene está triste porque te ganaste ese juguete y vos no \n")

                              opcion = input("OPCION A: Se lo das \n"
                                             "OPCION B: No se lo das \n")
                              if opcion == "A":
                                    print("Se lo regalás y entendés que a pesar de haber tenido un mal día todavía existe bondad e inocencia en el mundo. \n"
                                          "Ahora ese chico va a tener un lindo juguete con el cual jugar y tal vez hacerle su infancia un poco más fácil. \n"
                                          "Te volvés contento a tu casa :) FIN")
                                    exit()
                              elif opcion == "B":
                                    print("No se lo das porque ese chico no hizo ningún mérito para tenerlo y vos sí. \n"
                                          "Debería aprender a esforzarse más para que entienda que nadie le va a regalar nada en la vida :( \n"
                                          "FIN")
                                    exit()
                        else:
                              print("Perdiste, mejor suerte para la próxima :(")
                              exit()

                  elif opcion == "B":
                        print("Volvés a tu casa triste y asustado por lo que pasaste. \n"
                              "En el camino considerás seriamente la idea de mudarte de país. FIN. \n")

            elif opcion == "B":
                  print("Tu amigo te insiste en acompañarte igual, así que lo vas a tener que aguantar de todas formas... \n"
                        "LLegado el momento se encuentran con una valla bastante alta y te dice que la saltes. \n"
                        "Del otro lado hay una plaza tranquila, no te va a pasar nada te dice. \n"
                        "Al saltarla ves que hay una feria y tienen algunos juegos donde sortean premios. \n")

            opcion = input("OPCION A: Jugar \n"
                           "OPCION B: No jugar \n")

            if opcion == "A":
                  print("Te sumás y el chico que atiende el juego te dice que si superás el siguiente reto mental \n"
                        "te ganás un juguete de Cars. \n")

                  print("¿Cuánto es 5 * {}? ".format(numero_random))
                  opcion = int(input("¿Cuál es el resultado? \n"))

                  if opcion == 5 * numero_random:
                        print("¡¡¡GANASTE!!! \n"
                              "*Se añadió un Rayo McQueen a tu inventario* \n")
                        cars = True
                        print("De repente ves que un nene está triste porque te ganaste ese juguete y vos no \n")

                        opcion = input("OPCION A: Se lo das \n"
                                       "OPCION B: No se lo das \n")
                        if opcion == "A":
                              print("Se lo regalás y entendés que a pesar de haber tenido un mal día todavía existe bondad e inocencia en el mundo. \n"
                                    "Ahora ese chico va a tener un lindo juguete con el cual jugar y tal vez hacerle su infancia un poco más fácil. \n"
                                    "Te volvés contento a tu casa :) FIN")
                              exit()
                        elif opcion == "B":
                              print("No se lo das porque ese chico no hizo ningún mérito para tenerlo y vos sí. \n"
                                    "Debería aprender a esforzarse más para que entienda que nadie le va a regalar nada en la vida :( \n"
                                    "FIN")
                              exit()
                  else:
                        print("Perdiste, mejor suerte para la próxima :(")
                        exit()


elif opcion == "B":
      print("Los ladrones te encuentran, te noquean y te secuestran. Te hubieran matado pero saben que vales más si piden un rescate… \n"
            "De repente te despertás atado a una silla con un dolor muy fuerte de cabeza. Ves a tu alrededor y te das cuenta que estás en un cuarto con poca iluminación y solo hay una cama. \n\n"
            "Al rato llega un vigilante y te pone al tanto de la situación... Vas a tener una rutina y horarios muy específicos por cumplir, \n"
            "vas a vivir ahí hasta que alguien decida pagar el rescate y si nadie paga te matan \n"
            "¿Qué hacés? \n")
      opcion = input("OPCION A: Seguir sus órdenes y tratar de encontrar una salida \n"
                     "OPCION B: Desobedecerlos y tratar de encontrar una salida \n")

      if opcion == "A":
            print("No fue sencillo pero viste una oportunidad a las 5:30 de la mañana, a esa hora 2 guardias \n"
                  "desaparecían 15 minutos más o menos pero no era suficiente, necesitabas algo con lo que poder abrir la cerradura. \n\n"
                  "Viste que durante el aseo algunas pavas tenían trozos de metal en la parte inferior que podían ser arrancados sin que se notara \n"
                  "¿Qué hacés?\n")
            opcion = input("OPCION A: Arrancarla sin que se den cuenta \n"
                           "OPCION B: Es una idea ridícula, no la arrancás y seguís esperando a ver si se te ocurre algo mejor \n")

            if opcion == "A":
                        metal = True
                        print("*Se añadió un trozo de metal a tu inventario* \n")
                        print("Con esa pequeña pieza ya tenías todo lo necesario. Fingiste dormirte y esperaste a que fuera la hora. \n"
                        "Cuando fueron a vigilarte vieron que tu cama parecía más pequeña... te gritaron pero no se movía nadie... \n"
                        "Entraron pero ya te habías ido de la habitación aunque todavía tenías que escapar de la casa ¿Hacia dónde te dirigís? \n\n"
                        "A la izquierda una puerta semiabierta. A la derecha una ventana \n")

                        opcion = input("OPCION A: Puerta \n"
                                 "OPCION B: Ventana \n")

                        if opcion == "A":
                            print("Te das cuenta que está cerrada... Si tan solo tuvieras algo con qué abrirla...")
                            opcion = input("OPCION A: El trozo de metal no va a servir para abrir una cerradura... Intentás buscar otra salida \n"
                                                   "OPCION B: Intentar usar el trozo  de metal que recogiste \n")
                            if opcion == "A":
                                print("No hay tiempo, los secuestradores te están buscando por todos lados \n"
                                      "De todas formas decidís buscar otra salida caminando sigilosamente. \n\n"
                                      "Encontrás otra puerta que tiene un candado... Para abrirlo tenés que resolver una adivinanza...\n"
                                      "Si acertás podrás escapar, sino va a saltar una alarma que alertará a todos. \n\n"
                                      "Ahí te va: ¿Cuál es la estrella que no tiene luz?")
                                opcion = input("OPCION A: ESTRELLA FUGAZ \n"
                                               "OPCION B: ESTRELLA DE MAR \n")

                                if opcion == "A":
                                    print("TE EQUIVOCASTE!!!\n"
                                          "La alarma comienza a sonar y los secuestradores te encuentran... deciden sacarte \n"
                                          "tu comida y tus horarios para ir al baño dejándote completamente a tu merced... \n\n"
                                          "Sin ninguna posibilidad de escapar y muriéndote de hambre tu única esperanza es esperar a que paguen tu rescate. \n"
                                          "Pero lo que no sabés es que tu familia no puede pagarlo y por lo tanto te quedás esperando en vano. \n"
                                          "Moriste. FIN :( \n")
                                    exit()

                                elif opcion == "B":
                                    print("ACERTASTE!!! \n"
                                          "La puerta se abre delante tuyo, aparece un pasillo que te lleva hasta la salida. \n"
                                          "Lo recorrés y llegás al final hay una compuerta en el techo del pasillo que abrís \n"
                                          "Al subir ya estás afuera, te encontras en el patio trasero de la casa \n"
                                          "Te das cuenta que usaban ese pasillo para trasladar a las personas por ahí... De todas formas ya saliste, sos libre. FIN :)\n")
                                    exit()

                            elif opcion == "B":
                                print("*SE ELIMINÓ TROZO DE METAL DEL INVENTARIO* \n "
                                      "Felicidades! lograste destrabarla, al abrir la puerta ves que hay unas escaleras que dan a la planta baja \n"
                                      "Bajás y divisás la puerta que da a la calle pero no tenés con que abrirla. ¿Qué hacés? \n")
                                opcion = input("OPCION A: Divisás una silla... Si la estampás contra una ventana podrías escapar pero te arriegás a que te descubran \n"
                                               "OPCION B: Buscar en los cajones de los muebles a ver si encontrás alguna llave \n")

                                if opcion == "A":
                                    print("Con la silla en mano en mano empezás a buscar sigilosamente entre los distintos cuartos una ventana... \n"
                                          "Para tu fortuna encontrás una en la cocina, pero es un poco pequeña... Aún así le das con la silla y se rompe en mil pedazos. \n"
                                          "Se comienzan a escuchar ruidos por toda la casa... Se dieron cuenta que te estás queriendo escapar y no van a tardar en venir por vos. \n"
                                          "En eso tirás la silla e intentás acomodar tu cuerpo de la mejor manera posible para pasar por la ventana. \n"
                                          "Cuando ya te faltaba pasar la otra mitad de tu cuerpo uno de los secuestradores te agarra la pierna... \n"
                                          "pero vos lo comenzás a patear como un loco \n"
                                          "Le pateás la cara con una fuerza tremenda y te suelta, así que terminás de pasar la otra mitad de tu cuerpo afuera. \n"
                                          "Listo, saliste. Tenés todo el cuerpo raspado pero por lo menos estás a salvo. FIN :)\n")
                                    exit()


                                elif opcion == "B":
                                    print("No encontrás una sola llave en toda la casa, te empezás a desesperar y hacés ruido. \n"
                                          "Los secuestradores se dan cuenta y bajan a buscarte \n"
                                          "No toleran que no les hagas caso y al cabo de unos días manteniéndote deciden sacarte \n"
                                          "tu comida y tus horarios para ir al baño dejándote completamente a tu merced... \n\n"
                                          "Sin ninguna posibilidad de escapar y muriéndote de hambre tu única esperanza es esperar a que paguen tu rescate. \n"
                                          "Pero lo que no sabés es que tu familia no puede pagarlo y por lo tanto te quedás esperando en vano. \n"
                                          "Moriste. FIN")
                                    exit()

                        elif opcion == "B":
                            print("Abrís la ventana pero uno de los secuestradores te agarra y te empuja hacia atrás, trata de pegarte pero \n"
                        "lo equivás de milagro y eso te da una oportunidad para pegarle vos ahora. \n\n"
                        "Le pegás en la cara y te girás hacia la ventana que dejaste abierta, te acercás lo más rápido posible y salís.\n"
                        "De repente estás agarrado de la cornisa y ves que otro secuestrador viene pero este trae un arma y dispara al aire. \n"
                        "Tenés que tomar una decisión rápida. ¿Qué hacés? \n")
                        opcion = input("OPCION A: Tratás de moverte por la cornisa hacia otro cuarto para volver a entrar a la casa y salir mejor.\n"
                                       "OPCION B: Te tirás \n")

                        if opcion == "A":
                              print("En un intento de avanzar hacia adelante te resbalás y caés de cabeza, te morís. FIN.")

                        elif opcion == "B":
                            print("Te tirás y caés en una pierna, estás rengueando y como podés llegás a la calle... Empezás a gritar por ayuda... Segundos más tarde \n"
                                    "suenan sirenas de policía y te das cuenta que los vecino llamaron a la polcía debido a los tiros, mientras, vos seguís caminando. \n\n"
                                    "En eso la policía se baja de su patrulla y te derriban, de repente tenés a un perro olfateándote en busca de drogas. \n"
                                    "Escuchás a los vecinos gritar y pedir que te arresten por disturbios.\n"
                                    "Te meten en un auto y te llevan a declarar a la comisaría... Vos les contás todo. FIN.")
                            exit()

            elif opcion == "B":
                        metal = False
                        print("Perdés la oportunidad y no la pudiste volver a encontrar. Sin ninguna posibilidad de escapar y múriendote de hambre \n"
                              "Tu única esperanza es eperar a que paguen tu rescate. Pero lo que no sabés es que tu familia no puede pagarlo y \n"
                              "por lo tanto te quedás esperando en vano. \n"
                              "Moriste. FIN.")
                        exit()

      elif opcion == "B":
            print("Desobedecerlos fue un grave error. No toleran que no les hagas caso y al cabo de unos días manteniéndote deciden sacarte \n"
                        "tu comida y tus horarios para ir al baño dejándote completamente a tu merced... \n\n"
                        "Sin ninguna posibilidad de escapar y muriéndote de hambre tu única esperanza es esperar a que paguen tu rescate. \n"
                        "Pero lo que no sabés es que tu familia no puede pagarlo y por lo tanto te quedás esperando en vano. \n"
                        "Moriste. FIN")
            exit()