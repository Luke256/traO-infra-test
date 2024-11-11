#include <cstdint>
using namespace std;

#ifndef MX_LOG
#define MX_LOG 24
#endif

const uint32_t n = 1 << 27, mx = 1 << MX_LOG, mask = mx - 1;
char a[mx];
int main() {
    for (uint32_t t = 0, i = 16; t < n; t++, (i *= 5) &= mask) {
        a[i]++;
    }
}