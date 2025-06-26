sudo apt install -y make build-essential libssl-dev zlib1g-dev \
  libbz2-dev libreadline-dev libsqlite3-dev curl libncursesw5-dev \
  xz-utils tk-dev libxml2-dev libxmlsec1-dev libffi-dev liblzma-dev

curl https://pyenv.run | bash

export PATH="$HOME/.pyenv/bin:$PATH"
eval "$(pyenv init -)"
eval "$(pyenv virtualenv-init -)"

source ~/.bashrc   # ou ~/.zshrc

pyenv install 3.10.13
# Garanta que o pyenv está usando o Python 3.10.13
pyenv shell 3.10.13

# Agora crie a venv normalmente no diretório atual
python -m venv venv

source venv/bin/activate


sudo apt install python3-virtualenv

# Verifique se o Python 3.10 está instalado
python3.10 --version

# Crie a virtualenv com Python 3.10
python3.10 -m venv venv

virtualenv venv --python=python3.10

# Ative a virtualenv
source venv/bin/activate