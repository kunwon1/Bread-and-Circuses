# Copyright (c) 2017 David J Moore

import random

def Insult():
    c = random.randint(0,100)
    l = []

    if c < 10:
        l.append(GetSingularTarget().capitalize())
        l.append(GetSingularTargetNounJoiner())
        l.append(GetBadNounModifier())
        l.append(GetBadNoun())

        i = ' '.join(l)
        i = i + '!'
        return i

    elif c < 50:
        l.append(GetPluralTarget().capitalize())
        l.append(GetPluralTargetNounJoiner())
        l.append(GetBadNounModifier())
        l.append(GetBadNoun())

        i = ' '.join(l)
        i = i + '!'
        return i

    else:
        l.append(GetYouTarget().capitalize())
        l.append(GetPluralTargetNounJoiner())
        l.append(GetBadNounModifier())
        l.append(GetBadNoun())

        i = ' '.join(l)
        i = i + '!'
        return i


def GetBadNoun():
    BadNouns = ('cheese',
                'fungus',
                'garbage',
                'slop',
                'rats',
                'dogs',
                'criminals',
                'zombies',
                'lawyers')

    return random.choice(BadNouns)


def GetSingularTarget():
    Targets = ('your mother',
               'your father',
               'your sister',
               'your brother',
               'your grandmother',
               'your goldfish',
               'your dog',
               'your face',
               'your family')

    return random.choice(Targets)


def GetPluralTarget():
    Targets = ('your clothes',
               'your feet',
               'your relatives',
               'your smallclothes',
               'your breeches')

    return random.choice(Targets)


def GetYouTarget():
    return 'you'


def GetSingularTargetNounJoiner():
    Joiners = ('smells of',
               'smells like',
               'looks like',
               'is covered with',
               'is similar to',
               'is indistinguishable from',
               'consorts with')

    return random.choice(Joiners)


def GetPluralTargetNounJoiner():
    Joiners = ('smell of',
               'smell like',
               'look like',
               'are covered with',
               'are similar to',
               'are indistinguishable from',
               'consort with')

    return random.choice(Joiners)


def GetBadNounModifier():
    Modifiers = ('smelly',
                 'rotten',
                 'diseased',
                 'suppurating',
                 'festering')

    return random.choice(Modifiers)




