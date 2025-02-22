import unittest
import sys
sys.path.append("..")
import copy
from problem_5.p5 import cookies_distrubution_map

class TestProblem5(unittest.TestCase):
    ### Public tests
    def test_correctness_public_n2_split(self):
        """Public test #1 n = 2"""
        route = cookies_distrubution_map([(1,2), (2, 1)])
        self.assertEqual({((1,1), (1,2)), ((1,1), (2,1))}, set(route))

    def test_correctness_public_n2_sequential(self):
        """Public test #2 n = 2"""
        route = cookies_distrubution_map([(1,2), (1, 5)])
        self.assertEqual({((1,1), (1,2)), ((1,2), (1,5))}, set(route))

    def test_correctness_public_n3_tie(self):
        """Public test n = 3"""
        route = cookies_distrubution_map([(1, 1), (1,2), (2, 1)])
        self.assertEqual({((2, 2), (1, 2)), ((1, 2), (1, 1)), ((1, 1), (2, 1))}, set(route))

    def test_correctness_public_n4_sequential(self):
        """Public test #1 n = 4"""
        route = cookies_distrubution_map([(1, 1), (3, 3), (4, 4), (5, 5)])
        self.assertEqual({((2, 2), (1, 1)), ((2, 2), (3, 3)), ((3, 3), (4, 4)), ((4, 4), (5, 5))}, set(route))

    def test_correctness_public_n4_split(self):
        """Public test #2 n = 4"""
        route = cookies_distrubution_map([(1, 5), (2, 5), (1, 7), (6, 1)])
        self.assertEqual({((2, 2), (2, 5)), ((2, 5), (1, 5)), ((1, 5), (1, 7)), ((2, 2), (6, 1))}, set(route))

    def test_correctess_public_n6(self):
        """Public test n = 6"""
        route = cookies_distrubution_map([(1,4), (5, 1), (5, 5), (5, 4), (3, 2), (6, 4)])
        self.assertTrue(set(route) == {((3, 3), (3, 2)), ((3, 2), (5, 1)), ((3, 3), (1, 4)), ((5, 1), (5, 4)), ((5, 4), (5, 5)), ((5, 4), (6, 4))} \
            or set(route) == {((3, 3), (3, 2)), ((3, 2), (5, 1)), ((3, 3), (1, 4)), ((3, 3), (5, 4)), ((5, 4), (5, 5)), ((5, 4), (6, 4))})

    def test_correctess_n10_1(self):
        """Test #1 n = 10"""
        inputs = [(348, 583), (587, 193), (193, 843), (17, 302), (53, 386), (637, 99), (714, 800), (81, 601), (380, 848), (195, 215)]
        ori_inputs = copy.deepcopy(inputs) # avoid altered inputs
        route = cookies_distrubution_map(inputs)
        self.assertEqual(10, len(route))

        for apt in ori_inputs:
            cookies_delivered = False
            for walk in route:
                if walk[1] == apt:
                    cookies_delivered = True
            self.assertTrue(cookies_delivered)

        steps = 0
        for walk in route:
            steps += abs(walk[0][0] - walk[1][0]) + abs(walk[0][1]-walk[1][1])
        self.assertEqual(2651, steps)

    def test_correctess_n10_2(self):
        """Test #2 n = 10"""
        inputs = [(962, 721), (763, 560), (708, 923), (427, 236), (41, 87), (892, 47), (584, 873), (146, 615), (183, 163), (314, 795)]
        ori_inputs = copy.deepcopy(inputs) # avoid altered inputs
        route = cookies_distrubution_map(inputs)
        self.assertEqual(10, len(route))

        for apt in ori_inputs:
            cookies_delivered = False
            for walk in route:
                if walk[1] == apt:
                    cookies_delivered = True
            self.assertTrue(cookies_delivered)

        steps = 0
        for walk in route:
            steps += abs(walk[0][0] - walk[1][0]) + abs(walk[0][1]-walk[1][1])
        self.assertEqual(3432, steps)

    def test_correctess_n10_3(self):
        """Test #3 n = 10"""
        inputs = [(120, 939), (748, 977), (551, 762), (432, 8), (67, 380), (124, 993), (70, 757), (861, 781), (814, 81), (95, 908)]
        ori_inputs = copy.deepcopy(inputs) # avoid altered inputs
        route = cookies_distrubution_map(inputs)
        self.assertEqual(10, len(route))

        for apt in ori_inputs:
            cookies_delivered = False
            for walk in route:
                if walk[1] == apt:
                    cookies_delivered = True
            self.assertTrue(cookies_delivered)

        steps = 0
        for walk in route:
            steps += abs(walk[0][0] - walk[1][0]) + abs(walk[0][1]-walk[1][1])
        self.assertEqual(3116, steps)

    def test_correctess_n10_4(self):
        """Test #4 n = 10"""
        inputs = [(691, 399), (968, 764), (111, 562), (214, 997), (355, 82), (167, 440), (37, 130), (255, 547), (775, 844), (788, 454)]
        ori_inputs = copy.deepcopy(inputs) # avoid altered inputs
        route = cookies_distrubution_map(inputs)
        self.assertEqual(10, len(route))

        for apt in ori_inputs:
            cookies_delivered = False
            for walk in route:
                if walk[1] == apt:
                    cookies_delivered = True
            self.assertTrue(cookies_delivered)

        steps = 0
        for walk in route:
            steps += abs(walk[0][0] - walk[1][0]) + abs(walk[0][1]-walk[1][1])
        self.assertEqual(3184, steps)
    
    def test_correctess_n100_1(self):
        """Test #1 n = 100"""
        inputs = [(305, 550), (291, 459), (396, 316), (919, 67), (341, 691), (14, 241), (867, 38), (16, 214), (429, 523), (528, 590), (183, 693), (186, 17), (322, 497), (920, 851), (210, 719), (100, 606), (24, 467), (830, 396), (883, 585), (743, 819), (570, 756), (106, 374), (475, 238), (59, 299), (218, 917), (994, 12), (493, 276), (132, 459), (907, 446), (977, 172), (853, 127), (919, 521), (911, 700), (5, 393), (853, 804), (729, 915), (160, 340), (33, 92), (135, 359), (242, 104), (393, 264), (234, 36), (89, 563), (781, 80), (123, 595), (265, 151), (918, 796), (278, 218), (829, 940), (750, 165), (823, 27), (80, 718), (519, 826), (945, 86), (281, 552), (604, 513), (442, 570), (115, 56), (114, 414), (67, 46), (426, 775), (147, 438), (715, 938), (741, 749), (308, 730), (16, 665), (335, 274), (524, 845), (347, 41), (350, 345), (295, 766), (916, 155), (157, 844), (525, 270), (131, 407), (116, 62), (455, 568), (942, 750), (241, 477), (334, 223), (706, 943), (918, 48), (378, 839), (172, 880), (864, 397), (425, 218), (31, 642), (31, 889), (966, 17), (458, 431), (184, 128), (744, 971), (689, 172), (693, 206), (859, 729), (910, 588), (535, 208), (956, 582), (999, 461), (914, 658)]
        ori_inputs = copy.deepcopy(inputs) # avoid altered inputs
        route = cookies_distrubution_map(inputs)
        self.assertEqual(100, len(route))

        for apt in ori_inputs:
            cookies_delivered = False
            for walk in route:
                if walk[1] == apt:
                    cookies_delivered = True
            self.assertTrue(cookies_delivered)

        steps = 0
        for walk in route:
            steps += abs(walk[0][0] - walk[1][0]) + abs(walk[0][1]-walk[1][1])
        self.assertEqual(7765, steps)

    def test_correctess_n100_2(self):
        """Test #2 n = 100"""
        inputs = [(446, 409), (146, 578), (450, 315), (915, 616), (129, 857), (427, 285), (527, 436), (809, 961), (821, 816), (477, 798), (367, 228), (513, 837), (360, 295), (59, 850), (170, 656), (368, 140), (447, 894), (188, 801), (308, 52), (786, 469), (87, 697), (232, 32), (301, 113), (52, 894), (376, 308), (610, 539), (469, 627), (952, 150), (204, 73), (359, 676), (894, 483), (13, 78), (911, 115), (856, 755), (228, 832), (117, 336), (910, 875), (440, 303), (404, 646), (968, 651), (640, 202), (36, 63), (264, 308), (545, 779), (359, 369), (272, 831), (128, 530), (301, 156), (723, 114), (647, 210), (16, 371), (529, 291), (17, 772), (979, 985), (569, 601), (141, 633), (549, 40), (608, 593), (977, 670), (472, 470), (336, 634), (876, 218), (24, 688), (37, 969), (131, 286), (857, 195), (177, 680), (828, 525), (682, 654), (776, 716), (729, 677), (484, 28), (687, 323), (603, 354), (963, 880), (431, 473), (195, 254), (457, 565), (802, 975), (779, 24), (457, 574), (574, 851), (495, 112), (665, 642), (731, 743), (71, 962), (267, 107), (625, 910), (467, 299), (803, 4), (374, 318), (310, 861), (872, 613), (300, 869), (318, 368), (308, 519), (678, 82), (102, 743), (138, 620), (900, 558)]
        ori_inputs = copy.deepcopy(inputs) # avoid altered inputs
        route = cookies_distrubution_map(inputs)
        self.assertEqual(100, len(route))

        for apt in ori_inputs:
            cookies_delivered = False
            for walk in route:
                if walk[1] == apt:
                    cookies_delivered = True
            self.assertTrue(cookies_delivered)

        steps = 0
        for walk in route:
            steps += abs(walk[0][0] - walk[1][0]) + abs(walk[0][1]-walk[1][1])
        self.assertEqual(8205, steps)

    def test_correctess_n100_3(self):
        """Test #3 n = 100"""
        inputs = [(684, 717), (544, 502), (861, 715), (714, 919), (371, 278), (979, 725), (953, 999), (18, 300), (923, 16), (650, 171), (84, 141), (876, 50), (792, 474), (648, 579), (426, 344), (575, 76), (37, 584), (332, 98), (172, 927), (170, 356), (537, 195), (674, 984), (250, 968), (613, 309), (683, 663), (341, 887), (525, 687), (436, 996), (490, 311), (723, 592), (222, 377), (419, 589), (880, 438), (626, 238), (904, 173), (933, 218), (50, 298), (814, 246), (925, 381), (474, 991), (140, 136), (170, 662), (274, 289), (666, 276), (890, 869), (33, 147), (664, 407), (463, 664), (844, 438), (901, 618), (761, 531), (266, 427), (134, 836), (598, 79), (143, 859), (108, 371), (123, 844), (554, 448), (400, 518), (878, 862), (441, 592), (997, 44), (219, 1000), (856, 471), (551, 406), (435, 557), (822, 759), (530, 877), (656, 738), (722, 793), (861, 96), (713, 88), (959, 403), (305, 315), (723, 794), (305, 324), (302, 236), (878, 75), (148, 34), (974, 805), (438, 90), (132, 810), (927, 28), (10, 722), (10, 667), (567, 377), (661, 820), (267, 555), (254, 118), (209, 150), (201, 201), (812, 690), (289, 603), (499, 68), (744, 573), (636, 695), (47, 990), (628, 90), (988, 15), (523, 217)]

        ori_inputs = copy.deepcopy(inputs) # avoid altered inputs
        route = cookies_distrubution_map(inputs)
        self.assertEqual(100, len(route))

        for apt in ori_inputs:
            cookies_delivered = False
            for walk in route:
                if walk[1] == apt:
                    cookies_delivered = True
            self.assertTrue(cookies_delivered)

        steps = 0
        for walk in route:
            steps += abs(walk[0][0] - walk[1][0]) + abs(walk[0][1]-walk[1][1])
        self.assertEqual(8745, steps)

    def test_correctess_n1000_1(self):
        """Test #1 n = 1000"""
        inputs = [(574, 146), (901, 779), (684, 363), (495, 347), (597, 889), (524, 401), (635, 98), (102, 937), (132, 133), (359, 450), (223, 580), (107, 396), (258, 794), (256, 586), (327, 399), (937, 835), (620, 890), (147, 14), (567, 884), (545, 707), (402, 905), (40, 580), (185, 580), (794, 145), (247, 412), (686, 444), (35, 483), (468, 231), (285, 905), (827, 569), (377, 94), (502, 354), (334, 398), (983, 816), (67, 948), (423, 70), (897, 911), (828, 375), (616, 385), (179, 860), (169, 977), (301, 468), (717, 535), (90, 931), (501, 175), (642, 779), (673, 92), (883, 567), (57, 525), (573, 679), (717, 791), (180, 861), (288, 812), (693, 452), (899, 938), (782, 264), (257, 290), (150, 600), (124, 700), (449, 82), (604, 770), (968, 409), (110, 536), (52, 522), (418, 280), (683, 434), (177, 571), (451, 960), (199, 330), (19, 372), (808, 950), (828, 779), (164, 610), (733, 529), (260, 834), (148, 504), (248, 451), (453, 731), (497, 527), (250, 3), (418, 383), (319, 520), (214, 476), (816, 154), (861, 305), (429, 648), (722, 483), (96, 368), (720, 940), (531, 296), (646, 344), (739, 810), (184, 835), (828, 244), (459, 774), (44, 257), (196, 809), (90, 800), (891, 687), (725, 902), (855, 374), (290, 745), (265, 243), (607, 272), (740, 774), (671, 693), (727, 701), (899, 807), (913, 464), (159, 518), (603, 894), (589, 102), (981, 855), (785, 553), (503, 300), (701, 819), (734, 578), (112, 851), (607, 128), (111, 706), (151, 275), (494, 596), (783, 708), (971, 679), (906, 470), (894, 743), (636, 182), (885, 774), (590, 740), (79, 939), (743, 25), (953, 383), (247, 761), (243, 861), (748, 387), (648, 34), (553, 440), (521, 497), (804, 440), (104, 950), (459, 104), (668, 763), (998, 827), (328, 349), (907, 105), (139, 422), (261, 30), (288, 222), (477, 557), (921, 314), (147, 282), (851, 493), (292, 139), (350, 974), (57, 730), (806, 607), (650, 768), (696, 735), (762, 15), (866, 719), (783, 474), (833, 304), (259, 465), (24, 580), (811, 56), (152, 329), (902, 696), (719, 565), (379, 893), (425, 771), (518, 432), (573, 758), (404, 181), (811, 797), (284, 512), (108, 39), (167, 503), (190, 895), (801, 631), (935, 482), (153, 190), (55, 414), (547, 980), (819, 127), (961, 458), (308, 51), (602, 31), (388, 169), (831, 528), (161, 944), (316, 311), (560, 937), (974, 558), (320, 699), (712, 418), (972, 634), (288, 774), (798, 607), (325, 396), (159, 611), (122, 216), (941, 646), (190, 598), (353, 67), (330, 349), (536, 835), (640, 407), (661, 866), (428, 753), (629, 505), (1000, 570), (764, 559), (73, 287), (316, 859), (627, 343), (12, 466), (874, 830), (115, 549), (598, 10), (17, 172), (572, 812), (721, 526), (3, 475), (129, 889), (617, 307), (600, 474), (393, 688), (604, 862), (267, 948), (896, 872), (595, 377), (73, 161), (986, 784), (754, 550), (409, 394), (594, 421), (167, 363), (283, 803), (616, 198), (643, 957), (980, 313), (478, 493), (189, 628), (321, 924), (585, 485), (567, 836), (753, 688), (837, 431), (785, 241), (21, 501), (389, 12), (220, 54), (562, 83), (665, 822), (213, 451), (508, 786), (735, 676), (66, 917), (635, 836), (497, 228), (514, 537), (309, 833), (292, 991), (597, 980), (978, 653), (755, 999), (4, 295), (205, 712), (259, 832), (833, 15), (993, 153), (909, 419), (404, 512), (509, 714), (914, 354), (629, 630), (282, 168), (177, 640), (454, 122), (19, 688), (85, 157), (73, 668), (796, 236), (209, 705), (596, 309), (281, 553), (315, 466), (918, 625), (411, 839), (217, 834), (469, 771), (251, 329), (816, 726), (948, 406), (656, 872), (823, 393), (945, 727), (574, 155), (834, 658), (819, 368), (183, 953), (422, 808), (591, 262), (954, 174), (995, 175), (520, 71), (392, 300), (598, 786), (488, 524), (37, 588), (941, 878), (807, 887), (134, 121), (649, 221), (316, 408), (864, 402), (698, 617), (896, 574), (386, 85), (487, 653), (304, 43), (15, 596), (428, 585), (158, 999), (834, 617), (950, 581), (533, 131), (545, 761), (20, 549), (15, 205), (936, 274), (962, 802), (37, 727), (216, 442), (922, 110), (335, 533), (768, 52), (902, 379), (92, 16), (799, 506), (621, 100), (741, 16), (493, 845), (315, 591), (757, 796), (739, 92), (949, 63), (448, 446), (467, 69), (353, 950), (965, 422), (730, 290), (317, 219), (482, 188), (564, 514), (818, 421), (543, 729), (580, 867), (159, 456), (188, 492), (197, 949), (108, 899), (764, 557), (309, 382), (900, 63), (895, 622), (444, 170), (477, 118), (245, 635), (739, 213), (661, 940), (808, 56), (707, 162), (547, 973), (110, 846), (580, 314), (478, 693), (715, 529), (706, 319), (361, 28), (486, 953), (851, 557), (379, 171), (222, 605), (366, 628), (990, 105), (328, 763), (861, 94), (692, 402), (719, 755), (628, 637), (304, 177), (860, 889), (581, 809), (807, 230), (111, 792), (957, 156), (351, 383), (623, 805), (656, 848), (701, 761), (949, 170), (906, 614), (712, 999), (918, 439), (439, 999), (96, 925), (731, 869), (715, 259), (368, 310), (531, 862), (155, 175), (98, 458), (986, 103), (286, 756), (734, 794), (609, 772), (280, 215), (814, 494), (44, 594), (204, 305), (401, 999), (993, 218), (87, 156), (518, 599), (665, 541), (802, 138), (794, 939), (213, 637), (365, 20), (241, 488), (737, 148), (995, 672), (728, 984), (232, 897), (174, 974), (593, 787), (854, 175), (549, 195), (723, 268), (373, 765), (750, 850), (742, 101), (509, 415), (474, 686), (821, 254), (218, 104), (185, 821), (405, 861), (948, 215), (148, 274), (606, 860), (55, 720), (526, 998), (274, 130), (843, 534), (405, 717), (784, 219), (172, 329), (752, 434), (773, 466), (32, 602), (675, 559), (668, 947), (62, 472), (14, 157), (151, 571), (234, 426), (914, 432), (575, 737), (249, 963), (725, 663), (579, 618), (682, 463), (741, 787), (9, 362), (917, 604), (846, 562), (608, 532), (626, 806), (122, 778), (897, 882), (237, 625), (862, 924), (407, 371), (668, 830), (980, 13), (232, 101), (302, 992), (570, 505), (791, 235), (16, 733), (51, 98), (159, 800), (254, 543), (113, 275), (28, 60), (944, 450), (699, 8), (827, 441), (845, 965), (219, 850), (58, 88), (889, 16), (633, 566), (516, 417), (974, 212), (972, 41), (633, 813), (252, 627), (31, 250), (772, 352), (193, 550), (725, 667), (552, 339), (580, 685), (336, 724), (625, 836), (705, 716), (487, 466), (547, 279), (939, 385), (199, 575), (884, 22), (86, 51), (974, 315), (547, 108), (305, 355), (951, 350), (790, 414), (441, 108), (658, 631), (598, 64), (79, 21), (253, 146), (771, 419), (42, 219), (658, 878), (332, 875), (598, 747), (696, 87), (64, 139), (399, 120), (606, 41), (969, 758), (54, 211), (927, 761), (782, 266), (395, 522), (69, 757), (731, 993), (862, 393), (453, 621), (712, 305), (311, 537), (390, 25), (748, 246), (218, 80), (519, 813), (384, 378), (900, 105), (85, 63), (740, 125), (362, 210), (263, 88), (406, 792), (522, 833), (195, 200), (944, 831), (514, 353), (222, 324), (532, 886), (174, 662), (468, 969), (916, 979), (54, 853), (851, 114), (504, 168), (844, 493), (296, 386), (513, 482), (606, 292), (863, 335), (607, 418), (49, 783), (437, 263), (153, 166), (413, 809), (865, 143), (610, 936), (858, 256), (614, 808), (707, 770), (699, 101), (339, 612), (753, 81), (553, 294), (996, 226), (153, 202), (379, 505), (505, 492), (895, 3), (753, 346), (477, 402), (358, 311), (362, 461), (324, 596), (492, 171), (211, 310), (290, 603), (474, 284), (262, 859), (431, 551), (544, 846), (876, 35), (620, 347), (396, 441), (959, 51), (323, 618), (872, 797), (368, 141), (768, 102), (274, 851), (295, 636), (527, 295), (200, 404), (143, 925), (868, 683), (5, 317), (28, 557), (744, 638), (689, 312), (238, 278), (748, 636), (728, 303), (681, 457), (462, 907), (412, 183), (897, 835), (828, 726), (431, 672), (179, 79), (33, 928), (960, 784), (574, 65), (102, 115), (677, 432), (777, 946), (356, 925), (557, 677), (875, 825), (420, 272), (337, 921), (226, 187), (551, 472), (179, 591), (286, 61), (992, 196), (495, 720), (742, 579), (49, 234), (565, 617), (486, 473), (632, 945), (454, 777), (142, 282), (833, 50), (718, 487), (947, 975), (714, 108), (802, 319), (280, 14), (110, 469), (743, 251), (747, 123), (745, 342), (572, 42), (313, 685), (230, 916), (353, 501), (456, 724), (962, 465), (182, 619), (451, 902), (635, 583), (618, 512), (631, 204), (636, 282), (30, 750), (36, 821), (637, 107), (218, 532), (408, 711), (329, 656), (551, 867), (815, 293), (749, 595), (264, 419), (855, 613), (537, 285), (4, 963), (256, 662), (880, 944), (348, 278), (892, 113), (101, 895), (313, 168), (571, 283), (460, 205), (16, 546), (620, 175), (940, 958), (486, 104), (566, 878), (555, 878), (39, 696), (387, 238), (3, 630), (502, 942), (370, 832), (32, 437), (808, 231), (590, 408), (779, 195), (208, 114), (108, 265), (796, 275), (943, 56), (684, 708), (276, 654), (534, 513), (990, 662), (161, 685), (393, 928), (955, 951), (326, 600), (730, 186), (667, 237), (442, 802), (136, 341), (623, 221), (171, 70), (389, 567), (782, 632), (747, 513), (147, 777), (125, 448), (612, 706), (550, 255), (468, 55), (311, 211), (37, 753), (159, 599), (552, 435), (570, 331), (965, 601), (829, 829), (458, 913), (352, 993), (40, 925), (558, 860), (937, 600), (544, 31), (767, 863), (271, 31), (419, 256), (271, 934), (696, 165), (485, 476), (159, 235), (735, 669), (281, 987), (43, 679), (431, 248), (333, 378), (13, 913), (961, 850), (916, 433), (173, 398), (197, 328), (349, 880), (486, 440), (885, 473), (788, 522), (970, 562), (464, 300), (460, 824), (153, 20), (80, 426), (608, 582), (599, 991), (821, 964), (371, 755), (266, 473), (632, 530), (615, 459), (816, 360), (565, 211), (504, 619), (956, 609), (615, 706), (103, 424), (979, 494), (542, 731), (266, 82), (992, 711), (474, 358), (946, 564), (885, 594), (897, 559), (888, 492), (818, 415), (772, 964), (612, 984), (907, 87), (440, 701), (475, 668), (497, 836), (404, 150), (748, 863), (392, 154), (308, 182), (109, 220), (910, 98), (525, 525), (150, 657), (326, 990), (81, 548), (209, 325), (908, 335), (981, 167), (767, 961), (53, 962), (429, 566), (255, 548), (705, 766), (813, 201), (179, 171), (572, 651), (909, 245), (370, 525), (346, 415), (293, 421), (169, 791), (166, 466), (976, 173), (277, 324), (779, 809), (963, 490), (550, 92), (904, 175), (532, 294), (8, 47), (773, 259), (30, 712), (951, 683), (593, 975), (920, 439), (664, 599), (653, 184), (863, 570), (349, 178), (700, 36), (64, 454), (251, 308), (577, 948), (892, 295), (940, 619), (438, 799), (873, 718), (913, 9), (464, 281), (715, 680), (370, 237), (664, 217), (246, 467), (863, 664), (328, 2), (628, 541), (713, 100), (441, 962), (187, 399), (768, 701), (332, 399), (65, 284), (257, 881), (602, 745), (31, 389), (312, 915), (939, 668), (640, 771), (157, 803), (665, 953), (637, 455), (521, 33), (753, 657), (288, 158), (769, 382), (239, 27), (776, 668), (39, 667), (354, 679), (787, 817), (876, 337), (994, 976), (962, 251), (488, 350), (920, 7), (310, 999), (26, 575), (693, 499), (207, 745), (972, 966), (433, 441), (182, 670), (230, 756), (179, 534), (224, 914), (69, 384), (53, 705), (697, 389), (967, 640), (417, 591), (643, 903), (625, 867), (504, 568), (697, 227), (301, 654), (561, 217), (517, 943), (24, 98), (976, 325), (725, 316), (465, 905), (603, 299), (818, 135), (157, 380), (632, 771), (256, 84), (335, 804), (741, 269), (445, 545), (774, 28), (876, 94), (844, 538), (98, 330), (135, 468), (925, 764), (643, 786), (525, 910), (464, 183), (50, 110), (751, 566), (997, 231), (716, 370), (805, 555), (855, 156), (398, 289), (829, 265), (652, 480), (150, 233), (841, 895), (971, 596), (497, 277), (911, 182), (676, 428), (46, 688), (351, 906), (643, 251), (503, 100), (435, 45), (161, 736), (807, 600), (38, 275), (538, 85), (875, 237), (291, 464), (134, 81), (114, 651), (170, 183), (699, 923), (430, 259), (480, 89), (894, 125), (20, 653), (529, 103), (396, 266), (599, 427), (122, 26), (605, 269), (704, 620), (27, 768), (787, 654), (962, 515), (123, 363), (756, 294), (648, 831), (820, 696), (55, 713), (137, 374)]
        ori_inputs = copy.deepcopy(inputs) # avoid altered inputs
        route = cookies_distrubution_map(inputs)
        self.assertEqual(1000, len(route))

        for apt in ori_inputs:
            cookies_delivered = False
            for walk in route:
                if walk[1] == apt:
                    cookies_delivered = True
            self.assertTrue(cookies_delivered)

        steps = 0
        for walk in route:
            steps += abs(walk[0][0] - walk[1][0]) + abs(walk[0][1]-walk[1][1])
        self.assertEqual(25979, steps)

if __name__ == '__main__':
    unittest.main()