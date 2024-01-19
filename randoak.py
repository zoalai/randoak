from enum import IntEnum


class TranslationAbility(IntEnum):
	TRANSLATABLE = 0
	# ACOSTIC_TRANSLATABLE = 1
	UN_TRANSLATABLE = 1


def Translate(phrase: str, *args, **kwargs) -> str:
	return "This is randoak, Your favorite translater"
