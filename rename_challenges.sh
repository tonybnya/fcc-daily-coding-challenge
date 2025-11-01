#!/usr/bin/env bash

# ======================================
# Script Name : rename_challenges.sh
# Description : Rename files starting with "challenge_" to start with "fcc_"
#               and update corresponding imports inside test files.
# Usage       : ./rename_challenges.sh
# Author      : @tonybnya
# ======================================

# Configuration
OLD_PREFIX="challenge_"
NEW_PREFIX="fcc_"
TEST_DIR="tests"

# ---- STEP 1: Rename the challenge files ----
echo "🔁 Renaming files starting with '$OLD_PREFIX'..."

for file in ${OLD_PREFIX}*; do
    [[ -e "$file" ]] || continue
    new_name="${file/#$OLD_PREFIX/$NEW_PREFIX}"
    mv -- "$file" "$new_name"
    echo "Renamed: '$file' → '$new_name'"
done

# ---- STEP 2: Update imports inside test files ----
echo
echo "🛠 Updating imports in test files under '$TEST_DIR/'..."

# Loop through every test file in the tests directory
find "$TEST_DIR" -type f -name "test_*.py" | while read -r test_file; do
    if grep -q "from ${OLD_PREFIX}" "$test_file"; then
        sed -i "s/from ${OLD_PREFIX}/from ${NEW_PREFIX}/g" "$test_file"
        echo "Updated imports in: $test_file"
    fi
done

echo
echo "✅ All done!"
