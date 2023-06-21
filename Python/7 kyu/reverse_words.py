import os

import pyttsx3


def reverse_words(string: str) -> str:
    """
    Reverses the order of words in a given string.

    Args:
        string: The input string.

    Returns:
        The reversed string where each word is reversed.
    """
    return ' '.join([word[::-1] for word in string.split()])


# Initialize the text-to-speech engine
engine = pyttsx3.init()

# Test the function
input_string = input("Enter a string: ")
reversed_string = reverse_words(input_string)
print("Reversed string:", reversed_string)

# Speak the reversed string
engine.say(reversed_string)

# Save the output audio to a file
output_file = "output.wav"
engine.save_to_file(reversed_string, output_file)
engine.runAndWait()

# Provide the output file path
print("Output file saved:", os.path.abspath(output_file))
