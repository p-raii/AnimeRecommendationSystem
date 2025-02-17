from .models import AnimeData  # Import your model

class TrieNode:
    def __init__(self):
        self.children = {}
        self.is_end_of_word = False
        self.anime_titles = []

class Trie:
    def __init__(self):
        self.root = TrieNode()

    def insert(self, title):
        node = self.root
        for char in title.lower():
            if char not in node.children:
                node.children[char] = TrieNode()
            node = node.children[char]
        node.is_end_of_word = True
        node.anime_titles.append(title)

    def search_prefix(self, prefix):
        node = self.root
        for char in prefix.lower():
            if char not in node.children:
                return []  # No matches found
            node = node.children[char]

        return self._get_all_titles(node)

    def _get_all_titles(self, node):
        results = []
        if node.is_end_of_word:
            results.extend(node.anime_titles)
        for child in node.children.values():
            results.extend(self._get_all_titles(child))
        return results

trie = Trie()  # Create an instance of Trie

def load_anime_titles():
    anime_list = AnimeData.objects.values_list('title_english', 'title_romanji')  
    for title_english, title_romanji in anime_list:
        if title_english:
            trie.insert(title_english)
        if title_romanji:
            trie.insert(title_romanji)

# Load Trie when Django starts
load_anime_titles()