# cleanse-speech 🚀

[![PyPI version](https://badge.fury.io/py/cleanse_speech.svg)](https://badge.fury.io/py/cleanse_speech)
[![Downloads](https://pepy.tech/badge/cleanse_speech)](https://pepy.tech/project/cleanse_speech)
[![Downloads](https://pepy.tech/badge/cleanse_speech/month)](https://pepy.tech/project/cleanse_speech)

Python🐍 3.9+ support. 



```shell
pip install cleanse-speech
```

## Usage

```python
import io

from cleanse_speech import DLFA
from cleanse_speech import SpamShelf

if __name__ == '__main__':
    dfa = DLFA(words_resource=[
        ['你好'],
        io.BytesIO(b'sensitive'),
        SpamShelf.CN.ADVERTISEMENT,
    ])
    print(dfa.contains_illegal('This is a 你好 word.'))
    print(dfa.censor_all('This is a 你好 word.'))
    print(dfa.extract_illegal_words('This is a 你好 word.'))
    dfa.update_words(['sensitive', 'word', 'new'])
    print(dfa.extract_illegal_words('This is a new sensitive word.'))
```