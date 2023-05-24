from django.shortcuts import render
from django.http import HttpResponse
from functools import reduce

# Create your views here.


def index(request):
    return render(request,'index.html')


################################## control flow tool #############################################

def if_else(request):
    
    num = int(5)
    
    if num < int(10):
        print('number is less than 10')
    elif num == int(10):
        print("number is equal to 10")
    else:
        print('invalid')
        
    return HttpResponse("Check Terminal")

def for_loop(request):
    
    
    words = ['python', 'laravel', 'dotnet', 'django']
    
    words_val = []
    for i in words:
        words_val.append(i+" "+str(len(i)))
    
    print('\n'.join(words_val))   
    print('\n')
    
    for i in range(0,5):
        print(i)
     
    return HttpResponse("Check Terminal")


def break_continue(request):
    
    words = ['python', 'laravel', 544 , 'dotnet', 'django']
    
    for i in words:
        
        if type(i) == int:
            break
        else:
            print(i)
            continue
    
    return HttpResponse("Check Terminal")

def match(request):
    
    status = 545
    
    match status:
        case 400:
            print("Bad request")
        case 404:
            print("Not found")
        case 418:
            print("I'm a teapot")
        case _:
            print("Something's wrong with the internet")
    
    return HttpResponse("Check Terminal")
 
#################################################### function ######################################################### 
    
def lambda_function(request):
    
    return HttpResponse("Check Terminal")

def lambda_with_filter_map_reduce(request):
    
    # first parameter of filter is function and second one will have list of data.
    
    ages=[10,14,16,18,21,23]
    
    #--------------- filter ---------------------------
    
    adults_ages=list(filter(lambda a: a>18, ages))
    even_num_ages = list(filter(lambda a: a%2 == 0, ages))
    
    for i in adults_ages:
        print("adult ages: "+ str(i))
        
    for j in even_num_ages:
        print('even number ages: '+ str(j)) 
    
    #--------------- map ---------------------------
    
    map_str = list(map(str,ages))
    map_key = list(map(lambda a:'age:'+a, map_str))
    
    for item in map_str:
        print('string : '+ item)
    
    print('\n')  
        
    for item in map_key:
        print(item) 
        
    print('\n')  
    #------------------ reduce ------------------------
    
    #after the calculation previous index value has reduce
    reduce_with_lambda = reduce(lambda x,y : x+y,ages)  

    print(reduce_with_lambda)
    
    return HttpResponse("Check Terminal")


    
    



