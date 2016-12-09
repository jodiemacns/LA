From: https://github.com/tartley/python-regex-cheatsheet/blob/master/cheatsheet.rst
------------------------------------------------------------------------

Non-special chars match themselves. Exceptions are special characters:
----------------------------------------------------------------------

- \       Escape special char or start a sequence.
- .       Match any char except newline, see re.DOTALL
- ^       Match start of the string, see re.MULTILINE
- $       Match end of the string, see re.MULTILINE
- []      Enclose a set of matchable chars
- R|S     Match either regex R or regex S.
- ()      Create capture group, & indicate precedence

Quantifiers (append '?' for non-greedy):
----------------------------------------

- {m}     Exactly m repetitions
- {m,n}   From m (default 0) to n (default infinity)
- *       0 or more. Same as {,}
- +       1 or more. Same as {1,}
- ?       0 or 1. Same as {,1}
 
Special sequences:
------------------

- \A  Start of string
- \b  Match empty string at word (\w+) boundary
- \B  Match empty string not at word boundary
- \d  Digit
- \D  Non-digit
- \s  Whitespace [ \t\n\r\f\v], see LOCALE,UNICODE
- \S  Non-whitespace
- \w  Alphanumeric: [0-9a-zA-Z_], see LOCALE
- \W  Non-alphanumeric
- \Z  End of string
- \g<id>  Match prev named or numbered group,
- \a  ASCII Bell (BEL)
- \f  ASCII Formfeed
- \n  ASCII Linefeed
- \r  ASCII Carriage return
- \t  ASCII Tab
- \v  ASCII Vertical tab
- \\  A single backslash
- \xHH   Two digit hexadecimal character goes here
- \OOO   Three digit octal char (or just use an
- \DD    Decimal number 1 to 99, match
