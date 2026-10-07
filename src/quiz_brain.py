"""! @file quiz_brain.py
@brief The logic of the quiz: which question is asked next, and how it is asked.
"""

from constants import PROMPT_QUESTION
from question_model import Question


class QuizBrain:
    """! @brief Keeps track of where the player is in the quiz and asks questions."""

    def __init__(self, question_list: list[Question]) -> None:
        """! @brief Creates a quiz over a list of questions.
        @param question_list The questions to ask, in the order they are asked.
        """
        ## @brief How many questions have been asked so far; 0 before the first.
        self.question_number = 0
        ## @brief The questions of the quiz, in the order they are asked.
        self.question_list = question_list

    def next_question(self) -> None:
        """! @brief Asks the player the current question.

        Takes the question at the current position, moves the position on so that
        `question_number` is the number of the question being asked, and reads the
        player's answer. The answer is not checked yet.
        @return Nothing.
        """
        current_question = self.question_list[self.question_number]
        self.question_number += 1
        prompt = PROMPT_QUESTION.format(
            number=self.question_number, text=current_question.text
        )
        # The answer is read but not used yet: a later lecture part checks it.
        input(prompt)
