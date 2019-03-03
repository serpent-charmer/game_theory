# game_theory
```
_list = [
    (1, 2, 4, 3),
    (0, 2, 3, 3),
    (1, 2, 4, 3),
    (4, 3, 1, 0),
    (4, 3, 4, 1),
    ]
    m_a = prune_lose_a(check_doubles(_list))
    
    print("MOST WINNING A", m_a)
    print("MOST WINNING B", prune_lose_b(m_a))
```

```
MOST WINNING A [(1, 2, 4, 3), (4, 3, 4, 1)]
MOST WINNING B [(3, 1), (1, 4), (2, 3)]
```
