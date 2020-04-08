from fontTools.ttLib import TTFont, newTable
import sys


def main(font_path):
    font = TTFont(font_path)
    gasp_tbl = newTable("gasp")
    gasp_tbl.gaspRange = {8: 8, 65535: 15}
    font['gasp'] = gasp_tbl
    font.save(font.reader.file.name)


if __name__ == "__main__":
    main(sys.argv[1])

