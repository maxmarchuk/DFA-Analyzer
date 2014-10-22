DFA Creator + Analyzer
=========

DFA Creator + Analyzer is a tool for gathering necessary input for a Deterministic Finite Automata and analyzing strings to determine whether or not they are in that DFA's language.

Requirements
--------------
- [Python](https://www.python.org/)
- [pip](https://pypi.python.org/pypi/pip) or [easy_install](http://docs.ansible.com/easy_install_module.html) (for installing jsonpickle)
- [Jsonpickle](http://jsonpickle.github.io/) - decoding and encoding DFA objects (JSON format)


```sh
$ pip install jsonpickle
or
$ easy_install jsonpickle
```

Usage
----

Create the DFA
```sh
#Creates the DFA and a file containg the DFA
$ python dfa_creator.py

#test a string against the DFA
$ python file_created string_to_test
```
Example
----

```sh
$ python dfa_creator.py 
  Input a list of states (Hit Enter after each one): 
  State: s1
  State: s2
  State:              #Enter to finish listing items
  Define your alphabet: 
  Character: 0
  Character: 1
  Character: 
  Define the mappings for the following states (Hit Enter after each one): 
  s1 -0-> s1
  s1 -1-> s2
  s2 -0-> s1
  s2 -1-> s2
  Define which state is the starting state (s1, s2): s1
  Define which states are accepting states (s1, s2): 
  State: s2
  State: 
  What is the language that your DFA describes? ends with a 1
  DFA output into file "ends_with_a_1"

$ python analyzer.py ends_with_a_1 101
  ✓ "101" is in the language described by the DFA.
$ python analyzer.py ends_with_a_1 100
  ✗ "100" is NOT in the language described by the DFA.
$ ./analyzer.py ends_with_a_1 supercalifragilisticexpialidocious
  ✗ "supercalifragilisticexpialidocious1" is NOT in the language described by the DFA.
```
