# 🕹️ Juego Primer Semestre / Lógica de Programación

# Piedra, Papel o Tijera - Juego 

# 🎮 Descripción

Este proyecto es un juego interactivo por consola, desarrollado en lenguaje de programación Python desarrollado en el editor de código Visual Studio Code, permite al jugador enfrentarse a la computadora o jugar en modo miltijugador en una o varias partidas de piedra, papel o tijera. El diseño incluye un menú principal y toma de decisiones basadas en entradas válidas seleccionadas por el jugador, siguiendo un flujo previamente diseñado en Visio el cual esta adjunto en el repositorio de github. 

# 📌 Objetivo:

Implementar un juego popular con el cual se practique los conocimientos previamente adquiridos como estructuras condicionales, ingreso de datos, métodos de cadena, operadores lógicos, diccionarios, tuplas, listas, manejo de errores con try-except, interacción con el usuario desde la terminal y el uso de estructuras de control como bucles en el lenguaje de programación Python.

# 🛠️ Requisitos Técnicos:

• Python 3.+

• Biblioteca estándar random (incluida por defecto en el editor de código).

# 📂 Cómo jugar:

 • Ejecuta el archivo Python en tu consola:

 • Elige una opción del menú principal:

1. Jugar

 • Jugar contra la computadora

 - Se solicita el nombre del jugador.

 - Se pregunta si desea jugar un número específico de rondas.

 - El sistema ejecuta las partidas contra la computadora.

 - Al finalizar, se almacenan los resultados

 • Multijugador

 - Ambos jugadores ingresan sus nombres.

 - Las elecciones de cada uno no se muestran durante el ingreso para mantener la confidencialidad.

 - El sistema anuncia el ganador de cada partida y guarda los resultados.

2. Ver estadísticas de la última partida

 • Se muestran el resumen y conteo de rondas ganadas, perdidas o empatadas.

 • Si no se han jugado partidas, el sistema indicará que no hay estadísticas recientes.

 • Las estadísticas se reinician al comenzar un nuevo conjunto de partidas.

 • Estadísticas: (Última partida)

Jugador 1: ganó 1, perdió 1, empató 1
PC / Jugador 2: ganó 1, perdió 1, empató 1

3. Reglas del juego

 • Piedra gana a Tijera, la piedra aplasta la tijera"

 • Papel gana a Piedra, el papel envuelve la piedra"

 • Tijera gana a Papel, la tijera corta el papel"

 • Empate, si ambos jugadores eligen la misma opción, se repite la ronda hasta que haya un ganador."

4. Salir

 • Termina el juego y presenta el mensaje: ¡Hasta la próxima!"

# 📜 Lógica del juego (resumen del flujograma):

El programa sigue una lógica clara y previamente estructurada, dirigida por un menú principal. A continuación, 
se describe el flujo de decisiones que toma el usuario y cómo interactua con el sistema:

```INICIO
│
├─► Mostrar MENÚ PRINCIPAL
│     ├─ 1. Jugar
│     ├─ 2. Ver estadísticas
│     ├─ 3. Reglas del juego
│     └─ 4. Salir
│
├─► Si elige JUGAR:
│     ├─► Mostrar submenú:
│     │     ├─ 1. Contra la PC
│     │     └─ 2. Multijugador
│     │
│     ├─► Pedir nombres de los jugadores
│     ├─► Preguntar: ¿Cuántas partidas desea jugar?
│     └─► Bucle de N partidas:
│           ├─ Jugador 1 elige opción (PIEDRA, PAPEL o TIJERA)
│           ├─ Jugador 2 (o PC) elige opción
│           ├─ Determinar resultado
│           └─ Guardar resultado en historial
│
├─► Si elige VER ESTADÍSTICAS:
│     ├─► ¿Hay historial?
│     │     ├─ Sí → Mostrar resumen de partidas y estadísticas
│     │     └─ No → Mostrar mensaje de “No hay estadísticas recientes”
│
├─► Si elige REGLAS DEL JUEGO:
│     └─► Mostrar explicación de las reglas del juego
│
├─► Si elige SALIR:
│     └─► Finalizar el programa
│
└──► FIN``` 

# 🧠 Concluciones: 

1. Comprensión sólida de la lógica condicional: La mecánica del juego “Piedra, Papel o Tijera” se basa en tomar decisiones según reglas claras. Las cuales se implemenó con estructuras condicionales reforzando cómo pensar algorítmicamente, usando if, elif, y else de forma eficiente.

2.  Control del flujo del programa: Con el uso de bucles como (while, for) y validaciones, se aprendió cómo mantener un programa en funcionamiento continuo, pidiendo entradas válidas y permitiendo repetir acciones como jugar otra partida o salir.

3. Interacción con el usuario: El código guía al usuario paso a paso, solicita entradas de forma clara y maneja errores con mensajes predeterminados para el ingreso validó de datos. 

4. Gestión de datos y estadísticas: Guarda y muestra resultados de partidas jugadas con anterioridad, nos exigió usar estructuras de datos como listas y diccionarios, fundamentales para proyectos más grandes a un corto y largo plazo. 

5. . Modularidad y organización del código: Separar el juego en funciones (jugar_modo, jugar_partida, mostrar_estadisticas, etc.) demuestra la comprensión del diseño estructurado. Esto es esencial para hacer que el código sea reutilizable, legible y fácil de mantener.

Este juego me enseño cómo diseñar un problema en un flujograma que luego se convirtio en código funcional. Aunque parezca un proyecto simple, abarca muchos de los fundamentos clave que se necesitará como programador. Además, me dio una base sólida para proyectos más complejos ya que que ayudo a desarrollar un pensamiento lógico y estructurado potenciando la creatividad. 

# 📈 Créditos:

Desarrollado por: Roger Ordoñez

# ▶️ Recursos relacionados:

• Diagrama de Arquitectura.pdf

• Flujograma Piedra-Papel-Tijera.pdf

# ▶️ Links relacionados:

• Link repositorio: https://github.com/RogerSteven1104/JUEGO_PrimerSemestre.git

• Link video: https://mailinternacionaledu-my.sharepoint.com/:v:/g/personal/roordonezqu_uide_edu_ec/EY1vqNmOZ09HopyTdqMVDmIBbKCUrJZBRohgLZGH4mFe4g?e=4vR8fc&nav=eyJyZWZlcnJhbEluZm8iOnsicmVmZXJyYWxBcHAiOiJTdHJlYW1XZWJBcHAiLCJyZWZlcnJhbFZpZXciOiJTaGFyZURpYWxvZy1MaW5rIiwicmVmZXJyYWxBcHBQbGF0Zm9ybSI6IldlYiIsInJlZmVycmFsTW9kZSI6InZpZXcifX0%3D 

