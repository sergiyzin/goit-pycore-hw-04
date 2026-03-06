from typing import Callable


#def add(a: int, b: int) -> int:
#    return a + b


#def multiply(a: int, b: int) -> int:
#    return a * b


#def apply(a: int, b: int, operation: Callable[[int, int], int]) -> int:
#    return operation(a, b)


#print("Add:", apply(a=5, b=3, operation=add))
#print("Multiply:", apply(a=5, b=3, operation=multiply))

#from typing import Callable

#def power(exponent: int) -> Callable[[int], int]:
#    def inner(base: int) -> int:
#        return base ** exponent
#    return inner

#square = power(2)
#cube = power(3)

#print("Square", square(4))   # Square 16
#print("Cube", cube(4))       # Cube 64


#def apply_discount(price: float, discount: float) -> float:
#    return price * (1 - discount/100)

#print(apply_discount(price = 500, discount =10))

#def discount(percent: int) -> Callable[[float], float]:
   # def apply(price: float) -> float: 
    #   return price * (1 - percent/100)
    
    #return apply

#ten_off = discount(10)
#twenty_off = discount(20)

#print(twenty_off(500))
#print(ten_off(500))

#from functools import wraps


#def logger(func):
#    @wraps(func)
#    def inner(*args, **kwargs):
#        print(f"Calling {func.__name__} with arguments: {args}, {kwargs}")
#        result = func(*args, **kwargs)
#        print(f"Result: {result}")
#        return result

#    return inner


#@logger
#ef add(x: int, y: int) -> int:
#    return x + y


#add(x=2, y=3)


#current_user = {"name": "Sascha", "role": "interviewer"}
##def admin_only(func):
#    @wraps(func)
#    def wrapper(*args, **kwargs):
#        if current_user["role"] != "admin":
#            print(f"You are not allowed to perform this action.")
#            return None
#        return func(*args, **kwargs)
#    return wrapper

#@admin_only
#def delete_user(user_id: int):
#    print(f"User {user_id} deleted")

##    delete_user(43)


#map (func, (list, tuple, ...))
# lambda agrs: body ->
#numbs = [1, 2, 2, 2, 2, 3, 3, 32, 5, 25]

# Варіант з map + lambda
#squares = list(map(lambda x: x ** 2, numbs))

# Варіант з for
#squares_l = []
#for num in numbs:
#   squares_l.append(num ** 2)
#print(squares)
#print(squares_l)

