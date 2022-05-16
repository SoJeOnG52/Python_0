#from matplotlib import pyplot as pl
import matplotlib.pyplot as plt
## 한글 폰트 설정하기
import matplotlib.font_manager as fm
f_path= 'C:\Windows\Fonts\malgun.ttf'
font= fm. FontProperties(fname=f_path, size=18)
x = ["2000", "2005", "2010", "2015", "2019"]
ko = [11030, 18520, 22290, 28720, 33720] # 한국 국민1인당 총소득
jp = [36230, 40560, 43440, 38840, 41690] # 일본
ch = [940, 1760, 4340, 7940, 10410]
# plt.plot(x, ko, color='red', maker='o', linestyle='solid')
plt.plot(x,ko,'ro-') #7 과 같은 거
plt.plot(x,jp,'b*--')
plt.plot(x,ch,'g+-.')
plt.title('아시아 1인당 국민소득', fontproperties= font)
plt.xlabel("년도" , fontproperties= font)
plt.legend()
plt.ylabel("dollars")
plt.show()