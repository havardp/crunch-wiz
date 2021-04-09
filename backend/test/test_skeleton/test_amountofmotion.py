from crunch.skeleton.measurements import *
import numpy as np
import sympy as sym

tol = 1e-5
t = sym.symbols("t")


def test_amount_of_motion():
    test_array = [
        [
            (682.33496, 147.34991),
            (682.3375, 221.9163),
            (633.3446, 219.936),
            (590.20074, 288.53638),
            (543.2431, 339.46716),
            (731.28143, 223.76894),
            (782.2003, 288.50427),
            (854.69196, 319.87338),
            (713.6236, 374.71902),
            (680.24756, 382.5819),
            (695.9468, 515.76013),
            (699.9767, 674.45215),
            (750.8297, 366.86813),
            (823.2922, 490.2449),
            (911.49255, 660.72504),
            (670.5192, 137.64388),
            (695.95966, 133.82387),
            (654.8586, 159.18672),
            (713.5559, 149.39342),
            (972.2261, 660.7364),
            (968.289, 654.838),
            (909.549, 670.5135),
            (701.86365, 695.99384),
            (684.2707, 695.9826),
            (711.66296, 682.26044),
        ]
    ]
    [
        [
            (682.33496, 147.34991),
            (682.3375, 221.9163),
            (633.3446, 219.936),
            (590.20074, 288.53638),
            (543.2431, 339.46716),
            (731.28143, 223.76894),
            (782.2003, 288.50427),
            (854.69196, 319.87338),
            (713.6236, 374.71902),
            (680.24756, 382.5819),
            (695.9468, 515.76013),
            (699.9767, 674.45215),
            (750.8297, 366.86813),
            (823.2922, 490.2449),
            (911.49255, 660.72504),
            (670.5192, 137.64388),
            (695.95966, 133.82387),
            (654.8586, 159.18672),
            (713.5559, 149.39342),
            (972.2261, 660.7364),
            (968.289, 654.838),
            (909.549, 670.5135),
            (701.86365, 695.99384),
            (684.2707, 695.9826),
            (711.66296, 682.26044),
        ],
        [
            (682.32196, 147.32697),
            (682.37933, 223.77818),
            (635.20264, 219.95241),
            (590.18097, 288.5138),
            (543.2333, 339.44467),
            (731.30066, 223.78987),
            (782.2095, 288.52475),
            (854.7103, 319.9099),
            (713.5855, 374.66687),
            (680.218, 382.53506),
            (695.9048, 511.88055),
            (699.98126, 674.4231),
            (748.9264, 366.82184),
            (823.27167, 488.33722),
            (903.7147, 654.83356),
            (670.5175, 137.61668),
            (695.9638, 135.63985),
            (654.85956, 157.2625),
            (713.5377, 149.47784),
            (964.42255, 680.36206),
            (964.4108, 676.37195),
            (903.6723, 666.64746),
            (705.803, 695.9702),
            (686.23456, 695.9943),
            (711.62805, 682.27875),
        ],
    ]
    [
        [
            (682.33496, 147.34991),
            (682.3375, 221.9163),
            (633.3446, 219.936),
            (590.20074, 288.53638),
            (543.2431, 339.46716),
            (731.28143, 223.76894),
            (782.2003, 288.50427),
            (854.69196, 319.87338),
            (713.6236, 374.71902),
            (680.24756, 382.5819),
            (695.9468, 515.76013),
            (699.9767, 674.45215),
            (750.8297, 366.86813),
            (823.2922, 490.2449),
            (911.49255, 660.72504),
            (670.5192, 137.64388),
            (695.95966, 133.82387),
            (654.8586, 159.18672),
            (713.5559, 149.39342),
            (972.2261, 660.7364),
            (968.289, 654.838),
            (909.549, 670.5135),
            (701.86365, 695.99384),
            (684.2707, 695.9826),
            (711.66296, 682.26044),
        ],
        [
            (682.32196, 147.32697),
            (682.37933, 223.77818),
            (635.20264, 219.95241),
            (590.18097, 288.5138),
            (543.2333, 339.44467),
            (731.30066, 223.78987),
            (782.2095, 288.52475),
            (854.7103, 319.9099),
            (713.5855, 374.66687),
            (680.218, 382.53506),
            (695.9048, 511.88055),
            (699.98126, 674.4231),
            (748.9264, 366.82184),
            (823.27167, 488.33722),
            (903.7147, 654.83356),
            (670.5175, 137.61668),
            (695.9638, 135.63985),
            (654.85956, 157.2625),
            (713.5377, 149.47784),
            (964.42255, 680.36206),
            (964.4108, 676.37195),
            (903.6723, 666.64746),
            (705.803, 695.9702),
            (686.23456, 695.9943),
            (711.62805, 682.27875),
        ],
        [
            (682.2949, 147.3435),
            (682.34357, 221.86922),
            (633.3605, 219.89241),
            (590.2042, 288.4968),
            (545.1113, 337.5613),
            (731.2446, 221.90453),
            (780.2058, 288.44302),
            (854.67523, 321.7081),
            (713.55206, 370.80667),
            (678.3928, 382.4517),
            (695.94214, 511.81418),
            (699.9454, 678.36847),
            (746.9888, 364.86713),
            (821.33875, 482.46866),
            (913.47003, 664.58844),
            (668.63306, 137.6163),
            (695.94275, 135.65166),
            (654.8237, 157.2173),
            (711.7333, 149.46877),
            (968.33075, 680.3211),
            (968.28235, 674.4384),
            (913.4451, 674.4194),
            (697.9267, 697.9952),
            (682.2805, 697.91833),
            (711.6182, 684.2686),
        ],
    ]
    [
        [
            (682.33496, 147.34991),
            (682.3375, 221.9163),
            (633.3446, 219.936),
            (590.20074, 288.53638),
            (543.2431, 339.46716),
            (731.28143, 223.76894),
            (782.2003, 288.50427),
            (854.69196, 319.87338),
            (713.6236, 374.71902),
            (680.24756, 382.5819),
            (695.9468, 515.76013),
            (699.9767, 674.45215),
            (750.8297, 366.86813),
            (823.2922, 490.2449),
            (911.49255, 660.72504),
            (670.5192, 137.64388),
            (695.95966, 133.82387),
            (654.8586, 159.18672),
            (713.5559, 149.39342),
            (972.2261, 660.7364),
            (968.289, 654.838),
            (909.549, 670.5135),
            (701.86365, 695.99384),
            (684.2707, 695.9826),
            (711.66296, 682.26044),
        ],
        [
            (682.32196, 147.32697),
            (682.37933, 223.77818),
            (635.20264, 219.95241),
            (590.18097, 288.5138),
            (543.2333, 339.44467),
            (731.30066, 223.78987),
            (782.2095, 288.52475),
            (854.7103, 319.9099),
            (713.5855, 374.66687),
            (680.218, 382.53506),
            (695.9048, 511.88055),
            (699.98126, 674.4231),
            (748.9264, 366.82184),
            (823.27167, 488.33722),
            (903.7147, 654.83356),
            (670.5175, 137.61668),
            (695.9638, 135.63985),
            (654.85956, 157.2625),
            (713.5377, 149.47784),
            (964.42255, 680.36206),
            (964.4108, 676.37195),
            (903.6723, 666.64746),
            (705.803, 695.9702),
            (686.23456, 695.9943),
            (711.62805, 682.27875),
        ],
        [
            (682.2949, 147.3435),
            (682.34357, 221.86922),
            (633.3605, 219.89241),
            (590.2042, 288.4968),
            (545.1113, 337.5613),
            (731.2446, 221.90453),
            (780.2058, 288.44302),
            (854.67523, 321.7081),
            (713.55206, 370.80667),
            (678.3928, 382.4517),
            (695.94214, 511.81418),
            (699.9454, 678.36847),
            (746.9888, 364.86713),
            (821.33875, 482.46866),
            (913.47003, 664.58844),
            (668.63306, 137.6163),
            (695.94275, 135.65166),
            (654.8237, 157.2173),
            (711.7333, 149.46877),
            (968.33075, 680.3211),
            (968.28235, 674.4384),
            (913.4451, 674.4194),
            (697.9267, 697.9952),
            (682.2805, 697.91833),
            (711.6182, 684.2686),
        ],
        [
            (682.28455, 147.36288),
            (682.30884, 223.81573),
            (633.2994, 221.91037),
            (588.3215, 290.38446),
            (543.18884, 339.4423),
            (731.22687, 223.80797),
            (780.2758, 288.49133),
            (854.7316, 321.74393),
            (713.6055, 376.63275),
            (680.22766, 384.4439),
            (695.94666, 515.76544),
            (699.97284, 680.32587),
            (750.81165, 366.88293),
            (823.2598, 490.29218),
            (909.5341, 662.63544),
            (670.489, 137.62234),
            (695.9292, 135.673),
            (654.8597, 153.35454),
            (711.7385, 149.43486),
            (964.35156, 680.3367),
            (962.42847, 674.4401),
            (907.59357, 674.4372),
            (705.7662, 698.0062),
            (684.28345, 697.9999),
            (709.6974, 686.2256),
        ],
    ]
    [
        [
            (682.33496, 147.34991),
            (682.3375, 221.9163),
            (633.3446, 219.936),
            (590.20074, 288.53638),
            (543.2431, 339.46716),
            (731.28143, 223.76894),
            (782.2003, 288.50427),
            (854.69196, 319.87338),
            (713.6236, 374.71902),
            (680.24756, 382.5819),
            (695.9468, 515.76013),
            (699.9767, 674.45215),
            (750.8297, 366.86813),
            (823.2922, 490.2449),
            (911.49255, 660.72504),
            (670.5192, 137.64388),
            (695.95966, 133.82387),
            (654.8586, 159.18672),
            (713.5559, 149.39342),
            (972.2261, 660.7364),
            (968.289, 654.838),
            (909.549, 670.5135),
            (701.86365, 695.99384),
            (684.2707, 695.9826),
            (711.66296, 682.26044),
        ],
        [
            (682.32196, 147.32697),
            (682.37933, 223.77818),
            (635.20264, 219.95241),
            (590.18097, 288.5138),
            (543.2333, 339.44467),
            (731.30066, 223.78987),
            (782.2095, 288.52475),
            (854.7103, 319.9099),
            (713.5855, 374.66687),
            (680.218, 382.53506),
            (695.9048, 511.88055),
            (699.98126, 674.4231),
            (748.9264, 366.82184),
            (823.27167, 488.33722),
            (903.7147, 654.83356),
            (670.5175, 137.61668),
            (695.9638, 135.63985),
            (654.85956, 157.2625),
            (713.5377, 149.47784),
            (964.42255, 680.36206),
            (964.4108, 676.37195),
            (903.6723, 666.64746),
            (705.803, 695.9702),
            (686.23456, 695.9943),
            (711.62805, 682.27875),
        ],
        [
            (682.2949, 147.3435),
            (682.34357, 221.86922),
            (633.3605, 219.89241),
            (590.2042, 288.4968),
            (545.1113, 337.5613),
            (731.2446, 221.90453),
            (780.2058, 288.44302),
            (854.67523, 321.7081),
            (713.55206, 370.80667),
            (678.3928, 382.4517),
            (695.94214, 511.81418),
            (699.9454, 678.36847),
            (746.9888, 364.86713),
            (821.33875, 482.46866),
            (913.47003, 664.58844),
            (668.63306, 137.6163),
            (695.94275, 135.65166),
            (654.8237, 157.2173),
            (711.7333, 149.46877),
            (968.33075, 680.3211),
            (968.28235, 674.4384),
            (913.4451, 674.4194),
            (697.9267, 697.9952),
            (682.2805, 697.91833),
            (711.6182, 684.2686),
        ],
        [
            (682.28455, 147.36288),
            (682.30884, 223.81573),
            (633.2994, 221.91037),
            (588.3215, 290.38446),
            (543.18884, 339.4423),
            (731.22687, 223.80797),
            (780.2758, 288.49133),
            (854.7316, 321.74393),
            (713.6055, 376.63275),
            (680.22766, 384.4439),
            (695.94666, 515.76544),
            (699.97284, 680.32587),
            (750.81165, 366.88293),
            (823.2598, 490.29218),
            (909.5341, 662.63544),
            (670.489, 137.62234),
            (695.9292, 135.673),
            (654.8597, 153.35454),
            (711.7385, 149.43486),
            (964.35156, 680.3367),
            (962.42847, 674.4401),
            (907.59357, 674.4372),
            (705.7662, 698.0062),
            (684.28345, 697.9999),
            (709.6974, 686.2256),
        ],
        [
            (682.2757, 147.34175),
            (682.37384, 223.77084),
            (635.21967, 221.87141),
            (590.19885, 288.49597),
            (543.2002, 339.41116),
            (731.2291, 223.77487),
            (782.16473, 288.5279),
            (854.735, 321.79208),
            (713.59485, 376.6569),
            (680.2229, 384.46466),
            (695.9229, 517.6842),
            (699.96344, 682.2725),
            (748.91486, 366.8952),
            (823.2855, 490.29547),
            (903.6742, 652.9516),
            (670.509, 135.74841),
            (695.9256, 135.6739),
            (654.86414, 153.31128),
            (711.71375, 149.44438),
            (964.3381, 674.42285),
            (956.55945, 656.8116),
            (903.6889, 668.5606),
            (686.19086, 715.59143),
            (680.28796, 698.0564),
            (711.6293, 692.0558),
        ],
    ]
    # estimated = amount_of_motion(test_array)

    # print(estimated)
    """exact = 0.1544
    assert np.abs(round(estimated, 4) - exact) < tol """


test_amount_of_motion()