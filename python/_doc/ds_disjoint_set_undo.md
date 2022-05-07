https://github.com/jh05013/BOJ_algorithms/blob/master/python/ds/disjoint_set_undo.py

되돌리기를 지원하는 분리 집합입니다.

# 필드
- `sz` - **i가 자신이 포함된 집합의 대푯값일 경우**, `sz[i]`는 그 집합의 크기입니다.

# 선언
- `DisjointSetUndo(n)`는 크기가 n+1인 분리 집합을 선언합니다. (n+1인 이유는 1-indexing을 허용하기 위함입니다.)

# 연산
아래에서 서술하는 모든 연산의 시간 복잡도는 O(logn)입니다.
- `union(x, y)`는 `x`가 포함된 집합과 `y`가 포함된 집합을 하나로 합칩니다.
- `undo()`는 가장 최근에 실행한 `union`을 취소합니다. 이때, `x`와 `y`가 이미 같은 집합에 있어서 합쳐지지 않았더라도 `union` 자체는 실행된 것으로 간주합니다.
- `find(x)`는 `x`가 포함된 집합의 대푯값을 반환합니다.
