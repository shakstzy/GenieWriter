import pprint
import lyricsgenius as lg
import string

# from macpath import split
genius = lg.Genius("5iAKokbxLM9hHsS7LiHILuot9sYecAVaXKvMOIQuhKhdNXIhgQo8m6URTG-cPSkM")
from Phyme import Phyme
ph = Phyme()

def cleanUp(var):
    returnArr = []
    for item in var.values():
        returnArr.extend(item)
        # returnArr.append(v[1])
        
    return returnArr

def pullWord():
    return input('What word would you like lines for?')

def pullArtist():
    return input('What artist would you like to imitate?')

def getRhymes(rhymeWord):
    return [rhyme.split("(")[0] for rhyme in [val for sublist in [cleanUp(ph.get_perfect_rhymes(rhymeWord)), cleanUp(ph.get_family_rhymes(rhymeWord)), cleanUp(ph.get_additive_rhymes(rhymeWord)), cleanUp(ph.get_subtractive_rhymes(rhymeWord)), cleanUp(ph.get_assonance_rhymes(rhymeWord))] for val in sublist]]

def artistStorageWrite(artist, artistStorage):
    for s in artist.songs:
        artistStorage += s.lyrics

def splitIt(artistStorage):
    return artistStorage.split('\n')

def geniusPull(rhymeArtist):
    return genius.search_artist(rhymeArtist, max_songs=20, sort="popularity")

def matching(artistList, cleaned_lst, rhymeWord, returnString):
    for line in artistList:
        lis = list(line.split(" "))
        length = len(lis)
        lastWord = lis[length-1]
        lastWord = lastWord.translate(str.maketrans('', '', string.punctuation))
        for word in cleaned_lst:
            if lastWord == word or lastWord == rhymeWord:
                returnString.add(line)

def main():
    returnString = set()
    artistStorage = ""
    rhymeWord = pullWord()
    rhymeArtist = pullArtist()
    cleaned_lst = getRhymes(rhymeWord)
    print(cleaned_lst)
    artistStorageWrite(geniusPull(rhymeArtist), artistStorage)
    artistList = splitIt(artistStorage)
    matching(artistList, cleaned_lst, rhymeWord, returnString)
    print(returnString)

main()







