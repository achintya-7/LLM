import re
from utils.tokenizer import SimpleTokenizerV2, REGEX_EXPRESSION


def load_data() -> str:
    with open("assets/the-verdict.txt", "r") as f:
        raw_text = f.read()

    print("Total characters:", len(raw_text))

    return raw_text


def tokenize_data(raw_text: str) -> list[str]:
    tokens = re.split(REGEX_EXPRESSION, raw_text)
    processed_tokens = [token.strip() for token in tokens if token.strip()]
    return processed_tokens


def build_vocabulary(tokens: list[str]) -> dict[str, int]:
    all_words = sorted(set(tokens))
    vocab = {"<unk>": 0}
    vocab.update({token: i for i, token in enumerate(all_words, start=1)})
    return vocab


def main():
    raw_text = load_data()

    tokens = tokenize_data(raw_text)
    print("Total tokens:", len(tokens))

    vocab = build_vocabulary(tokens)

    text1 = "Hello, do you like tea?"
    text2 = "In the sunlit terraces of the palace."
    text = " <|endoftext|> ".join((text1, text2))

    tokenizer = SimpleTokenizerV2(vocab)
    ids = tokenizer.encode(text)
    print(ids)


if __name__ == "__main__":
    main()
