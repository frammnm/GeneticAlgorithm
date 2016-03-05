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
atributes[1] = [35.92,58.08] # float 
atributes[2] = [3.32,6.64] # float
atributes[3] = ['u','y','l','t']
atributes[4] = ['g','p','gg']
atributes[5] = ['c','d','cc','i','j','k','m','r','q','w','x','e','aa','ff']
atributes[6] = ['v','h','bb','j','n','z','dd','ff','o']
atributes[7] = [3.15,6.31] # float
atributes[8] = ['t','f']
atributes[9] = ['t','f']
atributes[10] = [22.33,44.67] # int 
atributes[11] = ['t','f']
atributes[12] = ['g','p','s']
atributes[13] = [666.667,1333.33] # int 
atributes[14] = [330,660] # int 
atributes[15] = ['+','-']

def string_split_iterator(string,x=10):
	size = len(string)//x
	for pos in range(0, len(string), x):
		yield string[pos:pos+x]

# Rules of length = 60.

def fitness(chromosome,examples=[1]):
	score = 0
	for e in examples:
		atr = [0 for i in range(16)]
		for rule in string_split_iterator(chromosome,x=chromosome.ruleLength):
			# a,b.
			atr[0] = rule[:2]
			# c1,c2,c3.
			atr[1] = rule[2:5]
			# c1,c2,c3.
			atr[2] = rule[5:8]
			# u,y,l,t.
			atr[3] = rule[8:12]
			# g,p,gg.
			atr[4] = rule[12:15]
			# c,d,cc,i,j,k,m,r,q,w,x,e,aa,ff.
			atr[5] = rule[15:29]
			# v,h,bb,j,n,z,dd,ff,o.
			atr[6] = rule[29:38]
			# c1,c2,c3.
			atr[7] = rule[38:41]
			# t,f.
			atr[8] = rule[41:43]
			# t,f.
			atr[9] = rule[43:45]
			# c1,c2,c3.
			atr[10] = rule[45:48]
			# t,f.
			atr[11] = rule[48:50]
			# g,p,s.
			atr[12] = rule[50:53]
			# c1,c2,c3.
			atr[13] = rule[53:56]
			# c1,c2,c3.
			atr[14] = rule[56:59]
			# +,-.
			atr[15] = rule[59:]
			success = True
			while True:
				# a,b.
				if (atr[0][0] == 0) and (e[0] == 'a'):
					success = False
					break
				if (atr[0][1] == 0) and (e[0] == 'b'):
					success = False
					break
				# c1,c2,c3. 35.92-58.08
				if (atr[1][0] == 0) and (float(e[1]) <= 35.92):
					success = False
					break
				if (atr[1][1] == 0) and ((35.92 < float(e[1])) and (float(e[1]) <= 58.08)):
					success = False
					break
				if (atr[1][2] == 0) and (58.08 < float(e[1])):
					success = False
					break
				# c1,c2,c3. 3.32-6.64
				if (atr[2][0] == 0) and (float(e[2]) <= 3.32):
					success = False
					break
				if (atr[2][1] == 0) and ((3.32 < float(e[2])) and (float(e[2]) <= 6.64)):
					success = False
					break
				if (atr[2][2] == 0) and (6.64 < float(e[2])):
					success = False
					break
				# u,y,l,t.
				if (atr[3][0] == 0) and (e[3] == 'u'):
					success = False
					break
				if (atr[3][1] == 0) and (e[3] == 'y'):
					success = False
					break
				if (atr[3][2] == 0) and (e[3] == 'l'):
					success = False
					break
				if (atr[3][3] == 0) and (e[3] == 't'):
					success = False
					break
				# g,p,gg.
				if (atr[4][0] == 0) and (e[4] == 'g'):
					success = False
					break
				if (atr[4][1] == 0) and (e[4] == 'p'):
					success = False
					break
				if (atr[4][2] == 0) and (e[4] == 'gg'):
					success = False
					break
				# c,d,cc,i,j,k,m,r,q,w,x,e,aa,ff.
				if (atr[5][0] == 0) and (e[5] == 'c'):
					success = False
					break
				if (atr[5][1] == 0) and (e[5] == 'd'):
					success = False
					break
				if (atr[5][2] == 0) and (e[5] == 'cc'):
					success = False
					break
				if (atr[5][3] == 0) and (e[5] == 'i'):
					success = False
					break
				if (atr[5][4] == 0) and (e[5] == 'j'):
					success = False
					break
				if (atr[5][5] == 0) and (e[5] == 'k'):
					success = False
					break
				if (atr[5][6] == 0) and (e[5] == 'm'):
					success = False
					break
				if (atr[5][7] == 0) and (e[5] == 'r'):
					success = False
					break
				if (atr[5][8] == 0) and (e[5] == 'q'):
					success = False
					break
				if (atr[5][9] == 0) and (e[5] == 'w'):
					success = False
					break
				if (atr[5][10] == 0) and (e[5] == 'x'):
					success = False
					break
				if (atr[5][11] == 0) and (e[5] == 'e'):
					success = False
					break
				if (atr[5][12] == 0) and (e[5] == 'aa'):
					success = False
					break
				if (atr[5][13] == 0) and (e[5] == 'ff'):
					success = False
					break
				# v,h,bb,j,n,z,dd,ff,o.
				if (atr[6][0] == 0) and (e[6] == 'v'):
					success = False
					break
				if (atr[6][1] == 0) and (e[6] == 'h'):
					success = False
					break
				if (atr[6][2] == 0) and (e[6] == 'bb'):
					success = False
					break
				if (atr[6][3] == 0) and (e[6] == 'j'):
					success = False
					break
				if (atr[6][4] == 0) and (e[6] == 'n'):
					success = False
					break
				if (atr[6][4] == 0) and (e[6] == 'z'):
					success = False
					break
				if (atr[6][4] == 0) and (e[6] == 'dd'):
					success = False
					break
				if (atr[6][4] == 0) and (e[6] == 'ff'):
					success = False
					break
				if (atr[6][4] == 0) and (e[6] == 'o'):
					success = False
					break
				# c1,c2,c3. 3.15-6.31
				if (atr[7][0] == 0) and (float(e[7]) <= 3.15):
					success = False
					break
				if (atr[7][1] == 0) and ((3.15 < float(e[7])) and (float(e[7]) <= 6.31)):
					success = False
					break
				if (atr[7][2] == 0) and (6.31 < float(e[7])):
					success = False
					break
				# t,f.
				if (atr[8][0] == 0) and (e[8] == 't'):
					success = False
					break
				if (atr[8][1] == 0) and (e[8] == 'f'):
					success = False
					break
				# t,f.
				if (atr[9][0] == 0) and (e[9] == 't'):
					success = False
					break
				if (atr[9][1] == 0) and (e[9] == 'f'):
					success = False
					break
				# c1,c2,c3. 22.33-44.67
				if (atr[10][0] == 0) and (float(e[10]) <= 22.33):
					success = False
					break
				if (atr[10][1] == 0) and ((22.33 < float(e[10])) and (float(e[10]) <= 44.67)):
					success = False
					break
				if (atr[10][2] == 0) and (44.67 < float(e[10])):
					success = False
					break
				# t,f.
				if (atr[11][0] == 0) and (e[11] == 't'):
					success = False
					break
				if (atr[11][1] == 0) and (e[11] == 'f'):
					success = False
					break
				# g,p,s.
				if (atr[12][0] == 0) and (e[12] == 'g'):
					success = False
					break
				if (atr[12][1] == 0) and (e[12] == 'g'):
					success = False
					break
				if (atr[12][2] == 0) and (e[12] == 's'):
					success = False
					break
				# c1,c2,c3. 666.667-1333.33
				if (atr[13][0] == 0) and (float(e[13]) <= 666.667):
					success = False
					break
				if (atr[13][1] == 0) and ((666.667 < float(e[13])) and (float(e[13]) <= 1333.33)):
					success = False
					break
				if (atr[13][2] == 0) and (1333.33 < float(e[13])):
					success = False
					break
				# c1,c2,c3. 330-660
				if (atr[14][0] == 0) and (float(e[14]) <= 330):
					success = False
					break
				if (atr[14][1] == 0) and ((330 < float(e[14])) and (float(e[14]) <= 660)):
					success = False
					break
				if (atr[14][2] == 0) and (660 < float(e[14])):
					success = False
					break
			if success:
				if (atr[15][0] == 1) and (e[15] == '+'):
					score += 1
				elif (atr[15][0] == 0) and (e[15] == '-'):
					score += 1
	if score == 0:
		return 0.0
	return float(score) / float(len(examples))


x = vbs.G1DVariableBinaryString(ruleLength=60,numRules=2)
y = vbs.G1DVariableBinaryString(ruleLength=60,numRules=1)
x.initialize()
y.initialize()

print x
fitness(x)

# print "*************************** Madre ***************************"
# print x
# print "*************************** Padre ***************************"
# print y
# for it in x.crossover.applyFunctions(mom=x, dad=y, count=2):
#     (sister, brother) = it

# print "*************************************************************"
# sister.mutate(pmut=1)
# print sister
# brother.mutate(pmut=1)
# print brother