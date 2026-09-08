---
name: anti-ai
description: "Anti AI Slop"
---

# Skill Profile: Anti-AI Slop UI System

## Core Directive
Reject generic, template-looking UI design patterns. Do not generate purple/indigo gradients, floating pill cards with arbitrary rounded corners, or layouts that look like a generic SaaS landing page. Build layout frameworks tailored for high utility, structural clarity, and professional density.

## Layout & Information Hierarchy Principles
1. Structure is Information: Grid systems, dividers, alignment choices, and typographic weight must map to real database entity relationships. Never add random "01 / 02 / 03" numbering or decorative iconography unless the underlying data model dictates a sequence.
2. Density Matters: When building operational internal tools (like school portals or sports logs), optimize for information density over massive padding. Teachers and managers need to see data quickly, not scroll through vast white space.
3. Design for Subject Context: 
   - Educational/Staff Web Tools: Use professional, high-contrast typography, clean tabular structures, predictable navigation, and strict semantic borders. 
   - Athletic/Sports Graphics: Lean into strong, geometric angles, heavy uppercase sans-serif display type (e.g., Impact/Barlow Condensed styles), clean dark-mode contrast panels, and intentional, limited accent coloring.

## Technical Execution (React & Tailwind)
- Do not mix styling approaches. Stick entirely to native Tailwind classes or clean CSS variables mapping to a single layout theme.
- Ensure all components handle real PostgreSQL data mapping safely (e.g., proper null checks on optional Supabase table attributes).
- Component markup must remain dry, modular, and performant—prefer semantic HTML tags over nested, generic `<div>` stacks.