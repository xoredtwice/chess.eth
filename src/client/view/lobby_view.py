from PyQt5.QtWidgets import QDialog, QPushButton, QLineEdit
from PyQt5.QtWidgets import QHBoxLayout, QVBoxLayout
from PyQt5.QtGui import QIcon

from src.logger import lprint, lsection

# 
class LobbyView(QDialog):

    # constructor
    def __init__(self, parent=None):
        super(LobbyView, self).__init__(parent)

        self.setWindowTitle("Chess.eth Lobby")
        self.setMinimumSize(800, 800)
        
        self.refreshButton = QPushButton('Refresh')
        self.refreshButton.setFixedWidth(300)
        self.refreshButton.clicked.connect(self.onClicked_refresh)

        # Constructing the layout, adding the components
        main_layout = QVBoxLayout()

        # l2 is a Horizontal layout. Custom components are here
        h1_layout = QHBoxLayout()

        l2_v1_layout = QVBoxLayout()
        l2_v1_layout.addWidget(self.refreshButton)
        h1_layout.addLayout(l2_v1_layout)

        # l2_v2_layout = QVBoxLayout()
        # l2_v2_layout.addLayout(self.paper_edit_view)
        # l2_v2_layout.addLayout(self.bib_edit_view)
        # h1_layout.addLayout(l2_v2_layout)

        # l2_v3_layout = QVBoxLayout()
        # # l3_layout.addWidget(self.pdf_view)
        # l2_v3_layout.addLayout(self.graph_view)

        # l2_v3_layout.addLayout(self.opinion_edit_view)

        # h1_layout.addLayout(l2_v3_layout)

        # ----------------------------------------------------
        main_layout.addLayout(h1_layout)

        self.setLayout(main_layout)
    def onClicked_refresh(self):
        lprint("Not implemented")