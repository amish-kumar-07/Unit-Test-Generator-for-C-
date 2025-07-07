# 🧪 C++ Unit Test Project – Google Test + CMake

This project demonstrates how to write and run unit tests for C++ using the [Google Test](https://github.com/google/googletest) framework and CMake. It includes optional code coverage reporting using `lcov`.

---

## 📁 Project Structure

```

.
├── CMakeLists.txt
├── src/
│   └── main.cpp
├── tests/
│   └── test_main.cpp
├── include/
├── third_party/
│   └── googletest/
└── README.md

````

---

## 🚀 Getting Started

### 1. Clone Google Test

```bash
git clone https://github.com/google/googletest.git third_party/googletest
````

---

### 2. Build the Project

```bash
mkdir build && cd build
cmake ..
cmake --build .
```

---

### 3. Run Unit Tests

```bash
ctest
# or
./unit_tests
```

---

## ✅ Sample Test Case

```cpp
TEST_F(AddTest, BasicAddition) {
    EXPECT_EQ(5, add(2, 3));
}
```

---

## 📊 Code Coverage (Optional)

### Enable coverage and generate report:

```bash
cmake -DCODE_COVERAGE=ON ..
cmake --build .
./unit_tests

lcov --capture --directory . --output-file coverage.info
genhtml coverage.info --output-directory coverage-report
```

Open: `coverage-report/index.html` in your browser.

---

## 📸 Code Coverage Snapshot

![image](https://github.com/user-attachments/assets/be4b056c-82d4-462e-98f4-46d12fcc073c)

---

## 🛠 Requirements

* C++17 compiler (GCC, Clang, MSVC)
* CMake 3.10+
* Google Test
* lcov (optional, for coverage report)

---

## 📄 License

MIT License © 2025

```
