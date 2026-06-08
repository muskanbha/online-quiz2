score = 0

print("Welcome to Online Quiz")

q1 = input("Python is a Programming Language? (yes/no): ")
if q1.lower() == "yes":
    score += 1

q2 = input("HTML stands for Hyper Text Markup Language? (yes/no): ")
if q2.lower() == "yes":
    score += 1

q3 = input("CSS is used for Styling Web Pages? (yes/no): ")
if q3.lower() == "yes":
    score += 1

print("Your Score =", score, "/3")