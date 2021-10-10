def solution(numbers):
    a = []

    #모든 수 더함
    for i in range(len(numbers)-1):
        for j in range(1,len(numbers)):
            if(i != j):
                print("index :",i,"+",j,"=",numbers[i] + numbers[j])
                a.append(numbers[i] + numbers[j])
    
    print(a)
    #중복된 수 삭제
    print(list(set(a)))
    a = list(set(a))
    return a    