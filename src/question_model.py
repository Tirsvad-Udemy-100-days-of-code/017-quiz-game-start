"""! @file question_model.py
@brief The model of one quiz question.
"""


class Question:
    """! @brief One quiz question and its correct answer.

    The text is the statement the player judges as true or false; the answer is
    the word that tells which it is.
    """

    def __init__(self, text: str, answer: str) -> None:
        """! @brief Creates a question.
        @param text The statement shown to the player.
        @param answer The correct answer, as written in the question data.
        """
        ## @brief The statement shown to the player.
        self.text = text
        ## @brief The correct answer to the statement.
        self.answer = answer
