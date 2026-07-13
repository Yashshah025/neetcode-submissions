import json
class Solution:

    def encode(self, strs: List[str]) -> str:
        # result = ""
        # for num in strs:
        #     x = len(num)
        #     result += str(x) + "*" + num
        # return result
        return json.dumps(strs)
    def decode(self, s: str) -> List[str]:
        # ans  = []
        # for i in range(2, len(s) + 1):
        #     x = s[i: int(s[i-2])]
        #     i = i + int(s[i-2])
        #     ans.append(x)
        # return ans
        return json.loads(s)