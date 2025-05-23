# Copyright 2015 Christoph Reiter
#
# This program is free software; you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation; either version 2 of the License, or
# (at your option) any later version.

from .i18n import register_translation


# Based on https://pkg-isocodes.alioth.debian.org/
# which is licensed under LGPL-2.1+
# Generated using _print_iso_639() (see below)
_ISO_639 = [
    ("Afar", "aa", "aar", ""),
    ("Abkhazian", "ab", "abk", ""),
    ("Achinese", "", "ace", ""),
    ("Acoli", "", "ach", ""),
    ("Adangme", "", "ada", ""),
    ("Adyghe; Adygei", "", "ady", ""),
    ("Afro-Asiatic languages", "", "afa", ""),
    ("Afrihili", "", "afh", ""),
    ("Afrikaans", "af", "afr", ""),
    ("Ainu", "", "ain", ""),
    ("Akan", "ak", "aka", ""),
    ("Akkadian", "", "akk", ""),
    ("Albanian", "sq", "alb", "sqi"),
    ("Aleut", "", "ale", ""),
    ("Algonquian languages", "", "alg", ""),
    ("Southern Altai", "", "alt", ""),
    ("Amharic", "am", "amh", ""),
    ("English, Old (ca. 450-1100)", "", "ang", ""),
    ("Angika", "", "anp", ""),
    ("Apache languages", "", "apa", ""),
    ("Arabic", "ar", "ara", ""),
    ("Official Aramaic (700-300 BCE); Imperial Aramaic (700-300 BCE)", "", "arc", ""),
    ("Aragonese", "an", "arg", ""),
    ("Armenian", "hy", "arm", "hye"),
    ("Mapudungun; Mapuche", "", "arn", ""),
    ("Arapaho", "", "arp", ""),
    ("Artificial languages", "", "art", ""),
    ("Arawak", "", "arw", ""),
    ("Assamese", "as", "asm", ""),
    ("Asturian; Bable; Leonese; Asturleonese", "", "ast", ""),
    ("Athapascan languages", "", "ath", ""),
    ("Australian languages", "", "aus", ""),
    ("Avaric", "av", "ava", ""),
    ("Avestan", "ae", "ave", ""),
    ("Awadhi", "", "awa", ""),
    ("Aymara", "ay", "aym", ""),
    ("Azerbaijani", "az", "aze", ""),
    ("Banda languages", "", "bad", ""),
    ("Bamileke languages", "", "bai", ""),
    ("Bashkir", "ba", "bak", ""),
    ("Baluchi", "", "bal", ""),
    ("Bambara", "bm", "bam", ""),
    ("Balinese", "", "ban", ""),
    ("Basque", "eu", "baq", "eus"),
    ("Basa", "", "bas", ""),
    ("Baltic languages", "", "bat", ""),
    ("Beja; Bedawiyet", "", "bej", ""),
    ("Belarusian", "be", "bel", ""),
    ("Bemba", "", "bem", ""),
    ("Bengali", "bn", "ben", ""),
    ("Berber languages", "", "ber", ""),
    ("Bhojpuri", "", "bho", ""),
    ("Bihari languages", "bh", "bih", ""),
    ("Bikol", "", "bik", ""),
    ("Bini; Edo", "", "bin", ""),
    ("Bislama", "bi", "bis", ""),
    ("Siksika", "", "bla", ""),
    ("Bantu languages", "", "bnt", ""),
    ("Bosnian", "bs", "bos", ""),
    ("Braj", "", "bra", ""),
    ("Breton", "br", "bre", ""),
    ("Batak languages", "", "btk", ""),
    ("Buriat", "", "bua", ""),
    ("Buginese", "", "bug", ""),
    ("Bulgarian", "bg", "bul", ""),
    ("Burmese", "my", "bur", "mya"),
    ("Blin; Bilin", "", "byn", ""),
    ("Caddo", "", "cad", ""),
    ("Central American Indian languages", "", "cai", ""),
    ("Galibi Carib", "", "car", ""),
    ("Catalan; Valencian", "ca", "cat", ""),
    ("Caucasian languages", "", "cau", ""),
    ("Cebuano", "", "ceb", ""),
    ("Celtic languages", "", "cel", ""),
    ("Chamorro", "ch", "cha", ""),
    ("Chibcha", "", "chb", ""),
    ("Chechen", "ce", "che", ""),
    ("Chagatai", "", "chg", ""),
    ("Chinese", "zh", "chi", "zho"),
    ("Chuukese", "", "chk", ""),
    ("Mari", "", "chm", ""),
    ("Chinook jargon", "", "chn", ""),
    ("Choctaw", "", "cho", ""),
    ("Chipewyan; Dene Suline", "", "chp", ""),
    ("Cherokee", "", "chr", ""),
    (
        "Church Slavic; Old Slavonic; Church Slavonic; Old Bulgarian; "
        "Old Church Slavonic",
        "cu",
        "chu",
        "",
    ),
    ("Chuvash", "cv", "chv", ""),
    ("Cheyenne", "", "chy", ""),
    ("Chamic languages", "", "cmc", ""),
    ("Coptic", "", "cop", ""),
    ("Cornish", "kw", "cor", ""),
    ("Corsican", "co", "cos", ""),
    ("Creoles and pidgins, English based", "", "cpe", ""),
    ("Creoles and pidgins, French-based", "", "cpf", ""),
    ("Creoles and pidgins, Portuguese-based", "", "cpp", ""),
    ("Cree", "cr", "cre", ""),
    ("Crimean Tatar; Crimean Turkish", "", "crh", ""),
    ("Creoles and pidgins", "", "crp", ""),
    ("Kashubian", "", "csb", ""),
    ("Cushitic languages", "", "cus", ""),
    ("Czech", "cs", "cze", "ces"),
    ("Dakota", "", "dak", ""),
    ("Danish", "da", "dan", ""),
    ("Dargwa", "", "dar", ""),
    ("Land Dayak languages", "", "day", ""),
    ("Delaware", "", "del", ""),
    ("Slave (Athapascan)", "", "den", ""),
    ("Dogrib", "", "dgr", ""),
    ("Dinka", "", "din", ""),
    ("Divehi; Dhivehi; Maldivian", "dv", "div", ""),
    ("Dogri", "", "doi", ""),
    ("Dravidian languages", "", "dra", ""),
    ("Lower Sorbian", "", "dsb", ""),
    ("Duala", "", "dua", ""),
    ("Dutch, Middle (ca. 1050-1350)", "", "dum", ""),
    ("Dutch; Flemish", "nl", "dut", "nld"),
    ("Dyula", "", "dyu", ""),
    ("Dzongkha", "dz", "dzo", ""),
    ("Efik", "", "efi", ""),
    ("Egyptian (Ancient)", "", "egy", ""),
    ("Ekajuk", "", "eka", ""),
    ("Elamite", "", "elx", ""),
    ("English", "en", "eng", ""),
    ("English, Middle (1100-1500)", "", "enm", ""),
    ("Esperanto", "eo", "epo", ""),
    ("Estonian", "et", "est", ""),
    ("Ewe", "ee", "ewe", ""),
    ("Ewondo", "", "ewo", ""),
    ("Fang", "", "fan", ""),
    ("Faroese", "fo", "fao", ""),
    ("Fanti", "", "fat", ""),
    ("Fijian", "fj", "fij", ""),
    ("Filipino; Pilipino", "", "fil", ""),
    ("Finnish", "fi", "fin", ""),
    ("Finno-Ugrian languages", "", "fiu", ""),
    ("Fon", "", "fon", ""),
    ("French", "fr", "fre", "fra"),
    ("French, Middle (ca. 1400-1600)", "", "frm", ""),
    ("French, Old (842-ca. 1400)", "", "fro", ""),
    ("Northern Frisian", "", "frr", ""),
    ("Eastern Frisian", "", "frs", ""),
    ("Western Frisian", "fy", "fry", ""),
    ("Fulah", "ff", "ful", ""),
    ("Friulian", "", "fur", ""),
    ("Ga", "", "gaa", ""),
    ("Gayo", "", "gay", ""),
    ("Gbaya", "", "gba", ""),
    ("Germanic languages", "", "gem", ""),
    ("Georgian", "ka", "geo", "kat"),
    ("German", "de", "ger", "deu"),
    ("Geez", "", "gez", ""),
    ("Gilbertese", "", "gil", ""),
    ("Gaelic; Scottish Gaelic", "gd", "gla", ""),
    ("Irish", "ga", "gle", ""),
    ("Galician", "gl", "glg", ""),
    ("Manx", "gv", "glv", ""),
    ("German, Middle High (ca. 1050-1500)", "", "gmh", ""),
    ("German, Old High (ca. 750-1050)", "", "goh", ""),
    ("Gondi", "", "gon", ""),
    ("Gorontalo", "", "gor", ""),
    ("Gothic", "", "got", ""),
    ("Grebo", "", "grb", ""),
    ("Greek, Ancient (to 1453)", "", "grc", ""),
    ("Greek, Modern (1453-)", "el", "gre", "ell"),
    ("Guarani", "gn", "grn", ""),
    ("Swiss German; Alemannic; Alsatian", "", "gsw", ""),
    ("Gujarati", "gu", "guj", ""),
    ("Gwich'in", "", "gwi", ""),
    ("Haida", "", "hai", ""),
    ("Haitian; Haitian Creole", "ht", "hat", ""),
    ("Hausa", "ha", "hau", ""),
    ("Hawaiian", "", "haw", ""),
    ("Hebrew", "he", "heb", ""),
    ("Herero", "hz", "her", ""),
    ("Hiligaynon", "", "hil", ""),
    ("Himachali languages; Western Pahari languages", "", "him", ""),
    ("Hindi", "hi", "hin", ""),
    ("Hittite", "", "hit", ""),
    ("Hmong; Mong", "", "hmn", ""),
    ("Hiri Motu", "ho", "hmo", ""),
    ("Croatian", "hr", "hrv", ""),
    ("Upper Sorbian", "", "hsb", ""),
    ("Hungarian", "hu", "hun", ""),
    ("Hupa", "", "hup", ""),
    ("Iban", "", "iba", ""),
    ("Igbo", "ig", "ibo", ""),
    ("Icelandic", "is", "ice", "isl"),
    ("Ido", "io", "ido", ""),
    ("Sichuan Yi; Nuosu", "ii", "iii", ""),
    ("Ijo languages", "", "ijo", ""),
    ("Inuktitut", "iu", "iku", ""),
    ("Interlingue; Occidental", "ie", "ile", ""),
    ("Iloko", "", "ilo", ""),
    ("Interlingua (International Auxiliary Language Association)", "ia", "ina", ""),
    ("Indic languages", "", "inc", ""),
    ("Indonesian", "id", "ind", ""),
    ("Indo-European languages", "", "ine", ""),
    ("Ingush", "", "inh", ""),
    ("Inupiaq", "ik", "ipk", ""),
    ("Iranian languages", "", "ira", ""),
    ("Iroquoian languages", "", "iro", ""),
    ("Italian", "it", "ita", ""),
    ("Javanese", "jv", "jav", ""),
    ("Lojban", "", "jbo", ""),
    ("Japanese", "ja", "jpn", ""),
    ("Judeo-Persian", "", "jpr", ""),
    ("Judeo-Arabic", "", "jrb", ""),
    ("Kara-Kalpak", "", "kaa", ""),
    ("Kabyle", "", "kab", ""),
    ("Kachin; Jingpho", "", "kac", ""),
    ("Kalaallisut; Greenlandic", "kl", "kal", ""),
    ("Kamba", "", "kam", ""),
    ("Kannada", "kn", "kan", ""),
    ("Karen languages", "", "kar", ""),
    ("Kashmiri", "ks", "kas", ""),
    ("Kanuri", "kr", "kau", ""),
    ("Kawi", "", "kaw", ""),
    ("Kazakh", "kk", "kaz", ""),
    ("Kabardian", "", "kbd", ""),
    ("Khasi", "", "kha", ""),
    ("Khoisan languages", "", "khi", ""),
    ("Central Khmer", "km", "khm", ""),
    ("Khotanese;Sakan", "", "kho", ""),
    ("Kikuyu; Gikuyu", "ki", "kik", ""),
    ("Kinyarwanda", "rw", "kin", ""),
    ("Kirghiz; Kyrgyz", "ky", "kir", ""),
    ("Kimbundu", "", "kmb", ""),
    ("Konkani", "", "kok", ""),
    ("Komi", "kv", "kom", ""),
    ("Kongo", "kg", "kon", ""),
    ("Korean", "ko", "kor", ""),
    ("Kosraean", "", "kos", ""),
    ("Kpelle", "", "kpe", ""),
    ("Karachay-Balkar", "", "krc", ""),
    ("Karelian", "", "krl", ""),
    ("Kru languages", "", "kro", ""),
    ("Kurukh", "", "kru", ""),
    ("Kuanyama; Kwanyama", "kj", "kua", ""),
    ("Kumyk", "", "kum", ""),
    ("Kurdish", "ku", "kur", ""),
    ("Kutenai", "", "kut", ""),
    ("Ladino", "", "lad", ""),
    ("Lahnda", "", "lah", ""),
    ("Lamba", "", "lam", ""),
    ("Lao", "lo", "lao", ""),
    ("Latin", "la", "lat", ""),
    ("Latvian", "lv", "lav", ""),
    ("Lezghian", "", "lez", ""),
    ("Limburgan; Limburger; Limburgish", "li", "lim", ""),
    ("Lingala", "ln", "lin", ""),
    ("Lithuanian", "lt", "lit", ""),
    ("Mongo", "", "lol", ""),
    ("Lozi", "", "loz", ""),
    ("Luxembourgish; Letzeburgesch", "lb", "ltz", ""),
    ("Luba-Lulua", "", "lua", ""),
    ("Luba-Katanga", "lu", "lub", ""),
    ("Ganda", "lg", "lug", ""),
    ("Luiseno", "", "lui", ""),
    ("Lunda", "", "lun", ""),
    ("Luo (Kenya and Tanzania)", "", "luo", ""),
    ("Lushai", "", "lus", ""),
    ("Macedonian", "mk", "mac", "mkd"),
    ("Madurese", "", "mad", ""),
    ("Magahi", "", "mag", ""),
    ("Marshallese", "mh", "mah", ""),
    ("Maithili", "", "mai", ""),
    ("Makasar", "", "mak", ""),
    ("Malayalam", "ml", "mal", ""),
    ("Mandingo", "", "man", ""),
    ("Maori", "mi", "mao", "mri"),
    ("Austronesian languages", "", "map", ""),
    ("Marathi", "mr", "mar", ""),
    ("Masai", "", "mas", ""),
    ("Malay", "ms", "may", "msa"),
    ("Moksha", "", "mdf", ""),
    ("Mandar", "", "mdr", ""),
    ("Mende", "", "men", ""),
    ("Irish, Middle (900-1200)", "", "mga", ""),
    ("Mi'kmaq; Micmac", "", "mic", ""),
    ("Minangkabau", "", "min", ""),
    ("Uncoded languages", "", "mis", ""),
    ("Mon-Khmer languages", "", "mkh", ""),
    ("Malagasy", "mg", "mlg", ""),
    ("Maltese", "mt", "mlt", ""),
    ("Manchu", "", "mnc", ""),
    ("Manipuri", "", "mni", ""),
    ("Manobo languages", "", "mno", ""),
    ("Mohawk", "", "moh", ""),
    ("Moldavian; Moldovan", "mo", "mol", ""),
    ("Mongolian", "mn", "mon", ""),
    ("Mossi", "", "mos", ""),
    ("Multiple languages", "", "mul", ""),
    ("Munda languages", "", "mun", ""),
    ("Creek", "", "mus", ""),
    ("Mirandese", "", "mwl", ""),
    ("Marwari", "", "mwr", ""),
    ("Mayan languages", "", "myn", ""),
    ("Erzya", "", "myv", ""),
    ("Nahuatl languages", "", "nah", ""),
    ("North American Indian languages", "", "nai", ""),
    ("Neapolitan", "", "nap", ""),
    ("Nauru", "na", "nau", ""),
    ("Navajo; Navaho", "nv", "nav", ""),
    ("Ndebele, South; South Ndebele", "nr", "nbl", ""),
    ("Ndebele, North; North Ndebele", "nd", "nde", ""),
    ("Ndonga", "ng", "ndo", ""),
    ("Low German; Low Saxon; German, Low; Saxon, Low", "", "nds", ""),
    ("Nepali", "ne", "nep", ""),
    ("Nepal Bhasa; Newari", "", "new", ""),
    ("Nias", "", "nia", ""),
    ("Niger-Kordofanian languages", "", "nic", ""),
    ("Niuean", "", "niu", ""),
    ("Norwegian Nynorsk; Nynorsk, Norwegian", "nn", "nno", ""),
    ("Bokm\xe5l, Norwegian; Norwegian Bokm\xe5l", "nb", "nob", ""),
    ("Nogai", "", "nog", ""),
    ("Norse, Old", "", "non", ""),
    ("Norwegian", "no", "nor", ""),
    ("N'Ko", "", "nqo", ""),
    ("Pedi; Sepedi; Northern Sotho", "", "nso", ""),
    ("Nubian languages", "", "nub", ""),
    ("Classical Newari; Old Newari; Classical Nepal Bhasa", "", "nwc", ""),
    ("Chichewa; Chewa; Nyanja", "ny", "nya", ""),
    ("Nyamwezi", "", "nym", ""),
    ("Nyankole", "", "nyn", ""),
    ("Nyoro", "", "nyo", ""),
    ("Nzima", "", "nzi", ""),
    ("Occitan (post 1500)", "oc", "oci", ""),
    ("Ojibwa", "oj", "oji", ""),
    ("Oriya", "or", "ori", ""),
    ("Oromo", "om", "orm", ""),
    ("Osage", "", "osa", ""),
    ("Ossetian; Ossetic", "os", "oss", ""),
    ("Turkish, Ottoman (1500-1928)", "", "ota", ""),
    ("Otomian languages", "", "oto", ""),
    ("Papuan languages", "", "paa", ""),
    ("Pangasinan", "", "pag", ""),
    ("Pahlavi", "", "pal", ""),
    ("Pampanga; Kapampangan", "", "pam", ""),
    ("Panjabi; Punjabi", "pa", "pan", ""),
    ("Papiamento", "", "pap", ""),
    ("Palauan", "", "pau", ""),
    ("Persian, Old (ca. 600-400 B.C.)", "", "peo", ""),
    ("Persian", "fa", "per", "fas"),
    ("Philippine languages", "", "phi", ""),
    ("Phoenician", "", "phn", ""),
    ("Pali", "pi", "pli", ""),
    ("Polish", "pl", "pol", ""),
    ("Pohnpeian", "", "pon", ""),
    ("Portuguese", "pt", "por", ""),
    ("Prakrit languages", "", "pra", ""),
    ("Proven\xe7al, Old (to 1500); Occitan, Old (to 1500)", "", "pro", ""),
    ("Pushto; Pashto", "ps", "pus", ""),
    ("Reserved for local use", "", "qaa-qtz", ""),
    ("Quechua", "qu", "que", ""),
    ("Rajasthani", "", "raj", ""),
    ("Rapanui", "", "rap", ""),
    ("Rarotongan; Cook Islands Maori", "", "rar", ""),
    ("Romance languages", "", "roa", ""),
    ("Romansh", "rm", "roh", ""),
    ("Romany", "", "rom", ""),
    ("Romanian", "ro", "rum", "ron"),
    ("Rundi", "rn", "run", ""),
    ("Aromanian; Arumanian; Macedo-Romanian", "", "rup", ""),
    ("Russian", "ru", "rus", ""),
    ("Sandawe", "", "sad", ""),
    ("Sango", "sg", "sag", ""),
    ("Yakut", "", "sah", ""),
    ("South American Indian languages", "", "sai", ""),
    ("Salishan languages", "", "sal", ""),
    ("Samaritan Aramaic", "", "sam", ""),
    ("Sanskrit", "sa", "san", ""),
    ("Sasak", "", "sas", ""),
    ("Santali", "", "sat", ""),
    ("Sicilian", "", "scn", ""),
    ("Scots", "", "sco", ""),
    ("Selkup", "", "sel", ""),
    ("Semitic languages", "", "sem", ""),
    ("Irish, Old (to 900)", "", "sga", ""),
    ("Sign Languages", "", "sgn", ""),
    ("Shan", "", "shn", ""),
    ("Sidamo", "", "sid", ""),
    ("Sinhala; Sinhalese", "si", "sin", ""),
    ("Siouan languages", "", "sio", ""),
    ("Sino-Tibetan languages", "", "sit", ""),
    ("Slavic languages", "", "sla", ""),
    ("Slovak", "sk", "slo", "slk"),
    ("Slovenian", "sl", "slv", ""),
    ("Southern Sami", "", "sma", ""),
    ("Northern Sami", "se", "sme", ""),
    ("Sami languages", "", "smi", ""),
    ("Lule Sami", "", "smj", ""),
    ("Inari Sami", "", "smn", ""),
    ("Samoan", "sm", "smo", ""),
    ("Skolt Sami", "", "sms", ""),
    ("Shona", "sn", "sna", ""),
    ("Sindhi", "sd", "snd", ""),
    ("Soninke", "", "snk", ""),
    ("Sogdian", "", "sog", ""),
    ("Somali", "so", "som", ""),
    ("Songhai languages", "", "son", ""),
    ("Sotho, Southern", "st", "sot", ""),
    ("Spanish; Castilian", "es", "spa", ""),
    ("Sardinian", "sc", "srd", ""),
    ("Sranan Tongo", "", "srn", ""),
    ("Serbian", "sr", "srp", ""),
    ("Serer", "", "srr", ""),
    ("Nilo-Saharan languages", "", "ssa", ""),
    ("Swati", "ss", "ssw", ""),
    ("Sukuma", "", "suk", ""),
    ("Sundanese", "su", "sun", ""),
    ("Susu", "", "sus", ""),
    ("Sumerian", "", "sux", ""),
    ("Swahili", "sw", "swa", ""),
    ("Swedish", "sv", "swe", ""),
    ("Classical Syriac", "", "syc", ""),
    ("Syriac", "", "syr", ""),
    ("Tahitian", "ty", "tah", ""),
    ("Tai languages", "", "tai", ""),
    ("Tamil", "ta", "tam", ""),
    ("Tatar", "tt", "tat", ""),
    ("Telugu", "te", "tel", ""),
    ("Timne", "", "tem", ""),
    ("Tereno", "", "ter", ""),
    ("Tetum", "", "tet", ""),
    ("Tajik", "tg", "tgk", ""),
    ("Tagalog", "tl", "tgl", ""),
    ("Thai", "th", "tha", ""),
    ("Tibetan", "bo", "tib", "bod"),
    ("Tigre", "", "tig", ""),
    ("Tigrinya", "ti", "tir", ""),
    ("Tiv", "", "tiv", ""),
    ("Tokelau", "", "tkl", ""),
    ("Klingon; tlhIngan-Hol", "", "tlh", ""),
    ("Tlingit", "", "tli", ""),
    ("Tamashek", "", "tmh", ""),
    ("Tonga (Nyasa)", "", "tog", ""),
    ("Tonga (Tonga Islands)", "to", "ton", ""),
    ("Tok Pisin", "", "tpi", ""),
    ("Tsimshian", "", "tsi", ""),
    ("Tswana", "tn", "tsn", ""),
    ("Tsonga", "ts", "tso", ""),
    ("Turkmen", "tk", "tuk", ""),
    ("Tumbuka", "", "tum", ""),
    ("Tupi languages", "", "tup", ""),
    ("Turkish", "tr", "tur", ""),
    ("Altaic languages", "", "tut", ""),
    ("Tuvalu", "", "tvl", ""),
    ("Twi", "tw", "twi", ""),
    ("Tuvinian", "", "tyv", ""),
    ("Udmurt", "", "udm", ""),
    ("Ugaritic", "", "uga", ""),
    ("Uighur; Uyghur", "ug", "uig", ""),
    ("Ukrainian", "uk", "ukr", ""),
    ("Umbundu", "", "umb", ""),
    ("Undetermined", "", "und", ""),
    ("Urdu", "ur", "urd", ""),
    ("Uzbek", "uz", "uzb", ""),
    ("Vai", "", "vai", ""),
    ("Venda", "ve", "ven", ""),
    ("Vietnamese", "vi", "vie", ""),
    ("Volap\xfck", "vo", "vol", ""),
    ("Votic", "", "vot", ""),
    ("Wakashan languages", "", "wak", ""),
    ("Wolaitta; Wolaytta", "", "wal", ""),
    ("Waray", "", "war", ""),
    ("Washo", "", "was", ""),
    ("Welsh", "cy", "wel", "cym"),
    ("Sorbian languages", "", "wen", ""),
    ("Walloon", "wa", "wln", ""),
    ("Wolof", "wo", "wol", ""),
    ("Kalmyk; Oirat", "", "xal", ""),
    ("Xhosa", "xh", "xho", ""),
    ("Yao", "", "yao", ""),
    ("Yapese", "", "yap", ""),
    ("Yiddish", "yi", "yid", ""),
    ("Yoruba", "yo", "yor", ""),
    ("Yupik languages", "", "ypk", ""),
    ("Zapotec", "", "zap", ""),
    ("Blissymbols; Blissymbolics; Bliss", "", "zbl", ""),
    ("Zenaga", "", "zen", ""),
    ("Standard Moroccan Tamazight", "", "zgh", ""),
    ("Zhuang; Chuang", "za", "zha", ""),
    ("Zande languages", "", "znd", ""),
    ("Zulu", "zu", "zul", ""),
    ("Zuni", "", "zun", ""),
    ("No linguistic content; Not applicable", "", "zxx", ""),
    ("Zaza; Dimili; Dimli; Kirdki; Kirmanjki; Zazaki", "", "zza", ""),
]

