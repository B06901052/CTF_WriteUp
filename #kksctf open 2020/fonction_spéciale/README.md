# fonction_spéciale
## 題目介紹
Selon une mission secrète du gouvernement pour un ordinateur doté d'intelligence, une fonction mathématique spéciale a été développée. Voici des exemples de ses entrées et sorties:
f(2522521337)=1215221512112317 
f(1215221512112317)=1112111522111511122112131117 f(1112111522111511122112131117)=31123115223115312221121113317
Puisque l'intelligence artificielle ne veut plus nous obéir, nous avons besoin de votre aide pour trouver le résultat de la fonction
f(2229555555768432252223133777492611)=x
Le drapeau a la forme kks{x}. Dans la composition de cette fonction, j'ai été aidé par un écrivain avec les initiales B. W., qui aime aussi les énigmes, comme nous et vous ;)
## 思路
* 因為我們可以看到感覺很多元素感覺重複，所以我認為可能有一些規律
* 後來發現 1215221512112317 的意思是 2522521337 由 1個2 1個5 2個2 1個5 ... 組成

## 程式實作
* code
```python
plain_text = '2229555555768432252223133777492611'
standard = plain_text[0]
count = 0
cipher =''
for i in range(len(plain_text)):
	if(standard == plain_text[i]):
		count += 1
	else:
		cipher += str(count)
		cipher += standard
		standard = plain_text[i]
		count = 1
cipher += str(count)
cipher += standard
print(cipher) #3219651716181413221532131123371419121621
```
* flag
kks{3219651716181413221532131123371419121621}