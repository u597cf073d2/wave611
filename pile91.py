# small utilities, no deps

def group_by(items, key):
    out = {}
    for it in items:
        out.setdefault(key(it), []).append(it)
    return out

def most_common(xs):
    return max(set(xs), key=xs.count) if xs else None
