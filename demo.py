from datastructures import Trie, UserGraph
from recommender import Recommender

t = Trie()
t.insert("iphone", "SKU1")
t.insert("iphone case", "SKU2")
t.insert("ipad", "SKU3")

print("Search results for prefix 'ip':", t.search_prefix("ip"))

g = UserGraph()
g.add_interaction("alice", "iphone", 3)
g.add_interaction("alice", "case", 1)
g.add_interaction("bob", "iphone", 2)
g.add_interaction("bob", "ipad", 5)

rec = Recommender(g)
print("Similar users to alice:", rec.similar_users("alice"))
print("Recommendations for alice:", rec.recommend("alice"))
print("Similar users to bob:", rec.similar_users("bob"))
print("Recommendations for bob:", rec.recommend("bob"))

