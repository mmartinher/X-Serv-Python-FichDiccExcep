#!/usr/bin/python
# -*- coding: utf-8 -*-

# Marina Martín Hernández
# Ejercicio 13.4:

fd = open('/etc/passwd','r')
lines = fd.readlines()
dicc = {}

for line in lines:
	element = line.split(':')
	user = element[0]
	shell = element[-1][:-1]
	dicc[user] = shell
print dicc['root']
try:
	print dicc['Imaginary']
except : 
	print ("\nIncorrect User")

