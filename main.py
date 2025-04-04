import csv
import inspect
import logging
import os
import shutil

import genanki  # type: ignore
from navertts import NaverTTS  # type: ignore

from strings import qfmt, afmt, css
from logging_setup import SPAM, SUCCESS

if __name__ == "__main__":
    from logging_setup import logging_setup
    from logging_setup import LoggingArgs

__SCRIPT_VERSION__ = "0.0.2"
__DECK_VERSION__ = "0.0.3-1"

headers = [
    "Vocab",
    "Pre-Vocab-Context",
    "Post-Vocab-Context",
    "Vocab-Pro",
    "Vocab-English",
    "Vocab-Sound",
    "Vocab-Sound-Is-TTS",
    "Vocab-Hanja",
    "Vocab-Topik",
    "Comment",
    "Sentence",
    "Sentence-English",
    "Sentence-Sound",
    "Sentence-Is-TTS",
    "Sentence-TTS-Source",
    "Sentence-TTS-Voice",
    "Sentence-TTS-Speed",
    "Vocab-Sound-Source",
    "Sentence-Sound-Source",
    "tags",
]


class MyNote(genanki.Note):

    @property
    def guid(self: genanki.Note) -> genanki.guid_for:
        # Generate note Hash from fields "Vocab", "Pre-Vocab-Context", "Post-Vocab-Context", "Vocab-Pro" # noqa: B950
        return genanki.guid_for(
            self.fields[0], self.fields[1], self.fields[2], self.fields[3]
        )


def add_media_to_package(package: genanki.Package) -> None:
    logging.log(SPAM, f"Start of '{inspect.currentframe().f_code.co_name}()'")  # type: ignore

    file_list = os.listdir("media")
    logging.log(SPAM, f"Files in 'media' folder: {file_list}")

    for mediaFile in file_list:
        logging.debug(f"Adding file '{mediaFile}' to package")
        package.media_files.append(f"media/{mediaFile}")
        logging.log(SPAM, f"Finished adding file '{mediaFile}' to package")

    logging.log(SPAM, f"End of '{inspect.currentframe().f_code.co_name}()'")  # type: ignore
    return


def add_notes_to_deck(notes: list[genanki.Note], deck: genanki.Deck) -> None:
    logging.log(SPAM, f"Start of '{inspect.currentframe().f_code.co_name}()'")  # type: ignore

    for n in notes:
        deck.add_note(n)

    logging.log(SPAM, f"End of '{inspect.currentframe().f_code.co_name}()'")  # type: ignore
    return


def build_deck() -> genanki.Deck:
    logging.log(SPAM, f"Start of '{inspect.currentframe().f_code.co_name}()'")  # type: ignore

    deck = genanki.Deck(1482631182, "KJMS Korean Class Vocab")

    logging.log(SPAM, f"End of '{inspect.currentframe().f_code.co_name}()'")  # type: ignore
    return deck


def build_model() -> genanki.Model:
    logging.log(SPAM, f"Start of '{inspect.currentframe().f_code.co_name}()'")  # type: ignore

    model = genanki.Model(
        1659843868,
        "KJMSKoreanNotes",
        fields=[
            {"name": "Vocab"},
            {"name": "Pre-Vocab-Context"},
            {"name": "Post-Vocab-Context"},
            {"name": "Vocab-Pro"},
            {"name": "Vocab-English"},
            {"name": "Vocab-Sound"},
            {"name": "Vocab-Sound-Is-TTS"},
            {"name": "Vocab-Hanja"},
            {"name": "Vocab-Topik"},
            {"name": "Comment"},
            {"name": "Sentence"},
            {"name": "Sentence-English"},
            {"name": "Sentence-Sound"},
            {"name": "Sentence-Is-TTS"},
            {"name": "Sentence-TTS-Source"},
            {"name": "Sentence-TTS-Voice"},
            {"name": "Sentence-TTS-Speed"},
            {"name": "Vocab-Sound-Source"},
            {"name": "Sentence-Sound-Source"},
        ],
        templates=[
            {
                "name": "Korean -> English",
                "qfmt": qfmt,
                "afmt": afmt,
            }
        ],
        css=css,
    )

    logging.log(SPAM, f"End of '{inspect.currentframe().f_code.co_name}()'")  # type: ignore
    return model


