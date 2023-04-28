rsync -av --delete -e ssh ../baojunwang/ baojunwanglab@35.198.198.73:~/baojunwang/
ssh -f baojunwanglab@35.198.198.73 "bash ~/baojunwang/build.sh"
