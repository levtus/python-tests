# To Install Package via pip: python3 -m pip install [package name]

# Import Packages
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

# Set Data
semester = np.array([1, 2, 3, # 4, 5, 6, 7, 8
                     ])
semesterGPA = np.array([3.500, 3.472, 3.614])
semesterWGPA = np.array([4.000, 3.952, 4.186])

# Plot Data
plt.plot(semester, semesterGPA, linestyle = 'solid', marker = '*', color = 'seagreen')
plt.plot(semester, semesterWGPA, linestyle = 'solid', marker = '*', color = 'gold')

# Plot Baseline United States GPA Average
plt.axhline(y = 3.05, color = 'lightslategray', linestyle = '-.')
plt.legend(['Unweighted GPA', 'Weighted GPA', 'United States Average GPA'])

# Set Plot Labels
plt.xlabel('Semester')
plt.ylabel('GPA')

# Set Plot Bounds
plt.ylim(0, 5)
plt.xlim(1, 8)

# Add Grid Lines of Opacity 0.3
plt.grid(alpha = 0.3)

# Show Plot
plt.show() 