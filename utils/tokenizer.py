import re

REGEX_EXPRESSION = r'([,.:;?_!"()\']|--|\s)'
REGEX_EXPRESSION_DECODE = r'\s+([,.?!"()\'])'


class SimpleTokenizerV1:
    def __init__(self, vocab):
        self.str_to_int = vocab
        self.int_to_str = {v: k for k, v in vocab.items()}

    def encode(self, text: str) -> list[int]:
        preprocssed = re.split(REGEX_EXPRESSION, text)
        preprocessed = [item.strip() for item in preprocssed if item.strip()]

        ids = [self.str_to_int[item] for item in preprocessed]
        return ids

    def decode(self, ids: list[int]) -> str:
        text = " ".join([self.int_to_str[id] for id in ids])
        text = re.sub(REGEX_EXPRESSION_DECODE, r"\1", text)
        return text


class SimpleTokenizerV2:
    def __init__(self, vocab):
        self.str_to_int = vocab
        self.int_to_str = {v: k for k, v in vocab.items()}

    def encode(self, text: str) -> list[int]:
        preprocssed = re.split(REGEX_EXPRESSION, text)
        preprocessed = [item.strip() for item in preprocssed if item.strip()]
        preprocessed = [
            item if item in self.str_to_int else "<unk>" for item in preprocessed
        ]

        ids = [self.str_to_int[item] for item in preprocessed]
        return ids

    def decode(self, ids: list[int]) -> str:
        text = " ".join([self.int_to_str[id] for id in ids])
        text = re.sub(REGEX_EXPRESSION_DECODE, r"\1", text)
        return text
