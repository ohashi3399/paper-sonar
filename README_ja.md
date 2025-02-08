# ᯤpaper-sonar
- 入力キーワードと類似した論文を提示するコード

## デモ

- [こちら](https://huggingface.co/spaces/ryota39/iclr2025-sonar)で公開

## 対象
- ICLR2025のaccepted papers


> [!NOTE]
> 論文のタイトルとアブストラクトとURLが取得できる会議であれば、対象ファイルを入れ替えれば流用できます

## 作成手順
1. タイトルとアブストの先頭600文字とURLを平文で連結
2. [埋め込みモデル](https://huggingface.co/intfloat/multilingual-e5-large-instruct)でvectorstoreに変換
3. [近似最近傍探索](https://github.com/facebookresearch/faiss)で類似したn件の論文情報を出力

> [!NOTE]
> 埋込モデルは[こちらのリーダーボード](https://huggingface.co/spaces/mteb/leaderboard)を基に選択しました

## 実装手順
- [こちらのリンク](https://iclr.cc/Downloads/2025)からaccepted papersをダウンロード
  - `data`に配置

- txtファイルに変換

```python
python src/build_db/json2txt.py
```

- vectorstoreに変換

```python
python src/build_db
```

## アプリ化
- Huggingfaceアカウントで新規のspacesを作成
- 以下のファイルを作成したspacesに移動
  - app.py
  - `data/db`フォルダと、フォルダ内に作成したvectorstoreファイル
  - requirements.txt

# 例

- `query`: `β  -calibration of Language Model Confidence Scores for Generative QA`
- `suggestion`
![suggestion](./data/img/suggestion.png)
