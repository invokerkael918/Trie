DIRECTIONS = [(0, -1), (0, 1), (-1, 0), (1, 0)]


class TrieNode:  #定义字典树的节点
    def __init__(self):
        self.children = {}
        self.is_word = False
        self.word = None


class Trie:
    def __init__(self):
        self.root = TrieNode()

    def add(self, word):  # 字典树插入单词
        node = self.root
        for c in word:
            if c not in node.children:
                node.children[c] = TrieNode()  # 在此节点申请节点
            node = node.children[c]  # 继续遍历
        node.is_word = True
        node.word = word  # 存入单词


class Solution:
    """
    @param board: A list of lists of character
    @param words: A list of string
    @return: A list of string
    """

    def wordSearchII(self, board, words):
        # write your code here
        if board is None or len(board) == 0:
            return []

        tree = Trie()
        for word in words:
            tree.add(word)  # 插入单词
        result = set()
        for i in range(len(board)):  # 遍历字母矩阵，将每个字母作为单词首字母开始搜索
            for j in range(len(board[0])):
                c = board[i][j]
                self.search(board, i, j, tree.root.children.get(c), set([(i, j)]), result)

        return list(result)

    def search(self, board, x, y, node, visited, result):  # 在字典树上dfs查找
        # reached out (x,y)
        if node is None:
            return
        if node.is_word:
            result.add(node.word)

        for dx, dy in DIRECTIONS:
            nx = dx + x
            ny = dy + y

            if not self.is_Valid(board, nx, ny):
                continue
            if (nx, ny) in visited:
                continue
            visited.add((nx, ny))
            self.search(board, nx, ny, node.children.get(board[nx][ny]), visited, result)
            visited.remove((nx, ny))

    def is_Valid(self, board, x, y):
        return 0 <= x < len(board) and 0 <= y < len(board[0])
