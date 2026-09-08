# BIE Canonical Architecture

## Product objective

The canonical BIE converts a source into a complete, source-grounded educational production while preserving provenance and supporting regeneration at concept, lesson, chapter, book, and course scale.

## Canonical layers

1. `ingestion` — PDF/EPUB/scan/structured-source intake and validation.
2. `document_intelligence` — page/layout-aware extraction, figures, tables, equations, structure.
3. `evidence` — provenance, retrieval, contradiction handling, verification.
4. `knowledge` — ontology, knowledge graph, terminology and relationships.
5. `learning` — prerequisites, dependencies, learning graph and coverage.
6. `pedagogy` — objectives, lesson architecture, teaching strategy and assessment alignment.
7. `script` — teaching script and narration plan.
8. `storyboard` — scene decomposition and visual representation planning.
9. `assets` — extraction, diagrams, charts, illustrations, reusable asset resolution and provenance.
10. `audio` — narration generation/import, measured timing, anchors and captions.
11. `scene_dsl` — deterministic intermediate representation for scenes.
12. `remotion` — component registry, code generation and project assembly.
13. `render` — render orchestration and artifact lifecycle.
14. `qa` — factual, pedagogical, visual, numerical, audio and provenance validation.
15. `repair` — targeted diagnosis, regeneration and re-render.
16. `course` — whole-book/course orchestration, cross-chapter memory, caching and incremental builds.
17. `platform` — persistence, workers, scheduling, eventing, security, policy and observability.

## Architectural rules

- Original source and evidence remain authoritative.
- Generated artifacts are derived, versioned and traceable.
- Domain modules do not call model vendors directly; provider adapters sit behind explicit interfaces.
- Audio duration is authoritative for narration-driven scene timing.
- A failed QA gate blocks publication and identifies the affected layer.
- Repair should rebuild only affected downstream artifacts when possible.
- Legacy M001-M200 packages are preserved until their capabilities are mapped and consolidated.
- Repeated infrastructure implementations are not copied blindly into the canonical runtime; one authoritative implementation is selected per concern after comparison.

## Acceptance path

```text
real source
 -> verified knowledge
 -> learning plan
 -> script
 -> storyboard
 -> assets + audio
 -> deterministic Remotion project
 -> render
 -> QA
 -> targeted repair if needed
 -> final MP4 + build/provenance manifest
```
