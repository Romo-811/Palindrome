
user_input = input("Please enter a word to check if it is a Palindrome. ")
front_letter = user_input[0]
back_letter = user_input[len(user_input)-1]
front_index = user_input.find(front_letter)
back_index = user_input.rfind(back_letter)

while back_index > 0:
    if front_letter == back_letter:
        front_index += 1
        back_index -= 1
        front_letter = user_input[front_index]
        back_letter = user_input[back_index]
        front_letter = front_letter
        back_letter = back_letter
    else:
        print(f'{user_input} is not a palindrome')
        break
if front_letter == back_letter:
    print(f'{user_input} is a palindrome')
