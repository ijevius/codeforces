#include <iostream>

int main() {
    long i;
    std::cin >> i;
    if (i%2==0 and i>2){
        std::cout << "YES" << std::endl;
        std::exit(0);
    }
    std::cout << "NO" << std::endl;
    return 0;
}
