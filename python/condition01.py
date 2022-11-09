number = input("정수입력> ")

last_character = number[-1]

last_number = int(last_character)

if last_number == 0 or last_number % 2 == 0 :
    print("even number")
    
if last_number == 1 or last_number % 2 == 1 :
    print("odd number")