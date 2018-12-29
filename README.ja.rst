romaji
-----

`romaji` は、日本語のひらがな/カタカナ表記を、標準的なローマ字とIMEでのローマ字タイピングに準ずるローマ字へ変換するライブラリです。
`pykakasi <https://pypi.org/project/pykakasi/>`_ は既に同じ機能を提供しており、一つのローマ字表記を返却します。
しかし、ローマ字への変換方法は幾つか存在する為、ひらがな/カタカナ表記の文字列は多くのローマ字表記をもつことになります。
例として、 `"ちゃ"` はローマ字表記 `"cha"`、`"tya"`、`"chixya"`、`"tixya"`、`"chilya"`、`"tilya"` をもつことができます。
`romaji` は可能な限り多くのローマ字表記を返却します。

入力文字列にひらがな/カタカナ以外の文字 (特に漢字など)が含まれている場合、 `romaji` はそれらの文字列をそのまま返却します。
例えば、 `romaji` は入力 `"お茶の水""` を `"o茶no水"` に変換します。
漢字を含むような文字列全体を変換したい場合、 `romaji` は `Janome <https://pypi.org/project/Janome/>`_  の tokenizer が提供する token 内の reading をローマ字へ変換することができます。
`romaji` は `Janome` と一緒に利用することを強くお奨めします。

ひらがな/カタカナからローマ字へのマッピングは一般的な IME の入力方式に基づいています。
その為、 `romaji` は、ヘボン式、日本式、訓令式等の標準的な変換方式を直接実装はしていませんが、それらを含む変換を行います。


Installation
-----

(in preparation)

.. code-block:: BashLexer

    $ git clone https://github.com/jikyo/romaji4p.git
    $ cd romaji4p
    $ pip install .


Usage
-----

.. code-block:: python

    >>> import romaji
    >>> romaji.transliterate('僕ドラえもん')
    ['僕doraemon', '僕doraemon\'', '僕doraemonn']
    >>> romaji.transliterate('諸行無常')
    []
