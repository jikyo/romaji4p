romaji
-----
`romaji` is a converter library to romanize Japanese hiragana/katakana string by standard and IME typing style.
Even though `pykakasi <https://pypi.org/project/pykakasi/>`_ already has provided the same functions, and returns only one romanized string.
However, there exists several different romanization systems, so one hiragana/katakana string has so many romanize string.
For example, `"ちゃ"` can be romanized as `"cha"`, `"tya"`, `"chixya"`, `"tixya"`, `"chilya"`, or `"tilya"`.
`romaji` provides romanized strings as many as possible.

If an input string contained non hiragana/katakana characters (includes kanji), `romaji` return the characters as same as the input.
For example, `romaji` converts the input `"お茶の水"` to `"o茶no水"`.
If there is a need to romanize the whole string which includes kanji, `romaji` can romaize the readings in the tokens which `Janome <https://pypi.org/project/Janome/>`_  tokenizer provides.
`romaji` strongly recommends to use with `Janome`.

The mapping from hiragana/katakana to romaji is based on common IME's system to input Japanese.
Therefor, `romaji` does not directly implement the standard system like Hepburn, Nihon-shiki or Kunrei-shiki, but includes them.


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