_ISO_639_1 = {}
_ISO_639_2 = {}
_LOWER = {}


def _fill_mappings():
    for entry in _ISO_639:
        name, _1, _2B, _2T = entry
        _LOWER[name.lower()] = name
        if _1:
            _ISO_639_1[_1] = entry
        _ISO_639_2[_2B] = entry
        if _2T:
            _ISO_639_2[_2T] = entry


_fill_mappings()


ISO_639_2 = list(_ISO_639_2.keys())


def _gettext(name, cache=None):
    cache = cache or []
    if not cache:
        t = register_translation("iso_639")
        cache.append(lambda s: t.wrap_text(t.gettext(s)))
    return cache[0](name)


def get_name(iso_code):
    """Returns the English name for the iso_639_1/2 code or an empty string
    if the code is not known.
    """

    if iso_code in _ISO_639_1:
        return _ISO_639_1[iso_code][0]
    if iso_code in _ISO_639_2:
        return _ISO_639_2[iso_code][0]

    return ""


def translate(text):
    """Given an iso code or a name tries to return a translated version
    for the current locale.

    If no translation is found returns an empty string.
    """

    # try to convert iso codes to English names and then translate
    name = get_name(text)
    if name:
        return _gettext(name)
    # not an iso code, try to match with the English name.
    # If all fails just return the original input
    lower = text.lower()
    if lower in _LOWER:
        return _gettext(_LOWER[lower])
    return ""


def _print_iso_639():
    """Prints the _ISO_639 list from above based on iso_639.xml.

    Maybe depend on the xml at runtime?
    """

    import os
    import pprint
    from xml.etree import cElementTree as ET  # noqa

    from .path import xdg_get_system_data_dirs

    entries = []
    for data_dir in xdg_get_system_data_dirs():
        iso_path = os.path.join(data_dir, "xml", "iso-codes", "iso_639.xml")
        if os.path.exists(iso_path):
            tree = ET.ElementTree(file=iso_path)
            for elm in tree.iterfind("iso_639_entry"):
                iso_639_1_code = elm.attrib.get("iso_639_1_code", "")
                iso_639_2B_code = elm.attrib["iso_639_2B_code"]
                iso_639_2T_code = elm.attrib["iso_639_2T_code"]
                if iso_639_2B_code == iso_639_2T_code:
                    iso_639_2T_code = ""
                name = elm.attrib["name"]
                entries.append((name, iso_639_1_code, iso_639_2B_code, iso_639_2T_code))
            break
    else:
        raise Exception("iso_639.xml not found")

    pprint.pprint(entries)
