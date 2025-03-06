import sys
from PyQt6.QtCore import (
    Qt,
)
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


class RegistrationWindow(QWidget):
    def __init__(self):
        super().__init__()

        # self.setGeometry(0, 0, 640, 640)
        self.setFixedSize(640, 640)
        self.setWindowTitle("Week 2 : Layout - User Registration Form")

        self.__init_ui()

    def __init_ui(self):
        root_layout = QVBoxLayout()
        root_layout.setContentsMargins(16, 16, 16, 16)
        root_layout.setSpacing(8)

        id_frame = QFrame()
        id_frame.setFrameShape(QFrame.Shape.Box)
        id_frame.setFrameShadow(QFrame.Shadow.Raised)
        id_layout = QVBoxLayout()
        id_layout.setContentsMargins(16, 24, 16, 24)
        id_layout.setSpacing(16)
        id_layout.addWidget(QLabel("Nama : Dzakanov Inshoofi"))
        id_layout.addWidget(QLabel("Nim : F1D02310110"))
        id_layout.addWidget(QLabel("Kelas : C"))
        id_frame.setLayout(id_layout)

        nv_frame = QFrame()
        nv_frame.setFrameShape(QFrame.Shape.Box)
        nv_frame.setFrameShadow(QFrame.Shadow.Raised)
        nv_layout = QHBoxLayout()
        nv_layout.setContentsMargins(16, 16, 16, 16)
        nv_layout.setSpacing(16)
        nv_layout.addWidget(QPushButton("Home"))
        nv_layout.addWidget(QPushButton("About"))
        nv_layout.addWidget(QPushButton("Contact"))
        nv_frame.setLayout(nv_layout)

        ur_frame = QFrame()
        ur_frame.setFrameShape(QFrame.Shape.Box)
        ur_frame.setFrameShadow(QFrame.Shadow.Raised)
        ur_layout = QFormLayout()
        ur_layout.setContentsMargins(196, 16, 196, 16)
        ur_layout.setSpacing(16)
        ur_layout.setFormAlignment(Qt.AlignmentFlag.AlignHCenter)
        ur_layout.setLabelAlignment(Qt.AlignmentFlag.AlignRight)
        ur_layout.addRow(QLabel("Full Name:"), QLineEdit())
        ur_layout.addRow(QLabel("Email:"), QLineEdit())
        ur_layout.addRow(QLabel("Phone:"), QLineEdit())

        sex_layout = QHBoxLayout()
        sex_layout.addWidget(QRadioButton("Male"))
        sex_layout.addWidget(QRadioButton("Female"))

        ur_layout.addRow(QLabel("Gender:"), sex_layout)

        country_selector = QComboBox()
        country_selector.setEditable(True)

        country_selector.addItems([
            "Canada", "Germany", "India", "China", "Japan", "Brazil", "Mexico"
        ])

        country_selector.setCurrentIndex(-1)

        ur_layout.addRow(QLabel("Country:"), country_selector)
        ur_frame.setLayout(ur_layout)

        ac_frame = QFrame()
        ac_frame.setFrameShape(QFrame.Shape.Box)
        ac_frame.setFrameShadow(QFrame.Shadow.Raised)
        ac_layout = QHBoxLayout()
        ac_layout.setContentsMargins(16, 16, 16, 16)
        ac_layout.setSpacing(16)
        ac_layout.addWidget(QPushButton("Submit"))
        ac_layout.addWidget(QPushButton("Cancel"))
        ac_frame.setLayout(ac_layout)

        root_layout.addWidget(QLabel("Identitas"))
        root_layout.addWidget(id_frame)
        root_layout.addWidget(QLabel("Navigation"))
        root_layout.addWidget(nv_frame)
        root_layout.addWidget(QLabel("User Registration"))
        root_layout.addWidget(ur_frame, 8)
        root_layout.addWidget(QLabel("Actions"))
        root_layout.addWidget(ac_frame)
        self.setLayout(root_layout)


if __name__ == "__main__":
    app = QApplication(sys.argv)

    window = RegistrationWindow()
    window.show()

    sys.exit(app.exec())
