import sympy as sp
from forward_kinematics_dh_class import ForwardKinematicsDH

# Definir variables simbólicas para las articulaciones y longitudes
q1, q2, q3 = sp.symbols('q1 q2 q3')
l1, l2, l3 = sp.symbols('l1 l2 l3')
d1, d2, d3 = sp.symbols('d1 d2 d3')
p1, p2, p3 = sp.symbols('p1 p2 p3')

# Tabala DH usando el orden [theta, d, l, alpha] para robot planar RR
DH_RR = [
    [q1, 0, l1, 0],        # Eslabón 1
    [q2, 0, l2, 0],        # Eslabón 2
]

# Tabla DH usando el orden [theta, d, l, alpha] para robot antropomórfico RRR
DH_RRR = [
    [q1, 0, l1, sp.pi/2],  # Eslabón 1
    [q2, 0, l2, 0],        # Eslabón 2
    [q3, 0, l3, 0],        # Eslabón 3
]

# Tabla DH usando el orden [theta, d, l, alpha] para robot SCARA RRP
DH_RRP = [
	[q1, 0, l1, 0],        # Eslabón 1
	[q2, 0, l2, sp.pi],    # Eslabón 2
	[0, d3,  0, 0],        # Eslabón 3
]

# Calcular las matrices simbólicas
MH_RR = ForwardKinematicsDH.symbolic(DH_RR)
MH_RRR = ForwardKinematicsDH.symbolic(DH_RRR)
MH_RRP = ForwardKinematicsDH.symbolic(DH_RRP)

# Imprimir las matrices resultantes
print('Matriz homogénea RR:')
sp.pprint(MH_RR, use_unicode=True)
print('Matriz homogénea RRR:')
sp.pprint(MH_RRR, use_unicode=True)
print('\nMatriz homogénea RRP:')
sp.pprint(MH_RRP, use_unicode=True)