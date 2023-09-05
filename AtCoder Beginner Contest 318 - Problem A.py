N, M, P = map(int, input().split())

if M > N:
    result = 0
else:
    result = (N - M) // P + 1

print(result)
