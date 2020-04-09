from fontTools.ttLib import TTFont, newTable
import sys


def main(font_path, gasp_ranges):
    font = TTFont(font_path)
    gasp_tbl = newTable("gasp")
    # "8=8,65535=15" --> {8: 8, 65535: 15}
    gasp_range = dict([
        map(int, i.split("="))
        for i in gasp_ranges.split(",")
    ])
    gasp_tbl.gaspRange = gasp_range
    font['gasp'] = gasp_tbl
    font.save(font.reader.file.name)


if __name__ == "__main__":
    main(sys.argv[1], sys.argv[2])

