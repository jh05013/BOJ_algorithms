2차원 점 `Pnt<T>`를 정의합니다.

# 필드
- `T x` - x 좌표
- `T y` - y 좌표
- `int idx` - 점의 레이블. int가 아닌 다른 레이블을 원하실 경우, 레이블을 모아 놓은 vector를 만들어서 사용하십시오.

연산 내부적으로는 좌표 범위의 제곱에 이르는 수를 사용합니다. `T`가 `long long`일 경우, 좌표의 절댓값은 10^9 이하여야 합니다.

# 선언
- `Pnt<T>()` - (0, 0)을 선언합니다.
- `Pnt<T>(x, y)` - (x, y)를 선언합니다.
- `Pnt<T>(x, y, idx)` - 레이블이 `idx`인 점 (x, y)를 선언합니다.

# 연산
## 입출력
- `cin >>`으로 x, y좌표를 입력받을 수 있습니다.
- `cout <<`으로 `(x, y)`를 출력할 수 있습니다.

## 기본 연산
- 두 점의 덧셈과 뺄셈을 지원합니다.
- 점과 스칼라의 곱셈과 나눗셈을 지원합니다.
- 두 점의 비교를 지원합니다. 비교의 결과는 각 점의 x, y좌표 순서쌍을 비교한 결과와 같습니다.
- `T dot(Pnt<T> p, Pnt<T> q)`는 두 점의 위치 벡터의 내적입니다.

## 거리
- `T sq(Pnt<T> p)`는 원점과 p 사이 거리의 제곱입니다.
- `double abs(Pnt<T> p)`는 원점과 p 사이 거리입니다.
- `T distsq(Pnt<T> p, Pnt<T> q)`는 p와 q 사이 거리의 제곱입니다.
- `double dist(Pnt<T> p, Pnt<T> q)`는 p와 q 사이 거리입니다.

## 각도
- `int ccw(Pnt<T> p, Pnt<T> q, Pnt<T> r)`은 p, q, r이 반시계 방향으로 놓여 있으면 -1, 한 직선 위에 놓여 있으면 0, 시계 방향으로 놓여 있으면 1입니다.
- `T orient(Pnt<T> p, Pnt<T> q, Pnt<T> r)`은 절댓값이 삼각형 pqr의 넓이의 두 배이고, 부호가 `ccw(p, q, r)`과 동일한 수입니다.
- TODO angle, etc.

## 변형
- `Pnt<T> scale(Pnt<T> c, Pnt<T> p, T factor)`는 c를 기준으로 p의 위치를 factor배 한 점입니다.
- `Pnt<T> rot90(Pnt<T> p)`는 원점을 기준으로 p를 반시계 방향으로 90도 회전시킨 점입니다.
- `Pnt<T> rot90(Pnt<T> c, Pnt<T> p)`는 c를 기준으로 p를 반시계 방향으로 90도 회전시킨 점입니다.
- TODO theta rotation

# 테스트 문제
[[BOJ 11758 CCW]]
```cpp
int main(){
	Pnt<ll> a, b, c; cin>>a>>b>>c;
	cout << ccw(a,b,c);
}
```
