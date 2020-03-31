
#Make VF
fontmake -m sources/Roboto-min.designspace -o variable --output-path fonts/Roboto[ital,wdth,wght].ttf

# Remove MVAR
gftools fix-unwanted-tables -t "MVAR" fonts/Roboto[ital,wdth,wght].ttf

# Merge Hints from VTT source
python -m vttLib mergefile sources/vtt-hinting.ttx fonts/Roboto[ital,wdth,wght].ttf
python -m vttLib compile fonts/Roboto[ital,wdth,wght].ttf
rm fonts/Roboto[ital,wdth,wght].ttf
mv fonts/Roboto[ital,wdth,wght]#1.ttf fonts/Roboto[ital,wdth,wght].ttf

#fix GASP
ttx -m fonts/Roboto[ital,wdth,wght].ttf sources/fixes/gasp-fix.ttx
mv sources/fixes/gasp-fix.ttf fonts/gasp-fix.ttf
ttx fonts/gasp-fix.ttf
rm fonts/gasp-fix.ttf
rm fonts/Roboto[ital,wdth,wght].ttf
ttx fonts/gasp-fix.ttx
rm fonts/gasp-fix.ttx
mv fonts/gasp-fix.ttf fonts/Roboto[ital,wdth,wght].ttf

#fix STAT
statmake --designspace sources/Roboto-min.designspace --stylespace sources/Roboto-min.stylespace fonts/Roboto[ital,wdth,wght].ttf

#remove TSI tables from VF
python -m vttLib compile fonts/Roboto[ital,wdth,wght].ttf --ship
rm fonts/Roboto[ital,wdth,wght].ttf
mv fonts/Roboto[ital,wdth,wght]#1.ttf fonts/Roboto[ital,wdth,wght].ttf
