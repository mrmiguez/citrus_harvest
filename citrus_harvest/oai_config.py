from collections import namedtuple
DataProvider = namedtuple('DataProvider', 'code oai_url mdprefix oai_sets')


'''
#
# OAI_DICT values
#
'''

'''
OAI_DICT = {
             'fiu': DataProvider('fiu', 'https://repox.library.miami.edu/repox/OAIHandler', 
                    'oai_dc', ['fsu_bzs', 'fiu_civil', 'fiu_dad', 'fiu_fls', 'fiu_iif', 'fiu_lgcf', 'fiu_lter', 'fiu_phc', 'fiu_ps', 'fiu_two', 'fiu_vms']), 
             'um': DataProvider('um',  'https://repox.library.miami.edu/repox/OAIHandler',
                    'oai_qdc', []),
             'fsu': DataProvider('fsu', 'https://fsu.digital.flvc.org/oai2',
                    'mods', ['fsu_digital_library'])
}'''

OAI_DICT = {
    'fsu': DataProvider('fsu', 'https://fsu.digital.flvc.org/oai2',
                        'mods', ['fsu_admiralleighpapers', 'fsu_hpuaanniegilliamscrapbook', 'fsu_susanbradfordeppespapers'])
}

# OUT_PATH = '/home/mrmiguez/'

OUT_PATH = 'c:\\Users\\mmiguez\\bin\\'