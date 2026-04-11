def word_count_dict(sentences):
    """
    Returns: dict[str, int] - global word frequency across all sentences
    """
    # Your code here
    word_count={}
    for sentence in sentences:
        if isinstance(sentence, list):
            words = sentence
        else:
            words = sentence.split()
        for word in words:
            if word in word_count:
                word_count[word]+=1
            else:
                word_count[word]=1
                

    return word_count
    
    pass