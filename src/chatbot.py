# Create chatbot blueprint
class Chatbot:

    # Constructor method
    # Runs automatically when object is created
    def __init__(self, name):

        # Save chatbot name
        self.name = name

    # Greeting method
    def greet(self):

        # Display chatbot name
        print(f"Hello, I am {self.name}")

    # Method to answer questions
    def answer_question(
        self,
        question,
        knowledge_text
    ):

        # Import search function
        from knowledge_search import search_knowledge

        # Search knowledge base
        answer = search_knowledge(
            question,
            knowledge_text
        )

        # Return answer
        return answer
