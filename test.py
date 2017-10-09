if [[ `sudo git status -uno` ]]; then
  sudo git add .
  sudo git commit -am "server changes"
  sudo git pull origin master
  sudo git push origin master
else
  echo "no changes available"
fi
