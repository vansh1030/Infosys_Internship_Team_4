from src.transcription.whisper_transcriber import transcribe_audio
from src.scoring.llm_scorer import score_conversation
from src.utils.text_cleaner import clean_chat


def get_multiline_input():
    print("\nPaste chat text. Type 'END' on a new line when finished:\n")
    lines = []

    while True:
        line = input()
        if line.strip().upper() == "END":
            break
        lines.append(line)

    return "\n".join(lines)


def main():
    print("=== GenAI Customer Support Quality Auditor ===\n")
    print("Modes:")
    print("1 → Chat Input")
    print("2 → Audio File\n")

    mode = input("Select mode (1/2): ").strip()

    try:
        if mode == "1":
            text = get_multiline_input()
            cleaned = clean_chat(text)

        elif mode == "2":
            file_path = input("Enter audio file path (e.g., data/calls/sample.mp3): ").strip()
            transcript = transcribe_audio(file_path)

            print("\nTranscript:\n")
            print(transcript)

            cleaned = clean_chat(transcript)

        else:
            print("Invalid mode selected.")
            return

        print("\nGenerating Quality Scores...\n")

        result = score_conversation(cleaned)

        print("=== Quality Evaluation ===\n")
        print(result)

    except Exception as e:
        print("\nError occurred:", str(e))


if __name__ == "__main__":
    main()