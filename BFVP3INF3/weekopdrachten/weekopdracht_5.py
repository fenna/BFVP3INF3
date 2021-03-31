
import re

"""
These are exercises. Do not change the function names, only fill in the parts
that are required. In case of the "here your pattern" you need to use a regular 
expression. An example is given in vraag1
Tip: Test your pattern in a test site such as https://regex101.com/
To learn more about regular expression visit 
https://www.guru99.com/python-regular-expressions-complete-tutorial.html
"""
class Regex:

    def vraag1(self):
        #nothing to be done, this is an example
        """Given this pattern, [ac][df]{2,3} which of the search strings will match?"""
        l = ['ad', 'add', 'abc', 'acdf', 'aaff', 'cdd']
        pat = "[ac][df]{2,3}"

        solution = [word for word in l if re.match(pat, word)]
        print(solution)
        return solution


    def vraag2(self):
        """Given this pattern, [ac]{2,3}[df]{2,3} which of the search strings will match?"""
        import re
        l = ['ad', 'add', 'abc', 'acdf', 'aaff', 'cdd']
        pat = "[ac]{2,3}[df]{2,3}"
        solution = [word for word in l if re.match(pat, word)]
        #print(solution)
        return solution


    def vraag3(self):
        """Given this pattern, [A-Z]?[0-9a-z]{3} which of the search strings will match?"""
        l = ['ad', 'add', 'A000', 'gggg', 'ggggH', 'Q12H', 'R0v1', '15bb']
        pat = "[A-Z]?[0-9a-z]{3}"
        expected = ['add', 'A000', 'gggg', 'ggggH', 'R0v1', '15bb']
        solution = [word for word in l if re.match(pat, word)]
        print(solution)
        assert (solution == expected)
        return solution


    def vraag4(self):
        """Given these strings, what pattern will describe them all?"""
        l = ["aaa", "aba", "aca", "ada"]
        pat = "^a[abcd]a$"
        solution = [word for word in l if re.match(pat, word)]
        assert (solution == l)
        return solution


    def vraag5(self):
        """Given these strings, what pattern will describe them all?"""
        l = ["aad", "aAd", "a2d", "a6D"]
        pat = "^a[aA26][dD]$"
        solution = [word for word in l if re.match(pat, word)]
        assert (solution == l)
        #print(solution)
        return solution


    def vraag6(self):
        """Given these strings, what pattern will describe them all?"""
        l = ["aaad", "aAddd", "aaa2ddd", "a6dD"]
        pat = "^a[aAd26]+[dD]$"
        solution = [word for word in l if re.match(pat, word)] 
        assert (solution == l)

        #print(solution)
        return solution


    def vraag7(self):
        """Given these strings, what pattern will describe them all?"""
        l = ["12a34", "254a1", "011aa56", "878a9"]
        pat = "^\d{2,3}a+\d{,2}$"
        solution = [word for word in l if re.match(pat, word)] 
        assert (solution == l)
        #print(solution)
        return solution


    def vraag8(self):
        """Given these strings, what pattern will describe them all?"""
        l = ["1 &abcdefghijklm", "2 &abcdefgh", "3 &abcdefghi", "4 &abcd"]
        pat = "^[1234] \&[a-z]+$"
        solution = [word for word in l if re.match(pat, word)] 
        assert (solution == l)
        #print(solution)
        return solution


    def vraag9(self):
        """Given these strings, what pattern will describe them all?"""
        l = ["foo 123|", "bar 211\\", "baz 2339|", "eek 831\\"]
        pat = r"^[a-z]{3} \d{3,}[\\\|]+$"
        solution = [word for word in l if re.match(pat, word)]
        #print(solution)
        assert (solution == l)
        return solution


    def vraag10(self):
        """Given these strings, what pattern will describe them all?"""
        l = ["01 Rose programmeur","02 Reindert programmeur","32 Piet systeemmanager","42 Marcel ontwikkelaar"]
        pat = "^\d{2} [A-Z][a-z]+ [a-z]+r$"
        solution = [word for word in l if re.match(pat, word)]
        #print(solution)
        assert (solution == l)
        return solution


    def vraag11(self):
        """
        Given these multiple alignments, define patterns that will describe them as 
        specific as possible and can be used to find new members of the sequence class. 
        The character “-” indicates a gap, this is inserted to keep sequences visually aligned; 
        when testing your regex you should remove these from the sequences.
        list of DNA alignment of transcription factor binding sites that should match
        “GAGA-G-CTCA”, “GAGAAG-CTCA”, “GAGA-GGCTCA”, “AAGAAGGCTCA”, “AAGAAG-CTCA”,
        """
        # DNA alignment of transcription factor binding sites
        l = ["GAGAGCTCA","GAGAAGCTCA","GAGAGGCTCA","AAGAAGGCTCA","AAGAAGCTCA"]
        pat = "[GA]AGA{1,2}G{1,2}CTCA"
        solution = [word for word in l if re.match(pat, word)]

        #print(solution)
        assert (solution == l)
        return solution
        

    def vraag12(self):
        """
        Given these multiple alignments, define patterns that will describe them 
        as specific as possible and can be used to find new members of the sequence class. 
        The character “-” indicates a gap, this is inserted to keep sequences visually aligned; 
        when testing your regex you should remove these from the sequences.
        A protein alignment of a small part of a zinc-binding domain

        “QLHAHAHGL”,“Q-HIHSHGL”,“QIHVHTHAL”,“NLHAHSHGI”,“N-HIHAHAI”,“QIHAHAHAL”
        """
        l = [“QLHAHAHGL”,“QHIHSHGL”,“QIHVHTHAL”,“NLHAHSHGI”,“NHIHAHAI”,“QIHAHAHAL”]
        pat = r"^[QN]$"
        solution = [word for word in l if re.match(pat, word)]
        print(solution)
        return solution


    def vraag13(self):
        """
        Given these multiple alignments, define patterns that will describe them as specific 
        as possible and can be used to find new members of the sequence class. 
        The character “-” indicates a gap, this is inserted to keep sequences visually aligned; 
        when testing your regex you should remove these from the sequences.

        A protein alignment of a hereditary triple-repeat human gene mutation
        “AGQRQRQRTSG”,“AGQRQR–TTG”,“AGQR—-TSA”,“AGNRQRQRTSG”,“AGQRNRQRTTA”,“AGQRNR–TSG”
        """
        l = ["here the allignments"]
        pat = "here your pattern"
        solution = [word for word in l if re.match(pat, word)]
        print(solution)
        return solution


    def vraag14(self):
        """
        Given this list of entries of flower-shops found online:
        Extract the florist’s name, address and city and print them to screen
        """

        pat = "" #here your pattern
        sl = ["Maison du Beau, Gasthuisstraatje 9 9712 AS Groningen", 
        "Attie's Special Flowers, Weerdingerstraat 201 7822 BK Emmen",
        "Bloemen Mozaiek, Van Lenneplaan 115/1 9721 PE Groningen",
        "Alex Aalders Bloemist, Nieuwe Huizen 7 9401 JS Assen", 
        "Groenland Bloemdecoraties, S.O.J. Palmelaan 297 9728 VJ Groningen"]
        """for i,word in enumerate(sl):
            m = re.match(pat,word)
            if m:
                print('name = {:30} address = {:30} city = {:20}'.format(
                m.group(1), m.group(2), m.group(3)) )
            else:
                print(str(i) + ': ' + p + ' not found in ' + w + '!' ) 
        """
        solution = [word for word in sl if re.match(pat, word)]
        print(solution)
        return solution