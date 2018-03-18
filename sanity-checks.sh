#!/bin/bash

redeclarations=$(grep 'from modules\.[a-z_]* import [a-z_]*' modules/*.py)
if [ -n "$redeclarations" ]; then
  echo "By importing another modules functions, you redeclare them."
  echo "This can result in the same function being registered twice."
  echo "Rewrite 'from modules.foo import bar' as 'from modules import foo'."
  echo
  echo "$redeclarations"
  exit 1
fi

exit 0
