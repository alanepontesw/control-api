
#!/bin/sh -x
# sincflow.sh
CURRENT=`git branch | grep "*" | awk '{print $2}'`
git checkout develop
git pull --rebase origin develop
git checkout $CURRENT
git pull --rebase origin develop