# Sprint 5 — Rapport de reprise et de validation du 6 septembre 2026

**SPRINT 5 READY FOR ACCEPTANCE: NO**

La validation automatique passe après correction des défauts constatés. Le test manuel des commandes, l'écoute et l'inspection visuelle dans Godot restent à effectuer. Ce rapport ne prononce ni l'acceptation du Sprint 5 ni le démarrage du Sprint 6.

## État Git repris

- Repository : `Enoranne/BO`.
- Branche de travail : `sprint-5`.
- HEAD reçu : `d1abe0a75698f21f08dcbf5d23646a0c66b8ceb3`.
- Base commune avec `sprint-4` : `41e0cfd8ec1682a7b056c343828094405911e42d`.
- Écart vérifié au démarrage et avant le commit de correction : **221 commits devant, 0 derrière `sprint-4`**.
- Arbre de travail Sprint 5 propre au démarrage. La branche complète a été ouverte dans un worktree distinct pour préserver le travail local préexistant sur Sprint 4.
- Le fetch de contrôle confirme que le HEAD distant reçu est inchangé. Le présent checkpoint ajoute les corrections et les preuves à cette base, sans réécriture de l'historique.

## 1. Résultats exacts

Commande exécutée depuis la racine du projet, avec Godot officiel `4.7.stable.official.5b4e0cb0f` :

```bash
GODOT_BIN=/workspace/scratch/7419187f4d74/godot-validation.tQeYiJ/Godot_v4.7-stable_linux.x86_64 bash tests/run_sprint5_validation.sh
```

Pour reproduire ailleurs, remplacer `GODOT_BIN` par le chemin du binaire Godot 4.7 installé.

Le cache `.godot` a été déplacé hors du projet avant cette exécution afin de vérifier l'import initial. Le script importe les ressources et les classes avant les contrats headless.

| Contrôle | Résultat final |
| --- | --- |
| Commande complète | Code de sortie **0**, aucune suite ignorée |
| Validations statiques | **23/23**, **1 221 assertions PASS**, 0 échec |
| Contrats Godot headless | **7/7**, **216 assertions PASS**, 0 échec |
| Diagnostics moteur | **0 ERROR, 0 SCRIPT ERROR, 0 WARNING** dans le journal final |
| Hygiène du diff | `git diff --check` : code de sortie 0 |

Les sept suites sont : Recorder, gameplay, visual contract, blocking, presentation, Sprint 5 scene contract et player input contract. Les deux dernières sont ajoutées par ce checkpoint.

Preuve complète : [validation.log](validation/2026-09-06/validation.log).

## 2. Erreurs constatées et corrections

| Défaut observé | Correction limitée |
| --- | --- |
| Le premier lancement s'arrête sur le contrôle anti-inventaire ; la règle existe avec une minuscule initiale. | Comparaison insensible à la casse dans le validateur. La règle de design reste intacte. |
| Le contrôle de l'interdiction d'implémenter ADR-001 ne reconnaît pas le gras Markdown. | Retrait des marqueurs de gras pour cette comparaison. L'interdiction reste intacte. |
| Sans cache, les tests headless ne reconnaissent pas les classes globales `Recorder` et `RecordableSource`. | Import éditeur headless au début de `run_headless.sh`. |
| L'import WAV émet 14 erreurs de lecture `p_position > length`. | Suppression des 120 octets parasites après le conteneur RIFF : 1 164 → 1 044 octets. Échantillons PCM et paramètres audio vérifiés identiques. Contrôle de longueur RIFF ajouté. |
| Trois tests terminent leurs assertions avec des ressources audio encore référencées à la fermeture. | Libération des scènes et références de test, puis délai de retrait des références audio avant fermeture. |
| `CharacterReadabilityPreview` charge, mais aucun des deux personnages ne construit sa géométrie. | Le garde de construction confondait les labels enfants avec une géométrie existante. Il recherche désormais les meshes et conserve les labels. |

Le lanceur vérifie désormais aussi les diagnostics moteur et la présence du message de fin des tests : un code de sortie 0 seul ne suffit plus.

Le WAV reste le son de test existant. Ses données PCM mono 16 bits, 100 Hz, 500 échantillons sont inchangées ; SHA-256 des échantillons : `9969c21ffcc25b1365d970985969943d522d270836b7ad3eadcc67d2080e24c5`.

Les fichiers UID et les paramètres d'import produits par Godot sont conservés avec le projet. La version déclarée du projet était déjà 4.7.

## 3. Captures et inspection réelle

**Aucune capture visuelle produite.** L'affichage natif X11/Wayland est indisponible et aucun outil Godot-MCP n'est exposé dans cette session. Godot fonctionne en headless.

