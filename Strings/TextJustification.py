class Solution:
    def fullJustify(self, words: list[str], maxWidth: int) -> list[str]:
        result = []
        i = 0
        n = len(words)

        while i < n:
            j = i
            letters = 0

            while j < n and letters + len(words[j]) + (j - i) <= maxWidth:
                letters += len(words[j])
                j += 1

            count = j - i
            spaces = maxWidth - letters

            if j == n or count == 1:
                line = " ".join(words[i:j])
                result.append(line + " " * (maxWidth - len(line)))

            else:
                gaps = count - 1
                base = spaces // gaps
                extra = spaces % gaps

                parts = []

                for k in range(count - 1):
                    parts.append(words[i + k])
                    parts.append(" " * (base + (k < extra)))

                parts.append(words[j - 1])
                result.append("".join(parts))

            i = j

        return result