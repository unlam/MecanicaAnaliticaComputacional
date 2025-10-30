<!-- LTeX: language=es-AR -->

# Mecánica Analítica Computacional

Aquí se publica el material de enseñanza utilizado en la [asignatura sobre esta temática](https://ingenieria.unlam.edu.ar/preview.php?seccion=3&idArticulo=510) en la carrera de grado en [Ingeniería Mecánica](https://ingenieria.unlam.edu.ar/index.php?seccion=3&idArticulo=371) de la Universidad Nacional de La Matanza.

[![DIIT-UNLaM](figurasLaTeX/ingenieria_logo_schwarz.png)](https://ingenieria.unlam.edu.ar/)
[![CC BY-NC-SA](https://upload.wikimedia.org/wikipedia/commons/1/12/Cc-by-nc-sa_icon.svg)](https://creativecommons.org/licenses/by-nc-sa/4.0/deed.es)
2025 Víctor A. Bettachini

<!--
![](figurasLaTeX/ambos.png)

<a href="https://unlam.github.io/MecanicaAnaliticaComputacional/opener.html" target="_blank">Lanzador de cuadernos Jupyter</a> 

Esta obra está bajo una <a rel="license" href="https://creativecommons.org/licenses/by-nc-sa/4.0/deed.es">Licencia Creative Commons Atribución-NoComercial-CompartirIgual 4.0 Internacional</a>.

<a rel="license" href="https://creativecommons.org/licenses/by-nc-sa/4.0/deed.es"><img alt="Licencia Creative Commons" style="border-width:0" src="https://i.creativecommons.org/l/by-nc-sa/4.0/88x31.png" /></a>

-->


## Descripción general del curso 

Este curso de grado introduce la mecánica analítica a través de métodos computacionales.
Ha sido diseñado para estudiantes de ingeniería con poca o ninguna experiencia en programación.
Los estudiantes aprenden a modelar dispositivos mecánicos como cuerpos rígidos, y a través de las ecuaciones de Euler-Lagrange analizar su dinámica y esfuerzos.


### Material de aprendizaje

Los nuevos temas se presentan en uno o más **[cuadernos Jupyter](https://jupyter.org/)** que combinan:
- Teoría y conceptos de física.
- Herramientas computacionales basadas en **[Python](https://www.python.org/)**.
- Ejemplos prácticos que ilustran el código que realiza todos los cálculos analíticos y numéricos requeridos.

Para cada tema se presenta un PDF con un **conjunto de problemas**.
Sus ejercicios pueden resolverse realizando modificaciones incrementales en el código de los ejemplos proporcionados. De esta forma, el foco del esfuerzo del estudiante se corre de resolver expresiones matemáticas complejas hacia el modelado físico y la interpretación de los resultados.


### Enfoque didáctico

El material del curso se diseñó para un modelo de [**aula invertida**](https://en.wikipedia.org/wiki/Flipped_classroom) en el que los estudiantes:
- Estudian los materiales y realizan los ejercicios antes de las reuniones semanales sincrónicas.
- Plantean sus preguntas y dudas al personal docente en estas reuniones.
- Terminan de resolver los problemas antes de que finalicen estas reuniones.


### Características técnicas

- **No requiere instalación**: ejecución de cuadernos basada en la nube.
- **Código abierto**: se proporcionan incluso las fuentes [LaTeX](https://www.latex-project.org/) de los conjuntos de problemas.
- **Requisitos**
Los cuadernos de este repositorio importan explícitamente las siguientes bibliotecas de Python cuando es necesario:
  - [SymPy](https://www.sympy.org/en/index.html) 1.14.0
  - [NumPy](https://numpy.org/) 2.3.3
  - [SciPy](https://scipy.org/) 1.16.2
  - [Matplotlib](https://matplotlib.org/) 3.10.6


## Ponte en contacto
Si tienes alguna pregunta sobre este curso, no dudes en [abrir una cuestión (issue)](https://github.com/unlam/MecanicaAnaliticaComputacional/issues) en su repositorio de GitHub.
¡Agradecemos los comentarios y sugerencias de la comunidad!



## Cronograma
Los temas del curso están divididos por áreas que pueden abarcar varias semanas.
En _Carpeta semanal_ se indica cuando se continúa con la misma temática.

| Carpeta semanal   | Área                | Temática |
|:------------------|:-------------------:|:----------------|
| 01Vectorial       | Mecánica Newtoniana | Metodología del curso. Análisis vectorial empleando SymPy. |
| 02Energía         | Mecánica analítica  | Coordenadas generalizadas. Energías cinética y potencial. |
| 03EulerLagrange   | "                   | Ecuaciones de Euler-Lagrange. |
| 04Ligaduras       | "                   | Ligaduras como función de coordenadas. |
| 05Simulación      | Numérico            | Resolución numérica de ecuaciones de Euler-Lagrange. |
| 06FuerzaLigadura  | Fuerzas             | Fuerza de ligadura por multiplicadores de Lagrange. |
| 07NoConservativas | "                   | Fuerzas no conservativas en el formalismo de Euler-Lagrange. |
| 08TensorInercia   | Cuerpo rígido       | Tensor de inercia de arreglos de masas puntuales. |
| 09MasaDistribuida | "                   | Tensor de inercia de cuerpos rígidos. |
| 10RotaciónEuler   | "                   | Ecuaciones de Euler para el cuerpo rígido. |
| 11 (continúa 10)  | "                   | **Proyecto final: discusión de su enunciado** |
| 12Vibraciones1GdL | Vibraciones         | Oscilaciones forzadas en sistemas de un grado de libertad. |
| 13VibracionesNGdL | "                   | Modos normales de oscilación en sistemas de múltiples grados de libertad. |
| 14 (continúa 13)  | "                   | " |
| 15Integrador      | Evaluación          | **Defensa del proyecto final** |
| 16 (continúa 15)  | "                   | **2.da oportunidad de defensa** |



### 01 Análisis vectorial
- [Cinemática vectorial](01Vectorial/cinemáticaVectorial.ipynb)
[![Cinemática vectorial](/figurasLaTeX/colab-badge-es.svg)](https://colab.research.google.com/github/unlam/MecanicaAnaliticaComputacional/blob/main/01Vectorial/cinemáticaVectorial.ipynb)
- [Primer guía de ejercicios (pset01) - Cinemática vectorial](01Vectorial/guíaVectorial.pdf)
[![Primer guía de ejercicios (pset01) - Cinemática vectorial](/figurasLaTeX/Icon_pdf-20.svg)](https://github.com/unlam/MecanicaAnaliticaComputacional/raw/refs/heads/main/01Vectorial/gu%C3%ADaVectorial.pdf)
  - Entregar ejercicio pset01e01 una hora tras publicarse. 
  - pset01e02 al inicio del próximo encuentro semanal.
  - Aquellos del pset02, al finalizar tal encuentro (iniciarlos durante la semana).
  - [Como realizar la entrega de ejercicios](01Vectorial/entregaEjercicios.ipynb)
[![Entrega de ejercicios](/figurasLaTeX/colab-badge-es.svg)](https://colab.research.google.com/github/unlam/MecanicaAnaliticaComputacional/blob/main/01Vectorial/entregaEjercicios.ipynb)


### 02 Energía
- [Resumen sobre principios variacionales](02Energía/apunteLanczos.pdf)
[![Resumen sobre principios variacionales](/figurasLaTeX/Icon_pdf-20.svg)](https://github.com/unlam/MecanicaAnaliticaComputacional/raw/refs/heads/main/02Energía/apunteLanczos.pdf)
- [Energía cinética de traslación](02Energía/energíaCinéticaTraslación.ipynb)
[![Energía cinética de traslación](/figurasLaTeX/colab-badge-es.svg)](https://colab.research.google.com/github/unlam/MecanicaAnaliticaComputacional/blob/main/02Energía/energíaCinéticaTraslación.ipynb)
- [Energía potencial gravitatoria](02Energía/energíaPotencialGravitatoria.ipynb)
[![Energía potencial gravitatoria](/figurasLaTeX/colab-badge-es.svg)](https://colab.research.google.com/github/unlam/MecanicaAnaliticaComputacional/blob/main/02Energía/energíaPotencialGravitatoria.ipynb)
- [Guía de ejercicios - Energía](02Energía/guíaEnergía.pdf)
  - pset02e02
  - pset02e03
  - pset02e04


### 03 Ecuaciones de Euler-Lagrange
- [Péndulos](03EulerLagrange/péndulos_eulerLagrange.ipynb)
[![Péndulos](/figurasLaTeX/colab-badge-es.svg)](https://colab.research.google.com/github/unlam/MecanicaAnaliticaComputacional/blob/main/03EulerLagrange/péndulos_eulerLagrange.ipynb)
- [Plantilla para Euler-Lagrange](03EulerLagrange/plantilla_eulerLagrange.ipynb)
[![Plantilla para Euler-Lagrange](/figurasLaTeX/colab-badge-es.svg)](https://colab.research.google.com/github/unlam/MecanicaAnaliticaComputacional/blob/main/03EulerLagrange/plantilla_eulerLagrange.ipynb)
- [Guía de ejercicios - Euler-Lagrange](03EulerLagrange/guíaEulerLagrange.pdf)
[![Guía de ejercicios - Euler-Lagrange](/figurasLaTeX/Icon_pdf-20.svg)](https://github.com/unlam/MecanicaAnaliticaComputacional/raw/refs/heads/main/03EulerLagrange/gu%C3%ADaEulerLagrange.pdf)
  - pset03e01c
  - pset03e02
  - pset03e03
  - pset03e04
    - [Energía potencial elástica](03EulerLagrange/energíaPotencialElástica_eulerLagrange.ipynb)
    [![Energía potencial elástica](/figurasLaTeX/colab-badge-es.svg)](https://colab.research.google.com/github/unlam/MecanicaAnaliticaComputacional/blob/main/03EulerLagrange/energíaPotencialElástica_eulerLagrange.ipynb)
    - [Partes rotantes](03EulerLagrange/partesRotantes_eulerLagrange.ipynb)
    [![Partes rotantes](/figurasLaTeX/colab-badge-es.svg)](https://colab.research.google.com/github/unlam/MecanicaAnaliticaComputacional/blob/main/03EulerLagrange/partesRotantes_eulerLagrange.ipynb)


### 04 Ligaduras
- [Ligaduras como función de coordenadas](04Ligaduras/ligadurasFunción.ipynb)
[![Ligaduras como función de coordenadas](/figurasLaTeX/colab-badge-es.svg)](https://colab.research.google.com/github/unlam/MecanicaAnaliticaComputacional/blob/main/04Ligaduras/ligadurasFunción.ipynb)
- [Máquina de Atwood con ligaduras](04Ligaduras/atwood_Ligaduras.ipynb)
[![Máquina de Atwood con ligaduras](/figurasLaTeX/colab-badge-es.svg)](https://colab.research.google.com/github/unlam/MecanicaAnaliticaComputacional/blob/main/04Ligaduras/atwood_Ligaduras.ipynb)
- [Resolución de sistemas lineales](04Ligaduras/resoluciónSistemasLineales.ipynb)
[![Resolución de sistemas lineales](/figurasLaTeX/colab-badge-es.svg)](https://colab.research.google.com/github/unlam/MecanicaAnaliticaComputacional/blob/main/04Ligaduras/resoluciónSistemasLineales.ipynb)
- [Guía de ejercicios - Ligaduras](04Ligaduras/guíaLigaduras.pdf)
[![Guía de ejercicios - Ligaduras](/figurasLaTeX/Icon_pdf-20.svg)](http://github.com/unlam/MecanicaAnaliticaComputacional/raw/refs/heads/main/04Ligaduras/gu%C3%ADaLigaduras.pdf)
  - pset04e02
  - pset04e03
  - pset04e04


### 05 Simulación
Para visualizar la dinámica de los sistemas hasta aquí modelados, se resuelven ahora sus ecuaciones de Euler-Lagrange con métodos numéricos.
- [Máquina de Atwood: simulación numérica](05Simulación/atwoodSimulación_Resuelto.ipynb)
[![Máquina de Atwood: simulación numérica](/figurasLaTeX/colab-badge-es.svg)](https://colab.research.google.com/github/unlam/MecanicaAnaliticaComputacional/blob/main/05Simulación/atwoodSimulación_Resuelto.ipynb)
- [Péndulo con soporte libre en la dirección horizontal: simulación numérica](05Simulación/pénduloLibre_Simulación_Resuelto.ipynb)
[![Péndulo con soporte libre en la dirección horizontal: simulación numérica](/figurasLaTeX/colab-badge-es.svg)](https://colab.research.google.com/github/unlam/MecanicaAnaliticaComputacional/blob/main/05Simulación/pénduloLibre_Simulación_Resuelto.ipynb)
- [Guía de ejercicios - Simulación](05Simulación/guíaSimulación.pdf)
[![Guía de ejercicios - Simulación](/figurasLaTeX/Icon_pdf-20.svg)](https://github.com/unlam/MecanicaAnaliticaComputacional/raw/refs/heads/main/05Simulación/gu%C3%ADaSimulación.pdf)
  - pset05e02a
  - pset05e02c
  - pset05e03
  - pset05e04
- Referencia
    - [2D and 3D graphics with matplotlib](https://www.github.com/jrjohansson/scientific-python-lectures/blob/master/Lecture-4-Matplotlib.ipynb) [![2D and 3D graphics with matplotlib](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/jrjohansson/scientific-python-lectures/blob/master/Lecture-4-Matplotlib.ipynb)


### 06 Fuerzas de ligadura
Determinar la dinámica de cada parte en un dispositivo es importante, pero es igualmente importante determinar las tensiones que deben soportar.
Comencemos a calcular estos torques y fuerzas.

- [Introducción a las fuerzas de ligadura](06FuerzasLigadura/fuerzasLigadura.ipynb)
[![Introducción a las fuerzas de ligadura](/figurasLaTeX/colab-badge-es.svg)](https://colab.research.google.com/github/unlam/MecanicaAnaliticaComputacional/blob/main/06FuerzasLigadura/fuerzasLigadura.ipynb)
- [Péndulo físico ideal](06FuerzasLigadura/pénduloIdeal_FuerzasLigadura.ipynb)
[![Péndulo físico ideal](/figurasLaTeX/colab-badge-es.svg)](https://colab.research.google.com/github/unlam/MecanicaAnaliticaComputacional/blob/main/06FuerzasLigadura/pénduloIdeal_FuerzasLigadura.ipynb)
- [Rodadura](06FuerzasLigadura/rodadura_FuerzasLigadura.ipynb)
[![Rodadura](/figurasLaTeX/colab-badge-es.svg)](https://colab.research.google.com/github/unlam/MecanicaAnaliticaComputacional/blob/main/06FuerzasLigadura/rodadura_FuerzasLigadura.ipynb)
- [Sistemas no holónomos](06FuerzasLigadura/sistemasNoHolónomos.ipynb)
[![Sistemas no holónomos](/figurasLaTeX/colab-badge-es.svg)](https://colab.research.google.com/github/unlam/MecanicaAnaliticaComputacional/blob/main/06FuerzasLigadura/sistemasNoHolónomos.ipynb)
- [Guía de ejercicios - Fuerzas de ligadura](06FuerzasLigadura/guíaFuerzasLigadura.pdf)
[![Guía de ejercicios - Fuerzas de ligadura](/figurasLaTeX/Icon_pdf-20.svg)](https://github.com/unlam/MecanicaAnaliticaComputacional/raw/refs/heads/main/06FuerzasLigadura/gu%C3%ADaFuerzasLigadura.pdf)
  - pset06e03
  - pset06e04
  - pset06e05


### 07 Fuerzas no conservativas
- [Fuerzas no conservativas y Euler-Lagrange](07NoConservativas/noConservativas.ipynb)
[![Fuerzas no conservativas y Euler-Lagrange](/figurasLaTeX/colab-badge-es.svg)](https://colab.research.google.com/github/unlam/MecanicaAnaliticaComputacional/blob/main/07NoConservativas/noConservativas.ipynb)
- [Guía de ejercicios - Fuerzas no conservativas](07NoConservativas/guíaNoConservativas.pdf)
[![Guía de ejercicios - Fuerzas no conservativas](/figurasLaTeX/Icon_pdf-20.svg)](https://github.com/unlam/MecanicaAnaliticaComputacional/raw/refs/heads/main/07NoConservativas/gu%C3%ADaNoConservativas.pdf)
  - pset07e02
  - pset07e03
    - [Cilindros solidarios](07NoConservativas/cilíndrosSolidarios_noConservativas_ayuda.ipynb)
    [![Cilindros solidarios](/figurasLaTeX/colab-badge-es.svg)](https://colab.research.google.com/github/unlam/MecanicaAnaliticaComputacional/blob/main/07NoConservativas/cilíndrosSolidarios_noConservativas_ayuda.ipynb)
  - pset07e04


### 08 Tensor de inercia
Comenzamos a estudiar sólidos de complejidad creciente.
De igual manera que una fuerza le da más o menos aceleración a distintos cuerpos según sus masas, un torque cambia más o menos la velocidad angular según cómo se distribuye la masa alrededor del eje de rotación.
La relación es más compleja que una simple cantidad escalar como la masa, se trata de un tensor denominado de inercia.
Se calculará dicho tensor de figuras geométricas simples, para luego avanzar a trabajar sobre dispositivos mecánicos más realistas.

- [Momento angular y torque](08TensorInercia/momentoAngularTorque.ipynb)
[![Momento angular y torque](/figurasLaTeX/colab-badge-es.svg)](https://colab.research.google.com/github/unlam/MecanicaAnaliticaComputacional/blob/main/08TensorInercia/momentoAngularTorque.ipynb)
- [Tensor de inercia](08TensorInercia/tensorInercia.ipynb)
[![Tensor de inercia](/figurasLaTeX/colab-badge-es.svg)](https://colab.research.google.com/github/unlam/MecanicaAnaliticaComputacional/blob/main/08TensorInercia/tensorInercia.ipynb)
- [Monóxido de carbono](08TensorInercia/monóxidoCarbono_tensorInercia.ipynb)
[![Monóxido de carbono](/figurasLaTeX/colab-badge-es.svg)](https://colab.research.google.com/github/unlam/MecanicaAnaliticaComputacional/blob/main/08TensorInercia/monóxidoCarbono_tensorInercia.ipynb)
- [Guía de ejercicios - Tensor de inercia](08TensorInercia/guíaTensorInercia.pdf)
[![Guía de ejercicios - Tensor de inercia](/figurasLaTeX/Icon_pdf-20.svg)](https://github.com/unlam/MecanicaAnaliticaComputacional/raw/refs/heads/main/08TensorInercia/gu%C3%ADaTensorInercia.pdf)
  - pset08e02
  - pset08e04
  - pset08e05


### 09 Masa distribuida
- [Masa distribuida](09MasaDistribuida/masaDistribuida.ipynb)
[![Masa distribuida](/figurasLaTeX/colab-badge-es.svg)](https://colab.research.google.com/github/unlam/MecanicaAnaliticaComputacional/blob/main/09MasaDistribuida/masaDistribuida.ipynb)
- [Tensor de inercia de un cubo](09MasaDistribuida/cubo_tensorInercia.ipynb)
[![Tensor de inercia de un cubo](/figurasLaTeX/colab-badge-es.svg)](https://colab.research.google.com/github/unlam/MecanicaAnaliticaComputacional/blob/main/09MasaDistribuida/cubo_tensorInercia.ipynb)
- [Guía de ejercicios - Masa distribuida](09MasaDistribuida/guíaDistribuciónMasa.pdf)
[![Guía de ejercicios - Masa distribuida](/figurasLaTeX/Icon_pdf-20.svg)](https://github.com/unlam/MecanicaAnaliticaComputacional/raw/refs/heads/main/09MasaDistribuida/gu%C3%ADaDistribuci%C3%B3nMasa.pdf)
  - pset09e01
  - pset09e02
  - pset09e03
  - pset09e04


### 10 Ecuaciones de Euler para la rotación
- [Ecuaciones de Euler](10RotaciónEuler/ecuacionesEuler.ipynb)
[![Ecuaciones de Euler](/figurasLaTeX/colab-badge-es.svg)](https://colab.research.google.com/github/unlam/MecanicaAnaliticaComputacional/blob/main/10RotaciónEuler/ecuacionesEuler.ipynb)
- [Engranaje desalineado](10RotaciónEuler/engranajeDesalineado.ipynb)
[![Engranaje desalineado](/figurasLaTeX/colab-badge-es.svg)](https://colab.research.google.com/github/unlam/MecanicaAnaliticaComputacional/blob/main/10RotaciónEuler/engranajeDesalineado.ipynb)
- [Guía de ejercicios - Ecuaciones de Euler](10RotaciónEuler/guíaRotacionEuler.pdf)
[![Guía de ejercicios - Ecuaciones de Euler](/figurasLaTeX/Icon_pdf-20.svg)](https://github.com/unlam/MecanicaAnaliticaComputacional/raw/refs/heads/main/10RotaciónEuler/gu%C3%ADaRotacionEuler.pdf)
  - pset10e02
  - pset10e03
  - pset10e05


### 12 Vibraciones con 1 grado de libertad
- [Oscilaciones amortiguadas](11Vibraciones1GdL/vibraciones1GdL.ipynb)
[![Oscilaciones amortiguadas](/figurasLaTeX/colab-badge-es.svg)](https://colab.research.google.com/github/unlam/MecanicaAnaliticaComputacional/blob/main/11Vibraciones1GdL/vibraciones1GdL.ipynb)
- [Forzado armónico](11Vibraciones1GdL/armónico1GdL.ipynb)
[![Forzado armónico](/figurasLaTeX/colab-badge-es.svg)](https://colab.research.google.com/github/unlam/MecanicaAnaliticaComputacional/blob/main/11Vibraciones1GdL/armónico1GdL.ipynb)
- [Forzado arbitrario](11Vibraciones1GdL/arbitrario1GdL.ipynb)
[![Forzado arbitrario](/figurasLaTeX/colab-badge-es.svg)](https://colab.research.google.com/github/unlam/MecanicaAnaliticaComputacional/blob/main/11Vibraciones1GdL/arbitrario1GdL.ipynb)
- [Guía de ejercicios - Vibraciones con 1 grado de libertad](11Vibraciones1GdL/guíaVibraciones1GdL.pdf)
[![Guía de ejercicios - Vibraciones con 1 grado de libertad](/figurasLaTeX/Icon_pdf-20.svg)](https://github.com/unlam/MecanicaAnaliticaComputacional/raw/refs/heads/main/11Vibraciones1GdL/gu%C3%ADaVibraciones1GdL.pdf)
  - pset12e01
  - pset12e02
  - pset12e03
  - pset12e04


### 13 Vibraciones con múltiples grados de libertad
- [Oscilaciones con múltiples grados de libertad](12VibracionesNGdL/vibracionesNGdL.ipynb)
[![Oscilaciones con múltiples grados de libertad](/figurasLaTeX/colab-badge-es.svg)](https://colab.research.google.com/github/unlam/MecanicaAnaliticaComputacional/blob/main/12VibracionesNGdL/vibracionesNGdL.ipynb)
- [Guía de ejercicios - Vibraciones con múltiples grados de libertad](12Vibraciones
NGdL/guíaVibracionesNGdL.pdf)
[![Guía de ejercicios - Vibraciones con múltiples grados de libertad](/figurasLaTeX/Icon_pdf-20.svg)](https://github.com/unlam/MecanicaAnaliticaComputacional/raw/refs/heads/main/12VibracionesNGdL/gu%C3%ADaVibracionesNGdL.pdf)
  - pset13e01
  - pset13e02


### 15 Trabajo integrador
- [Integrador: cuerpo rígido bajo fuerzas externas](15Integrador/integradorRígido.ipynb)
[![Integrador: cuerpo rígido bajo fuerzas externas](/figurasLaTeX/colab-badge-es.svg)](https://colab.research.google.com/github/unlam/MecanicaAnaliticaComputacional/blob/main/15Integrador/integradorRígido.ipynb)


## Bibliografía

### Principal 
Los fundamentos teóricos empleados en este curso se explican en forma completa en: 
- Lev Davidovich Landau y E. M. Lifshitz, _Mecánica - Curso de física teórica_ (Reverté, Barcelona, Estado Español, 2.a edición, 1994)

Los siguientes libros son recomendados como material complementario sobre los temas indicados.

### Mecánica vectorial 

- Ferdinand Pierre Beer, E. Russell Johnston, y Elliot R Eisenberg, _Mecánica vectorial para ingenieros -_
    - _Dinámica_ (McGraw-Hill, México DF, México, 9.a. edición, 2010)
    - _Estática_ (McGraw-Hill, México DF, México, 9.a edición 2010)
- W. Moebs et al., [_Física universitaria - Volúmen 1_](https://openstax.org/details/books/f%C3%ADsica-universitaria-volumen-1)
 (OpenStax, Houston, Estados Unidos de América, 2021)
- S. Alrasheed, [_Principles of Mechanics_](https://doi.org/10.1007/978-3-030-15195-9) (Springer Cham, Cham, Confederación Suiza, 1.a edición, 2019)


### Mecánica analítica y vectorial

- S. M. Targ, _Curso breve de mecánica teórica_ (Mir, Moscú, Unión de Repúblicas Socialistas Soviéticas, 2.a edición, 1976)


### Mecánica analítica

- Cornelius Lanczos, _The Variational Principles of Mechanics_ (University of Toronto press, 1952).
- Douglas Cline, [_Variational Principles in Classical Mechanics_](http://classicalmechanics.lib.rochester.edu/) (University of Rochester River Campus Libraries, Rochester, Estados Unidos de América, 3rd ed., 2021)
- John Robert Taylor, _Mecánica Clásica_ (Reverté, Barcelona, Estado Español, 1.a. edición, 2018)
- Jerry B. Marion, _Dinámica clásica de las partículas y sistemas_ (Reverté, Barcelona, Estado Español, 2.a. edición, 1975)


## Referencia

### Académica
- [Temática](https://github.com/unlam/MecanicaAnaliticaComputacional/blob/main/acad%C3%A9mico/tem%C3%A1tica.ipynb)
[![Temática](/figurasLaTeX/colab-badge-es.svg)](https://colab.research.google.com/github/unlam/MecanicaAnaliticaComputacional/blob/main/acad%C3%A9mico/tem%C3%A1tica.ipynb)  
- [Metodología](https://github.com/unlam/MecanicaAnaliticaComputacional/blob/main/acad%C3%A9mico/metodolog%C3%ADa.ipynb)
[![Metodología](/figurasLaTeX/colab-badge-es.svg)](https://colab.research.google/github/unlam/MecanicaAnaliticaComputacional/blob/main/acad%C3%A9mico/metodolog%C3%ADa.ipynb)
- [Cronograma](https://github.com/unlam/MecanicaAnaliticaComputacional/blob/main/acad%C3%A9mico/cronograma.md)
- [Programa analítico](https://github.com/unlam/MecanicaAnaliticaComputacional/blob/main/acad%C3%A9mico/programa.pdf)
- [Textos de referencia](https://github.com/unlam/MecanicaAnaliticaComputacional/blob/main/acad%C3%A9mico/bibliograf%C3%ADa.md)


### Informática
- [Lo básico para aprovechar Python](https://www.github.com/unlam/MecanicaAnaliticaComputacional/blob/main/acad%C3%A9mico/introducci%C3%B3nPython.ipynb)
[![Lo básico para aprovechar Python](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/unlam/MecanicaAnaliticaComputacional/blob/main/acad%C3%A9mico/introducci%C3%B3nPython.ipynb)
- [Anotaciones en cuadernos Jupyter: Markdown y LaTeX](https://www.github.com/unlam/MecanicaAnaliticaComputacional/blob/main/acad%C3%A9mico/markdownLaTeX.ipynb)
[![Anotaciones en cuadernos Jupyter: Markdown y LaTeX](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/unlam/MecanicaAnaliticaComputacional/blob/main/acad%C3%A9mico/markdownLaTeX.ipynb)
- [Incluir imágenes en cuadernos Jupyter](https://www.github.com/unlam/MecanicaAnaliticaComputacional/blob/main/acad%C3%A9mico/incluirIm%C3%A1genes.ipynb)
[![Incluir imágenes en cuadernos Jupyter](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/unlam/MecanicaAnaliticaComputacional/blob/main/acad%C3%A9mico/incluirIm%C3%A1genes.ipynb)
- [Otros aspectos del Python](https://www.github.com/unlam/MecanicaAnaliticaComputacional/blob/main/informática/másPython.ipynb)
[![Otros aspectos del Python](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/unlam/MecanicaAnaliticaComputacional/blob/main/informática/másPython.ipynb)

