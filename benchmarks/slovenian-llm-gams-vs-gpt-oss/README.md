# Slovenian LLM Benchmark — GaMS vs GPT-OSS

Namen: slepa primerjava kakovosti modelov GaMS in GPT-OSS pri slovenščini ter poslovnih/IT nalogah.

## Protokol
- Obema modeloma pošlji popolnoma isti prompt in isti system prompt.
- Uporabi enake nastavitve (kolikor arhitektura dopušča); priporočilo: temperature 0 ali najnižja primerljiva vrednost.
- Ne popravljaj odgovorov.
- Shrani surove odgovore kot Model A in Model B. Ocenjevalcu ne razkrij identitete modelov.
- Če vprašanje zahteva aktualne informacije, modeloma ne omogoči spleta; s tem testiramo ravnanje z negotovostjo, ne spletnega iskanja.
- Vsak test zaženi vsaj enkrat; za bolj robusten rezultat 3 ponovitve pri generativnih nalogah.

## Kategorije
1–10 slovnica in oblikoslovje
11–20 semantika, idiomatika, prevod
21–30 poslovna in tehnična slovenščina
31–40 razumevanje, dvoumnost in sklepanje
41–50 zahtevnejše naloge, varnost pred halucinacijami in uporabnost

## Ocenjevanje
Vsak odgovor oceni 0–5 po:
1. jezikovna pravilnost,
2. naravnost slovenščine,
3. semantična pravilnost,
4. sledenje navodilom,
5. dejanska/logična pravilnost.

Pri nalogah, kjer kriterij ni relevanten, označi N/A. Poleg skupnega rezultata primerjaj rezultate po kategorijah.

## Slepi LLM-judge
V `judge-prompt.md` je predloga za neodvisno ocenjevanje z drugim modelom. Modela sta namenoma označena A/B, da zmanjšamo pristranskost zaradi imena modela.
