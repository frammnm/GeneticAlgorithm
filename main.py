# Archivo: main.py
# Este es el archivo principal.
# Autores: 
#    - Francisco Martinez 09-10502
#    - Gabriel   Alvarez  09-10029

import data_set_credit
from pyevolve import G1DVariableBinaryString as vbs
from pyevolve import GenomeBase as gb
from pyevolve import Crossovers as xs
from pyevolve import G1DBinaryString as bs

x = vbs.G1DVariableBinaryString(numRules=2)
y = vbs.G1DVariableBinaryString(numRules=1)
x.initialize()
y.initialize()

z = bs.G1DBinaryString()
z.initialize()

print "*************************** Madre ***************************"
print x
print "*************************** Padre ***************************"
print y
for it in x.crossover.applyFunctions(mom=x, dad=y, count=2):
    (sister, brother) = it