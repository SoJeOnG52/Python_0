#경영정보학과 1851782 이소정
import numpy as np
import matplotlib.pyplot as plt
from matplotlib import font_manager, rc
font_path= "C:\Windows\Fonts\malgun.ttf"
font_name = font_manager.FontProperties(fname=font_path).get_name()
font = font_manager.FontProperties(fname=font_path, size= 15)
rc('font', family=font_name)
xtemp = ["2021.08", "2021.09", "2021.10", "2021.11", "2021.12", "2022.01"]
ytemp1 = [12639, 12541,	 12330,	 12325,	 13272,	 13238]
ytemp2 = [2748, 2474, 2679, 3496, 4934, 5837]
ytemp3 = [479, 431, 413, 439, 575, 503]
x= np.array(xtemp)
y1= np.array(ytemp1)
y2= np.array(ytemp2)
y3= np.array(ytemp3)
plt.plot(x, y1, 'r*-', label="산업")
plt.plot(x, y2, 'bo-', label="가정・상업")
plt.plot(x, y3, 'g+-', label="공공")
plt.title("최종 에너지 부문별 소비", fontproperties=font)
plt.ylabel("에너지량")
plt.xlabel("년도")
plt.show()