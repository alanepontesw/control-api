#!/bin/sh -x
FB="feat/$1"
git checkout develop
git pull --rebase origin develop
git checkout -b $FB
git push origin $FB
