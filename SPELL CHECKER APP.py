from spellchecker import SpellChecker
class SpellCheckerApp:
    def __init__(self):
        self.spell = SpellChecker()

    def correct_text(self, text):
        words = text.split()
        corrected_words = []
        for word in words:
           corrected_word = self.spell.correction(word)
           if corrected_word != word.lower():
               print(f"correcting '{word}' to '{corrected_word}'")
               corrected_words.append(corrected_word)

        return ' '.join(corrected_words)
    def run(self):
        print("....WELCOME TO SPELL CHECKER APP....")
        
        while True:
            text = input("enter the text to check or type 'exit' to quit...")
            if text.lower() == 'exit':
                print("...program has been closed...")
                break
            corrected_text = self.correct_text(text)
            print(f"corrected text: {corrected_text}")


if __name__ == "__main__":
    SpellCheckerApp().run()

