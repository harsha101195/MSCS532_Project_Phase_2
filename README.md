# Phase 2 Proof of Concept — Data Structures & Recommender System

The implementation demonstrates the foundational components of an e-commerce recommendation system using custom-built data structures.

---

## Project Structure

```
phase2_code/
│
├── datastructures.py     # Trie and UserGraph implementations
├── recommender.py        # Recommender engine (cosine similarity)
└── demo.py               # Script that demonstrates system functionality
```

No external packages are required — only Python’s standard library.

---

## How to Run the Demo

### **1. Navigate into the code directory and run the demonstration script**
```bash
python demo.py
```


### Expected Output

The script demonstrates:

- Trie prefix search results  
- User similarity scores  
- Recommended products for a target user  

Example:

```
Search results for prefix 'ip': [('iphone', ['SKU1']), ('iphone case', ['SKU2']), ('ipad', ['SKU3'])]
Similar users to alice: [('bob', 0.88)]
Recommendations for alice: [('ipad', 4.5)]
```

---

## Component Overview

### **Trie**
- Supports fast prefix search
- Stores product identifiers as payloads
- Suitable for autocomplete functionality

### **UserGraph**
- Stores user–product interactions
- Uses adjacency lists and weighted edges
- Supports vector extraction for similarity scoring

### **Recommender**
- User-based collaborative filtering
- Computes cosine similarity
- Recommends unseen products from similar users

---

