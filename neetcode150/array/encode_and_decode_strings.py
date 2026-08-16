"""
LeetCode 271 (Premium) - Encode and Decode Strings
"""


class CodecSol1:
    def encode(self, strs: list[str]) -> str:
        output = []
        for s in strs:
            # TODO-TALK: Encode each string as "<length>#<content>".
            output.append(str(len(s)))
            output.append('#')
            output.append(s)
        return ''.join(output)

    def decode(self, s: str) -> list[str]:
        i = 0
        result = []
        while i < len(s): # cannot be <= because len(s) is where the last i will be
            j = i # at each iteration, j should start with i
            # TODO-TALK: Move j to separator to parse the length prefix.
            while s[j] != '#':
                j += 1 # need this because lengh is not always one digit. can't assume idx 0 is the full length and idx1 is the #
            length = int(s[i:j])
            # TODO-TALK: Read exactly "length" chars after '#'.
            result.append(s[j + 1 : j + 1 + length]) # s[a:b] for b is exclusive
            i = j + 1 + length # this goes to the next start of length, if exists. remember, jth idx is the # right now
        return result


class CodecSol2:
    def encode(self, strs: list[str]) -> str:
        raise NotImplementedError("Implement CodecSol2.encode")

    def decode(self, s: str) -> list[str]:
        raise NotImplementedError("Implement CodecSol2.decode")


def run_basic_tests(codec_class) -> None:
    test_cases = [
        (["lint", "code", "love", "you"]),
        ([""]),
        (["a:b", "c#d", "e f"]),
        ([]),
    ]
    print(f"\nTesting: {codec_class.__name__}")
    passed = 0
    codec = codec_class()
    for strs in test_cases:
        encoded = codec.encode(strs)
        decoded = codec.decode(encoded)
        if decoded == strs:
            passed += 1
            print(f"PASS | strs={strs}")
        else:
            print(f"FAIL | strs={strs} -> decoded {decoded}")
    print(f"Passed {passed}/{len(test_cases)} test cases.")


if __name__ == "__main__":
    run_basic_tests(CodecSol1)
    # run_basic_tests(CodecSol2)

