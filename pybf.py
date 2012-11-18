"""
Very simple brainfuck interpreter.

Run bf program specified on command line
(or default program if no argument given)

Notes:
* if pointer p > pr["M"] it wraps around to 0
* if byte m[p] > mr["B"] it wraps around to 0
* EOF input will terminate program

Example:
python bf.py ",[.,]"
(just echos whatever input given, ctrl+D exits)

This code is free to use as you please with no warranties

by Thomas Burgess Sat Nov 17 21:33:15 CET 2012
"""

import sys

def pybf(prg):
    """
    Interprets brainfuck program "prg" io through std
    """
    pr = {">":+1, "<": -1, "M":30000} # pointer rule
    mr = {"+":+1, "-":-1, "B":256} # memory rule
    P = filter(lambda x: x in ['.', ',', '[', ']', '<', '>', '+', '-'], prg) # Clean up program
    m = [0] * pr["M"] # Memory
    p = 0 # Pointer
    l = 0 # Loop point
    i = 0 # index of current instruction
    while i < len(P):
        s = P[i] # Get current instruction
        p = (p + pr[s]) % pr["M"] if s in pr else p
        m[p] = (m[p] + mr[s]) % mr["B"] if s in mr else m[p]
        if s is ".":
            sys.stdout.write(chr(m[p]))
        elif s is ",":
            try:
                m[p] = ord(sys.stdin.read(1))
            except:
                return # No valid input given
        elif s is "]":
            i = l if m[p] > 0 else i
        elif s is "[":
            l = i
        i += 1

def main(argv = None):
    if argv is None:
        argv = sys.argv
    if len(argv) < 2: # Run default program
        bf("--------[-->+++<]>.------------.+++++++.--.------------.--[--->+<]>--.+++[->+++<]>.[--->+<]>-.---.-----------.--.[--->+<]>----..[->+++++<]>+.--[--->+<]>---.++.+++++++++++.------------.[--->+<]>---.+[->+++<]>.")
    else:
        bf(argv[1])

if __name__ == "__main__":
    sys.exit(main())

