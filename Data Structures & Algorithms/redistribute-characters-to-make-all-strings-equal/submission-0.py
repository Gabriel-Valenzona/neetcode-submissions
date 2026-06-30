class Solution:
    def makeEqual(self, words: List[str]) -> bool:
      char_count = defaultdict(int)

      # count char occurrences
      for word in words:
        for c in word:
          char_count[c] += 1
        
      # if char is divisible by len of words, then it is feasible to switch around
      # otherwise, return False
      for count in char_count.values():
        if count % len(words):
          return False
      
      return True
    