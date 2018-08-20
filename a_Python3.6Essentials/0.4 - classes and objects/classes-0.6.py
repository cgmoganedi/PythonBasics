class book:
    def __init__(self, pages):
        self.pages = pages
    def __lt__(self, other):
        return self.pages < other
    def __gt__(self, other):
        return self.pages > other
