from PyQt5.QtWidgets import (QApplication, 
                             QWidget, 
                             QStackedWidget, 
                             QLabel, 
                             QVBoxLayout,
                             QHBoxLayout, 
                             QPushButton, 
                             QTableWidget, 
                             QTableWidgetItem, 
                             QHeaderView)

from PyQt5.QtWidgets import QStyledItemDelegate
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QColor, QIcon
import fastf1
from fastf1.ergast import Ergast
from datetime import datetime, timezone

#cache data
fastf1.Cache.enable_cache("cache")

class CenterDelegate(QStyledItemDelegate):
    def initStyleOption(self, option, index):
        super().initStyleOption(option, index)
        option.displayAlignment = Qt.AlignCenter

class f1_app(QWidget):
    def __init__(self):
        super().__init__()

        # Main Driver (QStackedWidget)
        self.stack = QStackedWidget()
        self.main_layout = QVBoxLayout()

        #Pages
        self.home = QWidget()
        self.schedule = QWidget()
        self.constructors = QWidget()
        self.drivers = QWidget()

        self.initUI()

    def initUI(self):

        # Main Window
        self.setWindowTitle("F1 App")
        self.resize(500, 500)

        # Main Driver (QStackedWidget) Page
        self.stack.addWidget(self.home)
        self.stack.addWidget(self.schedule)
        self.stack.addWidget(self.constructors)
        self.stack.addWidget(self.drivers)

        self.main_layout.addWidget(self.stack)
        self.main_layout.setContentsMargins(0, 0, 0, 0)
        self.main_layout.setSpacing(0)

        self.setLayout(self.main_layout)

        #start with home
        self.home_func()

        self.setStyleSheet("""
        /* Home */      
        
            QWidget {
                background-color: #15151E;
            }

            QPushButton {
                color: #15151E;
                font-weight: bold;
                background-color: #FF1E00;
            }
                           
            QPushButton:hover {
                background-color: #ff3d1f;
            }

            QLabel {
                color: white;
                padding: 5px;
            }
               
            #next_session_title{
                    font-size: 20px;
            }
                                
            #next_session{
                    font-size: 25px;     
            }
                                
            #welcome{
                    font-size: 40px;
                    font-weight: bold;
                    background-color: #FF1E00;
            }
                                
            #previous_race_title{
                    font-size: 20px;
            }
                                
            #previous_race{
                    font-size: 25px;
            }
                                
            #first_podium{
                    font-size: 15px;
            }
                                
            #second_podium{
                    font-size: 15px;
            }
                                
            #third_podium{
                    font-size: 15px;
            }
                                
            #next_race_title{
                    font-size: 20px;
            }
                                
            #next_race{
                    font-size: 25px;
            }
            
            #circuit{
                    font-size: 15px;
            }
                                
            #schedule_button{
                    font-size: 17px;
            }
                                
            #constructor_leader_title{
                    font-size: 20px;
            }
                                
            #constructor_leader_name{
                    font-size: 25px;
            }
                                
            #constructor_button{
                    font-size: 17px;
            }  
                                      
            #driver_leader_title{
                    font-size: 20px;
            }  
                                
            #driver_leader_name{
                    font-size: 25px;
            }  
                                          
            #driver_button{
                    font-size: 17px;
            }

                           
        /* Schedule */
            
            QTableWidget{
                background-color: #1e1e1e;
                alternate-background-color: #252525;
                color: #e0e0e0;
                gridline-color: #444;
                font-size: 14px;
                selection-background-color: #444;
                selection-color: white;
            }

            QHeaderView::section{
                background-color: #333;
                color: white;
                padding: 6px;
                border: 1px solid #444;
                font-weight: bold;
            }

            QTableCornerButton::section{
                background-color: #333;
                border: 1px solid #444;
            }
                                
        """)

    


    def home_func(self):
        
        self.home.setObjectName("home")

        #next session field
        next_session_title = QLabel("Next Session:")
        next_session_title.setObjectName("next_session_title")
        next_session = QLabel("Australia FP1")
        next_session.setObjectName("next_session")

        welcome = QLabel("Welcome")
        welcome.setObjectName("welcome")

        previous_race_title = QLabel("Previous Race:")
        previous_race_title.setObjectName("previous_race_title")
        previous_race = QLabel("Abu Dhabi")
        previous_race.setObjectName("previous_race")
        next_race_title = QLabel("Next Race:")
        next_race_title.setObjectName("next_race_title")
        next_race = QLabel("Australia")
        next_race.setObjectName("next_race")
        circuit = QLabel("Albert Park Circuit")
        circuit.setObjectName("circuit")

        first_podium = QLabel("1. VER")
        first_podium.setObjectName("first_podium")
        second_podium = QLabel("2. PIA")
        second_podium.setObjectName("second_podium")
        third_podium = QLabel("3. NOR")
        third_podium.setObjectName("third_podium")

        schedule_button = QPushButton("See Full Schedule")
        schedule_button.setObjectName("schedule_button")

        constructor_leader_title = QLabel("Current Constuctor's Leader:")
        constructor_leader_title.setObjectName("constructor_leader_title")
        constructor_leader_name = QLabel("McLaren")
        constructor_leader_name.setObjectName("constructor_leader_name")
        constructor_button = QPushButton("See Constructor's Standings")
        constructor_button.setObjectName("constructor_button")

        driver_leader_title = QLabel("Current Driver's Leader:")
        driver_leader_title.setObjectName("driver_leader_title")
        driver_leader_name = QLabel("Lando Norris")
        driver_leader_name.setObjectName("driver_leader_name")
        driver_button = QPushButton("See Driver's Standings")
        driver_button.setObjectName("driver_button")

        previous_race_layout = QHBoxLayout()
        previous_race_layout.addWidget(previous_race)
        previous_race_layout.addStretch()
        previous_race_layout.addWidget(first_podium)
        previous_race_layout.addWidget(second_podium)
        previous_race_layout.addWidget(third_podium)
        previous_race_layout.setSpacing(10)

        next_race_layout = QHBoxLayout()
        next_race_layout.addWidget(next_race)
        next_race_layout.addStretch()
        next_race_layout.addWidget(circuit)

        home_layout = QVBoxLayout()

        home_widgets = [next_session_title, next_session, welcome, previous_race_title, previous_race_layout, next_race_title, 
                        next_race_layout, schedule_button, constructor_leader_title, constructor_leader_name, constructor_button, 
                        driver_leader_title, driver_leader_name, driver_button]
        special_widgets = [previous_race, first_podium, second_podium, third_podium, next_race, circuit]
        
        for home_widget in home_widgets:
            if home_widget == previous_race_layout:
                home_layout.addLayout(previous_race_layout)
            elif home_widget == next_race_layout:
                home_layout.addLayout(next_race_layout)
            else:
                home_layout.addWidget(home_widget)
        
        home_layout.setContentsMargins(0, 0, 0, 0)
        home_layout.setSpacing(0)

        #initilize home
        self.home.setLayout(home_layout)
        self.home_backend(home_widgets, special_widgets)

    def home_backend(self, home_widgets, special_widgets):

        home_widgets[7].clicked.connect(lambda: (self.stack.setCurrentIndex(1), self.schedule_func()))
        home_widgets[10].clicked.connect(lambda: (self.stack.setCurrentIndex(2), self.constructors_func()))
        home_widgets[13].clicked.connect(lambda: (self.stack.setCurrentIndex(3), self.drivers_func()))


        # get current schedule and time
        year = datetime.now().year
        schedule = fastf1.get_event_schedule(year)
        now = datetime.now(timezone.utc)

        # set up variables
        next_session = None
        next_race = None
        previous_race = None

        # check through each row
        for _, event in schedule.iterrows():

            for session_key in ["Session1Date", "Session2Date", "Session3Date",
                                "Session4Date", "Session5Date"]:
                session_time = event.get(session_key)

                #as soon as we reach a session ahead of our current time...
                if isinstance(session_time, datetime) and session_time > now:

                        # TESTING WEEKEND
                        if event["EventFormat"] == "testing":
                                if session_key == "Session1Date":
                                        session_name = "Testing Day 1"
                                elif session_key == "Session2Date":
                                        session_name = "Testing Day 2"
                                elif session_key == "Session3Date":
                                        session_name = "Testing Day 3"
                                elif session_key == "Session4Date":
                                        session_name = "Testing Day 4"
                                elif session_key == "Session5Date":
                                        session_name = "Testing Day 5"

                        # SPRINT WEEKEND
                        elif event["EventFormat"] == "sprint":
                                if session_key == "Session1Date":
                                        session_name = "FP1"
                                elif session_key == "Session2Date":
                                        session_name = "Qualifying"
                                elif session_key == "Session3Date":
                                        session_name = "Sprint Shootout"
                                elif session_key == "Session4Date":
                                        session_name = "Sprint"
                                elif session_key == "Session5Date":
                                       session_name = "Race"

                        # NORMAL WEEKEND
                        else:
                                if session_key == "Session1Date":
                                        session_name = "FP1"
                                elif session_key == "Session2Date":
                                        session_name = "FP2"
                                elif session_key == "Session3Date":
                                        session_name = "FP3"
                                elif session_key == "Session4Date":
                                        session_name = "Qualifying"
                                elif session_key == "Session5Date":
                                        session_name = "Race"

                        next_session = (event["EventName"], session_name)
                        break
            
            if next_session:
                break
            
        for _, event in schedule.iterrows():

                race_time = event.get("Session5Date")

                if isinstance(race_time, datetime):

                        if race_time < now:
                                previous_race = event["EventName"]
                                session = event.get_session("R")
                                session.load(telemetry=False)

                        elif race_time > now and next_race is None:
                                next_race = event["EventName"]
                                circuit = event["Location"]


                if previous_race == None:
                        last_schedule = fastf1.get_event_schedule(year - 1)
                        previous_race = last_schedule.iloc[-1]["EventName"]

                if previous_race is not None and next_race is not None:
                        break
        
        if next_session and next_race and previous_race and circuit:
            podium_abbr = session.results['Abbreviation'].head(3).tolist()

            home_widgets[1].setText(f"{next_session[0]} {next_session[1]}")
            special_widgets[0].setText(previous_race)
            special_widgets[1].setText(f"1. {podium_abbr[0]}")
            special_widgets[2].setText(f"2. {podium_abbr[1]}")
            special_widgets[3].setText(f"3. {podium_abbr[2]}")
            special_widgets[4].setText(next_race)
            special_widgets[5].setText(circuit)

        #constructors + drivers
        
        ergast = Ergast()
        resp = ergast.get_driver_standings(year)
        resp2 = ergast.get_constructor_standings(year)

        if not resp.content:
                driver = "Unavailable"
        else:
                leader = resp.content[0]
                driver = f"{leader.givenName[0]} {leader.familyName[0]} - {leader.constructorNames[0][0]}"

        if not resp2.content:
                constructor = "Unavailable"
        else:
                constructor_leader = resp2.content[0]
                constructor = f"{constructor_leader.constructorName[0]}"

        home_widgets[9].setText(constructor)
        home_widgets[12].setText(driver)
        
    def schedule_func(self): 

        self.schedule.setObjectName("schedule")

        table = QTableWidget()
        back_home = QPushButton("Home")

        schedule_layout = QVBoxLayout()
        schedule_layout.addWidget(table)
        schedule_layout.addWidget(back_home)

        self.schedule.setLayout(schedule_layout)

        self.schedule_backend(table, back_home)

    def schedule_backend(self, table, back_home):

        season = fastf1.get_event_schedule(datetime.now().year)
        headers = ["Grand Prix", "Date", "Location", "Winner"]

        table.setEditTriggers(QTableWidget.NoEditTriggers)
        table.setItemDelegate(CenterDelegate(table))
        table.setColumnCount(len(headers))
        table.setHorizontalHeaderLabels(headers)
        table.setRowCount(len(season))

        for row, event in season.iterrows():

                winner = "N/A"

                if event["EventDate"].date() < datetime.now().date():

                        try:
                                ergast = Ergast()
                                result = ergast.get_race_results(event["EventDate"].strftime("%Y"), event["RoundNumber"])
                                df = result.content[0]

                                winner = df.iloc[0]          
                                winner = winner['driverCode']  


                        except Exception:
                                winner = "N/A"

                data = [
                        event["EventName"],
                        event["EventDate"].strftime("%Y-%m-%d"),
                        event["Location"],
                        winner
                        ]
                
                for col, value in enumerate(data):
                    item = QTableWidgetItem(str(value))
                    item.setTextAlignment(Qt.AlignCenter)
                    table.setItem(row, col, item)

                if event["EventDate"].date() < datetime.now().date():
                        for col in range(table.columnCount()):
                                        table.item(row, col).setBackground(QColor("#BA2916"))

        # Stretch column
        header = table.horizontalHeader()
        header.setSectionResizeMode(QHeaderView.Stretch)
        
        # Hide row numbers
        table.verticalHeader().setVisible(False)

        back_home.clicked.connect(lambda: (self.stack.setCurrentIndex(0), self.loading()))

    def constructors_func(self):

        self.constructors.setObjectName("constructors")

        table = QTableWidget()
        back_home = QPushButton("Home")

        constructors_layout = QVBoxLayout()
        constructors_layout.addWidget(table)
        constructors_layout.addWidget(back_home)

        self.constructors.setLayout(constructors_layout)

        self.constructors_backend(table, back_home)

    def constructors_backend(self, table, back_home):

        headers = ["Position", "Constructor", "Wins", "Points"]
        year = datetime.now().year
        ergast = Ergast(result_type='pandas')
        resp = ergast.get_constructor_standings(year)

        if not resp.content:
                constructors = None
        else:   
                constructors = resp.content[0]

        if constructors is not None and not constructors.empty:

                table.setEditTriggers(QTableWidget.NoEditTriggers)
                table.setItemDelegate(CenterDelegate(table))
                table.setColumnCount(len(headers))
                table.setHorizontalHeaderLabels(headers)
                table.setRowCount(len(constructors))

                for row, constructor in constructors.iterrows():

                        data = [
                                        constructor.positionText,
                                        constructor.constructorName,
                                        constructor.wins,
                                        constructor.points,
                                ]

                        for col, value in enumerate(data):
                                item = QTableWidgetItem(str(value))
                                item.setTextAlignment(Qt.AlignCenter)
                                table.setItem(row, col, item)

                # Stretch column
                header = table.horizontalHeader()
                header.setSectionResizeMode(QHeaderView.Stretch)
                
                # Hide row numbers
                table.verticalHeader().setVisible(False)

        else:
            # No constructor data available
            pass

        back_home.clicked.connect(lambda: (self.stack.setCurrentIndex(0), self.loading()))

    def drivers_func(self):
        self.drivers.setObjectName("drivers")

        table = QTableWidget()
        back_home = QPushButton("Home")

        drivers_layout = QVBoxLayout()
        drivers_layout.addWidget(table)
        drivers_layout.addWidget(back_home)

        self.drivers.setLayout(drivers_layout)

        self.drivers_backend(table, back_home)
    
    def drivers_backend(self, table, back_home):

        headers = ["Position", "Driver", "Constructor", "Wins", "Points"]
        year = datetime.now().year
        ergast = Ergast(result_type='pandas')
        resp = ergast.get_driver_standings(year)

        if not resp.content:
                drivers = None
        else:   
                drivers = resp.content[0]

        if drivers is not None and not drivers.empty:

                table.setEditTriggers(QTableWidget.NoEditTriggers)
                table.setItemDelegate(CenterDelegate(table))
                table.setColumnCount(len(headers))
                table.setHorizontalHeaderLabels(headers)
                table.setRowCount(len(drivers))

                for row, driver in drivers.iterrows():

                        data = [
                                        driver.positionText,
                                        driver.familyName,
                                        driver.constructorNames[0],
                                        driver.wins,
                                        driver.points,
                                ]

                        for col, value in enumerate(data):
                                item = QTableWidgetItem(str(value))
                                item.setTextAlignment(Qt.AlignCenter)
                                table.setItem(row, col, item)

                # Stretch column
                header = table.horizontalHeader()
                header.setSectionResizeMode(QHeaderView.Stretch)
                
                # Hide row numbers
                table.verticalHeader().setVisible(False)

        else:
            # No constructor data available
            pass

        back_home.clicked.connect(lambda: (self.stack.setCurrentIndex(0), self.loading()))

    def loading(self):
        QApplication.processEvents()   
        self.home_func()

if __name__ == "__main__":
    app = QApplication([])
    window = f1_app()
    window.show()
    app.exec_()
