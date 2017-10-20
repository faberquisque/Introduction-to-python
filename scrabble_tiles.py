import matplotlib.pyplot as plt
import math

### CONSTANTS ###
ROWS = 10
VAL_OFFSET = 0.3
OFFSET = 0.5
VAL_TOTAL_OFFSET = VAL_OFFSET+OFFSET

### DATA PREPARATION ###
tiles = {'rr': (1, 8),'ch': (1,5), 'll': (1, 8), 'u': (5, 1), 'o': (9, 1), 'v': (1, 4), 'ñ': (1, 8), 'q': (1, 5), 'g': (2, 2), 'e': (12, 1), 'd': (5, 2), 'y': (1, 4), 'b': (2, 3), 'h': (2, 4), 'p': (2, 3), 'c': (4, 3), 'n': (5, 1), 'x': (1, 8), 'a': (12, 1), 'r': (5, 1), '#': (2, 0), 's': (6, 1), 'l': (4, 1), 'j': (1, 8), 'z': (1, 10), 'f': (1, 4), 't': (4, 1), 'i': (6, 1), 'm': (2, 3)}
tiles_list=[]
for letter in tiles.keys():
    for rep in range(tiles[letter][0]):
        tiles_list.append(letter)
tiles_list.sort(reverse=True)
COLUMNS = math.ceil(len(tiles_list)/ROWS)

### PLOT LETTERS ###
for y in range(ROWS,0,-1):
    for x in range(COLUMNS):
        if len(tiles_list)>0:
            letter = tiles_list.pop()
            plt.text(x+OFFSET,y-OFFSET,letter.upper(),
                horizontalalignment='center', 
                verticalalignment='center', 
                size = 'large')
            plt.text(x+VAL_TOTAL_OFFSET,y-VAL_TOTAL_OFFSET,tiles[letter][1],
                horizontalalignment='center', 
                verticalalignment='center', 
                size = 'small')

### AXES DRESS-UP ###
plt.grid()
plt.xticks(range(ROWS+1))
plt.yticks(range(COLUMNS+1)) 
plt.tick_params(
    axis='both',          
    which='both',      
    bottom='off',      
    left='off',         
    labelbottom='off',
    labelleft='off') 
plt.tight_layout() 

### OUTPUT ### 
plt.show()
plt.savefig('tiles.png')