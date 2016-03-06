# Archivo: main.py
# Este es el archivo principal.
# Autores: 
#    - Francisco Martinez 09-10502
#    - Gabriel   Alvarez  09-10029

import data_set_credit
from pyevolve import G1DVariableBinaryString
from pyevolve import G1DBinaryString
from pyevolve import GSimpleGA
from pyevolve import Selectors
from pyevolve import Mutators

atributes = []
atributes.append(['a','b'])
atributes.append([35.92,58.08,80.25])
atributes.append([3.32,6.64,9.96])
atributes.append(['u','y','l','t'])
atributes.append(['g','p','gg'])
atributes.append(['c','d','cc','i','j','k','m','r','q','w','x','e','aa','ff'])
atributes.append(['v','h','bb','j','n','z','dd','ff','o'])
atributes.append([3.15,6.31,9.46])
atributes.append(['t','f'])
atributes.append(['t','f'])
atributes.append([22.33,44.67,67])
atributes.append(['t','f'])
atributes.append(['g','p','s'])
atributes.append([666.667,1333.33,2000])
atributes.append([330,660,990])
atributes.append(['+','-'])

examples = data_set_credit.read_data_set('data_set/test_set.txt')

def string_split_iterator(string,x=10):
    size = len(string)//x
    for pos in range(0, len(string), x):
        yield string[pos:pos+x]

def fitness(chromosome,examples=examples):
    print examples
    score = 0
    for e in examples:
        atr = []
        for rule in string_split_iterator(chromosome,x=chromosome.ruleLength):
            success = True
            low = 0
            high = len(atributes[0])
            for i in range(15):
                atr.append(rule[low:high])
                for j in range(len(atr[i])):
                    # The atribute is continous.
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
                if not success:
                    break
                low = high
                high += len(atributes[i+1])
            if success:
                atr.append(rule[low:])
                if (atr[15][0] == 1) and (e[15] == '+'):
                    score += 1
                elif (atr[15][0] == 0) and (e[15] == '-'):
                    score += 1
    if score == 0:
        return 0.0
    return float(score)/float(len(examples))

def run_main():
    # Genome instance
    genome = G1DVariableBinaryString.G1DVariableBinaryString(ruleLength=60)

    # The evaluator function (objective function)
    genome.evaluator.set(fitness)
    genome.mutator.set(Mutators.G1DBinaryStringMutatorFlip)

    # Genetic Algorithm Instance
    ga = GSimpleGA.GSimpleGA(genome)
    ga.selector.set(Selectors.GTournamentSelector)
    ga.setGenerations(70)

    # Do the evolution, with stats dump
    # frequency of 10 generations
    ga.evolve(freq_stats=20)

    # Best individual
    print ga.bestIndividual()

if __name__ == "__main__":
    run_main()
   