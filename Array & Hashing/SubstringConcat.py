class Solution:
    def findSubstring(self, s: str, words: list[str]) -> list[int]:
        if not s or not words:
            return []

        word_len = len(words[0])
        word_count = len(words)
        total_len = word_len * word_count

        if total_len > len(s):
            return []

        # Required frequency of each word
        target = {}

        for word in words:
            target[word] = target.get(word, 0) + 1

        result = []

        # Try each possible alignment
        for offset in range(word_len):
            left = offset
            count = 0
            current = {}

            for right in range(offset, len(s) - word_len + 1, word_len):
                word = s[right:right + word_len]

                if word not in target:
                    current.clear()
                    count = 0
                    left = right + word_len
                    continue

                current[word] = current.get(word, 0) + 1
                count += 1

                # Too many occurrences of this word
                while current[word] > target[word]:
                    left_word = s[left:left + word_len]
                    current[left_word] -= 1
                    left += word_len
                    count -= 1

                # Found a valid concatenation
                if count == word_count:
                    result.append(left)

                    # Move window forward
                    left_word = s[left:left + word_len]
                    current[left_word] -= 1
                    left += word_len
                    count -= 1

        return result