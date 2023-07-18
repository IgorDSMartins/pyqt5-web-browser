import os
import sys
from PyQt5.QtCore import QUrl, QDateTime
from PyQt5.QtGui import QIcon, QFont
from PyQt5.QtWidgets import QApplication, QHBoxLayout, QLineEdit, QPushButton, QVBoxLayout, QWidget
from PyQt5.QtWebEngineWidgets import QWebEngineView


# Enable hardware acceleration
os.environ['QTWEBENGINE_CHROMIUM_FLAGS'] = '--enable-gpu-rasterization --enable-zero-copy'


class Browser(QWidget):
    def __init__(self):
        super().__init__()

        # Window settings
        self.setWindowTitle("Web Browser")
        self.setWindowIcon(QIcon('internet.png'))
        self.setGeometry(50, 50, 800, 600)

        # Home page
        self.home_url = "http://www.google.com"

        # Webview settings
        self.webview = QWebEngineView()
        self.webview.load(QUrl(self.home_url))
        self.webview.urlChanged.connect(self.update_address_bar)
        self.webview.loadFinished.connect(self.log_url)

        # Address bar settings
        self.address_bar = self.create_address_bar()
        self.address_bar.returnPressed.connect(self.load_url)

        # Navigation buttons
        self.back_button = self.create_nav_button("back.png", self.webview.back)
        self.forward_button = self.create_nav_button("forward.png", self.webview.forward)
        self.reload_button = self.create_nav_button("reload.png", self.webview.reload)  # Reload button
        self.home_button = self.create_nav_button("home.png", self.go_home)

        # Navigation bar layout
        self.nav_bar = QHBoxLayout()
        self.nav_bar.addWidget(self.back_button)
        self.nav_bar.addWidget(self.forward_button)
        self.nav_bar.addWidget(self.reload_button)  # Add the reload button to the navigation bar
        self.nav_bar.addWidget(self.home_button)
        self.nav_bar.addWidget(self.address_bar)
        self.nav_bar.setSpacing(0)
        self.nav_bar.setContentsMargins(0, 0, 0, 0)

        # Main layout
        self.layout = QVBoxLayout()
        self.layout.addLayout(self.nav_bar)
        self.layout.addWidget(self.webview)
        self.layout.setSpacing(0)
        self.layout.setContentsMargins(0, 0, 0, 0)

        self.setLayout(self.layout)

        self.log_file_name = f"websites_{QDateTime.currentDateTime().toString('yyyy-MM-dd_hh-mm-ss')}.log"

    def create_nav_button(self, icon, function):
        button = QPushButton()
        button.setIcon(QIcon(icon))
        button.setFixedSize(40, 40)
        button.clicked.connect(function)
        return button

    def create_address_bar(self):
        address_bar = QLineEdit()
        address_bar.setFixedHeight(40)
        font = QFont()
        font.setPointSize(18)
        address_bar.setFont(font)
        return address_bar

    def load_url(self):
        url = self.address_bar.text()
        if not url.startswith("http://") and not url.startswith("https://"):
            url = "http://" + url
        self.webview.load(QUrl(url))

    def update_address_bar(self, url):
        self.address_bar.setText(url.toString())

    def log_url(self):
        url = self.webview.url().toString()
        timestamp = QDateTime.currentDateTime().toString()
        log_entry = f"[{timestamp}] {url}\n"
        with open(self.log_file_name, "a") as log_file:
            log_file.write(log_entry)

    def go_home(self):
        self.webview.load(QUrl(self.home_url))


def main():
    app = QApplication(sys.argv)
    app.setWindowIcon(QIcon('internet.png'))

    browser = Browser()
    browser.show()

    app.lastWindowClosed.connect(app.quit)

    sys.exit(app.exec_())


if __name__ == "__main__":
    main()
