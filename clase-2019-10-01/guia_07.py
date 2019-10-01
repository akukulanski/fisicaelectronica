from math import pi, sin, cos, asin, acos
from constants import *

def ej1():
    """
    Un aparato de Rayos X, posee un anticátodo de Molibdeno sobre el que inciden electrones con
    una energı́a de 0,48×10 −14 J.
    a) ¿Cuál es la longitud de onda mı́nima medida en nm de los rayos X emitidos?
    b) ¿Cuál es su frecuencia?
    c) ¿Qué voltaje acelerador se emplea?
    Respuesta : a) 0,041 nm; b) 7.3×10 18 Hz c) 30 kV
    """
    print('=== ejercicio 1 ===')
    Ke = 0.48e-14 # [J]
    # hc/lo = Ke
    Ke_ev = Ke / e 
    lo = hc / Ke_ev
    print('a) Longitud de onda: {:.2f} nm'.format(lo*1e9))
    # Ke = e*V
    print('b) V=', Ke_ev, 'V')


def ej2():
    """
    Se aceleran electrones sobre un blanco de Molibdeno con un potencial determinado. Para este
    material, la longitud de onda de la lı́nea K α es de 0,71 Å y la K β es de 0,63 Å.
    a) Determinar el potencial aplicado tal que en el espectro (intensidad vs. longitud de onda)
    aparezca la lı́nea K α y no la K β
    b) Graficar el espectro
    Respuesta : a) ∼18 kV
    """
    print('=== ejercicio 2 ===')
    Vmax = hc/0.63e-10
    Vmin = hc/0.71e-10
    print('{:.3f}v < V < {:.3f}v'.format(Vmin, Vmax))

def ej3():
    """
    ¿Cuál es la distancia entre planos atómicos en la calcita si el ángulo entre estos planos y un haz
    de rayos X, de 41,56 keV, dispersado de orden 3, es de 8 ◦ 37’37”?.
    Respuesta : a) 0,3 nm
    """
    print('=== ejercicio 3 ===')
    Ef = 41.56e3 # eV
    ang = pi / 180 * (8+37/60+37/3600) # rad
    m = 3
    lo = hc / Ef # m
    #2*d*sin(ang) = m * lo
    d = m * lo / (2 * sin(ang))
    print('d = {:.3f} nm'.format(d*1e9))

def ej4():
    """
    Usando rayos X de λ=1,5 Å se observa un máximo de difracción de primer orden debido a una
    reflexión en un plano de átomos uniformemente distribuidos en una red cúbica simple, formando
    un ángulo de 18 ◦ respecto a la normal a dicho plano.
    a) Hallar la distancia interatómica.
    b) Hallar el ángulo de dispersión de segundo orden.
    Respuesta :a) 0,079 nm; b) no existe
    """
    print('=== ejercicio 4 ===')
    m = 1
    lo = 1.5e-10 # m
    ang = 18*pi/180 # rad (respecto a normal)
    d = m*lo/(2*cos(ang))
    print('d = {:.3f} pm'.format(d*1e12))

def ej5():
    """
    Considere un fotón proveniente de la lı́nea K α del Molibdeno que incide sobre un electrón en
    reposo, el cual sale despedido en la misma dirección en la que venı́a el fotón.
    a) Calcule la dirección y longitud de onda del fotón luego de la interacción
    b) Calcule el impulso adquirido por el electrón
    Respuesta : a)0,0758 nm; b) 1.8×10 −23 kg.m/s
    """
    print('=== ejercicio 5 ===')
    lo1 = 71e-12 # m
    ang = -pi
    delta_lo = lo_compton * (1-cos(ang))
    lo2 = lo1 + delta_lo
    print('a) long onda = {:.3f} pm'.format(lo2*1e12))
    Pe = hc*(1/lo1 + 1/lo2) # eV/c
    print('b) Pe = {:.3f} ev/c = {:.3g} kg*m/s'.format(Pe, Pe*e/c))

def ej9():
    """
    La primera lı́nea de la serie K del Tungsteno (K α ) tiene una longitud de onda de 0,0215 nm y
    la última lı́nea de la misma serie 0,0178 nm.
    a) Calcular el potencial de frenado (en V) de los fotoelectrones, que libera de un metal la lı́nea
    K α del Tungsteno.
    b) Calcular el voltaje mı́nimo a aplicar entre el filamento y el blanco de Tungsteno, necesario
    para excitar la misma lı́nea (serie K del Tungsteno).
    Respuesta : a) 57,6 kV; b) 69,6 kV
    """
    print('=== ejercicio 9 ===')
    lo_kalfa = 21.5e-12 # m
    lo_k_ultima = 17.8e-12 # m
    Ef = hc / lo_kalfa # eV
    Ke = Ef # eV
    Vf = Ke # V
    print('a) V = {:.2g} KV'.format(Vf/1e3))
    #hc/lo_k_ultima
    #print('b) ...')
    

ej1()
ej2()
ej3()
ej4()
ej5()
#ej4()
#ej4()
