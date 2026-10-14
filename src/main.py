# Import JSON library
# Used for saving data
import json

# Import chatbot class
from chatbot import Chatbot

# Import file reading function
from file_handler import read_knowledge_file


# Create Chatbot object
bot = Chatbot("AI Assistant")

# Show greeting
bot.greet()

try:

    # Read knowledge file
    knowledge = read_knowledge_file(
        "../data/knowledge_base.txt"
    )

    # Ask user for question
    question = input(
        "\nAsk a question: "
    )

    # Get chatbot answer
    answer = bot.answer_question(
        question,
        knowledge
    )

    # Print answer
    print("\nAnswer:")
    print(answer)

    # Create dictionary
    interaction = {

        # Store question
        "question": question,

        # Store answer
        "answer": answer
    }

    # Open output file
    with open(
        "../output/chat_history.json",
        "w"
    ) as file:

        # Save dictionary as JSON
        json.dump(
            interaction,
            file,
            indent=4
        )

    # Confirmation message
    print(
        "\nConversation saved successfully."
    )

except Exception as error:

    # Handle unexpected errors
    print(
        "\nSomething went wrong:"
    )

    print(error)
