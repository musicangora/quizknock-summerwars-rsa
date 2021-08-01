# quizknock-summerwars-rsa
 QuizKnockの企画動画で学ぶRSA暗号
 
 [![](https://img.youtube.com/vi/kvC55N4k9ng/0.jpg)](https://www.youtube.com/watch?v=kvC55N4k9ng)

夏になると見たくなる、映画「サマーウォーズ」では、主人公の健二が世界の危機を救うために暗算で暗号を解くシーンがあります。実際何をしているのかよくわからないまま楽しんでいる人も多いと思いますが、彼はとんでもないことをしています。

健二が説いた暗号は、RSA暗号だと言われています。RSA暗号は、現在様々なとことで使われている暗号方式で、公開鍵と秘密鍵の2つの鍵を使って暗号化する「公開鍵暗号方式」の一つです。QuizKnockの皆さんがこのRSA暗号を暗算で解くことで、暗号方式と健二のすごさを非常にわかりやすく説明してくれています。今回はこれを題材にPythonで実装することで、RSA暗号の仕組みと、健二のすごさと、計算機のありがたみを感じようというものです。

## 第1問
![image](https://user-images.githubusercontent.com/40447362/127762136-bd7cbb75-9dfa-4582-8075-5e6d74bc67bb.png)

第1問は、(単純に文字コード変換とも考えられるが)古典暗号のように対応表に基づいて文字列を数字に変換するものである。対応はAなら01、Bなら02 … Zなら26というように、アルファベットの大文字が二桁の数字に置き換えている。

二桁の数字を大文字のアルファベットに変換するプログラムはこんな感じである。

``` decoder.py
# 入力された数字の形式の暗号を文字列に解読する
def decoder(input_number):
    return chr(int(input_number) + 64)
```

入力の`input_number`は01~26の二桁の数字で、まずそれを`int()`で整数に変換する。次に、ASCIIコードを使って数字を文字に変換する。ASCIIコードでは65がA、65がBというように対応しているので、今回であれば入力された数字に64を足せば良い。最後にこれを`chr()`で文字に変換するとうまくいく。

ただし、今回入力が二桁区切りではなくすべてくっついた状態で与えられるので、二桁ごとに分割する必要がある。

入力された二桁以上の数字を二桁ごとに分割してリストに格納する関数はこんな感じである。

```formatter.py
# 入力された数字の形式の暗号を二桁ごとに区切ってリストに格納する
def formatter(input_number):
    input_list =[]
    while input_number > 0:
        input_list.append(str(input_number%100).zfill(2))
        input_number //= 100
    input_list.reverse()
    return input_list
```

二桁ごとに分割したいので、100で割った商とあまりを考える。また、一桁の数字も一旦二桁ごとに分割したかったので、整数型ではなく文字列に変換し、`zfill(2)`メソッドで0埋めしている。

## 第2問
![image](https://user-images.githubusercontent.com/40447362/127762195-1b995f09-1468-4ff5-9d82-2a8a8ab135db.png)

## 第3問
![image](https://user-images.githubusercontent.com/40447362/127762221-b350cfb7-7c73-4b3e-a377-5b651a670adf.png)

## 第4問、最終問題
動画内では第4問と最終問題で、「サマーウォーズ」の主人公、健二がいかにすごいことをしているかが説明されていますので、ぜひご覧ください。
