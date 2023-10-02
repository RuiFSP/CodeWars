"""
Define a method hello that returns "Hello, Name!" to a given name, or says
Hello, World! if name is not given (or passed as an empty String).

Assuming that name is a String and it checks for user typos to return a
name with a first capital letter (Xxxx).

Examples:

* With `name` = "john"  => return "Hello, John!"
* With `name` = "aliCE" => return "Hello, Alice!"
* With `name` not given
  or `name` = ""        => return "Hello, World!"

 """

def hello(name=''):
    return f"Hello, {name.title() or 'World'}!"

if __name__ == "__main__":
    assert hello("John") == "Hello, John!"
    assert hello("aLIce") == "Hello, Alice!"
    assert hello() == "Hello, World!"
    print("All tests Passed!!")
