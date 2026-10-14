# Create a function that searches knowledge text
def search_knowledge(question, knowledge_text):

    # Convert user question to lowercase
    # Makes searching easier
    question = question.lower()

    # Split file contents into separate lines
    lines = knowledge_text.split("\n")

    # Loop through every line
    for line in lines:

        # Compare question with each line
        if question in line.lower():

            # Return matching line
            return line

    # Return default message if nothing found
    return "Sorry, I could not find information."
