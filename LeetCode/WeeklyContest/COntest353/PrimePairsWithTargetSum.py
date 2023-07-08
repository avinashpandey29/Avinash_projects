class Solution:
    def findPrimePairs(self, n: int) -> List[List[int]]:

        if n == 1:
            return []

        def isPrime(k, check_already_exists, primenumberpair, n):

            res = []

            if (k == 1 or k == 0):
                return False

            for i in range(2, (k // 2) + 1):

                if (k % i == 0):
                    print("False")
                    return False

            print(k)

            if k + k == n:
                res.append(k)
                res.append(k)
                primenumberpair.append(res)

            if n - k not in check_already_exists:
                check_already_exists[k] = 1
            else:
                minimum = min(k, n - k)
                maximum = max(k, n - k)
                res.append(minimum)
                res.append(maximum)
                primenumberpair.append(res)
                # primenumberpair.sort()

            # print(primenumberpair)

            return primenumberpair

        check_already_exists = dict()
        primenumberpair = []

        for i in range(2, n + 1):
            isPrime(i, check_already_exists, primenumberpair, n)

        # print(primenumberpair)
        return primenumberpair










