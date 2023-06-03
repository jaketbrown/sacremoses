#!/usr/bin/env python3
import atheris
import sys
import fuzz_helpers


with atheris.instrument_imports(include=['sacremoses']):
    from sacremoses import MosesTokenizer, MosesDetokenizer, MosesTruecaser, MosesPunctNormalizer

languages = ['as', 'bn', 'ca', 'cs', 'de', 'el', 'en', 'es', 'et',
             'fi', 'fr', 'ga', 'gu', 'hi', 'hu', 'is', 'it', 'kn', 'lt',
             'lv', 'ml', 'mni','mr', 'nl', 'or', 'pa', 'pl', 'pt', 'ro',
             'ru', 'sk', 'sl', 'sv', 'ta', 'tdt', 'te', 'yue', 'zh']
def TestOneInput(data):
    fdp = fuzz_helpers.EnhancedFuzzedDataProvider(data)
    choice = fdp.ConsumeIntInRange(0, 3)
    if choice == 0:
        mt = MosesTokenizer(lang=fdp.PickValueInList(languages))
        mt.tokenize(fdp.ConsumeRemainingString(), return_str=fdp.ConsumeBool())
    elif choice == 1:
        mt = MosesDetokenizer(lang=fdp.PickValueInList(languages))
    elif choice == 2:
        mt = MosesTruecaser()
        mt.train(fdp.ConsumeRemainingString())
        mt.truecase(fdp.ConsumeRemainingString())
    elif choice == 3:
        mt = MosesPunctNormalizer()
        mt.normalize(fdp.ConsumeRemainingString())
def main():
    atheris.Setup(sys.argv, TestOneInput)
    atheris.Fuzz()


if __name__ == "__main__":
    main()