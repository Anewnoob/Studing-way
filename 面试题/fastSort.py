问题描述：
计算a ** n % b 其中a、b和n都是32位的非负整数
即求a的n次方对b的余数  (快速幂)
问题示例：
例如：2**31%3=2

class Solution:
    def fastPower(self, a, b, n):
        ans = 1
        while n > 0:
            if n % 2 == 1:
                ans = ans * a % b 
            a = a * a % b
            n = n / 2
        return ans % b
        
 if __name__ == '__main__':
    solution = Solution()
    print(solution.fastPower(2, 31, 3))
