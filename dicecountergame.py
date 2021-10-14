import random 
score = 0;

answer = input("What is your guess, between 1 and 6? Please type an integer!!")

random_number = random.randint(1,7)

print("You rolled a: " + str(random_number));

if (answer == random_number):
    score += 1;
else:
    score -= 0;

print("Your score is: " + str(score));
