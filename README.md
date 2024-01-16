# 欢迎使用 Pentools 集成工具箱！

Pentools 是一个渗透集成工具箱，旨在为零散的渗透工具提供集成 UI ，使用者可以自定义添加工具，自己搭建属于自己的渗透武器库，从而提高工作效率

<cent><img src="https://github.com/WuTongLiRan/Pentool/assets/134190463/14370278-1089-487b-8a57-91c0461e9489" alt="Pentool_README-1" width="40%" /></cent>

<cent>效果图⬆</cent>

> 此项目为本人初学两天 Python 的成果，也是本人的第一个项目。难免在代码和实现逻辑上不够优雅，大佬不喜勿喷

​	

## 安装

1. 要使用 Pentools 需要安装 PySide6 库 

   ```
   pip install PySide6
   
   //若下载慢可以换源,以下是使用清华pip源的下载示例：
   pip install PySide6 -i https://pypi.tuna.tsinghua.edu.cn/simple
   ```

2. 将项目下载到本地 (可通过 git 将项目下载到指定目录，或者手动下载 zip 压缩包并解压到指定目录)

3. 下载作为示例的渗透工具和 JDK 到项目目录下 (可选，也可以不下载)

   百度网盘-https://pan.baidu.com/s/1VW0CI-uzLD5zDAaA1GbMdA?pwd=24mh

   123云盘-https://www.123pan.com/s/C5VRVv-EtEAA.html提取码:04MZ

> 注意注意注意：这些渗透工具和 JDK 是通过网上收集而来，无法保证其安全性！！！无法保证其安全性！！！无法保证其安全性！！！
>
> 仅作为初次使用的参考
>
> 强烈建议熟悉如何添加工具列表后删掉这些渗透工具和 Java 文件，配置自己收集的工具和语言环境

一切就绪后项目目录结构如下：

```
├── gui_pentest
├── gui_scan
├── gui_shouji
├── resource
├── Java_path
├── GUIBuild.py
├── click.py
├── Pentools.bat
├── PentoolsGUI.py
├── config.py
├── 一键启动.vbs
└── README.MD
```

​	

## 原理

`GUIBuild.py`  通过读取 `config.py` 里的数据，自动生成 `PentoolsGUI.py` (UI 界面) 和 `click.py` (点击事件) 

​	

## 快速入门

1.打开 Pentools.bat ，将 python.exe 的路径修改成自己电脑上的正确路径

```
E:\Python\Python37\python.exe GUIBuild.py
E:\Python\Python37\python.exe PentoolGUI.py

//将python.exe的路径修改成自己电脑上的正确路径
//如果电脑不支持这种运行方式就直接改成 python GUIBuild.py 和 python PentoolsGUI.py
```

2.打开 config.py ，配置工具列表以及执行语句

```python
python = 'python3'#运行 Python 工具时使用的 Python 版本
tools = {
'工具分类1':{
         '工具1':
         "'执行语句 '",

         '工具2':
         "'执行语句 '",
         
},  

'工具分类2':{
         '工具1':
         "'执行语句'",

},
......
}
#执行语句的格式看下面的讲解

#设置电脑上的 JDK 路径
tools_path = os.getcwd()
if platform.system() == 'Windows' :
    java8_path = (tools_path + "\Java_path\jre_1.8_win\\bin\java").replace('\\','\\\\')#这里的路径是相对路径
    java9_path = (tools_path + "\Java_path\java9_win\\bin\java").replace('\\','\\\\')
    java11_path = (tools_path + "\Java_path\Java_11_win\\bin\java").replace('\\','\\\\')
else:
    java8_path = tools_path + "/Java_path/java_1.8/bin/java"
    java9_path = tools_path + "/Java_path/java9/bin/java"
    java11_path = tools_path + "/Java_path/Java_11_win/bin/java"
```

3.双击 `一键启动.vbs` 启动 UI

​	

## 如何配置工具列表？

可以去看一下 `click.py` ，用到了 `subprocess` 库

CMD 命令行工具，执行语句格式如下：

```
"'start cmd /k \"cd 工具路径" '",

例如：
'Dirsearch':
"'start cmd /k \"cd gui_shouji\Dirsearch\" '",
'Sqlmap':
" 'start cmd /k \"cd gui_pentest\Sqlmap\" ' ",
```

Python 工具，执行语句格式如下：

```
" '{python} {base_dir}工具/相对路径/工具.py ' ".format(python=python,base_dir=base_dir),

例如：
'Gr33k漏洞利用工具集':
" '{python} {base_dir}/gui_scan/Gr33k/Gr33k.py ' ".format(python=python,base_dir=base_dir),
```

exe 工具，执行语句格式如下：

```
"'cd 工具路径 && 工具.exe'",

例如：
'御剑扫描珍藏版 v1.1':
"'cd gui_shouji/yjdirscanv1.1 && 御剑目录扫描专业版v1.1.exe'",
```

Java 工具，执行语句格式如下：

```
一般是：
"'cd 工具路径 && ' + Java可执行文件路径 + ' -jar ' + '工具.jar'",

例如：
'通达OA综合利用工具 v1.0':
"'cd gui_scan && ' + java8_path + ' -jar ' + 'TODA.jar'",


必要时候也可以加上一些参数例如：
'BurpSuite_pro v2022.6':
"'cd gui_pentest/BurpSuite_Pro && ' + java11_path + ' -Xmx2048m -Dfile.encoding=utf-8 --illegal-access=permit -Dfile.encoding=utf-8 -javaagent:BurpSuiteLoader_v2022.jar -noverify -jar burpsuite_pro_v2022.6.1.jar'",

-Xmx2048m：设置 Java 虚拟机的最大堆内存为 2GB。
-Dfile.encoding=utf-8：用于设置 JVM 的字符编码为 UTF-8。
--illegal-access=permit：允许不安全的访问操作，这通常用于处理 Java 9+ 的非法访问限制。
-javaagent:BurpSuiteLoader_v2022.jar：指定了 Java 代理，这通常用于加载 Burp Suite Pro 的插件。
-noverify：禁用类文件验证，这有助于提高执行速度。
```

​	

## 运行

双击 `一键启动.vbs`

​	

## 通过全局快捷键启动

Pentools 本身没有快捷键启动的功能，可以配合办公效率神器 utools 来实现该功能

首先下载 utools ，完成基本的设置(账号注册、开机自启等等)

点开 个人中心 -> 本地文件启动，将 `一键启动.vbs` 拖入其中

打开 全局快捷键 界面，如图设置

<img src="https://github.com/WuTongLiRan/Pentools/assets/134190463/714446b9-b77e-49fb-8202-eb9c835e6a65" alt="Pentool_README-2" width="50%" />


到这里就大功告成了，当想要打开 Pentools 时，按下设置的快捷键：Ctrl+Tab 就能直接启动

​	

## 感谢

感谢以下项目，Pentool 受到了它们的启发：

- [PenKitGui](https://github.com/ccc-f/PenKitGui)
- One-Fox 渗透测试工具箱
