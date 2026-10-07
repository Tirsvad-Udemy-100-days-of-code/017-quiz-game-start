"""! @file main.py
@brief Entry point of the quiz game.

Builds the question bank from the course data and starts the quiz. The quiz is
completed by the later lecture parts.
"""

import logging

from constants import LOG_QUESTIONS_LOADED, QUESTION_KEY_ANSWER, QUESTION_KEY_TEXT
from data import question_data
from question_model import Question
from quiz_brain import QuizBrain

## @brief Logger of this module, for diagnostics only (the quiz uses print and input).
logger = logging.getLogger(__name__)


def build_question_bank(raw_questions: list[dict[str, str]]) -> list[Question]:
    """! @brief Turns the question dictionaries into Question objects.
    @param raw_questions The dictionaries, each with the text and answer of a question.
    @return The question bank: one Question per dictionary, in the order of the data.
    """
    question_bank: list[Question] = []
    for raw_question in raw_questions:
        question_text = raw_question[QUESTION_KEY_TEXT]
        question_answer = raw_question[QUESTION_KEY_ANSWER]
        new_question = Question(question_text, question_answer)
        question_bank.append(new_question)
    return question_bank


def main() -> None:
    """! @brief Builds the question bank and asks the player every question.

    The answers are not checked yet; a later lecture part does that.
    @return Nothing.
    """
    question_bank = build_question_bank(question_data)
    logger.info(LOG_QUESTIONS_LOADED, len(question_bank))
    quiz = QuizBrain(question_bank)
    while quiz.still_has_questions():
        quiz.next_question()


if __name__ == "__main__":
    main()