def build_notes_list() -> list[dict]:
    logging.log(SPAM, f"Start of '{inspect.currentframe().f_code.co_name}()'")  # type: ignore
    notes_list: list[dict] = []

    logging.debug("Creating backup input file")
    shutil.copyfile("input.csv", "input.csv.backup")
    logging.debug("Backup file created")
    with open("input.csv", "r") as infile:

        reader = csv.reader(infile)

        header = next(reader)

        notes_list = [dict(zip(header, row)) for row in reader]

    logging.log(SPAM, f"End of '{inspect.currentframe().f_code.co_name}()'")  # type: ignore
    return notes_list


def build_notes(model: genanki.Model, notes_list: list[dict]) -> list[genanki.Note]:
    logging.log(SPAM, f"Start of '{inspect.currentframe().f_code.co_name}()'")  # type: ignore
    notes: list[genanki.Note] = []

    for n in notes_list:
        note = MyNote(
            model=model,
            fields=[
                n["Vocab"],
                n["Pre-Vocab-Context"],
                n["Post-Vocab-Context"],
                n["Vocab-Pro"],
                n["Vocab-English"],
                n["Vocab-Sound"],
                n["Vocab-Sound-Is-TTS"],
                n["Vocab-Hanja"],
                n["Vocab-Topik"],
                n["Comment"],
                n["Sentence"],
                n["Sentence-English"],
                n["Sentence-Sound"],
                n["Sentence-Is-TTS"],
                n["Sentence-TTS-Source"],
                n["Sentence-TTS-Voice"],
                n["Sentence-TTS-Speed"],
                n["Vocab-Sound-Source"],
                n["Sentence-Sound-Source"],
            ],
            tags=n["tags"].split("|"),
        )

        notes.append(note)

    logging.log(SPAM, f"End of '{inspect.currentframe().f_code.co_name}()'")  # type: ignore
    return notes


def build_package(deck: genanki.Deck) -> genanki.Package:
    logging.log(SPAM, f"Start of '{inspect.currentframe().f_code.co_name}()'")  # type: ignore

    package = genanki.Package(deck)

    logging.log(SPAM, f"End of '{inspect.currentframe().f_code.co_name}()'")  # type: ignore
    return package


def export_package(package: genanki.Package) -> None:
    logging.log(SPAM, f"Start of '{inspect.currentframe().f_code.co_name}()'")  # type: ignore
    package.write_to_file(f"KoreanClassVocab-v{__DECK_VERSION__}.apkg")

    logging.log(SPAM, f"End of '{inspect.currentframe().f_code.co_name}()'")  # type: ignore
    return


def generate_audio(word: str) -> str:
    logging.log(SPAM, f"Start of '{inspect.currentframe().f_code.co_name}()'")  # type: ignore

    logger.debug("Generating TTS audio for '{word}'")
    tts = NaverTTS(word)
    normalized_word = normalize_for_filename(word)

    filename = f"media/{normalized_word}.mp3"

    tts.save(filename)
    logger.debug(f"Audio generated: '{filename}'")

    logging.log(SPAM, f"End of '{inspect.currentframe().f_code.co_name}()'")  # type: ignore
    return filename


def generate_missing_audio(notes: list[dict]) -> list[dict]:
    logging.log(SPAM, f"Start of '{inspect.currentframe().f_code.co_name}()'")  # type: ignore

    for n in notes:
        word = n["Vocab"]
        logging.debug(f"Word: '{word}")

        pronunciation = n["Vocab-Pro"]
        logging.debug(f"Word Pronunciation: '{pronunciation}'")

        sentence = n["Sentence"]
        logging.debug(f"Sentence: '{sentence}'")

        if word:
            if pronunciation:
                if not os.path.isfile(f"media/{pronunciation}.mp3"):
                    pronunciation_filename = generate_audio(pronunciation)
                    n["Vocab-Sound-Is-TTS"] = "Yes"
                    n["Vocab-Sound"] = (
                        f"[sound:{pronunciation_filename.split('/')[-1]}]"
                    )
                    n["Vocab-Sound-Source"] = "Papago Naver TTS"
                else:
                    logger.debug(
                        f"Audio pronunciation for '{pronunciation}' already exists, skipping"
                    )
            else:
                if not os.path.isfile(f"media/{word}.mp3"):
                    word_filename = generate_audio(word)
                    n["Vocab-Sound-Is-TTS"] = "Yes"
                    n["Vocab-Sound"] = f"[sound:{word_filename.split('/')[-1]}]"
                    n["Vocab-Sound-Source"] = "Papago Naver TTS"
                else:
                    logger.debug(f"Audio for '{word}' already exists, skipping")

        if sentence:
            normalized_sentence = normalize_for_filename(sentence)
            if not os.path.isfile(f"media/{normalized_sentence}.mp3"):
                sentence_filename = generate_audio(sentence)
                n["Sentence-Sound"] = f"[sound:{sentence_filename.split('/')[-1]}]"
                n["Sentence-Is-TTS"] = "Yes"
                n["Sentence-Sound-Source"] = "Papago Naver TTS"
            else:
                logger.debug(f"Audio for '{sentence}' already exists, skipping")

    logging.log(SPAM, f"End of '{inspect.currentframe().f_code.co_name}()'")  # type: ignore
    return notes


