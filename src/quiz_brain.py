"""! @file quiz_brain.py
@brief The logic of the quiz: which question is asked next, and how it is asked.
"""

from constants import (
    FEEDBACK_CORRECT_ANSWER,
    FEEDBACK_RIGHT,
    FEEDBACK_SCORE,
    FEEDBACK_WRONG,
    PROMPT_QUESTION,
)
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
        ## @brief The number of questions the player has answered right so far.
        self.score = 0

    def still_has_questions(self) -> bool:
        """! @brief Tells whether there are questions left to ask.
        @return True while `question_number` is below the number of questions, and
        False once every question has been asked.
        """
        return self.question_number < len(self.question_list)

    def next_question(self) -> None:
        """! @brief Asks the player the current question.

        Takes the question at the current position, moves the position on so that
        `question_number` is the number of the question being asked, reads the
        player's answer and checks it.
        @return Nothing.
        """
        current_question = self.question_list[self.question_number]
        self.question_number += 1
        prompt = PROMPT_QUESTION.format(
            number=self.question_number, text=current_question.text
        )
        user_answer = input(prompt)
        self.check_answer(user_answer, current_question.answer)

    def check_answer(self, user_answer: str, correct_answer: str) -> None:
        """! @brief Checks the player's answer and shows how the player is doing.

        The comparison ignores letter case. A right answer adds one to the score;
        any other text counts as wrong. The player sees whether the answer was
        right, the correct answer and the running score, then a blank line.
        @param user_answer The answer the player typed.
        @param correct_answer The correct answer of the question.
        @return Nothing.
        """
        if user_answer.lower() == correct_answer.lower():
            self.score += 1
            print(FEEDBACK_RIGHT)
        else:
            print(FEEDBACK_WRONG)
        print(FEEDBACK_CORRECT_ANSWER.format(answer=correct_answer))
        print(FEEDBACK_SCORE.format(score=self.score, answered=self.question_number))
        print()
