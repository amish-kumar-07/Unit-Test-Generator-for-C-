cmake_minimum_required(VERSION 3.10)
project(MyAddTestProject)

set(CMAKE_CXX_STANDARD 17)
set(CMAKE_CXX_STANDARD_REQUIRED ON)

# Enable coverage flags if using GCC or Clang
option(CODE_COVERAGE "Enable coverage reporting" ON)
if(CODE_COVERAGE AND (CMAKE_CXX_COMPILER_ID MATCHES "GNU|Clang"))
    message(STATUS "Building with code coverage enabled")
    add_compile_options(-g -O0 --coverage)
    add_link_options(--coverage)
endif()

# Include directories
include_directories(include)

# Add GoogleTest (assumed to be cloned into third_party/googletest)
add_subdirectory(third_party/googletest)

# Optional: Main binary (your app)
add_executable(main_exec src/main.cpp)

# Unit test target
enable_testing()
add_executable(unit_tests tests/test_main.cpp)
target_link_libraries(unit_tests gtest gtest_main)
add_test(NAME run_unit_tests COMMAND unit_tests)
