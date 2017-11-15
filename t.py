import functools
print(functools.reduce(lambda x,y:x*y,[i for i in range(5)]))