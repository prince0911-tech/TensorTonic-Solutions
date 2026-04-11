def remove_stopwords(tokens, stopwords):
    """
    Returns: list[str] - tokens with stopwords removed (preserve order)
    """
    # Your code here
    # tokens_copy=tokens.copy()
    # for i in tokens:
    #     if i in stopwords:
    #         tokens_copy.remove(i)
    # return tokens_copy

    return [word for word in tokens if word not in stopwords]
    pass