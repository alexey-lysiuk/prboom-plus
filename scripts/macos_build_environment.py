#!/usr/bin/env python

import hashlib
import os
import shutil
import subprocess
import sys
import urllib2


def _make_directory(path):
    if not os.path.exists(path):
        os.makedirs(path)


def _detect_cmake():
    for cmake_exe in ('cmake', '/Applications/CMake.app/Contents/bin/cmake'):
        try:
            subprocess.check_output([cmake_exe, '--version'])
        except (OSError, subprocess.CalledProcessError):
            continue

        return cmake_exe

    return None


class Configuration(object):
    def __init__(self):
        self_path = os.path.dirname(os.path.abspath(__file__))
        root_path = os.path.abspath(self_path + os.sep + os.pardir)
        build_path = root_path + os.sep + 'build_macos_dependencies'
        self.prefix = root_path + os.sep + 'dependencies_macos'
        bin_path = self.prefix + os.sep + 'bin'
        include_path = self.prefix + os.sep + 'include'
        lib_path = self.prefix + os.sep + 'lib'

        _make_directory(build_path)
        _make_directory(bin_path)
        _make_directory(include_path)
        _make_directory(lib_path)

        os.chdir(build_path)

        macos_min_ver = '10.9'
        common_flags = '-mmacosx-version-min=' + macos_min_ver

        sdk_path = root_path + os.sep + 'MacOSX' + macos_min_ver + '.sdk'
        if os.path.exists(sdk_path):
            common_flags += ' -isysroot ' + sdk_path

        cflags = common_flags + ' -I' + include_path
        ldflags = common_flags + ' -L' + lib_path

        # Workaround for undefined symbol _AudioUnitSetParameter linker error with playwave from libSDL2_mixer
        ldflags += ' -framework AudioUnit'

        self.environment = os.environ
        self.environment['PATH'] += ':' + bin_path
        self.environment['CPPFLAGS'] = cflags
        self.environment['CFLAGS'] = cflags
        self.environment['CXXFLAGS'] = cflags
        self.environment['OBJCFLAGS'] = cflags
        self.environment['OBJCXXFLAGS'] = cflags
        self.environment['LDFLAGS'] = ldflags

        self.make_executable = 'make'
        self.cmake_executable = _detect_cmake()


configuration = Configuration()


class Command(object):
    def __init__(self, *arguments):
        self._arguments = arguments
        self._previous = None

    def execute(self, workdir):
        if self._previous:
            self._previous.execute(workdir)

        subprocess.check_call(self._arguments, cwd=workdir, env=configuration.environment)


class Configure(Command):
    def __init__(self, *arguments):
        arguments = ('./configure', '--prefix=' + configuration.prefix) + arguments
        super(Configure, self).__init__(*arguments)


class ConfigureStatic(Configure):
    def __init__(self, *arguments):
        arguments = ('--enable-static', '--disable-shared') + arguments
        super(ConfigureStatic, self).__init__(*arguments)


class CMake(Command):
    def __init__(self, *arguments):
        arguments = (configuration.cmake_executable, '-DCMAKE_INSTALL_PREFIX=' + configuration.prefix) \
               + arguments + ('.',)
        super(CMake, self).__init__(*arguments)


class Make(Command):
    def __init__(self, *arguments):
        arguments = (configuration.make_executable,) + arguments
        super(Make, self).__init__(*arguments)


class Install(Make):
    def __init__(self, *arguments):
        arguments += ('install',)
        super(Install, self).__init__(*arguments)


class ConfigureInstall(Install):
    def __init__(self, *arguments):
        super(ConfigureInstall, self).__init__()
        self._previous = Configure(*arguments)


class ConfigureStaticInstall(Install):
    def __init__(self, *arguments):
        super(ConfigureStaticInstall, self).__init__()
        self._previous = ConfigureStatic(*arguments)


class CMakeInstall(Install):
    def __init__(self, *arguments):
        super(CMakeInstall, self).__init__()
        self._previous = CMake(*arguments)


Library = ConfigureStaticInstall
Tool = ConfigureInstall


