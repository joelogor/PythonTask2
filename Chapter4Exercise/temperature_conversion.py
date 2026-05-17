


def celsius_to_fahrenheit(celsius):

    fahrenheit = (9/5)* celsius + 32
    
    return fahrenheit
fahrenheit = 0 
celsius = 0
print("celsius" , "fahrenheit", sep = "  ")
for celsius in range (0,101):
    fahrenheit = celsius_to_fahrenheit(celsius)
    
    print(celsius , fahrenheit, sep = "          ")
    
    

