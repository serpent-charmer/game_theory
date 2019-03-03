def rotate(_matrix):
    return list(zip(*_matrix.copy()))

def alpha(_matrix):
    row_maxes = []
    for i in range(len(_matrix)):
        row_maxes.append(min(_matrix[i]))
    return max(row_maxes)

def beta(_matrix):
    column_maxes = []
    _r_c_matrix = rotate(_matrix)
    for i in range(len(_r_c_matrix)):
        column_maxes.append(max(_r_c_matrix[i]))
    return min(column_maxes)

def saddle_point(_matrix, _length):
    a = alpha(_matrix, _length)
    b = beta(_matrix, _length)
    return (a, b, a == b)

def check_doubles(_matrix):
    _remove = []
    
    _matrix.reverse()
    for i in reversed(range(len(_matrix))):
        if _matrix[i] in _remove:
            _matrix.remove(_matrix[i])
            continue
        _remove.append(_matrix[i])
    _matrix.reverse()
    
    return _matrix
        
    

def prune_lose_a(_o_matrix):

    _matrix = _o_matrix.copy()

    _remove = []

    for i in range(len(_matrix)):
        _e = _matrix[i]
        for j in range(len(_matrix)):
            if i == j:
                continue
            _e_n = _matrix[j]
            less = False
            for k in range(len(_e)):
                if _e[k] > _e_n[k]:
                    less = True
                    break
            if not less:
                _remove.append(_e)
    
    for r in set(_remove):
        _matrix.remove(r)
    return _matrix


def prune_lose_b(_o_matrix):

    _matrix = rotate(_o_matrix.copy())

    _remove = []

    for i in range(len(_matrix)):
        _e = _matrix[i]
        for j in range(len(_matrix)):
            if i == j:
                continue
            _e_n = _matrix[j]
            less = False
            for k in range(len(_e)):
                if _e[k] < _e_n[k]:
                    less = True
                    break
            if not less:
                _remove.append(_e)
                
    for r in set(_remove):
        _matrix.remove(r)
    return _matrix

if __name__ == "__main__":
    
    _list = [
    (1, 2, 4, 3),
    (0, 2, 3, 3),
    (1, 2, 4, 3),
    (4, 3, 1, 0),
    (4, 3, 4, 1)
    ]
    
    m_a = prune_lose_a(check_doubles(_list))
    
    print("MOST WINNING A", m_a)
    print("MOST WINNING B", prune_lose_b(m_a))
