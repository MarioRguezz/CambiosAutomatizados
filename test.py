if [[ `git status -uno` ]]; then
  git add .
  git commit -am "server changes"
  git pull origin master
  git push origin master
else
  echo "no changes available"
fi
