# [v2.138 unhinted offical](https://github.com/google/roboto/releases/tag/v2.138) vs master_ttf

Regression tests to determine whether the .ufos in master_ufo/ produce acceptable static fonts.


## Building ttfs

master_ttf/ built with [fontmake v1.6.0](https://github.com/googlei18n/fontmake/releases/tag/v1.6.0) using the following cli:

```
FONTS=$(ls -d ./master_ufo/*.ufo/)
for f in $FONTS
do
  fontmake -u $f -o ttf --no-production-names
done;
```

## Generating diffs

Diffs produced with [fontdiffenator](https://github.com/googlefonts/fontdiffenator) and [diffbrowsers](https://github.com/googlefonts/diffbrowsers)

## Summary for commit e7ece644e5714951089cd6916db07fc055c9383d
- No marks are missing
- mark below for uni1E2C fixed
- Some mkmks are missing but no visual difference
- Some mkmks are modified but no visual difference
- No kerns are missing
- No glyphs are missing
- caretSlopeRun, caretSlopeRise in italics are different
- Modified glyphs: Some distortions, are they acceptable? more distortions are occuring in the italic and condensed styles


## Diff Notes

Following summary has been made by M Foley by reviewing each diff image

### Modified Glyphs
- uni015E which looks like a 'K' now features a double story construction. Fixes https://github.com/google/roboto/issues/289
- sampi, uni0236, uni030F, uni1AB5 have the most notable distortions. Other glyphs seem fine

Roboto-LightItalic/glyphs_modified/gifs/Desktop_Windows_7_ie_9.0_.gif

### Modified Marks
- Changes only uni1E2C
