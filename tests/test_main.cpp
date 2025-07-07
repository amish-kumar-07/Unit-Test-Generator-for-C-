#include <gtest/gtest.h>
#include <limits>

class AddTest : public ::testing::Test {
protected:
    int add(int a, int b) { return a + b; }
};

TEST_F(AddTest, BasicAddition) {
    EXPECT_EQ(5, add(2, 3));
}

TEST_F(AddTest, ZeroAddition) {
    EXPECT_EQ(3, add(3, 0));
    EXPECT_EQ(0, add(0, 0));
}

TEST_F(AddTest, NegativeNumbers) {
    EXPECT_EQ(-5, add(-2, -3));
    EXPECT_EQ(1, add(-2, 3));
}

TEST_F(AddTest, MixedSign) {
    EXPECT_EQ(0, add(5, -5));
    EXPECT_EQ(-1, add(2, -3));
}

TEST_F(AddTest, LargeIntegers) {
    EXPECT_EQ(std::numeric_limits<int>::max() - 1, add(std::numeric_limits<int>::max() - 2, 1));
    EXPECT_EQ(std::numeric_limits<int>::min() + 1, add(std::numeric_limits<int>::min() + 2, -1));
}

TEST_F(AddTest, OverflowBehavior) {
    // Warning: this triggers undefined behavior in C++ for signed overflow, test is just illustrative
    int result = add(std::numeric_limits<int>::max(), 1);
    // Don't assert on overflow directly — just print to validate manually
    std::cout << "Overflow result: " << result << std::endl;
}
