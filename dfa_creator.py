#!/usr/bin/python
#
# Created by Max Marchuk
# View README.md for usage
#

import sys
import jsonpickle

def get_states():
    states = []
    print 'Input a list of states (Hit Enter after each one): '
    while True:
        temp_state = raw_input('State: ')
        if temp_state == '':
            break
        states.append(temp_state)
    return states

def get_alphabet():
    alphabet = []
    print 'Define your alphabet: '
    while True:
        char = raw_input('Character: ')
        if char == '':
            break
        alphabet.append(char)
    return alphabet

def get_transitions(states, alphabet):
    transitions = {}
    print 'Define the mappings for the following states (Hit Enter after each one): '
    for state in states:
        transitions[state] = {}
        for character in alphabet:
            map_string = state + ' -' + character + '-> '
            transitions[state][character] = raw_input(map_string)

    return transitions
 
def get_start_state(states):
    state_string = ', '.join(states)
    start_state = raw_input('Define which state is the starting state (' + state_string + '): ')
    return start_state

def get_accepting_states(states):
    accepting_states = []
    state_string = ', '.join(states)
    print 'Define which states are accepting states (' + state_string + '): '
    while True:
        s = raw_input('State: ')
        if s == '':
            break
        accepting_states.append(s)
    return accepting_states

if __name__ == '__main__':
    dfa = {}

    states = get_states()
    alphabet = get_alphabet()
    transitions = get_transitions(states, alphabet)
    start_state = get_start_state(states)
    accepting_states = get_accepting_states(states)
    
    #request all the information from user
    dfa['states'] = states
    dfa['alphabet'] = alphabet
    dfa['transitions'] = transitions
    dfa['start_state'] = start_state
    dfa['accepting_states'] = accepting_states
    dfa['info'] = raw_input('What is the language that your DFA describes? ')
    
    #throw the DFA into a file
    json_file = open(dfa['info'].replace(' ', '_'), 'w')
    json_file.write(jsonpickle.encode(dfa))

    print 'DFA output into file "' + dfa['info'].replace(' ', '_')
