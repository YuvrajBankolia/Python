questions = [
    ["Which language is used to create Facebook?", "Python", "French", "JavaScript", "PHP", 4],
    ["What is the capital of France?", "London", "Paris", "Berlin", "Madrid", 2],
    ["Who developed the theory of relativity?", "Newton", "Einstein", "Galileo", "Tesla", 2],
    ["What is the largest planet in our solar system?", "Earth", "Mars", "Jupiter", "Venus", 3],
    ["Which element has the chemical symbol 'O'?", "Gold", "Oxygen", "Silver", "Iron", 2],
    ["Which country is known as the Land of Rising Sun?", "China", "Japan", "India", "Thailand", 2],
    ["What is the square root of 64?", "6", "8", "10", "12", 2],
    ["Which programming language is widely used for AI?", "Java", "C++", "Python", "Ruby", 3]
]

# Prize money levels
levels = [1000, 2000, 5000, 10000, 20000, 40000, 80000, 160000]

# Game starts
money = 0
for i in range(len(questions)):
    question = questions[i]
    print(f"\n Question for Rs. {levels[i]} ")
    print(f"a. {question[1]}     b. {question[2]}")
    print(f"c. {question[3]}     d. {question[4]}")
    
    try:
        reply = int(input("Enter the correct answer (1-4): "))
        if reply == question[-1]:  
            print(f" Correct! You have won Rs. {levels[i]}")
            money = levels[i] 
        else:
            print(" Wrong Answer! You lost the game.")
            break
    except ValueError:
        print(" Invalid input! Please enter a number between 1 and 4.")
        break

print(f"\n You take home Rs. {money}! Thanks for playing.")