Il n'y a donc pas de preuve visuelle de la lumière, des matériaux, des intersections, des objets flottants ou de la lisibilité depuis la caméra de jeu. Aucune amélioration visuelle par rapport au Sprint 4 n'est déclarée.

## 4. Player Feel

Quatre parcours utilisent des événements `InputEventKey` et `InputEventMouseButton` injectés par `Input.parse_input_event` :

| Scène | Commandes simulées |
| --- | --- |
| Canonique | Positions WASD, interaction E |
| Canonique | Positions WASD avec codes logiques AZERTY Z/Q, clic gauche |
| Visual Slice | Positions WASD, interaction E |
| Visual Slice | Positions WASD avec codes logiques AZERTY Z/Q, clic gauche |

Chaque parcours déplace Malo avec le contrôleur existant, contourne la table et utilise les recouvrements de proximité réels du moteur. Il ne téléporte pas Malo et ne force pas la source sonore sélectionnée.

Les quatre parcours passent : déplacement dans les quatre directions ; refus de REC avant le Fisher ; prise contextuelle ; apparition du Fisher porté ; détection de Ronan ; maintien de R ; lampe REC et état HUD ; refus de PLAY pendant REC ; relâchement de R ; création d'un unique clip Ronan ; Space PLAY ; retour naturel à STOP ; P PLAY ; arrêt par la collision du mur avant.

L'ordre `FIND_FISHER → RECORD_RONAN → PLAY_RECORDING → COMPLETE` est vérifié dans les deux scènes. **Il s'agit de couverture d'intégration moteur automatisée.** Le ressenti, le clavier physique, l'écoute et l'ergonomie réelle du clic restent à vérifier manuellement.

## 5. Visual Slice et personnages

Les deux scènes s'instancient. Le wrapper applique ses matériaux, son HUD, ses détails Fisher et son décor ; le décor ne se duplique pas lors d'une seconde application.

La comparaison structurelle vérifie les formes/couches/transforms des collisions du décor, les marqueurs de blocking et la position/FOV de caméra. Ces valeurs restent identiques entre les deux scènes. Cette comparaison ne remplace pas une comparaison d'images.

Après correction, `CharacterReadabilityPreview` construit Malo et Ronan avec leurs labels. Les statures configurées restent 1,45 m et 1,68 m. La différence d'âge perçue, les silhouettes et leur visibilité depuis la caméra de jeu ne sont pas approuvées.

## 6. Coffee-table

**NON ÉVALUÉE — décision KEEP / REJECT en attente.** L'étape exige une Visual Slice stable et inspectée. Aucun GLB récupéré ou importé pendant cette reprise, aucune nouvelle génération lancée. La révision 1 existante reste le seul candidat prévu. Son échelle devra être examinée explicitement, compte tenu de l'écart entre l'enveloppe actuelle et la table attendue.

## 7. Cyclops

**NON TESTÉ — aucune adoption, décision KEEP / DISCARD en attente.** Les étapes visuelle et coffee-table ne sont pas franchies. Aucun addon installé et aucune expansion du salon réalisée pendant cette reprise.

## 8. Blockers restants

- Accès à un éditeur/runtime Godot avec affichage et commandes manuelles ; connexion Godot-MCP si disponible.
- Test manuel et écoute de la boucle dans les deux scènes.
- Captures A/B au même cadre, inspection de la Visual Slice et de la lisibilité des personnages.
- Ensuite seulement : round-trip coffee-table et spike Cyclops selon leurs conditions d'entrée.

Aucun échec automatique restant dans les contrôles exécutés. Cela ne prouve pas l'absence de défauts de présentation.

## 9. Recommandations immédiates

Reprendre sur le HEAD `sprint-5` contenant ce rapport. Ouvrir d'abord `Christmas1982.tscn`, jouer la boucle et capturer A ; ouvrir ensuite `Christmas1982_VisualSlice.tscn`, refaire la boucle et capturer B au même cadre. Inspecter les lumières, le décor, le HUD et Malo/Ronan/Fisher, puis `CharacterReadabilityPreview.tscn`.

Corriger seulement les défauts observés. Si ces étapes passent, récupérer la révision 1 de la table dans sa scène isolée, décider KEEP / REJECT, puis exécuter le spike Cyclops et décider KEEP / DISCARD.

## 10. Verdict

**SPRINT 5 READY FOR ACCEPTANCE: NO**

Les contrôles automatiques passent et les défauts constatés sont corrigés. Les preuves manuelles et visuelles requises manquent encore. Les responsabilités du Recorder, d'InteractionContext, de MaloController et de la présentation sont conservées ; aucune mécanique du Sprint 6 n'a été implémentée.
