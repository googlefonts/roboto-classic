# Compare generated instances against the official v2.138 release
OLD_FONTS=$(ls ../v2_138_fonts/*.ttf)
NEW_FONTS_PATH=../../master_ttf


for old_font in $OLD_FONTS
do
    filename=$(basename $old_font);
    new_font=$NEW_FONTS_PATH/$filename
    report_file=$(basename $old_font ttf)"md"
    diffenator $old_font $new_font -ol 10 -md > $report_file
    viz_diffenator.py $old_font $new_font -u http://127.0.0.1:5000 -l
done;