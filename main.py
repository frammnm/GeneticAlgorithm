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

def fitness(chromosome,examples=['b','25.67','3.25','u','g','c','h','2.29','f','t','01','t','g','00416','21','-']):
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
            while success:
                for i in range(15):
                    j = 0
                    while j < len(atr[i]):
                        if i in [1,2,7,10,13,14]:
                            if (atr[i][j] == 0) and (float(e[i]) <= atributes[i][j]):
                                success = False
                                break
                            if (atr[i][j+1] == 0) and ((atributes[i][j] < float(e[i])) and (float(e[i]) <= atributes[i][j+1])):
                                success = False
                                break
                            if (atr[i][j+2] == 0) and (atributes[i][j+1] < float(e[i])):
                                success = False
                                break
                            break
                        else:
                            if (atr[i][j] == 0) and (e[i] == atributes[i][j]):
                                success = False
                                break
                        j += 1
                if success:
                    if (atr[15][0] == 1) and (e[15] == '+'):
                        score += 1
                    elif (atr[15][0] == 0) and (e[15] == '-'):
                        score += 1
                    break
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