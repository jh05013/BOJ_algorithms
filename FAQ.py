head = "FAQ글이 문제 게시판에서 계속 밀려나는 이유로, FAQ 글을 모아 놓았습니다. 이 글을 찾기 쉽도록 문제 번호는 1000으로 두었습니다."
left = '<a href="http://www.acmicpc.net/board/view/'
mid = '">'
right = '</a><br>'

probs = [
    [1463, 19169, "1로 만들기"],
    [2839, 20711, "설탕 배달"],
    [6064, 21503, "카잉 달력"],
    [4344, 22366, "평균은 넘겠지"],
    [1874, 22447, "스택 수열"],
    [14499, 23937, "주사위 굴리기"],
    [10828, 23969, "스택"],
    [9012, 24691, "괄호"],
    [1010, 24868, "다리 놓기"],
    [7576, 25132, "토마토"],
    [11721, 25166, "열 개씩 끊어 출력하기"],
    [1920, 25204, "수 찾기"],
    [1003, 25213, "피보나치 함수"],
    [5430, 25456, "AC"],
    [1152, 25519, "단어의 개수"],
    [2178, 25832, "미로 찾기"],
    [1924, 25834, "2007년"],
    [1011, 26059, "Fly me to the Alpha Centauri"],
    [10989, 26132, "수 정렬하기 3"],
    [1316, 26273, "그룹 단어 체커"],
    [2448, 26520, "별 찍기 - 11"],
    [2675, 26587, "문자열 반복"],
    [2206, 27386, "벽 부수고 이동하기"],
    [1260, 27472, "DFS와 BFS"],
    [10845, 27578, "큐"],
    [2667, 27731, "단지번호붙이기"],
    [1912, 28134, "연속합"],
    [11728, 28332, "그대로 출력하기"],
    [11729, 28333, "그대로 출력하기 2"],
    [1707, 28396, "이분 그래프"],
    [11051, 28855, "이항 계수 2"],
    [15954, 29582, "인형들"],
    [1546, 29747, "평균"],
    [1110, 29928, "더하기 사이클"],
    [1157, 30509, "단어 공부"],
    [1005, 30959, "ACM 크래프트"],
    [2751, 31887, "수 정렬하기 2"],
    [11054, 32529, "가장 긴 바이토닉 부분 수열"],
    [1193, 32963, "분수 찾기"],
    [9935, 34565, "문자열 폭발"],
    [11004, 36672, "K번째 수"],
    [1002, 38854, "터렛"],
    [10519, 39199, "A+B - 4"],
    [1929, 39203, "소수 구하기"],
    [2108, 40713, "통계학"],
    [10872, 43390, "팩토리얼"],
    [2309, 43653, "일곱 난쟁이"],
    [6588, 44906, "골드바흐의 추측"],
    [18258, 45080, "큐 2"],
    [2798, 47357, "블랙잭"],
    [8958, 47874, "OX퀴즈"]]

probs.sort()
print(head)
for pn, bn, name in probs:
    print(left + str(bn) + mid + str(pn) + ' ' + name + right, end='')
