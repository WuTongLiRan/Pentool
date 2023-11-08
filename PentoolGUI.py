
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
        self.setStyleSheet("""
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
        """)

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
            """
            QPushButton:hover {
                background-color: #1A1C23;
            }
            """)
        
        self.button_l1 = QPushButton(self.scrollAreaWidgetContents)
        self.button_l1.setFont(QFont("微软雅黑", 10))
        self.verticalLayout.addWidget(self.button_l1)
        self.button_l1.setText("1-漏洞利用")
            
        self.button_l2 = QPushButton(self.scrollAreaWidgetContents)
        self.button_l2.setFont(QFont("微软雅黑", 10))
        self.verticalLayout.addWidget(self.button_l2)
        self.button_l2.setText("2-渗透测试")
            
        self.button_l3 = QPushButton(self.scrollAreaWidgetContents)
        self.button_l3.setFont(QFont("微软雅黑", 10))
        self.verticalLayout.addWidget(self.button_l3)
        self.button_l3.setText("3-信息收集")
            
        self.button_l4 = QPushButton(self.scrollAreaWidgetContents)
        self.button_l4.setFont(QFont("微软雅黑", 10))
        self.verticalLayout.addWidget(self.button_l4)
        self.button_l4.setText("4-密码攻击")
            
        self.button_l5 = QPushButton(self.scrollAreaWidgetContents)
        self.button_l5.setFont(QFont("微软雅黑", 10))
        self.verticalLayout.addWidget(self.button_l5)
        self.button_l5.setText("5-无线攻击")
            
        self.button_l6 = QPushButton(self.scrollAreaWidgetContents)
        self.button_l6.setFont(QFont("微软雅黑", 10))
        self.verticalLayout.addWidget(self.button_l6)
        self.button_l6.setText("6-逆向工程")
            
        self.button_l7 = QPushButton(self.scrollAreaWidgetContents)
        self.button_l7.setFont(QFont("微软雅黑", 10))
        self.verticalLayout.addWidget(self.button_l7)
        self.button_l7.setText("7-权限维持")
            
        self.button_l8 = QPushButton(self.scrollAreaWidgetContents)
        self.button_l8.setFont(QFont("微软雅黑", 10))
        self.verticalLayout.addWidget(self.button_l8)
        self.button_l8.setText("8-数字取证")
            
        self.button_l9 = QPushButton(self.scrollAreaWidgetContents)
        self.button_l9.setFont(QFont("微软雅黑", 10))
        self.verticalLayout.addWidget(self.button_l9)
        self.button_l9.setText("9-报告工具集")
            
        self.button_l10 = QPushButton(self.scrollAreaWidgetContents)
        self.button_l10.setFont(QFont("微软雅黑", 10))
        self.verticalLayout.addWidget(self.button_l10)
        self.button_l10.setText("10-嗅探/欺骗")
            
        self.button_l11 = QPushButton(self.scrollAreaWidgetContents)
        self.button_l11.setFont(QFont("微软雅黑", 10))
        self.verticalLayout.addWidget(self.button_l11)
        self.button_l11.setText("11-数据库评估软件")
            
        self.button_l12 = QPushButton(self.scrollAreaWidgetContents)
        self.button_l12.setFont(QFont("微软雅黑", 10))
        self.verticalLayout.addWidget(self.button_l12)
        self.button_l12.setText("12-Web程序")
            
        self.button_l13 = QPushButton(self.scrollAreaWidgetContents)
        self.button_l13.setFont(QFont("微软雅黑", 10))
        self.verticalLayout.addWidget(self.button_l13)
        self.button_l13.setText("13-某某某分类1")
            
        self.button_l14 = QPushButton(self.scrollAreaWidgetContents)
        self.button_l14.setFont(QFont("微软雅黑", 10))
        self.verticalLayout.addWidget(self.button_l14)
        self.button_l14.setText("14-某某某分类2")
            
        self.button_l15 = QPushButton(self.scrollAreaWidgetContents)
        self.button_l15.setFont(QFont("微软雅黑", 10))
        self.verticalLayout.addWidget(self.button_l15)
        self.button_l15.setText("15-某某某分类3")
            
        self.button_l16 = QPushButton(self.scrollAreaWidgetContents)
        self.button_l16.setFont(QFont("微软雅黑", 10))
        self.verticalLayout.addWidget(self.button_l16)
        self.button_l16.setText("16-某某某分类4")
            
        self.scrollArea.setWidget(self.scrollAreaWidgetContents)

        self.frame_2 = QFrame(self)
        self.frame_2.setGeometry(QRect(192, 27, 270, 491))
        self.frame_2.setFrameShape(QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QFrame.Raised)

        self.stackedWidget = QStackedWidget(self.frame_2)
        self.stackedWidget.setGeometry(QRect(0, 0, 291, 471))
        self.frame_2.setStyleSheet(
            """
            QScrollBar::add-page:vertical,QScrollBar::sub-page:vertical
            {
            background:#18191E;
            }
            """
        )
                
        self.page_1 = QWidget()
        self.scrollArea_1 = QScrollArea(self.page_1)
        self.scrollArea_1.setGeometry(QRect(0, 6, 256, 430))
        self.scrollArea_1.setWidgetResizable(True)
        self.scrollAreaWidgetContents_1 = QWidget()
        self.scrollAreaWidgetContents_1.setGeometry(QRect(0, 0, 271, 64))
        self.scrollAreaWidgetContents_1.setSizePolicy(sizePolicy)
        self.scrollAreaWidgetContents_1.setFont(QFont('微软雅黑', 10))
        self.verticalLayout_1 = QVBoxLayout(self.scrollAreaWidgetContents_1)
        self.verticalLayout_1.setObjectName('verticalLayout_1')
        self.verticalLayout_1.setContentsMargins(0, 0, 5, 0)
        self.button_1_1 = QPushButton(self.scrollAreaWidgetContents_1)
        self.verticalLayout_1.addWidget(self.button_1_1)
        self.button_1_1.setText('打开漏洞利用目录')
        self.button_1_1.clicked.connect(click.btn_1)
        self.button_1_2 = QPushButton(self.scrollAreaWidgetContents_1)
        self.verticalLayout_1.addWidget(self.button_1_2)
        self.button_1_2.setText('打开Powershell')
        self.button_1_2.clicked.connect(click.btn_2)
        self.button_1_3 = QPushButton(self.scrollAreaWidgetContents_1)
        self.verticalLayout_1.addWidget(self.button_1_3)
        self.button_1_3.setText('403bypasser')
        self.button_1_3.clicked.connect(click.btn_3)
        self.button_1_4 = QPushButton(self.scrollAreaWidgetContents_1)
        self.verticalLayout_1.addWidget(self.button_1_4)
        self.button_1_4.setText('通达OA综合利用工具 v1.0')
        self.button_1_4.clicked.connect(click.btn_4)
        self.button_1_5 = QPushButton(self.scrollAreaWidgetContents_1)
        self.verticalLayout_1.addWidget(self.button_1_5)
        self.button_1_5.setText('Gr33k漏洞利用工具集')
        self.button_1_5.clicked.connect(click.btn_5)
        self.button_1_6 = QPushButton(self.scrollAreaWidgetContents_1)
        self.verticalLayout_1.addWidget(self.button_1_6)
        self.button_1_6.setText('Cas反序列化利用工具v1.1')
        self.button_1_6.clicked.connect(click.btn_6)
        self.button_1_7 = QPushButton(self.scrollAreaWidgetContents_1)
        self.verticalLayout_1.addWidget(self.button_1_7)
        self.button_1_7.setText('神机 v1.9')
        self.button_1_7.clicked.connect(click.btn_7)
        self.button_1_8 = QPushButton(self.scrollAreaWidgetContents_1)
        self.verticalLayout_1.addWidget(self.button_1_8)
        self.button_1_8.setText('ThinkPHP综合利用工具 v2.3')
        self.button_1_8.clicked.connect(click.btn_8)
        self.button_1_9 = QPushButton(self.scrollAreaWidgetContents_1)
        self.verticalLayout_1.addWidget(self.button_1_9)
        self.button_1_9.setText('ThinkPhp漏洞利用工具 v1.2')
        self.button_1_9.clicked.connect(click.btn_9)
        self.button_1_10 = QPushButton(self.scrollAreaWidgetContents_1)
        self.verticalLayout_1.addWidget(self.button_1_10)
        self.button_1_10.setText('ThinkPhp命令执行检测工具')
        self.button_1_10.clicked.connect(click.btn_10)
        self.button_1_11 = QPushButton(self.scrollAreaWidgetContents_1)
        self.verticalLayout_1.addWidget(self.button_1_11)
        self.button_1_11.setText('Weblogic-framework v0.2.3')
        self.button_1_11.clicked.connect(click.btn_11)
        self.button_1_12 = QPushButton(self.scrollAreaWidgetContents_1)
        self.verticalLayout_1.addWidget(self.button_1_12)
        self.button_1_12.setText('Weblogic-Exp-Snapshot-all v1.0')
        self.button_1_12.clicked.connect(click.btn_12)
        self.button_1_13 = QPushButton(self.scrollAreaWidgetContents_1)
        self.verticalLayout_1.addWidget(self.button_1_13)
        self.button_1_13.setText('深X服edr任意用户登陆检测工具')
        self.button_1_13.clicked.connect(click.btn_13)
        self.button_1_14 = QPushButton(self.scrollAreaWidgetContents_1)
        self.verticalLayout_1.addWidget(self.button_1_14)
        self.button_1_14.setText('Shiro-exp_v2.51_by飞鸿')
        self.button_1_14.clicked.connect(click.btn_14)
        self.button_1_15 = QPushButton(self.scrollAreaWidgetContents_1)
        self.verticalLayout_1.addWidget(self.button_1_15)
        self.button_1_15.setText('ShiroScan反序列化回显工具v1.1')
        self.button_1_15.clicked.connect(click.btn_15)
        self.button_1_16 = QPushButton(self.scrollAreaWidgetContents_1)
        self.verticalLayout_1.addWidget(self.button_1_16)
        self.button_1_16.setText('Shiro attack v2.2_j1anFen')
        self.button_1_16.clicked.connect(click.btn_16)
        self.button_1_17 = QPushButton(self.scrollAreaWidgetContents_1)
        self.verticalLayout_1.addWidget(self.button_1_17)
        self.button_1_17.setText('Spring 漏洞利用工具v1.3')
        self.button_1_17.clicked.connect(click.btn_17)
        self.button_1_18 = QPushButton(self.scrollAreaWidgetContents_1)
        self.verticalLayout_1.addWidget(self.button_1_18)
        self.button_1_18.setText('Log4j')
        self.button_1_18.clicked.connect(click.btn_18)
        self.button_1_19 = QPushButton(self.scrollAreaWidgetContents_1)
        self.verticalLayout_1.addWidget(self.button_1_19)
        self.button_1_19.setText('OracleShellv1.0')
        self.button_1_19.clicked.connect(click.btn_19)
        self.button_1_20 = QPushButton(self.scrollAreaWidgetContents_1)
        self.verticalLayout_1.addWidget(self.button_1_20)
        self.button_1_20.setText('Tomcat弱密码检查')
        self.button_1_20.clicked.connect(click.btn_20)
        self.button_1_21 = QPushButton(self.scrollAreaWidgetContents_1)
        self.verticalLayout_1.addWidget(self.button_1_21)
        self.button_1_21.setText('FastJson反序列化检查工具')
        self.button_1_21.clicked.connect(click.btn_21)
        self.button_1_22 = QPushButton(self.scrollAreaWidgetContents_1)
        self.verticalLayout_1.addWidget(self.button_1_22)
        self.button_1_22.setText('Aliyun_AKTools_by_T00ls')
        self.button_1_22.clicked.connect(click.btn_22)
        self.button_1_23 = QPushButton(self.scrollAreaWidgetContents_1)
        self.verticalLayout_1.addWidget(self.button_1_23)
        self.button_1_23.setText('MDUT数据库利用工具')
        self.button_1_23.clicked.connect(click.btn_23)
        self.scrollArea_1.setWidget(self.scrollAreaWidgetContents_1)
        self.stackedWidget.addWidget(self.page_1)


        self.page_2 = QWidget()
        self.scrollArea_2 = QScrollArea(self.page_2)
        self.scrollArea_2.setGeometry(QRect(0, 6, 256, 430))
        self.scrollArea_2.setWidgetResizable(True)
        self.scrollAreaWidgetContents_2 = QWidget()
        self.scrollAreaWidgetContents_2.setGeometry(QRect(0, 0, 271, 64))
        self.scrollAreaWidgetContents_2.setSizePolicy(sizePolicy)
        self.scrollAreaWidgetContents_2.setFont(QFont('微软雅黑', 10))
        self.verticalLayout_2 = QVBoxLayout(self.scrollAreaWidgetContents_2)
        self.verticalLayout_2.setObjectName('verticalLayout_2')
        self.verticalLayout_2.setContentsMargins(0, 0, 5, 0)
        self.button_2_24 = QPushButton(self.scrollAreaWidgetContents_2)
        self.verticalLayout_2.addWidget(self.button_2_24)
        self.button_2_24.setText('打开渗透测试目录')
        self.button_2_24.clicked.connect(click.btn_24)
        self.button_2_25 = QPushButton(self.scrollAreaWidgetContents_2)
        self.verticalLayout_2.addWidget(self.button_2_25)
        self.button_2_25.setText('打开Powershell')
        self.button_2_25.clicked.connect(click.btn_25)
        self.button_2_26 = QPushButton(self.scrollAreaWidgetContents_2)
        self.verticalLayout_2.addWidget(self.button_2_26)
        self.button_2_26.setText('Godzilla v4.0')
        self.button_2_26.clicked.connect(click.btn_26)
        self.button_2_27 = QPushButton(self.scrollAreaWidgetContents_2)
        self.verticalLayout_2.addWidget(self.button_2_27)
        self.button_2_27.setText('冰蝎 T00ls 专版v3.0 Beta 11')
        self.button_2_27.clicked.connect(click.btn_27)
        self.button_2_28 = QPushButton(self.scrollAreaWidgetContents_2)
        self.verticalLayout_2.addWidget(self.button_2_28)
        self.button_2_28.setText('冰蝎魔改版 v3.3.2')
        self.button_2_28.clicked.connect(click.btn_28)
        self.button_2_29 = QPushButton(self.scrollAreaWidgetContents_2)
        self.verticalLayout_2.addWidget(self.button_2_29)
        self.button_2_29.setText('天蝎权限管理工具')
        self.button_2_29.clicked.connect(click.btn_29)
        self.button_2_30 = QPushButton(self.scrollAreaWidgetContents_2)
        self.verticalLayout_2.addWidget(self.button_2_30)
        self.button_2_30.setText('BurpSuite_pro v2022.3 ')
        self.button_2_30.clicked.connect(click.btn_30)
        self.button_2_31 = QPushButton(self.scrollAreaWidgetContents_2)
        self.verticalLayout_2.addWidget(self.button_2_31)
        self.button_2_31.setText('CobaltStrike 去特征版 v4.4')
        self.button_2_31.clicked.connect(click.btn_31)
        self.scrollArea_2.setWidget(self.scrollAreaWidgetContents_2)
        self.stackedWidget.addWidget(self.page_2)


        self.page_3 = QWidget()
        self.scrollArea_3 = QScrollArea(self.page_3)
        self.scrollArea_3.setGeometry(QRect(0, 6, 256, 430))
        self.scrollArea_3.setWidgetResizable(True)
        self.scrollAreaWidgetContents_3 = QWidget()
        self.scrollAreaWidgetContents_3.setGeometry(QRect(0, 0, 271, 64))
        self.scrollAreaWidgetContents_3.setSizePolicy(sizePolicy)
        self.scrollAreaWidgetContents_3.setFont(QFont('微软雅黑', 10))
        self.verticalLayout_3 = QVBoxLayout(self.scrollAreaWidgetContents_3)
        self.verticalLayout_3.setObjectName('verticalLayout_3')
        self.verticalLayout_3.setContentsMargins(0, 0, 5, 0)
        self.button_3_32 = QPushButton(self.scrollAreaWidgetContents_3)
        self.verticalLayout_3.addWidget(self.button_3_32)
        self.button_3_32.setText('打开信息收集目录')
        self.button_3_32.clicked.connect(click.btn_32)
        self.button_3_33 = QPushButton(self.scrollAreaWidgetContents_3)
        self.verticalLayout_3.addWidget(self.button_3_33)
        self.button_3_33.setText('打开Powershell')
        self.button_3_33.clicked.connect(click.btn_33)
        self.button_3_34 = QPushButton(self.scrollAreaWidgetContents_3)
        self.verticalLayout_3.addWidget(self.button_3_34)
        self.button_3_34.setText('御剑扫描珍藏版 v1.1')
        self.button_3_34.clicked.connect(click.btn_34)
        self.button_3_35 = QPushButton(self.scrollAreaWidgetContents_3)
        self.verticalLayout_3.addWidget(self.button_3_35)
        self.button_3_35.setText('Dirscan v3.0')
        self.button_3_35.clicked.connect(click.btn_35)
        self.button_3_36 = QPushButton(self.scrollAreaWidgetContents_3)
        self.verticalLayout_3.addWidget(self.button_3_36)
        self.button_3_36.setText('WebFinder v3.2')
        self.button_3_36.clicked.connect(click.btn_36)
        self.button_3_37 = QPushButton(self.scrollAreaWidgetContents_3)
        self.verticalLayout_3.addWidget(self.button_3_37)
        self.button_3_37.setText('Fofa_viewer v1.8')
        self.button_3_37.clicked.connect(click.btn_37)
        self.button_3_38 = QPushButton(self.scrollAreaWidgetContents_3)
        self.verticalLayout_3.addWidget(self.button_3_38)
        self.button_3_38.setText('Sqlmap')
        self.button_3_38.clicked.connect(click.btn_38)
        self.button_3_39 = QPushButton(self.scrollAreaWidgetContents_3)
        self.verticalLayout_3.addWidget(self.button_3_39)
        self.button_3_39.setText('JsFinder')
        self.button_3_39.clicked.connect(click.btn_39)
        self.button_3_40 = QPushButton(self.scrollAreaWidgetContents_3)
        self.verticalLayout_3.addWidget(self.button_3_40)
        self.button_3_40.setText('PackerFuzzer v1.3')
        self.button_3_40.clicked.connect(click.btn_40)
        self.scrollArea_3.setWidget(self.scrollAreaWidgetContents_3)
        self.stackedWidget.addWidget(self.page_3)


        self.page_4 = QWidget()
        self.scrollArea_4 = QScrollArea(self.page_4)
        self.scrollArea_4.setGeometry(QRect(0, 6, 256, 430))
        self.scrollArea_4.setWidgetResizable(True)
        self.scrollAreaWidgetContents_4 = QWidget()
        self.scrollAreaWidgetContents_4.setGeometry(QRect(0, 0, 271, 64))
        self.scrollAreaWidgetContents_4.setSizePolicy(sizePolicy)
        self.scrollAreaWidgetContents_4.setFont(QFont('微软雅黑', 10))
        self.verticalLayout_4 = QVBoxLayout(self.scrollAreaWidgetContents_4)
        self.verticalLayout_4.setObjectName('verticalLayout_4')
        self.verticalLayout_4.setContentsMargins(0, 0, 5, 0)
        self.scrollArea_4.setWidget(self.scrollAreaWidgetContents_4)
        self.stackedWidget.addWidget(self.page_4)


        self.page_5 = QWidget()
        self.scrollArea_5 = QScrollArea(self.page_5)
        self.scrollArea_5.setGeometry(QRect(0, 6, 256, 430))
        self.scrollArea_5.setWidgetResizable(True)
        self.scrollAreaWidgetContents_5 = QWidget()
        self.scrollAreaWidgetContents_5.setGeometry(QRect(0, 0, 271, 64))
        self.scrollAreaWidgetContents_5.setSizePolicy(sizePolicy)
        self.scrollAreaWidgetContents_5.setFont(QFont('微软雅黑', 10))
        self.verticalLayout_5 = QVBoxLayout(self.scrollAreaWidgetContents_5)
        self.verticalLayout_5.setObjectName('verticalLayout_5')
        self.verticalLayout_5.setContentsMargins(0, 0, 5, 0)
        self.scrollArea_5.setWidget(self.scrollAreaWidgetContents_5)
        self.stackedWidget.addWidget(self.page_5)


        self.page_6 = QWidget()
        self.scrollArea_6 = QScrollArea(self.page_6)
        self.scrollArea_6.setGeometry(QRect(0, 6, 256, 430))
        self.scrollArea_6.setWidgetResizable(True)
        self.scrollAreaWidgetContents_6 = QWidget()
        self.scrollAreaWidgetContents_6.setGeometry(QRect(0, 0, 271, 64))
        self.scrollAreaWidgetContents_6.setSizePolicy(sizePolicy)
        self.scrollAreaWidgetContents_6.setFont(QFont('微软雅黑', 10))
        self.verticalLayout_6 = QVBoxLayout(self.scrollAreaWidgetContents_6)
        self.verticalLayout_6.setObjectName('verticalLayout_6')
        self.verticalLayout_6.setContentsMargins(0, 0, 5, 0)
        self.scrollArea_6.setWidget(self.scrollAreaWidgetContents_6)
        self.stackedWidget.addWidget(self.page_6)


        self.page_7 = QWidget()
        self.scrollArea_7 = QScrollArea(self.page_7)
        self.scrollArea_7.setGeometry(QRect(0, 6, 256, 430))
        self.scrollArea_7.setWidgetResizable(True)
        self.scrollAreaWidgetContents_7 = QWidget()
        self.scrollAreaWidgetContents_7.setGeometry(QRect(0, 0, 271, 64))
        self.scrollAreaWidgetContents_7.setSizePolicy(sizePolicy)
        self.scrollAreaWidgetContents_7.setFont(QFont('微软雅黑', 10))
        self.verticalLayout_7 = QVBoxLayout(self.scrollAreaWidgetContents_7)
        self.verticalLayout_7.setObjectName('verticalLayout_7')
        self.verticalLayout_7.setContentsMargins(0, 0, 5, 0)
        self.scrollArea_7.setWidget(self.scrollAreaWidgetContents_7)
        self.stackedWidget.addWidget(self.page_7)


        self.page_8 = QWidget()
        self.scrollArea_8 = QScrollArea(self.page_8)
        self.scrollArea_8.setGeometry(QRect(0, 6, 256, 430))
        self.scrollArea_8.setWidgetResizable(True)
        self.scrollAreaWidgetContents_8 = QWidget()
        self.scrollAreaWidgetContents_8.setGeometry(QRect(0, 0, 271, 64))
        self.scrollAreaWidgetContents_8.setSizePolicy(sizePolicy)
        self.scrollAreaWidgetContents_8.setFont(QFont('微软雅黑', 10))
        self.verticalLayout_8 = QVBoxLayout(self.scrollAreaWidgetContents_8)
        self.verticalLayout_8.setObjectName('verticalLayout_8')
        self.verticalLayout_8.setContentsMargins(0, 0, 5, 0)
        self.scrollArea_8.setWidget(self.scrollAreaWidgetContents_8)
        self.stackedWidget.addWidget(self.page_8)


        self.page_9 = QWidget()
        self.scrollArea_9 = QScrollArea(self.page_9)
        self.scrollArea_9.setGeometry(QRect(0, 6, 256, 430))
        self.scrollArea_9.setWidgetResizable(True)
        self.scrollAreaWidgetContents_9 = QWidget()
        self.scrollAreaWidgetContents_9.setGeometry(QRect(0, 0, 271, 64))
        self.scrollAreaWidgetContents_9.setSizePolicy(sizePolicy)
        self.scrollAreaWidgetContents_9.setFont(QFont('微软雅黑', 10))
        self.verticalLayout_9 = QVBoxLayout(self.scrollAreaWidgetContents_9)
        self.verticalLayout_9.setObjectName('verticalLayout_9')
        self.verticalLayout_9.setContentsMargins(0, 0, 5, 0)
        self.scrollArea_9.setWidget(self.scrollAreaWidgetContents_9)
        self.stackedWidget.addWidget(self.page_9)


        self.page_10 = QWidget()
        self.scrollArea_10 = QScrollArea(self.page_10)
        self.scrollArea_10.setGeometry(QRect(0, 6, 256, 430))
        self.scrollArea_10.setWidgetResizable(True)
        self.scrollAreaWidgetContents_10 = QWidget()
        self.scrollAreaWidgetContents_10.setGeometry(QRect(0, 0, 271, 64))
        self.scrollAreaWidgetContents_10.setSizePolicy(sizePolicy)
        self.scrollAreaWidgetContents_10.setFont(QFont('微软雅黑', 10))
        self.verticalLayout_10 = QVBoxLayout(self.scrollAreaWidgetContents_10)
        self.verticalLayout_10.setObjectName('verticalLayout_10')
        self.verticalLayout_10.setContentsMargins(0, 0, 5, 0)
        self.scrollArea_10.setWidget(self.scrollAreaWidgetContents_10)
        self.stackedWidget.addWidget(self.page_10)


        self.page_11 = QWidget()
        self.scrollArea_11 = QScrollArea(self.page_11)
        self.scrollArea_11.setGeometry(QRect(0, 6, 256, 430))
        self.scrollArea_11.setWidgetResizable(True)
        self.scrollAreaWidgetContents_11 = QWidget()
        self.scrollAreaWidgetContents_11.setGeometry(QRect(0, 0, 271, 64))
        self.scrollAreaWidgetContents_11.setSizePolicy(sizePolicy)
        self.scrollAreaWidgetContents_11.setFont(QFont('微软雅黑', 10))
        self.verticalLayout_11 = QVBoxLayout(self.scrollAreaWidgetContents_11)
        self.verticalLayout_11.setObjectName('verticalLayout_11')
        self.verticalLayout_11.setContentsMargins(0, 0, 5, 0)
        self.scrollArea_11.setWidget(self.scrollAreaWidgetContents_11)
        self.stackedWidget.addWidget(self.page_11)


        self.page_12 = QWidget()
        self.scrollArea_12 = QScrollArea(self.page_12)
        self.scrollArea_12.setGeometry(QRect(0, 6, 256, 430))
        self.scrollArea_12.setWidgetResizable(True)
        self.scrollAreaWidgetContents_12 = QWidget()
        self.scrollAreaWidgetContents_12.setGeometry(QRect(0, 0, 271, 64))
        self.scrollAreaWidgetContents_12.setSizePolicy(sizePolicy)
        self.scrollAreaWidgetContents_12.setFont(QFont('微软雅黑', 10))
        self.verticalLayout_12 = QVBoxLayout(self.scrollAreaWidgetContents_12)
        self.verticalLayout_12.setObjectName('verticalLayout_12')
        self.verticalLayout_12.setContentsMargins(0, 0, 5, 0)
        self.scrollArea_12.setWidget(self.scrollAreaWidgetContents_12)
        self.stackedWidget.addWidget(self.page_12)


        self.page_13 = QWidget()
        self.scrollArea_13 = QScrollArea(self.page_13)
        self.scrollArea_13.setGeometry(QRect(0, 6, 256, 430))
        self.scrollArea_13.setWidgetResizable(True)
        self.scrollAreaWidgetContents_13 = QWidget()
        self.scrollAreaWidgetContents_13.setGeometry(QRect(0, 0, 271, 64))
        self.scrollAreaWidgetContents_13.setSizePolicy(sizePolicy)
        self.scrollAreaWidgetContents_13.setFont(QFont('微软雅黑', 10))
        self.verticalLayout_13 = QVBoxLayout(self.scrollAreaWidgetContents_13)
        self.verticalLayout_13.setObjectName('verticalLayout_13')
        self.verticalLayout_13.setContentsMargins(0, 0, 5, 0)
        self.scrollArea_13.setWidget(self.scrollAreaWidgetContents_13)
        self.stackedWidget.addWidget(self.page_13)


        self.page_14 = QWidget()
        self.scrollArea_14 = QScrollArea(self.page_14)
        self.scrollArea_14.setGeometry(QRect(0, 6, 256, 430))
        self.scrollArea_14.setWidgetResizable(True)
        self.scrollAreaWidgetContents_14 = QWidget()
        self.scrollAreaWidgetContents_14.setGeometry(QRect(0, 0, 271, 64))
        self.scrollAreaWidgetContents_14.setSizePolicy(sizePolicy)
        self.scrollAreaWidgetContents_14.setFont(QFont('微软雅黑', 10))
        self.verticalLayout_14 = QVBoxLayout(self.scrollAreaWidgetContents_14)
        self.verticalLayout_14.setObjectName('verticalLayout_14')
        self.verticalLayout_14.setContentsMargins(0, 0, 5, 0)
        self.scrollArea_14.setWidget(self.scrollAreaWidgetContents_14)
        self.stackedWidget.addWidget(self.page_14)


        self.page_15 = QWidget()
        self.scrollArea_15 = QScrollArea(self.page_15)
        self.scrollArea_15.setGeometry(QRect(0, 6, 256, 430))
        self.scrollArea_15.setWidgetResizable(True)
        self.scrollAreaWidgetContents_15 = QWidget()
        self.scrollAreaWidgetContents_15.setGeometry(QRect(0, 0, 271, 64))
        self.scrollAreaWidgetContents_15.setSizePolicy(sizePolicy)
        self.scrollAreaWidgetContents_15.setFont(QFont('微软雅黑', 10))
        self.verticalLayout_15 = QVBoxLayout(self.scrollAreaWidgetContents_15)
        self.verticalLayout_15.setObjectName('verticalLayout_15')
        self.verticalLayout_15.setContentsMargins(0, 0, 5, 0)
        self.scrollArea_15.setWidget(self.scrollAreaWidgetContents_15)
        self.stackedWidget.addWidget(self.page_15)


        self.page_16 = QWidget()
        self.scrollArea_16 = QScrollArea(self.page_16)
        self.scrollArea_16.setGeometry(QRect(0, 6, 256, 430))
        self.scrollArea_16.setWidgetResizable(True)
        self.scrollAreaWidgetContents_16 = QWidget()
        self.scrollAreaWidgetContents_16.setGeometry(QRect(0, 0, 271, 64))
        self.scrollAreaWidgetContents_16.setSizePolicy(sizePolicy)
        self.scrollAreaWidgetContents_16.setFont(QFont('微软雅黑', 10))
        self.verticalLayout_16 = QVBoxLayout(self.scrollAreaWidgetContents_16)
        self.verticalLayout_16.setObjectName('verticalLayout_16')
        self.verticalLayout_16.setContentsMargins(0, 0, 5, 0)
        self.scrollArea_16.setWidget(self.scrollAreaWidgetContents_16)
        self.stackedWidget.addWidget(self.page_16)

        self.stackedWidget.setCurrentIndex(0)
        self.button_l1.clicked.connect(self.display_page1)
            
        self.button_l2.clicked.connect(self.display_page2)
            
        self.button_l3.clicked.connect(self.display_page3)
            
        self.button_l4.clicked.connect(self.display_page4)
            
        self.button_l5.clicked.connect(self.display_page5)
            
        self.button_l6.clicked.connect(self.display_page6)
            
        self.button_l7.clicked.connect(self.display_page7)
            
        self.button_l8.clicked.connect(self.display_page8)
            
        self.button_l9.clicked.connect(self.display_page9)
            
        self.button_l10.clicked.connect(self.display_page10)
            
        self.button_l11.clicked.connect(self.display_page11)
            
        self.button_l12.clicked.connect(self.display_page12)
            
        self.button_l13.clicked.connect(self.display_page13)
            
        self.button_l14.clicked.connect(self.display_page14)
            
        self.button_l15.clicked.connect(self.display_page15)
            
        self.button_l16.clicked.connect(self.display_page16)
            
    def display_page1(self):
        self.stackedWidget.setCurrentIndex(1-1)
            
    def display_page2(self):
        self.stackedWidget.setCurrentIndex(2-1)
            
    def display_page3(self):
        self.stackedWidget.setCurrentIndex(3-1)
            
    def display_page4(self):
        self.stackedWidget.setCurrentIndex(4-1)
            
    def display_page5(self):
        self.stackedWidget.setCurrentIndex(5-1)
            
    def display_page6(self):
        self.stackedWidget.setCurrentIndex(6-1)
            
    def display_page7(self):
        self.stackedWidget.setCurrentIndex(7-1)
            
    def display_page8(self):
        self.stackedWidget.setCurrentIndex(8-1)
            
    def display_page9(self):
        self.stackedWidget.setCurrentIndex(9-1)
            
    def display_page10(self):
        self.stackedWidget.setCurrentIndex(10-1)
            
    def display_page11(self):
        self.stackedWidget.setCurrentIndex(11-1)
            
    def display_page12(self):
        self.stackedWidget.setCurrentIndex(12-1)
            
    def display_page13(self):
        self.stackedWidget.setCurrentIndex(13-1)
            
    def display_page14(self):
        self.stackedWidget.setCurrentIndex(14-1)
            
    def display_page15(self):
        self.stackedWidget.setCurrentIndex(15-1)
            
    def display_page16(self):
        self.stackedWidget.setCurrentIndex(16-1)
            
if __name__ == "__main__":
    app = QApplication(sys.argv)
    main_window = pages_window()
    main_window.show()
    exit(app.exec_())
            