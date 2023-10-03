""" 
One suggestion to build a satisfactory password is to start with a memorable phrase 
or sentence and make a password by extracting the first letter of each word.

Even better is to replace some of those letters with numbers (e.g., the letter O can be replaced with the number 0):

instead of including i or I put the number 1 in the password;
instead of including o or O put the number 0 in the password;
instead of including s or S put the number 5 in the password.
Examples:
"Give me liberty or give me death"  --> "Gml0gmd" 
"Keep Calm and Carry On"            --> "KCaC0"
"""


def make_password(phrase: str) -> str:
    # Define a dictionary for letter replacements
    replacements = {'i': '1', 'I': '1', 'o': '0', 'O': '0', 's': '5', 'S': '5'}

    pass_builder = []
    
    for word in phrase.split(' '):
        if word[0] in replacements:
            pass_builder.append(replacements.get(word[0]))
        else:
            pass_builder.append(word[0])

    return ''.join(pass_builder)


if __name__ == "__main__":
    assert make_password("Give me liberty or give me death") == "Gml0gmd"
    assert make_password("Keep Calm and Carry On") == "KCaC0"
    print("All tests passed")