# To Install Package via pip: python3 -m pip install [package name]

# Import Packages
import matplotlib.pyplot as plt
import matplotlib.ticker as ticker
from matplotlib.colors import is_color_like
import numpy as np
from numpy import mean 

# Set Constants
allowed = set('0123456789., ') # Allowed Characters
gpaValues = np.array([])
gpa = np.array([])
semesters = np.array([])
weighting = ''
mode = ''

# Get Data Mode
while True:
    mode = input('\033[1;36m Would you like to graph your semester GPA or your cumulative GPA? (semester/cumulative): ')
    if mode.lower() == 'semester':
        print('\033[1;32m Great, semester GPA it is!')
        break
    elif mode.lower() == 'cumulative':
        print('\033[1;32m Great, cumulative GPA it is!')
        break
    else: 
        print('\033[1;31m Sorry, your input was\'nt understood. Please try again.') 

while True:
    weighting = input('\033[1;36m Would you like to graph your weighted GPA or your unweighted GPA? (weighted/unweighted): ')
    if weighting.lower() == 'weighted':
        print('\033[1;32m Great, weighted GPA will be graphed!')
        break
    elif weighting.lower() == 'unweighted':
        print('\033[1;32m Great, unweighted GPA will be graphed!')
        break
    else: 
        print('\033[1;31m Sorry, your input wasn\'t understood. Please try again.')

while True:
    color = input('\033[1;36m What color would you like the series to take? (red, orange, yellow, green, blue, purple, pink, brown, gray, black, etc.): ')
    if is_color_like(color) == True:
        print('\033[1;32m Great, the color will be ' + color + '!')
        break
    print('\033[1;31m That doesn\'t seem to be a valid color. Please Try Again.')

while True: 
    gpaString = input('\033[1;36m Input your space-separated GPA values: ')
    if gpaString and allowed.issuperset(gpaString):
        gpaValues = gpaString.split()
        break
    print('\033[1;31m Invalid characters entered! Please Try Again: ')


if mode.lower() == 'semester':
    semesters = list(range(1, len(gpaValues) + 1))
    gpa = gpaValues
elif mode.lower() == 'cumulative':
    semesters = list(range(1, len(gpaValues) + 1))
    for i in range(0, len(gpaValues)):
        if i == 0: 
            gpa = np.append(gpa, float(gpaValues[0]))
        else:
          gpa = np.append(gpa, np.mean(np.array(gpaValues[0:i]).astype(float)))    
# Plot Data
plt.plot(semesters, gpa, linestyle = 'solid', marker = '*', color = color)

# Plot Baseline United States GPA Average

# Set Plot Labels
plt.xlabel('Semester')
if weighting.lower() == 'weighted':
    plt.ylabel('Weighted GPA')
    plt.axhline(y = 3.01, color = 'lightslategray', linestyle = '-.')
    plt.legend(['Weighted GPA', 'United States Average Unweighted GPA'])
elif weighting.lower() == 'unweighted':
    plt.ylabel('Unweighted GPA')
    plt.axhline(y = 3.36, color = 'lightslategray', linestyle = '-.')
    plt.legend(['Unweighted GPA', 'United States Average Weighted GPA'])
else:
    plt.ylabel('GPA')
    plt.legend(['GPA', 'United States Average GPA'])

# Set Plot Bounds
plt.ylim(0, 5.5)
plt.xlim(1, len(gpaValues))

# Add Grid Lines of Opacity 0.3
plt.grid(alpha = 0.3)

# Fix Axis Tick Marks
plt.xticks(range(1, len(gpaValues) + 1))

# Show Plot
plt.show() 