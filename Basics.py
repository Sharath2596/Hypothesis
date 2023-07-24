

# Print to the console.
print("Hello, world!")
#%%
# Print to the console.
print(22)
#%%
# Simple arithmetic
(5 + 4) / 3
#%%
# Assign variables.
country = 'Brazil'
age = 30

print(country)
print(age)
#%%
# Evaluations
# Double equals signs are used to check equivalency.
10**3 == 1000
#%%
# Evaluations
# A single equals sign is reserved for assignment statements.
10 ** 3 = 1000
#%%
# Evaluations
# Double equals signs are used to check equivalency.
10 * 3 == 40
#%%
# Evaluations
# Double equals signs are used to check equivalency.
10 * 3 == age
#%%
# Conditional statements
if age >= 18:
    print('adult')
else:
    print('minor')
#%%
# Loops
for number in [1, 2, 3, 4, 5]:
    print(number)
#%%
# Loops
my_list = [3, 6, 9]

for x in my_list:
    print(x / 3)
#%%
# Functions
def is_adult(age):

    if age >= 18:
        print('adult')
    else:
        print('minor')
#%%
# Use the function that was just created.
is_adult(18)--
#%%
# Use the function that was just created.
is_adult(17)
#%%
# Use the built-in sorted() function.
new_list = [20, 25, 10, 5]

sorted(new_list)
#%% md
<a name="2"></a>
## 2. [Jupyter Notebooks](https://www.coursera.org/learn/get-started-with-python/lecture/2l42i/jupyter-notebooks)
#%% md
**NOTE:** The import statements cell must be run before running some of the following cells. This setup step was not shown in the instructional video, but you will learn about import statements later in this course.
#%%
# Import statements.
import warnings
warnings.filterwarnings('ignore')

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import seaborn as sns
#%%
# Create a list.
my_list = [10, 'gold', 'dollars']
#%%
# Use the helper function to calculate F1 score used in the following graphics.
def f1_score(precision, recall):
    score = 2*precision*recall / (precision + recall)
    score = np.nan_to_num(score)

    return score
#%%
# Generate a graph of F1 score for different precision and recall scores.
x = np.linspace(0, 1, 101)
y = np.linspace(0, 1, 101)
X, Y = np.meshgrid(x, y)
Z = f1_score(X, Y)
fig = plt.figure()
fig.set_size_inches(10, 10)
ax = plt.axes(projection='3d')
ax.plot_surface(X, Y, Z, rstride=2, cstride=3, cmap='plasma')

ax.set_title('$F_{1}$ of precision, recall', size=18)
ax.set_xlabel('x')
ax.set_ylabel('y')
ax.set_zlabel('z')
ax.view_init(35, -65)
#%% md
**NOTE:** The following cells use markdown (like this cell) to create formatted text like headers and bullets, tables, and mathematical equations. You can select any cell and enter into edit mode to view the markdown text. Then run the cell to view the rendered output.
#%% md
### **Section 2**

* Part 1:
* Part 2:
#%% md
|Title|Author|Date|
|:--|:--|:-:|
|The Art of War|Sun Tzu|5th cent. BCE|
|Don Quixote de la Mancha|Miguel de Cervantes Saavedra|1605|
|Pride and Prejudice|Jane Austen|1813|

#%% md
$$
  \int_0^\infty \frac{x^3}{e^x-1}\,dx = \frac{\pi^4}{15}
$$
#%% md
<a name="3"></a>
## 3. [Object-oriented programming](https://www.coursera.org/learn/get-started-with-python/lecture/1SJMN/object-oriented-programming) 
#%%
# Assign a string to a variable and check its type.
magic = 'HOCUS POCUS'
print(type(magic))
#%%
# Use the swapcase() string method to convert from caps to lowercase.
magic = 'HOCUS POCUS'
magic = magic.swapcase()
magic
#%%
# Use the replace() string method to replace some letters with other letters.
magic = magic.replace('cus', 'key')
magic
#%%
# Use the split() string method to split the string into two strings.
magic = magic.split()
magic
#%%
# Set up the cell to create the `planets` dataframe.
# (This cell was not shown in the instructional video.)
import pandas as pd
data = [['Mercury', 2440, 0], ['Venus', 6052, 0,], ['Earth', 6371, 1],
        ['Mars', 3390, 2], ['Jupiter', 69911, 80], ['Saturn', 58232, 83],
        ['Uranus', 25362, 27], ['Neptune', 24622, 14]
]

cols = ['Planet', 'radius_km', 'moons']

planets = pd.DataFrame(data, columns=cols)
#%%
# Display the `planets` dataframe.
planets
#%%
# Use the shape dataframe attribute to check the number of rows and columns.
planets.shape
#%%
# Use the columns dataframe attribute to check column names.
planets.columns
#%% md
<a name="4"></a>
## 4. [Variables and data types](https://www.coursera.org/learn/get-started-with-python/lecture/k3ex2/variables-and-data-types) 
#%%
# Assign a list containing players' ages.
age_list = [34, 25, 23, 19, 29]
#%%
# Find the maximum age and assign to `max_age` variable.
max_age = max(age_list)
max_age
#%%
# Convert `max_age` to a string.
max_age = str(max_age)
max_age
#%%
# Reassign the value of `max_age`.
max_age = 'ninety-nine'
max_age
#%%
# FIRST, RE-RUN THE SECOND CELL IN THIS VIDEO.
# Check the value contained in `max_age` (SHOULD OUTPUT 34).
max_age
#%%
# Find the minimum age and assign to `min_age` variable.
min_age = min(age_list)

# Subtract `min_age` from `max_age`
max_age - min_age
#%% md
<a name="5"></a>
## 5. [Create precise variable names](https://www.coursera.org/learn/get-started-with-python/lecture/fB03O/create-precise-variable-names) 
#%%
# Trying to assign a value to a reserved keyword will return a syntax error.
else = 'everyone loves some esparagus'
#%%
# The word "asparagus" is misspelled. That's allowed.
esparagus = 'everyone loves some esparagus'
#%%
# Order of operations
2 * (3 + 4)
#%%
# Order of operations
(2 * 3) + 4
#%%
# Order of operations
3 + 4 * 10
#%% md
<a name="6"></a>
## 6. [Data types and conversions](https://www.coursera.org/learn/get-started-with-python/lecture/z9zda/data-types-and-conversions)
#%%
# Addition of 2 ints
print(7+8)
#%%
# Addition of 2 strings
print("hello " + "world")
#%%
# You cannot add a string to an integer.
print(7+"8")
#%%
# The type() function checks the data type of an object.
type("A")
#%%
# The type() function checks the data type of an object.
type(2)
#%%
# The type() function checks the data type of an object.
type(2.5)
#%%
# Implicit conversion
print(1 + 2.5)
#%%
# Explicit conversion (The str() function converts a number to a string.)
print("2 + 2 = " + str(2 + 2))
#%%
