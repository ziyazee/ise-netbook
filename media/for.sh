n=$@
for nn in $n
do
  if [ $nn = 'ziya' ]
  then
    continue
  fi
  echo "hello $nn"
done
exit 0
