#include "frozen/set.h"

int main() {
  frozen::set<int, 2> olaf = {3, 4};
  return !olaf.count(3);
}
