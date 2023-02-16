# Auto-copyright-statements

Consider the function my_copyright3(date, name, email) in 2.All_Copy_right.py
from Lecture 2. Since the parameters name and email have flexible lengths, the format of
the resultant copyright statement easily gets distorted. Now, rewrite the function as
my_copyright4(name, email, date=TODAY) so that the output always looks neat.

The three leftmost and the three rightmost columns of the statement are all “*”,
so do the first and the last rows.

– When name is set as “NAME”, the second row prints “*** programmed by NAME
for MSDM5002 ***”. There are two spaces before “programmed” and two spaces
after “MSDM5002”. The width of this row fixes the width of the statement.

– When date is set as “YYYY-MM-DD”, the third row prints “date: YYYY-MM-DD” at
the center. You can assume that the date always uses this format. Its default value
is TODAY; to initialize it, start the program with the following commands.
from datetime import date
TODAY = str(date.today())

– The fourth row fills the space between the “***” on the two sides with “-”.

– Starting from the fifth row, you need to print a paragraph:
You can use it as you like, but there might be many bugs. If you
find some bugs, please send them to “EMAIL”
when email is set as “EMAIL”.

– The paragraph is left-aligned. You need to determine when to start a new
row. In each row, there are two spaces before the first word and at least two
spaces after the last word.

– A word must not be broken into two rows, and punctuation must not start
a new row. However, email and its enclosing quotation marks are the
exception: they can be broken into two rows at any position so that they fill
as much space in the second-last row as possible.

Your function should give the following results. (Suppose TODAY = '2022-09-01')

>>> my_copyright4('IA', 'ia@ust.hk')
***************************************
*** programmed by IA for MSDM5002 ***
*** date: 2022-09-01 ***
***---------------------------------***
*** You can use it as you like, ***
*** but there might be many bugs. ***
*** If you find some bugs, please ***
*** send them to “ia@ust.hk” ***
***************************************

>>> my_copyright4('Alice & Bob', 'alice@wonder.land',
'2022-12-31')
************************************************
*** programmed by Alice & Bob for MSDM5002 ***
*** date: 2022-12-31 ***
***------------------------------------------***
*** You can use it as you like, but there ***
*** might be many bugs. If you find some ***
*** bugs, please send them to "alice@wonde ***
*** r.land" ***
************************************************

You can assume that the three parameters are always strings.





