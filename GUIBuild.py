from config import tools

def gen_click():
    no = 1
    with open('click.py','w',encoding='utf-8')as f:
        f.write("""
import subprocess
from config import java8_path
from config import java9_path
from config import java11_path
class click():
        """
        )
        for t in tools.values():
            for cmd in t.values():
                f.write("""
    def btn_{no}():
        subprocess.Popen( {cmd} , shell=True)
                """.format(no=no,cmd=cmd))
                no += 1

def gen_body():
    i = 0
    with open('PentoolsGUI.py','w',encoding='utf-8')as f:
        f.write("""
from PySide6.QtCore import (QRect, Qt)
from PySide6.QtGui import (QFont, QIcon)
from PySide6.QtWidgets import (QApplication, QFrame, QLabel, QPushButton, QScrollArea, QSizePolicy, QStackedWidget, QVBoxLayout, QWidget)
from click import click
import sys
import resource

class pages_window(QWidget):
    def __init__(self):
        super(pages_window, self).__init__()
        self.setObjectName("Form")
        self.setFixedSize(460, 500)
        self.setWindowFlag(Qt.WindowMaximizeButtonHint, False)
        self.setWindowTitle("Pen Testing Toolkit")
        self.setWindowIcon(QIcon("resource/icon.png"))
        self.setWindowFlag(Qt.WindowStaysOnTopHint)
        self.setStyleSheet(\"""
            QPushButton:hover {
                background-color: #14161B;
            }
            QScrollArea,QWidget,QPushButton{
                background-color:transparent;
                border:0px solid #838486;
            }

            QPushButton{
                height: 28px;
                border-radius: 5px;
                color: rgb(213, 213, 214);
                font: 10pt '微软雅黑';
            }

            QScrollBar:vertical
            {
                width:1.5px;
                background:transparent;
                margin:0px,0px,0px,0px;
                padding-top:0px;
                padding-bottom:0px;
            }

            QScrollBar::handle:vertical
            {
                width:8px;
                background:#74757A;
                border-radius:4px;
                min-height:20;
            }

            QScrollBar::handle:vertical:hover
            {
                width:8px;
                background:#74757A;
                border-radius:4px;
                min-height:20;
            }

            QScrollBar::add-line:vertical
            {
                height:0px;
                width:8px;
                subcontrol-position:bottom;
            }

            QScrollBar::sub-line:vertical
            {
                height:0px;
                width:8px;
                subcontrol-position:top;
            }

            QScrollBar::add-page:vertical,QScrollBar::sub-page:vertical
            {
                background:#22252E;
                border-radius:4px;
            }
        \""")

        self.label = QLabel(self)
        self.label.setGeometry(QRect(-50, 0, 560, 500))
        self.label.setStyleSheet("image:url(resource/tool_ui.jpg);")

        self.frame = QFrame(self)
        self.frame.setGeometry(QRect(0, 27, 177, 491))
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)

        self.scrollArea = QScrollArea(self.frame)
        self.scrollArea.setGeometry(QRect(7, 0, 165, 440))
        self.scrollArea.setWidgetResizable(True)

        self.scrollAreaWidgetContents = QWidget()
        self.scrollAreaWidgetContents.setGeometry(QRect(0, 0, 191, 142))
        sizePolicy = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Fixed)
        self.scrollAreaWidgetContents.setSizePolicy(sizePolicy)

        self.verticalLayout = QVBoxLayout(self.scrollAreaWidgetContents)
        self.verticalLayout.setContentsMargins(0, 0, 5, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.frame.setStyleSheet(
            \"""
            QPushButton:hover {
                background-color: #1A1C23;
            }
            \""")
        """
        )
        n = 0
        for title,tool in tools.items():
            n=n+1
            f.write("""
        self.button_l{n} = QPushButton(self.scrollAreaWidgetContents)
        self.button_l{n}.setFont(QFont("微软雅黑", 10))
        self.verticalLayout.addWidget(self.button_l{n})
        self.button_l{n}.setText("{n}-{title}")
            """.format(title=title,n=n))
        
        f.write(
                """
        self.scrollArea.setWidget(self.scrollAreaWidgetContents)

        self.frame_2 = QFrame(self)
        self.frame_2.setGeometry(QRect(192, 27, 270, 491))
        self.frame_2.setFrameShape(QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QFrame.Raised)

        self.stackedWidget = QStackedWidget(self.frame_2)
        self.stackedWidget.setGeometry(QRect(0, 0, 291, 471))
        self.frame_2.setStyleSheet(
            \"""
            QScrollBar::add-page:vertical,QScrollBar::sub-page:vertical
            {
            background:#18191E;
            }
            \"""
        )
                """
            )
        
        button_counter = 1  # 用于小工具的编号

        for category_counter, (category, tools_dict) in enumerate(tools.items(), start=1):
            f.write("\n")
            f.write(f"        self.page_{category_counter} = QWidget()\n")
            f.write(f"        self.scrollArea_{category_counter} = QScrollArea(self.page_{category_counter})\n")
            f.write(f"        self.scrollArea_{category_counter}.setGeometry(QRect(0, 6, 256, 430))\n")
            f.write(f"        self.scrollArea_{category_counter}.setWidgetResizable(True)\n")
            f.write(f"        self.scrollAreaWidgetContents_{category_counter} = QWidget()\n")
            f.write(f"        self.scrollAreaWidgetContents_{category_counter}.setGeometry(QRect(0, 0, 271, 64))\n")
            f.write(f"        self.scrollAreaWidgetContents_{category_counter}.setSizePolicy(sizePolicy)\n")
            f.write(f"        self.scrollAreaWidgetContents_{category_counter}.setFont(QFont('微软雅黑', 10))\n")
            f.write(f"        self.verticalLayout_{category_counter} = QVBoxLayout(self.scrollAreaWidgetContents_{category_counter})\n")
            f.write(f"        self.verticalLayout_{category_counter}.setObjectName('verticalLayout_{category_counter}')\n")
            f.write(f"        self.verticalLayout_{category_counter}.setContentsMargins(0, 0, 5, 0)\n")

            for tool, command in tools_dict.items():
                f.write(f"        self.button_{category_counter}_{button_counter} = QPushButton(self.scrollAreaWidgetContents_{category_counter})\n")
                f.write(f"        self.verticalLayout_{category_counter}.addWidget(self.button_{category_counter}_{button_counter})\n")
                f.write(f"        self.button_{category_counter}_{button_counter}.setText('{tool}')\n")
                f.write(f"        self.button_{category_counter}_{button_counter}.clicked.connect(click.btn_{button_counter})\n")

                button_counter += 1

            f.write(f"        self.scrollArea_{category_counter}.setWidget(self.scrollAreaWidgetContents_{category_counter})\n")
            f.write(f"        self.stackedWidget.addWidget(self.page_{category_counter})\n")
            f.write("\n")

        f.write(f"        self.stackedWidget.setCurrentIndex(0)") 
         
        n = 0
        for title,tool in tools.items():
            n=n+1
            f.write("""
        self.button_l{n}.clicked.connect(self.display_page{n})
            """.format(n=n))    
            
        n = 0
        for title,tool in tools.items():
            n=n+1
            f.write("""
    def display_page{n}(self):
        self.stackedWidget.setCurrentIndex({n}-1)
            """.format(n=n))    
            
        f.write(
            """
if __name__ == "__main__":
    app = QApplication(sys.argv)
    main_window = pages_window()
    main_window.show()
    exit(app.exec_())
            """
        )

if __name__ == "__main__":
    gen_click()
    gen_body()