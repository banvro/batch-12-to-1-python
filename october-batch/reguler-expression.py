# import re

# txt = """From Wikipedia, the free encyclopedia
# (912)-121-232-343
# Old Python logo, 1990s–2006

# New Python logo, 2006–present

# Guido van Rossum in 2014
# Main article: Python (programming language)
# The programming language Python was conceived in the late 1980s,[1] and its implementation was started in December 1989[2] by Guido van Rossum at CWI in the Netherlands as a successor to ABC capable of exception handling and interfacing with the Amoeba operating system.[3] Van Rossum is Python's principal author, and his continuing central role in deciding the direction of Python is reflected in the title given to him by the Python community, Benevolent Dictator for Life (BDFL).[4][5] (However, Van Rossum stepped down as leader on July 12, 2018.[6]). Python was named after the BBC TV show Monty Python's Flying Circus.[7]

# Python 2.0 was released on October 16, 2000, with many major new features, including a cycle-detecting garbage collector (in addition to reference counting) for memory management and support for Unicode. However, the most important change was to the development process itself, with a shift to a more transparent and community-backed process.[8]

# Python 3.0, a major, backwards-incompatible release, was released on December 3, 2008[9] after a long period of testing. Many of its major features have also been backported to the backwards-compatible, though now-unsupported, Python 2.6 and 2.7.[10]

# Early history
# In February 1991, Van Rossum published the code (labeled version 0.9.0) to alt.sources.[11][12] Already present at this stage in development were classes with inheritance, exception handling, functions, and the core datatypes of list, dict, str and so on. Also in this initial release was a module system borrowed from Modula-3; Van Rossum describes the module as "one of Python's major programming units".[1] Python's exception model also resembles Modula-3's, with the addition of an else clause.[3] In 1994 comp.lang.python, the primary discussion forum for Python, was formed, marking a milestone in the growth of Python's userbase.[1]"""


# ptn = "\d{4}"

# # matches = re.search(ptn, txt)

# # print(matches)


# # matches = re.finditer(ptn, txt)

# # print(matches)

# # for i in matches:
# #     print(i)


# matches = re.findall(ptn, txt)

# print(matches)


# x= """From Wikipedia, the free encyclopedia
# (912)-121-232-343
# Old Python logo, 1990s–2006

# New Python logo, 2006–present
# 9875645342
# Guido van Rossum in 2014
# Main article: Python (programming language)
# The programming language Python was conceived in the late 1980s,[1] and its implementation was started in December 1989[2] by Guido van Rossum at CWI in the Netherlands as a successor to ABC capable of exception handling and interfacing 8673456287with the Amoeba operating system.[3] Van Rossum is Python's principal author, and his continuing central role in deciding the direction of Python is reflected in the title given to him by the Python community, Benevolent Dictator for Life (BDFL).[4][5] (However, Van Rossum stepped down as leader on July 12, 2018.[6]). Python was 1234567890 named after the BBC TV show Monty Python's Flying Circus.[7]

# Python 2.0 was released on October 16, 2000, with many major new features, including a cycle-detecting garbage collector (in addition to reference counting) for memory management and support for Unicode. However, 2874526738 the most important change was to the development process itself, with a shift to a more transparent and community-backed process.[8]

# Python 3.0, a major, backwards-incompatible release, was released on December 3, 2008[9] after a long period of testing. Many of its major features have also been 9897652674 backported to the backwards-compatible, though now-unsupported, Python 2.6 and 2.7.[10]

# Early history
# In February 1991, Van Rossum published the code (labeled version 0.9.0) to alt.sources.[11][12] Already 9856342567 present at this stage in development were classes with inheritance, 5678945345 exception handling, functions, and the core datatypes of list, dict, str and so on. Also in this initial release was a module system borrowed from Modula-3; Van Rossum describes the module as "one of Python's major programming units".[1] Python's exception model also resembles Modula-3's, with the addition of an else clause.[3] In 1994 comp.lang.python, the primary discussion forum for Python, was formed, marking a milestone in the growth of Python's userbase.[1]"""

# ptrn to find numbers:  [9876]\d{9}







import re

txt = """From Wikipedia, the free encyclopedia
(912)-121-232-343
Old Python logo, 1990s–2006
abc@gmail.com
New Python logo, 2006–present
9875645342
Guido van Rossum in 2014
Main article: Python (programming language)
The programming language Python was conceived in the late 1980s,[1] and  abc12@gmail.com its implementation was started in December 1989[2] by Guido van Rossum at CWI in the Netherlands as a successor to ABC capable of exception handling and interfacing 8673456287with the Amoeba operating system.[3] Van xyz123abc@gmail.com Rossum is Python's principal author, and his continuing central role in deciding the direction of Python is reflected in the title given to him by the Python community, abc1xyz23@yahho.in Benevolent Dictator for Life (BDFL).[4][5] (However, Van Rossum stepped down as leader on July 12, 2018.[6]). Python was 1234567890 named after the BBC TV show Monty Python's Flying Circus.[7]

Python 2.0 was released on October 16, 2000, with many major new features, including a cycle-detecting garbage collector (in addition to reference counting) for memory management and support for Unicode. However, 2874526738 the most important change was to the development process itself, with a shift to a more transparent and community-backed process.[8]

Python 3.0, a major, backwards-incompatible release, was released xyz123451823981263@gmail.in on December 3, 2008[9] after a long period of testing. Many of its major features have also been 9897652674 backported to the backwards-compatible, though now-unsupported, Python 2.6 and 2.7.[10]

Early history
In February 1991, Van Rossum published the code (labeled version 0.9.0) to alt.sources.[11][12] Already 9856342567 present at this stage in development were classes with inheritance, 5678945345 exception handling, functions, and the core datatypes of list, dict, str and so on. Also in this initial release was a module system borrowed from Modula-3; Van Rossum describes the module as "one of Python's major programming units".[1] Python's exception model also resembles Modula-3's, with the addition of an else clause.[3] In 1994 comp.lang.python, the primary discussion forum for Python, was formed, marking a milestone in the growth of Python's userbase.[1]"""

p = "[a-z]+[0-9]*[a-z]*[0-9]*[@][a-z]+[.][a-z]{2,}"

d = re.findall(p, txt)

print(d)