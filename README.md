# Project Details
Calculator Overview:
For this project, you must create a calculator that works in Roman numerals. Your application should take
an equation as command line parameters and print the resulting number in roman numerals. 

For example, this could be how I call your application and what I’d expect the result to be:
Python main.py (VII + V ) * II + I
XXV

# Expected Errors Detection
Roman numerals do not have concepts of floating-point numbers, negative numbers, or zero. As a result,
the user, me, will not try to input any of these. Similarly, you should not report any of these either:

- [x] 1. If the result of an operation would result in zero, your application should print: “0 does not exist
in Roman numerals.”
- [x] 2. If the result of an operation would result in a floating-point number, your application should
print: “There is no concept of a fractional number in Roman numerals.”
- [x] 3. If the result of an operation would result in a negative number, your application should print:
“Negative numbers can’t be represented in Roman numerals.”
- [x] 4. If the result of an operation would result in a number greater than 3,999, your application
should print: “You’re going to need a bigger calculator.”
5. If the input cannot be parsed, your application should print: “I don’t know how to read this.”
Additional project details are as follows:
- [x] 6. Entry of a number into your application without any operations or other numbers should simply
print the number as their English numeral representation, i.e. VI should print 6.
- [x] 7. Only 4 operations must be supported: addition, subtraction, multiplication, and division.
- [x] 8. The order of operations matters. Multiplication and division should occur before multiplication
and subtraction.
- [x] 9. Two grouping operators may be used in the program input: ( ) and [ ]. Grouping operators take
precedence over multiplication and division.

Error Dections Added:
- [X] No numerals to equate
- [X] Back to Back operators
- [X] Check if there is roman numeral before and after operator.
- [X] User enters nothing 
- [X] User enters just space
- Brackets not working in  eval


# How to run using py script
1) Execute the script in cmd line root directory
```python main [expression here] ```
or
```py -m main [expression here]```


# How to run pytest cov

```python -m pytest --cov .  ```
or
```py -m pytest --cov . ``