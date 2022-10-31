import pprint

def cleanUp(var):
    returnArr = []
    for item in var.values():
        returnArr.extend(item)
        # returnArr.append(v[1])
        
    return returnArr


from Phyme import Phyme
ph = Phyme()
rhymeWord = input('What word would you like lines for?')
returnString = set()
rhymeTemp = [cleanUp(ph.get_family_rhymes(rhymeWord)), cleanUp(ph.get_perfect_rhymes(rhymeWord)), cleanUp(ph.get_partner_rhymes(rhymeWord)), cleanUp(ph.get_additive_rhymes(rhymeWord)), cleanUp(ph.get_subtractive_rhymes(rhymeWord)), cleanUp(ph.get_substitution_rhymes(rhymeWord)), cleanUp(ph.get_assonance_rhymes(rhymeWord)), cleanUp(ph.get_consonant_rhymes(rhymeWord))]
flattened = [val for sublist in rhymeTemp for val in sublist]
cleaned_lst = [rhyme.split("(")[0] for rhyme in flattened]
# for rhyme in flattened:
#     rhyme = rhyme.split("(")[0]
#     print(rhyme)
print(cleaned_lst)

#print(flattened)


