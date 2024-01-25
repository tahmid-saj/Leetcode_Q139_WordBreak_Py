class TrieNode:
    def __init__(self):
        self.isWord = False
        self.children = {}

class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        # return self.trieBFS(s, wordDict)

        # self.words = set(wordDict)
        # @cache
        # def recursive(index):
        #     if index < 0: return True

        #     for word in self.words:
        #         if s[index - (len(word) - 1):index + 1] == word and recursive(index - len(word)) == True: return True

        #     return False

        # return recursive(len(s) - 1)

        # return self.bottomUp(s, wordDict)

        return self.trieOptimization(s, wordDict)

    def trieBFS(self, s, wordDict):
        queue = deque([0])
        dp, words = set(), set(wordDict)

        while queue:
            start = queue.popleft()
            if start == len(s):
                return True

            for end in range(start + 1, len(s) + 1):
                if end in dp:
                    continue

                if s[start:end] in words:
                    queue.append(end)
                    dp.add(end)

        return False

    def bottomUp(self, s, wordDict):
        dp = [False for _ in range(len(s))]

        for i in range(0, len(s)):
            for word in wordDict:
                # out of bounds for first word
                if i < len(word) - 1:
                    continue

                # check if first word up to i is of length of word or dp[i - len(word)] is True
                if i == len(word) - 1 or dp[i - len(word)] == True:
                    if s[i - (len(word) - 1) : i + 1] == word:
                        dp[i] = True
                        break

        return dp[-1]
    
    def trieOptimization(self, s, wordDict):
        root = TrieNode()
        for word in wordDict:
            curr = root
            for letter in word:
                if not letter in curr.children:
                    curr.children[letter] = TrieNode()
                curr = curr.children[letter]
            curr.isWord = True

        dp = [False for _ in range(len(s))]
        for i in range(0, len(s)):
            if i == 0 or dp[i - 1] == True:
                curr = root
                for j in range(i, len(s)):
                    if s[j] not in curr.children: break

                    curr = curr.children[s[j]]
                    if curr.isWord == True: dp[j] = True
        
        return dp[-1]
