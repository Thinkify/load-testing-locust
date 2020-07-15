printf "########## Setting up virtualenv, activating it  and installing requirements ##########\n\n"
python3 -m virtualenv .env && source .env/bin/activate && pip3 install -r requirements.txt

printf "########## Setting up pre-commit git hook ##########\n"
git config core.hooksPath .githooks
printf "########## Set up pre-commit git hook ##########\n"
