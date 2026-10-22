"""
Práctica 2: Sistema Cardiovascular

Departamento de Ingeniería Eléctrica y Electrónica, Ingeniería Biomédica
Tecnológico Nacional de México [TecNM - Tijuana]
Blvd. Alberto Limón Padilla s/n, C.P. 22454, Tijuana, B.C., México

Nombre del alumno: Ibarra Monroy Ivana Valeria
Número de control: 23210709
Correo institucional: l23210709@tectijuana.edu.mx

Asignatura: Modelado de Sistemas Fisiológicos
Docente: Dr. Paul Antonio Valle Trujillo; paul.valle@tectijuana.edu.mx
"""
import numpy as np
import control as ctrl
import matplotlib.pyplot as plt
from scipy import signal
import pandas as pd

# Datos generales de la simulacion
x0,t0,tend,dt,w,h = 0,0,15,1E-3,7,3.5
N = round(tend/dt) + 1
t = np.linspace(t0,tend,N)
u = np.array(pd.read_excel(
    '/Users/ivanaibarra/Desktop/Modelado /practica2/signal.xlsx', header=None))
u = signal.resample(u,N,axis=0)
Pa = u[:,0]

def cardio(Z,L,R,C):
    num = [L*R,R*Z]
    den = [C*L*R*Z,L*R+L*Z,R*Z]
    sys = ctrl.tf(num,den)
    L = np.roots(den)
    return sys,L

# Funcion de transferencia: Hipotenso
Z,L,R,C = 0.010,0.001,1.00,3.500
syshipo,L = cardio(Z,L,R,C)
print(f"Funcion de transferencia del hipotenso: {syshipo}")
print(f"Polos del sistema: L1 = {L[0]:.3e}, L2 = {L[1]:.3e}\n")

# Funcion de transferencia: Normotenso
Z,L,R,C = 0.010,0.001,1.00,1.500
sysnormo,L = cardio(Z,L,R,C)
print(f"Funcion de transferencia del normotenso: {sysnormo}")
print(f"Polos del sistema: L1 = {L[0]:.3e}, L2 = {L[1]:.3e}\n")

# Funcion de transferencia: Hipertenso
Z,L,R,C = 0.010,0.001,1.00,1.000
syshiper,L = cardio(Z,L,R,C)
print(f"Funcion de transferencia del hipertenso: {syshiper}")
print(f"Polos del sistema: L1 = {L[0]:.3e}, L2 = {L[1]:.3e}\n")

#Controlador
def controlador(kP,kI,kD,sys):
    Cr = 1E-6
    Re = 1/(kI*Cr)
    Rr = kP*Re
    Ce = kD/Rr
    numPID = [Re*Rr*Ce*Cr,Re*Ce+Rr*Cr,1]
    denPID = [Re*Cr,0]
    PID = ctrl.tf(numPID,denPID)
    sysPID = ctrl.feedback(ctrl.series(PID,sys),1,sign=-1)
    return sysPID

# Controlador PID: Hipotenso
hipoPID = controlador(458.438,1112094.736,0.00627,syshipo)
print(f'Funcion de transferencia del hipotenso en lazo cerrado: {hipoPID}')
# Controlador PID: Hipertenso
hiperPID = controlador(126.595,293327.703,0.00140,syshiper)
print(f'Funcion de transferencia del hipotenso en lazo abierto: {hiperPID}')


# Funcion del sistema en lazo abierto
def openloop(t,sys,u):
    _,y = ctrl.forced_response(sys,t,u,x0)
    return y

# Funcion del sistema en lazo cerrado
def closedloop(t,sysPID,u):
    _,y = ctrl.forced_response(sysPID,t,u,x0)
    return y

# Respuestas en lazo abierto
PpL = openloop(t,syshipo,Pa)
PpN = openloop(t,sysnormo,Pa)
PpH = openloop(t,syshiper,Pa)
# Respuestas en lazo cerrado
PIDL = closedloop(t,hipoPID,Pa)
PIDH = closedloop(t,hiperPID,Pa)

clr1 = np.array([255,0,0])/255
clr2 = np.array([0,0,255])/255
clr3 = np.array([0,128,0])/255
def grafica(numero,y1,y2,y3,label1,label2,label3,archivo):
    fg = plt.figure(numero)
    fg.set_size_inches(w,h)
    plt.rcParams['font.size'] = 11
    plt.rcParams['font.family'] = 'serif'
    plt.rcParams['font.serif'] = ['Times New Roman']
    plt.plot(t,y1,'-',color=clr1,linewidth=0.3,label=label1)
    plt.plot(t,y2,'-',color=clr2,linewidth=0.3,label=label2)
    plt.plot(t,y3,'-',color=clr3,linewidth=0.3,label=label3)
    plt.xlim(0,15)
    plt.xticks(np.arange(0,16,1))
    plt.xlabel('t [s]')
    plt.ylabel('Vi(t) [V]')
    plt.legend(
        bbox_to_anchor=(0.5,-0.25),
        loc='upper center',
        ncol=3,
        frameon=False
    )
    fg.savefig(archivo,bbox_inches='tight')
    plt.show()

grafica(
    1,
    PpN,PpL,PpH,
    'Normotenso','Hipotenso','Hipertenso',
    'Lazo_abierto_python.pdf'
)
grafica(
    2,
    PpN,PpL,PIDL,
    'Normotenso','Hipotenso','PID Controlador',
    'Hipotenso_python.pdf'
)
grafica(
    3,
    PpN,PpH,PIDH,
    'Normotenso','Hipertenso','PID Controlador',
    'Hipertenso_python.pdf'
)