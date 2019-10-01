from math import pi, sin, cos, asin, acos
from constants import *

def ej1():
    """
    Una partı́cula alfa se apunta directamente hacia un núcleo de oro. Esa partı́cula tiene dos proto-
    nes, y su carga es de 2e = 2(1,60×10 −19 C), mientras que un núcleo de oro tiene 79 protones y una
    carga de 79e = 79(1,60×10 −19 C). ¿Qué energı́a cinética mı́nima debe tener la partı́cula alfa para
    acercarse a menos de 5×10 −14 m del centro del núcleo de oro? Suponga que el núcleo de oro, que
    tiene más o menos 50 veces la masa en reposo de una partı́cula alfa, permanece en reposo.
    Respuesta : 4,6 MeV
    """
    print('=== ejercicio 1 ===')
    q1 = 2*e # C
    q2 = 79*e # C
    d_min = 5e-14 # m
    # Ec_min = Ep(r=d_min) = k*q1*q2/r
    Ec_min = 1/(4*pi*8.85e-12)*q1*q2/d_min # J
    print('a) Ec min = {:.2g} J = {:.2g} eV'.format(Ec_min, Ec_min/e))


def ej2():
    """
    Una partı́cula α con una energı́a cinética de 7,68 MeV incide centralmente sobre el núcleo de
    un átomo de cobre. Sabiendo que q α = 2 q p y que el número atómico del cobre es 29; determinar la
    distancia de máximo acercamiento entre la partı́cula y el núcleo.
    Respuesta : 1,086×10 −14 m
    """
    print('=== ejercicio 2 ===')

def ej3():
    """
    Un átomo hipotético tiene tres niveles de energı́a: el fundamental, y los de 1 eV y 3 eV arriba
    del nivel fundamental.a) Calcule las frecuencias y las longitudes de onda de las lı́neas espectrales
    que puede emitir este átomo cuando se excita. b) ¿Qué longitudes de onda puede absorber este
    átomo, si al principio está en su nivel fundamental?
    Respuesta : a) λ 1−f =1240 nm, λ 2−1 =620 nm, λ 2−f =414 nm b) λ f −1 =1240 nm , λ f −2 =414 nm
    """
    print('=== ejercicio 3 ===')

def ej4():
    """
    Determine las energı́as cinética, potencial y total del átomo de hidrógeno en el primer nivel de
    excitación, y determine la longitud de onda del fotón emitido en la transición del primer nivel de
    excitación al nivel fundamental.
    Respuesta : a) K= 3,4 eV, U= -6,9 eV, E=-3,4 eV
    """
    print('=== ejercicio 4 ===')

def ej5():
    """
    ¿Qué energı́a (en eV) se requiere para llevar al electrón desde el estado fundamental al primero,
    al segundo y al tercer estado excitado en átomos de hidrógeno?
    Respuesta : E 12 = 10,12 eV, E 13 = 12 eV, E 14 = 12,656 eV
    """
    print('=== ejercicio 5 ===')


def ej6():
    """
    Un haz de electrones incide sobre un blanco de átomos de hidrógeno en su estado fundamental
    de energı́a. ¿Con qué energı́a mı́nima emergerán dichos electrones después de interactuar con un
    átomo de H, si su energı́a cinética al incidir sobre los átomos fuese de: a) 8,72 eV b) 11,21 eV
    Respuesta : a) 8,72 eV b) 1 eV
    """
    print('=== ejercicio 6 ===')

def ej10():
    """
    a) Si el electrón pasa a una órbita de radio mayor ¿Aumenta o disminuye su energı́a total?
    ¿Aumenta o disminuye su energı́a cinética? Explique con fórmulas y conceptualmente.
    b) ¿Cuál es la energı́a del fotón de longitud de onda más corta que puede ser emitido por el
    átomo de hidrógeno? Demuestre matemáticamente y explique conceptualmente.
    """
    print('=== ejercicio 10 ===')


ej1()
#ej2()
#ej3()
ej4()
ej5()
ej6()
ej10()
