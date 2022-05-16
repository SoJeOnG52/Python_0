from matplotlib import pyplot as plt
#import matplotlib.pyplot as plt
from matplotlib import font_manager, rc
font_path= "C:\Windows\Fonts\malgun.ttf"
font_name = font_manager.FontProperties(fname=font_path).get_name()
font = font_manager.FontProperties(fname=font_path, size= 20)
rc('font', family=font_name)
x = ["2000", "2005", "2010", "2015", "2019"]
ko = [11030, 18520, 22290, 28720, 33720]
jp = [36230, 40560, 43440, 38840, 41690]
ch = [940, 1760, 4340, 7940, 10410]
plt.plot(x, ko, 'b-', label="한국")
plt.plot(x, jp, 'r-', label="일본")
plt.plot(x, ch, 'g-', label="중국")
plt.title("한국 1인당 국민소득", fontproperties=font)
plt.ylabel("dollars")
plt.xlabel("년도")
plt.savefig("한국 1인당 국민소득.png", dpi=600)
plt.show()