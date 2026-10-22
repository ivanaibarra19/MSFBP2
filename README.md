# Práctica 2: Modelado y control del sistema cardiovascular

## Información de la estudiante

**Nombre completo:** ______________________________  
**Número de control:** ______________________________  
**Correo institucional:** ______________________________

**Asignatura:** Modelado de Sistemas Fisiológicos  
**Carrera:** Ingeniería Biomédica

## Docente

Dr. Paul Antonio Valle Trujillo; paul.valle@tectijuana.edu.mx

Departamento de Ingeniería Eléctrica y Electrónica, Tecnológico Nacional de México / Instituto Tecnológico de Tijuana, Blvd. Alberto Limón Padilla s/n, Tijuana, C. P. 22454, B. C., México.

## Descripción de la asignatura

La asignatura de Modelado de Sistemas Fisiológicos permite representar procesos del cuerpo humano mediante modelos matemáticos y herramientas de simulación. A través de analogías con circuitos eléctricos, se estudia la respuesta dinámica de sistemas biológicos y se aplican principios de control clásico. Estas herramientas ayudan al estudiante de Ingeniería Biomédica a interpretar el comportamiento fisiológico y evaluar sistemas de control mediante experimentación *in silico*.

## Objetivos

1. Identificar las variables y los parámetros hemodinámicos del modelo Windkessel de cuatro elementos.
2. Formular las ecuaciones diferenciales y obtener la función de transferencia del sistema cardiovascular.
3. Estudiar la estabilidad, los polos y el error en estado estacionario de los tres modelos.
4. Simular las condiciones hipotensa, normotensa e hipertensa en MATLAB/Simulink y Simscape Electrical.
5. Comparar las respuestas en lazo abierto utilizando una misma señal de entrada aleatoria.
6. Diseñar y ajustar dos controladores PID independientes para aproximar las respuestas hipotensa e hipertensa a la referencia normotensa.
7. Reproducir las simulaciones en Python y contrastarlas con los resultados de MATLAB.
8. Elaborar un diagrama biológico que relacione los componentes del modelo con el sistema cardiovascular.

## Descripción detallada del sistema

La práctica utiliza el **modelo Windkessel de cuatro elementos**, que representa la dinámica del sistema arterial mediante una impedancia característica (**Z**), una inertancia (**L**), una resistencia periférica (**R**) y una distensibilidad arterial (**C**). La presión arterial de entrada se identifica como $P_a(t)$ y la presión de salida como $P_p(t)$.

Se analizan tres condiciones cardiovasculares modificando únicamente la distensibilidad arterial. El caso normotenso funciona como referencia, mientras que los casos hipotenso e hipertenso se comparan con ella para evaluar el efecto de dos controladores PID mediante simulaciones computacionales.

| Parámetro | Hipotenso | Normotenso | Hipertenso |
|---|---:|---:|---:|
| Z | 0.010 | 0.010 | 0.010 |
| L | 0.001 | 0.001 | 0.001 |
| R | 1.000 | 1.000 | 1.000 |
| C | 3.500 | 1.500 | 1.000 |

La función de transferencia utilizada para los tres estados es:

$$
G(s)=\frac{P_p(s)}{P_a(s)}=\frac{LRs+RZ}{CLRZs^2+(LR+LZ)s+RZ}.
$$

La entrada aleatoria debe ser la misma para los tres casos y las simulaciones se realizan de **0 a 15 segundos**. El análisis es exclusivamente académico y *in silico*.

**Palabras clave:** Modelo Windkessel; sistema cardiovascular; presión arterial; controlador PID; MATLAB; Python; simulación.

## Lista de archivos incluidos en el repositorio

1. Cuaderno de MATLAB (`.mlx`) y versión exportada (`.pdf`).
2. Modelos de Simulink y Simscape Electrical (`.slx`).
3. Programa de simulación en Python (`.py`).
4. Archivo con la señal aleatoria utilizada en las simulaciones.
5. Gráficas de los estados hipotenso, normotenso e hipertenso en lazo abierto.
6. Gráficas de comparación de los sistemas con controladores PID.
7. Capturas de los parámetros y ganancias de ambos controladores.
8. Diagrama biológico del sistema cardiovascular.
9. Desarrollo matemático, análisis de estabilidad y resultados.
10. Archivos `README.md` y `CITATION.cff`.

## Referencias

[1] P. A. Valle, *Material de la asignatura Modelado de Sistemas Fisiológicos*, Tecnológico Nacional de México / Instituto Tecnológico de Tijuana. Disponible en: https://biomath.xyz/course/

[2] M. C. Khoo, *Physiological Control Systems: Analysis, Simulation, and Estimation*, 2nd ed., IEEE Press, 2018.

[3] N. S. Nise, *Control Systems Engineering*, 8th ed., John Wiley & Sons, 2020.
