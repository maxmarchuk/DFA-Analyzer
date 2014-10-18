#!/usr/bin/python
#
# Created by Max Marchuk
# View README.md for usage
#

import sys
import jsonpickle

#compare the string to the DFA
def analyze(dfa, str):
    current_state = dfa['start_state']
    for char in str:
        if char not in dfa['alphabet']:
            return False
        current_state = dfa['transitions'][current_state][char] 

    if current_state in dfa['accepting_states']:
        return True
    else:
        return False

def parse_file(filename):
    dfa_file = open(filename, 'r').read()
    return jsonpickle.decode(dfa_file)

if __name__ == '__main__':
    if len(sys.argv) < 3: 
        print 'Correct usage: ./analyze.py <DFA> <Test String>'
    else:
        filename = sys.argv[1]
        string = sys.argv[2]
        dfa_string = parse_file(filename)

        if analyze(dfa_string, string):
            print u'\u2713 "' + string + '" is in the language described by the DFA.'
        else:
            print u'\u2717 "' + string + '" is NOT in the language described by the DFA.'
