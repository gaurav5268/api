import requests
import random
import matplotlib.pyplot as plt

url = "https://dummyjson.com/users"
data = requests.get(url).json()

students = data["users"][:10]

names = []
scores = []

for student in students:
    names.append(student["firstName"])
    scores.append(random.randint(50, 100))

average_score = sum(scores) / len(scores)
print("Average Score:", average_score)

def plot_chart(names, scores):
    plt.bar(names, scores)
    plt.xlabel("Students")
    plt.ylabel("Scores")
    plt.title("Student Test Scores")
    plt.show()

plot_chart(names, scores)