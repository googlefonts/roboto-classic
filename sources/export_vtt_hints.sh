# Export vtt hinting from VTT source font and save as sources/vtt-hinting.ttx
set -e

SRC_TTF=sources/Roboto[ital,wdth,wght]_VTT.ttf
DST_TTX=sources/vtt-hinting.ttx

if [ -f "$SRC_TTF" ]; then
	echo "Exporting $SRC_TTF hints to $DST_TTX"
	python3 -m vttLib dumpfile $SRC_TTF $DST_TTX
	echo "Removing VTT font binary. To make more improvements, rerun 'sh sources/make_vtt_src_font.sh'."
	rm $SRC_TTF
else
	echo "VTT source font, '$SRC_TTF' does not exist so we cannot export its hints."
fi
