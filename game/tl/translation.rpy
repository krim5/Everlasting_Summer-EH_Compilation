init -1001 python:
    if _preferences.language == "english":
        translation=translation_en
    elif _preferences.language == "spanish":
        translation=translation_es
    elif _preferences.language == "italian":
        translation=translation_it
    elif _preferences.language == "chinese":
        translation=translation_ch
    else:
        translation=translation_ru

    translation_new=translation

    def merge_two_dicts(x, y):
        z = x.copy()
        z.update(y)
        return z
    translation_temp={}
    for i,k in translation.iteritems():
        translation_temp[i]={}
        translation_temp[i][_preferences.language]=k
    translation=merge_two_dicts(translation,translation_temp)

    def get_translation(string):
        renpy.log("%s" % string )
        return translation[string][_preferences.language]

