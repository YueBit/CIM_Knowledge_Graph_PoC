import sys
import neo4j_playground
from turtle import onclick
from PyQt5.QtGui     import *
from PyQt5.QtCore    import *
from PyQt5.QtWidgets import *

class App(QWidget):
    
    def __init__(self):
        super().__init__()
        self.title = 'MKG System'
        self.left = 100
        self.top = 100
        self.width = 960
        self.height = 540
        self.initUI()
    
    def initUI(self):
        self.setWindowTitle(self.title)
        self.setGeometry(self.left, self.top, self.width, self.height)
        
        # Set banner
        label = QLabel(self)
        pixmap = QPixmap('./icons/banner.png')
        pixmap = pixmap.scaledToWidth(470)
        label.setPixmap(pixmap)
        
        # Set Lable of Entering Title
        self.label1 = QLabel(self)
        self.label1.move(40, 270)
        self.label1.setText("Enter Your Questions, Troubles, Faults on Manufacuring")
        # self.label1.setStyleSheet("font-weight: bold")
        
        # Create Textbox
        self.textbox1 = QTextEdit(self)
        self.textbox1.move(40, 300)
        self.textbox1.resize(400, 130)
        self.textbox1.setAlignment(Qt.AlignmentFlag.AlignTop)
        
        # Set the query button
        self.button1 = QPushButton("Find the anwser in MKG",self)
        # self.button1.setText("Find the anwser in MKG")
        self.button1.move(295, 450)
        self.button1.clicked.connect(self.on_click)
        
        # Set idle icon
        self.label2 = QLabel(self)
        pixmap = QPixmap('./icons/knowledge.png').scaledToWidth(100)
        self.label2.setPixmap(pixmap)
        self.label2.move(670, 100)
        self.label2.resize(100, 100)
        
        # Set the Label for "Do you know"?
        self.label_hint = QLabel(self)
        self.label_hint.move(680, 270)
        self.label_hint.setText("Do you know?")
        self.label_hint.setStyleSheet("font-weight: bold")
        
        # Set the Label for recomendation?
        self.label_recommendation = QLabel(self)
        self.label_recommendation.move(570, 300)
        self.label_recommendation.setText("VCATS is short for Vehicle Configuration and Test System.")
        
        # Set connection icon
        self.label_connection_icon = QLabel(self)
        pixmap = QPixmap('./icons/connection.png').scaledToWidth(15)
        self.label_connection_icon.setPixmap(pixmap)
        self.label_connection_icon.move(805, 520)
        self.label_connection_icon.resize(15, 15)
        
        # Set the Label for recomendation?
        self.label_connection_status = QLabel(self)
        self.label_connection_status.move(830, 520)
        self.label_connection_status.setText("Status: System Idle")
        self.label_connection_status.setStyleSheet("color:gray")
        
        # Set Background Color
        self.setStyleSheet("background-color: white;")
        
        # Set fixed size
        self.setFixedSize(960, 540)
        
        # Set cause icon label
        self.label_cause_icon = QLabel(self)
        
        # Set the label causes
        self.label_cause = QLabel(self)
        
        # Set the label causes
        self.label_cause_content = QTextEdit(self)
        self.label_cause_content.setStyleSheet("background-color:#a4b7ed")
        self.label_cause_content.setAlignment(Qt.AlignmentFlag.AlignTop)
        self.label_cause_content.hide()
        
        # Set solution icon label
        self.label_solution_icon = QLabel(self)
        
        # Set the label causes
        self.label_solution_title = QLabel(self)
        
        # Set the label solution contents
        self.label_solution_content = QTextEdit(self)
        self.label_solution_content.setStyleSheet("background-color:#a4b7ed")
        self.label_solution_content.setAlignment(Qt.AlignmentFlag.AlignTop)
        self.label_solution_content.hide()
        
        # Set loading icon label
        self.label_loading_icon = QLabel(self)
        
        # Set the "It fixes my problem" button
        self.button_fix = QPushButton("It fixes my problem",self)
        self.button_fix.move(540, 450)
        # self.button1.clicked.connect(self.on_click)
        self.button_fix.hide()
        
        # Set the "Next" button
        self.button_next = QPushButton("Show me the next",self)
        self.button_next.move(795, 450)
        # self.button1.clicked.connect(self.on_click)
        self.button_next.hide()
        
        # Set the "New Idea" button
        self.button_new_idea = QPushButton("Report new issue",self)
        self.button_new_idea.move(675, 450)
        # self.button1.clicked.connect(self.on_click)
        self.button_new_idea.hide()
        
        # Set icon
        self.setWindowIcon(QIcon('./icons/icon.png'))
        self.show()
        
    # Draw the middle line
    def paintEvent(self, event):
         painter1 = QPainter(self)
         painter1.setPen(Qt.gray)
         painter1.drawLine(480,10,480,500)
         painter1.end()
         
    # Query Button behavior
    def on_click(self):
        self.label2.clear()
        print(f"test text is {self.textbox1.toPlainText()}")
        # Clear recommendation
        self.label_recommendation.clear()
        self.label_hint.clear()
        # Update the label for the loading icon
        pixmap_loading = QPixmap('./icons/loading.png').scaledToWidth(80)
        self.label_loading_icon.setPixmap(pixmap_loading)
        self.label_loading_icon.move(670,255)
        self.label_loading_icon.resize(80,80)
        ### Connect to KG
        uri = "neo4j+s://6b5c5675.databases.neo4j.io"
        user = "neo4j"
        password = "4KxVG3iBCo8GPKfK91t1sAWZLJTIo8qjt75DbpZ7tRY"
        kg = neo4j_playground.Knowledge_gragh()
        connectStatus = kg.connect(uri, user, password)
        if connectStatus == 1:
            self.label_connection_status.setText("MKG Is Connected")
        else:
            self.label_connection_status.setText("MKG Not Connected")
            
        # Find cause
        problem_name = self.textbox1.toPlainText()
        cause = kg.find_cause(problem_name)
        print("+++")
        print(cause)
        
        # Set Lable3 for cause
        self.label_cause.move(650,70)
        self.label_cause.resize(300,20)
        self.label_cause.setText("Possible Causes Found in MKG")
        self.label_cause.setStyleSheet("font-weight: bold")
        # Update the label for the idea icon
        pixmap_cause = QPixmap('./icons/idea.png').scaledToWidth(30)
        self.label_cause_icon.setPixmap(pixmap_cause)
        self.label_cause_icon.move(610,60)
        self.label_cause_icon.resize(40,40)
        # Update the cause in the GUI
        self.label_loading_icon.hide()
        self.label_cause_content.show()
        self.label_cause_content.move(540, 110)
        self.label_cause_content.resize(365, 120)
        self.label_cause_content.setText("TDSRCS service is not active on the VCATS Server")
        # Update the label for the solution icon
        pixmap_solution = QPixmap('./icons/Repair.png').scaledToWidth(30)
        self.label_solution_icon.setPixmap(pixmap_solution)
        self.label_solution_icon.move(610,260)
        self.label_solution_icon.resize(40,40)
        # Set Lable for solution title
        self.label_solution_title.move(650,270)
        self.label_solution_title.resize(300,20)
        self.label_solution_title.setText("Suggested Solution by the MKG")
        self.label_solution_title.setStyleSheet("font-weight: bold")
        # Set the text box for the solution
        self.label_solution_content.show()
        self.label_solution_content.move(540, 300)
        self.label_solution_content.resize(365, 128)
        self.label_solution_content.setText("Restart TDSRCS server on the VCATS server")
        # Show the button
        self.button_fix.show()
        self.button_new_idea.show()
        self.button_next.show()
        
        ### Close the connection
        kg.close()
        
if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = App()
    sys.exit(app.exec_())