def sum2(a, b):
    if(type(a) != int and type(a) != float):
        if(type(b) != int and type(b) != float):
            return("all arguments are not a numbers")
        else:
            return("1st argument is not a number")
    else:
        if(type(b) != int and type(b) != float):
            return("2nd argument is not a number")
    return(a+b)