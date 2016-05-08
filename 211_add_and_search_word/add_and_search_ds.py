class WordDictionary:
    # initialize your data structure here.
        
    def __init__(self):
        self.children = {}
        

    # @param {string} word
    # @return {void}
    # Adds a word into the data structure.
    def addWord(self, word):
        node = self
        for c in word:
            if c not in node.children:
                node.children[c] = WordDictionary()
            node = node.children[c]
        node.children['$'] =True
        
    # @param {string} word
    # @return {boolean}
    # Returns if the word is in the data structure. A word could
    # contain the dot character '.' to represent any one letter.
    def search(self, word):
        node = self
        if len(word):
            c = word[0]
            if c == '.':
                for cc in node.children:
                    if cc == '$':
                        continue
                    if node.children[cc].search(word[1:]):
                        return True
                return False
            else:
                if c not in node.children:
                    return False
                return node.children[c].search(word[1:])
        return '$' in self.children
        

# Your WordDictionary object will be instantiated and called as such:
# wordDictionary = WordDictionary()
# wordDictionary.addWord("word")
# wordDictionary.search("pattern")
