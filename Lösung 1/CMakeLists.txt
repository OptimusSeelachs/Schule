cmake_minimum_required(VERSION 3.10)
project(MeinProjekt)

# Füge alle Quelldateien hinzu
add_executable(
    main
    main.cpp
    Widerstand.cpp
    Reihe.cpp
    Parallel.cpp
)