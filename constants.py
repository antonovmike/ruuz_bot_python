from pathlib import Path

# CHOOSE LANGUAGE
RU_UZ = 'Русский - Узбекский'
EN_UZ = 'English - Uzbek'

# HEADINGS
MENU_HEADING = 'Главное меню / Main menu'
HEADING = 'Выберите тему / Choose a topic'
CONVERSATION_HDNG = 'Общение / Conversation / Suxbat'
FOOD_HEADING = 'Еда / Food / Ovqat'
GRAMMAR_HEADING = 'Грамматика / Grammar / Grammatika'
TRAVEL_HEADING = 'Путешестие / Travel'
ABOUT_HEADING = 'Про этот бот / About this bot / Bu bot haqida'
# HEADING RU
MENU_HEADING_RU = 'Главное меню'
HEADING_RU = 'Выберите тему'
CONVERSATION_HDNG_RU = 'Общение / Suxbat'
FOOD_HEADING_RU = 'Еда / Ovqat'
GRAMMAR_HEADING_RU = 'Грамматика / Grammatika'
TRAVEL_HEADING_RU = 'Путешестие'
ABOUT_HEADING_RU = 'Про этот бот / Bu bot haqida'
# HEADINGS EN
MENU_HEADING_EN = 'Main menu'
HEADING_EN = 'Choose a topic'
CONVERSATION_HDNG_EN = 'Conversation / Suxbat'
FOOD_HEADING_EN = 'Food / Ovqat'
GRAMMAR_HEADING_EN = 'Grammar / Grammatika'
TRAVEL_HEADING_EN = 'Travel'
ABOUT_HEADING_EN = 'About this bot / Bu bot haqida'

# HELP OR ABOUT
HELP_TXT_RU = Path('dictionaries/help_ru').read_text()
HELP_TXT_EN = Path('dictionaries/help_en').read_text()

# CONVERSATION
GREETINGS_TXT = Path('dictionaries/greetings').read_text()
HOW_ARE_YOU_TXT = Path('dictionaries/how_are_you').read_text()
BY_TXT = Path('dictionaries/by').read_text()

# FOOD
BAKED_GOODS_TXT = Path('dictionaries/food_baked_goods').read_text()
BERRIES_TXT = Path('dictionaries/food_berries').read_text()
BEVERAGES_TXT = Path('dictionaries/food_beverages').read_text()
FRUITS_TXT = Path('dictionaries/food_fruits').read_text()
GROATS_TXT = Path('dictionaries/food_groats').read_text()
MEAL_TXT = Path('dictionaries/food_meal').read_text()
MEAT_TXT = Path('dictionaries/food_meat').read_text()
MILK_TXT = Path('dictionaries/food_milk').read_text()
MISC_TXT = Path('dictionaries/food_misc').read_text()
SPICE_TXT = Path('dictionaries/food_spice').read_text()
VEGETABLES_TXT = Path('dictionaries/food_vegetables').read_text()

# GRAMMAR
UZ_VERB_FORMS_PNG = 'https://github.com/antonovmike/ruuz_bot_python/blob/test/pictures/uz_verb_forms.png?raw=true'
SOME_VERBS = 'https://github.com/antonovmike/ruuz_bot_python/blob/test/pictures/some_verbs.png?raw=true'
PRONOUN_PNG = 'https://github.com/antonovmike/ruuz_bot_python/blob/main/pictures/pronoun.png?raw=true'
CASES_PNG = 'https://github.com/antonovmike/ruuz_bot_python/blob/test/pictures/cases.png?raw=true'
CASE_GENITIVE_PNG = 'https://github.com/antonovmike/ruuz_bot_python/blob/test/pictures/case_genitive.png?raw=true'

# TRAVEL
TRAVEL_TXT = Path('dictionaries/travel_taxi').read_text()
