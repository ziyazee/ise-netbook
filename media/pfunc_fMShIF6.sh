
function getfiles() {
  files=`ls -1 | head -10`
  #statements
}
function setfiles() {

  count=1
  for file in $files

  do
    echo "$file"
    ((count++))
  done
  #statements
}
getfiles
setfiles
