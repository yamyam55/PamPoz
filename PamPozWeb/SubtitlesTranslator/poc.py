from googletrans import Translator
from SubtitlesTranslator import settings

def main():
    with open(settings.SUBTITLE_TOTRANSLATE_FILE, "r") as to_translate_file:
        to_translate_sub = to_translate_file.read()

    translated_subtitles = translate_subtitles(to_translate_sub)

    with open(settings.SUBTITLE_TRANSLATED_FILE,"w") as translated_file:
        translated_file.write(translated_subtitles)

def translate_subtitles(subtitles):
    translator = Translator()
    subtitles_entries = subtitles.split('\n\n')
    translated_subtitles_entries = []
    for current_subtitle_entry in subtitles_entries:
        try:
            translated_subtitles_entries += translate_entry(translator,current_subtitle_entry.split('\n'))
        except:
            print("Could not translate" + current_subtitle_entry)

    return create_translated_subtitles(translated_subtitles_entries)

def translate_entry(translator,subtitle_entry):

    subtitle_text_translation = translator.translate(subtitle_entry[settings.SUBTITLE_TEXT_INDEX], dest="hebrew")
    subtitle_entry[settings.SUBTITLE_TEXT_INDEX] = subtitle_text_translation.text
    return subtitle_entry

def create_translated_subtitles(translated_subtitles_entries):
    translated_subtitles_data = ""

    for current_translated_entry in translated_subtitles_entries:
        translated_subtitles_data += '\n'.join(current_translated_entry)
        # Empty line between subtitles entries.
        translated_subtitles_data += '\n\n'

    return translated_subtitles_data

if __name__ == "__main__":
    main()