class Solution:
    result = list()

    def expand(self, S):
        result = list()
        if S is None or len(S) == 0:
            return result
        self.result = list()
        # form the blocks

        blocks = list()
        i = 0
        while i < len(S):
            block = list()
            if S[i] == "{":
                i += 1
                while S[i] != "}":
                    if S[i] != ",":
                        block.append(S[i])
                    i += 1
                # i += 1
            else:
                block.append(S[i])
            i += 1
            blocks.sort()
            blocks.append(block)

        self.backtrack(blocks, 0, path=[])
        arr = [None] * len(self.result)

        for k in range(len(self.result)):
            arr[k] = self.result[k]
        # arr.sort()
        return arr

    def backtrack(self, blocks, index, path):
        # base
        if index == len(blocks):
            self.result.append("".join(path))
            return
        # logic
        block = blocks[index]

        for i in range(len(block)):
            char = block[i]
            # action
            path.append(char)
            # recurse
            self.backtrack(blocks, index + 1, path)
            # backtrack
            path.pop()


s = "{a,b}c{d,e}f"
s1 = "abcd"
if __name__ == "__main__":
    obj = Solution()
    print(obj.expand(s))
    print(obj.expand(s1))

# Backtrack Recursion
# Time Complexity: O(k^n)
# Space Complexity: O(n)
