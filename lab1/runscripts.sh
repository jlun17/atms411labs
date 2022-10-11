#!/usr/bin/bash
for i in {1..6..1}; 
do for p in {10..150..10};
do uvspec<UVSPEC_REPTRAN_THERMAL_cb"$i"_t"$p".INP>cb"$i"_"$p".out;
done;
done