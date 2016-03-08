# Archivo: main.py
# Este es el archivo principal.
# Autores: 
#    - Francisco Martinez 09-10502
#    - Gabriel   Alvarez  09-10029

import data_set_credit
from pyevolve import G1DVariableBinaryString
from pyevolve import GSimpleGA
from pyevolve import Selectors
from pyevolve import Mutators

atributes = []
atributes.append(['a','b']) # 0
atributes.append([35.92,58.08,80.25]) # 1
atributes.append([3.32,6.64,9.96]) # 2
atributes.append(['u','y','l','t']) # 3
atributes.append(['g','p','gg']) # 4
atributes.append(['c','d','cc','i','j','k','m','r','q','w','x','e','aa','ff']) # 5
atributes.append(['v','h','bb','j','n','z','dd','ff','o']) # 6
atributes.append([3.15,6.31,9.46]) # 7
atributes.append(['t','f']) # 8
atributes.append(['t','f']) # 9
atributes.append([22.33,44.67,67]) # 10
atributes.append(['t','f']) # 11
atributes.append(['g','p','s']) # 12
atributes.append([666.667,1333.33,2000]) # 13
atributes.append([330,660,990]) # 14
atributes.append(['+','-']) # 15

data_set = data_set_credit.read_data_set('data_set/training_set.txt')
examples = [data_set[0]]

def string_split_iterator(string,x=10):
    size = len(string)//x
    for pos in range(0, len(string), x):
        yield string[pos:pos+x]

def matches(chromosome,examples=examples):
    for e in examples:
        atr = []
        for rule in string_split_iterator(chromosome,x=chromosome.ruleLength):
            low = 0
            high = len(atributes[0])
            for i in range(15):
                atr.append(rule[low:high])
                for j in range(len(atr[i])):
                    # The atribute is continous.
                    if i in [1,2,7,10,13,14]:
                        if (atr[i][j] == 0) and (float(e[i]) <= atributes[i][j]):
                            return False
                        elif (atr[i][j+1] == 0) and ((atributes[i][j] <= float(e[i])) and (float(e[i]) <= atributes[i][j+1])):
                            return False
                        elif (atr[i][j+2] == 0) and (atributes[i][j+1] <= float(e[i])):
                            return False
                        break
                    else:
                        if (atr[i][j] == 0) and (e[i] == atributes[i][j]):
                            success = False
                            return False
                low = high
                high += len(atributes[i+1])

            atr.append(rule[low:])
            if (atr[15][0] == 1) and (e[15] == '+'):
                return True
            elif (atr[15][0] == 0) and (e[15] == '-'):
                return True
    return False

def fitness(chromosome,examples=examples):
    score = 0
    if (chromosome.stringLength/chromosome.ruleLength) > len(data_set):
        return 0.0
    for e in examples:
        atr = []
        for rule in string_split_iterator(chromosome,x=chromosome.ruleLength):
            low = 0
            high = len(atributes[0])
            for i in range(15):
                atr.append(rule[low:high])
                for j in range(len(atr[i])):
                    # The atribute is continous.
                    if i in [1,2,7,10,13,14]:
                        if (atr[i][j] == 0) and (float(e[i]) <= atributes[i][j]):
                            success = False
                        elif (atr[i][j+1] == 0) and ((atributes[i][j] <= float(e[i])) and (float(e[i]) <= atributes[i][j+1])):
                            success = False
                        elif (atr[i][j+2] == 0) and (atributes[i][j+1] <= float(e[i])):
                            success = False
                        break
                    else:
                        if (atr[i][j] == 0) and (e[i] == atributes[i][j]):
                            success = False
                            break
                low = high
                high += len(atributes[i+1])

            atr.append(rule[low:])
            if (atr[15][0] == 1) and (e[15] == '+'):
                score += 1
                break
            elif (atr[15][0] == 0) and (e[15] == '-'):
                score += 1
                break
    if score == 0:
        return 0.0
    print "entre"
    return (float(score)/float(len(examples)))**2

def run_main():
    # Genome instance
    genome = G1DVariableBinaryString.G1DVariableBinaryString(ruleLength=60)

    # The evaluator function (objective function)
    genome.evaluator.set(fitness)
    genome.mutator.set(Mutators.G1DBinaryStringMutatorFlip)

    # Genetic Algorithm Instance
    ga = GSimpleGA.GSimpleGA(genome)
    ga.selector.set(Selectors.GTournamentSelector)
    ga.setGenerations(1000)
    eval_func = 0
    # GABIL.
    for i in data_set[1:]:
        if eval_func == 0:
            # Do the evolution, with stats dump
            # frequency of 20 generations
            ga.evolve(freq_stats=20)

        # Best individual
        print ga.bestIndividual()
        # if matches(ga.bestIndividual(),examples = [i]):
        #     eval_func = 1
        # else:
        #     eval_func = 0

        examples.append(i)


if __name__ == "__main__":
    run_main()
   