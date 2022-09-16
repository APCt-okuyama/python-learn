# auzre functions へデプロイ

Flaskアプリとしてデプロイする

## Azure Functions
( pythonを利用するので `--os-type linux` を指定します。 検証目的なので従量課金)
```
# azure storage
az storage account create -n funcstorage0001 -g $RG_NAME -l $LOCATION --sku Standard_LRS --kind StorageV2
az storage account show-connection-string -g $RG_NAME -n funcstorage0001 -o tsv
# azure functions
az functionapp create -g $RG_NAME --consumption-plan-location $LOCATION --runtime python --runtime-version 3.9 --functions-version 4 --name my-example-func-py --os-type linux --storage-account funcstorage0001
```

※従量課金プランで作成しているので開発中は不用意にスケーリングされないようにScaleLimitを設定しておきます。
```
az resource update --resource-type Microsoft.Web/sites -g $RG_NAME -n my-example-func-py/config/web --set properties.functionAppScaleLimit=1
```

# functions作成

Python 仮想環境を作成してアクティブにする
```
python -m venv .venv
source .venv/bin/activate
```

functionsのプロジェクトを作成してHttpTrigger関数を追加
```
func init --python
func new
func start
```

deploy
```
func azure functionapp publish my-example-func-py --publish-local-settings -y
```

## Flask Appを利用するために。

Flaskをインストール
```
cat requirements.txt
azure-functions
Flask
pip install -r requirements.txt
```

MyFlaskAppを作成、routeの設定(host.json, HttpTrigger/function.json)
```
tree -L 1
.
├── HttpTrigger         # routeの設定(function.json)
├── MyFlaskApp          # flaskアプリを作成
├── README.md
├── getting_started.md
├── host.json           # routeの設定(routePrefixを追加)
├── local.settings.json
└── requirements.txt
```

localで確認
```
func start
curl localhost:7071/hello
hello my flask app! None
```

azureで確認
```
curl https://my-example-func-py.azurewebsites.net/hello
hello my flask app! None
```

以上。