def remove_non_ascii(text):
  return ''.join([i if ord(i) < 128 else ' ' for i in text])
