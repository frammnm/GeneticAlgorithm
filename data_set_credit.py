# Archivo: data_set_credit.py
# Este archivo contiene el metodo generador del data set de aprobacion de creditos.
# Autores: 
#    - Francisco Martinez 09-10502
#    - Gabriel   Alvarez  09-10029

import sys

def read_data_set(name):
	try:
		f = open(name,'r')
		res = []
		data = f.readlines()
		list1 = [] 
		list2 = [] 
		list7 = [] 
		list10 = [] 
		list13 = [] 
		list14 = [] 
		for line in data:
			atributes = []
			words = line.split(',')
			i = 0
			for w in words:
				if w == "?":
					i += 1
					continue
				if i == 1 : 
					list1.append(w)
				elif i == 2 : 
					list2.append(w)
				elif i == 7 : 
					list7.append(w)
				elif i == 10 :
					list10.append(w)
				elif i == 13 :
					list13.append(w)
				elif i == 14 : 
					list14.append(w) 
				atributes.append(w)
				i += 1
			res.append(atributes)
		f.close()

		print  "max atr 1 : " + str(max(list1)) + " min atr 1 :" + str(min(list1)) + "rangos: " +  str(float(min(list1)) + (float(max(list1)) - float(min(list1)))/3) + ", " + str(float(min(list1)) + 2*((float(max(list1))-float(min(list1)))/3)) 
		print  "max atr 2 : " + str(max(list2)) + " min atr 2 :" + str(min(list2)) + "rangos: " +  str(float(min(list2)) + (float(max(list2)) - float(min(list2)))/3) + ", " + str(float(min(list2)) + 2*((float(max(list2))-float(min(list2)))/3)) 
		print  "max atr 3 : " + str(max(list7)) + " min atr 3 :" + str(min(list7)) + "rangos: " +  str(float(min(list7)) + (float(max(list7)) - float(min(list7)))/3) + ", " + str(float(min(list7)) + 2*((float(max(list7))-float(min(list7)))/3)) 
		print  "max atr 4 : " + str(max(list10)) + " min atr 4 :" + str(min(list10)) + "rangos: " +  str(float(min(list10)) + (float(max(list10)) - float(min(list10)))/3) + ", " + str(float(min(list10)) + 2*((float(max(list10))-float(min(list10)))/3)) 
		print  "max atr 5 : " + str(max(list13)) + " min atr 5 :" + str(min(list13)) + "rangos: " +  str(float(min(list13)) + (float(max(list13)) - float(min(list13)))/3) + ", " + str(float(min(list13)) + 2*((float(max(list13))-float(min(list13)))/3)) 
		print  "max atr 6 : " + str(max(list14)) + " min atr 6 :" + str(min(list14)) + "rangos: " +  str(float(min(list14)) + (float(max(list14)) - float(min(list14)))/3) + ", " + str(float(min(list14)) + 2*((float(max(list14))-float(min(list14)))/3))

		return res
	except IOError as e:
		print "I/O error({0}): {1}".format(e.errno, e.strerror)
		sys.exit(1)


read_data_set("data_set/crx.data")