from kinetics import first_order, half_life_first
assert abs(first_order(1.0,0.1,half_life_first(0.1))-0.5)<1e-9
