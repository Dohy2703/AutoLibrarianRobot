
bk0 = '623398'  # 컴활 1급 실기
bk1 = '620123'  # 열전달
bk2 = '621121'  # 열역학
bk3 = '622432'  # 전기전자개론
bk4 = '625120'  # 재료역학 beer
bk5 = '623576'  # 토익
bk6 = '624875'  # 재료역학 gere
bk7 = '623908'  # 공학수학
bk8 = '625223'  # 기계설계
bk9 = '625327'  # 유체역학

books_model = {
    'd10_b1':{  # 10
        'p1':{'book':bk0},
        'p2':{'book':bk1},
        'p3':{'book':bk2},
        'p4': {'book': bk3},
        'p5': {'book': bk4},
        'p6': {'book': bk5},
        'p7': {'book': bk6},
        'p8': {'book': bk7},
        'p9': {'book': bk8},
        'p10':{'book':bk9}
    },
    'd10_b2': {  # 45, accum 55
        'p1': {'book1': bk0, 'book2':bk1},
        'p2': {'book1': bk0, 'book2': bk2},
        'p3': {'book1': bk0, 'book2': bk3},
        'p4': {'book1': bk0, 'book2': bk4},
        'p5': {'book1': bk0, 'book2': bk5},
        'p6': {'book1': bk0, 'book2': bk6},
        'p7': {'book1': bk0, 'book2': bk7},
        'p8': {'book1': bk0, 'book2': bk8},
        'p9': {'book1': bk0, 'book2': bk9},
        'p10': {'book1': bk1, 'book2': bk2},
        'p11': {'book1': bk1, 'book2': bk3},
        'p12': {'book1': bk1, 'book2': bk4},
        'p13': {'book1': bk1, 'book2': bk5},
        'p14': {'book1': bk1, 'book2': bk6},
        'p15': {'book1': bk1, 'book2': bk7},
        'p16': {'book1': bk1, 'book2': bk8},
        'p17': {'book1': bk1, 'book2': bk9},
        'p18': {'book1': bk2, 'book2': bk3},
        'p19': {'book1': bk2, 'book2': bk4},
        'p20': {'book1': bk2, 'book2': bk5},
        'p21': {'book1': bk2, 'book2': bk6},
        'p22': {'book1': bk2, 'book2': bk7},
        'p23': {'book1': bk2, 'book2': bk8},
        'p24': {'book1': bk2, 'book2': bk9},
        'p25': {'book1': bk3, 'book2': bk4},
        'p26': {'book1': bk3, 'book2': bk5},
        'p27': {'book1': bk3, 'book2': bk6},
        'p28': {'book1': bk3, 'book2': bk7},
        'p29': {'book1': bk3, 'book2': bk8},
        'p30': {'book1': bk3, 'book2': bk9},
        'p31': {'book1': bk4, 'book2': bk5},
        'p32': {'book1': bk4, 'book2': bk6},
        'p33': {'book1': bk4, 'book2': bk7},
        'p34': {'book1': bk4, 'book2': bk8},
        'p35': {'book1': bk4, 'book2': bk9},
        'p36': {'book1': bk5, 'book2': bk6},
        'p37': {'book1': bk5, 'book2': bk7},
        'p38': {'book1': bk5, 'book2': bk8},
        'p39': {'book1': bk5, 'book2': bk9},
        'p40': {'book1': bk6, 'book2': bk7},
        'p41': {'book1': bk6, 'book2': bk8},
        'p42': {'book1': bk6, 'book2': bk9},
        'p43': {'book1': bk7, 'book2': bk8},
        'p44': {'book1': bk7, 'book2': bk9},
        'p45': {'book1': bk8, 'book2': bk9}
    },
    'd10_b5_ang30':{  # 10  # accum 65
        'p1' : {'book1': bk0, 'book2': bk1, 'book3': bk2, 'book4': bk3, 'book5': bk4},
        'p2': {'book1': bk0, 'book2': bk1, 'book3': bk2, 'book4': bk3, 'book5': bk4},
        'p3': {'book1': bk0, 'book2': bk1, 'book3': bk2, 'book4': bk3, 'book5': bk4},
        'p4': {'book1': bk0, 'book2': bk1, 'book3': bk2, 'book4': bk3, 'book5': bk4},
        'p5': {'book1': bk0, 'book2': bk1, 'book3': bk2, 'book4': bk3, 'book5': bk4},
        'p6': {'book1': bk0, 'book2': bk1, 'book3': bk2, 'book4': bk3, 'book5': bk4},
        'p7': {'book1': bk0, 'book2': bk1, 'book3': bk2, 'book4': bk3, 'book5': bk4},
        'p8': {'book1': bk0, 'book2': bk1, 'book3': bk2, 'book4': bk3, 'book5': bk4},
        'p9': {'book1': bk0, 'book2': bk1, 'book3': bk2, 'book4': bk3, 'book5': bk4},
        'p10': {'book1': bk0, 'book2': bk1, 'book3': bk2, 'book4': bk3, 'book5': bk4}
    },
    'd10_b5_ang30_2':{  # 10  # accum 75
        'p1' : {'book1': bk5, 'book2': bk6, 'book3': bk7, 'book4': bk8, 'book5': bk9},
        'p2': {'book1': bk5, 'book2': bk6, 'book3': bk7, 'book4': bk8, 'book5': bk9},
        'p3': {'book1': bk5, 'book2': bk6, 'book3': bk7, 'book4': bk8, 'book5': bk9},
        'p4': {'book1': bk5, 'book2': bk6, 'book3': bk7, 'book4': bk8, 'book5': bk9},
        'p5': {'book1': bk5, 'book2': bk6, 'book3': bk7, 'book4': bk8, 'book5': bk9},
        'p6': {'book1': bk5, 'book2': bk6, 'book3': bk7, 'book4': bk8, 'book5': bk9},
        'p7': {'book1': bk5, 'book2': bk6, 'book3': bk7, 'book4': bk8, 'book5': bk9},
        'p8': {'book1': bk5, 'book2': bk6, 'book3': bk7, 'book4': bk8, 'book5': bk9},
        'p9': {'book1': bk5, 'book2': bk6, 'book3': bk7, 'book4': bk8, 'book5': bk9},
        'p10': {'book1': bk5, 'book2': bk6, 'book3': bk7, 'book4': bk8, 'book5': bk9}
    },
    'd10_b5_ang45':{  # 10  # accum 85
        'p1' : {'book1': bk0, 'book2': bk1, 'book3': bk2, 'book4': bk3, 'book5': bk4},
        'p2': {'book1': bk0, 'book2': bk1, 'book3': bk2, 'book4': bk3, 'book5': bk4},
        'p3': {'book1': bk0, 'book2': bk1, 'book3': bk2, 'book4': bk3, 'book5': bk4},
        'p4': {'book1': bk0, 'book2': bk1, 'book3': bk2, 'book4': bk3, 'book5': bk4},
        'p5': {'book1': bk0, 'book2': bk1, 'book3': bk2, 'book4': bk3, 'book5': bk4},
        'p6': {'book1': bk0, 'book2': bk1, 'book3': bk2, 'book4': bk3, 'book5': bk4},
        'p7': {'book1': bk0, 'book2': bk1, 'book3': bk2, 'book4': bk3, 'book5': bk4},
        'p8': {'book1': bk0, 'book2': bk1, 'book3': bk2, 'book4': bk3, 'book5': bk4},
        'p9': {'book1': bk0, 'book2': bk1, 'book3': bk2, 'book4': bk3, 'book5': bk4},
        'p10': {'book1': bk0, 'book2': bk1, 'book3': bk2, 'book4': bk3, 'book5': bk4}
    },
    'd10_b5_ang45_2':{  # 10  # accum 95
        'p1' : {'book1': bk5, 'book2': bk6, 'book3': bk7, 'book4': bk8, 'book5': bk9},
        'p2': {'book1': bk5, 'book2': bk6, 'book3': bk7, 'book4': bk8, 'book5': bk9},
        'p3': {'book1': bk5, 'book2': bk6, 'book3': bk7, 'book4': bk8, 'book5': bk9},
        'p4': {'book1': bk5, 'book2': bk6, 'book3': bk7, 'book4': bk8, 'book5': bk9},
        'p5': {'book1': bk5, 'book2': bk6, 'book3': bk7, 'book4': bk8, 'book5': bk9},
        'p6': {'book1': bk5, 'book2': bk6, 'book3': bk7, 'book4': bk8, 'book5': bk9},
        'p7': {'book1': bk5, 'book2': bk6, 'book3': bk7, 'book4': bk8, 'book5': bk9},
        'p8': {'book1': bk5, 'book2': bk6, 'book3': bk7, 'book4': bk8, 'book5': bk9},
        'p9': {'book1': bk5, 'book2': bk6, 'book3': bk7, 'book4': bk8, 'book5': bk9},
        'p10': {'book1': bk5, 'book2': bk6, 'book3': bk7, 'book4': bk8, 'book5': bk9}
    },
    'd15' : {  # 5  # accum 100
        'p1': {'book1': bk0, 'book2': bk1, 'book3': bk2, 'book4': bk3, 'book5': bk4},
        'p2': {'book1': bk0, 'book2': bk1, 'book3': bk2, 'book4': bk3, 'book5': bk4},
        'p3' : {'book1': bk5, 'book2': bk6, 'book3': bk7, 'book4': bk8, 'book5': bk9},
        'p4': {'book1': bk5, 'book2': bk6, 'book3': bk7, 'book4': bk8, 'book5': bk9},
        'p5' : {'book1': bk5, 'book2': bk6, 'book3': bk7, 'book4': bk8, 'book5': bk9}
    }
}

