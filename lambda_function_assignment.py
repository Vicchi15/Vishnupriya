from functools import reduce
def function_1():
    i1=[ ["34587", "Learning Python, Mark Lutz", 4, 40.95], 
           ["98762", "Programming Python, Mark Lutz", 5, 56.80], 
           ["77226", "Head First Python, Paul Barry", 3,32.95],
           ["88112", "Einführung in Python3, Bernd Klein",     3, 24.99]]


    sum1=list(map(lambda i:(i[0],i[2]*i[3]),input1))
    sum2=list(tuple(map(lambda i:(i[0],i[1]+10) if i[1]<100 else(i[0],i[1]),sum1)))
    print(sum2)

def function_2():
    i2=[[1, ("5464", 4, 9.99), ("8274",18,12.99), ("9744", 9, 44.95)],
               [2, ("5464", 9, 9.99), ("9744", 9, 44.95)],
               [3, ("5464", 9, 9.99), ("88112", 11, 24.99)],
               [4, ("8732", 7, 11.99), ("7733",11,18.99), ("88112", 5, 39.95)]]
    o=list(map(lambda x:[x[0]]+list(map(lambda y: y[1]*y[2],x[1:])),i2))
    req_result=list(map(lambda x:[x[0]]+[reduce(lambda y,z:y+z,x[1:])],o))
    print(req_result)
def main():
    function_1()
    function_2()
main()
