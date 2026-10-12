# Voice Test — Slovenian STT & TTS Benchmark

Ponovljiv primerjalni test govornih tehnologij za slovenski jezik.

## Namen
- primerjava Speech-to-Text (STT) modelov na istem slovenskem korpusu;
- primerjava Text-to-Speech (TTS) modelov z enakimi besedili;
- merjenje kakovosti, zakasnitve in primernosti za glasovne agente;
- omogočiti slepo primerjavo rezultatov z neodvisnim LLM ocenjevalcem.

## Struktura
- `stt/test-corpus.md` — 50 testnih izjav za STT
- `tts/test-corpus.md` — 50 testnih besedil za TTS
- `evaluation.md` — metrike, protokol in način ocenjevanja
- `results-template.csv` — skupna predloga rezultatov

## Priporočeni kandidati
STT: slovensko prilagojeni ASR modeli, Whisper, ElevenLabs Scribe in drugi ponudniki s slovenščino.
TTS: ElevenLabs in lokalni/odprti slovenski ali večjezični TTS modeli.

## Pravilo primerjave
Vsi modeli dobijo identičen vhod. Parametri, strojna oprema/API, čas testa in verzija modela se zabeležijo. Rezultati se pred ocenjevanjem anonimizirajo kot Model A, B, C ... .
