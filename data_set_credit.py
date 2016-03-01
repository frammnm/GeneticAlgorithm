# Archivo: data_set_credit.py
# Este archivo contiene el metodo generador del data set de aprobacion de creditos.
# Autores: 
#    - Francisco Martinez 09-10502
#    - Gabriel   Alvarez  09-10029

import sys

def read_data_set(name):
	try:
		f = open(name,'r')
		atributes = [[] for i in range(15)]
		classifier = []
		data = f.readlines()
		for line in data:
			words = line.split(',')
			for i in range(16):
				if i == 15:
					if "\n" in words[i]:
						classifier.append(words[i][:-1])
					else:
						classifier.append(words[i])
				else:
					atributes[i].append(words[i])

		return (atributes,classifier)
		f.close()
		return
	except IOError as e:
		print "I/O error({0}): {1}".format(e.errno, e.strerror)
		sys.exit(1)
