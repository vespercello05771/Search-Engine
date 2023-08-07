from spellchecker import SpellChecker
import re

class spellCheck():

    def spell_check(sentence) :
        # Create a SpellChecker object
        spell = SpellChecker()
        #to select  or numbers only
        words = re.findall(r'\b\w+\b', sentence)
        corrected_words = []
        for word in words:
            #gives the most likely corrected word based on cotnext
            corrected_word = spell.correction(word)
            if corrected_word is None :
                corrected_word = word
            corrected_words.append(corrected_word)

        corrected_sentence = ' '.join(corrected_words)  

        return corrected_sentence