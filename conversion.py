def kelvin_to_celcius(temp):
	'''
	Converts a temperature from Kelvin to Celcius	
	'''
	return temp - 273.15

def celcius_to_fahr(temp):
	'''
	Converts a temperature from Celcius to Fahrenheit
	'''
	return temp * (9/5) +32

def kelvin_to_fahr(temp):
	'''
	Converts a temperature from Kelvin to Fahrenheit,
	via Celcius
	'''
	temp_c = kelvin_to_celcius(temp)
	result = celcius_to_fahr(temp_c)
	return result 

print(" mucho lovo ")

print( " mucho mucho ")

