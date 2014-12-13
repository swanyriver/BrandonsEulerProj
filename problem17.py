hund = "hundredand"
tens = ["twenty","thirty","forty","fifty","sixty","seventy","eighty","ninety"]
single = ["one","two","three","four","five","six","seven","eight","nine"]
teens = ["ten","eleven","twelve","thirteen","fourteen","fifteen","sixteen","seventeen","eighteen","nineteen"]
thousand = "onethousand"

tentotal = sum([len(e) for e in tens])
singletotal = sum([len(e) for e in single])
teentotal = sum([len(e) for e in teens])

print len(tens), len(single), len(teens)

print len(hund) * 900 + tentotal*100 + singletotal * 100 + singletotal * 90 + teentotal * 10 + len(thousand) - 3*9