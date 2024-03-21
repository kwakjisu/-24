min_distance(A)
    // 입력: 숫자 배열 A[0..n-1]
    // 출력: 두 항목간의 거리들 중의 최소 거리
    dmin <- inf
    for i <- 0 to n-1 do
        for j <- 0 to n-1 do
            if i!=j and |A[i]-A[j]|<dmin
                dmin <- |A[i]-A[j]|
    return dmin