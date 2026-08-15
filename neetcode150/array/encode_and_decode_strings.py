"""
LeetCode 271 (Premium) - Encode and Decode Strings
"""


class CodecSol1:
    def encode(self, strs: list[str]) -> str:
        raise NotImplementedError("Implement CodecSol1.encode")

    def decode(self, s: str) -> list[str]:
        raise NotImplementedError("Implement CodecSol1.decode")


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
    # run_basic_tests(CodecSol1)
    # run_basic_tests(CodecSol2)
    pass
