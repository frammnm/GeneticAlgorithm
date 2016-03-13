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
import sys

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
atributes.append([22,45,67]) # 10
atributes.append(['t','f']) # 11
atributes.append(['g','p','s']) # 12
atributes.append([667,1333,2000]) # 13
atributes.append([330,660,990]) # 14
atributes.append(['+','-']) # 15

data_set = data_set_credit.read_data_set('data_set/training_set.txt')
test_set = data_set_credit.read_data_set('data_set/test_set.txt')
examples = [data_set[0]]
#examples = data_set

ruleLength = sum(len(atributes[i]) for i in range(len(atributes)))-1

def string_split_iterator(string,x=10):
    size = len(string)//x
    for pos in range(0, len(string), x):
        yield string[pos:pos+x]

def matches(chromosome,e):
    atr = []
    for rule in string_split_iterator(chromosome,x=ruleLength):
        low = 0
        high = len(atributes[0])
        success = True
        for i in range(15):
            atr.append(rule[low:high])
            for j in range(len(atr[i])):
                # The atribute is continous.
                if i in [1,2,7,10,13,14]:
                    if '.' in e[i]:
                        num = float(e[i])
                    else:
                        num = int(e[i])
                    if (atr[i][j] == 0) and (num < atributes[i][j]):
                        success = False
                    elif num == atributes[i][j] and atr[i][j] == 0 and atr[i][j+1] == 0:
                        success = False
                    elif (atr[i][j+1] == 0) and ((atributes[i][j] < num) and (num < atributes[i][j+1])):
                        success = False
                    elif num == atributes[i][j+1] and atr[i][j+1] == 0 and atr[i][j+2] == 0:
                        success = False
                    break
                else:
                    if (atr[i][j] == 0) and (e[i] == atributes[i][j]):
                        success = False
            low = high
            high += len(atributes[i+1])
            if not success:
                break
        if success:
            atr.append(rule[low:])
            if (atr[15][0] == 1) and (e[15] == '+'):
                return True
            elif (atr[15][0] == 0) and (e[15] == '-'):
                return True
            else:
                success = False
    return success

def fitness(chromosome,examples=examples):
    score = 0
    if (len(chromosome)/ruleLength) > 8 :
        return 0.0
    for e in examples:
        if matches(chromosome,e):
            score += 1 
    if score == 0:
        return 0.0
    return (100*float(score)/float(len(examples)))**2

def predict(chromosome,examples=test_set):
    score = 0
    for e in examples:
        if matches(chromosome,e):
            score += 1 
    if score == 0:
        return 0.0
    return 100*(float(score)/float(len(examples)))

def run_main():
    # First arg -f name of the file that contains the results.
    # Second arg -s [0,1] if 1 then RouletteWheel elif 0 then Tournament
    # Third arg -e [0,1] if 1 then Elitism elif 0 then noElitism
    # Fourth arg -c the crossover rate
    # Fifth arg -m the mutation rate
    
    name = "GABIL_Results.txt"

    # Genome instance
    genome = G1DVariableBinaryString.G1DVariableBinaryString(ruleLength=60)

    # The evaluator function (objective function)
    genome.evaluator.set(fitness)
    genome.mutator.set(Mutators.G1DBinaryStringMutatorFlip)

    # Genetic Algorithm Instance
    ga = GSimpleGA.GSimpleGA(genome)
    ga.selector.set(Selectors.GTournamentSelector)
    ga.terminationCriteria.set(GSimpleGA.ConvergenceCriteria)
    ga.setMultiProcessing()
    if len(sys.argv) > 1:
        if len(sys.argv[1:]) % 2 == 0:
            i = 1
            while i < len(sys.argv):
                if sys.argv[i] == '-f':
                    name = sys.argv[i+1]
                elif sys.argv[i] == '-s':
                    if sys.argv[i+1] == '0':
                        ga.selector.set(Selectors.GTournamentSelector)
                    elif sys.argv[i+1] == '1':
                        ga.selector.set(Selectors.GRouletteWheel)
                    else:
                        print "ERROR: Unknown argument!"
                        sys.exit(1)
                elif sys.argv[i] == '-e':
                    if sys.argv[i+1] == '0':
                        ga.setElitism(False)
                    elif sys.argv[i+1] == '1':
                        ga.setElitism(True)
                    else:
                        print "ERROR: Unknown argument!"
                        sys.exit(1)
                elif sys.argv[i] == '-c':
                    try:
                        crossoverRate = float(sys.argv[i+1])
                        ga.setCrossoverRate(crossoverRate)
                    except ValueError:
                        print "ERROR: Unknown argument!"
                        sys.exit(1)
                elif sys.argv[i] == '-m':
                    try:
                        mutationRate = float(sys.argv[i+1])
                        ga.setMutationRate(mutationRate)
                    except ValueError:
                        print "ERROR: Unknown argument!"
                        sys.exit(1)
                i += 2
        else:
            print "ERROR: Incorrect number of arguments!"
            sys.exit(1)

    # GABIL.
    eval_func = 0
    j = 1
    for i in data_set[1:]:
        if eval_func == 0:
            ga.setGenerations(100*j)
            # Do the evolution, with stats dump
            # frequency of 10 generations
            print " ********************************************************************************"
            ga.evolve(freq_stats=10)
            print " ********************************************************************************"
            j += 1

        if matches(ga.bestIndividual(),i):
            eval_func = 1
        else:
            eval_func = 0

        examples.append(i)

    f = open(name, 'a')

    f.write(str(ga.bestIndividual()))
    f.write("Prediccion " + str(predict(ga.bestIndividual().genomeList)) + "%" + "\n")

    f.close()

if __name__ == "__main__":
    run_main()