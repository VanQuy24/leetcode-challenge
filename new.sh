#!/bin/bash
# Usage: ./new_problem.sh "1. Two Sum"

set -e

if [ -z "$1" ]; then
  echo "❌ Please provide the problem name with number."
  echo '👉 Example: ./new_problem.sh "1. Two Sum"'
  exit 1
fi

INPUT="$1"

# Number = everything before the first dot
NUMBER=$(echo "$INPUT" | awk -F'.' '{print $1}' | xargs)
# Title  = everything after the first dot
TITLE=$(echo "$INPUT" | cut -d'.' -f2- | xargs)

# Build slug:
# 1) remove parentheses/brackets/braces only (keep inside chars)
# 2) remove apostrophes
# 3) replace & with 'and'
# 4) lowercase
# 5) collapse non-alnum to single '-'
# 6) trim leading/trailing '-'
SLUG=$(printf '%s' "$TITLE" \
  | tr -d '()[]{}' \
  | sed "s/'//g; s/&/ and /g" \
  | tr '[:upper:]' '[:lower:]' \
  | sed -E 's/[^a-z0-9]+/-/g; s/^-+//; s/-+$//')

mkdir -p solutions
FILENAME="solutions/${NUMBER}_${SLUG}.py"

if [ -f "$FILENAME" ]; then
  echo "⚠️  File already exists: $FILENAME"
  exit 0
fi

cat > "$FILENAME" <<EOL
"""
Title   : $TITLE
Number  : $NUMBER
Link    : https://leetcode.com/problems/$SLUG/
"""

from typing import List
import time


class Solution:
    def solve(self, *args, **kwargs):
        # TODO: implement solution
        pass


if __name__ == "__main__":
    s = Solution()

    # Add your test cases here
    # Each test case is {"input": (...args...), "expected": ...}
    tests = [
        # Example:
        # {"input": ([2, 7, 11, 15], 9), "expected": [0, 1]},
    ]

    for idx, t in enumerate(tests, 1):
        start = time.perf_counter()
        result = s.solve(*t["input"])
        end = time.perf_counter()
        runtime = (end - start) * 1000  # ms

        if result == t["expected"]:
            print(f"Test {idx}: PASSED in {runtime:.3f} ms")
        else:
            print(f"Test {idx}: FAILED in {runtime:.3f} ms "
                  f"(expected {t['expected']}, got {result})")
EOL


echo "✅ Created: $FILENAME"

# --- Update README.md Progress Tracker ---
if [ -f "README.md" ]; then
  TODAY=$(date +%Y-%m-%d)
  NEW_ENTRY="* [ ] $TODAY | [$NUMBER. $TITLE]($FILENAME)"

  if grep -q "## ✅ Progress Tracker" README.md; then
    awk -v entry="$NEW_ENTRY" '
      BEGIN {inserted=0}
      /^## ✅ Progress Tracker/ {
        print
        getline nextline
        if (nextline ~ /^- \[ \]/) {
          print entry
          print nextline
        } else {
          print entry
          if (nextline != "") print nextline
        }
        inserted=1
        next
      }
      {print}
    ' README.md > README.tmp && mv README.tmp README.md

    echo "📝 Updated Progress Tracker in README.md"
  fi
fi