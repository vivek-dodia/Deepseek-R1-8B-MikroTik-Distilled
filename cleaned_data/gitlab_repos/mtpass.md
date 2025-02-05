# Repository Information
Name: mtpass

# Files

File: config
================================================
[core]
	repositoryformatversion = 0
	filemode = false
	bare = false
	logallrefupdates = true
	symlinks = false
	ignorecase = true
[remote "origin"]
	url = https://gitlab.com/gavz/mtpass.git
	fetch = +refs/heads/*:refs/remotes/origin/*
[branch "master"]
	remote = origin
	merge = refs/heads/master
================================================

File: description
================================================
Unnamed repository; edit this file 'description' to name the repository.
================================================

File: bootstrap.sh
================================================
#!/bin/sh
autoreconf -i
================================================

File: CMakeLists.txt
================================================
CMAKE_MINIMUM_REQUIRED(VERSION 2.6)
PROJECT("mtpass")
FIND_PACKAGE(OpenSSL REQUIRED)
ADD_EXECUTABLE(mtpass mtpass.cpp)
INCLUDE_DIRECTORIES("${OPENSSL_INCLUDE_DIR}")
TARGET_LINK_LIBRARIES(mtpass ${OPENSSL_LIBRARIES})
INSTALL(TARGETS mtpass RUNTIME DESTINATION bin)
================================================

File: configure.ac
================================================
#                                               -*- Autoconf -*-
# Process this file with autoconf to produce a configure script.
AC_PREREQ([2.69])
AC_INIT([mtpass], [0.9], [manio@skyboo.net])
AC_CONFIG_SRCDIR([mtpass.cpp])
AC_CONFIG_HEADERS([config.h])
AC_CONFIG_FILES([Makefile])
AM_INIT_AUTOMAKE([foreign])
# Checks for programs.
AC_PROG_CXX
PKG_CHECK_MODULES([OPENSSL], [openssl])
# Checks for libraries.
# Checks for header files.
AC_CHECK_HEADERS([fcntl.h string.h unistd.h])
# Checks for typedefs, structures, and compiler characteristics.
AC_CHECK_HEADER_STDBOOL
# Checks for library functions.
AC_OUTPUT
================================================