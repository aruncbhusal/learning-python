# This file contains a list of dictionaries which contain the
# question and the answer, that will be converted into Question object
# in the quiz.py file. These are copied from the course:

# question_data = [
# {"text": "A slug's blood is green.", "answer": "True"},
# {"text": "The loudest animal is the African Elephant.", "answer": "False"},
# {"text": "Approximately one quarter of human bones are in the feet.", "answer": "True"},
# {"text": "The total surface area of a human lungs is the size of a football pitch.", "answer": "True"},
# {"text": "In West Virginia, USA, if you accidentally hit an animal with your car, you are free to take it home to eat.", "answer": "True"},
# {"text": "In London, UK, if you happen to die in the House of Parliament, you are entitled to a state funeral.", "answer": "False"},
# {"text": "It is illegal to pee in the Ocean in Portugal.", "answer": "True"},
# {"text": "You can lead a cow down stairs but not up stairs.", "answer": "False"},
# {"text": "Google was originally called 'Backrub'.", "answer": "True"},
# {"text": "Buzz Aldrin's mother's maiden name was 'Moon'.", "answer": "True"},
# {"text": "No piece of square dry paper can be folded in half more than 7 times.", "answer": "False"},
# {"text": "A few ounces of chocolate can to kill a small dog.", "answer": "True"}
# ]

# The above list was used to create the quiz, but we can also try some other source for the questions,
# like the open trivia database ( opentb.com ) and generate an API which is a URL that generates a JSON file.
# This JSON file closely resembles the structure of a Python dictionary so we can just reformat that and get a similar format
# as above. I will now do it all from scratch rather than just copying from the course files.

question_data = [
    {
      "type": "boolean",
      "difficulty": "easy",
      "category": "Science: Computers",
      "question": "Ada Lovelace is often considered the first computer programmer.",
      "correct_answer": "True",
      "incorrect_answers": [
        "False"
      ]
    },
    {
      "type": "boolean",
      "difficulty": "easy",
      "category": "Science: Computers",
      "question": "'HTML' stands for Hypertext Markup Language.",
      "correct_answer": "True",
      "incorrect_answers": [
        "False"
      ]
    },
    {
      "type": "boolean",
      "difficulty": "easy",
      "category": "Science: Computers",
      "question": "Time on Computers is measured via the EPOX System.",
      "correct_answer": "False",
      "incorrect_answers": [
        "True"
      ]
    },
    {
      "type": "boolean",
      "difficulty": "easy",
      "category": "Science: Computers",
      "question": "Pointers were not used in the original C programming language; they were added later on in C++.",
      "correct_answer": "False",
      "incorrect_answers": [
        "True"
      ]
    },
    {
      "type": "boolean",
      "difficulty": "easy",
      "category": "Science: Computers",
      "question": "The NVidia GTX 1080 gets its name because it can only render at a 1920x1080 screen resolution.",
      "correct_answer": "False",
      "incorrect_answers": [
        "True"
      ]
    },
    {
      "type": "boolean",
      "difficulty": "easy",
      "category": "Science: Computers",
      "question": "The Windows ME operating system was released in the year 2000.",
      "correct_answer": "True",
      "incorrect_answers": [
        "False"
      ]
    },
    {
      "type": "boolean",
      "difficulty": "easy",
      "category": "Science: Computers",
      "question": "RAM stands for Random Access Memory.",
      "correct_answer": "True",
      "incorrect_answers": [
        "False"
      ]
    },
    {
      "type": "boolean",
      "difficulty": "easy",
      "category": "Science: Computers",
      "question": "The logo for Snapchat is a Bell.",
      "correct_answer": "False",
      "incorrect_answers": [
        "True"
      ]
    },
    {
      "type": "boolean",
      "difficulty": "easy",
      "category": "Science: Computers",
      "question": "The Windows 7 operating system has six main editions.",
      "correct_answer": "True",
      "incorrect_answers": [
        "False"
      ]
    },
    {
      "type": "boolean",
      "difficulty": "easy",
      "category": "Science: Computers",
      "question": "The programming language 'Python' is based off a modified version of 'JavaScript'.",
      "correct_answer": "False",
      "incorrect_answers": [
        "True"
      ]
    }
]