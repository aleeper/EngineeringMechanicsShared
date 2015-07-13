#!/bin/bash
CWHITE="\x1B[0m"
CGREEN="\x1B[32m"
CRED="\x1B[31m"

DIR=$( cd "$( dirname "${BASH_SOURCE[0]}" )" && pwd )

# Detect spaces in the path to this directory.
if [ $(echo $DIR | wc -w) != 1 ]; then
  echo -e "${CRED}ERROR:${CWHITE} This folder is in a directory path that contains spaces, which"
  echo -e "       will cause problems with other scripts this project. Please move the folder"
  echo -e "       for this repository to a path that does not contain spaces."
  return
fi

echo -e "********************************************************************************"
echo -e "Adding $DIR to your TEXINPUTS environment variable."
echo -e "********************************************************************************"
export TEXINPUTS=$DIR/common:$DIR/common/packages:$DIR/common/3rdparty: ;

echo -e "Please remember to ${CGREEN}fetch${CWHITE} and ${CGREEN}merge${CWHITE}:"
echo -e "  * Before starting to work."
echo -e "  * Before ${CGREEN}pushing${CWHITE} to the remote."
echo -e "********************************************************************************"

# We'll also set up the git hooks, but we don't need to say anything about it.
(cd $DIR/.git/hooks/ && ln -sf ../../scripts/hooks/pre-commit pre-commit)
(cd $DIR/.git/hooks/ && ln -sf ../../scripts/hooks/post-commit post-commit)

echo -e "All is good, carry on!"
echo -e "********************************************************************************"
