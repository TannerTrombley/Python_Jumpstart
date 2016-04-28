import datetime
import subprocess as sub_proc

class Entry:
    """
    The Entry class contains the date that the entry was created  and the name of the file that contains the text
    """
    def __init__(self, file_name, path):
        self.created = datetime.datetime.today()
        self.file = file_name
        self.file_path = path

    def open(self):
        sub_proc.Popen(["gedit", self.file_path])

    def __str__(self):
        return self.file_name + str(self.created)