class Package(object):
    def __init__(self, name, source, checksum, commands=Library()):
        self.name = name
        self.source = source
        self.checksum = checksum
        self.commands = commands

        self._filename = None
        self._work_path = None

    def build(self):
        print('=' * 80 + '\n Building ' + self.name + '\n' + '=' * 80)

        self._setup_workdir()

        if isinstance(self.commands, tuple) or isinstance(self.commands, list):
            for command in self.commands:
                command.execute(self._work_path)
        else:
            self.commands.execute(self._work_path)

        self._work_path = None
        self._filename = None

    def _setup_workdir(self):
        assert not self._filename
        self._filename = self.source.rsplit('/', 1)[1]

        if os.path.exists(self._filename):
            checksum = _calculate_checksum(self._filename)
        else:
            checksum = self._download()

        if checksum != self.checksum:
            raise Exception("Checksum for %s doesn't match!" % self._filename)

        assert not self._work_path
        self._work_path = self._guess_work_path()
        self._extract()

    def _download(self):
        try:
            response = urllib2.urlopen(self.source)
        except urllib2.HTTPError, urllib2.URLError:
            request = urllib2.Request(self.source)
            request.add_header('User-Agent',
                               'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:60.0) Gecko/20100101 Firefox/60.0')
            opener = urllib2.build_opener()
            response = opener.open(request)

        checksum = hashlib.sha256()
        step = 64 * 1024
        total = 0

        try:
            with open(self._filename, 'wb') as f:
                while True:
                    data = response.read(step)
                    total += len(data)

                    if not data:
                        sys.stdout.write('\n')
                        return checksum.hexdigest()

                    f.write(data)
                    checksum.update(data)

                    sys.stdout.write('\rDownloading %s: %i bytes' % (self._filename, total))
                    sys.stdout.flush()
        except IOError:
            os.unlink(self._filename)
            raise

    def _guess_work_path(self):
        files = subprocess.check_output(['tar', '-tf', self._filename])
        return files[:files.find('/')]

    def _extract(self):
        try:
            subprocess.check_call(['tar', '-xf', self._filename])
        except (IOError, subprocess.CalledProcessError):
            shutil.rmtree(self._work_path, ignore_errors=True)
            raise


def _calculate_checksum(filename):
    checksum = hashlib.sha256()

    with open(filename, 'rb') as f:
        data = True

        while data:
            data = f.read(64 * 1024)
            checksum.update(data)

    return checksum.hexdigest()


