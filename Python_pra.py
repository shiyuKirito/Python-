import urllib.request


class city:
    city_id = int(101050100)# 19 17 11 11 11 07 08 17 10 05 10 09 09
    city_str1 = str(r'http://www.weather.com.cn/weather/')
    city_str2 = str(r'.shtml" target="_blank">')
    city_str3 = str(r'<')
    city_len1 = len(city_str1)+len(city_str2)+len(city_str3)+len(str(city_id))
    city_jump = list()
    city_jump = [19, 17, 11, 11, 11, 7, 8, 17, 10, 5, 10, 9, 9]
    city_jump_id = 0
    
    def __init__(self):
        city.city_id += 1
        if city.city_id == 101050707: # 没有101050707
            city.city_id += 1

    def solve(self):
        self.getname()
        self.getwea_am()
        self.getwind_am()
        self.getmaxtem_am()
        self.getwea_pm()
        self.getwind_pm()
        self.getmintem_pm()
        self.nex()

    def getname(self):
        global strall
        self.city_str = city.city_str1+str(city.city_id)+city.city_str2
        strall.find(self.city_str)
        self.ans_str = strall[strall.find(self.city_str)+city.city_len1-1:len(strall)]
        strall = strall[strall.find(self.city_str)+city.city_len1-1:len(strall)]
        self.ans_str = self.ans_str[:self.ans_str.find(city.city_str3)]
        ans.append(self.ans_str)

    def getwea_am(self):
        global strall
        self.ans_str = strall[strall.find('width="89"')+len('width="89">'):len(strall)]
        strall = strall[strall.find('width="89">')+len('width="89">'):len(strall)]
        self.ans_str = self.ans_str[:self.ans_str.find(city.city_str3)]
        ans.append(self.ans_str)

    def getwind_am(self):
        global strall
        self.ans_str = strall[strall.find('<span>')+len('<span>'):len(strall)]
        strall = strall[strall.find('<span>')+len('<span>'):len(strall)]
        self.ans_str = self.ans_str[:self.ans_str.find(city.city_str3)]
        ans.append(self.ans_str)
        self.ans_str = strall[strall.find('class="conMidtabright">')+len('class="conMidtabright>"'):len(strall)]
        strall = strall[strall.find('class="conMidtabright">')+len('class="conMidtabright">'):len(strall)]
        self.ans_str = self.ans_str[:self.ans_str.find(r'</span')]
        ans.append(self.ans_str)

    def getmaxtem_am(self):
        global strall
        self.ans_str = strall[strall.find('width="92">')+len('width="92">'):len(strall)]
        strall = strall[strall.find('width="92">')+len('width="92">'):len(strall)]
        self.ans_str = self.ans_str[:self.ans_str.find(city.city_str3)]
        ans.append(self.ans_str)

    def getwea_pm(self):
        global strall
        self.ans_str = strall[strall.find('width="98">')+len('width="98">'):len(strall)]
        strall = strall[strall.find('width="98">')+len('width="98">'):len(strall)]
        self.ans_str = self.ans_str[:self.ans_str.find(city.city_str3)]
        ans.append(self.ans_str)

    def getwind_pm(self):
        global strall
        self.ans_str = strall[strall.find('<span>')+len('<span>'):len(strall)]
        strall = strall[strall.find('<span>')+len('<span>'):len(strall)]
        self.ans_str = self.ans_str[:self.ans_str.find(city.city_str3)]
        ans.append(self.ans_str)
        self.ans_str = strall[strall.find('class="conMidtabright">')+len('class="conMidtabright>"'):len(strall)]
        strall = strall[strall.find('class="conMidtabright">')+len('class="conMidtabright">'):len(strall)]
        self.ans_str = self.ans_str[:self.ans_str.find(r'</span')]
        ans.append(self.ans_str)

    def getmintem_pm(self):
        global strall
        self.ans_str = strall[strall.find('width="86">')+len('width="86">'):len(strall)]
        strall = strall[strall.find('width="86">')+len('width="86">'):len(strall)]
        self.ans_str = self.ans_str[:self.ans_str.find(city.city_str3)]
        ans.append(self.ans_str)

    def nex(self):
        if city.city_id % 100 == city.city_jump[city.city_jump_id]:
            city.city_id = city.city_id-city.city_jump[city.city_jump_id]+100
            city.city_jump_id += 1


fp = urllib.request.urlopen(r'http://www.weather.com.cn/textFC/heilongjiang.shtml#')
strall = str(fp.read().decode('utf-8'))
ans = list()
ans = ['城市', '白天天气现象', '白天风向', '白天风力', '白天最高气温', '夜间天气现象', '夜间风向', '夜间风力', '夜间最低气温']
c1 = city()
c1.solve()
for i in range(1, 143):
    c1 = city()
    c1.solve()
cnt = 0
for i in ans:
    print('%-10s'%i, end='\t')
    cnt += 1
    if cnt % 9 == 0:
        print('')
        