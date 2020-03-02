@echo off

if [%1]==[] goto usage

md bin
copy "%1\bin\FLAC.*" bin
copy "%1\bin\dumb.*" bin
copy "%1\bin\FLAC.*" bin
copy "%1\bin\glib-2.*" bin
copy "%1\bin\libcharset.*" bin
copy "%1\bin\libfluidsynth-2.*" bin
copy "%1\bin\libiconv.*" bin
copy "%1\bin\libintl.*" bin
copy "%1\bin\libmpg123.*" bin
copy "%1\bin\libpng16.*" bin
copy "%1\bin\modplug.*" bin
copy "%1\bin\ogg.*" bin
copy "%1\bin\opus.*" bin
copy "%1\bin\pcre.*" bin
copy "%1\bin\pcreposix.*" bin
copy "%1\bin\portmidi.*" bin
copy "%1\bin\SDL2*.*" bin
copy "%1\bin\vorbis*.*" bin
copy "%1\bin\zlib*.*" bin

md include
xcopy /s /i "%1\include\FLAC" include\FLAC
xcopy /s /i "%1\include\fluidsynth" include\fluidsynth
xcopy /s /i "%1\include\libmodplug" include\libmodplug
xcopy /s /i "%1\include\libpng16" include\libpng16
xcopy /s /i "%1\include\ogg" include\ogg
xcopy /s /i "%1\include\opus" include\opus
xcopy /s /i "%1\include\SDL2" include\SDL2
xcopy /s /i "%1\include\vorbis" include\vorbis
copy "%1\include\dumb.h" include
copy "%1\include\fluidsynth.h" include
copy "%1\include\fmt123.h" include
copy "%1\include\mad.h" include
copy "%1\include\mpg123.h" include
copy "%1\include\pcre.h" include
copy "%1\include\pcreposix.h" include
copy "%1\include\png.h" include
copy "%1\include\pngconf.h" include
copy "%1\include\pnglibconf.h" include
copy "%1\include\portmidi.h" include
copy "%1\include\porttime.h" include
copy "%1\include\zconf.h" include
copy "%1\include\zlib.h" include

md lib
copy "%1\lib\dumb.lib" lib
copy "%1\lib\FLAC.lib" lib
copy "%1\lib\fluidsynth.lib" lib
copy "%1\lib\glib-2.0.lib" lib
copy "%1\lib\libmpg123.lib" lib
copy "%1\lib\libpng16.lib" lib
copy "%1\lib\mad.lib" lib
copy "%1\lib\modplug.lib" lib
copy "%1\lib\ogg.lib" lib
copy "%1\lib\opus.lib" lib
copy "%1\lib\opusfile.lib" lib
copy "%1\lib\pcre.lib" lib
copy "%1\lib\pcreposix.lib" lib
copy "%1\lib\portmidi.lib" lib
copy "%1\lib\SDL2.lib" lib
copy "%1\lib\SDL2_image.lib" lib
copy "%1\lib\SDL2_mixer.lib" lib
copy "%1\lib\SDL2_net.lib" lib
copy "%1\lib\manual-link\SDL2main.lib" lib
copy "%1\lib\vorbis.lib" lib
copy "%1\lib\vorbisenc.lib" lib
copy "%1\lib\vorbisfile.lib" lib
copy "%1\lib\zlib.lib" lib

goto :eof

:usage
echo Usage: %0 prefix-path
exit /b 1
