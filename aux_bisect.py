import bisect

# Forma muy eficiente de buscar un elemento en una lista ordenada
def find_index(vocab, w):
    i = bisect.bisect_left(vocab, w)
    if i != len(vocab) and vocab[i] == w:
        return i
    return False


def insert_in_position(vocab, w, position):
    if position == len(vocab) or vocab[position] != w:
        vocab.insert(position, w)


# Agrega un elemento en una lista ordenada
def insert_ordered(vocab, w):
    position = bisect.bisect_left(vocab, w)
    insert_in_position(vocab, w, position)

    return position
