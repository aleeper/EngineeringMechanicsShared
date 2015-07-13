#!/bin/bash
DIR=$( cd "$( dirname "${BASH_SOURCE[0]}" )" && pwd )

(cd $DIR/.. && git diff-index --name-only --diff-filter=MA --cached HEAD -- | xargs -n 1 sed -i 's/[ \t]*$//')
