class Solution:
    def romanToInt(self, s: str) -> int:
        result: int = 0

        for i, e in enumerate(s):

            if e == "I":
                if i + 1 <= (len(s) - 1):
                    if s[i + 1] == "V":
                        result += 4
                        continue
                    if s[i + 1] == "X":
                        result += 9
                        continue

                result += 1

            elif e == "V":
                if i - 1 >= 0:
                    if s[i - 1] == "I":
                        continue

                result += 5

            elif e == "X":
                if i - 1 >= 0:
                    if s[i - 1] == "I":
                        continue

                if i + 1 <= (len(s) - 1):
                    if s[i + 1] == "L":
                        result += 40
                        continue
                    elif s[i + 1] == "C":
                        result += 90
                        continue

                result += 10

            elif e == "L":
                if i - 1 >= 0:
                    if s[i - 1] == "X":
                        continue

                result += 50

            elif e == "C":
                if i - 1 >= 0:
                    if s[i - 1] == "X":
                        continue

                if i + 1 <= (len(s) - 1):
                    if s[i + 1] == "D":
                        result += 400
                        continue
                    elif s[i + 1] == "M":
                        result += 900
                        continue

                result += 100
            
            elif e == "D":
                if i - 1 >= 0:
                    if s[i - 1] == "C":
                        continue

                result += 500

            else:
                if i - 1 >= 0:
                    if s[i - 1] == "C":
                        continue

                result += 1000
        
        return result
