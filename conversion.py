def kelvin_to_celcius(temp):
	return temp - 273.15

def celcius_to_fahr(temp):
	return temp * (9/5) +32

def kelvin_to_fahr(temp):
	temp_c = kelvin_to_celcius(temp)
	result = celcius_to_fahr(temp_c)
	return result 

print(" mucho lovo ")

print( " mucho mucho ")

