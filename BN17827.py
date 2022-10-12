#백준 17827번 달팽이 리스트 //11일 강의에 리스트 나와서 리스트 풀어봄

N,M,V = map(int,input().split()) #N,M,V 변수 받음
C_arr = list(map(int,input().split())) #N개의 정수 리스트로 받음
A_arr = list() #answer_array

for i in range(M): #질문 M번 -> M번 반복

    K = input() #질문에 해당하는 K
    K = int(K) #정수형 선언

    if K < N : # N보다 작을때는 바로 대입
        A_arr.append(C_arr[K])
    else: # N보다 클때
        K2 = (K - N)%(N - V + 1) # 반복되는 부분에서 해당값
        K2 += (V - 1)
        A_arr.append(C_arr[K2])
      

for i in range(M): #해당값 출력
    print(A_arr[i])