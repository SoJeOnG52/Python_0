
from matplotlib import pyplot as plt
from matplotlib import font_manager, rc
font_path = "C:\Windows\Fonts\malgun.ttf"
font_name = font_manager.FontProperties(fname=font_path).get_name()
font=font_manager.FontProperties(fname=font_path, size=20)
rc('font', family=font_name)
x = ["Mon", "Tue", "Wed", "Thur","Fri","Sat","Sun"]
y1 = [15.6, 14.2, 16.3, 18.2, 17.1, 20.2, 22.4]
y2 = [20.1, 23.1, 23.8, 25.9, 23.4, 25.1, 26.3]
plt.plot(x, y1, 'b-', label="서울")
plt.plot(x, y2, 'r-', label="부산")
plt.title("서울/부산의 기온", fontproperties=font)
plt.xlabel("day")
plt.ylabel("기온(섭씨)")
plt.legend()
plt.show()
