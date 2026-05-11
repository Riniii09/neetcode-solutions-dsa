class Solution:
    def validWordAbbreviation(self, word: str, abbr: str) -> bool:
        if word==abbr:
            return True
        i = 0
        j = 0
        num_seq = 0
        num_list = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]
        while i<len(word) and j < len(abbr):
            if abbr[j] not in num_list:
                if abbr[j] != word[i]:
                    return False
                i = i + 1
                j = j + 1
            else:
                if abbr[j] == "0" and num_seq == 0:
                    return False
                num_seq = 0
                while j < len(abbr) and abbr[j] in num_list:
                    num_seq = (num_seq * 10) + int(abbr[j])
                    j = j + 1
                i = i + num_seq
        if i == len(word) and j == len(abbr):
            return True
        else:
            return False