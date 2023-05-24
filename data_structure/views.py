from django.shortcuts import render
from django.http import HttpResponse


def list_base(request):
    
    # Lists are used to store multiple items in a single variable.
    # Lists are one of 4 built-in data types in Python used to store collections of data, the other 3 are Tuple, Set, and Dictionary, all with different qualities and usage.
    
    list = [1,2,3,4,5,6] #Lists are created using square brackets:
    
    print('basic list: '+str(list), end='\n')
    
    list.append(7) #for append element in list
    print('appaned: '+ str(list))
    
    list.pop() #it is delete last element
    print('pop: '+ str(list))
    
    list.insert(0,'#') # Insert an item at a given position 
    print('insert: '+ str(list))
    
    list.remove('#') # it is removing given element
    print('remove: '+ str(list))
    
    #sort() - arrange elements in accending order
    #popleft() - to delete left element
    
    return HttpResponse('check Terminal')
    
def list_comprehensions(request):
    
    squares = list(map(lambda x: x**2, range(10))) 
    print('squares(method one):'+str(squares))
    
    squares = [x**2 for x in range(10)]
    print('squares(method two):'+str(squares))
    
    print("Double for loop with condition: "+str( [(x,y) for x in [1,2,3] for y in [3,4,5] if x != y] )) # here x is first loop
    
    # above example equivalent:
    # combs = []
    # for x in [1,2,3]:
    #     for y in [3,1,4]:
    #         if x != y:
    #             combs.append((x, y))
    
    return HttpResponse('check Terminal')

def nested_list_comprehensions(request):
    
    matrix = [
        [1, 2, 3, 4],
        [5, 6, 7, 8],
        [9, 10, 11, 12],
    ]
    
    print( [ [row[i] for row in matrix] for i in range(len(matrix[0])) ] ) # here i is first loop
    
    #above example equivalent:
    # transposed = []
    # for i in range(4):
    #     transposed.append([row[i] for row in matrix])

    # output
    # [[1, 5, 9], [2, 6, 10], [3, 7, 11], [4, 8, 12]]
    
    return HttpResponse('check Terminal')
    
