#!/bin/bash

echo "Removing rot13 link..."
if rm "$HOME/bin/rot13"; then
    echo -e "\033[32mDone.\033[0m"
else
    echo "Something went wrong."
fi
