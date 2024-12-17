
#Initialized the variable and used a list of lists
games = [[0, 0, 0],
         [0, 0, 0],     
         [0, 0, 0]]

'''games[0][1] = 1 *this represents assigning a value in a list of lists by setting that specific index value'''

#Gettting a simple grid to show the tic-tac toe map
#Now need to figure out how do we classify what the user will be moving to in tic-tac toe

print("   a  b  c")

for count, row in enumerate(games):
    print(count, row)
    count += 1

#Enumerate returns both the index value and the value of the thing you are ITERATING over

