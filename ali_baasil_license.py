# Baasil Ali
# 12 / 14 / 2022
#
# This program must store the correct answers
# in a list. From there, the program must read the
# student's answers for each of the 20 questions 
# from a text file and store the ansers in another list.

# Store the correct answers in a list
correct_answers = ['A', 'C', 'A', 'A', 'D', 'B', 'C', 'A', 'C', 'B', 'A', 'D', 'C', 'A', 'D', 'C', 'B', 'B', 'D', 'A']

# Open the student answers file and read the answers into a list
with open('student_answers.txt') as f:
    student_answers = [line.strip() for line in f]

# Initialize a list to store the question numbers of the incorrectly answered questions
incorrect_questions = []

# Initialize variables to store the number of correct and incorrect answers
num_correct = 0
num_incorrect = 0

# Loop through the answers and compare them to the correct answers
for i in range(len(correct_answers)):
    if correct_answers[i] == student_answers[i]:
        num_correct += 1
    else:
        num_incorrect += 1
        incorrect_questions.append(i+1)

# Check if the student passed or failed the exam
if num_correct >= 15:
    print('The student passed the exam.')
else:
    print('The student failed the exam.')

# Print the number of correct and incorrect answers
print('Number of correct answers: %.2f' % num_correct)
print('Number of incorrect answers: %.2f' % num_incorrect)

# Print the question numbers of the incorrectly answered questions
if num_incorrect > 0:
    print('Question numbers of incorrectly answered questions:')
    for i in range(len(incorrect_questions)):
        print(incorrect_questions[i])
