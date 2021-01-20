# Super safe RSA 2
## 題目介紹
Wow, he made the exponent really large so the encryption MUST be safe, right?! Connect with nc 2018shell2.picoctf.com 29661.
## 思路
* 連接到他給的port之後，我們會找到n,c,e。(e,n)為public key 且 c 為 cipher
* 因為題目和我們的觀察都看到e很大，所以我們推論d應該很小，所以可能是weiner's attack的時機 
* 只要拿到private key d 我們就可以將cipher還原，並找出flag。

## 程式實作
* code
```python
import math
e = 56172436577459725698934391359139104915041430213184221292301658571726414059411889155782982024019814564512291421932489731563519296372873415080546379424619308859152360214209740169135159761234894923144971372974038021945201954600238994209605035703317119192844975463915465725406543097929017637859019950590916533609
n = 77531969503748326589677418948315140870584015245386763633241518845356850979564402923266696704186567270006361208862086254527576010412135230279553684940635956656649728134893874567619948675304052482720430367748612708917105846534082863042823913166120865362252479206576942147071396319459112580853771742537940112457
c = 1778673018511075140350698252891639557906407090250539057221806340768776705763113815373271713598206734943304136885307657644746166557801527614555955063613958550715606102502660768573300084767410478866161295739179626743292839204862654148472896949835346074323716667404949929701903737872090588147698250826373180618
def Weiners_attack(e,n):
	continued_fraction = compute_continued_fraction(e,n)
	#print(continued_fraction)
	convergences = convergences_of_fraction(continued_fraction)
	#print(convergences)
	for (k, d) in convergences:
		if(k!=0):
			fail = (e*d - 1)%k
			phi =  (e*d - 1)//k 
			if((k!=0) and (fail==0)):
				b = n - phi + 1
				determine = ( b**2 - 4*n )
				#print(determine)
				if(determine>= 0):
					(determine_sqrt) = sqrt_or_fail(determine)
					if((determine_sqrt != -1)and((b+determine_sqrt)%2 == 0)):
						return d


def compute_continued_fraction(e,n):
	integer = e // n
	number = [integer]
	while integer * n != e:
		tmp_e = e
		tmp_n = n
		e = tmp_n
		n = tmp_e - n*integer
		integer = e // n
		number.append(integer)
	return number

def convergences_of_fraction(continued_fraction):
	convergences = []
	for i in range(len(continued_fraction)):
		convergences.append(continued_fraction_to_rational(continued_fraction[0:i+1]))
	return convergences

def continued_fraction_to_rational(continued_fraction):
	fraction = 0
	if(len(continued_fraction) == 1):
		return(continued_fraction[0],1)
	#print(len(continued_fraction))
	denominator = continued_fraction[len(continued_fraction)-1]
	numerator = 1
	for i in range(2,len(continued_fraction)):
		numerator, denominator = denominator, continued_fraction[len(continued_fraction)-i]*denominator+numerator
	numerator += continued_fraction[0]*denominator
	return(numerator,denominator)


def sqrt_or_fail(determine):
	h = determine & 0xF;
	#print("h :",h)
	if h > 9:
		return -1 
	if ( h != 2 and h != 3 and h != 5 and h != 6 and h != 7 and h != 8 ):
		t = isqrt(determine)
		#print(t)
		if t*t == determine:
			return t
		else:
			return -1
	return -1

def isqrt(n):
	if n < 0:
		raise ValueError('square root not defined for negative numbers')

	if n == 0:
		return 0
	a, b = divmod(bitlength(n), 2)
	x = 2**(a+b)
	while True:
		y = (x + n//x)//2
		if y >= x:
			return x
		x = y

def bitlength(x):
	assert x >= 0
	n = 0
	while x > 0:
		n = n+1
		x = x>>1
	return n

d = Weiners_attack(e,n)
print("private_key",d)
plain_text = pow(c, d, n)
plain_text = hex(plain_text)
print(plain_text) #0x7069636f4354467b77407463685f793075725f5870306e336e74245f6340723366753131795f353439353632377d
```
透過找到 d = 65537
並還原出hex 為 0x7069636f4354467b77407463685f793075725f5870306e336e74245f6340723366753131795f353439353632377d
再透過線上hex to string轉換器，得到最後我們要的flag。
https://codebeautify.org/hex-string-converter
* flag
picoCTF{w@tch_y0ur_Xp0n3nt$_c@r3fu11y_5495627}