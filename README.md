## WSL2に環境構築

```bash
sudo apt update && sudo apt install -y make build-essential libssl-dev zlib1g-dev \
libbz2-dev libreadline-dev libsqlite3-dev wget curl llvm libncurses5-dev libncursesw5-dev \
xz-utils tk-dev libffi-dev liblzma-dev python-openssl git
```

## pyenv入れる

```bash
curl https://pyenv.run | bash
```

## pyenvのパスを通す

```bash

echo 'export PATH="$HOME/.pyenv/bin:$PATH"' >> ~/.bashrc
echo 'eval "$(pyenv init --path)"' >> ~/.bashrc
echo 'eval "$(pyenv init -)"' >> ~/.bashrc


#echo 'export PYENV_ROOT="$HOME/.pyenv"' >> ~/.bashrc
#echo 'export PATH="$PYENV_ROOT/bin:$PATH"' >> ~/.bashrc
#echo 'eval "$(pyenv init --path)"' >> ~/.bashrc
#echo 'eval "$(pyenv init -)"' >> ~/.bash_profile
source ~/.bashrc
```

## nvm消した

```bash

export NVM_DIR="$([ -z "${XDG_CONFIG_HOME-}" ] && printf %s "${HOME}/.nvm" || printf %s "${XDG_CONFIG_HOME}/nvm")"
[ -s "$NVM_DIR/nvm.sh" ] && \. "$NVM_DIR/nvm.sh" 
rm -rf ~/.nvm
source ~/.bashrc
```

## python3.10 入れた

```bash
pyenv install 3.10.13
pyenv local 3.10.13
```

## pythonのディレクトリ環境の用意

```bash
python -m venv fastApiTutorial #fastApiTutorial は任意 
source fastApiTutorial/bin/activate #これで仮想に入る
pip install -r requirements.txt # 仮想化でライブラリインストール
deactivate #仮想環境から離脱
```

## validation

pydantic

## pip 最新化

```bash
pip install --upgrade pip
```