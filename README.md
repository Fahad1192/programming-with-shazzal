# Assigment-2

## Immutable

Immutable is the when no change is possible over time. In Python, if the value of an object cannot be changed over time, then it is known as immutable. Once created, the value of these objects is permanent.

Objects of built-in type that are immutable are:

* Numbers (Integer, Rational, Float, Decimal, Complex & Booleans)
* Strings
* Tuples
* Frozen Sets
* User-Defined Classes (It purely depends upon the user to define the characteristics)

Example:

Creating a Tuple which contains English name of weekdays

`weekdays = ‘Sunday’, ‘Monday’, ‘Tuesday’, ‘Wednesday’, ‘Thursday’, ‘Friday’, ‘Saturday’`

Printing the elements of tuple weekdays

`print(weekdays)`

`Output [1]:  (‘Sunday’, ‘Monday’, ‘Tuesday’, ‘Wednesday’, ‘Thursday’, ‘Friday’, ‘Saturday’)`


tuples are immutable, so you cannot add new elements, hence, using merge of tuples with the # + operator to add a new imaginary day in the tuple ‘weekdays’

`weekdays  +=  ‘Pythonday’`

Printing the elements of tuple weekdays

`print(weekdays)`

`Output [3]: (‘Sunday’, ‘Monday’, ‘Tuesday’, ‘Wednesday’, ‘Thursday’, ‘Friday’, ‘Saturday’, ‘Pythonday’)`
