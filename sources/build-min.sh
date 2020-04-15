set -e

mkdir -p fonts

#Make unhinted VF
fontmake -m sources/Roboto-min.designspace -o variable --output-path fonts/Roboto[ital,wdth,wght].ttf
# Remove MVAR
python Scripts/drop_mvar.py fonts/Roboto[ital,wdth,wght].ttf
# Fix STAT
statmake --designspace sources/Roboto-min.designspace --stylespace sources/Roboto-min.stylespace fonts/Roboto[ital,wdth,wght].ttf
# Add smooth gasp table
python Scripts/fix_gasp.py fonts/Roboto[ital,wdth,wght].ttf "65535=15"


# Make hinted
# Transfer Hints and compile them
mkdir -p fonts/hinted
cp fonts/Roboto[ital,wdth,wght].ttf fonts/hinted/Roboto[ital,wdth,wght].ttf
python -m vttLib mergefile sources/vtt-hinting.ttx fonts/hinted/Roboto[ital,wdth,wght].ttf
python -m vttLib compile fonts/hinted/Roboto[ital,wdth,wght].ttf --ship
mv fonts/hinted/Roboto[ital,wdth,wght]#1.ttf fonts/hinted/Roboto[ital,wdth,wght].ttf
# Add gasp table
python Scripts/fix_gasp.py fonts/hinted/Roboto[ital,wdth,wght].ttf "8=8,65535=15"


# Make web
# TODO confirm we don't need to subset
mkdir -p fonts/web
python Scripts/subset_for_web.py fonts/hinted/Roboto[ital,wdth,wght].ttf fonts/web/Roboto[ital,wdth,wght].ttf
# Can be removed once all browsers support slnt and ital axes properly
mkdir -p fonts/web/split
python Scripts/split_slnt_vf.py fonts/web/Roboto[ital,wdth,wght].ttf fonts/web/split

