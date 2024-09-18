def EvenNumbers(n):
    num = []
    for i in n:
      if (i % 2 == 0) :
        num.append(str(i))
    return num
        
def OddNumbers(n):
    apple = []
    for i in n:
      if (i % 2 != 0 ):
        apple.append(str(i))
    return apple