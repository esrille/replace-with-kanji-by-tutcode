# 置換変換 by TUT-code

このプロジェクトでは、日本語を梅棹式表記法で入力しやすくするためのTUT-code用のまぜがき辞書およびローマ字かな変換表を提供しています。IMEには、[uim-tutcode](https://github.com/uim/uim-doc-ja/wiki/UimTutcode)もしくは[tsf-tutcode](https://github.com/deton/tsf-tutcode)を利用します。どちらも、もともとは漢直入力用のIMEですが、置換変換ではこれを通常のローマ字入力を使用して利用します(そのほかのユーティリティーなどをくみあわせると、かな入力でも使用できます)。

## 背景

[梅棹忠夫](http://rondokreanto.com/tadao_umesao/)さん(1920-2010)は、耳できいただけで意味がわかるような、わかりやすい日本語の表記法を著作のなかでつかわれていました。その表記法は「梅棹式」とよばれることがあります。梅棹式表記の原則は、つぎの2つです。

* 和語はかなでかく。1音の動詞で意味が判別しにくいときは、漢字の使用も許容(例:切る、着る)。
* 漢語は漢字でかく。固有名詞のほかは、常用漢字を意識してむずかしい漢字はさける。

参考: 「漢字はやめたい」, 『[日本語の将来](https://www.amazon.co.jp/dp/4140910011)』,  梅棹忠夫, 2004.

日本語の表記は、明治時代以降、かなづかいを表音式にあらためたり、日常的に使用する漢字の数をへらしたり、複雑な漢字の字体を簡単なものにかえたり、といった努力がつづけられてきました。昭和23年(1948)におこなわれた調査では、社会生活に必要な読み書き能力(リテラシー)をもっている日本人は、まだ6.2%にすぎなかったそうです([「国語の現状の分析」](http://www.bunka.go.jp/kokugo_nihongo/sisaku/joho/joho/kakuki/01/tosin01/02.html))。

こうした日本語の表記の平明化の努力は、つねにそれに反対する立場のひとたちとのせめぎあいでもありました。そういった明治時代から戦後までの50年間の過程は、保科孝一さんの『[国語問題五十年](http://uwazura.cocolog-nifty.com/blog/2006/07/post_c707.html)』などからしることができます。

ワープロの登場以前に梅棹さんは『[知的生産の技術](https://www.amazon.co.jp/dp/4004150930/)』(1969)という本をかかれています。文章によるコミュニケーションの重要性をのべられたこの本が、その後のワープロ開発者にあたえた影響はとてもおおきなものがあったようです。富士通でOASYS(親指シフト)の開発をリードされた神田泰典さんは、その原点というような「人間にふさわしいかな入力方式の考察」([1](http://www.ykanda.jp/oasgif/nin-1.jpg), [2](http://www.ykanda.jp/oasgif/nin-2.jpg))の参考文献として、『知的生産の技術』をあげられています。また最初の日本語ワープロJW-10を開発された天野真家さんも[ブログ](http://www.ne.jp/asahi/kanmu/heishi/wp1.html)のなかで、梅棹さんがつくられた京大型カードや『知的生産の技術』のことにふれられています。

ただ残念なことに、ワープロはそれまでの日本語の表記の平明化の努力にさからうかのように、ふたたびよりおおくの漢字をつかう方向に日本語をうごかしていきます。しかし、実際にはよめないひとが多数の漢字が依然としてあり、『読めても読めなくても和語は「かな書き」を好む傾向がうかがえる』とNHK放送文化研究所の吉沢信さんはのべられています(「[かな書きか　漢字書きか](http://www.nhk.or.jp/bunken/summary/kotoba/kotobax3/pdf/062.pdf)」, 2010)。梅棹さんはこれを『[日本語と事務革命](https://www.amazon.co.jp/dp/4062923386/)』のなかで「ワープロ反動」とよばれて、ワープロの漢字変換をやめるように提案をされました。

## 置換変換

置換変換では、ひらがなはタイプしていけば本文中にそのまま直接入力されていきます。ひらがなで文を入力するために、[確定]キーや[無変換]キーをおす必要ありません。漢字にしたい部分があれば、その末尾にカーソルをうごかして(入力中であれば、もともとカーソルが末尾にありますけれども)、変換キーをおします。そうすると、カーソルの直前のひらがなが漢字に置換されます。変換キーをおすのは、文節変換のIMEのように文節のあとではなくて、漢字の熟語の直後になります。

※ [変換]キーは実際にはスペースバーなどにわりあててつかいます。

「しろうとむけワープロの登場を期待したいですね。」という梅棹さんの文(『日本語と事務革命』p.205)を入力したいときは、つぎのようにします。

    しろうとむけ[Caps/on]ワープロ[Caps/off]のとうじょう[変換]をきたい[変換]したいですね。

カタカナの部分はCaps Lockをつかいます。漢字は、意図的に漢字にしたい部分の最後で[変換]キーをおします。[変換]キーは、さきにひらがなで文を入力したあとで、カーソルを目的の位置に移動しておしてもかまいません。

同音異義語がなければ[変換]をおして候補がでた状態でそのまま次の文字を入力していけば大丈夫です。梅棹式は、同音異義語をさけるような言葉えらびもこみで梅棹式というべきでしょうから、じょうたつすれば変換候補をつぎつぎに表示していくような操作はへっていくはずです。

また漢字をまだならっていない小学生であれば、

    しろうとむけ[Caps/on]ワープロ[Caps/off]のとうじょうをきたいしたいですね。

のように、よりかんたんに入力できます。漢字変換のことや文節といった概念はしらなくても大丈夫です。

置換変換では、カーソルの直前にあるひらがなの文字列にたいして、なるべくながい漢字の熟語におきかえようとします。そのため「いきがい論」と入力したいときには、最初は「いき概論」のようになります。これを修正するには、>か右カーソルキーを順におしていくと対象がみじかくなっていって、「いきが異論」、「いきがい論」といった具合に、目的の漢字がでてくるようになります。ただ、実用では>や右カーソルキーをつかって熟語のながさをなおさないといけない場面はあまりないようです。きちんとした研究はしていませんけれども、日本語の助詞というのがそもそもそういう役割をもっているようにもおもいます。

※ 置換変換に相当する機能は、『[ Tコードの補助入力：字形組み合わせ法と交ぜ書き変換法]( http://id.nii.ac.jp/1001/00015068/)』(1990)以降、T-codeやTUT-codeといった漢直方式のユーザーのなかでは、機能の一部としてずっとつかわれていたようです。このプロジェクトは、この交ぜ書き変換法を通常のローマ字入力やかな入力をつかっているひとにも利用しやすい形にしたものです。

## 辞書について

置換変換では、漢字にしたい箇所で個別に[変換]キーをおさないかぎりは漢字はでてきません。そのため、文全体でかな漢字変換をかけて、IMEにまかせてよくしらない漢字までたくさんつかってしまう、という状況はさけやすくはなっています。それでも、辞書にむずかしい漢字の熟語がはいっていると、あやまって使用してしまう場面もかんがえられます。

このプロジェクトのrestrained.dicは、[tc2](https://github.com/kanchoku/tc)のmazegaki.dicをベースにして、

* 固有名詞のほかは常用漢字に漢字を制限。
* 用言は、1音の動詞に限定。
* 和語の熟語を削除(1字のものは、のこしています)。

といった平明化をくわえたもので、mazegaki.dicのかわりに使用できます。

辞書にカスタマイズをくわえたいときは、my.mdicを変更してから、restrain.shを実行すると、あたらしいrestrained.dicが生成されます。辞書の和をとったり、差をとったり、といった操作には[skkdic-expr2](https://github.com/skk-dev/skktools)をつかっています。

## つかい方

### uim-tutcodeの場合

[UimPref](https://github.com/uim/uim-doc-ja/wiki/UimPref)を起動して、

* コード表ファイルにromaji-rule.scmを、
* 交ぜ書き変換辞書にrestrained.dicを、

指定してください。[変換]キーは、[TUT-Code key bindings 3]の"postfix mazegaki conversion"に空白を入力すると、スペースバーにわりあてることができます。

CAPS LOCKでカタカナを入力するためには、[tutcode-rule]の"Use uppercase rule to input opposite kana"にチェックをいれておきます。

### tsf-tutcodeの場合

[設定ダイアログ](https://github.com/deton/tsf-tutcode#設定)をひらいて、


* ローマ字・仮名変換表にtsf-romaji.txtをよみこんで、
* SKK辞書にrestrained.dicを、

指定してください。[変換]キーは、tsf-romaji.txtのなかで、スペースバーにKanaK機能をわりあてています。

CAPS LOCKでカタカナを入力するためには、設定の[キー2]の[かな/カナ]に\x14といれておきます。

tsf-tutcodeでは、[ニュー・スティックニーかな配列](https://github.com/esrille/new-stickney)で置換変換をつかうこともできます。その場合は、[TSF-NewStickney.ahk](https://github.com/esrille/new-stickney/blob/master/ahk/TSF-NewStickney.ahk)をAutoHotkeyで実行してください。


## 参考

* [『日本語と事務革命』— 梅棹式表記法のための日本語入力システムをかんがえる](http://shiki.esrille.com/2017/04/blog-post.html)

### ライセンスについて

* restrained.dicの使用条件は[tc2](https://github.com/kanchoku/tc)にならいます。
* tsf-romaji.txtの使用条件は、[tsf-tutcode](https://github.com/deton/tsf-tutcode)にならいます。
* romaji-rule.scmの使用条件は、[uim](https://github.com/uim/uim)にならいます。

