#from collections import namedtuple

#cat = namedtuple("cat", ["name","age", "owner"])

#cat1 = cat("John", "10", "Karabat")
#print(cat1[2])
#print(f"{cat1.name} is {cat1.age} years old. His owner is {cat1.owner}.")


#from collections import Counter

#marks = [4,23,2,3,32,4,23,3,2,3,4,4,32]
#count = Counter(marks)
#print(count.most_common())

#letters = Counter("Banana")
#print(letters)



#grouped = defaultdict(list)

#for word in words
    #first_letter = word[-1]
    ##grouped[first_letter].append(word)


#print(grouped)
#from collections import defaultdict
#grouped_simple = {}
#words = ["apple", "lemon", "plum", "wold"]

#for word in words:
#    
#    first_letter = word[0]
#    if first_letter not in grouped_simple:
#        grouped_simple[first_letter] = []
#
#    grouped_simple[first_letter].append(word)
#
#print(grouped_simple)

#from collections import defaultdict

#d = defaultdict(int)

#d["apple"] += 3
#d["orange"] += 2
#d["grape"] += 1
#print(dict(d))

# stack, deque
#stack = []
#stack.append("a")
#stack.append("b")
#stack.append("c")
#print(stack)
#print("Last element:", stack[-1])
#
#print(stack.pop())
#print(stack.pop())
#print(stack.pop())

#stack = []
#stack.append("a")
#stack.append("b")
#stack.append("c")
#print("Stack:", stack)
#print("Last element:", stack[-1])

#queue = []
#queue.append("a")
#queue.append("b")
#queue.append("c")

#print(queue.pop(0))
#print(queue.pop(0))
#print(queue.pop(0))
#deque

#def a(): 
##    b()

#def b(): 
#    c()   

#def c(): 
#    print("Hello in c")  

#a()

#from collections import deque

#tasks = [
#    {"type": "fast", "name": "wash dishes"},
#    {"type": "slow", "name": "watch series"},
#    {"type": "fast", "name": "walk with a dog"},
#    {"type": "slow", "name": "read the book"},
#]

#queue = deque()

#for task in tasks:
#    if task["type"] == "fast":
#        queue.appendleft(task)
#    elif task["type"] == "slow":
#        queue.append(task)
#    print(list(queue))

#while queue:
#    t = queue.popleft()
##    print(f"Doing: {t['name']}")

#from decimal import Decimal, ROUND_HALF_UP, ROUND_DOWN

#print(0.1 + 0.2 == 0.3)   # False
#print(0.1 + 0.2)          # 0.30000000000000004 через особливості float [web:8][web:11]

# В Decimal потрібно використовувати крапку, а не кому в рядку!
# Decimal("0,2") викличе помилку InvalidOperation [web:2]
#print(Decimal("0.1") + Decimal("0.2") == Decimal("0.3"))
#print(Decimal("0.1") + Decimal("0.2"))

#price = Decimal("1.3242")

#print(price.quantize(Decimal("0.00")))                         # за замовчуванням ROUND_HALF_EVEN [web:2]
#print(price.quantize(Decimal("0.00"), rounding=ROUND_HALF_UP)) # звичне округлення .5 вгору [web:7][web:10]
#print(price.quantize(Decimal("0.00"), rounding=ROUND_DOWN))    # завжди вниз [web:7]




