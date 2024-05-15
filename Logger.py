from os import getcwd, path
from datetime import datetime

class Logger:

    logFilePath = None
    messagesLogFilePath = None

    def __init__(self):
        
        rootPath = getcwd()
        self.logFilePath = path.join(rootPath, "logs", "error.log")
        self.messagesLogFilePath = path.join(rootPath, "logs", "message.log")
    
        if (path.isfile(self.logFilePath)):
            self.logFile = open(self.logFilePath, "a")
        else:
            self.logFile = open(self.logFilePath, "x")
            
        if (path.isfile(self.messagesLogFilePath)):
            self.messagesLogFile = open(self.messagesLogFilePath, "a")
        else:
            self.messagesLogFile = open(self.messagesLogFilePath, "x")

    def error(self, err):
        today = datetime.now()
        self.logFile.write("\n" + today.strftime("%Y-%m-%d %H:%M:%S") + " " + err)
        self.messagesLogFile.write("\nERROR: " + today.strftime("%Y-%m-%d %H:%M:%S") + " " + err)
        print("\nERROR: " + today.strftime("%Y-%m-%d %H:%M:%S") + " " + err)
        
    def message(self, message):
        today = datetime.now()
        self.messagesLogFile.write("\nMESSAGE: " + today.strftime("%Y-%m-%d %H:%M:%S") + " " + message)
        print("\nMESSAGE: " + today.strftime("%Y-%m-%d %H:%M:%S") + " " + message)