class TrieNode:
    def __init__(self):
        self.children = {}
        self.is_word = False


class WordDictionary:

    def __init__(self):
        # do intialization if necessary
        self.root = TrieNode()

    """
    @param: word: Adds a word into the data structure.
    @return: nothing
    """

    def addWord(self, word):
        # write your code here
        node = self.root
        for c in word:
            if c not in node.children:
                node.children[c] = TrieNode()
            node = node.children[c]
        node.is_word = True

    def find(self, word, index, now):
        if now is None:
            return False
        if index >= len(word):
            return now.is_word

        c = word[index]
        if c == ".":
            for child in now.children:
                if self.find(word, index + 1, now.children[child]):
                    return True
        else:
            return self.find(word, index + 1, now.children.get(c))
        return False

    """
    @param: word: A word could contain the dot character '.' to represent any one letter.
    @return: if the word is in the data structure.
    """

    def search(self, word):
        # write your code here
        if word is None:
            return False
        return self.find(word, 0, self.root)
