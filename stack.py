def check_parentheses(code):
  stack = []
  for char in code:
      if char == '(':
          stack.append(char)
      elif char == ')':
          if not stack:
              return "Invalid"
          stack.pop()
  return "Valid" if not stack else "Invalid"

# Test
print(check_parentheses("()"))         # Valid
print(check_parentheses("(())"))       # Valid  
print(check_parentheses("(()"))        # Invalid
print(check_parentheses("abc)def"))    # Invalid