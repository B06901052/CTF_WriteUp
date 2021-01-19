# Red Team
## 題目介紹
We overheard that Shou's company hoarded a shiny flag at a super secret subdomain.

His company's domain: shoustinycompany.cf (Challenge is down now)

Note: You are allowed to use subdomain scanner in this challenge.
* shoustinycompany.cf

## 思路
* 用[subdomain scanner](https://pentest-tools.com/information-gathering/find-subdomains-of-domain#)掃描給的網域
  * 得到 docs.shoustinycompany.cf
* 進去看到兩個txt
![](img/README_2021-01-20-02-40-50.png)
* 進到lookingglassv1.shoustinycompany.cf發現一個可以輸入dig, ip指令的欄位``
* ```dig @142.93.28.144 shoustinycompany.cf axfr```
* 列出的其中一個subdomain，連進去就是flag
  * rea11ysu9erse3retsubd0ma1n00000.shoustinycompany.cf