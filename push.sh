#!/bin/sh -x
# push.sh
CURRENT=`git branch | grep "*" | awk '{print $2}'`
git push origin ${CURRENT}
