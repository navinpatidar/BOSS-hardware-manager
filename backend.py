import os
class hw_info_in_xml :
    def __init__(self):
        os.system("lshw -xml -numeric > ./resources/hw.xml")
