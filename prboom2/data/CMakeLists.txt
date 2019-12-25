set(RDATAWAD_SOURCES
    rd_main.c
    rd_util.c
    rd_util.h
    rd_output.c
    rd_output.h
    rd_sound.c
    rd_sound.h
    rd_palette.c
    rd_palette.h
    rd_graphic.c
    rd_graphic.h
)

add_executable(rdatawad ${RDATAWAD_SOURCES})
target_include_directories(rdatawad PRIVATE "${CMAKE_CURRENT_BINARY_DIR}/..")

set(WAD_DATA prboom-plus.wad)

set(PALETTE
    palette.rgb
)

set(LUMPS
    lumps/switches.lmp
    lumps/animated.lmp
    lumps/crbrick.lmp
    lumps/crtan.lmp
    lumps/crgray.lmp
    lumps/crgreen.lmp
    lumps/crbrown.lmp
    lumps/crgold.lmp
    lumps/crred.lmp
    lumps/crblue.lmp
    lumps/crblue2.lmp
    lumps/crorange.lmp
    lumps/cryellow.lmp
)

set(COLORMAPS 
    lumps/watermap.lmp
)

set(TABLES
    lumps/sinetabl.lmp
    lumps/tangtabl.lmp
    lumps/tantoang.lmp
    lumps/gammatbl.lmp
    lumps/chexdeh.lmp
    lumps/bfgbex.lmp
    lumps/nervebex.lmp
    lumps/glshadow.lmp
    lumps/glfp.lmp
    lumps/glvp.lmp
    lumps/-prbhud-.lmp
    lumps/m_ammo.lmp
    lumps/m_armour.lmp
    lumps/m_arrow.lmp
    lumps/m_health.lmp
    lumps/m_key.lmp
    lumps/m_normal.lmp
    lumps/m_shadow.lmp
    lumps/m_power.lmp
    lumps/m_weap.lmp
    lumps/m_mark.lmp
)

# TODO: make option
set(DOGS TRUE)
# TODO: make option
set(NONFREE_GRAPHICS TRUE)

set(SOUNDS "")

if(DOGS)
    if(NONFREE_GRAPHICS)
        set(
            ${SOUNDS}
            sounds/dsdgsit.wav
            sounds/dsdgatk.wav
            sounds/dsdgact.wav
            sounds/dsdgdth.wav
            sounds/dsdgpain.wav
        )
    else()
        set(
            ${SOUNDS}
            sounds/free/dsdgsit.wav
            sounds/free/dsdgatk.wav
            sounds/free/dsdgact.wav
            sounds/free/dsdgdth.wav
            sounds/free/dsdgpain.wav
        )
    endif()
endif()

if(NONFREE_GRAPHICS)
    set(
        ${SOUNDS}
        sounds/dssecret.wav
        sounds/dsgibdth.wav
    )
endif()

