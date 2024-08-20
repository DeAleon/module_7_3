class WordsFinder:
    def __init__(self, *args):
        self.file_names = args

    def get_all_words(self):
        all_words = {}
        for file_ in self.file_names:
            with open(file_, encoding='utf-8') as file:
                text = file.read().lower()
                stop_text = [',', '.', '=', '!', '?', ';', ':', ' - ']
                for i in stop_text:
                    text.replace(i, '')
                all_words[file_] = text.split()
        return all_words

    def find(self, word):
        word = word.lower()
        result = {}
        for key, values in self.get_all_words().items():
            for i in range(len(values)):
                if word == values[i]:
                    result[key] = values.index(word) + 1
            return result

    def count(self, word):
        word = word.lower()
        result = {}
        for key, values in self.get_all_words().items():
            result[key] = values.count(word)
        return result


finder2 = WordsFinder('test_file.txt')
print(finder2.get_all_words())  # Все слова
print(finder2.find('TEXT'))  # 3 слово по счёту
print(finder2.count('teXT'))  # 4 слова teXT в тексте всего
