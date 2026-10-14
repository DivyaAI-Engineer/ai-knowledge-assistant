# Import Python's operating system library
# This helps us check whether files exist
import os


# Create a function called read_knowledge_file
# It receives a file path as input
def read_knowledge_file(file_path):

    # Check if the file exists
    if not os.path.exists(file_path):

        # Raise an error if file is missing
        raise FileNotFoundError(
            "Knowledge file not found."
        )

    # Open the file in read mode
    with open(file_path, "r") as file:

        # Read all content from file
        content = file.read()

    # Return content back to caller
    return content
