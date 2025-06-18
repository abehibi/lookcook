# lookcook
方法1：GitHubの画面で直接ファイルを編集する
「Add file」→「Edit file」などで、Webページのコードを書き換える
「Commit changes（保存）」をすれば、変更が共有される

方法2：パソコンにコピーして作業する（ちょっと上級）
Pull（プル）：他の人の変更をパソコンに取り込む

Branch（ブランチ）：いろんなバージョンを同時に作れる

Merge（マージ）：別々に作った内容を一緒にする

ここから重要！！！

□操作１：リポジトリを「クローン」する
クローンっていうのは「GitHubにあるプロジェクトを、パソコンにコピーする」ことだよ。

GitHub Desktopで「File」→「Clone repository…」を選ぶ

「GitHub.com」タブで、自分のリポジトリを選ぶ（例：my-webapp）

パソコンの保存場所を選んで「Clone」を押す

✅ これでパソコンの中に、プロジェクトのフォルダがコピーされました！

🪜 操作２：Visual Studio Code で開こう（おすすめ）
Visual Studio Code（VSCode）がインストールされてなければこちらから：
https://code.visualstudio.com/

VSCodeを開いて、「ファイル」→「フォルダーを開く」

さっきクローンしたフォルダ（例：my-webapp）を選ぶ

✏️ これでファイル（HTML、CSS、JSなど）を自由に編集できるようになるよ！

🪜 操作３：編集したら「GitHubにアップロード」する
GitHub Desktopに戻る

画面に「変更したファイル」が表示される

下の方に「Summary（メモ）」に何を変えたか書く（例：ボタン追加）

「Commit to main」を押す（＝保存）

右上の「Push origin」を押す（＝GitHubにアップロード！）
