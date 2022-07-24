## 日历打印器 v3.1

> 对着《程序设计思想与方法》一步步抄出来的，边写边学，原来是python2的代码，对应python3进行了改写。

- 功能：输入年份（**v3.0之前** 1900之后），打印日历（**v1.0** 命令行 / **v2.0及之后** txt文本文件）。

#### 编译：

- 用`pyinstaller -F calendar_v1.0.py`方式打包生成exe（7.52M）。
- 用`pyinstaller -F calendar_v2.0.py`方式打包生成exe（10.1M）。
- 用`pyinstaller -F -w -i calendar.ico calendar_v3.0.py`方式打包生成`calendar_v3.0.1.exe`（10.1M）。
- 用`pyinstaller -F -w -i calendar.ico calendar_v3.0.py --upx-dir <DIR>`方式打包生成`calendar_v3.0.2.exe`（8.97M）。
- 用`pyinstaller -F -w -i calendar.ico calendar_v3.1.py`方式打包生成`calendar_v3.1.1.exe`（10.1M）。
- 用`upx calendar_v3.1.1.exe`方式压缩生成`calendar_v3.1.2.exe`（10.0M）。
- 用`pyinstaller -F -w -i calendar.ico calendar_v3.1.py --upx-dir <DIR>`方式打包生成`calendar_v3.1.3.exe`（8.97M）。
- exe文件：https://wwx.lanzoui.com/b01ihdbmd (52pj)

#### 截图：

<img src="https://z3.ax1x.com/2021/07/16/WQZdsK.png" alt="v1.0" style="zoom:50%;" />

<img src="https://z3.ax1x.com/2021/07/16/WQZNxx.jpg" alt="v2.0" style="zoom:50%;" />

[![v3.0](https://z3.ax1x.com/2021/07/18/W3ZWHf.png)](https://imgtu.com/i/W3ZWHf)

[![v3.1](https://z3.ax1x.com/2021/07/19/WJo70x.png)](https://imgtu.com/i/WJo70x)

#### 其他：

周数可能还能实现，农历有点困难，毕竟calendar模块是没有农历的，我自己也不懂农历。

> [xxdahai](https://www.52pojie.cn/home.php?mod=space&uid=107128) 农历用这个模块：zhdate  发表于 2021-8-13 11:27

#### END

[![Page Views Count](https://badges.toozhao.com/badges/01G6ZJY3322Y59H9X1J3XHN2M5/green.svg)](https://badges.toozhao.com/stats/01G6ZJY3322Y59H9X1J3XHN2M5 "Get your own page views count badge on badges.toozhao.com")
