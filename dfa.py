#!/usr/bin/python
import sys

def get_states():
    states = []
    print 'Input a list of states (hit the enter key when finished): '
    while True:
        temp_state = raw_input('State: ')
        if temp_state == '':
            print states
            break
        states.append(temp_state)
        print states
    return states

def get_alphabet():
    alphabet = []
    print 'Define your alphabet (Hit the enter key  when finished): '
    while True:
        char = raw_input('Character: ')
        if char == '':
            print alphabet 
            break
        alphabet.append(char)
        print alphabet
    return alphabet

def get_transitions(states, alphabet):
    transitions = {}
    print 'Define the mappings for the following states: '
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
    print '(Hit the enter key when finished)'
    while True:
        s = raw_input('State: ')
        if s == '':
            print accepting_states
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
    
    dfa['states'] = states
    dfa['alphabet'] = alphabet
    dfa['transitions'] = transitions
    dfa['start_state'] = start_state
    dfa['accepting_states'] = accepting_states
    print dfa
