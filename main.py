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

atributes = [0 for i in range(16)]
atributes[0] = ['a','b']
atributes[1] = []
atributes[2] = []
atributes[3] = ['u','y','l','t']
atributes[4] = ['g','p','gg']
atributes[5] = ['c','d','cc','i','j','k','m','r','q','w','x','e','aa','ff']
atributes[6] = ['v','h','bb','j','n','z','dd','ff','o']
atributes[7] = []
atributes[8] = ['t','f']
atributes[9] = ['t','f']
atributes[10] = []
atributes[11] = ['t','f']
atributes[12] = ['g','p','s']
atributes[13] = []
atributes[14] = []
atributes[15] = ['+','-']

def fitness(chromosome):
	for value in chromosome:
		print "hola"

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

print "*************************************************************"
sister.mutate(pmut=1)
print sister
brother.mutate(pmut=1)
print brother