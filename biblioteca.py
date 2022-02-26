

#sistema de simulacion de una biblioteca

#ch0l0h4twh1t3

#Challenge : Sistema de Biblioteca

print("""
 ________  ___  ________  ___       ___  ________  _________  _______   ________  ________                 ________       ___    ___ ________      
|\   __  \|\  \|\   __  \|\  \     |\  \|\   __  \|\___   ___\\  ___ \ |\   ____\|\   __  \               |\   ____\     |\  \  /  /|\   ____\     
\ \  \|\ /\ \  \ \  \|\ /\ \  \    \ \  \ \  \|\  \|___ \  \_\ \   __/|\ \  \___|\ \  \|\  \  ____________\ \  \___|_    \ \  \/  / | \  \___|_    
 \ \   __  \ \  \ \   __  \ \  \    \ \  \ \  \\\  \   \ \  \ \ \  \_|/_\ \  \    \ \   __  \|\____________\ \_____  \    \ \    / / \ \_____  \   
  \ \  \|\  \ \  \ \  \|\  \ \  \____\ \  \ \  \\\  \   \ \  \ \ \  \_|\ \ \  \____\ \  \ \  \|____________|\|____|\  \    \/  /  /   \|____|\  \  
   \ \_______\ \__\ \_______\ \_______\ \__\ \_______\   \ \__\ \ \_______\ \_______\ \__\ \__\               ____\_\  \ __/  / /       ____\_\  \ 
    \|_______|\|__|\|_______|\|_______|\|__|\|_______|    \|__|  \|_______|\|_______|\|__|\|__|              |\_________\\___/ /       |\_________\
                                                                                                             \|_________\|___|/        \|_________|
               
""")
def lib_rom(int_rom):
	print(f"\nsu Libro es: {romance.get(int_rom)}")
	print(f"\n {rom_lib.get(int_rom)}")
	
def lib_terr(int_terr):
    print(f"\nsu Libro es: {terror.get(int_terr)}\n")
    print(f"\n {terr_lib_content.get(int_terr)}")
    
def lib_sus(int_sus):
	print(f"\nSu Libro es: {suspenso.get(int_sus)}")
	print(f"{sus_lib.get(int_sus)}")

print("""
Elija categoria:
    
    1: Terror
    2: suspenso
    3: romance
""")
s_i_e=int(input(" > "))
biblioteca={
1:"terror",
2:"suspenso",
3:"romance",}

romance={
1:"Orgullo y prejuicio",
2:"El ruiseñor",
3:"Edenbrooke",
4:"Tú y yo, invencibles",
5:"El jinete de bronce",
}

