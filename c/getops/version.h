/**
 * 
 *  @file   version.h 
 *  @brief  Versioning variables
 *
 */
#ifndef VERSION_H
#define VERSION_H

#include <string>

#define STR_HELPER(x) #x
#define STR(x) STR_HELPER(x)


// Application Version
#define VER_VAR     0   // Variant
#define VER_DEV     0   // Developer
#define VER_MAJOR   1   // Major
#define VER_MINOR   0   // Minor
#define VER_RC      9   // Release/Beta

#define VERSION_FULL   "" STR(VER_VAR) "." STR(VER_DEV) "." STR(VER_MAJOR) "." STR(VER_MINOR) "." STR(VER_RC)

std::string version_full_str = VERSION_FULL;


#endif
