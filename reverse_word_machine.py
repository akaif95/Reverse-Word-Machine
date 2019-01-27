#This program is designed to simply reverse the order of any word
#AKA it will show the word backwards like how it would appear in a mirror reflection

word = input("""
             Please enter the word or sentence you would like to reverse. Note that
             any numbers or symbols are convereted into strings:
             
             """).strip()

reversed_word = word[::-1]

print(reversed_word)
