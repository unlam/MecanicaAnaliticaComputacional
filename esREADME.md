<!-- LTeX: language=es-AR -->

# Mecánica Analítica Computacional

Todo el material de enseñanza utilizado en la asignatura [Mecánica Analítica Computacional](https://ingenieria.unlam.edu.ar/preview.php?seccion=3&idArticulo=510) de la carrera de grado en [Ingeniería Mecánica](https://ingenieria.unlam.edu.ar/index.php?seccion=3&idArticulo=371) de la Universidad Nacional de La Matanza está publicado aquí.

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
| 11 (continúa 10)  | "                   | **Proyecto final: enunciado del problema** |
| 12Vibraciones1GdL | Vibraciones         | Oscilaciones forzadas en sistemas de un grado de libertad. |
| 13VibracionesNGdL | "                   | Modos normales de oscilación en sistemas de múltiples grados de libertad. |
| 14 (continúa 13)  | "                   | " |
| 15Integrador      | Evaluación          | **Defensa del proyecto final** |
| 16 (continúa 15)  | "                   | **2.da oportunidad de defensa** |



### 01 Análisis vectorial
- [Cinemática vectorial](01Vectorial/cinemáticaVectorial.ipynb)
[![Cinemática vectorial](/figurasLaTeX/colab-badge-es.svg)](https://colab.research.google.com/github/unlam/MecanicaAnaliticaComputacional/blob/main/01Vectorial/cinemáticaVectorial.ipynb) |

| Contenido                 | Enlace |
|---------------------------------|------|
| Cinemática vectorial | [![clase_1](/figurasLaTeX/colab-badge-es.svg)](https://colab.research.google.com/github/unlam/MecanicaAnaliticaComputacional/blob/main/01Vectorial/cinemáticaVectorial.ipynb) |
| Guía de ejercicios | [![clase_1](/figurasLaTeX/Icon_pdf-20.svg)](https://github.com/unlam/MecanicaAnaliticaComputacional/blob/main/01Vectorial/guíaVectorial.pdf) |
| Entrega de ejercicios | [![clase_1](/figurasLaTeX/colab-badge-es.svg)](https://colab.research.google.com/github/unlam/MecanicaAnaliticaComputacional/blob/main/01Vectorial/entregaEjercicios.ipynb) |


### 02 Energía

| Contenido                 | Enlace |
|---------------------------------|------|
| Resumen sobre principios variacionales | [![clase_2](/figurasLaTeX/Icon_pdf-20.svg)](https://github.com/unlam/MecanicaAnaliticaComputacional/blob/main/02Energía/apunteLanczos.pdf) |
| Energía cinética de traslación | [![clase_2](/figurasLaTeX/colab-badge-es.svg)](https://colab.research.google.com/github/unlam/MecanicaAnaliticaComputacional/blob/main/02Energía/energíaCinéticaTraslación.ipynb) |
| Energía potencial gravitatoria | [![clase_2](/figurasLaTeX/colab-badge-es.svg)](https://colab.research.google.com/github/unlam/MecanicaAnaliticaComputacional/blob/main/02Energía/energíaPotencialGravitatoria.ipynb) |
| Guía de ejercicios | [![clase_2](/figurasLaTeX/Icon_pdf-20.svg)](https://github.com/unlam/MecanicaAnaliticaComputacional/blob/main/02Energía/guíaEnergía.pdf) |


### 03 Ecuaciones de Euler-Lagrange

| Contenido                 | Enlace |
|---------------------------------|------|
| Péndulos | [![clase_3](/figurasLaTeX/colab-badge-es.svg)](https://colab.research.google.com/github/unlam/MecanicaAnaliticaComputacional/blob/main/03EulerLagrange/péndulos_eulerLagrange.ipynb) |
| Plantilla para Euler-Lagrange | [![clase_3](/figurasLaTeX/colab-badge-es.svg)](https://colab.research.google.com/github/unlam/MecanicaAnaliticaComputacional/blob/main/03EulerLagrange/plantilla_eulerLagrange.ipynb) |
| Guía de ejercicios | [![clase_3](/figurasLaTeX/Icon_pdf-20.svg)](https://github.com/unlam/MecanicaAnaliticaComputacional/blob/main/03EulerLagrange/guíaEulerLagrange.pdf) |
| Energía potencial elástica | [![clase_3](/figurasLaTeX/colab-badge-es.svg)](https://colab.research.google.com/github/unlam/MecanicaAnaliticaComputacional/blob/main/03EulerLagrange/energíaPotencialElástica_eulerLagrange.ipynb) |
| Partes rotantes | [![clase_3](/figurasLaTeX/colab-badge-es.svg)](https://colab.research.google.com/github/unlam/MecanicaAnaliticaComputacional/blob/main/03EulerLagrange/partesRotantes_eulerLagrange.ipynb) |


### 04 Ligaduras

| Contenido                 | Enlace |
|---------------------------------|------|
| Función de ligadura | [![clase_4](/figurasLaTeX/colab-badge-es.svg)](https://colab.research.google.com/github/unlam/MecanicaAnaliticaComputacional/blob/main/04Ligaduras/ligadurasFunción.ipynb) |
| Máquina de Atwood | [![clase_4](/figurasLaTeX/colab-badge-es.svg)](https://colab.research.google.com/github/unlam/MecanicaAnaliticaComputacional/blob/main/04Ligaduras/atwood_Ligaduras.ipynb) |
| Resolución de sistemas lineales | [![clase_4](/figurasLaTeX/colab-badge-es.svg)](https://colab.research.google.com/github/unlam/MecanicaAnaliticaComputacional/blob/main/04Ligaduras/resoluciónSistemasLineales.ipynb) |
| Guía de ejercicios | [![clase_4](/figurasLaTeX/Icon_pdf-20.svg)](https://github.com/unlam/MecanicaAnaliticaComputacional/blob/main/04Ligaduras/guíaLigaduras.pdf) |


### 05 Simulación

| Contenido                 | Enlace |
|---------------------------------|------|
| Máquina de Atwood | [![clase_5](/figurasLaTeX/colab-badge-es.svg)](https://colab.research.google.com/github/unlam/MecanicaAnaliticaComputacional/blob/main/05Simulación/atwoodSimulación_Resuelto.ipynb) |
| Péndulo con soporte libre en la dirección horizontal | [![clase_5](/figurasLaTeX/colab-badge-es.svg)](https://colab.research.google.com/github/unlam/MecanicaAnaliticaComputacional/blob/main/05Simulación/pénduloLibre_Simulación_Resuelto.ipynb) |
| Guía de ejercicios | [![clase_5](/figurasLaTeX/Icon_pdf-20.svg)](https://github.com/unlam/MecanicaAnaliticaComputacional/blob/main/05Simulación/guíaSimulación.pdf) |


### 06 Fuerzas de ligadura

| Contenido                 | Enlace |
|---------------------------------|------|
| Fuerzas de ligadura | [![clase_6](/figurasLaTeX/colab-badge-es.svg)](https://colab.research.google.com/github/unlam/MecanicaAnaliticaComputacional/blob/main/06FuerzasLigadura/fuerzasLigadura.ipynb) |
| Péndulo físico ideal | [![clase_6](/figurasLaTeX/colab-badge-es.svg)](https://colab.research.google.com/github/unlam/MecanicaAnaliticaComputacional/blob/main/06FuerzasLigadura/pénduloIdeal_FuerzasLigadura.ipynb) |
| Rodadura | [![clase_6](/figurasLaTeX/colab-badge-es.svg)](https://colab.research.google.com/github/unlam/MecanicaAnaliticaComputacional/blob/main/06FuerzasLigadura/rodadura_FuerzasLigadura.ipynb) |
| Sistemas no holónomos | [![clase_6](/figurasLaTeX/colab-badge-es.svg)](https://colab.research.google.com/github/unlam/MecanicaAnaliticaComputacional/blob/main/06FuerzasLigadura/sistemasNoHolónomos.ipynb) |
| Guía de ejercicios | [![clase_6](/figurasLaTeX/Icon_pdf-20.svg)](https://github.com/unlam/MecanicaAnaliticaComputacional/blob/main/06FuerzasLigadura/guíaFuerzasLigadura.pdf) |


### 07 Fuerzas no conservativas

| Contenido                 | Enlace |
|---------------------------------|------|
| Fuerzas no conservativas y Euler-Lagrange | [![clase_7](/figurasLaTeX/colab-badge-es.svg)](https://colab.research.google.com/github/unlam/MecanicaAnaliticaComputacional/blob/main/07NoConservativas/noConservativas.ipynb) |
| Guía de ejercicios | [![clase_7](/figurasLaTeX/Icon_pdf-20.svg)](https://github.com/unlam/MecanicaAnaliticaComputacional/blob/main/07NoConservatives/guíaNoConservativas.pdf) |
| Cilindros solidarios | [![clase_7](/figurasLaTeX/colab-badge-es.svg)](https://colab.research.google.com/github/unlam/MecanicaAnaliticaComputacional/blob/main/07NoConservativas/cilíndrosSolidarios_noConservativas_ayuda.ipynb) |


### 08 Tensor de inercia

| Contenido                 | Enlace |
|---------------------------------|------|
| Momento angular y torque | [![clase_8](/figurasLaTeX/colab-badge-es.svg)](https://colab.research.google.com/github/unlam/MecanicaAnaliticaComputacional/blob/main/08TensorInercia/momentoAngularTorque.ipynb) |
| Tensor de inercia | [![clase_8](/figurasLaTeX/colab-badge-es.svg)](https://colab.research.google.com/github/unlam/MecanicaAnaliticaComputacional/blob/main/08TensorInercia/tensorInercia.ipynb) |
| Monóxido de carbono | [![clase_8](/figurasLaTeX/colab-badge-es.svg)](https://colab.research.google.com/github/unlam/MecanicaAnaliticaComputacional/blob/main/08TensorInercia/monóxidoCarbono_tensorInercia.ipynb) |
| Guía de ejercicios | [![clase_8](/figurasLaTeX/Icon_pdf-20.svg)](https://github.com/unlam/MecanicaAnaliticaComputacional/blob/main/08TensorInercia/guíaTensorInercia.pdf) |


### 09 Masa distribuida

| Contenido                 | Enlace |
|---------------------------------|------|
| Masa distribuida | [![clase_9](/figurasLaTeX/colab-badge-es.svg)](https://colab.research.google.com/github/unlam/MecanicaAnaliticaComputacional/blob/main/09MasaDistribuida/masaDistribuida.ipynb) |
| Tensor de inercia de un cubo | [![clase_9](/figurasLaTeX/colab-badge-es.svg)](https://colab.research.google.com/github/unlam/MecanicaAnaliticaComputacional/blob/main/09MasaDistribuida/cubo_tensorInercia.ipynb) |
| Guía de ejercicios | [![clase_9](/figurasLaTeX/Icon_pdf-20.svg)](https://github.com/unlam/MecanicaAnaliticaComputacional/blob/main/09MasaDistribuida/guíaDistribuciónMasa.pdf) |


### 10 Ecuaciones de Euler para la rotación

| Contenido                 | Enlace |
|---------------------------------|------|
| Ecuaciones de Euler | [![clase_10](/figurasLaTeX/colab-badge-es.svg)](https://colab.research.google.com/github/unlam/MecanicaAnaliticaComputacional/blob/main/10RotaciónEuler/rotaciónEuler.ipynb) |
| Engranaje desalineado | [![clase_10](/figurasLaTeX/colab-badge-es.svg)](https://colab.research.google.com/github/unlam/MecanicaAnaliticaComputacional/blob/main/10RotaciónEuler/engranajeDesalineado.ipynb) |
| Guía de ejercicios | [![clase_10](/figurasLaTeX/Icon_pdf-20.svg)](https://github.com/unlam/MecanicaAnaliticaComputacional/blob/main/10RotaciónEuler/guíaRotacionEuler.pdf) |


### 11 Vibraciones con 1 grado de libertad

| Contenido                 | Enlace |
|---------------------------------|------|
| Oscilaciones amortiguadas | [![clase_11](/figurasLaTeX/colab-badge-es.svg)](https://colab.research.google.com/github/unlam/MecanicaAnaliticaComputacional/blob/main/11Vibraciones1GdL/vibraciones1GdL.ipynb) |
| Forzado armónico | [![clase_11](/figurasLaTeX/colab-badge-es.svg)](https://colab.research.google.com/github/unlam/MecanicaAnaliticaComputacional/blob/main/11Vibraciones1GdL/armónico1GdL.ipynb) |
| Forzado arbitrario | [![clase_11](/figurasLaTeX/colab-badge-es.svg)](https://colab.research.google.com/github/unlam/MecanicaAnaliticaComputacional/blob/main/11Vibraciones1GdL/arbitrario1GdL.ipynb) |
| Guía de ejercicios | [![clase_11](/figurasLaTeX/Icon_pdf-20.svg)](https://github.com/unlam/MecanicaAnaliticaComputacional/blob/main/11Vibraciones1GdL/guíaVibraciones1GdL.pdf) |


### 12 Vibraciones con múltiples grados de libertad

| Contenido                 | Enlace |
|---------------------------------|------|
| Oscilaciones con múltiples grados de libertad | [![clase_12](/figurasLaTeX/colab-badge-es.svg)](https://colab.research.google.com/github/unlam/MecanicaAnaliticaComputacional/blob/main/12VibracionesNGdL/vibracionesNGdL.ipynb) |
| Guía de ejercicios | [![clase_12](/figurasLaTeX/Icon_pdf-20.svg)](https://github.com/unlam/MecanicaAnaliticaComputacional/blob/main/12VibracionesNGdL/guíaVibracionesNGdL.pdf) |


### 15 Trabajo integrador

| Contenido                 | Enlace |
|---------------------------------|------|
| Instrucciones | [![clase_15](/figurasLaTeX/colab-badge-es.svg)](https://colab.research.google.com/github/unlam/MecanicaAnaliticaComputacional/blob/main/15Integrador/integradorRígido.ipynb) |


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


## Información auxiliar

### Sobre el curso
- [Temática](https://github.com/unlam/MecanicaAnaliticaComputacional/blob/main/acad%C3%A9mico/tem%C3%A1tica.ipynb)
[![Temática](/figurasLaTeX/colab-badge-es.svg)](https://colab.research.google.com/github/unlam/MecanicaAnaliticaComputacional/blob/main/acad%C3%A9mico/tem%C3%A1tica.ipynb)  
- [Metodología](https://github.com/unlam/MecanicaAnaliticaComputacional/blob/main/acad%C3%A9mico/metodolog%C3%ADa.ipynb)
[![Metodología](/figurasLaTeX/colab-badge-es.svg)](https://colab.research.google/github/unlam/MecanicaAnaliticaComputacional/blob/main/acad%C3%A9mico/metodolog%C3%ADa.ipynb)
- [Cronograma](https://github.com/unlam/MecanicaAnaliticaComputacional/blob/main/acad%C3%A9mico/cronograma.md)
- [Programa analítico](https://github.com/unlam/MecanicaAnaliticaComputacional/blob/main/acad%C3%A9mico/programa.pdf)
- [Textos de referencia](https://github.com/unlam/MecanicaAnaliticaComputacional/blob/main/acad%C3%A9mico/bibliograf%C3%ADa.md)


### Python y Jupyter
- [Lo básico para aprovechar Python](https://www.github.com/unlam/MecanicaAnaliticaComputacional/blob/main/acad%C3%A9mico/introducci%C3%B3nPython.ipynb)
[![Lo básico para aprovechar Python](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/unlam/MecanicaAnaliticaComputacional/blob/main/acad%C3%A9mico/introducci%C3%B3nPython.ipynb)
- [Anotaciones en cuadernos Jupyter: Markdown y LaTeX](https://www.github.com/unlam/MecanicaAnaliticaComputacional/blob/main/acad%C3%A9mico/markdownLaTeX.ipynb)
[![Anotaciones en cuadernos Jupyter: Markdown y LaTeX](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/unlam/MecanicaAnaliticaComputacional/blob/main/acad%C3%A9mico/markdownLaTeX.ipynb)
- [Incluir imágenes en cuadernos Jupyter](https://www.github.com/unlam/MecanicaAnaliticaComputacional/blob/main/acad%C3%A9mico/incluirIm%C3%A1genes.ipynb)
[![Incluir imágenes en cuadernos Jupyter](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/unlam/MecanicaAnaliticaComputacional/blob/main/acad%C3%A9mico/incluirIm%C3%A1genes.ipynb)
- [Biblioteca matplolib para generar gráficos](https://www.github.com/unlam/MecanicaAnaliticaComputacional/blob/main/acad%C3%A9mico/matplotlib.ipynb)
[![Biblioteca matplolib para generar gráficos](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/unlam/MecanicaAnaliticaComputacional/blob/main/acad%C3%A9mico/matplotlib.ipynb)
- [Otros aspectos del Python](https://www.github.com/unlam/MecanicaAnaliticaComputacional/blob/main/informática/másPython.ipynb)
[![Otros aspectos del Python](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/unlam/MecanicaAnaliticaComputacional/blob/main/informática/másPython.ipynb)