_packages = [
    # Dependencies of SDL2_mixer
    Package(
        name='ogg',
        source='https://downloads.xiph.org/releases/ogg/libogg-1.3.4.tar.gz',
        checksum='fe5670640bd49e828d64d2879c31cb4dde9758681bb664f9bdbf159a01b0c76e',
    ),
    Package(
        name='vorbis',
        source='https://downloads.xiph.org/releases/vorbis/libvorbis-1.3.6.tar.xz',
        checksum='af00bb5a784e7c9e69f56823de4637c350643deedaf333d0fa86ecdba6fcb415',
    ),
#     Package(
#         name='FLAC',
#         source='https://downloads.xiph.org/releases/flac/flac-1.3.3.tar.xz',
#         checksum='213e82bd716c9de6db2f98bcadbc4c24c7e2efe8c75939a1a84e28539c4e1748',
#         commands=Library('--disable-cpplibs',)
#     ),
#     Package(
#         name='Yasm',
#         source='https://www.tortall.net/projects/yasm/releases/yasm-1.3.0.tar.gz',
#         checksum='3dce6601b495f5b3d45b59f7d2492a340ee7e84b5beca17e48f862502bd5603f',
#     ),
#     Package(
#         name='vpx',
#         source='https://github.com/webmproject/libvpx/archive/v1.8.2.tar.gz',
#         checksum='8735d9fcd1a781ae6917f28f239a8aa358ce4864ba113ea18af4bb2dc8b474ac',
#         commands=Library('--disable-examples', '--disable-unit-tests')
#     ),
#     Package(
#         name='ffi',
#         source='https://sourceware.org/pub/libffi/libffi-3.2.1.tar.gz',
#         checksum='d06ebb8e1d9a22d19e38d63fdb83954253f39bedc5d46232a05645685722ca37'
#     )
#     Package(
#         name='gettext',
#         source='https://ftp.gnu.org/gnu/gettext/gettext-0.20.1.tar.xz',
#         checksum='53f02fbbec9e798b0faaf7c73272f83608e835c6288dd58be6c9bb54624a3800'
#     )
#     # TODO: sndfile (?)
#     Package(
#         name='fluidsynth',
#         source='https://github.com/FluidSynth/fluidsynth/archive/v2.1.0.tar.gz',
#         checksum='526addc6d8445035840d3af7282d3ba89567df209d28e183da04a1a877da2da3',
#         commands=CMakeInstall(
#             '-DCMAKE_BUILD_TYPE=Release',
#             '-DBUILD_SHARED_LIBS=NO',
#             '-DLIB_SUFFIX=',
#             '-Denable-framework=NO',
#             '-Denable-readline=NO',
#             '-Denable-sdl2=NO'
#         )
#     )
#     Package(
#         name='mad',
#         source='https://downloads.sourceforge.net/project/mad/libmad/0.15.1b/libmad-0.15.1b.tar.gz',
#         checksum='bbfac3ed6bfbc2823d3775ebb931087371e142bb0e9bb1bee51a76a6e0078690'
#     )
#     # Dependencies of SDL2_image
#     Package(
#         name='jpeg',
#         source='http://www.ijg.org/files/jpegsrc.v9c.tar.gz',
#         checksum='650250979303a649e21f87b5ccd02672af1ea6954b911342ea491f351ceb7122'
#     )
#     Package(
#         name='png',
#         source='https://downloads.sourceforge.net/libpng/libpng-1.6.37.tar.xz',
#         checksum='505e70834d35383537b6491e7ae8641f1a4bed1876dbfe361201fc80868d88ca'
#     )
#     Package(
#         name='xz',
#         source='https://downloads.sourceforge.net/project/lzmautils/xz-5.2.4.tar.gz',
#         checksum='b512f3b726d3b37b6dc4c8570e137b9311e7552e8ccbab4d39d47ce5f4177145'
#     )
#     Package(
#         name='tiff',
#         source='https://download.osgeo.org/libtiff/tiff-4.1.0.tar.gz',
#         checksum='5d29f32517dadb6dbcd1255ea5bbc93a2b54b94fbf83653b4d65c7d6775b8634',
#     )
#     Package(
#         name='webp',
#         source='https://storage.googleapis.com/downloads.webmproject.org/releases/webp/libwebp-1.0.1.tar.gz',
#         checksum='8c744a5422dbffa0d1f92e90b34186fb8ed44db93fbacb55abd751ac8808d922',
#         commands=Library('--disable-gif',)
#     )
#     # SDL2 libraries
#     Package(
#         name='SDL2',
#         source='https://www.libsdl.org/release/SDL2-2.0.9.tar.gz',
#         checksum='255186dc676ecd0c1dbf10ec8a2cc5d6869b5079d8a38194c2aecdff54b324b1',
#         commands=Library('--without-x',)
#     ),
#     Package(
#         name='SDL2_image',
#         source='https://www.libsdl.org/projects/SDL_image/release/SDL2_image-2.0.5.tar.gz',
#         checksum='bdd5f6e026682f7d7e1be0b6051b209da2f402a2dd8bd1c4bd9c25ad263108d0',
#         commands=Library(
#             '--disable-jpg-shared',
#             '--disable-png-shared',
#             '--disable-tif-shared',
#             '--disable-webp-shared'
#         )
#     )
#     Package(
#         name='SDL2_mixer',
#         source='https://www.libsdl.org/projects/SDL_mixer/release/SDL2_mixer-2.0.4.tar.gz',
#         checksum='b4cf5a382c061cd75081cf246c2aa2f9df8db04bdda8dcdc6b6cca55bede2419',
#         # TODO:
#         commands=Library('--disable-music-ogg-shared', '--disable-music-flac-shared')
#     ),
#     Package(
#         name='SDL2_net',
#         source='https://www.libsdl.org/projects/SDL_net/release/SDL2_net-2.0.1.tar.gz',
#         checksum='15ce8a7e5a23dafe8177c8df6e6c79b6749a03fff1e8196742d3571657609d21'
#     )
]


def _main():
    if not configuration.cmake_executable:
        cmake_package = Package(
            name='cmake',
            source='https://github.com/Kitware/CMake/releases/download/v3.16.2/cmake-3.16.2.tar.gz',
            checksum='8c09786ec60ca2be354c29829072c38113de9184f29928eb9da8446a5f2ce6a9'
        )
        _packages.insert(0, cmake_package)
        configuration.cmake_executable = 'cmake'

    for package in _packages:
        package.build()


if __name__ == '__main__':
    _main()
