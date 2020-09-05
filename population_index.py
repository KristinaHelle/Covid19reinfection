"""
# code based on code of ??? ADE group.
This Code  Build a map which associate to a population name of the model  an
index, in order to create a list that will record the dynamics of the populations.

We first created a dictionary named "index" which will has as keys the names of
populations and as  values the associated index.

output desired ==> index : dictionary
"""
from parameters_reinfection import *
#from parameters_original import NE, NP, NI, NL
import numpy as np
NE = 2; NP = 3; NI = 5; NP = 7; NL = 11; NA = 13; NU = 17


compartments = [('S',  0, '__'),
                ('A',  0, 't_'), ('A',  0, '__'),
                ('U',  0, 't_'), ('U',  0, '__'),
                ('E', NE, 'ta'), ('P', NP, 'ta'), ('I', NI, 'ta'), ('L', NL, 'ta'),
                ('E', NE, 'tm'), ('P', NP, 'tm'), ('I', NI, 'tm'), ('L', NL, 'tm'),
                ('E', NE, 'um'), ('P', NP, 'um'),
                ('E', NE, '_m'), ('P', NP, '_m'), ('I', NI, '_m'), ('L', NL, '_m'),
                ('E', NE, 'om'), ('P', NP, 'om'), ('I', NI, 'om'), ('L', NL, 'om'),
                ('E', NE, 'us'), ('P', NP, 'us'),
                ('E', NE, '_s'), ('P', NP, '_s'), ('I', NI, '_s'), ('L', NL, '_s'),
                ('E', NE, 'oa'), ('P', NP, 'oa'), ('I', NI, 'oa'), ('L', NL, 'oa'),
                ('U', NU, 'ta'), ('U', NU, 'tm'), ('U', NU, 'om'), ('U', NU, 'os'), ('U', NU, 'oa'),
                ('A', NA, 'ta'), ('A', NA, 'tm'), ('A', NA, 'om'), ('A', NA, 'os'), ('A', NA, 'oa'),
                ('R',  0, '__'), ('D',  0, '__')
                ]

index = dict()
ind = 0
for i in compartments:
    notation = i[0] + i[2]
    if i[1] == 0:
        index[notation] = ind
        ind += 1
    else:
        for k in np.arange(1, i[1] + 1):
            notation_k = notation + '_' + str(k)
            index[notation_k] = ind
            ind += 1
print(index)


