# PyQt5 Web Browser

This project demonstrates a simple web browser built using PyQt5. The browser supports basic features such as a navigation bar, URL loading, logging visited URLs with timestamps, and browser controls such as back, forward, reload, and return to home.

## Requirements

- Python 3.x
- PyQt5

You can install PyQt5 using pip:
```
pip install PyQt5 PyQtWebEngine
```

## Description

Here is a quick overview of what the main components in the code do:

- The Browser class defines the browser window and its components. It creates a QMainWindow instance with a QWebEngineView as the central widget, which will display the web pages.
- The address bar is a QLineEdit. When you press return in the address bar, it loads the URL entered.
- Navigation buttons (back, forward, reload, home) are QPushButton instances with associated icons.
- The URLs visited are logged in a file named "websites_{timestamp}.log", where the timestamp is when the program is launched.

## Usage

Clone this repository and run the script:
```
python Web-Browser.py
```

The script will launch a web browser window. You can use it to navigate the web. It starts with a home page (http://www.google.com by default). The address bar updates as you navigate. You can type a URL into the address bar to navigate directly to that page. Pressing the return key will initiate loading the URL.

The back, forward, and reload buttons work as you would expect. The home button returns you to the home page.

## Notes

- The script enables hardware acceleration using the QTWEBENGINE_CHROMIUM_FLAGS environment variable.
- The application logs all visited URLs with a timestamp into a log file.
- Remember to replace icon filenames with the paths of your actual icons. In this code, we have 'internet.png', 'back.png', 'forward.png', 'reload.png', and 'home.png' as placeholders.

## Screenshots

![Web Browser](https://i.imgur.com/J7PhiWk.png)

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
