import unittest

from src.chatbot import Chatbot


class TestChatbot(unittest.TestCase):

    def test_bot_name(self):

        bot = Chatbot("AI Assistant")

        self.assertEqual(
            bot.name,
            "AI Assistant"
        )


if __name__ == "__main__":
    unittest.main()
