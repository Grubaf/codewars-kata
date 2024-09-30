class RomanNumerals:
	SYMBOLS = {
		'M': 1000,
		'CM': 900,
		'D': 500,
		'CD': 400,
		'C': 100,
		'XC': 90,
		'L': 50,
		'XL': 40,
		'X': 10,
		'IX': 9,
		'V': 5,
		'IV': 4,
		'I': 1,
	}

	@staticmethod
	def to_roman(val : int) -> str:
		s = ''

		while val >= 1:
			for k, v in RomanNumerals.SYMBOLS.items():
				if val >= v:
					s += k
					val -= v
					break

		return s

	@staticmethod
	def from_roman(roman_num : str) -> int:
		n = 0
		a = [c for c in roman_num]

		while len(a):
			if a[0] in ['C', 'X', 'I'] and len(a) > 1 and RomanNumerals.SYMBOLS[a[1]] > RomanNumerals.SYMBOLS[a[0]]:
				n += RomanNumerals.SYMBOLS[a[1]] - RomanNumerals.SYMBOLS[a[0]]
				a = a[1:]
			else:
				n += RomanNumerals.SYMBOLS[a[0]]

			a = a[1:]

		return n
