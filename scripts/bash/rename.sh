#!/usr/bin/env bash


for file in .* *; do
# skip current/previous dirs and unresolved wildcards
if [[ "$file"=="grimm*" ]]
  then
    old="grimm.3"
    new="Grimm.S03E"
    newname=${file/grimm.3/Grimm.S03E}
    mv "$file" ./$newname
    # ${string/substring/replacement}
fi
done