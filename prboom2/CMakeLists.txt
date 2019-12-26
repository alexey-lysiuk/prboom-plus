cmake_minimum_required(VERSION 3.0)

project("PrBoom-Plus" VERSION 2.5.1.7 LANGUAGES C)

set(CMAKE_MODULE_PATH "${CMAKE_CURRENT_SOURCE_DIR}/cmake")

set(PACKAGE_NAME "${PROJECT_NAME}")
set(PACKAGE_TARNAME "prboom-plus")
set(PACKAGE_VERSION "${PROJECT_VERSION}")
set(PACKAGE_STRING "${PROJECT_NAME} ${PROJECT_VERSION}")

include(CheckSymbolExists)

check_symbol_exists(stricmp "string.h" HAVE_STRICMP)
check_symbol_exists(strnicmp "string.h" HAVE_STRNICMP)
# TODO: min, max

check_symbol_exists(getopt "unistd.h" HAVE_GETOPT)
check_symbol_exists(mmap "sys/mman.h" HAVE_MMAP)
check_symbol_exists(sched_setaffinity "sched.h" HAVE_SCHED_SETAFFINITY)
check_symbol_exists(usleep "unistd.h" HAVE_USLEEP)

include(CheckIncludeFile)

check_include_file("sys/wait.h" HAVE_SYS_WAIT_H)
check_include_file("unistd.h" HAVE_UNISTD_H)
check_include_file("asm/byteorder.h" HAVE_ASM_BYTEORDER_H)

# TODO: Windows libs

find_package(OpenGL)
if(OPENGL_FOUND)
    # TODO: make option
    set(GL_DOOM TRUE)
endif()
if (OPENGL_GLU_FOUND)
    # TODO: make options
    set(USE_GLU_IMAGESCALE TRUE)
    set(USE_GLU_MIPMAP TRUE)
    set(USE_GLU_TESS TRUE)
endif()
# TODO: link with OpenGL

find_package(SDL2 REQUIRED)
if(SDL2_FOUND)
    # TODO: check for SDL_JoystickGetAxis
endif()

# TODO: make option, HAVE_..., USE_..., check function
find_package(SDL2_image)

# TODO: make option, HAVE_..., USE_..., check function 
find_package(SDL2_mixer)

# TODO: make option, HAVE_..., USE_..., check function
find_package(SDL2_net)

find_package(zlib)
if(ZLIB_FOUND)
    set(HAVE_ZLIB TRUE)
endif()

# TODO: other dependencies
# pcre
# mad
# ...

set(DOOMWADDIR "${CMAKE_INSTALL_PREFIX}/share/games/doom" CACHE PATH "Path to install prboom.wad and look for other WAD files")

configure_file(cmake/config.h.cin config.h)

if (MSVC)
    add_definitions("/D_CRT_SECURE_NO_WARNINGS")
else()
    # TODO: GCC/Clang options
endif()

add_subdirectory(data)
# TODO
#add_subdirectory(src)
