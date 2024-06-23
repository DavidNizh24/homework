i = 20

while i >= 1:
    print(i)
    i = i - 1




    correct_password = 'luka'
user_input = ''

while correct_password != user_input:
    user_input = input("Please enter your password: ")
    
    if user_input == correct_password:
        print("You succsesfully signed in")
    else:
        print("Password is incorrect")


        i = 0

while i <= 10:
    if i % 2 == 0:
        print(str(i) + " is even")
    else:
        print(str(i) + " is odd")
    i = i + 1