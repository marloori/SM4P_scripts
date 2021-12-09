#include <stdio.h>
#include <gsl/gsl_rng.h>
#include "bootstrap.h"

int main(int argc, char** argv) {
  double data[3] = {0.5, 2.8, 4.1};
  struct sample test_sample;
  define_sample(test_sample, data);
  return 0;
}
