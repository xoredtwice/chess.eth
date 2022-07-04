from PyQt5.QtWidgets import QApplication
from src.client.view.table_view import TableView
import sys

def run_chess_client(root_path, conf):
    app = QApplication(sys.argv)


    receipts = None
    # creating a window object
    main = TableView(conf, receipts)

    # showing the window
    main.show()

    # loop
    sys.exit(app.exec_())