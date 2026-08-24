class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        wordset=set(wordList)
        if endWord not in wordList:
            return 0
        queue=deque([(beginWord,1)])
        while queue:
            words,steps=queue.popleft()
            if words==endWord:
                return steps
            for i in range(len(words)):
                for c in "abcdefghijklmnopqrstuvwxyz":
                    nxtword=words[:i]+c+words[i+1:]
                    if nxtword in wordset:
                        wordset.remove(nxtword)
                        queue.append((nxtword,steps+1))
        return 0