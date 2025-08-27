#create a question bank

from data import question_data
from question_model import Question
from quiz_brain import QuizBrain

question_bank=[

]
for i in question_data:
    question1=Question(i['question'],i['correct_answer'])
    question_bank.append(question1)
obj=QuizBrain(question_bank)
obj.next_question()
while obj.still_has_questions():
    obj.next_question()
print("You have completed the quiz")
print(f"Your final score was {obj.score}")