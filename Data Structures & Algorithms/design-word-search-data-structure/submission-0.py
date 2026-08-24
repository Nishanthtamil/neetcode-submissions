class TrieNode:
    def __init__(self):
        self.children={}
        self.endword=False

class WordDictionary:

    def __init__(self):
        self.root=TrieNode()
        

    def addWord(self, word: str) -> None:
        cur=self.root
        for i in word:
            if i not in cur.children:
                cur.children[i]=TrieNode()
            cur=cur.children[i]
        cur.endword=True
        

    def search(self, word: str) -> bool:
        def dfs(i,node):
            if i==len(word):
                return node.endword
            char=word[i]
            if char==".":
                for c in node.children:
                    if dfs(i+1,node.children[c]):
                        return True
                return False
            else:
                if char in node.children:
                    return dfs(i+1,node.children[char])
                else:
                    return False
        return dfs(0,self.root)
        
