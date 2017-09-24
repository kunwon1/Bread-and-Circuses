import random

def choice(list,nospace=False):
    ret = random.choice(list)
    if nospace:
        return ret
    return ret + ' '


class MakeName(object):

    def __init__(self):
        name = ''
        prefix = [
                'Big',
                'Little',
                'Wide',
                'Narrow',
                'Blue',
                'Green',
                'Dowdy',
                'Feckless',
                'Mean',
                'Coward',
                'Loud',
                'Quiet',
                'Silent',
                'Sagacious',
                'Wise',
                'Old'
                ]

        solomale = [
                'Jim',
                'Bob',
                'Quint',
                'Bart',
                'Victor',
                'Dante',
                'Taj',
                'Omar'
                ]

        solofemale = [
                'Giana',
                'Helga',
                'Zelda',
                'Amelie',
                'Willow'
                ]

        suffix = [
                'The Quick',
                'The Brutal',
                'The Boorish',
                'Thiefmarked',
                'The Convict',
                'The Snake',
                'The Fox',
                'The Mongrel',
                'The Chained'
                ]

        #consonant at the end, or equivlanet
        endcons1 = [
                'ek',
                'eq',
                'er',
                'ew',
                'et',
                'ep',
                'es',
                'ed',
                'edg',
                'edw',
                'en',
                'em',
                'an',
                'am',
                'ang',
                'at',
                'ut',
                'uz',
                'uzz',
                'azz',
                'or',
                'orp',
                'vid',
                ]

        #start and end with vowelsound
        vow1 = [
                'ea',
                'era',
                'erea',
                'aa',
                'uu',
                'ee',
                'ata',
                'utu',
                'uru',
                'ulu',
                'udu',
                'ada',
                'ara',
                'apa',
                'iri',
                'irri',
                'iggi',
                'egga',
                'agga',
                'oo',
                'y'
                ]

        #start with cons sound
        startcons1 = [
                'ta',
                'ra',
                're',
                'pi',
                'ki',
                'ke',
                'we',
                've',
                'vi',
                'da',
                'ma',
                'va',
                'tee',
                'dee',
                'ree',
                'quee',
                'bo',
                'ba',
                'do',
                'vo',
                'hu',
                'ju',
                'fa'
                ]

        sg = random.randint(1,2)

        #TODO
        sg = 1

        if sg == 1:
            die = random.randint(1,1000)

            if die <= 10:
                name += choice(prefix)
                name += choice(solofemale)
                name += choice(suffix, True)
                self.name = name
                return

            if die <= 35:
                name += choice(prefix)
                name += choice(solofemale, True)
                self.name = name
                return

            if die <= 60:
                name += choice(solofemale)
                name += choice(suffix, True)
                self.name = name
                return

            if die <= 100:
                name += choice(prefix)
                name += choice(endcons1, True).title()
                name += choice(vow1, True)
                name += choice(vow1, True)
                self.name = name
                return
            
            if die <= 240:
                name += choice(prefix)
                name += choice(endcons1, True).title()
                name += choice(vow1, True)
                name += choice(startcons1, True)
                self.name = name
                return

            else:
                rounds = random.randint(1,3)
                round = 1

                name += choice(vow1, True).title()

                while round <= rounds:
                    if round == 1:
                        name += choice(startcons1, True)
                        round = round + 1
                    if round == 2:
                        name += choice(endcons1, True)
                        round = round + 1
                    if round == 3:
                        name += choice(vow1, True)
                        round = round + 1
                name = name + ' '

                rounds = random.randint(2,3)
                round = 1

                while round <= rounds:
                    if round == 1:
                        name += choice(startcons1, True).title()
                        round = round + 1
                    if round == 2:
                        name += choice(endcons1, True)
                        round = round + 1
                    if round == 3:
                        name += choice(vow1, True)
                        round = round + 1

                if die >= 990:
                    self.name = name + ' ' + choice(suffix, True)
                    return
                elif die >= 980:
                    self.name = choice(prefix) + name 
                    return
                else:
                    self.name = name
                    return



