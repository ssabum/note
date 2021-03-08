# 유클리드 호제법, a를 b로 나눈 나머지를 r이라 하면
# a와 b의 최대공약수는 b와 r의 최대공앿수와 같다.
def gcd(a, b):
    if a % b == 0:
        return b
    else:
        return gcd(b, a % b)