set(GRAPHICS
    graphics/dig0.ppm
    graphics/dig1.ppm
    graphics/dig2.ppm
    graphics/dig3.ppm
    graphics/dig4.ppm
    graphics/dig5.ppm
    graphics/dig6.ppm
    graphics/dig7.ppm
    graphics/dig8.ppm
    graphics/dig9.ppm
    graphics/diga.ppm
    graphics/digb.ppm
    graphics/digc.ppm
    graphics/digd.ppm
    graphics/dige.ppm
    graphics/digf.ppm
    graphics/digg.ppm
    graphics/digh.ppm
    graphics/digi.ppm
    graphics/digj.ppm
    graphics/digk.ppm
    graphics/digl.ppm
    graphics/digm.ppm
    graphics/dign.ppm
    graphics/digo.ppm
    graphics/digp.ppm
    graphics/digq.ppm
    graphics/digr.ppm
    graphics/digs.ppm
    graphics/digt.ppm
    graphics/digu.ppm
    graphics/digv.ppm
    graphics/digw.ppm
    graphics/digx.ppm
    graphics/digy.ppm
    graphics/digz.ppm
    graphics/dig45.ppm
    graphics/dig47.ppm
    graphics/dig58.ppm
    graphics/dig91.ppm
    graphics/dig93.ppm
    graphics/stbr123.ppm
    graphics/stbr124.ppm
    graphics/stbr125.ppm
    graphics/stbr126.ppm
    graphics/stbr127.ppm
    graphics/boxul.ppm
    graphics/boxuc.ppm
    graphics/boxur.ppm
    graphics/boxcl.ppm
    graphics/boxcc.ppm
    graphics/boxcr.ppm
    graphics/boxll.ppm
    graphics/boxlc.ppm
    graphics/boxlr.ppm
    graphics/stkeys6.ppm
    graphics/stkeys7.ppm
    graphics/stkeys8.ppm
    graphics/stcfn096.ppm
    graphics/m_butt1.ppm
    graphics/m_butt2.ppm
    graphics/m_colors.ppm
    graphics/m_palno.ppm
    graphics/m_palsel.ppm
    graphics/m_vbox.ppm
    graphics/cross1.ppm
    graphics/cross2.ppm
    graphics/cross3.ppm
)

if(NONFREE_GRAPHICS)
    set(GRAPHICS
        ${GRAPHICS}
        graphics/m_generl.ppm
        graphics/m_setup.ppm
        graphics/m_auto.ppm
        graphics/m_keybnd.ppm
        graphics/m_chat.ppm
        graphics/m_compat.ppm
        graphics/m_enem.ppm
        graphics/m_mess.ppm
        graphics/m_stat.ppm
        graphics/m_weap.ppm
        graphics/m_horsen.ppm
        graphics/m_versen.ppm
        graphics/prboom.ppm
        graphics/m_accel.ppm
        graphics/m_loksen.ppm
    )
endif()

set(FLATS
    flats/-n0_tex-.ppm
)

set(SPRITES
    sprites/tnt1a0.ppm
)
set(SPRITEP "0,0,sprites/tnt1a0.ppm")

