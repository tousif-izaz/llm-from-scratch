import re


class SimpleTokenizerV2:
    def __init__(self, vocab):
        self.str_to_int = vocab  #A
        self.int_to_str = {i: s for s, i in vocab.items()}
        
    def encode(self, text):
        preprocessed = re.split(r'([,.?_!"()\']|--|\s)', text)
        preprocessed = [item.strip() for item in preprocessed if item.strip()]
        preprocessed = [item if item in self.str_to_int else "<|unk|>" for item in preprocessed]
        ids = [self.str_to_int[s] for s in preprocessed]
        return ids
    
    def decode(self, ids):
        text = " ".join([self.int_to_str[id] for id in ids])
        text = re.sub(r'\s+([,.?!"()\'])', r'\1', text)
        return text


with open("the-verdict.txt", 'r', encoding='utf-8') as f:
    raw_text = f.read()

preprocessed = re.split(r'([,.?"()\']|--|\s)', raw_text)
preprocessed = [item.strip() for item in preprocessed if item.strip()]
all_words = sorted(list(set(preprocessed)))
all_words.extend(["<|endoftext|>", "<|unk|>"])
vocab = {token: integer for integer,token in enumerate(all_words)}
tokenizer = SimpleTokenizerV2(vocab)
text = """"It's the last he painted, you know," Mrs. Gisburn said with pardon"""
ids = tokenizer.encode(text)
print(ids)
print(tokenizer.decode(ids))