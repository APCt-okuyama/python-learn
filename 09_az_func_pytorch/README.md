# PyTorch を使用して事前トレーニング済みの画像分類モデルを Azure Functions にデプロイする

試してみる

[チュートリアル PyTorch](https://learn.microsoft.com/ja-jp/azure/azure-functions/machine-learning-pytorch?tabs=bash)

## 構築手順

基本的にはTensorFlow(08_az_func_tensorflow)と同様の内容になる。
ヘルパー関数の実装がPyTorchを利用したものになる。
 
```
python -m venv .venv
source .venv/bin/activate
#deactivate
func init --worker-runtime python
func new --name classify --template "HTTP trigger"
```

```
pip install --no-cache-dir -r requirements.txt
```
## 構成
```
tree 
.
├── README.md
├── classify
│   ├── __init__.py
│   ├── function.json
│   ├── labels.txt
│   └── predict.py ※ pytorch を利用下処理
├── getting_started.md
├── host.json
├── local.settings.json
└── requirements.txt
```

確認
```
curl http://localhost:7071/api/classify?img=https://raw.githubusercontent.com/Azure-Samples/functions-python-pytorch-tutorial/master/resources/assets/Bernese-Mountain-Dog-Temperament-long.jpg
```