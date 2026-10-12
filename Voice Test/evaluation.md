# Metodologija ocenjevanja

## STT
Meri WER, CER, zakasnitev do prvega delnega prepisa in končnega prepisa ter po možnosti real-time factor. Posebej označi napake pri dvojini, šumnikih, imenih/krajih, številkah/datumih/času/denarju in strokovni terminologiji.

Ločeno testiraj čist govor, hrup, telefonski zvok, hitrejši govor ter različne govorce oziroma narečne vplive.

## TTS
Slepo ocenjevanje 1–5: naravnost (MOS), razumljivost, pravilnost izgovorjave, naglas/prozodija, številke/datumi/kratice/imena in primernost za daljši pogovor.

Tehnično meri time-to-first-audio, hitrost generiranja, streaming in stabilnost glasu.

## End-to-end voice agent
Meri: speech end → STT final → LLM first token → TTS first audio. Zabeleži interruption/barge-in, zaznavo konca govora in ponovitve.

## Slepa primerjava
Modele anonimiziraj kot A/B/C. Pri STT uporabi referenčni tekst in prepise. Pri TTS naj bo človeški MOS primarna ocena; LLM naj analizira strukturirane rezultate oziroma zvok samo, če ga dejansko prejme.

## Ponovljivost
Zabeleži model/version, datum, API/lokalno izvajanje, strojno opremo, kvantizacijo, nastavitve, format zvoka, sample rate in jezik.
