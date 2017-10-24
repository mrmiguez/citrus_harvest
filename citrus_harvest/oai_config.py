from collections import namedtuple

DataProvider = namedtuple('DataProvider', 'code oai_url mdprefix oai_sets')

OAI_DICT = {
    'fiu': DataProvider('fiu', 'https://repox.library.miami.edu/repox/OAIHandler',
                        'oai_dc',
                        ['fiu_bzs', 'fiu_civil', 'fiu_dad', 'fiu_fls', 'fiu_iif',
                         'fiu_lgcf', 'fiu_lter', 'fiu_phc', 'fiu_ps', 'fiu_two',
                         'fiu_vms']),
    'um': DataProvider('um', 'https://repox.library.miami.edu/repox/OAIHandler',
                       'oai_qdc',
                       ['um_arc5100', 'um_arc5200', 'um_arc5300', 'um_arcdigital',
                        'um_asm0015', 'um_asm0034', 'um_asm0037', 'um_asm0038',
                        'um_asm0055', 'um_asm0060', 'um_asm0075', 'um_asm0085',
                        'um_asm0216', 'um_asm0286', 'um_asm0299', 'um_asm0300',
                        'um_asm0301', 'um_asm0304', 'um_asm0344', 'um_asm0383',
                        'um_asm0400', 'um_asm0409', 'um_asm0410', 'um_asm0447',
                        'um_asm0471', 'um_asm0491', 'um_asm0530', 'um_asm0566',
                        'um_asm0567', 'um_asm0569', 'um_asm0570', 'um_asm0610',
                        'um_asm0636', 'um_asm0650', 'um_asm0655', 'um_asm0656',
                        'um_asm5000', 'um_asu0651', 'um_chc0015', 'um_chc0111',
                        'um_chc0124', 'um_chc0126', 'um_chc0184', 'um_chc0189',
                        'um_chc0193', 'um_chc0219', 'um_chc0336', 'um_chc0339',
                        'um_chc0347', 'um_chc0356', 'um_chc0359', 'um_chc0364',
                        'um_chc0380', 'um_chc0398', 'um_chc0400', 'um_chc0460',
                        'um_chc0468', 'um_chc0484', 'um_chc0487', 'um_chc5006',
                        'um_chc5010', 'um_chc5017', 'um_chc5047', 'um_chc5061O',
                        'um_chc5066', 'um_chc5122', 'um_chc5123', 'um_chc5143',
                        'um_chc5209', 'um_chc5212', 'um_chc5223', 'um_chc5246',
                        'um_chc5252', 'um_chc5260', 'um_chc5277', 'um_chc5278',
                        'um_chc5298J', 'um_chc5299', 'um_chc5312H', 'um_chc5313',
                        'um_chc5324', 'um_chc5330', 'um_chc5352', 'um_chc5372',
                        'um_chc9999', 'um_cubanphotos', 'um_cwsi', 'um_oralhistory',
                        'um_pamphlets', 'um_rinhart', 'um_scbooks', 'um_students',
                        'um_sutherland', 'um_swingle', 'um_theater', 'um_tobaccoart',
                        'um_umathletics', 'um_umcolleges', 'um_umevents', 'um_umiscel',
                        'um_umpeople', 'um_umphotos', 'um_umservice', 'um_umstudents',
                        'um_umsupport', 'um_wtswingle']),
    'fsu': DataProvider('fsu', 'https://fsu.digital.flvc.org/oai2',
                        'mods', ['fsu_digital_library'])
}

# # testing dict
# OAI_DICT = {
    # 'fiu': DataProvider('fiu', 'https://repox.library.miami.edu/repox/OAIHandler',
                        # 'oai_dc', ['fiu_bzs', 'fiu_civil']),
    # 'um': DataProvider('um', 'https://repox.library.miami.edu/repox/OAIHandler',
                       # 'oai_qdc',
                       # ['um_arc5100', 'um_arc5200', 'um_arc5300', 'um_arcdigital']),                        
    # 'fsu': DataProvider('fsu', 'https://fsu.digital.flvc.org/oai2',
                        # 'mods', ['fsu_admiralleighpapers'])
            # }

OUT_PATH = '/home/mrmiguez/OAI_export/'

# local test
# OUT_PATH = 'c:\\Users\\mmiguez\\bin\\'
