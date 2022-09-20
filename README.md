# python-learn

基本的なPythonの利用方法  
機械学習関連  
Azureへのデプロイなどなど  

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