# TODO
# if(DOGS)
#     if(NONFREE_GRAPHICS)
# SPRITES += sprites/dogsd5.ppm
# SPRITEP += 32,59,sprites/dogsd5.ppm
# SPRITES += sprites/dogsh5.ppm
# SPRITEP += 32,59,sprites/dogsh5.ppm
# SPRITES += sprites/dogsc5.ppm
# SPRITEP += 32,59,sprites/dogsc5.ppm
# SPRITES += sprites/dogsg5.ppm
# SPRITEP += 32,59,sprites/dogsg5.ppm
# SPRITES += sprites/dogsb1.ppm
# SPRITEP += 32,59,sprites/dogsb1.ppm
# SPRITES += sprites/dogsa5.ppm
# SPRITEP += 32,59,sprites/dogsa5.ppm
# SPRITES += sprites/dogse5.ppm
# SPRITEP += 32,59,sprites/dogse5.ppm
# SPRITES += sprites/dogsc1.ppm
# SPRITEP += 32,59,sprites/dogsc1.ppm
# SPRITES += sprites/dogsd1.ppm
# SPRITEP += 32,59,sprites/dogsd1.ppm
# SPRITES += sprites/dogsb5.ppm
# SPRITEP += 32,59,sprites/dogsb5.ppm
# SPRITES += sprites/dogsf5.ppm
# SPRITEP += 32,59,sprites/dogsf5.ppm
# SPRITES += sprites/dogsa1.ppm
# SPRITEP += 32,59,sprites/dogsa1.ppm
# SPRITES += sprites/dogse1.ppm
# SPRITEP += 32,59,sprites/dogse1.ppm
# SPRITES += sprites/dogsf1.ppm
# SPRITEP += 32,59,sprites/dogsf1.ppm
# SPRITES += sprites/dogsd2d8.ppm
# SPRITEP += 32,59,sprites/dogsd2d8.ppm
# SPRITES += sprites/dogsh2.ppm
# SPRITEP += 32,59,sprites/dogsh2.ppm
# SPRITES += sprites/dogsg1.ppm
# SPRITEP += 32,59,sprites/dogsg1.ppm
# SPRITES += sprites/dogsh8.ppm
# SPRITEP += 32,59,sprites/dogsh8.ppm
# SPRITES += sprites/dogse8.ppm
# SPRITEP += 32,59,sprites/dogse8.ppm
# SPRITES += sprites/dogsd4d6.ppm
# SPRITEP += 32,59,sprites/dogsd4d6.ppm
# SPRITES += sprites/dogsh4.ppm
# SPRITEP += 32,59,sprites/dogsh4.ppm
# SPRITES += sprites/dogsa2a8.ppm
# SPRITEP += 32,59,sprites/dogsa2a8.ppm
# SPRITES += sprites/dogse2.ppm
# SPRITEP += 32,59,sprites/dogse2.ppm
# SPRITES += sprites/dogsf8.ppm
# SPRITEP += 32,59,sprites/dogsf8.ppm
# SPRITES += sprites/dogsh1.ppm
# SPRITEP += 32,59,sprites/dogsh1.ppm
# SPRITES += sprites/dogsa4a6.ppm
# SPRITEP += 32,59,sprites/dogsa4a6.ppm
# SPRITES += sprites/dogse4.ppm
# SPRITEP += 32,59,sprites/dogse4.ppm
# SPRITES += sprites/dogsb4b6.ppm
# SPRITEP += 32,59,sprites/dogsb4b6.ppm
# SPRITES += sprites/dogsf4.ppm
# SPRITEP += 32,59,sprites/dogsf4.ppm
# SPRITES += sprites/dogsh6.ppm
# SPRITEP += 32,59,sprites/dogsh6.ppm
# SPRITES += sprites/dogsb2b8.ppm
# SPRITEP += 32,59,sprites/dogsb2b8.ppm
# SPRITES += sprites/dogsf2.ppm
# SPRITEP += 32,59,sprites/dogsf2.ppm
# SPRITES += sprites/dogsc2c8.ppm
# SPRITEP += 32,59,sprites/dogsc2c8.ppm
# SPRITES += sprites/dogsg2.ppm
# SPRITEP += 32,59,sprites/dogsg2.ppm
# SPRITES += sprites/dogsg6.ppm
# SPRITEP += 32,59,sprites/dogsg6.ppm
# SPRITES += sprites/dogsc4c6.ppm
# SPRITEP += 32,59,sprites/dogsc4c6.ppm
# SPRITES += sprites/dogsg4.ppm
# SPRITEP += 32,59,sprites/dogsg4.ppm
# SPRITES += sprites/dogsg8.ppm
# SPRITEP += 32,59,sprites/dogsg8.ppm
# SPRITES += sprites/dogsf6.ppm
# SPRITEP += 32,59,sprites/dogsf6.ppm
# SPRITES += sprites/dogsn0.ppm
# SPRITEP += 32,59,sprites/dogsn0.ppm
# SPRITES += sprites/dogse6.ppm
# SPRITEP += 32,59,sprites/dogse6.ppm
# SPRITES += sprites/dogsd3d7.ppm
# SPRITEP += 32,59,sprites/dogsd3d7.ppm
# SPRITES += sprites/dogsh3.ppm
# SPRITEP += 32,59,sprites/dogsh3.ppm
# SPRITES += sprites/dogsh7.ppm
# SPRITEP += 32,59,sprites/dogsh7.ppm
# SPRITES += sprites/dogsi0.ppm
# SPRITEP += 32,59,sprites/dogsi0.ppm
# SPRITES += sprites/dogsa3a7.ppm
# SPRITEP += 32,59,sprites/dogsa3a7.ppm
# SPRITES += sprites/dogse3.ppm
# SPRITEP += 32,59,sprites/dogse3.ppm
# SPRITES += sprites/dogsb3b7.ppm
# SPRITEP += 32,59,sprites/dogsb3b7.ppm
# SPRITES += sprites/dogsf3.ppm
# SPRITEP += 32,59,sprites/dogsf3.ppm
# SPRITES += sprites/dogsf7.ppm
# SPRITEP += 32,59,sprites/dogsf7.ppm
# SPRITES += sprites/dogse7.ppm
# SPRITEP += 32,59,sprites/dogse7.ppm
# SPRITES += sprites/dogsc3c7.ppm
# SPRITEP += 32,59,sprites/dogsc3c7.ppm
# SPRITES += sprites/dogsg3.ppm
# SPRITEP += 32,59,sprites/dogsg3.ppm
# SPRITES += sprites/dogsg7.ppm
# SPRITEP += 32,59,sprites/dogsg7.ppm
# SPRITES += sprites/dogsj0.ppm
# SPRITEP += 32,59,sprites/dogsj0.ppm
# SPRITES += sprites/dogsk0.ppm
# SPRITEP += 32,59,sprites/dogsk0.ppm
# SPRITES += sprites/dogsl0.ppm
# SPRITEP += 32,59,sprites/dogsl0.ppm
# SPRITES += sprites/dogsm0.ppm
# SPRITEP += 32,59,sprites/dogsm0.ppm
# else
# SPRITES += sprites/free/dogsa1.ppm
# SPRITEP += 10,30,sprites/free/dogsa1.ppm
# SPRITES += sprites/free/dogsa2a8.ppm
# SPRITEP += 14,29,sprites/free/dogsa2a8.ppm
# SPRITES += sprites/free/dogsa3a7.ppm
# SPRITEP += 15,29,sprites/free/dogsa3a7.ppm
# SPRITES += sprites/free/dogsa4a6.ppm
# SPRITEP += 12,29,sprites/free/dogsa4a6.ppm
# SPRITES += sprites/free/dogsa5.ppm
# SPRITEP += 10,30,sprites/free/dogsa5.ppm
# SPRITES += sprites/free/dogsb1.ppm
# SPRITEP += 9,30,sprites/free/dogsb1.ppm
# SPRITES += sprites/free/dogsb2b8.ppm
# SPRITEP += 13,29,sprites/free/dogsb2b8.ppm
# SPRITES += sprites/free/dogsb3b7.ppm
# SPRITEP += 14,29,sprites/free/dogsb3b7.ppm
# SPRITES += sprites/free/dogsb4b6.ppm
# SPRITEP += 12,29,sprites/free/dogsb4b6.ppm
# SPRITES += sprites/free/dogsb5.ppm
# SPRITEP += 9,29,sprites/free/dogsb5.ppm
# SPRITES += sprites/free/dogsc1.ppm
# SPRITEP += 10,30,sprites/free/dogsc1.ppm
# SPRITES += sprites/free/dogsc2c8.ppm
# SPRITEP += 11,29,sprites/free/dogsc2c8.ppm
# SPRITES += sprites/free/dogsc3c7.ppm
# SPRITEP += 14,29,sprites/free/dogsc3c7.ppm
# SPRITES += sprites/free/dogsc4c6.ppm
# SPRITEP += 12,29,sprites/free/dogsc4c6.ppm
# SPRITES += sprites/free/dogsc5.ppm
# SPRITEP += 10,30,sprites/free/dogsc5.ppm
# SPRITES += sprites/free/dogsd1.ppm
# SPRITEP += 10,30,sprites/free/dogsd1.ppm
# SPRITES += sprites/free/dogsd2d8.ppm
# SPRITEP += 12,29,sprites/free/dogsd2d8.ppm
# SPRITES += sprites/free/dogsd3d7.ppm
# SPRITEP += 14,29,sprites/free/dogsd3d7.ppm
# SPRITES += sprites/free/dogsd4d6.ppm
# SPRITEP += 13,29,sprites/free/dogsd4d6.ppm
# SPRITES += sprites/free/dogsd5.ppm
# SPRITEP += 9,29,sprites/free/dogsd5.ppm
# SPRITES += sprites/free/dogse1.ppm
# SPRITEP += 10,30,sprites/free/dogse1.ppm
# SPRITES += sprites/free/dogse2.ppm
# SPRITEP += 14,29,sprites/free/dogse2.ppm
# SPRITES += sprites/free/dogse3.ppm
# SPRITEP += 14,29,sprites/free/dogse3.ppm
# SPRITES += sprites/free/dogse4.ppm
# SPRITEP += 13,29,sprites/free/dogse4.ppm
# SPRITES += sprites/free/dogse5.ppm
# SPRITEP += 9,29,sprites/free/dogse5.ppm
# SPRITES += sprites/free/dogse6.ppm
# SPRITEP += 13,29,sprites/free/dogse6.ppm
# SPRITES += sprites/free/dogse7.ppm
# SPRITEP += 14,29,sprites/free/dogse7.ppm
# SPRITES += sprites/free/dogse8.ppm
# SPRITEP += 14,29,sprites/free/dogse8.ppm
# SPRITES += sprites/free/dogsf1.ppm
# SPRITEP += 10,30,sprites/free/dogsf1.ppm
# SPRITES += sprites/free/dogsf2.ppm
# SPRITEP += 13,29,sprites/free/dogsf2.ppm
# SPRITES += sprites/free/dogsf3.ppm
# SPRITEP += 16,29,sprites/free/dogsf3.ppm
# SPRITES += sprites/free/dogsf4.ppm
# SPRITEP += 13,29,sprites/free/dogsf4.ppm
# SPRITES += sprites/free/dogsf5.ppm
# SPRITEP += 9,28,sprites/free/dogsf5.ppm
# SPRITES += sprites/free/dogsf6.ppm
# SPRITEP += 13,29,sprites/free/dogsf6.ppm
# SPRITES += sprites/free/dogsf7.ppm
# SPRITEP += 16,29,sprites/free/dogsf7.ppm
# SPRITES += sprites/free/dogsf8.ppm
# SPRITEP += 13,29,sprites/free/dogsf8.ppm
# SPRITES += sprites/free/dogsg1.ppm
# SPRITEP += 9,30,sprites/free/dogsg1.ppm
# SPRITES += sprites/free/dogsg2.ppm
# SPRITEP += 12,29,sprites/free/dogsg2.ppm
# SPRITES += sprites/free/dogsg3.ppm
# SPRITEP += 13,29,sprites/free/dogsg3.ppm
# SPRITES += sprites/free/dogsg4.ppm
# SPRITEP += 11,29,sprites/free/dogsg4.ppm
# SPRITES += sprites/free/dogsg5.ppm
# SPRITEP += 8,28,sprites/free/dogsg5.ppm
# SPRITES += sprites/free/dogsg6.ppm
# SPRITEP += 11,29,sprites/free/dogsg6.ppm
# SPRITES += sprites/free/dogsg7.ppm
# SPRITEP += 13,29,sprites/free/dogsg7.ppm
# SPRITES += sprites/free/dogsg8.ppm
# SPRITEP += 12,29,sprites/free/dogsg8.ppm
# SPRITES += sprites/free/dogsh1.ppm
# SPRITEP += 9,25,sprites/free/dogsh1.ppm
# SPRITES += sprites/free/dogsh2.ppm
# SPRITEP += 10,26,sprites/free/dogsh2.ppm
# SPRITES += sprites/free/dogsh3.ppm
# SPRITEP += 11,26,sprites/free/dogsh3.ppm
# SPRITES += sprites/free/dogsh4.ppm
# SPRITEP += 11,26,sprites/free/dogsh4.ppm
# SPRITES += sprites/free/dogsh5.ppm
# SPRITEP += 9,26,sprites/free/dogsh5.ppm
# SPRITES += sprites/free/dogsh6.ppm
# SPRITEP += 11,26,sprites/free/dogsh6.ppm
# SPRITES += sprites/free/dogsh7.ppm
# SPRITEP += 11,26,sprites/free/dogsh7.ppm
# SPRITES += sprites/free/dogsh8.ppm
# SPRITEP += 10,26,sprites/free/dogsh8.ppm
# SPRITES += sprites/free/dogsi0.ppm
# SPRITEP += 10,30,sprites/free/dogsi0.ppm
# SPRITES += sprites/free/dogsj0.ppm
# SPRITEP += 10,30,sprites/free/dogsj0.ppm
# SPRITES += sprites/free/dogsk0.ppm
# SPRITEP += 11,27,sprites/free/dogsk0.ppm
# SPRITES += sprites/free/dogsl0.ppm
# SPRITEP += 11,20,sprites/free/dogsl0.ppm
# SPRITES += sprites/free/dogsm0.ppm
# SPRITEP += 12,15,sprites/free/dogsm0.ppm
# SPRITES += sprites/free/dogsn0.ppm
# SPRITEP += 13,15,sprites/free/dogsn0.ppm
# endif
# endif
#
# if NONFREE_GRAPHICS
# SPRITES += sprites/pls1a0.ppm
# SPRITEP += 8,12,sprites/pls1a0.ppm
# SPRITES += sprites/pls1b0.ppm
# SPRITEP += 9,12,sprites/pls1b0.ppm
# SPRITES += sprites/pls1c0.ppm
# SPRITEP += 8,12,sprites/pls1c0.ppm
# SPRITES += sprites/pls1d0.ppm
# SPRITEP += 9,12,sprites/pls1d0.ppm
# SPRITES += sprites/pls1e0.ppm
# SPRITEP += 25,37,sprites/pls1e0.ppm
# SPRITES += sprites/pls1f0.ppm
# SPRITEP += 25,37,sprites/pls1f0.ppm
# SPRITES += sprites/pls1g0.ppm
# SPRITEP += 26,42,sprites/pls1g0.ppm
# SPRITES += sprites/pls2a0.ppm
# SPRITEP += 7,10,sprites/pls2a0.ppm
# SPRITES += sprites/pls2b0.ppm
# SPRITEP += 6,8,sprites/pls2b0.ppm
# SPRITES += sprites/pls2c0.ppm
# SPRITEP += 5,6,sprites/pls2c0.ppm
# SPRITES += sprites/pls2d0.ppm
# SPRITEP += 7,10,sprites/pls2d0.ppm
# SPRITES += sprites/pls2e0.ppm
# SPRITEP += 11,16,sprites/pls2e0.ppm
# endif

