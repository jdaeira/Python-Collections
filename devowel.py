state_names = ["Alabama", "California", "Oklahoma", "Florida"]
vowels = list('aeiou')
output = []

print(state_names)

for state in state_names:
  state_list = list(state.lower())
  print(state_list)

  for vowel in vowels:
  	while True:
  		try:
  			state_list.remove(vowel)
  		except:
  			break
  output.append(''.join(state_list).capitalize())

print(output)
  		