# Create a source VTT font by merging vtt-hinting.ttx into the unhinted VF
set -e

SRC_TTF=fonts/unhinted/Roboto[ital,wdth,wght].ttf
DST_TTF=sources/Roboto[ital,wdth,wght]_VTT.ttf

if [ -f "$SRC_TTF" ]; then
	echo "Merging '$SRC_TTF' into '$DST_TTF'"
	cp $SRC_TTF $DST_TTF
	python -m vttLib mergefile sources/vtt-hinting.ttx $DST_TTF
	echo "VTT source font saved to '$DST_TTF'"
else
	echo "'$SRC_TTF' does not exist. Please build the fonts first. See the Readme"
fi
