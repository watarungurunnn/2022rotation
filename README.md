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
1. 実行方法

    terminalで2022rotationがあるディレクトリに行き、
    ```
    $ python main.py インプットファイルへのパス (--name アウトプットファイルの名前)(-o アウトプットファイルを格納するディレクトリのパス) (--model モデル名)
    ```
    と実行。(カッコの中は任意)
    example:
    ```
    $ python main.py input.xls --name result.xls --model 'Sakaguchi'
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
    ※ 二回目以降は
    ```
    $ git checkout ブランチ名
    ```
1. .pyファイル及びREADMEを編集
1. 新しくインストールしたパッケージがあればrequirements.txtに追記
1. flake8とmypyのチェックを行う

   ```bash
   $ flake8 src/
   $ flake8 main.py
   $ mypy src/
   $ mypy main.py
   ```
   ここで表示されるメッセージを元に体裁を整えてください。

1. isortでライブラリのimport順を整える

   ```bash
   $ isort src/
   $ isort main.py
   ```
1. (自身が作成した箇所はREADME.mdを更新する)
1. リモートリポジトリに反映
    ```
    $ git pull origin main
    ```
    競合が生じていたら[こちら](https://backlog.com/ja/git-tutorial/pull-request/10/)を参照

    以下で自分の名前のブランチにいることを確認してください。
    ```
    $ git branch
    ```

    ```
    $ git add 変更したファイル
    $ git commit -m "メッセージ"
    $ git push origin 自分のブランチ名
    ```


1. 最後にブラウザでgithubのレポジトリのページからPRを出し、確認してmerge


## パッケージ
### input

### optimize

### output