suspenso={
1:"Perdida",
2:"La verdad sobre el caso Harry Quebert",
3:"La sombra del viento",
4:"IT",
5:"El silencio de la ciudad blanca",
}
terror={
1:"Hex de Thomas Olde Heuvelt",
2:"La chica de al lado de Jack Ketchum",
3:"Apartamento 16 de Adam Nevill",
4:"El bazar de los malos sueños (2021) de Stephen King",
5:"Reinas del abismo (2020)",
#etc
}
rom_lib={
1:"""
AgotadoEditorial: DESTINO
Año de edición: 2007
Materia: Literatura universal
ISBN: 978-84-233-3955-6
Páginas: 488
Encuadernación: Cartoné
Colección: Ancora y delfín

Satírica, antirromántica, profunda y mordaz a un tiempo, la obra de Jane Austen nace de la observación de la vida doméstica y de un profundo conocimiento de la condición humana.
Orgullo y prejuicio ha fascinado a generaciones de lectores por sus inolvidables personajes y su desopilante retrato de una sociedad, la Inglaterra victoriana y rural, tan contradictoria como absurda.
Con la llegada del rico y apuesto señor Darcy a su región, las vidas de los Bennet y sus cinco hijas se vuelven del revés. El orgullo y la distancia social, la astucia y la hipocresía, los malentendidos y los juicios apresurados abocan a los personajes al escándalo y al dolor, pero también a la comprensión, el conocimiento y el amor verdadero.
""",
2:"""
Editorial: DEBOLSILLO
Año de edición: 2017
Materia: Narrativa histórica
ISBN: 978-84-663-3840-0
Páginas: 592
Encuadernación: Rústica
Colección: Best seller

Dos hermanas buscan su propio camino hacia la supervivencia, el amor y la libertad en la Francia ocupada durante la Segunda Guerra Mundial.50 semanas en el TOP10 del New York Times
Más de 1.500.000 ejemplares vendidos
Uno de los 10 libros más vendidos en USA en 2015
Premio Goodreads Mejor Novela de Ficción HistóricaFrancia, 1939. En el tranquilo pueblo de Carriveau, Vianne Mauriac se despide de su marido, Antoine, que debe marchar al frente. Ella no cree que los nazis vayan a invadir Francia, pero lo hacen, con batallones de soldados marchando por las calles, con caravanas de camiones y tanques, con aviones que llenan los cielos y lanzan bombas sobre los inocentes. Cuando un capitán alemán requisa la casa de Vianne, ella y su hija deben convivir con el enemigo o arriesgarse a perderlo todo. Sin comida ni dinero ni esperanza, Vianne se ve obligada a tomar decisiones cada vez más difíciles para sobrevivir.La hermana de Vianne, Isabelle, es una joven rebelde de dieciocho años que busca un propósito para su vida con toda la temeraria pasión de la juventud. Mientras miles de parisinos escapan de la ciudad ante la inminente llegada de los alemanes, Isabelle se encuentra con Gaëton, un partisano que cree que los franceses pueden luchar contra los nazis desde dentro de Francia. Isabelle se enamora completamente pero, tras sentirse traicionada, decide unirse a la Resistencia. 
""",
3:"""
Editorial: LIBROS DE SEDA
Año de edición: 2016
Materia: Novela romántica
ISBN: 978-84-16550-60-9
Páginas: 524
Encuadernación: Rústica

Marianne Daventry haría cualquier cosa para escapar del aburrimiento de Bath y las atenciones amorosas de un cretino que no le interesa en absoluto. Así que cuando le llega una invitación de su hermana gemela, Cecily, para que se una a ella en una maravillosa casa de campo, aprovecha la oportunidad. Por fin podrá relajarse y disfrutar del campo, que tanto le gusta, mientras su hermana se las arregla para librarse de las atenciones del guapo heredero de Edenbrooke. Sin embargo, Marianne acabará por descubrir que incluso los mejores planes pueden salir mal: primero será un aterrador encuentro con un salteador de caminos, después un coqueteo aparentemente inofensivo... el caso es que, al final, Marianne se verá envuelta en una inesperada aventura llena de intriga y de amor, tan apasionante que no podrá dar descanso a su mente. ¿Será capaz de controlar su corazón traidor o caerá rendida ante un misterioso desconocido?
""",
4:"""
Editorial: Editorial Planeta
Temática: Novela contemporánea
Colección: (Fuera de colección)
País de publicación: España

Lucas es familiar, impulsivo y transparente.
Juliette es fuerte, introspectiva y liberal.
Él vive en Vallecas, trabaja en un taller de coches junto a su mejor amigo y por las tardes tocan en un grupo de música que marcará el curso de sus vidas para siempre.
Ella ha crecido con su abuela en un barrio acomodado, pero sueña con ser independiente, volar alto y dejar huella en el corazón de alguien.
Una noche de 1978, en pleno estallido de la movida madrileña, sus caminos se cruzan. Entonces surge la atracción, el deseo, el amor. Un amor radiactivo que lo arrolla todo a su paso mientras los dos se vuelven inseparables en un ambiente desenfrenado lleno de cambios, atrapados entre el éxito y el fracaso, la luz y la oscuridad, el perdón y el orgullo.
Pero Lucas es imperfecto.
Y Juliette guarda secretos.
¿Es eterna la pasión? ¿Se pueden olvidar la mentira y la traición sin que queden esquirlas?
""",
5:"""
Título original: The Bronze Horseman
Editorial: Mondadori
Año publicación: 2002 (2000)
Temas: Romántica
Nota media: 8 / 10 (21 votos)

Leningrado, 1941: la guerra parece lejana en esta ciudad de antigua grandeza, donde espléndidos palacios y avenidas señoriales hablan de otra época, cuando la ciudad era conocida como San Petersburgo.Dos hermanas Tatiana y Dasha Metanov, comparten un minúsculo apartamento con su familia. La vida es dura, pero todavía hay cabida para soñar y amar.Todo cambia cuando un comunicado de la radio informa que Alemania ha invadido la URSS. Ese día Tatiana conoce a Alexander, un joven oficial del Ejército Rojo de misterioso y turbulento pasado.Tatiana siente que se embarca en un camino de amor tortuoso, de sacrificio y negación, pues Dasha también está enamorada de Alexander. Cuando el ejército alemán bloquea la ciudad en el duro invierno, los amantes se encontrarán atrapados en los vaivenes de la historia, y deberán entablar tina indómita lucha para realizar su amor y lograr la libertad.
""",
}
sus_lib={
1:"""
Editorial: DEBOLSILLO
Año de edición:2014
Materia: Thriller / novela negra / policiaca
ISBN: 978-84-9032-837-8
Páginas: 576
Encuadernación: Rústica
Colección: BEST SELLER ( 9032 )

Sinopsis
No pierdas el tren. Perdida es tu próxima parada.
El libro que se ha convertido en un referente del thriller psicológico contemporáneo.En un caluroso día de verano, Amy y Nick se disponen a celebrar su quinto aniversario de bodas en North Carthage, a orillas del río Mississippi. Pero Amy desaparece esa misma mañana sin dejar rastro. A medida que la investigación policial avanza las sospechas recaen sobre Nick. Sin embargo, este insiste en su inocencia. Es cierto que se muestra extrañamente evasivo y frío, pero ¿es capaz de matar?Perdida es una obra maestra, un thriller psicológico brillante con una trama tan apasionante y giros tan inesperados que es imposible parar de leer. Una novela sobre el lado más oscuro del matrimonio; los engaños, las decepciones, la obsesión, el miedo. Una radiografía actual de los medios de comunicación y su capacidad para modelar la opinión pública. Pero sobre todo es la historia de amor entre dos personas perdidamente enamoradas.
""",
2:"""
Editorial: DEBOLSILLO
Formato: Libro
Presentación: Tapa blanda
ISBN: 9789585433922
Autores: JOEL DICKER
Categoría: Policiaca

La verdad sobre el caso Harry Quebert. Por Joël Dicker. Quién mató a Nola Kallergan es la gran incógnita a desvelar en este thriller incomparable cuya experiencia de lectura escapa a cualquier tentativa de descripción. Intentémoslo: una gran novela policíaca y romántica a tres tiempos —1975, 1998 y 2008— acerca del asesinato de una joven de quince años en la pequeña ciudad de Aurora, en New Hampshire. En 2008, Marcus Goldman, un joven escritor, visita a su mentor —Harry Quebert, autor de una aclamada novela—, y descubre que éste tuvo una realción secreta con Nola Kellergan. Poco después, Harry es arrestado y acusado de asesinato, al encontrarse el cadáver de Nola enterrado en su jardín. Marcus comienza a investigar y a escribir un libro sobre el caso. Mientras intenta demostrar la inocencia de Harry, una trama de secretos a la luz. La verdad solo llega al final de un largo, intrincado y apasionante recorrido.
""",
3:"""
Editorial: Booket
Temática: Novela contemporánea
Colección: Fuera de colección
Número de páginas: 572

Un amanecer de 1945, un muchacho es conducido por su padre a un misterioso lugar oculto en el corazón de la ciudad vieja: el Cementerio de los Libros Olvidados. Allí, Daniel Sempere encuentra un libro maldito que cambia el rumbo de su vida y le arrastra a un laberinto de intrigas y secretos enterrados en el alma oscura de la ciudad. La Sombra del Viento es un misterio literario ambientado en la Barcelona de la primera mitad del siglo xx, desde los últimos esplendores del Modernismo hasta las tinieblas de la posguerra.

Aunando las técnicas del relato de intriga y suspense, la novela histórica y la comedia de costumbres, La Sombra del Viento es sobre todo una trágica historia de amor cuyo eco se proyecta a través del tiempo. Con gran fuerza narrativa, el autor entrelaza tramas y enigmas a modo de muñecas rusas en un inolvidable relato sobre los secretos del corazón y el embrujo de los libros cuya intriga se mantiene hasta la última página.
""",
4:"""
stockEditorial: DEBOLSILLO
Año de edición: 2019
Materia Bolsillo
ISBN: 978-84-663-4792-1
Páginas: 1504
Encuadernación: Rústica
Colección: Bestseller

¿Quién o qué mutila y mata a los niños de un pequeño pueblo norteamericano?
¿Por qué llega cíclicamente el horror a Derry en forma de un payaso siniestro que va sembrando la destrucción a su paso? Esto es lo que se proponen averiguar los protagonistas de esta novela. Tras veintisiete años de tranquilidad y lejanía, una antigua promesa infantil les hace volver al lugar en el que vivieron su infancia y juventud como una terrible pesadilla. Regresan a Derry para enfrentarse con su pasado y enterrar definitivamente la amenaza que los amargó durante su niñez. Saben que pueden morir, pero son conscientes de que no conocerán la paz hasta que aquella cosa sea destruida para siempre. It es una de las novelas más ambiciosas de Stephen King, con la que ha logrado perfeccionar de un modo muy personal las claves del género de terror. La crítica ha dicho...
""",
5:"""
Título alternativo: Trilogia de la Ciudad Blanca 1
Editorial: Planeta
Año publicación: 2016
Temas: Misterio y suspense
Nota media: 8 / 10 (64 votos)

Tasio Ortiz de Zárate, el brillante arqueólogo condenado por los asesinatos que aterrorizaron Vitoria hace dos décadas, está a punto de salir de prisión cuando los crímenes se reanudan. En la Catedral Vieja, una pareja de veinte años aparece muerta por picaduras de abeja en la garganta. Pero solo serán los primeros.
Unai López de Ayala, un joven experto en perfiles criminales, está obsesionado con prevenir los crímenes, una tragedia personal no le permite encarar el caso como uno más. Sus métodos enervan a Alba, la subcomisaria, con la que mantiene una ambigua relación marcada por los crímenes… pero el tiempo corre en su contra y la amenaza acecha en cualquier esquina. ¿Quién será el siguiente?

Una novela negra absorbente que mezcla mitología y leyendas, arqueología y secretos de familia. Elegante. Compleja. Hipnótica.
""",

}

