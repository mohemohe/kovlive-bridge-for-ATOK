# kovlive-bridge-for-ATOK

## これは何？

[ATOKダイレクト API][1] を利用して、入力した日本語をこふ語に変換します。  

## 動作環境（未検証）

- Windows もしくは Mac OS X
- ATOK 2008 以上
- Python 2.5.2 以上
- Python 3.0 以上

## 推奨環境

- Windows 10
- ATOK 2015
- Python 2.7.10
- Python 3.5

## 使い方

Python 2.x と Python 3.x の両方が必要です。  
`python` で Python 2.x 、 `python3` で Python 3.x が実行できる環境を構築してください。

Windows かつ ATOK 2015 を使用している方は `.\Windows\SETUP.EXE` を使用してインストールしてください。  
それ以外のバージョンや、 OS X を使用している方は、 [http://www.atok.com/useful/developer/api/][1] より、該当するバージョンに対応したモジュールをダウンロードし、 解凍後の atok_direct_setuptool 内のファイルを `./Windows/` に上書きしてからインストールしてください。

インストール後、すぐに使用可能な状態になっています。  
文字入力後、確定する前に ATOKダイレクトを起動（`Ctrl + Insert`） し、候補ありの表示が出てから ATOKダイレクト候補呼び出しキー（`Ctrl + 0`）で変換候補を表示します。

詳しくは [https://ghippos.net/blog/posts/2015-12-01-tue][2] に記載しています。

## ライセンス

bridge.py は WTFPL の範囲で好きにしやがれ。  
kovlive の権利は [@kenkov][3] が保有しています。  
その他の ATOKダイレクト API 関連のファイルの権利は （株）ジャストシステム が保有しています。

## 謝辞

[@kenkov][3] 氏に最大限の感謝を。



  [1]: http://www.atok.com/useful/developer/api/
  [2]: https://ghippos.net/blog/posts/2015-12-01-tue
  [3]: https://twitter.com/kenkov