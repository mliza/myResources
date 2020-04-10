#!/usr/local/bin/python3.7
import scipy.constants as physicalConstants

# <---- Length ----> 
def feet2Inches(feet):
    inches = feet / 12
    return inches 

def feet2Meters(feet): 
    meters = 0.3048 * feet 
    return meters 

def miles2Meters(miles):
    meters = 1609.34 * miles 
    return meters 
# <---- Length ---->


# <---- Mass ---->
def kilograms2Pounds(kilograms):
    pounds = 0.45359237 * kilograms
    return pounds

def kilograms2Ounces(kilograms): 
    ounces = 0.0283495231 * kilograms 
    return ounces 
# <---- Mass ----> 


# <---- Pressure ---->
def PSI2Pascals(PSI):
    pascals = (14.696 / 101325) * PSI 
    return pascals 

def pascals2ATM(pascals): 
    atm = 101325 * pascals 
    return atm 
# <---- Pressure ---->


# <---- Temperature ---->
def fahrenheit2Celcius(fahrenheit):
    celcius = (fahrenheit - 32) / 1.8
    return celcius 

def celcius2Fahrenheit(celcius):
    fahrenheit = 1.8 * celcius + 32 
    return fahrenheit 

def celcius2Kelvin(celcius): 
    kelvin = celcius + 273.15 
    return kelvin 

def kelvin2Rankine(kelvin): 
    rankine = 1.8 * kelvin
    return rankine
# <---- Temperature ---->


# <---- Energy ---->
def joules2ElectronVolts(joules):
    electronVolts = joules / physicalConstants.eV  
    return electronVolts 
# <---- Energy ---->
