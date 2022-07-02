from PyQt5.QtWidgets import QDialog, QPushButton, QLineEdit
from PyQt5.QtWidgets import QHBoxLayout, QVBoxLayout, QLabel
from PyQt5.QtGui import QIcon
from PyQt5 import QtCore

from src.utils.logger import lprint, lsection

from src.pychess.chess_utils import load_game_state, parse_board, print_board

class TableView(QDialog):

    # constructor
    def __init__(self, parent=None):
        super(TableView, self).__init__(parent)

        self.setWindowTitle("Chess.eth Table View")
        self.setMinimumSize(800, 800)
        
        self.refreshButton = QPushButton('Refresh')
        self.refreshButton.setFixedWidth(300)
        self.refreshButton.setFixedHeight(100)
        self.refreshButton.clicked.connect(self.onClicked_refresh)

        self.squares = []
        # Constructing the layout, adding the components
        main_layout = QVBoxLayout()

        # l2 is a Horizontal layout. Custom components are here
        chessLayout = QHBoxLayout()
        xOffset = 10
        yOffset = 10
        sqSize = 50
        for i in range(8):
            file_layout = QVBoxLayout()
            for j in range(8):
                newSq = QLabel(' ')
                newSq.resize(sqSize, sqSize)
                newSq.move(xOffset + i * sqSize, yOffset + j * sqSize)
                newSq.setAlignment(QtCore.Qt.AlignCenter)
                if (i+j) % 2 == 0:
                    newSq.setStyleSheet("QLabel { background-color : purple; color : black; font-size: 40pt; }");
                else:
                    newSq.setStyleSheet("QLabel { background-color : white; color : black; font-size: 40pt;}");
                file_layout.addWidget(newSq)
                self.squares.append(newSq)
            chessLayout.addLayout(file_layout)

        l2_v1_layout = QVBoxLayout()
        l2_v1_layout.addWidget(self.refreshButton)

        # ----------------------------------------------------
        main_layout.addLayout(chessLayout)
        main_layout.addLayout(l2_v1_layout)

        self.setLayout(main_layout)
    def onClicked_refresh(self):
        turn, board64W, board64B, pieces256, engagements, visibility = load_game_state()
        pieces, view = parse_board(pieces256)
        for rank in range(8):
            for file in range(8):
                self.squares[file * 8 + (7-rank)].setText(view[rank][file])
        print_board(view)