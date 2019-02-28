#!/bin/sh -x
FB="fix/$1"
git checkout master
git pull --rebase origin master
git checkout -b $FB master
git push origin $FB