terr_lib_content={
1:"""
Título: Hex
Autor: Thomas Olde
Género: Terror
Año de publicación: 2020
Editorial: Nocturna
Saga: No
Número de páginas: 512
PVP: 19,50€
ISBN: 978-84-17834-52-4

Sinopsis del libro Hex
Bienvenido a Black Spring, una población pintoresca con un macabro secreto: una mujer recorre las calles con la boca y los ojos cosidos, entra en los hogares y espía a la gente mientras duerme.

La llaman la Bruja de Black Rock.

Los vecinos se han acostumbrado tanto a su presencia que a veces se les olvida lo que ocurrirá si algún día abre los ojos. Para protegerse de curiosos, los fundadores de Black Spring han instalado equipos de vigilancia con los que mantienen la zona en cuarentena. Hasta que unos adolescentes, hartos de su aislamiento, deciden saltarse las normas y convertir la maldición en una experiencia viral.

Nadie se imagina la siniestra pesadilla que entonces los aguarda.""",


2:"""
Idioma original: inglés
Título original: The Girl Next Door
Año de publicación: 1989
Valoración: recomendable

La chica de al lado comienza como algunas novelas de Stephen King: ambientada en los años 50, es verano y un grupo de niños pasan el tiempo jugando, viendo la televisión, bebiendo Coca-cola, etc. Los niños (entre ellos, David, el narrador de la historia) rondan los trece años y beben los vientos por Meg, una chica que acaba de llegar al vecindario con su hermana pequeña, Susan, a vivir con su tía y sus primos. Y ahora es cuando todos esperamos que ocurra algo sobrenatural, que los niños vivan una experiencia terrible, pero que salgan sanos y salvos (al menos, la mayoría de ellos) de la misma y puedan llegar a la edad adulta con más o menos taras mentales.""",

3:"""
Editorial: Booket
Temática: Terror
Colección: Terror
Número de páginas: 416

Algunas puertas deberían permanecer cerradas... En Barrington House, un elegante bloque de pisos londinense, hay un apartamento vacío. Nadie entra, nadie sale. Y ha permanecido así durante cincuenta años. Hasta que una noche el vigilante oye unos ruidos después de medianoche y decide ir a investigar. Lo que experimenta allí basta para cambiar su vida para siempre. La joven Apryl llega a Barrington House procedente de Estados Unidos. Ha heredado un apartamento de su misteriosa tía abuela Lillian, fallecida en extrañas circunstancias. Se rumorea que Lillian estaba loca. Pero su diario insinúa que estuvo implicada en un suceso terrible e inexplicable varias décadas atrás. Decidida a averiguar algo sobre esta excéntrica mujer, Apryl comenzará a desentrañar la historia oculta de Barrington House. No tardará demasiado en descubrir que un mal que transforma a la gente aún habita el edificio. Y que la puerta del apartamento 16 es el acceso a algo mucho más terrorífico...""",
4:"""
Editorial:PLAZA & JANES EDITORES, S.A.
Año de edición:2017
ISBN:978-84-01-01732-2
Páginas:608
Encuadernación:Cartoné
Colección:EXITOS

Stephen King nos presenta en El bazar de los malos sueños una excepcional selección de relatos, algunos nuevos y otros revisados en profundidad. Cada uno viene precedido de su propia introducción, donde habla sobre sus orígenes y sobre los motivos que lo llevaron a escribirlo, incluyendo aspectos autobiográficos.

Aunque han pasado ya treinta y cinco años desde que escribió su primera colección, Stephen King sigue deslumbrándonos con su maestría en el género. En esta ocasión trata temas como la moralidad, la vida después de la muerte, la culpa y lo que corregiríamos del pasado si pudiéramos ver el futuro.""",
5:"""
ENCUADERNACIÓNCartoné con sobrecubierta
FORMATO14x21cm
ISBN978-84-17553-77-7
PÁGINAS384
PRECIO24,50 €
EDICIÓN 1ª COLECCIÓN

A finales del XIX, y durante los primeros años del XX, existió una estirpe de narradoras que revolucionó el panorama del miedo y el terror psicológico con relatos magistrales sobre casas encantadas, apariciones y presencias fantasmales. En esta antología presentamos a dieciséis maestras del escalofrío exquisito; escritoras cuyas narraciones se perdieron en las revistas pulp de principios del siglo pasado y que llegan hasta nosotros con energías renovadoras. Descubriremos así el lado oscuro de Frances Hodgson Burnett, las pesadillas de la atormentada Marie Corelli, la mezcla de espanto y ciencia ficción de Margaret St. Clair, la explosiva combinación de biología y monstruosidad de Sophie Wenzell Ellis, la poética visión del «otro lado» de Leonora Carrington o la sutileza de lady Eleanor Smith al enfrentar magia y sobresalto. Cuentos que rompieron con las barreras del género y que elevaron a sus autoras por encima del papel que la sociedad les asignó como niñas dóciles y sumisas mujeres casaderas."""
}


tipo=biblioteca.get(s_i_e)


if tipo=="terror":
	print("\nElija Libro:\n")
	print("""
1:   Hex de Thomas Olde Heuvelt
2:   La chica de al lado de Jack Ketchum
3:   Apartamento 16 de Adam Nevill
4:   El bazar de los malos sueños (2021) de Stephen King
5:   Reinas del abismo (2020)""")
	int_terr=int(input(" > "))
	lib_terr(int_terr)
	
elif tipo=="suspenso":
	print("\nElija Libro:\n")
	print("""
1: Perdida
2: La verdad sobre el caso Harry Quebert
3: La sombra del viento
4: IT
5: El silencio de la ciudad blanca""")
	int_sus=int(input(" > "))
	lib_sus(int_sus)
	
elif tipo=="romance":
	print("\nElija libro:\n")
	print("""
1: Orgullo y prejuicio
2: El ruiseñor
3: Edenbrooke
4: Tú y yo, invencibles
5: El jinete de bronce

""")
	int_rom=int(input(" > "))
	lib_rom(int_rom)
