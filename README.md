# python-learn

基本的なPythonの利用方法  
機械学習関連  
Azureへのデプロイなどなど  

## install (ubuntu)

pyenvが必要とするモジュールをインストール
```
sudo apt install \
  build-essential libssl-dev zlib1g-dev \
  libbz2-dev libreadline-dev libsqlite3-dev curl llvm \
  libncursesw5-dev tk-dev libxml2-dev libxmlsec1-dev libffi-dev liblzma-dev \
  libopencv-dev git
```

pyenv をインストール  
(https://github.com/pyenv/pyenv#getting-pyenv)  
```
Automatic installer
curl https://pyenv.run | bash
```
※パスを通す

python 3.9.11 を install して 利用する
```
pyenv install 3.9.11
#pyenv local 3.9.11
pyenv global 3.9.11
python -VV
Python 3.9.11 (main, Dec 14 2022, 13:46:15) 
[GCC 9.4.0]
```

## version
```
python -VV
Python 3.9.11 (main, Jun 27 2022, 09:49:05)
[GCC 9.4.0]
```
※linuxで作業

## Python 仮想環境を作成してアクティブにする
```
python -m venv .venv
source .venv/bin/activate
```

## pip コマンド
```
pip install <package name>
pip uninstall <package name>
pip show <package name>
pip list
:
などなど
:
```

## pyenv

```
# インストール可能な一覧
pyenv install --list

# インストール済み一覧
pyenv versions

# 必要なversionをインストール
pyenv install 3.9.11
pyenv install 3.7.13

# バージョンの切り替え (global or local)
pyenv global 3.9.11
pyenv global 3.7.13
pyenv local 3.9.11
  python --version で確認する
```

# azure resource group

```
RG_NAME=az-example-python
LOCATION=japaneast
az group create -n $RG_NAME -l $LOCATION
#az group delete --name $RG_NAME -y
```
