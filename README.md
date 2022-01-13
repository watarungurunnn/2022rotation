# 2022rotation

## 開発時の環境
### python環境
1. pythonのバージョンは3.8系推奨
1. 仮想環境の構築
    ```
    $ python3 -m venv .venv
    ```
1. 仮想環境のアクティベート(terminalを開くごとに行う)
    ```
    $ source .venv/bin/activate
    ```
1. requirements.txtから依存ライブラリのインストール
    ```
    $ pip install -r requirements.txt
    ```

### 開発手順
1. githubからクローンしてくる
    ```
    $ git clone https://github.com/watarungurunnn/2022rotation.git [ローカルフォルダ名]
    ```
1. [名前]/[タスク]でブランチを作成
    ```
    $ git checkout -b ブランチ名
    ```
1. flake8とmypyのチェックを行う

   ```bash
   $ flake8 src/
   $ mypy src/
   ```

1. isortでライブラリのimport順を整える

   ```bash
   $ isort src/
   $ isort tests/
   ```
1. (自身が作成した箇所はREADME.mdを更新する)
9. 最後にPRを出し、確認してmerge


## パッケージ
