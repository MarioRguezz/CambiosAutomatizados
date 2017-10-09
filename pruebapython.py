if __name__ == '__main__':
    num =  int(raw_input("What is your number? "))
    n = num % 2
    if n == 0 and (2<= num <=5):
         print('Not Weird jose')
    elif n == 0 and (6<= num <=20):
          print('Weird')
    elif n == 0 and num > 20:
          print("Not Weird")
    elif num % 2 != 0:
          print('Weird')
    elif n != 0:
          print('Weird')
