import os
import xml.etree.ElementTree as ET



class LogParser:
    @staticmethod
    def ids_by_message(xml, message):
        root = ET.fromstring(""""<?xml.etree.ElementTree version="1.0" encoding="UTF-8"?>
<log>
    <entry id="1">
        <message>Application started</message>
    </entry>
    <entry id="2">
        <message>Application ended</message>
    </entry>
</log>)"""
        print(root)
        lst = {}
        for child in root:
            if child.tag == 'entry':
                for msg in child:
                    lst[int(child.attrib)] = msg.text

        for key in lst.keys():
            if message == lst[key]:
                return [key]


xml = """"<?xml.etree.ElementTree version="1.0" encoding="UTF-8"?>
<log>
    <entry id="1">
        <message>Application started</message>
    </entry>
    <entry id="2">
        <message>Application ended</message>
    </entry>
</log>"""
print(LogParser.ids_by_message(xml, 'Application ended'))