def normalize_for_filename(input: str) -> str:
    logging.log(SPAM, f"Start of '{inspect.currentframe().f_code.co_name}()'")  # type: ignore

    keepCharacters = (" ", ".", "_")
    logging.debug(f"Filename to clean: {input}")
    clean = "".join(c for c in input if c.isalnum() or c in keepCharacters).rstrip()
    logging.debug(f"Clean filename: {clean}")

    logging.log(SPAM, f"End of '{inspect.currentframe().f_code.co_name}()'")  # type: ignore
    return clean


def update_input_file(notes: list[dict]) -> None:

    try:
        logging.log(SPAM, f"Start of '{inspect.currentframe().f_code.co_name}()'")  # type: ignore
        with open("input.csv", "w") as outfile:
            writer = csv.DictWriter(outfile, fieldnames=headers)

            writer.writeheader()
            writer.writerows(notes)

        logger.debug("Successfully wrote data to 'input.csv'")

        os.remove("input.csv.backup")
        logger.debug("Backup file 'input.csv.backup' removed")
    except Exception as e:
        logger.critical(
            "Something went wrong while writing to 'input.csv'. Backing out."
        )

        if os.path.isfile("input.csv.backup"):
            shutil.copyfile("input.csv.backup", "input.csv")
            logger.debug("Backup file successfully renamed to main file.")

        raise e

    logging.log(SPAM, f"End of '{inspect.currentframe().f_code.co_name}()'")  # type: ignore
    return


def main() -> None:
    logging.log(SPAM, f"Start of '{inspect.currentframe().f_code.co_name}()'")  # type: ignore
    logging.log(SUCCESS, "'궁중무술 한국어 어 수업' Anki Deck Script")
    logging.log(SUCCESS, f"Version v{__SCRIPT_VERSION__}")
    logging.log(SUCCESS, "##########################################")

    model = build_model()
    logging.info("Finished building model")

    deck = build_deck()
    logging.info("Finished initializing deck")

    package = build_package(deck)
    logging.info("Finished initializing package")

    notes_list = build_notes_list()
    logging.info("Finished importing notes from file")

    notes_list = generate_missing_audio(notes_list)
    logging.info("Finished generating missing audio")

    notes = build_notes(model, notes_list)
    logging.info("Finished building notes")

    update_input_file(notes_list)
    logging.info("Finished writing changes to 'input.csv'")

    add_notes_to_deck(notes, deck)
    logging.info("Finished adding notes to deck")

    add_media_to_package(package)
    logging.info("Finished adding media to package")

    export_package(package)
    logging.info("Finished exporting package")

    logging.log(SPAM, f"End of '{inspect.currentframe().f_code.co_name}()'")  # type: ignore
    return


if __name__ == "__main__":

    def main_setup() -> LoggingArgs:
        global logger

        logArgs = LoggingArgs(underscores_to_dashes=True).parse_args(known_only=True)

        logging_setup(logLevel=logArgs.log_level, logToFile=logArgs.logToFile)  # type: ignore
        logger = logging.getLogger(__name__)
        logger.log(SUCCESS, "Logging setup completed")
        logger.info("INFO logging enabled")
        logger.debug("Debug logging enabled")
        logger.log(SPAM, "Spam logging enabled")

        logger.debug("Log Args: %s", logArgs)
        if logArgs.extra_args:
            logger.debug("Unparsed Args: %s", logArgs.extra_args)

        return logArgs

    logArgs: LoggingArgs = main_setup()

    main()
    logging.log(SUCCESS, "##########################################")
    logging.log(SUCCESS, "Script execution complete")

else:
    logger = logging.getLogger(__name__)
