import numpy as np
import re
from collections import Counter

def calculate_entropy(texto):

    if not texto: return 0.0
    
    words = re.findall(r'\w+', texto.lower())
    total_words = len(words)
    
    if total_words == 0: return 0.0
    
    counts = Counter(words)
    probs = np.array([count / total_words for count in counts.values()])
    
    entropy = -np.sum(probs * np.log2(probs))
    
    return entropy