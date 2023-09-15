import streamlit as stream

stream.header("Template codes for loops in python")
stream.subheader("For loop")
stream.write("Here is a classic for loop in python that prints hello, you! 5 times:")

c = '''
    for i in range(5):
        print("hello, you")
    '''
stream.code(c)

stream.subheader("While loop")
stream.write("Here is a classic while loop that will print Hey, You! 7 times:-")

c2 = '''
    i = 0
    while i>=7:
        print("Hey, You!")
     '''
stream.code(c2)