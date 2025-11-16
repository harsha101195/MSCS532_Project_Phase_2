from datastructures import UserGraph, cosine_similarity

class Recommender:
    def __init__(self, graph):
        self.graph = graph

    def similar_users(self, user):
        target = self.graph.get_user_vector(user)
        sims = []
        for other in self.graph.user_hist:
            if other == user:
                continue
            sim = cosine_similarity(target, self.graph.get_user_vector(other))
            sims.append((other, sim))
        sims.sort(key=lambda x: x[1], reverse=True)
        return sims[:5]

    def recommend(self, user):
        vec = self.graph.get_user_vector(user)
        items = set(vec.keys())
        sims = self.similar_users(user)
        scores = {}
        for other, sim in sims:
            for product, w in self.graph.graph[other]:
                if product not in items:
                    scores[product] = scores.get(product, 0) + sim * w
        ranked = sorted(scores.items(), key=lambda x: x[1], reverse=True)
        return ranked[:5]
