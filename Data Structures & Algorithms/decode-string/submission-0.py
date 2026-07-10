class Solution:
    def decodeString(self, s: str) -> str:
        string_stack = []
        count_stack = []
        curr_string = ''
        curr_count = 0
        for char in s:
            if char.isdigit():
                curr_count = curr_count*10 + int(char)
            elif char == '[':
                string_stack.append(curr_string)
                count_stack.append(curr_count)
                curr_string = ''
                curr_count = 0
            elif char == ']':
                count = count_stack.pop()
                prev_str = string_stack.pop()
                curr_string = prev_str + count*curr_string
            else:
                curr_string = curr_string + char
        return curr_string
                
