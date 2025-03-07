import sys
from PyQt6.QtCore import Qt
from PyQt6.QtWidgets import (
    QApplication,
    QWidget,
    QFormLayout,
    QVBoxLayout,
    QHBoxLayout,
    QFrame,
    QLineEdit,
    QComboBox,
    QRadioButton,
    QPushButton,
    QLabel,
)
from qt_material import apply_stylesheet


class RegistrationWindow(QWidget):
    def __init__(self):
        super().__init__()

        self.setGeometry(0, 0, 640, 640)
        # self.setFixedSize(640, 640)
        self.setWindowTitle("Week 2 : Layout - User Registration Form")

        self.__init_ui()

    def __init_ui(self):
        root_layout = QVBoxLayout()
        root_layout.setContentsMargins(16, 16, 16, 16)
        root_layout.setSpacing(8)

        id_frame = self.__create_frame()
        id_frame.setLayout(self.__get_identity_layout())

        nv_frame = self.__create_frame()
        nv_frame.setLayout(self.__get_navigation_layout())

        ur_frame = self.__create_frame()
        ur_frame.setLayout(self.__get_user_registration_layout())

        ac_frame = self.__create_frame()
        ac_frame.setLayout(self.__get_actions_layout())

        root_layout.addWidget(QLabel("Identitas"))
        root_layout.addWidget(id_frame)
        root_layout.addWidget(QLabel("Navigation"))
        root_layout.addWidget(nv_frame)
        root_layout.addWidget(QLabel("User Registration"))
        root_layout.addWidget(ur_frame, 8)
        root_layout.addWidget(QLabel("Actions"))
        root_layout.addWidget(ac_frame)
        self.setLayout(root_layout)

    def __create_frame(self) -> QFrame:
        frame = QFrame()
        frame.setFrameShape(QFrame.Shape.Box)
        frame.setFrameShadow(QFrame.Shadow.Raised)
        return frame

    def __get_identity_layout(self) -> QVBoxLayout:
        layout = QVBoxLayout()
        layout.setContentsMargins(16, 24, 16, 24)
        layout.setSpacing(16)
        layout.addWidget(QLabel("Nama : Dzakanov Inshoofi"))
        layout.addWidget(QLabel("Nim : F1D02310110"))
        layout.addWidget(QLabel("Kelas : C"))
        return layout

    def __get_navigation_layout(self) -> QHBoxLayout:
        layout = QHBoxLayout()
        layout.setContentsMargins(16, 16, 16, 16)
        layout.setSpacing(16)
        layout.addWidget(QPushButton("Home"))
        layout.addWidget(QPushButton("About"))
        layout.addWidget(QPushButton("Contact"))
        return layout

    def __get_user_registration_layout(self) -> QFormLayout:
        layout = QFormLayout()
        layout.setContentsMargins(178, 16, 178, 16)
        layout.setSpacing(16)
        layout.setFormAlignment(Qt.AlignmentFlag.AlignHCenter)
        layout.setLabelAlignment(Qt.AlignmentFlag.AlignRight)
        layout.addRow(QLabel("Full Name:"), QLineEdit())
        layout.addRow(QLabel("Email:"), QLineEdit())
        layout.addRow(QLabel("Phone:"), QLineEdit())

        gender_layout = QHBoxLayout()
        gender_layout.addWidget(QRadioButton("Male"))
        gender_layout.addWidget(QRadioButton("Female"))

        layout.addRow(QLabel("Gender:"), gender_layout)

        country_selector = QComboBox()
        country_selector.setEditable(True)

        country_selector.addItems([
            "Canada", "Germany", "India", "China", "Japan", "Brazil", "Mexico"
        ])

        country_selector.setCurrentIndex(-1)

        layout.addRow(QLabel("Country:"), country_selector)
        return layout

    def __get_actions_layout(self) -> QHBoxLayout:
        layout = QHBoxLayout()
        layout.setContentsMargins(16, 16, 16, 16)
        layout.setSpacing(16)
        layout.addWidget(QPushButton("Submit"))
        layout.addWidget(QPushButton("Cancel"))
        return layout


if __name__ == "__main__":
    app = QApplication(sys.argv)
    apply_stylesheet(app, "light_amber.xml")

    window = RegistrationWindow()
    window.show()

    sys.exit(app.exec())
