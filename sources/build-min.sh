
#Make VF
fontmake -m sources/Roboto-min.designspace -o variable --output-path fonts/Roboto[ital,wdth,wght].ttf

# Remove MVAR
gftools fix-unwanted-tables -t "MVAR" fonts/Roboto[ital,wdth,wght].ttf

# Transfer Hints and compile them
python -m vttLib mergefile sources/vtt-hinting.ttx fonts/Roboto[ital,wdth,wght].ttf
python -m vttLib compile fonts/Roboto[ital,wdth,wght].ttf --ship
mv fonts/Roboto[ital,wdth,wght]#1.ttf fonts/Roboto[ital,wdth,wght].ttf

# Add gasp table
python Scripts/fix_gasp.py fonts/Roboto[ital,wdth,wght].ttf

# Fix STAT
statmake --designspace sources/Roboto-min.designspace --stylespace sources/Roboto-min.stylespace fonts/Roboto[ital,wdth,wght].ttf

# Make web
mkdir -p fonts/web
python Scripts/subset_for_web.py fonts/Roboto[ital,wdth,wght].ttf fonts/web/Roboto[ital,wdth,wght].ttf
# Can be removed once all browsers support slnt and ital axes properly
python Scripts/split_slnt_vf.py fonts/web/Roboto[ital,wdth,wght].ttf

