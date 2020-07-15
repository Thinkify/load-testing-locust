printf "########## Setting up virtualenv ##########\n"
python3 -m virtualenv .env
printf "########## Activating virtualenv ##########\n"
source .env/bin/activate
printf "########## Installing requirements ##########\n"
pip3 install -r requirements.txt
printf "########## Setting up pre-commit git hook ##########\n"
git config core.hooksPath .githooks
