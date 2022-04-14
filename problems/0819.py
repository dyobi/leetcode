"819. Most Common Word"

# Given a string paragraph and a string array of the banned words banned, return the most frequent word that is not banned. It is guaranteed there is at least one word that is not banned, and that the answer is unique.
# The words in paragraph are case-insensitive and the answer should be returned in lowercase.

# Input: paragraph = "Bob hit a ball, the hit BALL flew far after it was hit.", banned = ["hit"] / Output: "ball"
# Explanation: 
# "hit" occurs 3 times, but it is a banned word.
# "ball" occurs twice (and no other word does), so it is the most frequent non-banned word in the paragraph. 
# Note that words in the paragraph are not case sensitive,
# that punctuation is ignored (even if adjacent to words, such as "ball,"), 
# and that "hit" isn't the answer even though it occurs more because it is banned.

# Input: paragraph = "a.", banned = [] / Output: "a"

class Solution:
    def mostCommonWord(self, paragraph: str, banned: List[str]) -> str:
        
        c = ['.' , ',', '!', '?', '\'', ';']
        
        count = {}
        
        for i in c :
            paragraph = paragraph.replace(i, ' ')
            
        for word in paragraph.lower().split(' ') :
            
            if word != '' and word not in count and word not in banned:
                count[word] = paragraph.lower().split(' ').count(word)
                
        return sorted(count, key = count.get, reverse = True)[0]