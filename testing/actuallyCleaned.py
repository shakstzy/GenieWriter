from Phyme import Phyme
import pprint
import lyricsgenius as lg
import string

# from macpath import split
genius = lg.Genius(
    "5iAKokbxLM9hHsS7LiHILuot9sYecAVaXKvMOIQuhKhdNXIhgQo8m6URTG-cPSkM", timeout = 10, retries = 3)
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
        # print(s.lyrics)


def splitIt(artistStorage):
    return artistStorage.split('\n')


def geniusPull(rhymeArtist):
    return genius.search_artist(rhymeArtist, max_songs=20, sort="popularity")


def matching(artistList, cleaned_lst, rhymeWord, returnString):
    temp = set()
    for line in artistList:
        lis = list(line.split(" "))
        length = len(lis)
        lastWord = lis[length-1]
        lastWord = lastWord.translate(
            str.maketrans('', '', string.punctuation))
        for word in cleaned_lst:
            if lastWord == word or lastWord == rhymeWord:
                temp.add(line)
    return temp


def main():
    returnString = set()
    artistStorage = ""
    rhymeWord = pullWord()
    # print(rhymeWord)
    rhymeArtist = pullArtist()
    # print(rhymeArtist)
    cleaned_lst = getRhymes(rhymeWord)
   # print(cleaned_lst)
    # artistStorageWrite(geniusPull(rhymeArtist), artistStorage)
    artist = geniusPull(rhymeArtist)
    for s in artist.songs:
        artistStorage += s.lyrics
    artistList = splitIt(artistStorage)
    # print(artistList)
    returnString = matching(artistList, cleaned_lst, rhymeWord, returnString)
    # print(returnString)
    return returnString


def compute(artist, lyrics):
    returnString = set()
    artistStorage = ""
    rhymeWord = lyrics
    # print(rhymeWord)
    rhymeArtist = artist
    # print(rhymeArtist)
    cleaned_lst = getRhymes(rhymeWord)
   # print(cleaned_lst)
    # artistStorageWrite(geniusPull(rhymeArtist), artistStorage)
    artist = geniusPull(rhymeArtist)
    for s in artist.songs:
        artistStorage += s.lyrics
    artistList = splitIt(artistStorage)
    # print(artistList)
    returnString = matching(artistList, cleaned_lst, rhymeWord, returnString)
    # print(returnString)
    return returnString
