from PyQt5.QtWidgets import QApplication
from src.view.table_view import TableView

def run_chess_client(conf, receipts):
    app = QApplication(sys.argv)

    # creating a window object
    main = TableView(conf, receipts)

    # showing the window
    main.show()

    # loop
    sys.exit(app.exec_())