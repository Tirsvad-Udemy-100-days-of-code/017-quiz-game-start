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
