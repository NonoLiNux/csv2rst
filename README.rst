*****************************************
csv2rst - convert CSV files to rST markup
*****************************************

Make CSV files readable in a text editor by converting it into
reStructuredText markup.


Usage
=====
::

    $ ./csv2rst.py input.csv output.rst


Example
=======

CSV::

    Gender,First name,Year of birth
    M,Alphonse,1932
    F,Béatrice,1964
    F,Charlotte,1970
    F,Anne-Charlotte,1980

is transformed into the following rST table::

    +--------+----------------+---------------+
    | Gender | First name     | Year of birth |
    +--------+----------------+---------------+
    | M      | Alphonse       | 1932          |
    +--------+----------------+---------------+
    | F      | Béatrice       | 1964          |
    +--------+----------------+---------------+
    | F      | Charlotte      | 1970          |
    +--------+----------------+---------------+
    | F      | Anne-Charlotte | 1980          |
    +--------+----------------+---------------+


License
=======
Make good use ;)
