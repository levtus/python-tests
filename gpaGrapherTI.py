import ti_plotlib as plt
from ti_system import *
from random import *

x=[]
y=[]

plt.cls()
print('\033[1;36m Welcome to GPA Grapher!')
print('\033[1;36m This program will graph your GPA over time.')

# Set Constants
allowed = set('0123456789., ') # Allowed Characters


while True:
    weighting = input('\033[1;36m Would you like to graph your weighted GPA or your unweighted GPA? (1 (weighted), 2 (unweighted)): ')
    if weighting == 1:
        print('\033[1;32m Great, weighted GPA will be graphed!')
        break
    elif weighting == '2':
        print('\033[1;32m Great, unweighted GPA will be graphed!')
        break
    else: 
        print('\033[1;31m Sorry, your input wasn\'t understood. Please try again.')

while True:
    color = input('\033[1;36m Pick a Series Color (1 (red), 2 (orange), 3 (yellow), 4 (green), 5 (blue), 6 (black)): ')
    if color == 1:
        plt.color(255, 0, 0)
        print('\033[1;32m Color Red Selected.')
        break
    elif color == 2:
        plt.color(255, 128, 0)
        print('\033[1;32m Color Orange Selected.')
        break
    elif color == 3:
        plt.color(255, 216, 0)
        print('\033[1;32m Color Yellow Selected.')
        break
    elif color == 4:
        plt.color(0, 128, 64)
        print('\033[1;32m Color Green Selected.')
        break
    elif color == 5:
        plt.color(0, 64, 128)
        print('\033[1;32m Color Blue Selected.')
        break
    elif color == 6:
        plt.color(16, 16, 16)
        print('\033[1;32m Color Black Selected.')
        break
    else
        print('\033[1;31m That doesn\'t seem to be a valid color. Please Try Again.')

while True: 
    gpaString = input('\033[1;36m Input your space-separated GPA values: ')
    if gpaString and allowed.issuperset(gpaString):
        gpaValues = gpaString.split()
        break
    print('\033[1;31m Invalid characters entered! Please Try Again: ')
    
if weighting == 1:
    plt.labels("Semester", "Weighted GPA")
elif weighting == 2:
    plt.labels("Semester", "Unweighted GPA")
else:
    plt.labels("Semester", "GPA")

x = range(1, len(gpaValues) + 1)
y = gpaValues
plt.auto-window(x, y)
plt.axes("on")
plt.show_plot()