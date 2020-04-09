from fontTools.ttLib import TTFont
import sys


def main(font_path):
    font = TTFont(font_path)
    if "MVAR" in font:
        del font['MVAR']
    font.save(font.reader.file.name)


if __name__ == "__main__":
    main(sys.argv[1])

