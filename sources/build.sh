set -e

mkdir -p fonts


#Make unhinted VF
mkdir -p fonts/unhinted
UNHINTED_VF_PATH=fonts/unhinted/Roboto[ital,wdth,wght].ttf
fontmake -m sources/Roboto.designspace -o variable --output-path $UNHINTED_VF_PATH
python Scripts/drop_mvar.py $UNHINTED_VF_PATH
statmake --designspace sources/Roboto.designspace --stylespace sources/Roboto.stylespace $UNHINTED_VF_PATH
python Scripts/fix_gasp.py $UNHINTED_VF_PATH "65535=15"
python Scripts/instantiate_statics.py $UNHINTED_VF_PATH fonts/unhinted/static


# Make Android
mkdir -p fonts/android
ANDROID_VF_PATH=fonts/android/Roboto[ital,wdth,wght].ttf
cp $UNHINTED_VF_PATH $ANDROID_VF_PATH
python Scripts/force_yminmax.py $ANDROID_VF_PATH $ANDROID_VF_PATH
python Scripts/instantiate_statics.py $ANDROID_VF_PATH fonts/android/static


# Make hinted
mkdir -p fonts/hinted
HINTED_VF_PATH=fonts/hinted/Roboto[ital,wdth,wght].ttf
# Transfer Hints and compile them
cp $UNHINTED_VF_PATH $HINTED_VF_PATH
python -m vttLib mergefile sources/vtt-hinting.ttx $HINTED_VF_PATH
python -m vttLib compile $HINTED_VF_PATH $HINTED_VF_PATH.fix --ship
mv $HINTED_VF_PATH.fix $HINTED_VF_PATH
python Scripts/touchup_for_web.py $HINTED_VF_PATH
python Scripts/fix_gasp.py $HINTED_VF_PATH "8=8,65535=15"
python Scripts/instantiate_statics.py $HINTED_VF_PATH fonts/hinted/static


# Make web
mkdir -p fonts/web
WEB_VF_PATH=fonts/web/Roboto[ital,wdth,wght].ttf
python Scripts/subset_for_web.py $HINTED_VF_PATH $WEB_VF_PATH
python Scripts/touchup_for_web.py $WEB_VF_PATH
# Can be removed once all browsers support slnt and ital axes properly
mkdir -p fonts/web/split
python Scripts/split_slnt_vf.py $WEB_VF_PATH fonts/web/split
python Scripts/instantiate_statics.py $WEB_VF_PATH fonts/web/static
python Scripts/touchup_for_web.py fonts/web/static/Roboto-Thin.ttf
python Scripts/touchup_for_web.py fonts/web/static/Roboto-ThinItalic.ttf


# Make ChromeOS
mkdir -p fonts/chromeos
CHROMEOS_VF_PATH=fonts/chromeos/Roboto[ital,wdth,wght].ttf
cp $HINTED_VF_PATH $CHROMEOS_VF_PATH
pyftsubset --unicodes="*" --name-IDs='*' --name-legacy --name-languages="*" \
	   --recalc-bounds --recalc-timestamp --canonical-order \
	   --layout-features="*" --notdef-outline $CHROMEOS_VF_PATH \
	   --output-file=$CHROMEOS_VF_PATH.fix
mv $CHROMEOS_VF_PATH.fix $CHROMEOS_VF_PATH
python Scripts/instantiate_statics.py $CHROMEOS_VF_PATH fonts/chromeos/static

