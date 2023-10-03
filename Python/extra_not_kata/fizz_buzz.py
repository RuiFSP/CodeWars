""" When recruiting developers for your team, you often interview people who struggle with basic code. 
There is a famous article talking about
Why can’t programmers…program? where it talks about the “FizzBuzz” problem.

Let’s work on this basic program and make sure that we can do it 😊

Specs
Write a function fizz_buzz which takes a single number as an argument, and returns a list of numbers 
from 1 to that number, but replaces some of them according to these rules:

If the number is divisible by 3, then replace it with ‘Fizz’
If the number is divisible by 5, then replace it with ‘Buzz’
If the number is divisible by both 3 and 5, then replace it with ‘FizzBuzz’
e.g.

fizz_buzz(7)
# => [1, 2, 'Fizz', 4, 'Buzz', 'Fizz', 7] """

def fizz_buzz(num):
    
    print(f"This is the numebr for range {num}")
    
    my_list = []
    
    for i in range(1,num+1):
        if i % 3 == 0 and i % 5 == 0:
            my_list.append("FizzBuzz")
        elif i % 3 == 0:
            my_list.append("Fizz")
        elif i % 5 == 0:
            my_list.append("Buzz")
        else:
            my_list.append(i)
        
    return my_list



if __name__ == "__main__":
    assert len(fizz_buzz(5)) == 5
    assert fizz_buzz(20).count('Fizz') == 5
    assert fizz_buzz(33).count('Buzz') == 4
    assert fizz_buzz(50).count('FizzBuzz') == 3
    print("All tests passed")