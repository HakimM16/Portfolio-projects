def find_longest_palindromic_substring(param):
    longest = "a"

    def helper(param):
        reverse = param[::-1]
        if reverse == param:
            return True
        return False
    
    for i in range(0, len(param)):
        for j in range(i + 1, len(param) + 1):
            substring = param[i:j]
            print(substring, j)
            if helper(substring):
                if len(substring) > len(longest):
                    longest = substring
                    print(longest)
    
    if longest == "a":
        print(f"There is no palidrome in {param}")
    else:
        print(f"The longest palidrome is {longest}")

#find_longest_palindromic_substring("saippuakivikauppias")
find_longest_palindromic_substring("abccccdd")