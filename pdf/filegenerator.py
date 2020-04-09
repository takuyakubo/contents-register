from reportlab.pdfgen import canvas
from reportlab.pdfbase import pdfmetrics
from reportlab.lib.units import mm
from html.parser import HTMLParser
from .util import registor_fonts
import math

registor_fonts()

class PDFdata:
    def __init__(self):

        self.document_height = None
        self.document_width = None
        self.line_width = .5
        self.font_name = None
        self.font_size = None
        self.pdf_states = [['setLineWidth', [self.line_width]]]

    def setTitle(self, title):
        self.pdf_states.append(['setTitle', [title]])

    def setSubject(self, subject):
        self.pdf_states.append(['setSubject', [subject]])

    def setPageSize(self, width, height):
        if width == self.document_width and height == self.document_height:
            return
        self.pdf_states.append(['setPageSize', [(width, height)]])
        self.document_width = width
        self.document_height = height

    def setFont(self, font_name, font_size):
        if font_name == self.font_name and font_size == self.font_size:
            return
        self.pdf_states.append(['setFont', [font_name, font_size]])
        self.font_name = font_name
        self.font_size = font_size

    def drawString(self, pos_x, pos_y, text, align='l', rep_ratio=True, font_info=None):
        if font_info is not None:
            self.setFont(*font_info)
        pos_x_ = pos_x * self.document_width if rep_ratio else pos_x
        pos_y_ = pos_y * self.document_height if rep_ratio else pos_y
        if align == 'r':
            m_name = 'drawRightString'
        elif align == 'c':
            m_name = 'drawCentredString'
        elif align == 'l':
            m_name = 'drawString'
        else:
            raise Exception('align allows only "l", "r" or "c"')
        self.pdf_states.append([m_name, [pos_x_, pos_y_, text]])

    def drawLine(self, start_x, start_y, length, direction='h', rep_ratio=True, width_info=None):
        pos_x1 = start_x * self.document_width if rep_ratio else start_x
        pos_y1 = start_y * self.document_height if rep_ratio else start_y
        if direction == 'h':
            length_ = length * self.document_width if rep_ratio else length
            pos_x2 = pos_x1 + length_
            pos_y2 = pos_y1
        elif direction == 'v':
            length_ = length * self.document_height if rep_ratio else length
            pos_x2 = pos_x1
            pos_y2 = pos_y1 - length_
        else:
            raise Exception('direction allows only "h" or "v"')
        self.draw_line(pos_x1, pos_y1, pos_x2, pos_y2, width_info)

    def drawFreeLine(self, start_x, start_y, end_x, end_y, rep_ratio=True, width_info=None):
        pos_x1 = start_x * self.document_width if rep_ratio else start_x
        pos_y1 = start_y * self.document_height if rep_ratio else start_y
        pos_x2 = end_x * self.document_width if rep_ratio else end_x
        pos_y2 = end_y * self.document_height if rep_ratio else end_y
        self.draw_line(pos_x1, pos_y1, pos_x2, pos_y2, width_info)

    def draw_line(self, x1, y1, x2, y2, width_info):
        if width_info is not None:
            self.setLineWidth(width_info)
        self.pdf_states.append(['line', [x1, y1, x2, y2]])
    def setLineWidth(self, width):
        if width == self.line_width:
            return
        self.pdf_states.append(['setLineWidth', [width]])

    def export(self, filepath):
        pdfFile = canvas.Canvas(filepath)
        pdfFile.saveState()
        for prop in self.pdf_states:
            getattr(pdfFile, prop[0])(*prop[1])
        pdfFile.save()
