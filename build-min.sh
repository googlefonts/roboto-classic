
#Make VF
fontmake -o ttf-interpolatable -m Roboto-min.designspace --no-production-names
fonttools varLib Roboto-min.designspace
mv Roboto-min-VF.ttf fonts/Roboto-unhinted.ttf

# Remove MVAR
ttx -x MVAR fonts/Roboto-unhinted.ttf
rm fonts/Roboto-unhinted.ttf
ttx fonts/Roboto-unhinted.ttx
rm fonts/Roboto-unhinted.ttx

# Merge Hints from VTT source
python -m vttLib dumpfile HintingSource/VTTSourceRoboto-min-VF.ttf

mv HintingSource/VTTSourceRoboto-min-VF_VTT_Hinting.ttx fonts/VTTSourceRoboto-min-VF_VTT_Hinting.ttx

python -m vttLib mergefile fonts/VTTSourceRoboto-min-VF_VTT_Hinting.ttx fonts/Roboto-unhinted.ttf

rm fonts/VTTSourceRoboto-min-VF_VTT_Hinting.ttx

python -m vttLib compile fonts/Roboto-unhinted.ttf

rm fonts/Roboto-unhinted.ttf

mv fonts/Roboto-unhinted#1.ttf fonts/Roboto[ital,wdth,wght].ttf

#fix maxp
ttx -m fonts/Roboto[ital,wdth,wght].ttf fonts/fixes/maxp-fix.ttx
mv fonts/fixes/maxp-fix.ttf fonts/maxp-fix.ttf
ttx fonts/maxp-fix.ttf
rm fonts/maxp-fix.ttf
rm fonts/Roboto[ital,wdth,wght].ttf
ttx fonts/maxp-fix.ttx
rm fonts/maxp-fix.ttx
mv fonts/maxp-fix.ttf fonts/Roboto[ital,wdth,wght].ttf

#fix GASP
ttx -m fonts/Roboto[ital,wdth,wght].ttf fonts/fixes/gasp-fix.ttx
mv fonts/fixes/gasp-fix.ttf fonts/gasp-fix.ttf
ttx fonts/gasp-fix.ttf
rm fonts/gasp-fix.ttf
rm fonts/Roboto[ital,wdth,wght].ttf
ttx fonts/gasp-fix.ttx
rm fonts/gasp-fix.ttx
mv fonts/gasp-fix.ttf fonts/Roboto[ital,wdth,wght].ttf

#fix STAT

#remove TSI tables from VF
ttx -x TSI0 -x TSI1 -x TSI2 -x TSI3 -x TSI5 fonts/Roboto[ital,wdth,wght].ttf
rm fonts/Roboto[ital,wdth,wght].ttf
ttx fonts/Roboto[ital,wdth,wght].ttx
rm fonts/Roboto[ital,wdth,wght].ttx