set(WAD_SRC 
    ${PALETTE}
    ${LUMPS}
    ${COLORMAPS}
    ${TABLES}
    ${SOUNDS}
    ${GRAPHICS}
    ${FLATS}
    ${SPRITES}
)

set(WAD_CMDLINE 
    -palette ${PALETTE}
    -lumps ${LUMPS}
    -marker C_START -lumps ${COLORMAPS} -marker C_END
    -marker B_START -lumps ${TABLES} -marker B_END
    -sounds ${SOUNDS}
    -graphics ${GRAPHICS}
    -marker FF_START -flats ${FLATS} -marker FF_END
    -marker SS_START -sprites ${SPRITEP} -marker SS_END
)

# TODO: output to build root (?)
add_custom_command(
    OUTPUT ${WAD_DATA}
    COMMAND rdatawad -I ${CMAKE_CURRENT_SOURCE_DIR} ${WAD_CMDLINE} -o ${WAD_DATA}
    DEPENDS rdatawad ${WAD_SRC}
)
# TODO: remove all and add to executable as dependency
add_custom_target(prboomwad ALL DEPENDS ${WAD_DATA})

# message("${WAD_CMDLINE}")

# add_custom_target(prboomwad #ALL
#     rdatawad -I ${CMAKE_CURRENT_SOURCE_DIR} ${WAD_CMDLINE} -o ${WAD_DATA}
#     DEPENDS rdatawad ${WAD_SRC}
# )
