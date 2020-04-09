from reportlab.rl_config import TTFSearchPath
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.pdfbase import pdfmetrics


def registor_font(font_set_name, fonts_detail, FontsPath):
    TTFSearchPath.append(FontsPath + font_set_name)
    for f in fonts_detail:
        pdfmetrics.registerFont(TTFont(f, fonts_detail[f]))


def registor_fonts(FontsPath=None):
    # フォントの登録
    if FontsPath is None:
        # Fonts folder の場所
        FontsPath = '../assets/Fonts/'
    # Mplus-1p
    font_set_name = 'Mplus-1p'
    fonts_detail = {
        'Mplus1-med': 'Mplus1p-Medium.ttf',
        'Mplus1-lit': 'Mplus1p-Light.ttf',
        'Mplus1-bld': 'Mplus1p-Bold.ttf',
        'Mplus1-reg': 'Mplus1p-Regular.ttf',
        'Mplus1-thn': 'Mplus1p-Thin.ttf',
        'Mplus1-blk': 'Mplus1p-Black.ttf',
        'Mplus1-exblk': 'Mplus1p-ExtraBold.ttf'
    }
    registor_font(font_set_name, fonts_detail, FontsPath)

    # Muli
    font_set_name = 'Muli'
    fonts_detail = {
        'Muli-reg': 'Muli-Regular.ttf',
        'Muli-lit': 'Muli-LightItalic.ttf',
        'Muli-sbit': 'Muli-SemiBoldItalic.ttf',
        'Muli-it': 'Muli-Italic.ttf',
        'Muli-bit': 'Muli-BoldItalic.ttf',
        'Muli-xb': 'Muli-ExtraBold.ttf',
        'Muli-l': 'Muli-Light.ttf',
        'Muli-sb': 'Muli-SemiBold.ttf',
        'Muli-blit': 'Muli-BlackItalic.ttf',
        'Muli-b': 'Muli-Bold.ttf',
        'Muli-xlit': 'Muli-ExtraLightItalic.ttf',
        'Muli-xbit': 'Muli-ExtraBoldItalic.ttf',
        'Muli-xl': 'Muli-ExtraLight.ttf',
        'Muli-blk': 'Muli-Black.ttf',
    }
    registor_font(font_set_name, fonts_detail, FontsPath)

    # Symbola ★マークなど
    font_set_name = 'Symbola'
    fonts_detail = {
        'Symbola': 'Symbola.ttf'
    }
    registor_font(font_set_name, fonts_detail, FontsPath)

    # Fraktur
    font_set_name = 'Fraktur'
    fonts_detail = {
        'Fraktur': 'UnifrakturMaguntia.ttf'
    }
    registor_font(font_set_name, fonts_detail, FontsPath)