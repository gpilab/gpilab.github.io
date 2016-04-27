#!/bin/bash
# find and replace text in all docs found by grep
FIND=$1
REPLACE=$2
REGEX="s/${FIND}/${REPLACE}/g"

FILES=`git grep -l "$FIND" * `

echo " "
echo "Files:"
echo "$FILES"
echo " "
echo "regex:  $REGEX"
echo " "

read -p "These files will be modified.  Do you want to continue? " -n 1 -r
echo    # (optional) move to a new line
if [[ $REPLY =~ ^[Yy]$ ]]
then
    echo "replacing strings"
    for fn in $FILES
    do
        sed -i -e $REGEX $fn
    done
else
    echo "skipping"
fi

echo " "
echo "Done."
