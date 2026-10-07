"""! @file constants.py
@brief Constants of the quiz game.

Every literal the program uses is named here, so the other modules contain no
magic strings. Later gateways add the prompt and feedback texts.
"""

from typing import Final

## @brief Key of the question text in a dictionary of `question_data`.
QUESTION_KEY_TEXT: Final = "text"

## @brief Key of the correct answer in a dictionary of `question_data`.
QUESTION_KEY_ANSWER: Final = "answer"

## @brief The answer word of a statement that is true, as written in `question_data`.
ANSWER_TRUE: Final = "True"

## @brief The answer word of a statement that is false, as written in `question_data`.
ANSWER_FALSE: Final = "False"

## @brief Log message for the finished question bank; `%d` is the number of questions.
LOG_QUESTIONS_LOADED: Final = "Loaded %d questions."

## @brief Prompt for one question; `number` is its number and `text` its statement.
PROMPT_QUESTION: Final = "Q.{number}: {text} (True/False)?: "

## @brief Feedback after a right answer.
FEEDBACK_RIGHT: Final = "You got it right!"

## @brief Feedback after a wrong answer.
FEEDBACK_WRONG: Final = "That's wrong."

## @brief Tells the player the correct answer; `answer` is the correct answer.
FEEDBACK_CORRECT_ANSWER: Final = "The correct answer was: {answer}."

## @brief Running score; `score` is the points, `answered` the questions asked so far.
FEEDBACK_SCORE: Final = "Your current score is: {score}/{answered}"

## @brief Message when the last question has been answered.
MESSAGE_QUIZ_COMPLETE: Final = "You've completed the quiz"

## @brief Final score; `score` is the points, `total` the number of questions.
MESSAGE_FINAL_SCORE: Final = "Your final score was: {score}/{total}"