books_model2 = {
    '20_1':{  # 20cm distance
        'p1' : {'book1': bk0, 'book2': bk1, 'book3': bk2, 'book4': bk3, 'book5': bk4},
        'p2': {'book1': bk0, 'book2': bk1, 'book3': bk2, 'book4': bk3, 'book5': bk4},
        'p3': {'book1': bk0, 'book2': bk1, 'book3': bk2, 'book4': bk3, 'book5': bk4},
        'p4': {'book1': bk0, 'book2': bk1, 'book3': bk2, 'book4': bk3, 'book5': bk4},
        'p5': {'book1': bk0, 'book2': bk1, 'book3': bk2, 'book4': bk3, 'book5': bk4},
        'p6': {'book1': bk0, 'book2': bk1, 'book3': bk2, 'book4': bk3, 'book5': bk4},
        'p7': {'book1': bk0, 'book2': bk1, 'book3': bk2, 'book4': bk3, 'book5': bk4},
        'p8': {'book1': bk0, 'book2': bk1, 'book3': bk2, 'book4': bk3, 'book5': bk4},
        'p9': {'book1': bk0, 'book2': bk1, 'book3': bk2, 'book4': bk3, 'book5': bk4},
        'p10': {'book1': bk0, 'book2': bk1, 'book3': bk2, 'book4': bk3, 'book5': bk4},
        'p11': {'book1': bk0, 'book2': bk1, 'book3': bk2, 'book4': bk3, 'book5': bk4},
        'p12': {'book1': bk0, 'book2': bk1, 'book3': bk2, 'book4': bk3, 'book5': bk4},
        'p13': {'book1': bk0, 'book2': bk1, 'book3': bk2, 'book4': bk3, 'book5': bk4},
        'p14': {'book1': bk0, 'book2': bk1, 'book3': bk2, 'book4': bk3, 'book5': bk4},
        'p15': {'book1': bk0, 'book2': bk1, 'book3': bk2, 'book4': bk3, 'book5': bk4},
        'p16': {'book1': bk0, 'book2': bk1, 'book3': bk2, 'book4': bk3, 'book5': bk4},
        'p17': {'book1': bk0, 'book2': bk1, 'book3': bk2, 'book4': bk3, 'book5': bk4},
        'p18': {'book1': bk0, 'book2': bk1, 'book3': bk2, 'book4': bk3, 'book5': bk4},
        'p19': {'book1': bk0, 'book2': bk1, 'book3': bk2, 'book4': bk3, 'book5': bk4},
        'p20': {'book1': bk0, 'book2': bk1, 'book3': bk2, 'book4': bk3, 'book5': bk4}
    },
    '20_2':{  # 20  # accum 40
        'p1' : {'book1': bk5, 'book2': bk6, 'book3': bk7, 'book4': bk8, 'book5': bk9},
        'p2': {'book1': bk5, 'book2': bk6, 'book3': bk7, 'book4': bk8, 'book5': bk9},
        'p3': {'book1': bk5, 'book2': bk6, 'book3': bk7, 'book4': bk8, 'book5': bk9},
        'p4': {'book1': bk5, 'book2': bk6, 'book3': bk7, 'book4': bk8, 'book5': bk9},
        'p5': {'book1': bk5, 'book2': bk6, 'book3': bk7, 'book4': bk8, 'book5': bk9},
        'p6': {'book1': bk5, 'book2': bk6, 'book3': bk7, 'book4': bk8, 'book5': bk9},
        'p7': {'book1': bk5, 'book2': bk6, 'book3': bk7, 'book4': bk8, 'book5': bk9},
        'p8': {'book1': bk5, 'book2': bk6, 'book3': bk7, 'book4': bk8, 'book5': bk9},
        'p9': {'book1': bk5, 'book2': bk6, 'book3': bk7, 'book4': bk8, 'book5': bk9},
        'p10': {'book1': bk5, 'book2': bk6, 'book3': bk7, 'book4': bk8, 'book5': bk9},
        'p11': {'book1': bk5, 'book2': bk6, 'book3': bk7, 'book4': bk8, 'book5': bk9},
        'p12': {'book1': bk5, 'book2': bk6, 'book3': bk7, 'book4': bk8, 'book5': bk9},
        'p13': {'book1': bk5, 'book2': bk6, 'book3': bk7, 'book4': bk8, 'book5': bk9},
        'p14': {'book1': bk5, 'book2': bk6, 'book3': bk7, 'book4': bk8, 'book5': bk9},
        'p15': {'book1': bk5, 'book2': bk6, 'book3': bk7, 'book4': bk8, 'book5': bk9},
        'p16': {'book1': bk5, 'book2': bk6, 'book3': bk7, 'book4': bk8, 'book5': bk9},
        'p17': {'book1': bk5, 'book2': bk6, 'book3': bk7, 'book4': bk8, 'book5': bk9},
        'p18': {'book1': bk5, 'book2': bk6, 'book3': bk7, 'book4': bk8, 'book5': bk9},
        'p19': {'book1': bk5, 'book2': bk6, 'book3': bk7, 'book4': bk8, 'book5': bk9},
        'p20': {'book1': bk5, 'book2': bk6, 'book3': bk7, 'book4': bk8, 'book5': bk9}
    },
    '25_1':{  # 20  # accum 60
        'p1' : {'book1': bk0, 'book2': bk1, 'book3': bk2, 'book4': bk3, 'book5': bk4},
        'p2': {'book1': bk0, 'book2': bk1, 'book3': bk2, 'book4': bk3, 'book5': bk4},
        'p3': {'book1': bk0, 'book2': bk1, 'book3': bk2, 'book4': bk3, 'book5': bk4},
        'p4': {'book1': bk0, 'book2': bk1, 'book3': bk2, 'book4': bk3, 'book5': bk4},
        'p5': {'book1': bk0, 'book2': bk1, 'book3': bk2, 'book4': bk3, 'book5': bk4},
        'p6': {'book1': bk0, 'book2': bk1, 'book3': bk2, 'book4': bk3, 'book5': bk4},
        'p7': {'book1': bk0, 'book2': bk1, 'book3': bk2, 'book4': bk3, 'book5': bk4},
        'p8': {'book1': bk0, 'book2': bk1, 'book3': bk2, 'book4': bk3, 'book5': bk4},
        'p9': {'book1': bk0, 'book2': bk1, 'book3': bk2, 'book4': bk3, 'book5': bk4},
        'p10': {'book1': bk0, 'book2': bk1, 'book3': bk2, 'book4': bk3, 'book5': bk4},
        'p11' : {'book1': bk0, 'book2': bk1, 'book3': bk2, 'book4': bk3, 'book5': bk4},
        'p12': {'book1': bk0, 'book2': bk1, 'book3': bk2, 'book4': bk3, 'book5': bk4},
        'p13': {'book1': bk0, 'book2': bk1, 'book3': bk2, 'book4': bk3, 'book5': bk4},
        'p14': {'book1': bk0, 'book2': bk1, 'book3': bk2, 'book4': bk3, 'book5': bk4},
        'p15': {'book1': bk0, 'book2': bk1, 'book3': bk2, 'book4': bk3, 'book5': bk4},
        'p16': {'book1': bk0, 'book2': bk1, 'book3': bk2, 'book4': bk3, 'book5': bk4},
        'p17': {'book1': bk0, 'book2': bk1, 'book3': bk2, 'book4': bk3, 'book5': bk4},
        'p18': {'book1': bk0, 'book2': bk1, 'book3': bk2, 'book4': bk3, 'book5': bk4},
        'p19': {'book1': bk0, 'book2': bk1, 'book3': bk2, 'book4': bk3, 'book5': bk4},
        'p20': {'book1': bk0, 'book2': bk1, 'book3': bk2, 'book4': bk3, 'book5': bk4}
    },
    '25_2': {  # 20  # accum 80
        'p1': {'book1': bk5, 'book2': bk6, 'book3': bk7, 'book4': bk8, 'book5': bk9},
        'p2': {'book1': bk5, 'book2': bk6, 'book3': bk7, 'book4': bk8, 'book5': bk9},
        'p3': {'book1': bk5, 'book2': bk6, 'book3': bk7, 'book4': bk8, 'book5': bk9},
        'p4': {'book1': bk5, 'book2': bk6, 'book3': bk7, 'book4': bk8, 'book5': bk9},
        'p5': {'book1': bk5, 'book2': bk6, 'book3': bk7, 'book4': bk8, 'book5': bk9},
        'p6': {'book1': bk5, 'book2': bk6, 'book3': bk7, 'book4': bk8, 'book5': bk9},
        'p7': {'book1': bk5, 'book2': bk6, 'book3': bk7, 'book4': bk8, 'book5': bk9},
        'p8': {'book1': bk5, 'book2': bk6, 'book3': bk7, 'book4': bk8, 'book5': bk9},
        'p9': {'book1': bk5, 'book2': bk6, 'book3': bk7, 'book4': bk8, 'book5': bk9},
        'p10': {'book1': bk5, 'book2': bk6, 'book3': bk7, 'book4': bk8, 'book5': bk9},
        'p11': {'book1': bk5, 'book2': bk6, 'book3': bk7, 'book4': bk8, 'book5': bk9},
        'p12': {'book1': bk5, 'book2': bk6, 'book3': bk7, 'book4': bk8, 'book5': bk9},
        'p13': {'book1': bk5, 'book2': bk6, 'book3': bk7, 'book4': bk8, 'book5': bk9},
        'p14': {'book1': bk5, 'book2': bk6, 'book3': bk7, 'book4': bk8, 'book5': bk9},
        'p15': {'book1': bk5, 'book2': bk6, 'book3': bk7, 'book4': bk8, 'book5': bk9},
        'p16': {'book1': bk5, 'book2': bk6, 'book3': bk7, 'book4': bk8, 'book5': bk9},
        'p17': {'book1': bk5, 'book2': bk6, 'book3': bk7, 'book4': bk8, 'book5': bk9},
        'p18': {'book1': bk5, 'book2': bk6, 'book3': bk7, 'book4': bk8, 'book5': bk9},
        'p19': {'book1': bk5, 'book2': bk6, 'book3': bk7, 'book4': bk8, 'book5': bk9},
        'p20': {'book1': bk5, 'book2': bk6, 'book3': bk7, 'book4': bk8, 'book5': bk9}
    },
    '20_7': {  # 10  $ accum 90
        'p1': {'book1': bk0, 'book2': bk1, 'book3': bk2, 'book4': bk3, 'book5': bk4, 'book6':bk5, 'book7':bk6},
        'p2': {'book1': bk0, 'book2': bk1, 'book3': bk2, 'book4': bk3, 'book5': bk4, 'book6':bk5, 'book7':bk6},
        'p3': {'book1': bk0, 'book2': bk1, 'book3': bk2, 'book4': bk3, 'book5': bk4, 'book6':bk5, 'book7':bk6},
        'p4': {'book1': bk0, 'book2': bk1, 'book3': bk2, 'book4': bk3, 'book5': bk4, 'book6':bk5, 'book7':bk6},
        'p5': {'book1': bk0, 'book2': bk1, 'book3': bk2, 'book4': bk3, 'book5': bk4, 'book6':bk5, 'book7':bk6},
        'p6': {'book1': bk0, 'book2': bk1, 'book3': bk2, 'book4': bk3, 'book5': bk4, 'book6':bk5, 'book7':bk6},
        'p7': {'book1': bk0, 'book2': bk1, 'book3': bk2, 'book4': bk3, 'book5': bk4, 'book6':bk5, 'book7':bk6},
        'p8': {'book1': bk0, 'book2': bk1, 'book3': bk2, 'book4': bk3, 'book5': bk4, 'book6':bk5, 'book7':bk6},
        'p9': {'book1': bk0, 'book2': bk1, 'book3': bk2, 'book4': bk3, 'book5': bk4, 'book6':bk5, 'book7':bk6},
        'p10': {'book1': bk0, 'book2': bk1, 'book3': bk2, 'book4': bk3, 'book5': bk4, 'book6':bk5, 'book7':bk6}
    },
    '25_8': {  # 10  $ accum 100
        'p1': {'book1': bk0, 'book2': bk1, 'book3': bk2, 'book4': bk3, 'book5': bk4, 'book6':bk5, 'book7':bk6, 'book8':bk7},
        'p2': {'book1': bk0, 'book2': bk1, 'book3': bk2, 'book4': bk3, 'book5': bk4, 'book6':bk5, 'book7':bk6, 'book8':bk7},
        'p3': {'book1': bk0, 'book2': bk1, 'book3': bk2, 'book4': bk3, 'book5': bk4, 'book6':bk5, 'book7':bk6, 'book8':bk7},
        'p4': {'book1': bk0, 'book2': bk1, 'book3': bk2, 'book4': bk3, 'book5': bk4, 'book6':bk5, 'book7':bk6, 'book8':bk7},
        'p5': {'book1': bk0, 'book2': bk1, 'book3': bk2, 'book4': bk3, 'book5': bk4, 'book6':bk5, 'book7':bk6, 'book8':bk7},
        'p6': {'book1': bk0, 'book2': bk1, 'book3': bk2, 'book4': bk3, 'book5': bk4, 'book6':bk5, 'book7':bk6, 'book8':bk7},
        'p7': {'book1': bk0, 'book2': bk1, 'book3': bk2, 'book4': bk3, 'book5': bk4, 'book6':bk5, 'book7':bk6, 'book8':bk7},
        'p8': {'book1': bk0, 'book2': bk1, 'book3': bk2, 'book4': bk3, 'book5': bk4, 'book6':bk5, 'book7':bk6, 'book8':bk7},
        'p9': {'book1': bk0, 'book2': bk1, 'book3': bk2, 'book4': bk3, 'book5': bk4, 'book6':bk5, 'book7':bk6, 'book8':bk7},
        'p10': {'book1': bk0, 'book2': bk1, 'book3': bk2, 'book4': bk3, 'book5': bk4, 'book6':bk5, 'book7':bk6, 'book8':bk7}
    }
}



if __name__ == '__main__':
    # print(books_model['d10_b1']['p1']['book'])
    # print(len(books_model['d10_b1']))
    for item in books_model['d10_b2']['p1']['book']:
        print(item)
