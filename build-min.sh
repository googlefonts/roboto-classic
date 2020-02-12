fontmake -o ttf-interpolatable -m Roboto-min.designspace --no-production-names
fonttools varLib Roboto-min.designspace

ttx -x MVAR Roboto-min-VF.ttf
rm Roboto-min-VF.ttf
ttx Roboto-min-VF.ttx
rm Roboto-min-VF.ttx

mv Roboto-min-VF.ttf fonts/Roboto-min-VF.ttf