onetonine = 36
ten = 3
eleven = 6
twelve = 6
thirteen =8
fourteen = 8
fifteen = 7
eighteen = 8
nineteen = 8
teens = 3 + 6 + 6 + 8 + 8 + 7 + 8 + 8 
singles = 36
tens = 54
num_lengths = {20: 6, 30: 6, 4: 5, 50: 5, 60: 5, 70: 7, 80: 6, 90: 6}
hundreds = singles + tens + sum(x*10+singles for x in num_lengths)
hundreds = 4418
hundred_lengths = {100: 'onehundred', 200: 'twohundred', 300: 'threehundred', 400: 'fourhundred', 500: 'fivehundred', 600: 'sixhundred', 700: 'sevenhundred', 800: 'eighthundred', 900: 'ninehundred'}
sum = 4418
for x in hundred_lengths:
    n = len(hundred_lengths[x])
    sum += n 
    sum += 99*(n+3)+hundreds
sum += len('onethousand')
print(sum)
