class TrieNode:
    def __init__(self):
        self.children = {}
        self.is_end = False
        self.payloads = []

class Trie:
    def __init__(self):
        self.root = TrieNode()

    def insert(self, word, payload=None):
        node = self.root
        for ch in word.lower():
            if ch not in node.children:
                node.children[ch] = TrieNode()
            node = node.children[ch]
        node.is_end = True
        if payload:
            node.payloads.append(payload)

    def search_prefix(self, prefix):
        node = self.root
        for ch in prefix.lower():
            if ch not in node.children:
                return []
            node = node.children[ch]
        results = []
        self._collect(node, prefix.lower(), results)
        return results

    def _collect(self, node, prefix, out):
        if node.is_end:
            out.append((prefix, list(node.payloads)))
        for ch, nxt in node.children.items():
            self._collect(nxt, prefix + ch, out)


from collections import defaultdict, Counter
import math

class UserGraph:
    def __init__(self):
        self.graph = defaultdict(list)
        self.user_hist = defaultdict(Counter)

    def add_interaction(self, user, product, weight=1.0):
        self.graph[user].append((product, weight))
        self.user_hist[user][product] += weight

    def get_user_vector(self, user):
        return self.user_hist.get(user, Counter())

def cosine_similarity(a, b):
    if not a or not b:
        return 0.0
    dot = sum(a[k] * b.get(k, 0.0) for k in a)
    na = math.sqrt(sum(v*v for v in a.values()))
    nb = math.sqrt(sum(v*v for v in b.values()))
    if na == 0 or nb == 0:
        return 0.0
    return dot / (na * nb)
