# Roboto VF

This is a variable version of Roboto intended to be a 1:1 match with the official non-variable release from Google.

This is not an official Google project, but was enabled with generous funding by Google Fonts, who contracted Type Network.
The Roboto family of instances contained 6 weights and two widths of normal, along with italic of the regular width.
The project began by taking UFO instances generated during the build process of the Roboto v2.136 release, which have quadratic outlines. 
The Thin, Regular and Bold UFOs required some fixes for interpolation compatibility, and a build script was written that preserves outline overlaps.

* [/sources](sources/) contains new source UFOs

* [/fonts](fonts/) folder contains variation font TTFs

  * **Roboto[ital,wdth,wght].ttf** has deltas min, default, max, and also intermediate instances

Both fonts have named instances for all the styles in the v2.136 release.

## Install

    # Create a new virtualenv
    virtualenv env
    # Activate env
    source env/bin/activate
    # Install dependencies
    pip install -r requirements.txt

## Generate

    sh sources/build.sh


## Font hinting

The fonts have been hinted using Microsoft VTT and compiled using [vttLib](https://github.com/daltonmaag/vttLib). The hinting data is stored as xml in `sources/vtt-hinting.ttx`.

If you would like to make modifications to the hints using VTT, you'll need to do the following:

- Rebuild the fonts. We MUST ensure that hint modifications are being done on the latest binaries.
- Make a VTT source font which contains the existing hinting data by running `sh sources/make_vtt_src_font.sh`. The font will be exported to `sources/Roboto[ital,wdth,wght]_VTT.ttf`.
- In VTT, edit the newly generated font.
- Export the source font's hinting data back to `sources/vtt-hinting.ttx` by running `sh sources/export_vtt_hints.sh`
- Commit your changes using git.

Warning: vttLib doesn't support transformed composites. Please ensure source files do not contain them.


# License

Both fonts and software found in this repo are all available under the Apache License v2.0
