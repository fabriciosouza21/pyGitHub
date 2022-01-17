class Process_text():
    cleaner = []

    def add_cleaner(self, cleaner):
        self.cleaner.append(cleaner)

    def run_cleaner(self, text)->str:
        for cleaner in  self.cleaner:
            text = cleaner.clean(text)
        return text
