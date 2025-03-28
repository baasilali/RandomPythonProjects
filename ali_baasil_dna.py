# Baasil Ali
# 12 / 14 / 2022
#
# This is a program that in essence will use a dictionary to 
# and will take in information repeatedly until ENTER
# is pressed. The information will be stored and analyzed.

dnaDictionary = {'TTT': 'Phe', 'TCT': 'Ser', 'TGT': 'Cys', 'TAT': 'Tyr',
'TTC': 'Phe', 'TCC': 'Ser', 'TGC': 'Cys', 'TAC': 'Tyr',
'TTG': 'Leu', 'TCG': 'Ser','TGG': 'Trp', 'TAG': '***',
'TTA': 'Leu', 'TCA': 'Ser', 'TGA': '***','TAA': '***',
'CTT': 'Leu', 'CCT': 'Pro', 'CGT': 'Arg', 'CAT': 'His',
'CTC': 'Leu', 'CCC': 'Pro', 'CGC': 'Arg', 'CAC': 'His',
'CTG': 'Leu', 'CCG': 'Pro', 'CGG': 'Arg', 'CAG': 'Gln',
'CTA': 'Leu', 'CCA': 'Pro', 'CGA': 'Arg', 'CAA': 'Gln',
'GTT': 'Val', 'GCT': 'Ala', 'GGT': 'Gly', 'GAT': 'Asp',
'GTC': 'Val','GCC': 'Ala', 'GGC': 'Gly', 'GAC': 'Asp',
'GTG': 'Val', 'GCG': 'Ala','GGG': 'Gly', 'GAG': 'Glu',
'GTA': 'Val', 'GCA': 'Ala', 'GGA': 'Gly','GAA': 'Glu',
'ATT': 'Ile', 'ACT': 'Thr', 'AGT': 'Ser', 'AAT': 'Asn',
'ATC': 'Ile', 'ACC': 'Thr', 'AGC': 'Ser', 'AAC': 'Asn',
'ATG': 'Met', 'ACG': 'Thr', 'AGG': 'Arg', 'AAG': 'Lys',
'ATA': 'Ile', 'ACA': 'Thr', 'AGA': 'Arg', 'AAA': 'Lys'}

def clean_sequence(s):
    sequence = ''
    lower_case = [chr(ascii) for ascii in range(97, 123)]
    upper_case = [chr(ascii) for ascii in range(65, 91)]

    for letter in s:
        if letter in lower_case:
            sequence += upper_case[lower_case.index(letter)]
        elif letter in upper_case:
            sequence += letter

    return sequence

def main():

    while True:
        sequence = input('Enter a nucleotide sequence, or just press ENTER to quit: ')
        sequence = clean_sequence(sequence)

        if(len(sequence) == 0): break
        if len(sequence) % 3 == 0:
            for i in range(0, len(sequence), 3):
                nucletide = sequence[i:i+3]
                if dnaDictionary.get(nucletide) is not None:
                    print('{0} {1}'.format(nucletide, dnaDictionary.get(nucletide)))
                else:
                    print('{0} {1}'.format(nucletide, 'invalid sequence'))

        else:
            print('You must give complete triples')


main()